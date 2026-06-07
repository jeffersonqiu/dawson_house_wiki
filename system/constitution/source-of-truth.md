# Source of Truth

## Authoritative

- **`Dawson's wiki/wiki/`** — compiled renovation knowledge (rooms, vendors, tasks, decisions)
- Maintained by the compiler agent from `inbox/`, `raw/`, and approved review queue items
- Direct human edits in compiled notes are overrides — preserve on next compile, do not silently revert

## Inputs only (not the database)

| Location | Source |
|----------|--------|
| `raw/sheets/` | Google Sheets exports |
| `raw/drive/` | Google Drive exports |
| `Dawson's wiki/inbox/` | Quick human capture in Obsidian |

Inputs are preserved for audit. Do not treat them as the final record.

## Not renovation knowledge

- `system/` — harness config, state, logs
- `AGENT.md`, `HARNESS_PLAN.md` — project docs

## Provenance

Compiled facts should link or cite their source when practical (inbox note, sheet export, drive file). Full `Sources/` folder is deferred.
