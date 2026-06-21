# Proposal: Kitchen appliances — Hob, Hood, Oven confirmed (GRH Logistics SS-S017303)

**Date:** 2026-06-21
**Proposed by:** Extractor (extraction-06)
**Status:** ✅ APPROVED + COMPILED (compile-03, 2026-06-21) — Hob, Hood, Oven updated; GRH Logistics vendor created; TASK-0006 closed.

## What to change

Source: `raw/drive/grh-hoekee-hob-hood-oven-2026-06-14.md` (GRH Logistics Sales Order SS-S017303, 14 Jun 2026) + `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` (Update 2026-06-21).

All three kitchen appliances are now confirmed via a corroborating purchase order. Two have significant product/price changes:

| Item | Current compiled note | New value |
|------|----------------------|-----------|
| Hob | Bosch PUE611BB5J $1,159 shortlisted | **Bertazzoni P603I30NV** $916 **ordered** — brand change |
| Hood | Bosch DWBM98G50B $799 shortlisted | **Bosch DWB97CM50B** $1,179 **ordered** — model change, +$380 |
| Oven | Bosch HHF113BR0B 71L $849 shortlisted | **Bosch HHF113BR0B 66L** $749 **ordered** — price −$100, capacity corrected |

**Actions:**
1. **UPDATE** `Dawson's wiki/wiki/Rooms/Kitchen/Hob.md`
2. **UPDATE** `Dawson's wiki/wiki/Rooms/Kitchen/Hood.md`
3. **UPDATE** `Dawson's wiki/wiki/Rooms/Kitchen/Oven.md`
4. **UPDATE** `Dawson's wiki/wiki/Rooms/Kitchen/Kitchen.md` — Items list values
5. **CREATE** `Dawson's wiki/wiki/Vendors/GRH Logistics.md`

## Why / cited sources

- `raw/drive/grh-hoekee-hob-hood-oven-2026-06-14.md` — GRH Logistics Sales Order SS-S017303, 14 Jun 2026. All three items listed in a single bundle. $2,850 total, $550 deposit paid (PayNow D010535). This corroborating purchase document justifies upgrading status to `ordered`.
- `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` (Update 2026-06-21) — all three rows listed as "Confirmed" in the 2026-06-20 reno sheet, matching the GRH invoice items.

**Pricing note:** GRH SO gives only a bundle total ($2,850); reno sheet supplies individual prices: Hood $1,179 + Hob $916 + Oven $749 = $2,844 (vs. $2,850 — $6 gap, likely rounding or a minor accessory charge). Individual prices from reno sheet; SO is the corroborating purchase document.

## Open questions / judgment calls

1. **TASK-0006 status:** "Finalise kitchen stove-sink-oven-hood layout" — the confirmed purchase of these three appliances implies the layout was finalised. But the GRH SO doesn't specify placement. Human: is TASK-0006 now done, and if so, what is the final layout (stove/sink relative position)?

2. **Mayer MCS5P Pot Set (FOC):** The GRH SO includes a free 5-piece Mayer pot set. No tracking needed, but worth a brief note in the Hob/Hood notes as it's a useful cross-reference.

3. **Hood model change significance:** DWB97CM50B is a different Bosch model from DWBM98G50B — likely a newer/different spec (different width/suction). The price increase ($799→$1,179) suggests an upgrade. No action needed from human unless they recall choosing a specific model — the GRH invoice is authoritative.

## Proposed records

```yaml
# UPDATE Hob.md:
name: Hob
room: Kitchen
status: ordered
vendor: "GRH Logistics"
model: "Bertazzoni P603I30NV Induction Hob (3 Cooking Zones)"
price: "$916.00"
currency: SGD
notes: |
  Replaces the previously-shortlisted Bosch PUE611BB5J ($1,159) — brand fully changed to
  Bertazzoni. Ordered via GRH Logistics SS-S017303 (14 Jun 2026), bundled with Hood + Oven
  ($2,850 total, $550 deposit paid). Individual price from reno sheet (Update 2026-06-21).
  FOC Mayer MCS5P 5pcs Pot Set included in the bundle.
source: "raw/drive/grh-hoekee-hob-hood-oven-2026-06-14.md; raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Update 2026-06-21)"
confidence: high

# UPDATE Hood.md:
name: Hood
room: Kitchen
status: ordered
vendor: "GRH Logistics"
model: "Bosch DWB97CM50B (DWZ2CB114 accessory kit) Chimney Hood"
price: "$1,179.00"
currency: SGD
notes: |
  Model changed from DWBM98G50B ($799) to DWB97CM50B ($1,179) — different Bosch model, price
  increased $380. DWZ2CB114 is an accessory kit bundled with the DWB97CM50B. Ordered via GRH
  Logistics SS-S017303 (14 Jun 2026), bundled with Hob + Oven.
source: "raw/drive/grh-hoekee-hob-hood-oven-2026-06-14.md; raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Update 2026-06-21)"
confidence: high

# UPDATE Oven.md:
name: Oven
room: Kitchen
status: ordered
vendor: "GRH Logistics"
model: "Bosch HHF113BR0B Built-in Oven 66L (60×60 S/S)"
price: "$749.00"
currency: SGD
notes: |
  Same model code (HHF113BR0B) but capacity corrected from 71L to 66L, and price corrected
  from $849 to $749. Ordered via GRH Logistics SS-S017303 (14 Jun 2026), bundled with Hob + Hood.
source: "raw/drive/grh-hoekee-hob-hood-oven-2026-06-14.md; raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Update 2026-06-21)"
confidence: high

# CREATE GRH Logistics Vendor.md:
name: GRH Logistics
type: appliance
contact: ""
location: "33 Ubi Ave 3 #01-34 Vertex"
notes: |
  GST Reg: 201709071R. Kitchen appliances vendor — Hob + Hood + Oven bundle (Sales Order
  SS-S017303, 14 Jun 2026). Bundle total: $2,850; deposit: $550 (PayNow D010535, 14-Jun-26);
  balance: $2,300. Delivery: TBA, 2–5PM window (vendor updates 3 days prior).
  Also appears under the folder name "Hoekee" in Drive — likely a referrer or trade name.
related_items: ["Hob", "Hood", "Oven"]
source: "raw/drive/grh-hoekee-hob-hood-oven-2026-06-14.md"
confidence: high
```
