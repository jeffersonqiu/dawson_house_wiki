# Proposal: New items — Settee upholstery, Headboard upholstery, Queen mattress, WC price, draft VO task

**Date:** 2026-06-21
**Proposed by:** Extractor (extraction-06)
**Status:** ✅ APPROVED + COMPILED (compile-03, 2026-06-21) — Settee Cushion + Upholstery.md, Headboard Cushion + Upholstery.md, Queen Size Mattress.md created; TASK-0015 created; WC price noted in bathroom room notes.

## What to change

Source: `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` (Update 2026-06-21).

Five related items from the 2026-06-20 reno sheet update — grouped together because they're all smaller/simpler records vs. the major purchase proposals above.

**Actions:**
1. **CREATE** `Dawson's wiki/wiki/Rooms/Living-Dining/Settee Cushion + Upholstery.md`
2. **CREATE** `Dawson's wiki/wiki/Rooms/Master Bedroom/Headboard Cushion + Upholstery.md`
3. **CREATE** `Dawson's wiki/wiki/Rooms/Common Bedroom/Queen Size Mattress.md`
4. **FLAG** WC price update ($799×2) — see open question #4 below; no notes file to UPDATE yet (WC has no compiled item note, just $0 placeholder in bathroom room notes)
5. **CREATE** `Dawson's wiki/wiki/Tasks/TASK-0015 - Track draft Variation Order (Section J + D reductions).md`
6. **UPDATE** `Dawson's wiki/wiki/Rooms/Living-Dining/Living-Dining.md` — add Settee Cushion + Upholstery to Items
7. **UPDATE** `Dawson's wiki/wiki/Rooms/Master Bedroom/Master Bedroom.md` — add Headboard Cushion + Upholstery to Items
8. **UPDATE** `Dawson's wiki/wiki/Rooms/Common Bedroom/Common Bedroom.md` — add Queen Size Mattress to Items

## Why / cited sources

All from `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` (Update 2026-06-21 — reno sheet as of 2026-06-20):

- **Settee Cushion & Upholstery:** "Settee Cushion & Upholstery | Living/Dining | bycoesa.com | $950.00 | 1 | $950.00" — new row in 2026-06-20 reno sheet. The "settee" is the Bud Studio carpentry unit (Section J item 4: "Settee c/w half ht storage", $2,235). bycoesa.com is a Singapore upholstery vendor.

- **Headboard Cushion & Upholstery:** "Headboard Cushion & Upholstery | Master Bedroom | bycoesa.com | $950.00 | 1 | $950.00" — also new. Distinct from the Bud Studio "one-sided headboard" (Appendix A Section J item 14, $1,225) — that is built-in carpentry. This $950 upholstery is the fabric/cushion element that goes ON the built-in frame.

- **Queen Size Mattress (Common Bedroom):** "Queen Size Mattress | Common Bedroom | Downtime Mattress - Queen | W152 x D190 x H20.5 | $0 | 1 | $0 | from current house, fully paid" — a $0 item (the mattress is being brought from their current home). No purchase needed.

- **WC price:** "WC | Master Bathroom | (model TBD) | $799.00 | 1 | $799.00" and "WC | Common Bathroom | (model TBD) | $799.00 | 1 | $799.00" — price now populated at $799 each (was $0 placeholder). No model specified yet. No purchase invoice found.

- **Draft VO:** The 2026-06-20 reno sheet contains a second "commented" summary showing: Section J (Carpentry) $26,595 → $22,045 (−$4,550) and Section D (Masonry & Wet Works) $12,080 → $11,690 (−$390). This appears to be a draft Variation Order being prepared with Bud Studio — not yet signed.

## Open questions / judgment calls

1. **Settee/Headboard upholstery status:** Neither row is marked "Confirmed" in the reno sheet. No purchase invoice found. Both are listed at $950 from bycoesa.com. Proposing `status: shortlisted` with `confidence: medium`. **Human: has bycoesa.com been engaged/paid for either of these yet?**

2. **Settee upholstery placement — is this for the banquette/settee bench in the Living-Dining?** Bud Studio's "Settee c/w half ht storage" (Section J item 4, $2,235) is a built-in seating unit in the Living/Dining room. The bycoesa.com upholstery would be the fabric cushioning for it. This distinction should be noted in the item note.

