"""Dawson House Wiki — Conversation agent, exposed via a personal Telegram bot.

Run modes:
    python telegram_bot.py            # long-polling (recommended for personal use)

Required environment variables (see bot/.env.example):
    TELEGRAM_BOT_TOKEN       — from @BotFather
    TELEGRAM_ALLOWED_USER_IDS — comma-separated Telegram numeric user IDs allowed to chat
    ANTHROPIC_API_KEY        — Claude API key
    CLAUDE_MODEL             — optional, defaults to claude-sonnet-4-6

GCP Secret Manager (optional, used for deployment — see bot/gcp/):
    If GCP_PROJECT_ID is set and TELEGRAM_BOT_TOKEN / ANTHROPIC_API_KEY are NOT
    present in the environment, they're fetched from Secret Manager (secret ID
    == variable name, "latest" version) using the host's Application Default
    Credentials. Locally this is never triggered — bot/.env supplies both
    values directly. See bot/gcp/setup-secrets.sh.

Design notes:
    - Read-only Conversation agent: answers questions from the compiled wiki
      (Dawson's wiki/wiki/**). Never writes to the wiki directly (per
      system/agents/conversation.md and write-safety.md).
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
import sys

from dotenv import load_dotenv

import anthropic
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from wiki_context import build_system_prompt

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("dawson-wiki-bot")

DEFAULT_MODEL = "claude-sonnet-4-6"
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

    api_key = _config_value("ANTHROPIC_API_KEY", project_id)
    if not api_key:
        sys.exit("ANTHROPIC_API_KEY is not set (see bot/.env.example or bot/gcp/setup-secrets.sh)")

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
        "anthropic_api_key": api_key,
        "model": os.environ.get("CLAUDE_MODEL", DEFAULT_MODEL),
        "allowed_user_ids": allowed_ids,
    }


CONFIG = _load_config()
CLAUDE = anthropic.Anthropic(api_key=CONFIG["anthropic_api_key"])


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
        response = CLAUDE.messages.create(
            model=CONFIG["model"],
            max_tokens=1500,
            system=system_prompt,
            messages=history,
        )
        reply_text = "".join(
            block.text for block in response.content if block.type == "text"
        ).strip()
    except Exception:  # noqa: BLE001 - want to report any failure to the user
        logger.exception("Claude API call failed")
        await message.reply_text(
            "Sorry, something went wrong talking to Claude. Please try again."
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
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info(
        "Starting Dawson House Wiki Telegram bot (model=%s, allowed_users=%s)",
        CONFIG["model"],
        sorted(CONFIG["allowed_user_ids"]) or "NONE",
    )
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
