"""Dawson House Wiki — Conversation agent, exposed via a personal Telegram bot.

Run modes:
    python telegram_bot.py            # long-polling (recommended for personal use)

Required environment variables (see bot/.env.example):
    TELEGRAM_BOT_TOKEN       — from @BotFather
    TELEGRAM_ALLOWED_USER_IDS — comma-separated Telegram numeric user IDs allowed to chat
    LLM_MODEL                — optional, litellm "<provider>/<model>" string used by the
                                Conversation agent AND (by default) /research
                                (default: openai/gpt-4o-mini, or anthropic/<CLAUDE_MODEL>
                                if CLAUDE_MODEL is set and LLM_MODEL isn't). Whichever
                                *_API_KEY the provider needs (e.g. OPENAI_API_KEY,
                                ANTHROPIC_API_KEY) should also be set — but it's
                                soft-required: if missing, the bot still starts, and
                                chat/research just reply that they aren't configured
                                yet (see _ensure_model_api_key).
    RESEARCH_LLM_MODEL       — optional, overrides the model used by /research only
                                (default: same as LLM_MODEL).
    CLAUDE_MODEL             — optional, legacy. If set (and LLM_MODEL is unset),
                                LLM_MODEL defaults to anthropic/<CLAUDE_MODEL> instead
                                of openai/gpt-4o-mini.
    TAVILY_API_KEY           — required for /research's web_search tool
                                (https://tavily.com), regardless of LLM_MODEL.
                                Also soft-required, same as above.
    DAILY_REVIEW_HOUR        — optional, hour (0-23, WIKI_TZ) at which the daily
                                clarification review runs (default: 21, i.e. 9pm).
    DAILY_REVIEW_MAX_QUESTIONS — optional, max clarifying questions asked per day
                                (default: 3).
    WIKI_TZ                  — optional, IANA timezone for /note timestamps and
                                the daily review schedule (default: Asia/Singapore).

GCP Secret Manager (optional, used for deployment — see bot/gcp/):
    If GCP_PROJECT_ID is set and a required *_API_KEY / TELEGRAM_BOT_TOKEN is NOT
    present in the environment, it's fetched from Secret Manager (secret ID ==
    variable name, "latest" version) using the host's Application Default
    Credentials. Locally this is never triggered — bot/.env supplies values
    directly. See bot/gcp/setup-secrets.sh.

Design notes:
    - Read-only Conversation agent: answers questions from the compiled wiki
      (Dawson's wiki/wiki/**). Never writes to the wiki directly (per
      system/agents/conversation.md and write-safety.md).
    - Both the Conversation agent and /research are model-agnostic via
      LLM_MODEL / RESEARCH_LLM_MODEL (see llm_client.py and research_agent.py,
      both backed by litellm) — e.g. set LLM_MODEL=openai/gpt-4o-mini +
      OPENAI_API_KEY to use ChatGPT instead of Claude. /research's web search
      is a client-side tool backed by the Tavily Search API (TAVILY_API_KEY),
      not a provider-native server tool, so it works the same regardless of
      which LLM is configured.
    - /research is a separate, narrowly-scoped Research agent (research_agent.py)
      that DOES write to the wiki — but only new notes under
      Dawson's wiki/wiki/Research/**, never Rooms/Vendors/Tasks/Decisions (see
      system/agents/research.md and write-safety.md).
    - Wiki content is loaded fresh on every message (cheap — small vault) so
      edits made via the Compiler are reflected immediately without restarting
      the bot. Use /refresh to force-reload if you ever cache this.
    - Per-chat conversation history is kept in memory only (lost on restart) —
      fine for a personal assistant; no persistence layer needed for v1.
    - Access is restricted to TELEGRAM_ALLOWED_USER_IDS — anyone else messaging
      the bot gets a polite refusal. This matters because the wiki contains
      personal financial/renovation data.
    - /note <text> and photo messages are quick-capture: they append a
      timestamped entry to Dawson's wiki/inbox/{date} telegram capture.md
      (and save any photo under Dawson's wiki/zz_images/), via capture.py.
      Same write-safety as the user's own manual inbox notes — never touches
      the compiled wiki (see system/agents/capture.md).
    - Once a day (DAILY_REVIEW_HOUR), daily_review.py asks the configured LLM
      to find up to DAILY_REVIEW_MAX_QUESTIONS ambiguous points in that day's
      capture file (incl. any photos, via vision) and asks the user via
      Telegram inline-keyboard multiple choice. Answers are appended to the
      capture file as a "## Clarifications" section for the Extractor to pick
      up later. Soft-required like chat/research: silently skipped if the LLM
      key isn't configured.
"""

