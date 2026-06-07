# Extractor Agent

**Status:** proven — first pass completed (`system/runs/2026-06-07-extraction-01.md`, 6 proposals)

## Purpose

Pull structured facts from `raw/` and `inbox/` using `system/schemas/`.

## Inputs

- `raw/sheets/`, `raw/drive/`
- `Dawson's wiki/inbox/*.md`
- `system/schemas/*.yaml`
- `system/constitution/*`

## Outputs

- Structured records (item, vendor, task) — live inside review queue proposals; the proposal
  files ARE the durable structured output, not a separate YAML dump
- Low-confidence (and, on a first pass, essentially all "new entity") items → `system/review_queue/`
- Run log → `system/runs/` — keep this LEAN: a summary table + proposal index + learnings.
  Do not duplicate full YAML records into the run log (see gotcha 0 below)

## May write

- `system/review_queue/**`
- `system/runs/**`
- `system/state/**` (processed manifest)

## Must not

- Write compiled wiki notes directly
- Delete or edit inbox/raw sources
- Write `system/constitution/`, `agents/`, `prompts/`, `schemas/` (Harness only)

## How to run a pass (procedure that worked)

1. Read `note-creation.md` + the schemas first — they define what's worth a record and the
   record shape. Read the latest ingestion run log's "Next steps" — it often flags specific
   reconciliation issues (conflicting figures, superseded drafts) worth resolving explicitly.
2. Read every raw source in full, including ones that look like low-value supplementary
   material — see gotcha 3.
3. **Group into a small, reviewable set of proposals (5–10 files), not one-per-fact.** Sensible
   axes: by vendor, by room/theme, by record type (tasks/decisions). One proposal = one
   self-contained reviewable unit (compiled note path + why + cited sources + YAML records +
   open questions).
4. **Write each proposal file immediately after drafting it** — don't hold several in memory
   to emit at the end (this caused a stall on the first attempt at this task; see gotcha 0).
5. Write the run log LAST: summary table of sources, an index of proposal files (one-line
   description each — not their YAML content), rough record counts, and a "Learnings" section.

## Known gotchas / judgment calls (from extraction-01 — read before re-running)

0. **CRITICAL — composing one giant final output stalls the agent.** A first attempt asked for
   both full YAML dumps in the run log AND separate proposal files; it stalled mid-composition
   (10 min no progress, watchdog-killed) before writing anything. Always write incrementally —
   one proposal file per `Write` call, run log last and lean.
1. **`source` field convention**: the schema doesn't specify a list type, so when a record is
   corroborated by multiple raw files, use a semicolon-separated string: `"path/a.md; path/b.md"`.
   Consistent and grep-able. (Harness: consider formalizing this, or changing `source` to `list`.)
2. **Cross-document price discrepancies are usually explainable (rebates/GST/bundling), not
   errors.** Record both figures with the discrepancy flagged rather than silently picking one —
   picking wrong plants a hard-to-unwind false fact.
3. **Don't skim "comment"/"review" documents — they hide real task-shaped material.** A 21-page
   design-review-comments PDF looked like idle feedback but contained firm decisions ("we won't
   have a dishwasher"), genuinely open follow-ups ("wardrobe wood vs white — not sure"), and
   multi-item layout puzzles. A skim would have missed all of it. Read these in full.
4. **"Confirmed" in a source tracker ≠ automatically `status: ordered`.** This pass required an
   independently corroborating purchase-order/invoice document before marking an item "ordered";
   "Confirmed"-only rows were rated "shortlisted" + medium confidence. (Harness/human: confirm
   whether that's the right level of skepticism.)
5. **Room naming is inconsistent across sources — flag it, don't silently pick one.** The same
   room appeared as "Study Room/Guest Bedroom", "Bedroom 2", "Common Bedroom" (signed contract),
   and "Guest Bedroom" (item tracker) across different documents. Pick a working name, cite your
   reasoning, and flag the ambiguity in the proposal — canonical naming is a Harness/human/
   Compiler decision (the signed contract's terminology is the natural tie-breaker, since it's
   the legally authoritative as-built reference).
6. **No "whole-house"/cross-cutting item category exists in the `Rooms/{Room}/{Item}.md`
   layout.** Items like Aircon, Day Curtain, and Painting Works apply to "All rooms" per the
   source tracker but `note-creation.md` has no sanctioned pattern for this. Park them somewhere
   pragmatic, flag loudly, and let Harness decide (a "Whole House" pseudo-room? a `scope` field?
   prose in the room note instead of a dedicated item note?).
7. **Propagate OCR/source-quality issues into the `confidence` field, not just a footnote.**
   When a source has multiple conflicting OCR readings of the same number, trust the
   cross-referenced/corroborated figure but mark uncorroborated sub-facts (e.g. balance amounts,
   delivery dates) as separately low-confidence.
8. **Budget near-zero extraction time for sources the ingestion run already flagged as
   metadata-only or out-of-scope** (binary archives, photo batches, house-purchase-scoped
   spreadsheets) — confirm they're empty/irrelevant, then move on; don't over-invest there.
