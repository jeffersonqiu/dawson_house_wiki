# Compiler Agent

**Status:** proven — two runs completed (`system/runs/2026-06-08-compile-01.md`, `-02.md`)

## Purpose

Turn approved extracted facts into Obsidian markdown in `Dawson's wiki/wiki/`.

## Inputs

- Approved facts (from extractor or cleared review queue)
- `system/constitution/note-creation.md`
- `system/schemas/*.yaml`

## Outputs

- New or updated compiled notes under `Dawson's wiki/wiki/`
- Run log → `system/runs/`

## May write

- `Dawson's wiki/wiki/**` (when justified and approved)
- `system/runs/**`
- `system/state/**` (entity registry)

## Must not

- Create placeholder notes
- Overwrite human sections without merge
- Delete `inbox/` or `raw/` files
- Write `system/constitution/`, `agents/`, `prompts/`, `schemas/` (Harness only)

## How to run a pass (procedure that worked)

1. List `system/review_queue/*.md` and check each file's `**Status:**` line first — the
   approval gate (only `✅ APPROVED` proposals may be compiled) is non-negotiable. If multiple
   proposals are pending, offer the human a choice between batch-approval and one-at-a-time
   review; one-at-a-time surfaces reframes (see gotcha 1) that batch approval would miss.
2. For each approved proposal, read the CURRENT state of every note it touches before editing
   — merge into existing sections/Items lists, don't overwrite. Update the provenance footer
   to cite the new proposal alongside the original one(s).
3. Record-level updates (price/status/model changes to an existing item) and brand-new notes
   both need a footer note explaining what changed and citing the approving proposal — this is
   the only durable trace of "why does this note say X now" for future readers.
4. When a proposal's `notes:` field says a record "SUPERSEDES"/"RENAMES" a prior one, say so
   explicitly in the compiled note's body, not just the footer — readers hitting the note cold
   need the history.
5. Renaming an item note is a write (new file) + delete (old file), not an in-place rename —
   grep the owning room note's Items list (and any other `[[wikilink]]` references) afterward
   and update them to the new name.
6. Write the run log last, modeled on `2026-06-08-compile-01.md` / `2026-06-14-compile-02.md`:
   per-proposal summary, an "Override decisions" section for anything structurally
   human-decided (new rooms, reassigned tasks, reframes), and "Open items carried forward".

## Known gotchas / judgment calls (from compile-01/02 — read before re-running)

1. **CRITICAL — a free-text answer during review can overturn an entire proposal's premise.**
   In compile-02, a Kitchen-design proposal looked routine until the human's free-text
   correction ("this is not kitchen but for common toilet!") reframed almost all of its content
   as belonging to a different, not-yet-existing room (Common Bathroom), and a second
   correction ("kitchen sink will be zuhne brand instead") supplied Kitchen's actual missing
   item. When a correction like this lands: STOP, ask targeted confirming questions, do
   grounding research (read the affected notes in full, grep the raw sheet for concrete
   numbers/prices) — then confirm the restructuring plan with the human BEFORE writing. Don't
   compile the reframe straight from the correction text.
2. **Review-queue proposal files are a durable audit trail for reframes, not just approvals.**
   Rather than silently compiling the corrected version, rewrite the affected proposal file(s)
   with a "Resolution" section at the top (dated, attributed) describing what actually happened
   and why, keeping the original proposed text below marked "superseded" — so the file still
   answers "what was originally proposed AND what was decided instead, and why."
3. **Splitting one proposed note into two (or more) rooms can happen at compile time**, not
   just at extraction time, if the approved reframe calls for it — e.g. compile-02 split a
   single proposed "Bathroom.md" into "Master Bathroom" + "Common Bathroom" using the
   [[Whole House]] "naming note" pattern (a blockquote at the top of each new note explaining
   the split and linking the sibling note) as the template.
4. **Reassigning a task's `area`** (e.g. from "Bathroom (Master and/or Common — unclear)" to
   "Common Bathroom") is just a normal task-note edit + footer note — no special handling
   needed once the structural ambiguity that caused the original hedge is resolved.
5. **TaskUpdate's ID parameter is `taskId`**, not `task_id` — `task_id` fails with
   InputValidationError.
