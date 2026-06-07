# Proposal: Master Bedroom + Guest Bedroom — furniture item records

**Date:** 2026-06-07
**Proposed by:** Extractor
**Status:** awaiting human approval

## What to change

Create two new compiled room notes + item notes:

- `Dawson's wiki/wiki/Rooms/Master Bedroom/Master Bedroom.md` (room note)
- `Dawson's wiki/wiki/Rooms/Master Bedroom/Bed Frame + Mattress.md`
- `Dawson's wiki/wiki/Rooms/Master Bedroom/Working-Vanity Desk.md`
- `Dawson's wiki/wiki/Rooms/Guest Bedroom/Guest Bedroom.md` (room note)
- `Dawson's wiki/wiki/Rooms/Guest Bedroom/Murphy Bedframe.md`
- `Dawson's wiki/wiki/Rooms/Guest Bedroom/Ironing Set.md`

Trigger: "Real room in source data" + "Real item to track" — both bedrooms have multiple
tracked furniture items with prices/models, plus rich design-intent notes from the moodboard
and dedicated Bud Studio carpentry scope (wardrobes, headboard, vanity).

## Why / cited sources

- `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` §"Furniture & Appliances" (Master Bedroom +
  Guest Bedroom groups) — authoritative tracker.
- `raw/drive/whatsapp-image-2026-02-07-bed-frame-2026-06-07.md` — bed-frame reference photo
  (metadata-only; empty OCR — corroborates the item exists as a tracked purchase candidate).
- `raw/drive/jm-house-moodboard-2026-06-07.md` (slides 21-28, 34) — Master Bedroom + Guest/
  Study Bedroom design-intent notes ("what we know we want" / floorplan / moodboard themes).
- `raw/drive/jm-house-moodboard-v2-2026-06-07.md` (slides 18-23, 25) — v2 Master Bedroom +
  Bedroom 2/Murphy-bed concepts.
- `raw/drive/skyville-dawson-bud-studio-first-draft-comments-2026-06-07.md` (pages 10-16) —
  client review comments on the Master Bedroom render (parquet colour, wardrobe finish,
  library-shelf concept, full-length mirror placement).
- `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` Appendix A Section J (Carpentry) — wardrobe/
  headboard/vanity-cabinet line items for Master Bedroom & Master Bathroom.

## Proposed item records

