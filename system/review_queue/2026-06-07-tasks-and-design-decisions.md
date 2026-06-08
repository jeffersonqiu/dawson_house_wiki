# Proposal: Tasks, follow-ups & design decisions (incl. inbox note's 3 items)

**Date:** 2026-06-07
**Proposed by:** Extractor
**Status:** ✅ APPROVED (2026-06-08, by Jefferson)

**Human decision notes:**
- All 7 tasks (TASK-0001 through TASK-0007) approved as proposed, including TASK-0006's
  three-in-one grouping (kitchen stove/sink/oven/hood layout) — agree it's one decision
  thread, not three independent tasks.
- All 5 candidate `04 Decisions.md` rows approved for inclusion in the master decisions log,
  including the TV-size row with its flagged 65"-vs-75" note (the Gain City order is the
  closing signal — treat as DECIDED: 65", with the review-comment musing recorded as context
  for why the question briefly came up).
- TASK-0003 (shoe rack on bomb shelter door) — agreed it may be new/out-of-scope; keep the
  Change-Order flag in the note as written so it surfaces naturally in conversation with
  Bud Studio.
- Owners/areas/due-date inferences accepted as written.

## What to change

Create new task notes:

- `Dawson's wiki/wiki/Tasks/TASK-0001 - Fix under-sink wetness.md`
- `Dawson's wiki/wiki/Tasks/TASK-0002 - Confirm exhaust fan plan for kitchen.md`
- `Dawson's wiki/wiki/Tasks/TASK-0003 - Add shoe rack on top of bomb shelter door.md`
- `Dawson's wiki/wiki/Tasks/TASK-0004 - Resolve Master Bedroom wardrobe finish (wood vs white).md`
- `Dawson's wiki/wiki/Tasks/TASK-0005 - Decide full-length mirror placement in Master Bedroom.md`
- `Dawson's wiki/wiki/Tasks/TASK-0006 - Finalise kitchen stove-sink-oven-hood layout.md`
- `Dawson's wiki/wiki/Tasks/TASK-0007 - Confirm Other Furniture dining table delivery.md`

Trigger: "Real task or follow-up" per `note-creation.md`. TASK-0001/0002/0003 come directly
from the inbox capture note ("To remind Jaslyn"); TASK-0004/0005/0006 are open design
decisions surfaced explicitly in the client's first-draft render review comments (genuine
unresolved follow-ups, not idle musings — each uses language like "open to suggestions",
"still considering", "actually 1m is ok" implying active back-and-forth); TASK-0007 tracks
the dining table's outstanding delivery against its paid deposit.

## Why / cited sources

- `Dawson's wiki/inbox/House renov note.md` — "To remind Jaslyn: under sink wetness / exhaust
  in kitchen / shoe rack on top of bomb shelter door" (3 short bullet items, dated by file
  mtime ~2026-06-07).
- `raw/drive/skyville-dawson-bud-studio-first-draft-comments-2026-06-07.md` — pages 13, 16
  (wardrobe finish + mirror placement, Master Bedroom) and page 9 (kitchen layout questions).
- `raw/drive/dining-table-other-furniture-2026-06-07.md` + `raw/sheets/reno-sheet-bud-studio-2026-06-07.md`
  — dining table $450 deposit paid 30 May 2026, $1,000 balance presumably still due on delivery.

## Proposed task records