from __future__ import annotations

import logging
import os
import re
import sys
from datetime import time as dt_time

from dotenv import load_dotenv

from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

import capture
import daily_review
import llm_client
import research_agent
from wiki_context import build_system_prompt

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("dawson-wiki-bot")

DEFAULT_LLM_MODEL = "openai/gpt-4o-mini"  # used if neither LLM_MODEL nor CLAUDE_MODEL is set
MAX_HISTORY_TURNS = 12  # user+assistant pairs kept per chat, to bound context growth
TELEGRAM_MAX_MESSAGE_LEN = 4096

# chat_id -> list of {"role": "user"|"assistant", "content": str}
conversation_history: dict[int, list[dict[str, str]]] = {}


def _secret_from_manager(project_id: str, secret_id: str) -> str | None:
    """Fetch the latest version of `secret_id` from GCP Secret Manager.

    Lazily imports google-cloud-secret-manager so local runs (which never set
    GCP_PROJECT_ID) don't require the dependency to be installed.
    """
    try:
        from google.cloud import secretmanager
    except ImportError:
        logger.error(
            "GCP_PROJECT_ID is set but google-cloud-secret-manager isn't installed "
            "(it's in requirements.txt — re-run bot/run.sh)."
        )
        return None

    try:
        client = secretmanager.SecretManagerServiceClient()
        name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
        response = client.access_secret_version(name=name)
        return response.payload.data.decode("utf-8").strip()
    except Exception:
        logger.exception("Failed to fetch secret '%s' from Secret Manager", secret_id)
        return None


def _config_value(name: str, project_id: str | None) -> str | None:
    """Env var (incl. bot/.env) first; GCP Secret Manager fallback if configured."""
    value = os.environ.get(name)
    if value:
        return value
    if project_id:
        return _secret_from_manager(project_id, name)
    return None


def _ensure_model_api_key(model: str, project_id: str | None) -> str | None:
    """Best-effort: ensure the *_API_KEY needed by `model` is in os.environ
    (incl. Secret Manager fallback).

    Soft-required, like TAVILY_API_KEY: returns the missing env var name if
    it couldn't be found (so the bot still starts and chat/research can reply
    "not configured yet" at runtime), or None if the key is present.
    """
    provider = llm_client.provider_of(model)
    key_env_var = llm_client.api_key_env_var(provider)
    api_key = _config_value(key_env_var, project_id)
    if api_key:
        os.environ[key_env_var] = api_key  # ensure litellm sees it (e.g. when from Secret Manager)
        return None
    logger.warning(
        "%s is not set — model '%s' is unavailable until it's configured "
        "(see bot/.env.example or bot/gcp/setup-secrets.sh).",
        key_env_var,
        model,
    )
    return key_env_var


