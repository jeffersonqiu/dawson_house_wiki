# Capture Agent

**Status:** implemented (v1) — a SEPARATE Telegram bot from the Conversation
agent, with its own bot token (`CAPTURE_BOT_TOKEN`), exposing `/note` + photo
messages, plus an end-of-day clarification review (`bot/capture_bot.py` +
`bot/capture.py` + `bot/daily_review.py`; see `bot/README.md`).

## Purpose

Let the user quickly drop raw notes and photos collected throughout the day
(prices overheard, items spotted, photos of materials/quotes) into the wiki's
inbox via Telegram, in the same format as the user's own manual inbox notes —
then, once a day, ask up to a few short clarifying questions about anything
ambiguous before the Extractor picks the day's notes up.

## Why a separate bot

This agent runs as its own Telegram bot, distinct from the Conversation agent
(`bot/telegram_bot.py`, `system/agents/conversation.md`). A photo sent to the
Conversation bot purely for discussion (e.g. "why doesn't this match my
spec?") must never be mistaken for data to file away — and a single bot can't
reliably distinguish those intents from a photo message alone. Splitting by
bot makes the user's intent explicit: only photos/notes sent to the Capture
bot are captured. Both bots share `TELEGRAM_ALLOWED_USER_IDS` and the
underlying `capture.py`/`daily_review.py` modules.

## Inputs

- `/note <text>` and photo messages (with optional caption) via Telegram
- `Dawson's wiki/wiki/Rooms/*`, `Dawson's wiki/wiki/Vendors/*` — used to ground
  multiple-choice options in the daily review (existing room/vendor names)
- The day's own capture file, plus any attached photos (read by the daily
  review's vision-capable LLM call)

## Outputs

- `Dawson's wiki/inbox/{YYYY-MM-DD} telegram capture.md` — one file per day,
  timestamped entries (`## HH:MM`), Obsidian image embeds (`![[filename]]`)
  for photos
- `Dawson's wiki/zz_images/tg-{timestamp}.jpg` — photos captured via Telegram
- Once a day (`DAILY_REVIEW_HOUR`, default 21:00 `WIKI_TZ`): up to
  `DAILY_REVIEW_MAX_QUESTIONS` (default 3) Telegram messages with
  inline-keyboard multiple-choice questions about that day's capture file —
  answers are appended to the same file under `## Clarifications (...)`

## May write

- `Dawson's wiki/inbox/**` — **new files only** (one per day); appends to its
  own `{date} telegram capture.md` files only, never edits or deletes other
  inbox notes
- `Dawson's wiki/zz_images/**` — new photo files only

## Must not

- Write to `Dawson's wiki/wiki/`, `system/review_queue/`,
  `system/constitution|agents|prompts|schemas/`
- Edit or delete existing inbox notes (incl. the user's own manual notes, or
  past days' capture files) — only append to *today's* capture file
- Fabricate answers to its own clarifying questions, or invent
  room/vendor names not present in the wiki or the day's notes
- Ask more than `DAILY_REVIEW_MAX_QUESTIONS` per day, or ask at all if the
  day's notes are already clear, or if nothing was captured that day

## Implementation notes

- `/note <text>` and photo messages append a timestamped entry to today's
  capture file (created on first use each day, with minimal YAML
  frontmatter), mirroring the user's existing manual inbox notes so the
  Extractor treats them identically.
- The daily review runs as a `JobQueue.run_daily()` job at `DAILY_REVIEW_HOUR`
  (`WIKI_TZ`, default `Asia/Singapore`). It only acts if today's capture file
  exists and hasn't been reviewed yet (`reviewed: true` in its frontmatter) —
  if the user captured nothing that day, it's a silent no-op.
- Question generation is a single litellm call (same `LLM_MODEL` as chat) with
  the day's notes as text plus any referenced photos as vision content blocks
  (base64 data URLs). The model returns strict JSON
  (`{"questions": [{"question": ..., "options": [...]}]}`), capped and
  validated before use.
- Each question is sent as a Telegram message with an inline keyboard: one
  button per option, plus "Other (type below)" (switches to free-text reply)
  and "Skip". Answers are appended as `- Q: ...` / `  A: ...` pairs under a
  `## Clarifications (timestamp)` heading, then the file is marked
  `reviewed: true` so it's never re-processed.
- Assumes 1:1 private Telegram chats only (`chat_id == user_id` for each
  `TELEGRAM_ALLOWED_USER_IDS` entry), so the scheduled job can message users
  directly without an incoming update.
- Soft-required like chat/`/research`: if the configured LLM's `*_API_KEY`
  isn't set, the daily review is silently skipped (logged), while `/note` and
  photo capture (no LLM involved) keep working regardless.
- Same access control as the Conversation agent (`TELEGRAM_ALLOWED_USER_IDS`).