```yaml
- name: Bed Frame + Mattress
  room: Master Bedroom
  status: shortlisted
  vendor: ""
  model: "Dunlopillo King Size Storage Drawer Bed Frame (L190 x W183 x H30.5)"
  price: "$2,039.00"
  currency: SGD
  notes: |
    Listed in Reno Sheet tracker, NOT flagged "Confirmed" — appears to be a shortlisted/
    planned purchase. A WhatsApp reference photo exists (file dated 7 Feb 2026, in Drive
    folder "02 Bed Frame + Mattress") but contains no extractable text/order info — purely a
    product-reference image, not a purchase record.
    Design context (moodboard slides 22-23): explicit preference for "soft bed frame", a
    "3 layers" bed frame concept, "light hidden in thin built-in bedframe" — a storage-drawer
    frame broadly fits the "soft"/layered aesthetic described, though the moodboard's exact
    "3 layers" / hidden-light concept may go beyond what this off-the-shelf model offers
    (possible gap between aspirational moodboard concept and the actual shortlisted SKU —
    human to confirm whether this is the final pick or a placeholder).
    Bud Studio Appendix A includes a matching custom one-sided headboard (Section J item 14,
    35sqft, $1,225, height based on 800mm) — built around whichever bed frame is finalised.
  source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Furniture & Appliances); raw/drive/whatsapp-image-2026-02-07-bed-frame-2026-06-07.md; raw/drive/jm-house-moodboard-2026-06-07.md"
  confidence: medium

- name: Working-Vanity Desk
  room: Master Bedroom
  status: shortlisted
  vendor: ""
  model: "Interdesk Classic (W100 x D60)"
  price: "$399.00"
  currency: SGD
  notes: |
    Listed in Reno Sheet tracker (paired with a matching Kave Lexa Swivel Chair, $300, same
    room group — H84 x W59 x D60). Neither flagged "Confirmed".
    Design context: moodboard slide 21 explicitly lists "vanity table/space + storage in the
    toilet, dedicated for skincare" as a "what we know we want" item, and slide 34 reiterates
    "vanity table between bed and window". Render-comment page 16 confirms a sizing decision:
    "Study / vanity table - actually 1m is ok!" (i.e. the 1-metre-wide desk size was approved
    during design review — matches this item's W100 spec). Bud Studio Appendix A includes a
    matching "seated vanity cabinet" for Master Bathroom (Section J item 17, 3ft, $600).
  source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Furniture & Appliances); raw/drive/jm-house-moodboard-2026-06-07.md; raw/drive/skyville-dawson-bud-studio-first-draft-comments-2026-06-07.md (page 16)"
  confidence: medium

- name: Murphy Bedframe
  room: Guest Bedroom
  status: shortlisted
  vendor: ""
  model: "Alegra Vertical Murphy Bed (Natural) - Queen"
  price: "$1,899.00"
  currency: SGD
  notes: |
    Listed in Reno Sheet tracker with Qty/Total shown as blank/zero ("$0.00") — likely a
    placeholder/not-yet-committed line (price shown but quantity & total left empty), distinct
    from a true "Confirmed" purchase.
    Design context: this directly matches the moodboard's stated room concept — "Study Room/
    Guest Bedroom... Murphy bed" (slide 27) and "convertible to guest bedroom... upgradable to
    kid's bedroom" (slide 26); v2 moodboard devotes 2 slides to "Murphy bed bedroom" concepts
    (slides 23, 25). Bud Studio Appendix A includes a matching "top hung cabinet above loose
    murphy bed" for Common Bedroom (Section J item 10, 6ft, $1,140) — confirms the murphy-bed
    concept is a settled design direction even if this specific SKU/purchase isn't finalised.
  source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Furniture & Appliances); raw/drive/jm-house-moodboard-2026-06-07.md; raw/drive/jm-house-moodboard-v2-2026-06-07.md"
  confidence: medium

- name: Ironing Set
  room: Guest Bedroom
  status: shortlisted
  vendor: ""
  model: "Philips AIS8540/80 All-in-One 8500 Series (W39.2 x H60.2 x D597)"
  price: "$739.00"
  currency: SGD
  notes: "Listed in Reno Sheet tracker (Guest Bedroom group), not flagged Confirmed — a planned/shortlisted appliance purchase, likely tied to the room's 'storage space... to fold laundry' / utility-room dual-function concept from the moodboard (slide 4-8 design preferences mention 'desk to fold laundry' near the service yard, and the guest bedroom doubles as a study/utility space)."
  source: "raw/sheets/reno-sheet-bud-studio-2026-06-07.md (Furniture & Appliances); raw/drive/jm-house-moodboard-2026-06-07.md"
  confidence: low
```

## Proposed room note seeds

