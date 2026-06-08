---
name: Whole House
confidence: medium
source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md; raw/drive/gain-city-aircon-lg-2026-06-07.md"
---

# Whole House

A pseudo-room for **cross-cutting items** that span multiple physical rooms and don't belong
to any single `Rooms/{Room}/` folder. The Reno Sheet furniture/appliance tracker groups
several items as "All rooms" (Aircon, Day Curtain, Painting Works, etc.) — this folder is the
canonical home for those.

> **Why this folder exists:** the Extractor's first pass flagged that no "Whole House"
> placement pattern was sanctioned by `note-creation.md`, and provisionally filed the Aircon
> under Kitchen. On compile review (2026-06-08), that placement was judged actively
> misleading — a system covering Master Bedroom + Living/Common Bedroom zones has no business
> being filed under "Kitchen". This folder formalises the cross-cutting-item pattern going
> forward; future "All rooms" tracker items (Day Curtain, Painting Works, etc.) should be
> compiled here too as they're extracted.

## Items

- [[Aircon]] — ordered, $4,973.00 (Gain City — LG System 2, two zones)

## Sources

- `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` (Furniture & Appliances tracker — "All
  rooms" group; Exclusions section)
- `raw/drive/gain-city-aircon-lg-2026-06-07.md` — Gain City Sales Order SO-B0000296812

---
*Compiled 2026-06-08 — new room folder created per the human override documented in
`system/review_queue/2026-06-07-kitchen-and-wholehouse-appliances.md`.*
