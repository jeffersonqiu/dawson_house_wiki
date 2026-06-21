# Proposal: Curtains — Secret Furnishing DANI collection confirmed

**Date:** 2026-06-21
**Proposed by:** Extractor (extraction-06)
**Status:** ✅ APPROVED + COMPILED (compile-03, 2026-06-21) — Curtains.md created under Whole House; Secret Furnishing vendor created.

## What to change

Sources: `raw/drive/secret-furnishing-curtains-vt70917-2026-06-20.md` (Tax Invoice VT70917, 20 Jun 2026) + `raw/drive/secret-furnishing-curtains-colors-2026-06-20.md` (fabric specs) + `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` (Update 2026-06-21).

A whole-house curtains purchase is now confirmed with a tax invoice and $500 deposit paid.

**Actions:**
1. **CREATE** `Dawson's wiki/wiki/Rooms/Whole House/Curtains.md` — new item note (see note on placement below)
2. **UPDATE** `Dawson's wiki/wiki/Rooms/Whole House/Whole House.md` — add Curtains to Items
3. **CREATE** `Dawson's wiki/wiki/Vendors/Secret Furnishing.md`
4. **NOTE for Kitchen.md and affected room notes:** The prior "Day Curtain LACE RL040" ($263.40 × 6 = some rooms) placeholder is now superseded by this confirmed purchase. The "Night Curtain $0" placeholder rows are similarly superseded. Update if applicable.

## Why / cited sources

- `raw/drive/secret-furnishing-curtains-vt70917-2026-06-20.md` — Tax Invoice VT70917 (20 Jun 2026). GST Reg 201910468R. Customer: Marcella Risye. DANI-21 Earth (day curtain) + DANI-22 Rattan (night curtain), 4-room flat. Total $1,840; deposit $500 (Amex); balance due after measurement. Measurement: 16 Oct 2026; Installation: 16 Nov 2026. Salesperson: Jia Jia, 84481455.
- `raw/drive/secret-furnishing-curtains-colors-2026-06-20.md` — DANI fabric specs: 100% Polyester, 230 gsm, Dimout, Light Fastness 4–5, Martindale 20,000 rubs.
- `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` (Update 2026-06-21) — "Curtains (Day & Night, all applicable rooms): Secret Furnishing DANI collection, $1,840, Confirmed, $500 deposit".

## Open questions / judgment calls

1. **Placement — Whole House vs. per-room notes:** Curtains apply to all applicable rooms. Per extractor.md gotcha #6, there is no standard "whole-house" item category. The [[Whole House]] pseudo-room already exists (see Aircon.md). Proposing to place Curtains.md under `Rooms/Whole House/` — consistent with Aircon precedent. If the Compiler prefers per-room curtain notes (one per bedroom + living/dining), that's also reasonable but would be more granular than the invoice supports (single invoice for whole flat). **Human: Whole House or per-room?**

2. **Key milestone dates:** Measurement 16 Oct 2026 and Installation 16 Nov 2026 are important project milestones (curtains come very late, after reno). Should a TASK be created for these? Or is it sufficient to document them in the Curtains note?

3. **Balance amount:** $1,840 − $500 deposit = $1,340 estimated balance, but invoice says "balance after measurement" — could change slightly after measurement. Document as "~$1,340" with a note.

4. **DANI-21 Earth = Day curtain; DANI-22 Rattan = Night curtain:** Both are Dimout fabrics (not blackout). This is a design choice — Dimout provides partial light control. If the human expected blackout curtains for the Master Bedroom, flag this.

5. **"Day Curtain LACE RL040" placeholder:** The reno sheet previously had "Day Curtain LACE RL040, $43.90 × 6 = $263.40" across all rooms. This is now fully superseded by the Secret Furnishing invoice. The room notes that mention it (if any) should have the reference removed.

## Proposed records

```yaml
# CREATE Curtains.md (under Whole House):
name: Curtains (Day & Night)
room: Whole House
status: ordered
vendor: "Secret Furnishing"
model: "DANI collection — DANI-21 Earth (day/dimout) + DANI-22 Rattan (night/dimout). 100% Polyester, 230 gsm, Dimout, LF 4–5, Martindale 20,000 rubs."
price: "$1,840.00"
currency: SGD
notes: |
  Whole-flat curtains package: day + night, all applicable rooms in the 4-room flat.
  Tax Invoice VT70917 (20 Jun 2026). Deposit: $500 (Amex). Balance: ~$1,340 (confirmed after
  measurement on 16 Oct 2026). Installation: 16 Nov 2026. Salesperson: Jia Jia, 84481455.
  Supersedes the prior "Day Curtain LACE RL040" ($263.40) placeholder and all "Night Curtain
  $0" placeholders in the reno sheet tracker.
  DANI-21 Earth: day curtain (lighter dimout, allows some natural light).
  DANI-22 Rattan: night curtain (heavier dimout, provides more privacy/light control).
source: "raw/drive/secret-furnishing-curtains-vt70917-2026-06-20.md; raw/drive/secret-furnishing-curtains-colors-2026-06-20.md; raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Update 2026-06-21)"
confidence: high

# CREATE Secret Furnishing Vendor.md:
name: Secret Furnishing
type: supplier
contact: "Jia Jia — 84481455"
location: ""
notes: |
  GST Reg: 201910468R. Curtains vendor for whole-flat DANI collection. Tax Invoice VT70917
  (20 Jun 2026). Total $1,840; deposit $500 (Amex); balance ~$1,340 due after measurement.
  Key dates: Measurement 16 Oct 2026; Installation 16 Nov 2026.
related_items: ["Curtains (Day & Night)"]
source: "raw/drive/secret-furnishing-curtains-vt70917-2026-06-20.md"
confidence: high
```