```yaml
- name: Master Bedroom
  notes: |
    "1 big master bedroom" was a stated top-level design principle (moodboard slide 2) — an
    explicit tradeoff consideration was even raised about whether to "open the glass door to
    make a bigger living room, sacrificing master bedroom size" (slide 9, unresolved in the
    source material). Stated wants (slide 21): doors should reveal both rooms on entry (no
    blocking wall/mirror); dedicated vanity + skincare storage in the ensuite; must fit a
    king-size bed (matches the floor-plan annotation "KING SIZE BED 1900 X 2000").
    Design-review decisions/open items from the first-draft render comments (pages 13-16):
      - Parquet flooring colour to be adjusted to look more true-to-life ("more similar
        like IRL")
      - Wardrobe door finish: wood vs. white still under discussion ("Open to keep it white
        if wood doesn't work" — explicitly flagged as undecided, may cascade to TV-wall finish)
      - Wall treatment: considering light-coloured limewash paint if wardrobe doors go wood
      - Wants a flushed horizontal "library" shelf element on the wall (referenced an
        inspiration image)
      - Full-length mirror placement still UNRESOLVED ("is missing... open to suggestions
        on placement")
      - Vanity/study desk: 1m width APPROVED ("actually 1m is ok!")
    Bud Studio Appendix A carpentry scope here is the single largest room allocation: full-
    height casement wardrobes x2 (Section J items 11-12, ~$5,925 incl. exposed laminate
    panels), suspended TV-wall ledge ($480), one-sided headboard ($1,225), suspended bedside
    tables ($670), plus the two-sided partition wall (Section E item 3, $930).
  source: "raw/drive/jm-house-moodboard-2026-06-07.md; raw/drive/skyville-dawson-bud-studio-first-draft-comments-2026-06-07.md; raw/sheets/reno-sheet-bud-studio-2026-06-07.md"
  confidence: high

- name: Guest Bedroom
  notes: |
    Referred to inconsistently across sources as "Study Room/Guest Bedroom" (moodboard v1,
    slide 26), "Bedroom 2" (moodboard v2, slides 21-22), and "Common Bedroom" (Bud Studio
    Appendix A, Section J item 10) — likely all the SAME physical room described from
    different angles (design-brief vs. as-built scope-of-works framing). Filed here as
    "Guest Bedroom" to match the Reno Sheet furniture tracker's grouping label; a human
    should confirm whether "Common Bedroom" (used in the signed contract) is the preferred
    canonical name — see call-out #2.
    Stated design intent (moodboard slide 26-27): convertible to guest bedroom on demand;
    upgradable to a kid's bedroom in 3-5 years (must comfortably fit a queen bed); built-in
    study table 1.4-1.6m; full wardrobe wall; Murphy bed; colour scheme to mirror the master
    bedroom. v2 adds: "sofa turned bed?" as an open idea (slide 29).
  source: "raw/drive/jm-house-moodboard-2026-06-07.md; raw/drive/jm-house-moodboard-v2-2026-06-07.md; raw/sheets/reno-sheet-bud-studio-2026-06-07.md"
  confidence: medium
```

## Human-judgment call-outs

1. **No items had a "Confirmed" purchase order document on file for either bedroom** — unlike
   Living/Dining and Kitchen, none of the bedroom furniture has a corroborating Gain City/
   vendor order PDF; everything here is sourced solely from the Reno Sheet tracker (with the
   Bud Studio carpentry scope as secondary corroboration of the underlying design DIRECTION,
   not the specific furniture SKUs). I rated all four items "shortlisted"/medium-or-lower
   confidence accordingly — none should be presented as settled purchases.
2. **Room-naming inconsistency**: the same physical "second bedroom" is called "Study Room/
   Guest Bedroom" (moodboard v1), "Bedroom 2" (moodboard v2), "Common Bedroom" (signed
   contract Appendix A), and grouped as "Guest Bedroom" (Reno Sheet furniture tracker). I
   used "Guest Bedroom" (matching the furniture tracker, since that's the item-grouping
   source) but flag this as needing a single canonical name — possibly "Common Bedroom" to
   match the legally-binding contract's terminology, which will also be the term used in any
   future as-built/scope cross-references.
3. **Murphy Bedframe's tracker row shows a blank Qty and "$0.00" total** despite a populated
   unit price — I read this as "price researched but purchase not committed" rather than "free/
   $0 item"; a human with sheet-editing context could confirm this interpretation.
4. Confidence: medium for Bed Frame, Working-Vanity Desk, Murphy Bedframe (each corroborated
   by independent moodboard/render-comment design-intent references, even without a purchase
   order); low for Ironing Set (single-source tracker mention, weakest design-intent linkage).
