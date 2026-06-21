# Proposal: Bathroom — new room note + grout/lighting/tile follow-ups (2nd design revision meeting)

**Date:** 2026-06-13
**Proposed by:** Extractor
**Status:** ✅ APPROVED (2026-06-14, by Jefferson) — approved WITH CHANGES, see "Resolution"
below. The single combined `Bathroom.md` proposed in open question #1 was rejected in favour
of an immediate Master/Common split, and this proposal absorbed the (reframed) content from
the companion Kitchen proposal.

## Resolution (2026-06-14, by Jefferson)

During review of the companion Kitchen proposal
(`system/review_queue/2026-06-13-jaslyn-meeting-kitchen-design-updates.md`), Jefferson
corrected that its entire wall-colour/countertop/sink/cabinet-colour/sink-size/drying-rack
discussion is actually about the **Common Bathroom** ("common toilet"), not Kitchen. Combined
with this proposal's own grout/LED/green-tile items (also Common-Bathroom-flavoured —
shower grout, mirror niche, green wall tile), Jefferson decided:

- **Split immediately into `Rooms/Master Bathroom/Master Bathroom.md` and
  `Rooms/Common Bathroom/Common Bathroom.md`** (rejecting open question #1's "single combined
  note for now" suggestion) — both created with Appendix A scope breakdowns and a "naming
  note" explaining the split.
- **[[Common Bathroom]]** got the full "2nd design revision" section covering BOTH this
  proposal's items AND the reframed Kitchen-proposal items:
  - Wall colour (reddish + subway tiles + lemon), lime-wash texture
  - Travertine countertop + round undermount sink (NEW scope vs. contract — no countertop in
    Common Bathroom's existing Appendix A scope)
  - Cabinet colour (darker bottom half, red-hair-material contrast)
  - Sink size (80cm) + drying rack/drawer layout
  - Shower grout upgrade, LED mirror-niche lighting, green wall tile research
- **Tasks created** (renumbered/retitled from both proposals' originals, all under Common
  Bathroom):
  - [[TASK-0008 - Confirm Common Bathroom vanity countertop material (travertine) and round undermount sink]]
    (was Kitchen TASK-0008)
  - [[TASK-0009 - Update Common Bathroom cabinet colour (darker bottom half, reduce contrast)]]
    (was Kitchen TASK-0009)
  - [[TASK-0010 - Confirm Common Bathroom sink size (80cm) and drying-rack-drawer layout]]
    (was Kitchen TASK-0010)
  - [[TASK-0011 - Upgrade Common Bathroom shower grout to water-resistant type]]
    (this proposal's TASK-0011, area reassigned from "Master and/or Common — unclear")
  - [[TASK-0012 - Add LED lighting in Common Bathroom mirror niche-shelf]]
    (this proposal's TASK-0012, area reassigned)
  - [[TASK-0013 - Resolve Common Bathroom green wall — lighter-brown render update vs. tile research]]
    (this proposal's TASK-0013, area reassigned, ALSO folds in the Kitchen meeting's "lighter
    brown wall colour instead of green" action item — open question #2 below is resolved by
    treating both as the same Common Bathroom green-wall surface)
- **Master Bathroom** got only its Appendix A scope breakdown (~$9,310) — no 2nd-revision
  discussion content applied to it; it remains a "naming note" companion to Common Bathroom.
- Shampoo-dish-colour and lighting colour-temperature minor points (open question #3) were
  included in [[Common Bathroom]]'s open-discussion content as originally suggested — not
  elevated to standalone tasks.

## What to change (ORIGINAL PROPOSAL TEXT — superseded by Resolution above)

1. **CREATE** `Dawson's wiki/wiki/Rooms/Bathroom/Bathroom.md` — a new room note. Trigger:
   "Real room in source data" per `note-creation.md` — the contract (Appendix A) already
   carries substantial bathroom scope (Section D items 6-10, Section E items 4-5, Section H
   items 2-3, Section I item 1, Section J items 16-17, Section K item 4 — tiling,
   waterproofing, doors, glass, mirror cabinet, vanity cabinet, countertop — roughly
   $3,680+$860+$650+$3,240+$650+$1,395+$1,695+$700+$570+$600+$555 across Master Bathroom +
   Common Bathroom), but no room note exists yet (the first extraction pass focused on
   furniture/appliance "Items", and the Reno Sheet's bathroom rows are all $0.00
   placeholders, so it was correctly skipped at the time per `note-creation.md`'s
   no-placeholder rule). The 2nd design revision meeting now adds REAL design-decision
   content (grout, tile colour/material, lighting) — see open question #1 for the
   Master-vs-Common split question.

2. **CREATE** new task records (task.yaml schema):
   - TASK-0011: Upgrade shower grout to water-resistant type + update design
   - TASK-0012: Add LED lighting in bathroom mirror niche/shelf
   - TASK-0013: Research/confirm green wall tile sizing and whether custom-made

## Why / cited sources

- `Dawson's wiki/inbox/Meeting with Jaslyn.md` — "Color and Material Choices for Bathroom"
  outline section, plus 3 of the 8 action items (grout upgrade, LED niche lighting, green
  wall tile research).
- `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` — Appendix A: "Master Bathroom" (Section D
  items 6-8, E item 4, H item 3, I item 1, J items 16-17, K item 4) and "Common Bathroom"
  (Section D items 9-10, E item 5, H item 2) line items; furniture tracker's Sink/WC/Faucet
  $0.00 placeholder rows for both bathrooms.

## Open questions / judgment calls

1. **Master Bathroom vs. Common Bathroom — the meeting doesn't distinguish.** The signed
   contract (Appendix A) treats these as two separate scoped rooms with different line items
   (e.g. Master Bathroom gets a glass shower partition + seated vanity cabinet + mirror
   cabinet; Common Bathroom does not). The 2nd design revision meeting's transcript summary
   never says which bathroom is being discussed for the grout/tile/lighting topics — it's
   plausible the meeting covered both, or one as a template for the other. I'm proposing a
   SINGLE combined `Bathroom.md` note for now (documenting both contract scopes side by side
   and the meeting's open items without assigning them to one or the other), following the
   precedent set for [[Whole House]] (a pragmatic placeholder pattern, flagged for
   Harness/human to decide whether to split into `Rooms/Master Bathroom/` and
   `Rooms/Common Bathroom/` later once the design decisions are room-specific).
2. **Green wall tiles vs. the "lighter brown wall colour instead of green" action item** —
   the Kitchen proposal (`2026-06-13-jaslyn-meeting-kitchen-design-updates.md`) covers an
   action item to change a wall from green to "lighter brown". This proposal's green-wall-TILE
   item (action item: "research... custom green wall tiles... whether they need to be
   custom-made") could be the SAME green surface being discussed for replacement, or a
   DIFFERENT green tile elsewhere that's being kept/researched rather than replaced — the
   transcript doesn't make the relationship clear. Flagging both proposals' authors should
   cross-check this with Jaslyn/Bud Studio renders directly.
3. **Shampoo dish colour** ("Speaker 2 suggesting a fun, colorful option") and **lighting
   colour-temperature debate** ("natural lighting looks cooler than artificial light") are
   minor/low-confidence discussion points — included in the room note's "open design
   discussion" section for completeness but NOT elevated to standalone tasks (too minor to
   track individually; the LED-niche task (TASK-0012) covers the lighting follow-up that
   actually has an action item attached).

## Proposed records

```yaml
- id: TASK-0011
  title: "Upgrade shower grout to water-resistant type + update bathroom design"
  status: open
  area: "Bathroom (Master and/or Common — unclear, see review_queue proposal open question #1)"
  due: ""
  owner: "Jaslyn (Bud Studio)"
  notes: |
    Action item from the 2nd design revision meeting: "Upgrade the grout in the shower area
    to a more water-resistant type and update the design to reflect this change." Discussion
    context: tile colour saturation debate ("recommending a more saturated hue") and a
    floor-tile mismatch concern ("the three pictures almost look like two different rooms").
    Both Master Bathroom and Common Bathroom have contracted shower/wet-area tiling scope
    (Appendix A Section D items 6-10) — grout spec wasn't broken out separately in the
    contract, so this is likely a spec refinement within existing tiling line items rather
    than new scope (lower Change-Order risk than the kitchen countertop question).
  related:
    - "Rooms/Bathroom/Bathroom.md"
    - "Vendors/Bud Studio.md"
  source: "Dawson's wiki/inbox/Meeting with Jaslyn.md"
  confidence: medium

- id: TASK-0012
  title: "Add LED lighting in bathroom mirror niche/shelf"
  status: open
  area: "Bathroom (Master and/or Common — unclear, see review_queue proposal open question #1)"
  due: ""
  owner: "Jaslyn (Bud Studio)"
  notes: |
    Action item from the 2nd design revision meeting: "Add LED lighting in the niche/shelf
    area behind the mirror in the bathroom." Master Bathroom has a contracted "top hung
    mirror cabinet" (Appendix A Section J item 16, 3ft, $570) — this LED addition likely
    applies to that cabinet/niche if Master Bathroom, though Common Bathroom's mirror
    arrangement isn't separately specified in the contract. Related lighting discussion in
    the same meeting debated colour temperature ("natural lighting looks cooler than
    artificial light") — minor context, not separately tracked.
  related:
    - "Rooms/Bathroom/Bathroom.md"
    - "Vendors/Bud Studio.md"
  source: "Dawson's wiki/inbox/Meeting with Jaslyn.md"
  confidence: low

- id: TASK-0013
  title: "Research/confirm green wall tile sizing and whether custom-made"
  status: open
  area: "Bathroom (Master and/or Common — unclear, see review_queue proposal open question #1)"
  due: ""
  owner: "jeff / Marcella"
  notes: |
    Action item from the 2nd design revision meeting: "Research and confirm the exact size
    and tile options for the custom green wall tiles, including whether they need to be
    custom-made." May relate to the Kitchen proposal's "lighter brown wall colour instead of
    green" action item (`2026-06-13-jaslyn-meeting-kitchen-design-updates.md`) — possibly the
    same green surface being reconsidered, or a different one being kept. Needs
    cross-checking against the actual renders with Jaslyn/Bud Studio.
  related:
    - "Rooms/Bathroom/Bathroom.md"
    - "TASK-0009"
  source: "Dawson's wiki/inbox/Meeting with Jaslyn.md"
  confidence: low
```
