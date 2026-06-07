# Dawson House Wiki — What We Are Building

North-star document for this project. For repo layout and working rules, see `AGENT.md`.

## Problem

Renovation information is scattered across Google Sheets, Google Drive, chat logs, and ad-hoc notes. It is hard to maintain a single clear picture of rooms, items, vendors, tasks, and decisions.

## Goal

Build a **personal renovation knowledge base** where:

1. You can dump information quickly from multiple sources.
2. The system gradually compiles it into clean, browsable Obsidian markdown.
3. A future **agent harness** maintains the compiled wiki; humans capture in `inbox/` and approve risky changes via review queue.

The compiled wiki (`Dawson's wiki/wiki/`) is the human-readable database. Google Sheets and Drive are inputs, not the source of truth.

## Architecture

```text
Inputs                    Local project
────────                  ─────────────
Google Sheets      →      raw/sheets/
Google Drive       →      raw/drive/
Obsidian capture   →      Dawson's wiki/inbox/

                          ↓ (future harness)

                          Dawson's wiki/wiki/     ← compiled knowledge
                            Rooms/
                            Vendors/
                            Tasks/

                          system/               ← rules, schemas, state, logs
```

**Three layers:**

| Layer | Role |
|-------|------|
| `raw/` + `inbox/` | Unprocessed input |
| `Dawson's wiki/wiki/` | Compiled renovation knowledge (Obsidian) |
| `system/` | Harness config — constitution, agents, prompts, schemas, state |

## The harness (future)

Four roles, built incrementally:

| Agent | Job |
|-------|-----|
| **Harness** | Maintain `system/` rules, roles, prompts, schemas — only agent that may edit harness config |
| **Ingestion** | Pull Sheets/Drive snapshots into `raw/`; track import state |
| **Extractor** | Pull structured facts from `raw/` and `inbox/`; flag uncertain items for review |
| **Compiler** | Write justified updates to `Dawson's wiki/wiki/`; preserve human-written sections |
| **Conversation** | Answer questions from the wiki; trigger pipeline steps; require approval before writes |

Harness material lives in `system/`, not in the Obsidian vault.

## Design principles

- **Start simple** — skeleton and rules first; automation later.
- **Data-driven notes** — no placeholder room/vendor/task pages.
- **Room-centric** — items live under room folders when compiled.
- **Human in the loop** — capture in `inbox/`; risky or uncertain compiles go to `system/review_queue/` first.
- **Preserve originals** — inbox notes and raw snapshots stay unless the user archives them.

## Phases

### Phase 1 — Skeleton ✓

- [x] Folder structure (`raw/`, vault, `system/`)
- [x] Obsidian vault at `Dawson's wiki/`
- [x] `inbox/` for quick capture
- [x] `AGENT.md` entry point
- [x] Git hygiene (`.gitignore`, `.gitkeep` in empty dirs)
- [x] `HARNESS_PLAN.md`

### Phase 2 — Rules and contracts ✓

- [x] Constitution in `system/constitution/`
- [x] Schemas in `system/schemas/` (item, vendor, task)
- [x] Agent role stubs in `system/agents/`
- [x] Note creation / compiler rules in `system/constitution/note-creation.md`

### Phase 3 — MCP ingestion (current)

- [x] Project MCP config (`.cursor/mcp.json`) — Drive + Sheets via `google-workspace-mcp-advanced`
- [x] Setup guide (`MCP_SETUP.md`)
- [ ] User completes OAuth in `.env` and verifies tools in Cursor
- [ ] First pull from Sheets/Drive → `raw/`
- [x] Prompt templates in `system/prompts/`
- [x] Review queue format in `system/review_queue/README.md`
- [ ] Compile first real notes after extraction + review

### Phase 4 — Automated ingestion

- Scheduled sync, dedup, manifest in `system/state/`

### Phase 5 — Query and conversation

- Conversation agent over the compiled wiki
- Optional: search indexing, dashboards, image/OCR pipeline

Phases 4–5 are not started. Do not skip ahead.

## Not building yet

Image/OCR, vector DB, cloud hosting, live auto-sync, conversational bot UI. Revisit when Phases 2–3 are solid.

## Success criteria (end state)

- Open Obsidian and see an accurate, organized renovation picture.
- Drop a note in `inbox/` or refresh a Sheet — facts flow into the right room/vendor/task pages.
- Ask "what's the status on the kitchen hob?" and get a grounded answer.
- Every compiled fact traceable to a source (inbox note, sheet row, or drive doc).
