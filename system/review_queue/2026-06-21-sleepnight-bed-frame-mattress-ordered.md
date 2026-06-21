# Proposal: Bed Frame + Mattress — Sleepnight confirmed, Dunlopillo dropped

**Date:** 2026-06-21
**Proposed by:** Extractor (extraction-06)
**Status:** ✅ APPROVED + COMPILED (compile-03, 2026-06-21) — Bed Frame + Mattress.md replaced; Lux Grandeur vendor created.

## What to change

Sources: `raw/drive/sleepnight-bed-frame-mattress-ltb100594-2026-06-14.md` (Lux Grandeur Invoice LTB 100594, 14 Jun 2026) + `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` (Update 2026-06-21) + `system/review_queue/2026-06-19-sleepnight-payment-and-swatches.md` (extraction-05, awaiting approval).

The Dunlopillo King Size Storage Drawer Bed Frame ($2,039, shortlisted) has been replaced by a confirmed Sleepnight purchase. A purchase invoice exists AND the remaining balance has been paid (per the extraction-05 proposal).

**Actions:**
1. **UPDATE** `Dawson's wiki/wiki/Rooms/Master Bedroom/Bed Frame + Mattress.md` — complete product replacement, status → ordered
2. **UPDATE** `Dawson's wiki/wiki/Rooms/Master Bedroom/Master Bedroom.md` — Items list entry
3. **CREATE** `Dawson's wiki/wiki/Vendors/Lux Grandeur (Sleepnight).md`
4. **SUPERSEDE** extraction-04 proposal `system/review_queue/2026-06-20-sleepnight-bed-frame-research.md` — that proposal added Sleepnight as a "researching" alternative; the product is now confirmed/ordered

## Why / cited sources

- `raw/drive/sleepnight-bed-frame-mattress-ltb100594-2026-06-14.md` — Lux Grandeur Invoice LTB 100594 (14 Jun 2026): Sleepnight "Blissful sleep 10" Kingsize Mattress (Crest Collection 10") + Kingsize Storage Drawer Bedframe (no headboard, internal 114, Wego Brown WG 003 fabric). Total $2,619, deposit $1,319 paid. Delivery 18 Nov 2026.
- `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` (Update 2026-06-21) — row reads: Sleepnight "Blissful sleep 10" Kingsize, $2,619, Confirmed, $1,319 deposit paid, delivery 18-11-26.
- `system/review_queue/2026-06-19-sleepnight-payment-and-swatches.md` (extraction-05) — the remaining payment was made (SPayLater, $1,300 balance). That proposal should also be compiled to update status → ordered and add payment context.

**Corroboration chain:** Invoice + reno sheet + payment receipt = three independent confirmations. Confidence: high.

## Open questions / judgment calls

1. **Fabric swatches from extraction-05:** The extraction-05 proposal `2026-06-19-sleepnight-payment-and-swatches.md` also contains an uncontextualised fabric swatch item (MYSTIC 07, STAN FR) that was photographed the same day as the payment. That swatch is held at low confidence in the extraction-05 proposal — compile it or not separately. It does NOT affect the Bed Frame + Mattress record here.

2. **No headboard included:** The invoice explicitly says "no headboard". Bud Studio's Appendix A Section J item 14 includes a "one-sided headboard" ($1,225, height 800mm) — this is a BUILT-IN headboard by Bud Studio, separate from the bed frame purchase. The note should clarify this distinction.

3. **Moodboard "soft bed frame" / "3 layers" concept:** The current Bed Frame + Mattress note raises the question of whether the Dunlopillo's storage-drawer style satisfies the moodboard's "soft bed frame, 3 layers" concept (slides 22-23). The Sleepnight Blissful also has a storage drawer. The fabric-upholstered Wego Brown WG 003 frame does satisfy the "soft" aesthetic better. The "3 layers / hidden light" moodboard concept remains an aspirational note — not a blocker.

4. **Extraction-04 proposal coordination:** The extraction-04 proposal `2026-06-20-sleepnight-bed-frame-research.md` was approved by the user ("Yes all approved") but proposed only ADDING an "in-store research" section and changing status to `researching`. This extraction-06 proposal goes further (complete product replacement, status `ordered`). The Compiler should use this extraction-06 proposal instead of the extraction-04 one.

## Proposed records

```yaml
# UPDATE Bed Frame + Mattress.md:
name: Bed Frame + Mattress
room: Master Bedroom
status: ordered
vendor: "Lux Grandeur (Sleepnight)"
model: "Sleepnight 'Blissful sleep 10' Kingsize Mattress (Crest Collection 10\") + Kingsize Storage Drawer Bedframe (no headboard, internal 114, Wego Brown WG 003 fabric)"
price: "$2,619.00"
currency: SGD
notes: |
  Replaces the previously-shortlisted Dunlopillo King Size Storage Drawer Bed Frame ($2,039).
  Mattress: Sleepnight 'Blissful sleep 10' (Crest Collection 10-inch), King size.
  Bedframe: Storage drawer style, upholstered in Wego Brown WG 003 (INNOVATEX New Wego range),
  no headboard (the built-in headboard is Bud Studio Appendix A Section J item 14 — separate).
  Internal dimension 114 = clearance/frame internal width.
  Deposit: $1,319 paid (Jun 2026). Remaining: $1,300, paid via SPayLater (see extraction-05
  proposal 2026-06-19-sleepnight-payment-and-swatches.md).
  Delivery: 18 November 2026.
  Warranties: 12-year mattress; lifetime gas spring (bedframe).
  Purchased at Tan Boon Liat Building (Lux Grandeur Pte Ltd, GST Reg 201117925K).
source: "raw/drive/sleepnight-bed-frame-mattress-ltb100594-2026-06-14.md; raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Update 2026-06-21); system/review_queue/2026-06-19-sleepnight-payment-and-swatches.md"
confidence: high

# CREATE Lux Grandeur (Sleepnight) Vendor.md:
name: Lux Grandeur (Sleepnight)
type: supplier
contact: ""
location: "315 Outram Rd #03-04/05 Tan Boon Liat Building"
notes: |
  GST Reg: 201117925K. Trades as Sleepnight / Sleepy Night. Vendor for Master Bedroom Bed Frame
  + Mattress. Invoice LTB 100594 (14 Jun 2026). Total $2,619; deposit $1,319; balance $1,300
  (paid via SPayLater). Delivery 18 Nov 2026. Warranties: 12yr mattress, lifetime gas spring.
related_items: ["Bed Frame + Mattress"]
source: "raw/drive/sleepnight-bed-frame-mattress-ltb100594-2026-06-14.md"
confidence: high
```
