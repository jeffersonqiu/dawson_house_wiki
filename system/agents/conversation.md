# Conversation Agent

**Status:** implemented (v1) — two access points:
1. In Claude Code, via `/ask-wiki` (`.claude/commands/ask-wiki.md`)
2. Standalone Telegram bot — `bot/telegram_bot.py` (see `bot/README.md` for setup)

## Purpose

Answer renovation questions from the compiled wiki; trigger pipeline steps on request.

## Inputs

- `Dawson's wiki/wiki/**`
- `system/constitution/*`
- Optional: `raw/`, `inbox/` for context

## Outputs

- Chat responses (read-only by default)
- Pipeline triggers → Ingestion / Extractor / Compiler
- Write proposals → `system/review_queue/`

## May write

- `system/review_queue/**`
- `system/runs/**`

## Must not

- Write compiled wiki without user approval
- Auto-run ingestion against Google APIs (not built)
- Write `system/constitution/`, `agents/`, `prompts/`, `schemas/` (Harness only)

## Implementation notes (Telegram bot, v1)

- **Why Telegram (not WhatsApp):** Telegram Bot API requires no business verification —
  a bot token is issued instantly via @BotFather, the API is free, and
  `python-telegram-bot` is a mature library. WhatsApp Business API requires Meta
  business verification (2-14 day approval), message-template approval, and
  per-conversation costs — overkill for a personal assistant. Revisit only if
  WhatsApp's ubiquity becomes a hard requirement.
- **Read-only by design:** the bot loads the entire compiled wiki as context on every
  message and answers from it. It explicitly does NOT write to `Dawson's wiki/wiki/` or
  `system/review_queue/` — those still require a Claude Code session
  (`/extract`, `/compile`, or asking Claude Code to add a review-queue proposal).
  This keeps the hard approval gate in `write-safety.md` intact: the bot can describe
  what a proposed change would look like, but cannot make it.
- **Access control:** restricted via `TELEGRAM_ALLOWED_USER_IDS` (numeric Telegram user
  IDs) — the wiki contains personal financial data, so the bot refuses anyone not on
  this list.
- **No persistence:** per-chat conversation history is in-memory only, lost on restart.
  Acceptable for a personal Q&A assistant; revisit if multi-day conversation continuity
  becomes important.
