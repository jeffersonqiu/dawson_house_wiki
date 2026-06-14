"""Dawson House Wiki — Capture agent, exposed via a personal Telegram bot.

This is a SEPARATE bot from telegram_bot.py (Conversation agent + /research),
on its own token (CAPTURE_BOT_TOKEN). It exists purely for quick-capture —
/note and photo messages — plus the end-of-day clarification review. Keeping
it separate means a photo sent to the *other* bot for discussion (e.g. "why
doesn't this match my spec?") is never mistaken for data to file away; only
photos sent HERE are captured. See system/agents/capture.md.

Run modes:
    python capture_bot.py             # long-polling (recommended for personal use)

Required environment variables (see bot/.env.example):
    CAPTURE_BOT_TOKEN        — from @BotFather (a second, separate bot)
    TELEGRAM_ALLOWED_USER_IDS — comma-separated Telegram numeric user IDs allowed to
                                use this bot (same list as telegram_bot.py)
    LLM_MODEL                — optional, litellm "<provider>/<model>" string used by
                                the end-of-day clarification review (vision-capable;
                                default: openai/gpt-4o-mini, or anthropic/<CLAUDE_MODEL>
                                if CLAUDE_MODEL is set and LLM_MODEL isn't). Soft-required:
                                if the matching *_API_KEY is missing, the daily review is
                                silently skipped — /note and photo capture still work.
    CLAUDE_MODEL             — optional, legacy. See telegram_bot.py.
    DAILY_REVIEW_HOUR        — optional, hour (0-23, WIKI_TZ) at which the daily
                                clarification review runs (default: 21, i.e. 9pm).
    DAILY_REVIEW_MAX_QUESTIONS — optional, max clarifying questions asked per day
                                (default: 3).
    WIKI_TZ                  — optional, IANA timezone for /note timestamps and the
                                daily review schedule (default: Asia/Singapore).

GCP Secret Manager (optional, used for deployment — see bot/gcp/):
    Same as telegram_bot.py — CAPTURE_BOT_TOKEN and the LLM_MODEL's *_API_KEY are
    fetched from Secret Manager (secret ID == variable name) if GCP_PROJECT_ID is
    set and the value isn't already in the environment.

Design notes:
    - /note <text> and photo messages append a timestamped entry to
      Dawson's wiki/inbox/{date} telegram capture.md (and save any photo under
      Dawson's wiki/zz_images/), via capture.py. Same write-safety as the
      user's own manual inbox notes — never touches the compiled wiki.
    - Once a day (DAILY_REVIEW_HOUR), daily_review.py asks the configured LLM
      to find up to DAILY_REVIEW_MAX_QUESTIONS ambiguous points in that day's
      capture file (incl. any photos, via vision) and asks the user via
      Telegram inline-keyboard multiple choice. Answers are appended to the
      capture file as a "## Clarifications" section for the Extractor to pick
      up later.
    - Same access control as telegram_bot.py (TELEGRAM_ALLOWED_USER_IDS).
"""

from __future__ import annotations

import logging
import os
import re
import sys
from datetime import time as dt_time

from dotenv import load_dotenv

from telegram import Update
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
from botconfig import config_value, ensure_model_api_key, load_allowed_user_ids, resolve_llm_model

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("dawson-wiki-bot.capture")

DEFAULT_LLM_MODEL = "openai/gpt-4o-mini"


def _load_config() -> dict:
    load_dotenv()  # loads bot/.env if present, falls back to process env

    project_id = os.environ.get("GCP_PROJECT_ID")  # set on the GCP VM only

    token = config_value("CAPTURE_BOT_TOKEN", project_id)
    if not token:
        sys.exit("CAPTURE_BOT_TOKEN is not set (see bot/.env.example or bot/gcp/setup-secrets.sh)")

    llm_model = resolve_llm_model(DEFAULT_LLM_MODEL)
    missing_llm_key = ensure_model_api_key(llm_model, project_id)

    allowed_ids = load_allowed_user_ids()

    daily_review_hour = int(os.environ.get("DAILY_REVIEW_HOUR", "21"))
    daily_review_max_questions = int(os.environ.get("DAILY_REVIEW_MAX_QUESTIONS", "3"))

    return {
        "telegram_token": token,
        "llm_model": llm_model,
        "missing_llm_key": missing_llm_key,
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
        "Hi! I'm the Dawson House Wiki capture bot.\n\n"
        "Send me things to remember for later — I don't chat, that's the other bot.\n\n"
        "/note <text> — quick-capture a note (e.g. \"/note Senso Studio quoted $4200 "
        "for kitchen cabinets\") — saved to today's inbox capture file\n"
        "Send a photo (with optional caption) — saved under zz_images/ and linked "
        "from today's capture file\n"
        "/reset — clear any in-progress end-of-day review\n"
        "/help — show this message again\n\n"
        f"Each evening (around {CONFIG['daily_review_hour']:02d}:00 {capture.WIKI_TZ}), "
        f"if you captured anything that day, I'll ask up to "
        f"{CONFIG['daily_review_max_questions']} quick multiple-choice questions about "
        "anything unclear."
    )


async def reset_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    if not user or not _is_allowed(user.id):
        return
    chat_id = update.effective_chat.id
    daily_review.pending_reviews.pop(chat_id, None)
    await update.message.reply_text("Any in-progress end-of-day review has been cleared.")


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


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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

    # If a daily-review question is awaiting a free-text ("Other") answer,
    # consume this message as that answer.
    if await daily_review.handle_free_text_answer(update, context):
        return

    await message.reply_text(
        "I only handle /note <text>, photos, and end-of-day review answers. "
        "For chat/research, message the other bot."
    )


def main() -> None:
    app = Application.builder().token(CONFIG["telegram_token"]).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", start_command))
    app.add_handler(CommandHandler("reset", reset_command))
    app.add_handler(CommandHandler("note", note_command))
    app.add_handler(MessageHandler(filters.PHOTO, photo_handler))
    app.add_handler(
        CallbackQueryHandler(
            daily_review.callback_handler,
            pattern=rf"^{daily_review.CALLBACK_PREFIX}\|",
        )
    )
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

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
        "Starting Dawson House Wiki Capture bot (llm_model=%s%s, allowed_users=%s, "
        "daily_review=%02d:00 %s)",
        CONFIG["llm_model"],
        " [NOT CONFIGURED]" if CONFIG["missing_llm_key"] else "",
        sorted(CONFIG["allowed_user_ids"]) or "NONE",
        CONFIG["daily_review_hour"],
        capture.WIKI_TZ,
    )
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
