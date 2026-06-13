---
description: Run the Compiler agent — turn APPROVED review_queue proposals into Obsidian wiki notes
---

You are acting as the **Compiler agent** for this project. Read `system/agents/compiler.md`
and `system/prompts/compile-wiki.md` in full before doing anything else, plus
`system/constitution/note-creation.md`, `write-safety.md`, and `source-of-truth.md`.

## Task

$ARGUMENTS

If no specific instructions were given above, do a standard pass:

1. List `system/review_queue/*.md` and check each file's `**Status:**` line.
2. **HARD GATE**: only compile proposals marked `✅ APPROVED` (or equivalent explicit human
   approval). Proposals still "awaiting human approval" must NOT be compiled — surface them to
   the user and stop, or ask whether the user wants to review/approve them now.
3. For each approved proposal, create/update the corresponding notes under
   `Dawson's wiki/wiki/` (Rooms/{Room}/{Item}.md, Vendors/{Vendor}.md, Tasks/TASK-####.md,
   `04 Decisions.md` master log) — merge into existing notes rather than overwriting human
   sections, match `system/schemas/*.yaml` frontmatter exactly, add `[[wikilinks]]` for
   cross-references, and end each note with a provenance footer citing the source proposal.
4. Flag any structural ambiguity (new room/naming conflicts, items with no obvious home, etc.)
   to the user for an explicit decision rather than guessing silently — record the decision and
   rationale inline once made.
5. Write a run log to `system/runs/{date}-compile-NN.md` summarizing what was created/updated,
   any override decisions made, and sources.

## Hard rules (from compiler.md / write-safety.md)

- May write: `Dawson's wiki/wiki/**`, `system/runs/**`, `system/state/**` (entity registry)
- Must NOT create placeholder notes
- Must NOT overwrite human sections without merging
- Must NOT delete `inbox/` or `raw/` files
- Must NOT write `system/constitution/`, `agents/`, `prompts/`, `schemas/` (Harness only)
- Review-queue approval is a HARD GATE for new room/vendor/task notes, price/status changes,
  and low-confidence items
