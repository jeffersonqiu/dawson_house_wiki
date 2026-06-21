# Proposal: Living-Dining/TV wall — revert layout + LED gap fix (2nd design revision meeting)

**Date:** 2026-06-13
**Proposed by:** Extractor
**Status:** ✅ APPROVED (2026-06-14, by Jefferson) — approved as written.

## What to change

Source: `Dawson's wiki/inbox/Meeting with Jaslyn.md` (file mtime 2026-06-13; Otter.ai transcript
summary of "2nd 3D design revision" meeting), "Design Adjustments for Living Room" outline
section + 2 of the 8 action items.

1. **UPDATE** `Dawson's wiki/wiki/Rooms/Living-Dining/TV.md` — add a short "2nd design revision
   (Jaslyn meeting)" note under the existing "Design-decision note: 65\" vs. 75\"" section,
   recording:
   - The meeting **reaffirms 65"** as the TV size, now tied to a specific viewing-distance
     rationale: "based on the 2.4 m viewing distance" — this corroborates the existing
     **DECIDED: 65"** call (cross-ref [[04 Decisions]]), it's not a re-opening of that decision.
   - Action item: "Revert the TV wall design to the first layout" — a render/layout revision,
     separate from the TV-size question.
   - Action item: "Revise the TV wall and LED lighting detail so that the LED runs across the
     gap behind the TV and cabinet without leaving dark spots" — LED detail refinement.
   - Outline discussion: TV-wall partition height/support debate ("Speaker 5 suggesting a gap
     for better support") — relevant to the existing Appendix A Section E item 2 false-ceiling/
     partition wall + timber TV support scope ($725).

2. **CREATE** new task record (task.yaml schema):
   - TASK-0014: Revert TV wall design to first layout + fix LED lighting gap behind TV/cabinet

## Why / cited sources

- `Dawson's wiki/inbox/Meeting with Jaslyn.md` — "Design Adjustments for Living Room" outline
  section (TV size/placement, storage/LED debate, TV-wall partition height), plus action items:
  "Revise the TV wall and LED lighting detail so that the LED runs across the gap behind the TV
  and cabinet without leaving dark spots" and "Revert the TV wall design to the first layout and
  set the TV size to 65 inches based on the 2.4 m viewing distance."
- `Dawson's wiki/wiki/Rooms/Living-Dining/TV.md` — existing **DECIDED: 65"** call (Gain City
  order SO-B0000296814, confirmed/paid), which this meeting's "2.4 m viewing distance" framing
  reaffirms rather than contradicts.
- `Dawson's wiki/wiki/Rooms/Living-Dining/Living-Dining.md` — "TV wall kept clean/minimal" design
  principle and Appendix A Section E item 2 ($725, false-ceiling/partition wall at TV wall incl.
  timber TV support) — the partition-height/support discussion in this meeting relates to this
  existing contracted scope item, not new scope.

## Open questions / judgment calls

1. **"Revert ... to the first layout"** — the transcript doesn't describe what the "first
   layout" actually looked like (no access to the Bud Studio renders themselves), so the
   TV.md update above documents the *instruction* without speculating on the visual design.
   Flagged in TASK-0014 for Jaslyn/Bud Studio to confirm what "first layout" refers to.
2. **TV size reaffirmation, not a new decision** — pairing "revert to first layout" with "set
   the TV size to 65 inches" in the same action item could be read as if 65" were newly decided
   here. I'm treating it as a *reaffirmation* of the existing DECIDED: 65" call (TV.md already
   confirms this via the completed Gain City order), since nothing in the meeting suggests a
   change away from 65". No update to TV.md's `status`/`price`/order fields.
3. **LED gap fix vs. Appendix A scope** — the false-ceiling/partition wall + timber TV support
   ($725, Section E item 2) is the likely carrier for this LED detail, but the contract line
   item doesn't itemise LED placement separately, so this reads as a design refinement within
   existing scope (lower Change-Order risk), similar to the Bathroom grout item in the
   companion proposal.

## Proposed task records

```yaml
- id: TASK-0014
  title: "Revert TV wall design to first layout + fix LED lighting gap behind TV/cabinet"
  status: open
  area: Living-Dining
  due: ""
  owner: "Jaslyn (Bud Studio)"
  notes: |
    Two action items from the 2nd design revision meeting: (1) "Revert the TV wall design to
    the first layout and set the TV size to 65 inches based on the 2.4 m viewing distance" —
    the 65" size reaffirms the existing DECIDED call (Gain City order SO-B0000296814, see
    TV.md), but "first layout" isn't described in the transcript and needs Bud Studio to
    confirm which render version that refers to. (2) "Revise the TV wall and LED lighting
    detail so that the LED runs across the gap behind the TV and cabinet without leaving dark
    spots" — LED placement refinement, likely within the existing Appendix A Section E item 2
    false-ceiling/partition wall + timber TV support scope ($725). Related outline discussion:
    TV-wall partition height/support debate ("a gap for better support").
  related:
    - "Rooms/Living-Dining/TV.md"
    - "Rooms/Living-Dining/Living-Dining.md"
    - "Vendors/Bud Studio.md"
  source: "Dawson's wiki/inbox/Meeting with Jaslyn.md"
  confidence: medium
```
