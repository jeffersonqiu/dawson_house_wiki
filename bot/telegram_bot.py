"""Dawson House Wiki — Conversation agent, exposed via a personal Telegram bot.

Run modes:
    python telegram_bot.py            # long-polling (recommended for personal use)

Required environment variables (see bot/.env.example):
    TELEGRAM_BOT_TOKEN       — from @BotFather
    TELEGRAM_ALLOWED_USER_IDS — comma-separated Telegram numeric user IDs allowed to chat
    LLM_MODEL                — optional, litellm "<provider>/<model>" string used by the
                                Conversation agent AND (by default) /research
                                (default: anthropic/<CLAUDE_MODEL>). Whichever
                                *_API_KEY the provider needs (e.g. ANTHROPIC_API_KEY,
                                OPENAI_API_KEY) must also be set.
    RESEARCH_LLM_MODEL       — optional, overrides the model used by /research only
                                (default: same as LLM_MODEL).
    CLAUDE_MODEL             — optional, legacy. Used as the default model for
                                LLM_MODEL if LLM_MODEL is unset (default: claude-sonnet-4-6).
    TAVILY_API_KEY           — required for /research's web_search tool
                                (https://tavily.com), regardless of LLM_MODEL.

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
"""

from __future__ import annotations

import logging
import os
import re
import sys

from dotenv import load_dotenv

from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

import llm_client
import research_agent
from wiki_context import build_system_prompt

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("dawson-wiki-bot")

DEFAULT_CLAUDE_MODEL = "claude-sonnet-4-6"
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


def _load_config() -> dict:
    load_dotenv()  # loads bot/.env if present, falls back to process env

    project_id = os.environ.get("GCP_PROJECT_ID")  # set on the GCP VM only

    token = _config_value("TELEGRAM_BOT_TOKEN", project_id)
    if not token:
        sys.exit("TELEGRAM_BOT_TOKEN is not set (see bot/.env.example or bot/gcp/setup-secrets.sh)")

    # LLM_MODEL is a litellm "<provider>/<model>" string, used by both the
    # Conversation agent and (by default) /research. Default to Anthropic via
    # the (legacy) CLAUDE_MODEL/default, so existing configs behave exactly as
    # before unless LLM_MODEL is set.
    claude_model = os.environ.get("CLAUDE_MODEL", DEFAULT_CLAUDE_MODEL)
    llm_model = os.environ.get("LLM_MODEL", f"anthropic/{claude_model}")
    research_llm_model = os.environ.get("RESEARCH_LLM_MODEL", llm_model)

    # Ensure the right *_API_KEY is set (incl. Secret Manager fallback) for
    # every provider in use across both models.
    for model in {llm_model, research_llm_model}:
        provider = llm_client.provider_of(model)
        key_env_var = llm_client.api_key_env_var(provider)
        api_key = _config_value(key_env_var, project_id)
        if not api_key:
            sys.exit(
                f"{key_env_var} is not set, required for model {model} "
                "(see bot/.env.example or bot/gcp/setup-secrets.sh)"
            )
        os.environ[key_env_var] = api_key  # ensure litellm sees it (e.g. when from Secret Manager)

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

    return {
        "telegram_token": token,
        "llm_model": llm_model,
        "research_llm_model": research_llm_model,
        "allowed_user_ids": allowed_ids,
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
        "/research <description> — search the web for alternatives (e.g. "
        "\"/research extendable dining table, ~180x90cm, dark wood, under $1500 "
        "SGD, for the Living-Dining room\") and save a comparison note to the wiki\n"
        "/reset — clear this chat's conversation memory\n"
        "/help — show this message again"
    )


async def reset_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    if not user or not _is_allowed(user.id):
        return
    chat_id = update.effective_chat.id
    conversation_history.pop(chat_id, None)
    await update.message.reply_text("Conversation memory cleared.")


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
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info(
        "Starting Dawson House Wiki Telegram bot (llm_model=%s, research_llm_model=%s, allowed_users=%s)",
        CONFIG["llm_model"],
        CONFIG["research_llm_model"],
        sorted(CONFIG["allowed_user_ids"]) or "NONE",
    )
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