3. **Headboard upholstery vs. Bud Studio headboard:** Bud Studio Appendix A Section J item 14 is a "one-sided headboard" for the Master Bedroom ($1,225, height 800mm). The bycoesa.com $950 "Headboard Cushion & Upholstery" is the fabric/cushion layer on top of that carpentry structure. Both items exist (the carpentry headboard from Bud + the fabric upholstery from bycoesa). The note should clearly document this distinction.

4. **WC — no item notes yet, $799 price populated:** Currently, both Master Bathroom and Common Bathroom room notes have WC as $0 placeholder content only (no item note compiled). Since no model is confirmed, I'm NOT proposing to create WC item notes yet — instead noting the price ($799 each) in this proposal for the Compiler to add to the relevant bathroom room notes as a factual update. **Human: is there a specific WC model chosen, or is $799 a budget figure?**

5. **Draft VO — Section J −$4,550 and Section D −$390:** The Section J reduction ($26,595 → $22,045) could reflect removal of the built-in study table in the Common Bedroom (now replaced by the freestanding Interdesk), or other carpentry scope reductions. Section D reduction ($390) is minor and likely a layout change. This is NOT a confirmed Change Order — it's a draft. TASK-0015 is created to track it.

## Proposed records

```yaml
# CREATE Settee Cushion + Upholstery.md (Living-Dining):
name: Settee Cushion + Upholstery
room: Living-Dining
status: shortlisted
vendor: "bycoesa.com"
model: ""
price: "$950.00"
currency: SGD
notes: |
  Fabric cushion + upholstery for the Bud Studio built-in settee (Section J item 4: "Settee
  c/w half ht storage", $2,235 — the carpentry shell is Bud Studio's scope). The $950 covers
  the fabric/upholstery to be fitted onto the carpentry bench. No purchase invoice found; vendor
  is bycoesa.com (Singapore upholstery). Status shortlisted until purchase confirmed.
source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Update 2026-06-21)"
confidence: medium

# CREATE Headboard Cushion + Upholstery.md (Master Bedroom):
name: Headboard Cushion + Upholstery
room: Master Bedroom
status: shortlisted
vendor: "bycoesa.com"
model: ""
price: "$950.00"
currency: SGD
notes: |
  Fabric cushion + upholstery for the Master Bedroom headboard. The built-in carpentry headboard
  is Bud Studio Appendix A Section J item 14 ("one-sided headboard", 35 sqft, $1,225, H800mm) —
  the $950 from bycoesa.com is the fabric/upholstery layer on top of that structure. No purchase
  invoice found. Status shortlisted until purchase confirmed.
source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Update 2026-06-21)"
confidence: medium

# CREATE Queen Size Mattress.md (Common Bedroom):
name: Queen Size Mattress
room: Common Bedroom
status: n/a
vendor: "Downtime"
model: "Downtime Mattress — Queen (W152 x D190 x H20.5)"
price: "$0.00"
currency: SGD
notes: |
  Bringing this mattress from the current house — fully paid, no new purchase needed.
  Status n/a (resolved — no action required). Sized for queen bed (matches Murphy Bed or a
  standard queen frame when Murphy Bed is folded up).
source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Update 2026-06-21)"
confidence: high

# CREATE TASK-0015:
id: TASK-0015
title: "Track draft Variation Order — Section J (Carpentry) and Section D (Masonry) reductions"
status: open
area: Whole House
due: ""
owner: jeff
notes: |
  The 2026-06-20 reno sheet contains a draft/commented VO showing two scope reductions vs. the
  signed contract (2026-06-07):
  - Section J (Carpentry Works): $26,595 → $22,045 (reduction of $4,550)
  - Section D (Masonry & Wet Works): $12,080 → $11,690 (reduction of $390)
  These are NOT yet signed — the main summary table in the reno sheet still shows the original
  figures. Actions needed: (1) confirm the scope changes with Bud Studio, (2) get a signed
  Variation Order, (3) update the contract sum in the wiki once the VO is signed.
  The Section J reduction may relate to removal of the built-in study table from the Common
  Bedroom carpentry scope (replaced by the freestanding Interdesk desk — see Study Desk note).
related: ["Dawson's wiki/wiki/Vendors/Bud Studio.md", "Dawson's wiki/wiki/Rooms/Common Bedroom/Study Desk.md"]
source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Update 2026-06-21)"
confidence: medium
```