```yaml
- id: TASK-0001
  title: "Fix under-sink wetness (kitchen)"
  status: open
  area: Kitchen
  due: ""
  owner: "Jaslyn (Bud Studio)"
  notes: |
    Captured verbatim from the homeowner's inbox note as a reminder to raise with Jaslyn
    (Bud Studio's designer/PM contact, 65 8774 7331). No further detail on the nature/
    location of the wetness issue is given in the source — likely a plumbing/waterproofing
    snag the contractor needs to inspect or address before/during kitchen works.
  related:
    - "Vendors/Bud Studio.md"
    - "Rooms/Kitchen/Kitchen.md"
  source: "Dawson's wiki/inbox/House renov note.md"
  confidence: high

- id: TASK-0002
  title: "Confirm exhaust fan / ventilation plan for kitchen"
  status: open
  area: Kitchen
  due: ""
  owner: "Jaslyn (Bud Studio)"
  notes: |
    Captured verbatim from the inbox note: "Exhaust in kitchen" — a reminder to raise with
    Jaslyn. Likely relates to confirming exhaust/ventilation provisions alongside the chimney
    hood (see TASK-0006 — hood placement is itself an open question, "Chimney hood on top of
    stove?" per the design-review comments) — these two follow-ups may be the same underlying
    conversation thread; flagged as related but kept separate per the inbox's own item split.
  related:
    - "Vendors/Bud Studio.md"
    - "Rooms/Kitchen/Hood.md"
    - "TASK-0006"
  source: "Dawson's wiki/inbox/House renov note.md"
  confidence: high

- id: TASK-0003
  title: "Add shoe rack on top of bomb shelter door"
  status: open
  area: "Entrance Foyer / Whole House"
  due: ""
  owner: "Jaslyn (Bud Studio)"
  notes: |
    Captured verbatim from the inbox note: "Shoe rack on top of bomb shelter door" — a
    reminder to raise with Jaslyn. HDB flats include a household shelter ("bomb shelter");
    this appears to be an ad-hoc storage idea (using the space above the shelter door for
    shoe storage) that isn't yet reflected in the Bud Studio Appendix A carpentry scope —
    the contracted scope DOES include a separate "extended cardboard for shoe rack" /
    "half ht cabinet at dry pantry" concept at the Entrance Foyer (Section J items 1-2a,
    moodboard slide 13), but nothing explicitly tied to the bomb-shelter door. Possibly a
    new/additional ask outside current contracted scope — worth flagging to Bud Studio as
    a potential Change Order item (per Renovation Agreement clause 4).
  related:
    - "Vendors/Bud Studio.md"
  source: "Dawson's wiki/inbox/House renov note.md"
  confidence: high

- id: TASK-0004
  title: "Resolve Master Bedroom wardrobe door finish — wood vs. white"
  status: open
  area: "Master Bedroom"
  due: "before carpentry/millworks fabrication (Bud Studio Appendix B Milestone 3, 35% payment)"
  owner: "jeff / Marcella"
  notes: |
    Open design decision surfaced in the client's first-draft render review (page 13):
    "Wardrobe doors - wood finishing instead of white? Not sure if its going to be too dark
    considering the flooring will be dark too. Open to keep it white if wood doesn't work."
    This decision CASCADES — the same comment notes "With wardrobe doors being wooden, does
    that mean tv wall will also be wooded finishing?" and a follow-up comment (page 15) ties
    the wall-paint choice to it too: "Wall - light-coloured limewash paint if the wardrobe
    doors are wood?" — i.e. wardrobe-finish, TV-wall finish, and wall-paint colour are a
    linked decision bundle that should be resolved together, ideally before Bud Studio
    fabricates the millworks (the 35%-of-contract "before fabrication of millworks" payment
    milestone, $25,481.75, is the natural deadline pressure point).
  related:
    - "Rooms/Master Bedroom/Master Bedroom.md"
    - "Vendors/Bud Studio.md"
  source: "raw/drive/skyville-dawson-bud-studio-first-draft-comments-2026-06-07.md (page 13, 15)"
  confidence: medium

- id: TASK-0005
  title: "Decide full-length mirror placement in Master Bedroom"
  status: open
  area: "Master Bedroom"
  due: ""
  owner: "jeff / Marcella"
  notes: |
    Open design decision from the render review (page 16): "Full length mirror in master
    bedroom is missing. Open to suggestions on placement, but also thought of having it in
    this wall ->" (pointing to a referenced wall in the render, not captured in OCR text).
    Connects to a stated original design want — moodboard slide 21: "Opening the door should
    immediately reveal both rooms, not blocked by wall/mirror" — i.e. the mirror's placement
    must be chosen carefully so it does NOT become the very obstruction the brief warned
    against. A genuinely open spatial decision, not yet resolved in any source document.
  related:
    - "Rooms/Master Bedroom/Master Bedroom.md"
  source: "raw/drive/skyville-dawson-bud-studio-first-draft-comments-2026-06-07.md (page 16); raw/drive/jm-house-moodboard-2026-06-07.md (slide 21)"
  confidence: medium

- id: TASK-0006
  title: "Finalise kitchen stove / sink / oven / hood relative layout"
  status: open
  area: "Kitchen"
  due: ""
  owner: "jeff / Marcella / Jaslyn (Bud Studio)"
  notes: |
    Bundle of THREE related open layout questions raised together in the dry-pantry render
    review (page 9), all about appliance placement relative to one another:
      - "Replace sink with stove / Replace stove with sink" — i.e. literally swapping their
        positions was on the table
      - "Oven moves here, with stove" — oven repositioning tied to the stove's final spot
      - "Chimney hood on top of stove?" — hood placement contingent on where the stove ends up
    These three appliances/fixtures cannot be finalised independently — resolving the stove
    position is the upstream decision that the other two cascade from. Grouped as ONE task
    (rather than three) because they are a single layout-resolution exercise per the source
    comment thread. Directly relevant to the Hob/Hood/Oven item proposals
    (`2026-06-07-kitchen-and-wholehouse-appliances.md`), which I rated only "shortlisted"/
    medium-confidence specifically because of this open layout question.
  related:
    - "Rooms/Kitchen/Hob.md"
    - "Rooms/Kitchen/Hood.md"
    - "Rooms/Kitchen/Oven.md"
    - "Vendors/Bud Studio.md"
  source: "raw/drive/skyville-dawson-bud-studio-first-draft-comments-2026-06-07.md (page 9)"
  confidence: medium

- id: TASK-0007
  title: "Track Other Furniture dining table — balance payment & delivery"
  status: open
  area: "Living-Dining"
  due: ""
  owner: "jeff / Marcella"
  notes: |
    The custom dining table ($1,450.00 total) has a $450 downpayment PAID on 30 May 2026 —
    leaving an estimated ~$1,000 balance presumably due on completion/delivery (no explicit
    balance-due figure or delivery date found in the source order form, which is OCR-degraded/
    handwritten). Logged as an open follow-up to track the remaining payment + delivery
    scheduling against the room's render-confirmed spec ("Dining table - 180cm").
  related:
    - "Rooms/Living-Dining/Dining Table.md"
  source: "raw/drive/dining-table-other-furniture-2026-06-07.md; raw/sheets/reno-sheet-bud-studio-2026-06-07.md"
  confidence: low
```

