# Proposal: Kitchen sink — upgraded to 80cm bundle + water filter price correction

**Date:** 2026-06-21
**Proposed by:** Extractor (extraction-06)
**Status:** ✅ APPROVED + COMPILED (compile-03, 2026-06-21) — Sink.md updated to 80cm bundle; Water Filter.md created; Kitchen Tap cancelled.

## What to change

Source: `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` (Update 2026-06-21).

The kitchen sink situation has changed significantly since the 2026-06-14 compile:

| Item | Current state | New value |
|------|--------------|-----------|
| Sink | Zuhne Oslo 60cm Workstation Sink, $788, shortlisted | **Oslo 316 Workstation Sink & Kitchen Mixer Set 80cm / Gunmetal Honeycomb, $1,087.20** |
| Kitchen Tap (GROHE Eurosmart) | Flagged for future compile in Sink.md; proposed as CREATE in extraction-04 | **CANCELLED — tap now bundled into the sink set** |
| Water Filter (3M AP Easy Complete) | Proposed as CREATE ($549) in extraction-04 | **Price corrected to $215** |

**Actions:**
1. **UPDATE** `Dawson's wiki/wiki/Rooms/Kitchen/Sink.md` — new model (80cm bundle, gunmetal finish), new price ($1,087.20), note the included mixer
2. **UPDATE** `Dawson's wiki/wiki/Rooms/Kitchen/Kitchen.md` — Items list: replace separate Sink $788 + Kitchen Tap $499 with the bundle at $1,087.20
3. **CREATE** `Dawson's wiki/wiki/Rooms/Kitchen/Water Filter.md` — $215 (corrected from extraction-04's $549)
4. **SUPERSEDE** extraction-04 proposal `system/review_queue/2026-06-20-kitchen-tap-and-water-filter.md` — the Kitchen Tap.md creation is cancelled (tap is bundled); Water Filter price is corrected to $215

## Why / cited sources

- `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` (Update 2026-06-21) — the 2026-06-20 reno sheet shows a single "Sink & Kitchen Tap (Bundle)" row: "Oslo 316 Workstation Sink & Kitchen Mixer Set 80cm / Gunmetal Honeycomb", $1,087.20. The separate Zuhne Oslo 60cm $788 and GROHE Eurosmart $499 rows no longer appear.
- The bundle is $1,087.20 vs. the prior separate total of $788 + $499 = $1,287 — this bundle is $200 CHEAPER while upgrading from 60cm to 80cm.

**Water filter:** The reno sheet 2026-06-20 shows 3M AP Easy Complete at $215 (vs. $549 in the 2026-06-13 reno sheet). No corroborating invoice found. The price may now include a filtered-water faucet (the RIGEL Faucet row at $99 has also disappeared from the 2026-06-20 tracker). Flagged as open question #2 below.

## Open questions / judgment calls

1. **Status of the Sink bundle:** No corroborating purchase order/invoice found for this sink bundle — unlike the appliances (GRH SO) or the bed (Sleepnight invoice). The reno sheet marks it as the current row (no explicit "Confirmed" flag visible in the Update 2026-06-21 diff). Proposing `status: shortlisted` with `confidence: medium` until an invoice appears. **Human: is this sink bundle ordered/paid yet?**

2. **Water filter price drop + missing RIGEL faucet:** The 3M AP Easy Complete price dropped from $549 to $215, and the RIGEL Kitchen Faucet ($99) row disappeared from the tracker. This could mean: (a) the faucet was included in the $215 bundle, (b) the faucet is no longer needed (the Oslo bundle includes a mixer), or (c) the $549 included a faucet that's now separately handled. **Human: does the $215 water filter still include a separate drinking-water faucet, or is the Oslo sink bundle's mixer used for drinking water too?**

3. **Oslo 316 vs. Zuhne Oslo:** "Oslo 316" appears to be Zuhne's 316 stainless steel grade product — likely the same brand (Zuhne Oslo), just upgraded from the 304SS/60cm spec to the 316SS/80cm spec and bundled with a matched "Kitchen Mixer". The GROHE Eurosmart tap is dropped. Note the gunmetal colour (vs. the prior natural/honeycomb finish).

4. **Sink.md note re: travertine cross-reference:** The existing Sink.md note contains a paragraph explaining that the 2nd-design-revision travertine discussion was about Common Bathroom, not Kitchen. This note should be RETAINED in the updated Sink.md — the cross-reference is still valid and useful context.

## Proposed records

```yaml
# UPDATE Sink.md:
name: Sink & Kitchen Mixer (Bundle)
room: Kitchen
status: shortlisted
vendor: ""
model: "Oslo 316 Workstation Sink & Kitchen Mixer Set 80cm / Gunmetal Honeycomb"
price: "$1,087.20"
currency: SGD
notes: |
  Upgraded from the 2026-06-14 Zuhne Oslo 60cm single-basin ($788, shortlisted) to an 80cm
  bundled set including the kitchen mixer tap in gunmetal finish. The bundle is ~$200 cheaper
  than the prior separate Zuhne 60cm $788 + GROHE Eurosmart $499. No purchase invoice found yet;
  confirm status when order is placed.
  The separate GROHE Eurosmart kitchen tap row is dropped — mixer is included in this bundle.
  316 stainless steel = higher corrosion resistance than the prior 304SS spec.
source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Update 2026-06-21)"
confidence: medium

# CREATE Water Filter.md:
name: Water Filter
room: Kitchen
status: shortlisted
vendor: "3M"
model: "3M AP Easy Complete (Under-Sink)"
price: "$215.00"
currency: SGD
notes: |
  Price corrected from $549 (reno sheet as of 2026-06-13) to $215 (reno sheet as of
  2026-06-20). The RIGEL Kitchen Faucet ($99) row also disappeared from the tracker in the
  same update — unclear whether the faucet is now included in the $215 or separately covered
  by the Oslo sink bundle's mixer. No purchase invoice found. Flag for confirmation.
source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Update 2026-06-21)"
confidence: medium
```

## Superseded proposals

The extraction-04 proposal `system/review_queue/2026-06-20-kitchen-tap-and-water-filter.md` proposed:
- CREATE `Kitchen Tap.md` (GROHE Eurosmart, $499) → **CANCELLED** — tap is now bundled into the Oslo sink set
- CREATE `Water Filter.md` ($549) → **SUPERSEDED** by this proposal (price is $215)

The Compiler should mark that extraction-04 proposal as superseded rather than compiling it. Compiling it would create an incorrect Kitchen Tap note for a product no longer in the tracker.
