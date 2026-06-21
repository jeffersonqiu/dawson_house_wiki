# Proposal: Study Desk (Common Bedroom) — Interdesk Ultra confirmed, open question resolved

**Date:** 2026-06-21
**Proposed by:** Extractor (extraction-06)
**Status:** ✅ APPROVED + COMPILED (compile-03, 2026-06-21) — Study Desk.md created; B.S. Furniture vendor created.

## What to change

Sources: `raw/drive/interdesk-sales-receipt-h3037-2026-06-20.md` (B.S. Furniture Sales H#3037, 20 Jun 2026) + `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` (Update 2026-06-21).

The Interdesk Ultra desk is now a confirmed purchase. The "which room" open question from extraction-04 is resolved by the Drive folder name ("11 Interdesk - Study Table Common Bedroom") and the receipt billed to Jefferson Qiu.

**Actions:**
1. **CREATE** `Dawson's wiki/wiki/Rooms/Common Bedroom/Study Desk.md`
2. **UPDATE** `Dawson's wiki/wiki/Rooms/Common Bedroom/Common Bedroom.md` — add Study Desk to Items
3. **CREATE** `Dawson's wiki/wiki/Vendors/B.S. Furniture.md`
4. **SUPERSEDE** extraction-04 proposal `system/review_queue/2026-06-20-second-room-desk-research.md` — that proposal had status `researching` with the room open question unresolved; this extraction-06 proposal uses the confirmed data

## Why / cited sources

- `raw/drive/interdesk-sales-receipt-h3037-2026-06-20.md` — B.S. Furniture Pte Ltd, Sales H#3037 (20 Jun 2026). Bill to: Jefferson Qiu, 86 Dawson Road #05-03. Items: Ultra Table Top 1400×700×25mm Walnut ($599) + Ultra Frame Black ($0) + Assembly ($50) = $649 total, fully paid. Drive folder name: "11 Interdesk - Study Table Common Bedroom" — unambiguous room assignment.
- `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` (Update 2026-06-21) — row reads "Study Desk (Jeff) | Common Bedroom | Interdesk Ultra 140×70cm Walnut, Dual Motor electric height-adjustable | $649.00 | Confirmed, fully paid".

## Open questions / judgment calls

1. **Moodboard "Built-in study table" implication:** The Common Bedroom design intent (moodboard slides 26–27) specifies a "Built-in study table, 1.4–1.6 m" — this was expected to be Bud Studio carpentry. The Interdesk Ultra (140cm = 1.4m) is a **freestanding, purchased desk**, not a built-in. If a built-in desk was in the Bud Studio Appendix A scope, this purchase could be replacing it — which may mean a **Change Order is needed to remove that carpentry line item**. Human: was the built-in study table removed from Bud Studio's scope? If so, has a VO been issued? (The reno sheet's draft VO shows Section J reduction from $26,595→$22,045 — this could partly explain that reduction.)

2. **Adan desk folder name note:** The Fortytwo folder ("09 Fortytwo - Murphy Bed & Risye's Study Desk") calls the Adan desk "Risye's Study Desk" — but that desk is the Master Bedroom working/vanity desk for Marcella (Risye). The Interdesk Ultra is Jeff's study desk for the Common Bedroom. Two different desks for two different people. Do not confuse them.

3. **Assembly fee ($50):** The $649 receipt total includes $50 assembly. The reno sheet records $649 as the item price. No split needed — $649 is the all-in delivered-and-assembled price.

## Proposed records

```yaml
# CREATE Study Desk.md:
name: Study Desk (Jeff)
room: Common Bedroom
status: ordered
vendor: "B.S. Furniture"
model: "Interdesk Ultra — Table Top 1400×700×25mm Walnut + Ultra Frame Black, electric height-adjustable (Dual Motor, 3 Stages)"
price: "$649.00"
currency: SGD
notes: |
  Jeff's study desk for the Common Bedroom. Fully paid (B.S. Furniture Sales H#3037, 20 Jun
  2026): tabletop $599 + assembly $50 = $649. Ultra Frame Black included at $0 (bundled with
  top). Electrically height-adjustable: Dual Motor, 3 Stages. Walnut finish, 140cm wide.
  NOTE: the Common Bedroom moodboard called for a "built-in study table 1.4–1.6m" (Bud Studio
  carpentry). This freestanding desk may replace that built-in scope — check whether a Change
  Order is needed to remove that carpentry line item from the Bud Studio contract.
source: "raw/drive/interdesk-sales-receipt-h3037-2026-06-20.md; raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Update 2026-06-21)"
confidence: high

# CREATE B.S. Furniture Vendor.md:
name: B.S. Furniture
type: supplier
contact: ""
location: ""
notes: |
  Company Reg: 202523442D. Vendor for Common Bedroom Study Desk (Interdesk Ultra). Sales
  Receipt H#3037 (20 Jun 2026). Bill to Jefferson Qiu. Fully paid at purchase ($649).
related_items: ["Study Desk (Jeff)"]
source: "raw/drive/interdesk-sales-receipt-h3037-2026-06-20.md"
confidence: high
```
