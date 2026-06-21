# Proposal: Study desk research — Interdesk Ultra (Second room items.md)

**Date:** 2026-06-20
**Proposed by:** Extractor
**Status:** ⛔ SUPERSEDED (compile-03, 2026-06-21) — room question resolved (Common Bedroom), product confirmed via invoice. See `system/review_queue/2026-06-21-interdesk-study-desk-common-bedroom-confirmed.md`.

## What to change

Source: `Dawson's wiki/inbox/Second room items.md` + `Dawson's wiki/zz_images/IMG_9211.jpeg`.

The inbox note reads: *"Jeff's study table — Considering: Interdesk (140cm x 70cm, Walnut
color)"*. The image is a product price card photographed at what appears to be a roadshow or
showroom, showing:

- **Brand/Model:** Interdesk Ultra Shimo Ash (electric height-adjustable, Dual Motor, 3 Stages)
- **Size considering:** 140CM (L) × 70CM (B) × 2.5CM (H), Walnut colour
- **Price:** S$599 for 140cm (from the size/price table on the card; the displayed 160cm unit
  was S$649 roadshow promo, down from S$849)
- **Material:** Laminated wood tabletop. Multiple colours available (incl. Walnut, Shimo Ash,
  and ~14 others on the swatch chips)

See open question #1 for the critical ambiguity about WHICH room this desk belongs to.

### Primary proposal (Common Bedroom interpretation — see open question #1):

**CREATE** `Dawson's wiki/wiki/Rooms/Common Bedroom/Study Desk.md` — new item note.

**UPDATE** `Dawson's wiki/wiki/Rooms/Common Bedroom/Common Bedroom.md` — add `[[Study Desk]]`
to Items list.

### Alternative proposal (Master Bedroom replacement — see open question #1):

**UPDATE** `Dawson's wiki/wiki/Rooms/Master Bedroom/Working-Vanity Desk.md` — add an
"In-store research (Jun 2026)" section noting the Interdesk Ultra as an alternative under
consideration, without replacing the current Adan 1.2M record yet.

## Why / cited sources

- `Dawson's wiki/inbox/Second room items.md` — filename "Second room items" suggests Common
  Bedroom (= "second room"); the item is framed as "Jeff's study table".
- `Dawson's wiki/zz_images/IMG_9211.jpeg` — product price card with full spec/pricing.
- `Dawson's wiki/wiki/Rooms/Common Bedroom/Common Bedroom.md` — design intent already states
  "Built-in study table, 1.4–1.6 m" (moodboard slides 26–27), and 140cm fits exactly within
  that 1.4–1.6m spec.
- `Dawson's wiki/wiki/Rooms/Master Bedroom/Working-Vanity Desk.md` — current record is Adan
  1.2M Electric Adjustable Table ($139, shortlisted) — also an electric adjustable desk,
  though smaller (120cm) and much cheaper. Interdesk Ultra at 140cm/$599 is a competing option
  in the same functional category.

## Open questions / judgment calls

1. **CRITICAL — which room?** The file title "Second room items" points to the Common Bedroom,
   and 140cm matches the moodboard's "1.4–1.6m study table" spec for that room exactly. But:
   - The Common Bedroom's study table was originally conceived as a BUILT-IN (Bud Studio
     carpentry) — switching to a freestanding Interdesk would mean dropping that built-in scope,
     which could be a Change Order/cost-saving decision worth flagging to Bud Studio.
   - Alternatively, "Jeff's study table" could be his personal desk in the **Master Bedroom**
     (where the Working-Vanity Desk already lives, currently the Adan 1.2M at $139) — the
     Interdesk Ultra at $599 is more expensive but also a higher-spec product.
   - A third possibility: both rooms need a desk and this is just the research phase for one of
     them. **Human: which room is this desk for?**

2. **Status: researching vs. shortlisted?** Only one option was photographed/noted and the
   framing is "considering" — treating as `status: researching` until confirmed. If the human
   says this is the chosen desk, upgrade to `shortlisted`.

3. **Price: is $599 the confirmed price?** The card shows the 140cm size from S$599 (not the
   roadshow-promo price, which applied to the 160cm unit displayed). If the roadshow was still
   running on the day they photographed it, the 140cm might have had a similar promo discount —
   but $599 is the best available figure from the card.

## Proposed record

```yaml
- name: Study Desk (Jeff)
  room: Common Bedroom    # see open question #1 — may be Master Bedroom instead
  status: researching
  vendor: "Interdesk"
  model: "Interdesk Ultra Shimo Ash — 140CM (L) x 70CM (B) x 2.5CM (H), Walnut colour, Dual Motor (3 Stages) electric height-adjustable"
  price: "$599.00"
  currency: SGD
  notes: |
    Seen at a roadshow/showroom, 2026-06 (exact date not recorded). Jeff considering the 140cm
    Walnut version. Electric height-adjustable (dual motor, 3 stages) — same functional category
    as the current Adan 1.2M in Master Bedroom (also electric adjustable). If for Common Bedroom:
    140cm matches the moodboard's 1.4–1.6m study table spec; note this would replace/subsume the
    built-in study table concept in the Bud Studio carpentry scope. Confirm with human which room
    before compiling.
  source: "Dawson's wiki/inbox/Second room items.md; Dawson's wiki/zz_images/IMG_9211.jpeg"
  confidence: medium
```
