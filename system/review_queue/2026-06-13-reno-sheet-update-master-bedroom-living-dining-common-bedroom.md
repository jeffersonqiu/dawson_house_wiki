# Proposal: Reno Sheet 2026-06-12 update — desk/chair swap, table lamp consolidation, new Smart Lock, Ironing Set price check

**Date:** 2026-06-13
**Proposed by:** Extractor
**Status:** awaiting human approval

## What to change

Update 3 existing item notes (price/vendor/status changes — review-queue gate applies) and
create 1 new item note, all driven by the "02 Reno Sheet x Bud Studio" tracker re-pull on
2026-06-12/13 (see `system/runs/2026-06-13-ingestion-03.md`):

1. **UPDATE** `Dawson's wiki/wiki/Rooms/Master Bedroom/Working-Vanity Desk.md`
   - Desk: "Interdesk Classic" $399.00 → **"Adan 1.2M Electric Adjustable Table" $139.00**
   - Chair: "Kave Lexa Swivel Chair" $300.00 → **"Kave Einara" $275.40**, status → confirmed/ordered
     (paid order S04948, "Incoming, End June")
2. **UPDATE** `Dawson's wiki/wiki/Rooms/Living-Dining/Table Lamps (Kave).md`
   - Drop the "Nuvira" lamp (no longer in the tracker); keep only **"Kave - Malachi" $190.40**
     (was $224.00), status → confirmed/ordered (same order S04948, "In Stock", delivery 30/09/26)
   - Rename note from "Table Lamps (Kave Malachi + Nuvira)" to **"Table Lamp (Kave Malachi)"**
3. **UPDATE** `Dawson's wiki/wiki/Rooms/Common Bedroom/Ironing Set.md`
   - Price discrepancy: compiled note says $739.00; current tracker pull says $599.00. Recommend
     adopting **$599.00** as current (tracker is the live source of truth and this is the
     post-2026-06-12 pull), but flag as `confidence: low` until corroborated — the discrepancy
     wasn't marked "NEWLY EDITED" so it's unclear if intentional.
4. **CREATE** `Dawson's wiki/wiki/Rooms/Living-Dining/Smart Lock.md` (new item, new row in
   tracker as of 2026-06-12)

Trigger for #4: "Real item to track" per `note-creation.md` — new row in the authoritative
Reno Sheet tracker with brand/model/price, grouped under Living/Dining.

## Why / cited sources

- `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` — "Furniture & Appliances (current, as of
  2026-06-12)" table (re-pulled 2026-06-13) is now the authoritative version; old table marked
  SUPERSEDED but kept for audit.
- `raw/drive/kave-order-s04948-2026-06-13.md` — Kave Home Order # S04948 (12/06/2026), corroborates
  the chair (Einara, "Incoming, End June") and lamp (Malachi, "In Stock", delivery 30/09/26) as
  paid/Confirmed. Down payment $427.34 paid against a $465.80 total.
- `system/runs/2026-06-13-ingestion-03.md` — ingestion diff summary and follow-up list.

## Open questions / judgment calls

1. **Working/Vanity Desk — is the Adan table a genuine swap or a data-entry slip?** $399→$139
   and a completely different brand/model is a big jump, but it's listed alongside the
   newly-Confirmed chair in the same edit pass. I'm treating it as a deliberate swap (the
   1m-width decision in `04 Decisions.md` references the *width* of the desk, not the brand —
   the Adan table top is 120cm W which still satisfies "~1m ok", arguably even closer). Desk
   itself is NOT marked "Confirmed" in the tracker (only the chair is) — recommend keeping desk
   status as `shortlisted`, chair as `ordered`. **Human: please confirm the desk swap is real**
   before I finalize — if it's a typo, the old Interdesk Classic $399 entry should be restored
   instead.
2. **Table Lamp — Nuvira dropped or just consolidated in the tracker?** The new tracker row is
   singular ("Table Lamp", not "Table Lamps") and only lists Malachi. I'm proposing to drop
   Nuvira from the compiled note rather than keep it as a second shortlisted item, but if you
   still want the Nuvira lamp, it should probably get its own note re-added later.
