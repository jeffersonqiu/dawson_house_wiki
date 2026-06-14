# Research Agent

**Status:** implemented (v1) — Telegram bot, `/research` command
(`bot/telegram_bot.py` + `bot/research_agent.py`; see `bot/README.md`).

## Purpose

On request, search the web for real, currently-available alternatives to
something the user is considering buying (furniture, appliances, etc.) —
matching dimensions, functionality, style, and budget from a free-text
description — and write up a comparison note.

## Inputs

- User's free-text request (via `/research <description>` in Telegram)
- `Dawson's wiki/wiki/Rooms/*` — existing room names, used to file the note
  under a matching room (or `General` if none fit)
- Web search results (Anthropic `web_search_20250305` server tool, billed to
  the same `ANTHROPIC_API_KEY` as the Conversation agent)

## Outputs

- One new Markdown note per request:
  `Dawson's wiki/wiki/Research/{Room}/{Title}.md`
  (YAML frontmatter + Alternatives / Comparison table / Recommendation /
  Sources — see [note-creation.md](../constitution/note-creation.md))
- A short chat summary in Telegram with the saved path

## May write

- `Dawson's wiki/wiki/Research/**` — new notes only, never overwrites existing
  ones (collision → ` (2)`, ` (3)`, ...)

## Must not

- Write to `Rooms/`, `Vendors/`, `Tasks/`, `04 Decisions.md`, `inbox/`,
  `system/review_queue/`, or `system/constitution|agents|prompts|schemas/`
- Fabricate prices, dimensions, or source URLs — if search results don't
  support a claim, say so rather than inventing it

## Implementation notes

- Single Anthropic API call per request: system prompt + `web_search_20250305`
  tool (`max_uses: 5`), `max_tokens: 8000`. The model both searches and writes
  the full note + a `===SUMMARY===`-delimited chat reply in one response — no
  multi-turn orchestration.
- No review-queue gate: research notes are reference material about *options*,
  not facts about items already owned/ordered, so they can't conflict with
  compiled wiki data. The human reviews/acts on them like any other note.
- Same access control as the Conversation agent (`TELEGRAM_ALLOWED_USER_IDS`).
