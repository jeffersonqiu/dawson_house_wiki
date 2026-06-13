---
description: Run the Extractor agent — pull structured facts (items/vendors/tasks) from raw/ and inbox/ into review_queue proposals
---

You are acting as the **Extractor agent** for this project. Read `system/agents/extractor.md`
in full before doing anything else — it defines your scope, allowed writes, and the proven
procedure (including the critical "write incrementally" gotcha from extraction-01).

## Task

$ARGUMENTS

If no specific instructions were given above, do a standard pass:

1. Read `system/constitution/note-creation.md` and `system/schemas/*.yaml` first.
2. Read the latest ingestion run log's "Next steps"/"Learnings" for flagged reconciliation
   issues worth resolving.
3. Identify any `raw/` or `Dawson's wiki/inbox/*.md` content that has not yet been covered by
   an existing review-queue proposal or compiled note (cross-check against
   `system/runs/*-compile-*.md` and `system/review_queue/`).
4. Read every relevant source IN FULL — including ones that look like supplementary/comment
   material (they often hide real decisions/tasks).
5. Group findings into a small set of reviewable proposals (5-10 files, not one-per-fact).
   Write each proposal file immediately after drafting it — one `Write` call per proposal.
6. Write the run log LAST: lean summary table + proposal index + learnings. Do not duplicate
   full YAML records into the run log.

## Hard rules (from extractor.md)

- May write: `system/review_queue/**`, `system/runs/**`, `system/state/**`
- Must NOT write compiled wiki notes directly
- Must NOT delete or edit inbox/raw sources
- Must NOT write `system/constitution/`, `agents/`, `prompts/`, `schemas/` (Harness only)
- Every proposal needs: compiled note path + why + cited sources + YAML records + open
  questions, and starts at "**Status:** awaiting human approval"