3. **Ironing Set price** — see #3 above. Proposing $599.00 with low confidence; if you have
   the actual Philips AIS8540/80 retail price handy, that would resolve it definitively.
4. **Smart Lock** — no independent corroboration beyond the tracker row (no order/invoice yet).
   Proposing `status: researching`, `confidence: low`.

## Proposed records

```yaml
- name: Working-Vanity Desk
  room: Master Bedroom
  status: shortlisted   # desk only — not marked Confirmed in tracker
  vendor: ""
  model: "Adan 1.2M Electric Adjustable Table (table top 120x60cm, legs adjustable H75-110cm) + Kave Einara chair (H84xW59xD60, $275.40, ordered via Kave order S04948)"
  price: "$139.00 (desk, shortlisted) + $275.40 (chair, ordered)"
  currency: SGD
  notes: |
    SUPERSEDES the previous "Interdesk Classic $399 + Kave Lexa $300" record (compiled
    2026-06-08). Reno Sheet re-pull 2026-06-12 shows desk swapped to Adan 1.2M Electric
    Adjustable Table ($139, not yet Confirmed) and chair swapped to Kave Einara ($275.40,
    now Confirmed/ordered per Kave Order S04948 dated 12/06/2026 — "Incoming, End June").
    The 1m-width decision in 04 Decisions.md (render-comment page 16, "Study / vanity table -
    actually 1m is ok!") is still satisfied by the Adan table's 120cm top width.
  source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Furniture & Appliances, current as of 2026-06-12); raw/drive/kave-order-s04948-2026-06-13.md"
  confidence: medium

- name: Table Lamp (Kave Malachi)
  room: Living-Dining
  status: ordered
  vendor: "Kave"
  model: "Kave - Malachi (H22 x W20 x D20)"
  price: "$190.40"
  currency: SGD
  notes: |
    RENAMES/REPLACES "Table Lamps (Kave Malachi + Nuvira)" (compiled 2026-06-08, $460 combined,
    confidence low). Reno Sheet re-pull 2026-06-12 shows a single consolidated "Table Lamp" row
    — only Malachi remains, price $190.40 (was $224.00), now marked Confirmed via Kave Order
    S04948 (12/06/2026, "In Stock", delivery with installation scheduled 30/09/26). The Nuvira
    lamp ($236.00) no longer appears in the tracker — treated as dropped.
  source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Furniture & Appliances, current as of 2026-06-12); raw/drive/kave-order-s04948-2026-06-13.md"
  confidence: high

- name: Ironing Set
  room: Common Bedroom
  status: shortlisted
  vendor: ""
  model: "Philips AIS8540/80 All-in-One 8500 Series (W39.2 x H60.2 x D597)"
  price: "$599.00"
  currency: SGD
  notes: |
    Price discrepancy vs. previously compiled $739.00 (2026-06-08). Current Reno Sheet pull
    (2026-06-12/13) shows $599.00 for the same product/dimensions. Not marked "NEWLY EDITED" in
    the tracker's edit-tracking column, so unclear whether this is a genuine price update or an
    OCR/read variance between pulls. Recommend adopting $599.00 as current best-available figure
    but keeping confidence low pending corroboration (e.g. checking the Philips/Courts listing
    price directly).
  source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Furniture & Appliances, current as of 2026-06-12)"
  confidence: low

- name: Smart Lock
  room: Living-Dining
  status: researching
  vendor: ""
  model: "Best D Digital Door Lock BDL-5000"
  price: "$388.00"
  currency: SGD
  notes: |
    NEW row in the Reno Sheet tracker as of 2026-06-12, grouped under Living/Dining (likely the
    main entrance door). No Confirmed marker, no independent order/invoice yet.
  source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Furniture & Appliances, current as of 2026-06-12)"
  confidence: low
```

---
*Extraction run: 2026-06-13. Source: `/ingest` change-check (`system/runs/2026-06-13-ingestion-03.md`)
re-pulled `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` and added
`raw/drive/kave-order-s04948-2026-06-13.md`.*