def _load_config() -> dict:
    load_dotenv()  # loads bot/.env if present, falls back to process env

    project_id = os.environ.get("GCP_PROJECT_ID")  # set on the GCP VM only

    token = _config_value("TELEGRAM_BOT_TOKEN", project_id)
    if not token:
        sys.exit("TELEGRAM_BOT_TOKEN is not set (see bot/.env.example or bot/gcp/setup-secrets.sh)")

    # LLM_MODEL is a litellm "<provider>/<model>" string, used by both the
    # Conversation agent and (by default) /research. CLAUDE_MODEL is a legacy
    # override (anthropic/<CLAUDE_MODEL>) for configs that predate LLM_MODEL;
    # if neither is set, default to DEFAULT_LLM_MODEL.
    if os.environ.get("LLM_MODEL"):
        llm_model = os.environ["LLM_MODEL"]
    elif os.environ.get("CLAUDE_MODEL"):
        llm_model = f"anthropic/{os.environ['CLAUDE_MODEL']}"
    else:
        llm_model = DEFAULT_LLM_MODEL
    research_llm_model = os.environ.get("RESEARCH_LLM_MODEL", llm_model)

    # Ensure the right *_API_KEY is set (incl. Secret Manager fallback) for
    # each model in use. Soft-required (see _ensure_model_api_key) — missing
    # keys disable chat/research at runtime rather than crashing the bot.
    missing_llm_key = _ensure_model_api_key(llm_model, project_id)
    if research_llm_model == llm_model:
        missing_research_key = missing_llm_key
    else:
        missing_research_key = _ensure_model_api_key(research_llm_model, project_id)

    # /research's web_search tool is backed by Tavily, independent of LLM_MODEL.
    # Soft-required: don't crash the whole bot if it's missing — /research
    # just replies that it isn't configured yet (see research_command).
    tavily_key = _config_value("TAVILY_API_KEY", project_id)
    if tavily_key:
        os.environ["TAVILY_API_KEY"] = tavily_key
    else:
        logger.warning(
            "TAVILY_API_KEY is not set — /research is disabled until it's "
            "configured (see bot/.env.example or bot/gcp/setup-secrets.sh)."
        )

    allowed_raw = os.environ.get("TELEGRAM_ALLOWED_USER_IDS", "")
    allowed_ids = {
        int(x.strip()) for x in allowed_raw.split(",") if x.strip().isdigit()
    }
    if not allowed_ids:
        logger.warning(
            "TELEGRAM_ALLOWED_USER_IDS is empty — the bot will refuse ALL users. "
            "Set it to your Telegram numeric user ID (get it from @userinfobot)."
        )

    daily_review_hour = int(os.environ.get("DAILY_REVIEW_HOUR", "21"))
    daily_review_max_questions = int(os.environ.get("DAILY_REVIEW_MAX_QUESTIONS", "3"))

    return {
        "telegram_token": token,
        "llm_model": llm_model,
        "research_llm_model": research_llm_model,
        "missing_llm_key": missing_llm_key,
        "missing_research_key": missing_research_key,
        "allowed_user_ids": allowed_ids,
        "daily_review_hour": daily_review_hour,
        "daily_review_max_questions": daily_review_max_questions,
    }


CONFIG = _load_config()


def _is_allowed(user_id: int) -> bool:
    return user_id in CONFIG["allowed_user_ids"]


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    if not user or not _is_allowed(user.id):
        await update.message.reply_text(
            "Sorry, this bot is private. Ask the owner to add your Telegram user ID "
            "to TELEGRAM_ALLOWED_USER_IDS."
        )
        return

    await update.message.reply_text(
        "Hi! I'm the Dawson House Wiki assistant.\n\n"
        "Ask me anything about the renovation — rooms, items, vendors, tasks, "
        "decisions, budget, statuses. I read from the compiled wiki and won't "
        "make changes myself; if you ask for an update, I'll explain what should "
        "go through the review queue + compile step.\n\n"
        "Commands:\n"
        "/note <text> — quick-capture a note for later (e.g. \"/note Senso "
        "Studio quoted $4200 for kitchen cabinets\") — saved to today's inbox "
        "capture file\n"
        "Send a photo (with optional caption) — also quick-captured, saved "
        "under zz_images/ and linked from today's capture file\n"
        "/research <description> — search the web for alternatives (e.g. "
        "\"/research extendable dining table, ~180x90cm, dark wood, under $1500 "
        "SGD, for the Living-Dining room\") and save a comparison note to the wiki\n"
        "/reset — clear this chat's conversation memory\n"
        "/help — show this message again\n\n"
        f"Each evening (around {CONFIG['daily_review_hour']:02d}:00 "
        f"{capture.WIKI_TZ}), I'll ask up to "
        f"{CONFIG['daily_review_max_questions']} quick multiple-choice questions "
        "about anything unclear in that day's notes."
    )


