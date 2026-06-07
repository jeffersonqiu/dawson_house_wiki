# Dawson House Wiki — Agent Entry Point

Read this first when working on this repository.

## What this project is

A local renovation knowledge base. Obsidian vault + folder structure + `system/` rules/schemas for a future harness. **Current work is setup, not building the harness yet.** Vision and phases: `HARNESS_PLAN.md`.

## Layout

```text
dawson_house_wiki/
  AGENT.md
  raw/sheets/              Google Sheets snapshots (future imports)
  raw/drive/               Google Drive snapshots (future imports)
  Dawson's wiki/           Obsidian vault — open this folder only
    inbox/                 raw human capture in Obsidian
    wiki/                  compiled renovation notes
      Rooms/ Vendors/ Tasks/
  system/
    constitution/          project rules
    agents/                future harness role definitions
    prompts/               future prompt templates
    schemas/               data contracts
    state/                 machine state
    runs/                  run logs
    review_queue/          proposed changes awaiting approval
```

## Rules

- `raw/` and `inbox/` are inputs. `Dawson's wiki/wiki/` is the compiled database.
- Do not create compiled `.md` notes until real data justifies them.
- Do not put agent/harness material in the vault. Keep it in `system/`.
- Do not open the project root in Obsidian.

**Who may touch what:** `system/constitution/write-safety.md` — per-folder read/write by role.

Editing `system/constitution/`, `agents/`, `prompts/`, or `schemas/` → you are the **Harness agent** ([harness.md](system/agents/harness.md)). No other agent may write there.

## Where to look before acting

| Folder | Use when |
|--------|----------|
| `system/constitution/` | Rules, note-creation policy, write safety |
| `system/agents/` | Harness role definitions |
| `system/prompts/` | Prompt templates |
| `system/schemas/` | Structured data contracts |
| `system/state/` | Sync/import state |
| `system/runs/` | Run logs |
| `system/review_queue/` | Items needing user approval |

Read `system/constitution/` before changing the vault or compiled notes.

## Phase

Phase 2 complete. **MCP setup:** `MCP_SETUP.md` (Google Drive + Sheets). Next: verify MCP, then ingest to `raw/`.