## Candidate `04 Decisions.md` rows (decisions ALREADY MADE — for the Compiler's single master log)

These are firm, dated decisions (not open follow-ups) surfaced in the design-review comments —
included here as candidate rows rather than tasks, since `note-creation.md` routes "important
decisions" to the master decisions log:

| Decision | Why / context | Source |
|----------|---------------|--------|
| Dry pantry layout: chose Option 1 over Option 2 | "Prefer dry pantry option 1 compared to 2. Let's go with this." | render-comments page 6 |
| No dishwasher | "We've decided — we won't have a dishwasher!" | render-comments page 9 |
| One combo washer/dryer only (not separate units) | "We'll only have 1 wash & dry machine" | render-comments page 9 |
| Vanity/study desk width: 1 metre approved | "Study / vanity table - actually 1m is ok!" | render-comments page 16 |
| TV size: ordered 65" (Samsung Frame) — though 75" was raised as a consideration in review | Gain City SO-B0000296814 confirms 65" purchased; comments page 5 shows 75" was floated mid-review | `gain-city-tv-samsung-2026-06-07.md`; render-comments page 5 — **possible conflict, see call-out #3** |

## Human-judgment call-outs

1. **Inbox tasks (0001-0003) have NO due dates or extra context** — the inbox note is a
   3-line capture with no dates beyond the file's own modification timestamp (2026-06-07).
   I assigned owner "Jaslyn (Bud Studio)" because the note's heading explicitly says "To
   remind Jaslyn" — but the *due* field is left blank since nothing in the source implies
   urgency or a deadline window.
2. **TASK-0003 (shoe rack on bomb shelter door) may be OUT OF CONTRACTED SCOPE** — I could
   not find any line item in the Bud Studio Appendix A that covers this specific ask. If
   it's genuinely new scope, raising it could trigger the contract's Change Order process
   (cost impact + written agreement required per clause 4) — flagged so the human can decide
   whether to fold it into an existing carpentry conversation or treat it as a fresh ask.
3. **Possible TV-size decision conflict** (75" floated in review vs. 65" ultimately ordered)
   — I did NOT create a task for this because the ORDER (a completed, paid commitment) is the
   stronger signal of the actual final decision; listed it as a candidate decisions-log row
   instead, with the conflict flagged so a human can confirm "yes, we went with 65 in the
   end" (closing the loop) rather than leaving it looking like an open question.
4. **TASK-0006 groups three render-comments into one task** rather than three — they're
   phrased as a single back-and-forth about one layout puzzle; splitting them would create
   artificial task fragmentation. A human may disagree and prefer them split per-appliance to
   track independently — easy to split later if so.
5. Confidence: high for the three inbox-sourced tasks (verbatim capture, unambiguous);
   medium for the design-decision tasks (clearly real open questions, but no explicit
   deadlines/owners stated — inferred from contract milestones where reasonable); low for
   TASK-0007 (balance amount and delivery date are both inferred/estimated, not stated).