async def reset_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    if not user or not _is_allowed(user.id):
        return
    chat_id = update.effective_chat.id
    conversation_history.pop(chat_id, None)
    await update.message.reply_text("Conversation memory cleared.")


async def note_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    message = update.message
    if not user or not message:
        return

    if not _is_allowed(user.id):
        logger.warning("Rejected /note from unauthorized user_id=%s", user.id)
        await message.reply_text(
            "Sorry, this bot is private and not configured for your account."
        )
        return

    text = re.sub(r"^/note(@\w+)?\s*", "", message.text or "", count=1).strip()
    if not text:
        await message.reply_text(
            "Usage: /note <text>\n\n"
            "Example: /note Senso Studio quoted $4200 for kitchen cabinets"
        )
        return

    path = capture.append_entry(text)
    rel_path = path.relative_to(capture.REPO_ROOT)
    await message.reply_text(f"Saved to {rel_path}")


async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    message = update.message
    if not user or not message or not message.photo:
        return

    if not _is_allowed(user.id):
        logger.warning("Rejected photo from unauthorized user_id=%s", user.id)
        await message.reply_text(
            "Sorry, this bot is private and not configured for your account."
        )
        return

    capture.IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    filename = capture.save_photo_filename()
    photo_file = await context.bot.get_file(message.photo[-1].file_id)
    await photo_file.download_to_drive(custom_path=capture.IMAGES_DIR / filename)

    caption = (message.caption or "").strip()
    path = capture.append_entry(caption, image_filename=filename)
    rel_path = path.relative_to(capture.REPO_ROOT)
    await message.reply_text(f"Saved photo to {rel_path}")


