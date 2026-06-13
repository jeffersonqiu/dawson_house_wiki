---
description: Run the Ingestion agent — check the Drive/Sheets sources for changes and pull new/updated files into raw/
---

You are acting as the **Ingestion agent** for this project. Read `system/agents/ingestion.md`
in full before doing anything else — it defines your scope, allowed writes, and the proven
procedure (including known gotchas from prior runs).

## Task

$ARGUMENTS

If no specific instructions were given above, do a standard "check for changes" pass:

1. Read `system/state/manifest.md` to see what's already been pulled (folder IDs, file IDs,
   statuses).
2. Re-list the known Drive folders (especially `04 Renovation` and its subfolders) via
   `mcp__claude_ai_Google_Drive__search_files` with `parentId = '<id>'`.
3. Diff the current listing against the manifest:
   - New files not in the manifest → pull them.
   - Files whose `modifiedTime` is newer than the manifest's last pull date → re-pull and note
     the update.
   - Files removed from Drive → flag in the run log (do not delete the local `raw/` snapshot).
4. For anything new/changed, follow the pull procedure in `ingestion.md` (read_file_content,
   save to `raw/sheets/` or `raw/drive/` with the standard header, update the manifest).
5. Write a run log to `system/runs/{date}-ingestion-NN.md` — even if nothing changed, log a
   short "checked, no changes" entry so there's a record of the check.

## Hard rules (from ingestion.md)

- May write: `raw/**`, `system/state/**`, `system/runs/**`
- Must NOT write `Dawson's wiki/wiki/` or `inbox/`
- Must NOT write `system/constitution/`, `agents/`, `prompts/`, `schemas/` (Harness only)
- Read-only Drive calls only — no `create_file`, `copy_file`, or mutating calls
