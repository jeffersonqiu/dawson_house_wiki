# Proposal: Murphy Bed + Adan Desk — Fortytwo order confirmed

**Date:** 2026-06-21
**Proposed by:** Extractor (extraction-06)
**Status:** ✅ APPROVED + COMPILED (compile-03, 2026-06-21) — Murphy Bedframe.md and Working-Vanity Desk.md updated; Fortytwo vendor created.

## What to change

Source: `raw/drive/fortytwo-order-murphy-bed-adan-desk-2026-06-15.md` (Fortytwo Order #1001489322, 14 Jun 2026) + `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` (Update 2026-06-21).

Two items confirmed via a single Fortytwo purchase order:

| Item | Current compiled note | New value |
|------|----------------------|-----------|
| Murphy Bedframe (Common Bedroom) | Alegra Vertical Murphy Bed **(Natural)**, $1,899, shortlisted | Alegra Vertical Murphy Bed **(Grey)**, **$1,307.04**, **ordered** |
| Working-Vanity Desk (Master Bedroom) | Adan 1.2M Electric Adjustable Table, **$139.00**, shortlisted | Same model, **$129.96**, **ordered** |

**Actions:**
1. **UPDATE** `Dawson's wiki/wiki/Rooms/Common Bedroom/Murphy Bedframe.md` — colour (Natural → Grey), price ($1,899 → $1,307.04), status → ordered
2. **UPDATE** `Dawson's wiki/wiki/Rooms/Common Bedroom/Common Bedroom.md` — Items list entry
3. **UPDATE** `Dawson's wiki/wiki/Rooms/Master Bedroom/Working-Vanity Desk.md` — price correction ($139 → $129.96), status desk → ordered (chair was already ordered)
4. **UPDATE** `Dawson's wiki/wiki/Rooms/Master Bedroom/Master Bedroom.md` — Items list entry
5. **CREATE** `Dawson's wiki/wiki/Vendors/Fortytwo.md`

## Why / cited sources

- `raw/drive/fortytwo-order-murphy-bed-adan-desk-2026-06-15.md` — Fortytwo Order #1001489322 (14 Jun 2026): Alegra Vertical Murphy Bed (Grey) $1,307.04 + Adan 1.2M Electric Adjustable Table (Maple/White) $129.96 = $1,437.00 total. 12 months installment $119.75/month starting 15 Jun 2026. Delivery 11 Oct 2026.
- `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` (Update 2026-06-21) — both rows confirmed, matching the Fortytwo order values.

## Open questions / judgment calls

1. **Murphy Bed colour discrepancy (Natural → Grey):** The wiki and prior reno sheet both said "Natural". The Fortytwo order and the 2026-06-20 reno sheet both say "Grey". This is a real colour change — **Grey is the confirmed colour**. The wiki note should be updated clearly (not just a note in the margins; this is a definitive change).

2. **Murphy Bed price drop:** $1,899 → $1,307.04 is a $592 reduction. Likely a promotion, bundle discount, or model variant. The Fortytwo invoice is authoritative at $1,307.04. No corroboration of the old $1,899 figure beyond the earlier reno sheet.

3. **Fortytwo folder name:** The Drive folder is "09 Fortytwo - Murphy Bed & Risye's Study Desk" — "Risye's Study Desk" refers to the Adan desk (Marcella Risye's working/vanity desk in the Master Bedroom). Confirmed correct placement.

4. **Working-Vanity Desk status nuance:** The existing note has a mixed status — desk `shortlisted`, chair `ordered`. After this update, the desk is also ordered. The model field in the current note bundles desk + chair together. The Compiler may choose to split them into two records or keep them combined; the existing "combined" pattern is fine as long as the desk status is clearly updated.

5. **Delivery date 11 Oct 2026:** This is earlier than the Sleepnight bed (18 Nov 2026). Note it as a milestone — the Murphy Bed arrives first.

## Proposed records

```yaml
# UPDATE Murphy Bedframe.md:
name: Murphy Bedframe
room: Common Bedroom
status: ordered
vendor: "Fortytwo"
model: "Alegra Vertical Murphy Bed (Grey) — Queen (vertical fold)"
price: "$1,307.04"
currency: SGD
notes: |
  Colour confirmed as Grey (was listed as Natural in prior reno sheet — corrected per Fortytwo
  order). Price: $1,307.04 (was $1,899 — $592 reduction, likely a promotion). Ordered via
  Fortytwo Order #1001489322 (14 Jun 2026). Payment: 12-month installment plan, $119.75/month
  from 15 Jun 2026. Delivery: 11 October 2026. Bud Studio Appendix A Section J item 10
  ("top hung cabinet above loose murphy bed", 6 ft, $1,140) is the companion built-in carpentry.
source: "raw/drive/fortytwo-order-murphy-bed-adan-desk-2026-06-15.md; raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Update 2026-06-21)"
confidence: high

# UPDATE Working-Vanity Desk.md (desk portion only — chair already ordered):
name: Working-Vanity Desk
room: Master Bedroom
status: ordered
vendor: "Fortytwo"
model: "Adan 1.2M Electric Adjustable Table (Maple/White, table top 120x60cm, legs adjustable H75-110cm) + Kave Einara chair (H84xW59xD60, $275.40, ordered via Kave order S04948)"
price: "$129.96 (desk, ordered) + $275.40 (chair, ordered)"
currency: SGD
notes: |
  Desk price corrected from $139.00 to $129.96 per Fortytwo Order #1001489322 (14 Jun 2026).
  Both desk and chair are now ordered. Desk ordered same order as Murphy Bed (Common Bedroom).
  Delivery: 11 October 2026. Vanity/study desk 1m width was approved in design review (see
  04 Decisions) — Adan's 120cm top satisfies this.
source: "raw/drive/fortytwo-order-murphy-bed-adan-desk-2026-06-15.md; raw/drive/kave-order-s04948-2026-06-13.md; raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Update 2026-06-21)"
confidence: high

# CREATE Fortytwo Vendor.md:
name: Fortytwo
type: supplier
contact: ""
location: ""
notes: |
  Online furniture retailer. Order #1001489322 (14 Jun 2026): Alegra Vertical Murphy Bed (Grey)
  $1,307.04 + Adan 1.2M Electric Adjustable Table (Maple/White) $129.96. Grand total $1,437.00;
  12-month installment plan at $119.75/month starting 15 Jun 2026. Delivery: 11 Oct 2026,
  12pm–3pm.
related_items: ["Murphy Bedframe", "Working-Vanity Desk"]
source: "raw/drive/fortytwo-order-murphy-bed-adan-desk-2026-06-15.md"
confidence: high
```