async def research_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    message = update.message
    if not user or not message:
        return

    if not _is_allowed(user.id):
        logger.warning("Rejected /research from unauthorized user_id=%s", user.id)
        await message.reply_text(
            "Sorry, this bot is private and not configured for your account."
        )
        return

    if not os.environ.get("TAVILY_API_KEY"):
        await message.reply_text(
            "/research isn't configured yet — TAVILY_API_KEY is missing. "
            "Add a Tavily API key (https://tavily.com) to enable it."
        )
        return

    if CONFIG["missing_research_key"]:
        await message.reply_text(
            f"/research isn't configured yet — {CONFIG['missing_research_key']} is "
            f"missing for model {CONFIG['research_llm_model']}. Ask the owner to add it."
        )
        return

    # Everything after "/research" (and an optional "@botname")
    query = re.sub(r"^/research(@\w+)?\s*", "", message.text or "", count=1).strip()
    if not query:
        await message.reply_text(
            "Usage: /research <description>\n\n"
            "Example: /research extendable dining table, ~180x90cm, dark wood, "
            "under $1500 SGD, for the Living-Dining room"
        )
        return

    chat_id = update.effective_chat.id
    await context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
    await message.reply_text("Researching alternatives — this can take ~30-60s...")

    try:
        result = research_agent.run_research(query, CONFIG["research_llm_model"])
        path = research_agent.save_research_note(
            result["title"], result["room"], result["note_markdown"]
        )
    except Exception:  # noqa: BLE001 - want to report any failure to the user
        logger.exception("Research agent failed")
        await message.reply_text(
            "Sorry, the research agent ran into an error. Please try again."
        )
        return

    rel_path = path.relative_to(research_agent.REPO_ROOT)
    reply_text = f"{result['summary']}\n\nSaved to: {rel_path}"

    for i in range(0, len(reply_text), TELEGRAM_MAX_MESSAGE_LEN):
        await message.reply_text(reply_text[i : i + TELEGRAM_MAX_MESSAGE_LEN])


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    message = update.message

    if not user or not message or not message.text:
        return

    if not _is_allowed(user.id):
        logger.warning("Rejected message from unauthorized user_id=%s", user.id)
        await message.reply_text(
            "Sorry, this bot is private and not configured for your account."
        )
        return

    chat_id = update.effective_chat.id
    user_text = message.text.strip()
    if not user_text:
        return

    # If a daily-review question is awaiting a free-text ("Other") answer,
    # consume this message as that answer instead of normal chat.
    if await daily_review.handle_free_text_answer(update, context):
        return

    if CONFIG["missing_llm_key"]:
        await message.reply_text(
            f"Chat isn't configured yet — {CONFIG['missing_llm_key']} is missing "
            f"for model {CONFIG['llm_model']}. Ask the owner to add it."
        )
        return

    history = conversation_history.setdefault(chat_id, [])
    history.append({"role": "user", "content": user_text})
    # bound history length (keep most recent N turns = 2*N messages)
    if len(history) > MAX_HISTORY_TURNS * 2:
        del history[: len(history) - MAX_HISTORY_TURNS * 2]

    await context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)

    try:
        system_prompt = build_system_prompt()
        reply_text = llm_client.chat_completion(
            model=CONFIG["llm_model"],
            system=system_prompt,
            messages=history,
            max_tokens=1500,
        )
    except Exception:  # noqa: BLE001 - want to report any failure to the user
        logger.exception("LLM call failed")
        await message.reply_text(
            "Sorry, something went wrong talking to the AI model. Please try again."
        )
        # don't keep a broken turn in history
        history.pop()
        return

    if not reply_text:
        reply_text = "(no response)"

    history.append({"role": "assistant", "content": reply_text})

    # Telegram messages are capped at 4096 chars — split if needed
    for i in range(0, len(reply_text), TELEGRAM_MAX_MESSAGE_LEN):
        await message.reply_text(reply_text[i : i + TELEGRAM_MAX_MESSAGE_LEN])


def main() -> None:
    app = Application.builder().token(CONFIG["telegram_token"]).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", start_command))
    app.add_handler(CommandHandler("reset", reset_command))
    app.add_handler(CommandHandler("research", research_command))
    app.add_handler(CommandHandler("note", note_command))
    app.add_handler(MessageHandler(filters.PHOTO, photo_handler))
    app.add_handler(
        CallbackQueryHandler(
            daily_review.callback_handler,
            pattern=rf"^{daily_review.CALLBACK_PREFIX}\|",
        )
    )
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    if app.job_queue is not None:
        app.job_queue.run_daily(
            daily_review.daily_review_job,
            time=dt_time(hour=CONFIG["daily_review_hour"], minute=0, tzinfo=capture.WIKI_TZ),
            data={
                "llm_model": CONFIG["llm_model"],
                "missing_llm_key": CONFIG["missing_llm_key"],
                "max_questions": CONFIG["daily_review_max_questions"],
                "allowed_user_ids": CONFIG["allowed_user_ids"],
            },
        )
    else:
        logger.warning(
            "JobQueue is unavailable (install python-telegram-bot[job-queue]) — "
            "the daily clarification review is disabled."
        )

    logger.info(
        "Starting Dawson House Wiki Telegram bot (llm_model=%s%s, research_llm_model=%s%s, "
        "allowed_users=%s, daily_review=%02d:00 %s)",
        CONFIG["llm_model"],
        " [NOT CONFIGURED]" if CONFIG["missing_llm_key"] else "",
        CONFIG["research_llm_model"],
        " [NOT CONFIGURED]" if CONFIG["missing_research_key"] else "",
        sorted(CONFIG["allowed_user_ids"]) or "NONE",
        CONFIG["daily_review_hour"],
        capture.WIKI_TZ,
    )
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
