# Proposal: Kitchen appliances + whole-house Aircon — item records

**Date:** 2026-06-07
**Proposed by:** Extractor
**Status:** ✅ APPROVED — WITH ONE STRUCTURAL CHANGE (2026-06-08, by Jefferson)

**Human decision notes:**
- **Aircon placement (call-out #1) — OVERRIDE the proposed Kitchen placement.** Create a new
  `Whole House` room folder (`Dawson's wiki/wiki/Rooms/Whole House/Whole House.md`) and file
  `Aircon.md` there instead of under Kitchen. Rationale: the Aircon system spans Master
  Bedroom + Living/Common Bedroom zones (per the Gain City order itself) — filing a
  whole-house system under "Kitchen" would be actively misleading, not just imperfect. This
  also creates the canonical home for future cross-cutting items the Extractor flagged
  (Day Curtain, Painting Works, etc.) — establishing the "Whole House" pattern now.
- All other items (Fridge, Washer-Dryer, Microwave, Hob, Hood, Oven) approved as proposed,
  staying under `Rooms/Kitchen/`.
- Kitchen room note seed approved as written, MINUS the Aircon Appendix-A cross-reference
  (move that reference to the new Whole House note instead).
- Price-discrepancy handling (both tracker and order-line figures recorded side-by-side) —
  approved as the right call; do not silently pick one figure.

## What to change

Create a new compiled room note + item notes:

- `Dawson's wiki/wiki/Rooms/Kitchen/Kitchen.md` (room note)
- `Dawson's wiki/wiki/Rooms/Kitchen/Fridge.md`
- `Dawson's wiki/wiki/Rooms/Kitchen/Washer-Dryer.md`
- `Dawson's wiki/wiki/Rooms/Kitchen/Microwave.md`
- `Dawson's wiki/wiki/Rooms/Kitchen/Hob.md`
- `Dawson's wiki/wiki/Rooms/Kitchen/Hood.md`
- `Dawson's wiki/wiki/Rooms/Kitchen/Oven.md`
- `Dawson's wiki/wiki/Rooms/Kitchen/Aircon.md` (whole-house item, filed under Kitchen per the
  Reno Sheet's "All rooms" grouping placed alongside the kitchen-area appliance cluster — see
  call-out #1 for an alternative placement)

Trigger: "Real room in source data" + "Real item to track" — this is the densest cluster of
CONFIRMED, vendor-ordered appliances in the corpus (3 of 4 have completed Gain City Sales
Orders with order numbers, prices, and outstanding-balance figures).

## Why / cited sources

- `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` §"Furniture & Appliances" (Kitchen group +
  "All rooms" Aircon row) — authoritative tracker.
- `raw/drive/fridge-washer-dryer-microwave-2026-06-07.md` — Gain City SO-B0000296807 (fridge +
  washer/dryer + microwave bundle order).
- `raw/drive/gain-city-aircon-lg-2026-06-07.md` — Gain City SO-B0000296812 (LG System-2 aircon,
  master bedroom 12k/12k + living/common-room 24k/12k).
- `raw/drive/jm-house-moodboard-2026-06-07.md` (slides 16-19) and
  `jm-house-moodboard-v2-2026-06-07.md` (slides 11-14) — kitchen design-intent notes.
- `raw/drive/skyville-dawson-bud-studio-first-draft-comments-2026-06-07.md` (pages 6-9) —
  client review comments on the dry-pantry/kitchen render (key decisions: dry pantry option 1
  chosen, "we won't have dishwasher", appliance placement swaps).

## Proposed item records

```yaml
- name: Fridge
  room: Kitchen
  status: ordered
  vendor: "Gain City"
  model: "Samsung 655L Side-By-Side Refrigerator RS70F65Q3TSS (W91.2 x H178.0 x D71.6cm, Silver)"
  price: "$1,759.00 (Gain City order line) / $1,501.13 (Reno Sheet tracker figure, post-rebate?)"
  currency: SGD
  notes: |
    Status "Confirmed". Part of bundled Gain City Sales Order SO-B0000296807 (fridge + washer/
    dryer + microwave), ordered 6 Jun 2026, CASH terms, bundle total $3,215.00 outstanding.
    PRICE DISCREPANCY: the Reno Sheet tracker shows $1,501.13 but the Gain City order line
    item shows $1,759.00 — likely the tracker figure nets out a share of the order's combined
    rebates/discounts (-$360 BTO instant cash rebate spread across the 3 items, GST treatment,
    etc.) rather than being a data error. Listed both for traceability; a human could
    reconcile exactly how the per-item tracker figures were derived from the bundle invoice.
    Schematic floor plan also lists "2 DOOR FRIDGE SAMSUNG" as a furniture-legend annotation —
    consistent with this model. Bud Studio Appendix A includes a dedicated "full ht. cabinet
    for fridge incl. 2 side panels" (Section J item 5, $1,950) to house this unit.
  source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Furniture & Appliances); raw/drive/fridge-washer-dryer-microwave-2026-06-07.md"
  confidence: high

- name: Washer-Dryer
  room: Kitchen
  status: ordered
  vendor: "Gain City"
  model: "Sharp Washer/Dryer 12.5/8KG ES-FW12D8PAS (W598 x D640 x H850mm)"
  price: "$1,664.00 (Gain City order line, post -$185 discount) / $1,577.94 (Reno Sheet tracker figure)"
  currency: SGD
  notes: |
    Status "Confirmed". Same bundled order as Fridge/Microwave (SO-B0000296807). Same
    tracker-vs-order price discrepancy pattern noted on the Fridge record applies here too.
    Design context: moodboard explicitly states "We'll only have 1 wash & dry machine"
    (render comment, page 9) — i.e. a combo unit was a deliberate choice, matching this SKU.
  source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Furniture & Appliances); raw/drive/fridge-washer-dryer-microwave-2026-06-07.md; raw/drive/skyville-dawson-bud-studio-first-draft-comments-2026-06-07.md"
  confidence: high

- name: Microwave
  room: Kitchen
  status: ordered
  vendor: "Gain City"
  model: "Samsung Microwave Oven 23L MS23DG4504AGSP (W48.9 x H27.5 x D37.7cm)"
  price: "$152.00 (Gain City order line, post -$17 discount) / $144.22 (Reno Sheet tracker figure)"
  currency: SGD
  notes: "Status 'Confirmed'. Third item in the bundled Gain City order SO-B0000296807 alongside Fridge and Washer-Dryer. Same minor tracker-vs-order price variance pattern as the other two bundle items (likely rebate/GST allocation)."
  source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Furniture & Appliances); raw/drive/fridge-washer-dryer-microwave-2026-06-07.md"
  confidence: high

- name: Hob
  room: Kitchen
  status: shortlisted
  vendor: ""
  model: "Bosch Induction Hob PUE611BB5J (W259.2 x H5.1 x D52.2)"
  price: "$1,159.00"
  currency: SGD
  notes: |
    Listed in the Reno Sheet tracker WITHOUT a "Confirmed" flag — appears to be a planned
    purchase, not yet ordered (no matching purchase-order document found in raw/).
    DESIGN-DECISION NOTE: client review comments include "Replace sink with stove / Replace
    stove with sink" (page 9) — i.e. the kitchen layout's stove/sink placement was an open
    question being actively reconsidered at render-review stage; the chosen brand/model
    (Bosch induction) appears settled, but FINAL POSITIONING in the kitchen layout may still
    be in flux. Worth a human check before treating "shortlisted" as final.
  source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Furniture & Appliances); raw/drive/skyville-dawson-bud-studio-first-draft-comments-2026-06-07.md (page 9)"
  confidence: medium

- name: Hood
  room: Kitchen
  status: shortlisted
  vendor: ""
  model: "Bosch DWBM98G50B Chimney Hood (H45-84 x W90 x D50.5)"
  price: "$799.00"
  currency: SGD
  notes: "Listed in Reno Sheet tracker, not flagged Confirmed. Render-comment page 9 raises an open question — 'Chimney hood on top of stove?' — suggesting hood placement (and possibly choice) was still being finalised at review stage."
  source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Furniture & Appliances); raw/drive/skyville-dawson-bud-studio-first-draft-comments-2026-06-07.md (page 9)"
  confidence: medium

- name: Oven
  room: Kitchen
  status: shortlisted
  vendor: ""
  model: "Bosch Built-in Oven 71L HHF113BR0B"
  price: "$849.00"
  currency: SGD
  notes: "Listed in Reno Sheet tracker, not Confirmed. Render-comment page 9 notes 'Oven moves here, with stove' — i.e. oven placement within the kitchen layout was being actively reworked during the design-review round."
  source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Furniture & Appliances); raw/drive/skyville-dawson-bud-studio-first-draft-comments-2026-06-07.md (page 9)"
  confidence: medium

- name: Aircon
  room: Kitchen   # whole-house item — see call-out #1 on placement
  status: ordered
  vendor: "Gain City"
  model: "LG System 2 Aircon Alpha — Master 12k/12k (Z3UQ28GFA1/2X12GSJBO) + Living 24K/Room 12K (Z4UQ34GFA1/1X12GSJB0/1X24GSKBO), incl. 1+4yr EW-Basic warranty plans"
  price: "$4,973.00"
  currency: SGD
  notes: |
    Status "Confirmed". Gain City Sales Order SO-B0000296812, ordered 6 Jun 2026, CASH terms,
    full $4,973.00 outstanding, delivery method "INSTALLATION". Two independent system-2 units
    covering Master Bedroom (12k/12k) and Living/Common Bedroom (24k/12k) zones.
    NOTE: The Bud Studio "Excluding" list (Reno Sheet header) explicitly EXCLUDES aircon
    (~$4,000 estimated allowance) from the contractor's scope — this Gain City order is the
    actual realised aircon spend, slightly above that allowance ($4,973 vs ~$4,000 estimate).
  source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Furniture & Appliances + Exclusions); raw/drive/gain-city-aircon-lg-2026-06-07.md"
  confidence: high
```

## Proposed room note seed (Kitchen.md)

```yaml
name: Kitchen
notes: |
  Combined Kitchen + (dry pantry + service yard, per the Bud Studio "Kitchen/Yard" grouping
  and moodboard slide 12's "Kitchen: ... / Service Yard: ..." split). Design principles
  (J&M House Moodboard slides 2, 16-19; v2 slides 11-14):
    - Open up to the service area to make the kitchen feel bigger
    - Counter/cabinet below should be wider than cabinets above (less "stuffy" feel)
    - Dedicated coffee corner; "BRIGHT, two-tone cabinet, backsplash tiles & hidden lights,
      cool Japandi" aesthetic
    - Open question (moodboard): separate water filter for drinking water — RESOLVED per
      Reno Sheet: "3M AP Easy Complete (Under-Sink)" filter + "RIGEL Kitchen Faucet" listed
  CONFIRMED design decisions from the first-draft render review (client comments, pages 6-9):
    - Dry pantry layout: chose OPTION 1 over option 2 ("Let's go with this")
    - "We've decided — we won't have a dishwasher!" (explicit, definitive)
    - Stove/sink/oven/hood relative placement was still being actively reworked at review
      time ("Replace sink with stove / Replace stove with sink"; "Oven moves here, with
      stove"; "Chimney hood on top of stove?") — see per-item notes for Hob/Hood/Oven
    - Robot cleaner gets a dedicated "home" corner; dryer rack on top of W/D unit
    - Considered an all-dark-brown finish (top + bottom hung cabinets) — referenced an
      Instagram inspiration image
  Bud Studio Appendix A scope for this area: extensive — hacking ($2,800 incl. in Section B
  item 1), tiling/waterproofing/plastering (Section D, ~$2,860 of the $12,080 D-total),
  6 carpentry items (Section J items 5-9, ~$8,745), and 3 of 4 Worktop/Countertop line items
  (Section K, ~$3,515 of $4,070 — Lian Hin quartz Raw Edition Tundra).
source: "raw/drive/jm-house-moodboard-2026-06-07.md; raw/drive/jm-house-moodboard-v2-2026-06-07.md; raw/drive/skyville-dawson-bud-studio-first-draft-comments-2026-06-07.md; raw/sheets/reno-sheet-bud-studio-2026-06-07.md"
confidence: high
```

## Human-judgment call-outs

1. **Aircon is a WHOLE-HOUSE item, not kitchen-specific** — the Reno Sheet lists it under
   "All rooms". I filed it under Kitchen purely because that's where it sits in the tracker's
   row order and because note-creation.md says "Items live under room folders, not a global
   Items/ folder" (no "Whole House" room exists). A human may prefer a dedicated "Whole House"
   or "General" room/area for cross-cutting items (Aircon here, and potentially "Day Curtain"
   from the same "All rooms" tracker group, painting works, etc.) — flagging for Compiler
   judgment; this is the single biggest structural question across all the item proposals.
2. **Three appliances (Fridge/Washer-Dryer/Microwave) show price discrepancies between the
   Reno Sheet tracker and the Gain City Sales Order line items** — likely explained by
   rebate/discount/GST allocation across the bundled order, but I have not reverse-engineered
   the exact math. Recorded both figures with the discrepancy flagged rather than picking one.
3. **Hob/Hood/Oven are NOT flagged "Confirmed"** in the tracker, yet the render-comment
   feedback shows their relative kitchen-layout POSITIONS were still being actively reworked —
   meaning even the brand/model choices recorded in the tracker might be provisional pending
   a finalised layout. I rated these "shortlisted"/medium-confidence rather than
   "ordered"/high to reflect that uncertainty.
4. Confidence: high for the 4 items with completed Gain City Sales Orders (Fridge,
   Washer-Dryer, Microwave, Aircon); medium for the 3 tracker-only kitchen appliances whose
   layout placement is still in flux per the design-review comments.
