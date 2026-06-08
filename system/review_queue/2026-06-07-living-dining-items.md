# Proposal: Living/Dining room — furniture, appliance & decor item records

**Date:** 2026-06-07
**Proposed by:** Extractor
**Status:** ✅ APPROVED (2026-06-08, by Jefferson)

**Human decision notes:**
- Room name: keep combined `Living-Dining` (call-out #1) — matches the tracker, floor plan,
  and Bud Studio scope, all of which treat it as one open-plan zone.
- All 6 item notes approved, INCLUDING the smaller decor items (Sound Bar, TV Console,
  Coffee Machine, Table Lamps) — per-item notes are the established pattern (see
  `Kitchen/Induction Hob.md` precedent in note-creation.md) and these are cheap to maintain
  even at lower confidence; resolves call-out #2 in favour of "create them."
- TV-size note (call-out #3): keep as written — the 65" Gain City order is the strongest
  signal of the final call; also reflected in the approved `04 Decisions.md` candidate row
  from the companion tasks/decisions proposal.

## What to change

Create a new compiled room note and item notes under it:

- `Dawson's wiki/wiki/Rooms/Living-Dining/Living-Dining.md` (room note)
- `Dawson's wiki/wiki/Rooms/Living-Dining/Dining Table.md`
- `Dawson's wiki/wiki/Rooms/Living-Dining/TV.md`
- `Dawson's wiki/wiki/Rooms/Living-Dining/Sound Bar.md`
- (lower-priority/optional — see call-out #2 for which of the smaller decor items genuinely
  warrant their own note vs. folding into the room note's furniture list)

Trigger: "Real room in source data" + "Real item to track" per `note-creation.md` — the
"02 Reno Sheet x Bud Studio" furniture/appliance tracker explicitly groups these by room
("Living/Dining"), several have CONFIRMED purchase status with vendor order numbers, and the
Dining Table has an active deposit/contract with its own vendor (Other Furniture).

## Why / cited sources

- `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` §"Furniture & Appliances" — authoritative
  room-grouped tracker with brand/model/dimensions/price/status for every item.
- `raw/drive/dining-table-other-furniture-2026-06-07.md` — Other Furniture order form/
  downpayment record for the custom dining table.
- `raw/drive/gain-city-tv-samsung-2026-06-07.md` — Gain City Sales Order SO-B0000296814
  (TV + accessories), confirms purchase.
- `raw/drive/gain-city-denza-lucky-draw-2026-06-07.md` — promo coupon stub batch tied to the
  same Gain City order/receipt no. (0000296814).
- `raw/drive/jm-house-moodboard-2026-06-07.md` (esp. slides 9, 13–15) and
  `jm-house-moodboard-v2-2026-06-07.md` (slides 5–10) — design-intent notes for this room.
- `raw/drive/skyville-dawson-bud-studio-first-draft-comments-2026-06-07.md` (pages 3–9) —
  client review comments specific to this room's render (TV console curve, mirror+storage
  placement, 75" TV consideration, dry pantry layout choice).

## Proposed item records

```yaml
- name: Dining Table
  room: Living-Dining
  status: ordered
  vendor: "Other Furniture"
  model: "Custom — H75 x W180 x D90cm; teak (per OCR fragment, unconfirmed)"
  price: "$1,450.00"
  currency: SGD
  notes: |
    Status "Confirmed" in the Reno Sheet tracker. $450 downpayment PAID 30 May 2026 (per
    hand-annotated order form). Vendor: "Other Furniture" (Design Director Lukas Drasnar,
    showroom 315 Outram Road #14-02A, Singapore 169074, +65 8111 8900 / info@otherfurniture.com).
    Source OCR is degraded (handwritten overlay) — figures "$1,360"/"$4360" also appear as
    OCR artefacts; the Reno Sheet's clean $1,450.00 total + $450 downpayment is treated as
    authoritative per cross-reference.
    Design context: client wants the table integrated with/behind the sofa in an open
    living/dining layout (moodboard slide 9 — "Big dining table integrated to living room
    behind sofa"); first-draft render comment notes "Dining table — 180cm" (matches the
    180cm width spec).
  source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Furniture & Appliances); raw/drive/dining-table-other-furniture-2026-06-07.md"
  confidence: high

- name: TV
  room: Living-Dining
  status: ordered
  vendor: "Gain City"
  model: "Samsung 65\" The Frame LS03HE 4K Vision AI Smart TV (QA65LS03HWKXXS) + Frame Brown Bezel (VG-SCFF65BWBXY)"
  price: "$3,199.00"
  currency: SGD
  notes: |
    Status "Confirmed". Gain City Sales Order SO-B0000296814, ordered 6 Jun 2026, CASH terms,
    full $3,199.00 outstanding at order time, delivery via SUBCON-FREE DEL. Bundle includes
    1+2yr extended warranty (online register) and a -$140 Samsung VOC discount.
    DESIGN-DECISION NOTE: client review comments on the first-draft render explicitly raised
    "We're considering a 75\" TV, can we try to see how that would look like on 2nd round?"
    (page 5 comment) — but the FINAL ordered unit is 65" (per the confirmed Gain City order),
    so the 75" idea was evidently NOT adopted. Worth a human confirm — see call-out #3.
    Also came with a Gain City "Spend $100, win a BYD Denza D9" lucky-draw coupon batch
    (coupon serials ~0613601-30 / 0846641-44, qualifying period 16 Mar–16 Aug 2026, draw
    27 Aug 2026) tied to the same order/receipt no. — minor, but logged for completeness.
  source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Furniture & Appliances); raw/drive/gain-city-tv-samsung-2026-06-07.md; raw/drive/gain-city-denza-lucky-draw-2026-06-07.md; raw/drive/skyville-dawson-bud-studio-first-draft-comments-2026-06-07.md"
  confidence: high

- name: Sound Bar
  room: Living-Dining
  status: shortlisted
  vendor: ""
  model: "Sonos Beam Gen 2 (Dolby Atmos Wireless Speaker)"
  price: "$899.00"
  currency: SGD
  notes: "Listed in the Reno Sheet furniture tracker without a 'Confirmed' status flag — appears to be a planned/shortlisted purchase, not yet ordered."
  source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Furniture & Appliances)"
  confidence: medium

- name: TV Console / Storage (IKEA EKET)
  room: Living-Dining
  status: shortlisted
  vendor: "IKEA"
  model: "EKET Cabinet (35x35x70cm w/ door+shelf, x2 @ $85; 35x25x35cm, x3 @ $30) — brown walnut effect"
  price: "$260.00 (combined: $170 + $90)"
  currency: SGD
  notes: |
    Two EKET cabinet variants listed for the TV-wall storage system, neither flagged
    "Confirmed" — appears to be a planned modular storage solution for the TV wall.
    Design context: comment-page feedback proposed a custom curved-corner TV console block
    instead ("What if we custom one block on the edge, with same finishing to have a curve
    corner?") — possible conflict between the IKEA-modular Reno Sheet line item and the
    bespoke-carpentry render concept; the Bud Studio Appendix A DOES separately quote a
    custom "seated tv console" (9ft, $1,710 — Section J item 3), so these may be
    complementary or alternative solutions. Needs human disambiguation.
  source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Furniture & Appliances); raw/drive/skyville-dawson-bud-studio-first-draft-comments-2026-06-07.md (page 3)"
  confidence: low

- name: Coffee Machine
  room: Living-Dining
  status: shortlisted
  vendor: ""
  model: "Nespresso Creatista Plus"
  price: "$899.00"
  currency: SGD
  notes: "Listed in Reno Sheet tracker (Living/Dining group); also appears as an annotation on the schematic floor plan ('COFFEE MACHINE'). 'Dedicated coffee corner' was a stated design want in the moodboard (slides 9, 16)."
  source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Furniture & Appliances); raw/drive/skyville-dawson-bud-studio-first-draft-2026-06-07.md"
  confidence: medium

- name: Table Lamps (Kave Malachi + Nuvira)
  room: Living-Dining
  status: shortlisted
  vendor: "Kave"
  model: "Kave - Malachi (H22xW20xD20, $224) and Kave - Nuvira (H32.5xW27xD27, $236)"
  price: "$460.00 (combined)"
  currency: SGD
  notes: "Two table lamp models listed, neither flagged Confirmed — likely shortlisted decor."
  source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Furniture & Appliances)"
  confidence: low
```

## Proposed room note seed (Living-Dining.md)

A short room overview capturing the design brief is recommended (rather than a placeholder):

```yaml
name: Living-Dining
notes: |
  Combined Living Room + Dining Room (open-plan per the moodboard's stated preference —
  "Open space", "1 big master bedroom" tradeoffs discussed). Design principles from the
  J&M House Moodboard (slides 2, 9, 13-15):
    - Question whether a sofa is even needed (family spends more time at dining table)
    - Big dining table integrated into the living space, ideally behind/near the sofa
    - All blinds: top-mounted, floor-length, end-to-end (bigger than window OK)
    - Dedicated coffee corner
    - TV wall kept clean/minimal — "just TV and TV console in similar colour to dining"
    - Two-tone wall, floor-to-ceiling curtains, light grey carpet, dark greyish-brown
      extendable dining table with matching chairs
  Bud Studio Appendix A scope for this area: false-ceiling/partition wall at TV wall incl.
  timber TV support ($725, Section E item 2); seated TV console + settee w/ storage
  (Section J items 3-4, $1,710 + $2,235); DB-box & dry-pantry cabinetry at Entrance Foyer
  (Section J items 1-2a).
source: "raw/drive/jm-house-moodboard-2026-06-07.md; raw/drive/jm-house-moodboard-v2-2026-06-07.md; raw/sheets/reno-sheet-bud-studio-2026-06-07.md"
confidence: medium
```

## Human-judgment call-outs

1. **Room naming**: Reno Sheet groups items as "Living/Dining" — I propose folder
   `Rooms/Living-Dining/` (filesystem-safe). A human may prefer separate "Living Room" and
   "Dining Room" rooms to mirror the moodboard's room-by-room structure — but the furniture
   tracker, the Bud Studio scope, and the floor plan ("LIVING DINING" as one zone) all treat
   it as one open-plan space, so I recommend keeping it combined.
2. **Which small decor items deserve their own note vs. a room-note mention?** I included
   Sound Bar, TV Console, Coffee Machine, and Table Lamps as separate item proposals because
   the schema/note-creation pattern (`Kitchen/Induction Hob.md`) suggests per-item notes are
   the norm — but a human may reasonably judge some of these (lamps, in particular) too minor
   to warrant individual notes and prefer a single "Living/Dining decor" rollup. Flagging for
   the Compiler's discretion.
3. **Possible TV-size conflict** (75" considered in render feedback vs. 65" actually ordered)
   — flagged inline above; would make a good `04 Decisions.md` row if the human confirms the
   65" was the final call (it appears to be, since it's the CONFIRMED Gain City order, but the
   moodboard/comments don't explicitly say "we decided on 65 instead of 75").
4. Confidence is high for items with a "Confirmed" Reno-Sheet flag AND a corroborating
   purchase-order document (Dining Table, TV); medium/low for shortlisted-only items where
   the only source is a single tracker row with no order confirmation.
