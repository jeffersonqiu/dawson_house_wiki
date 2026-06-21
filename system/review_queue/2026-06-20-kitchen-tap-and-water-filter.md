# Proposal: Kitchen tap + water filter — compile-02 flagged tracker rows

**Date:** 2026-06-20
**Proposed by:** Extractor
**Status:** ⛔ SUPERSEDED (compile-03, 2026-06-21) — Kitchen Tap.md NOT created (mixer now bundled into Oslo 316 sink set). Water Filter compiled at $215 (not $549). See `system/review_queue/2026-06-21-kitchen-sink-bundle-and-water-filter.md`.

## What to change

These two items were flagged as "out of scope for this compile" in the compile-02 run
(2026-06-14) and noted in `Dawson's wiki/wiki/Rooms/Kitchen/Sink.md` as items for a future
pass. Both are real rows in the Furniture & Appliances tracker alongside the Kitchen Sink
(Zuhne Oslo) — no new source content, just the pre-existing tracker.

1. **CREATE** `Dawson's wiki/wiki/Rooms/Kitchen/Kitchen Tap.md`
2. **CREATE** `Dawson's wiki/wiki/Rooms/Kitchen/Water Filter.md`
3. **UPDATE** `Dawson's wiki/wiki/Rooms/Kitchen/Kitchen.md` — add both items to the Items list.

## Why / cited sources

- `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` (Furniture & Appliances tracker, current as
  of 2026-06-12) — both rows are in the Kitchen group alongside the Zuhne Oslo Sink.
  - Line ~235: `Kitchen Tap | Kitchen | GROHE Eurosmart Cosmopolitan Single-Lever Sink Mixer
    1/2", Chrome | — | $499.00 | 1 | $499.00`
  - Line ~237: `Drinking Water Filter | Kitchen | 3M AP Easy Complete (Under-Sink) | | $549.00
    | 1 | $549.00`
- `Dawson's wiki/wiki/Rooms/Kitchen/Sink.md` — explicitly flags both as "not yet compiled as
  items; flagged for a future pass but out of scope for this compile."
- `Dawson's wiki/wiki/Rooms/Kitchen/Kitchen.md` — the Design principles section already notes
  "Separate water filter for drinking water — RESOLVED: '3M AP Easy Complete (Under-Sink)'
  filter + 'RIGEL Kitchen Faucet'" — the faucet brand in the moodboard is "RIGEL" but the
  tracker row is "GROHE". See open question #1.

## Open questions / judgment calls

1. **Kitchen Tap brand discrepancy: "RIGEL" (moodboard) vs. "GROHE" (tracker).** The compiled
   `Kitchen.md` design principles section says *"'RIGEL Kitchen Faucet' listed in the Reno Sheet
   tracker"* — but the current tracker row (as of 2026-06-12 re-pull) says GROHE Eurosmart
   Cosmopolitan, not RIGEL. This was probably a brand swap between the original and the re-pull.
   Proposing to compile the tracker's current value (GROHE), note the earlier RIGEL reference,
   and mark `confidence: medium` until corroborated. **Human: is GROHE the right tap, or was
   RIGEL preferred?**

2. **Status: shortlisted?** Neither row is marked "Confirmed" in the tracker. Treating both as
   `shortlisted` (same as the Sink). The kitchen design principles say the 3M filter was
   "RESOLVED" — which could warrant `status: shortlisted` or even `ordered` if an actual order
   exists. No independent order/invoice was found. Staying at `shortlisted` for now.

## Proposed records

```yaml
- name: Kitchen Tap
  room: Kitchen
  status: shortlisted
  vendor: ""
  model: "GROHE Eurosmart Cosmopolitan Single-Lever Sink Mixer 1/2\", Chrome"
  price: "$499.00"
  currency: SGD
  notes: |
    Kitchen.md's design principles reference a "RIGEL Kitchen Faucet" as the planned tap —
    but the current Furniture & Appliances tracker row (as of 2026-06-12) lists GROHE Eurosmart
    Cosmopolitan. Likely a brand swap between earlier and later tracker versions. See open
    question #1.
  source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Furniture & Appliances, current as of 2026-06-12)"
  confidence: medium

- name: Water Filter
  room: Kitchen
  status: shortlisted
  vendor: "3M"
  model: "3M AP Easy Complete (Under-Sink)"
  price: "$549.00"
  currency: SGD
  notes: |
    Kitchen.md's design principles mark this as "RESOLVED" — indicating it's essentially the
    chosen product. No independent order/invoice found; keeping status shortlisted until an
    order record is available.
  source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Furniture & Appliances, current as of 2026-06-12)"
  confidence: medium
```
