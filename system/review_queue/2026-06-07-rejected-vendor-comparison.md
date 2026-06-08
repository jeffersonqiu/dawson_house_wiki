# Proposal: Rejected-vendor comparison — Senso Studio, ZX/Kove Design, Reno Studio

**Date:** 2026-06-07
**Proposed by:** Extractor
**Status:** ✅ APPROVED (2026-06-08, by Jefferson)

**Human decision notes:**
- Approved as THREE separate vendor notes (Senso Studio / ZX Design (Kove Interior Design) /
  Reno Studio (The Good Rocket)) — matches the Bud Studio note's pattern and keeps each
  vendor's distinct contacts/quotes/contract numbers cleanly separated, per the Extractor's
  primary recommendation over the single-combined-note alternative in call-out #1.
- "ZX Design" vs. "KOVE Interior Design" naming ambiguity: keep as proposed (one vendor note,
  both names documented) — I don't have independent confirmation either way, so the
  Extractor's "same vendor, two names" inference stands as the working assumption; flag
  remains visible in the note for future correction if it surfaces.
- Comparison summary table approved for inclusion / future use in a vendor-comparison page.

## What to change

Create three new compiled vendor notes (or, alternatively, ONE combined "Vendor Comparison —
ID Quotes (rejected)" note — see call-out #1 for the judgment call):

- `Dawson's wiki/wiki/Vendors/Senso Studio.md`
- `Dawson's wiki/wiki/Vendors/ZX Design (Kove Interior Design).md`
- `Dawson's wiki/wiki/Vendors/Reno Studio (The Good Rocket).md`

Trigger: "Real vendor" per `note-creation.md` — these are three concretely-quoted, named,
contact-having alternative ID/contractor vendors that were seriously evaluated (full written
quotations + named designers + contact cards on file) before Bud Studio was selected. They
materially explain "why Bud Studio" and are worth keeping as comparison-shopping history.

## Why / cited sources

All three were found in `04 Renovation / 0 Archive / 02. IDs Archive` — a folder explicitly
dedicated to archived vendor-comparison documents (per ingestion run 02's folder walk).

- **Senso Studio** — `raw/drive/senso-studio-quotation-26-q0125-03-2026-06-07.md`,
  `raw/drive/senso-studio-quotation-106k-2026-06-07.md`,
  `raw/drive/senso-studio-marcella-jeff-dawson-rd-2026-06-07.md`,
  `raw/drive/senso-studio-namecards-2026-06-07.md`
- **ZX Design / Kove Interior Design** — `raw/drive/zx-kove-marcella-jeff-quotation-v2-2026-06-07.md`,
  `raw/drive/zx-design-layout-plan-2026-06-07.md`
- **Reno Studio (The Good Rocket Pte Ltd)** — `raw/drive/reno-studio-quotation-2026-06-07.md`

## Proposed vendor records

```yaml
- name: Senso Studio
  type: contractor
  contact: "Emily Neo (Sales Manager / Designer), +65 9339 3683, emily@sensostudio.sg; Joshua Lee (Design Consultant), +65 9019 2161, joshua@sensostudio.sg"
  location: "sensostudio.sg (Senso Studio Pte. Ltd.)"
  notes: |
    REJECTED alternative ID/renovation vendor — considered before Bud Studio was selected.
    TWO quotation revisions on file, both dated 01/02/2026, same project (86 Dawson Rd):
      - Ref 26-Q0125--02 ("Quotation 106k" — larger/earlier scope; full hacking of kitchen +
        2 toilets + service yard + 2 bedrooms + demolish ~48ft of full-height walls; vinyl
        flooring throughout living/bedrooms; grand total not captured in OCR but filename
        suggests ~$106,000 — section subtotals on file: Hacking $11,500 / Tiling-Masonry
        $28,580 / False-ceiling-partition $5,200 / Plumbing $4,090 / Carpentry [total truncated])
      - Ref 26-Q0125--03 (reduced/later-revised scope — drops the vinyl-flooring & most wall
        demolition; section subtotals: Hacking $4,800 / Tiling-Masonry $18,230 / False-ceiling
        $5,200 / Plumbing $2,930 / Carpentry [total truncated])
    Preliminary/design-consultancy package was complimentary ($0) in both. Has a separate
    project proposal/concept deck on file ("Marcella & Jeff (Dawson Rd)") — primarily visual,
    no extractable text beyond cover page.
  related_items: []
  source: "raw/drive/senso-studio-quotation-26-q0125-03-2026-06-07.md; raw/drive/senso-studio-quotation-106k-2026-06-07.md; raw/drive/senso-studio-marcella-jeff-dawson-rd-2026-06-07.md; raw/drive/senso-studio-namecards-2026-06-07.md"
  confidence: medium   # both quotation totals are incomplete (OCR truncation cut off carpentry sections / grand totals before the final figure)

- name: ZX Design (Kove Interior Design)
  type: contractor
  contact: "Rachelle (designer/PIC, layout plan); Bernice (co-designer, quotation); mobile on file 8357 5973 (client's own — vendor's direct contact not captured)"
  location: "\"ZX Design — HOUSE TO HOME\" / operating as KOVE Interior Design for this quotation"
  notes: |
    REJECTED alternative ID/renovation vendor — considered before Bud Studio was selected.
    Quotation V2 dated 7-Feb-2026, designers Rachelle & Bernice, target key-collection "July
    2026". Total contract amount ~S$66,775 (per source cross-reference; full payment schedule
    not captured in extraction — lowest of the four quotes on file).
    Section subtotals on file: Professional services $1,000 (lump sum) / General services
    (hacking/demolition incl. HDB-approval-subject wall removals) $4,800 / Masonry $17,375 /
    Plumbing $3,230 / [Ceiling & partition truncated in extraction].
    Also produced a floor LAYOUT PLAN drawing (OCR'd from a WhatsApp image) labelling rooms
    as Balcony / Living-Dining / Bedrm 3 / Store / Common Bath / Master Bath / Kitchen —
    drawn by Rachelle, "subject to modification… to suit construction purposes".
    NOTE: Vendor appears under TWO names in the source material ("ZX Design" on the layout
    plan vs. "KOVE Interior Design" on the quotation cover/filename) — likely the same studio
    operating under both a trade name and a registered design-firm name; treated as one vendor
    here pending human confirmation.
  related_items: []
  source: "raw/drive/zx-kove-marcella-jeff-quotation-v2-2026-06-07.md; raw/drive/zx-design-layout-plan-2026-06-07.md"
  confidence: medium   # name ambiguity (ZX vs Kove) + total amount sourced from a cross-reference note rather than the primary document's own grand-total line (truncated in OCR)

- name: Reno Studio (The Good Rocket Pte Ltd)
  type: contractor
  contact: "Jeremy (PIC); renostud.io; The Good Rocket Pte Ltd, Co. Reg. 202101870N, 12 Woodlands Square, Woods Square Solo 1 #03-43, S737714"
  location: "12 Woodlands Square, Woods Square Solo 1, #03-43, Singapore 737714"
  notes: |
    REJECTED alternative ID/renovation vendor — considered before Bud Studio was selected.
    Quotation no. JN140326, dated 14/03/2026, valid 7 days, client "Marcella". TOTAL: $68,750.00
    (subtotal $69,022.80 less a small $272.80 discount) — the most COMPLETE and clearly-totalled
    of the three rejected quotes (full section breakdown captured).
    Section breakdown (SGD): Design/PM services (complimentary) / Cleaning-haulage-protection-
    disposal $2,600 / Demolition $7,080 / Masonry (tiling/screeding) $15,164 / Vinyl flooring
    $2,522.80 / Carpentry & countertops $28,590 / Tempered glass $1,750 / Doors $3,450 /
    Partition $3,132 / Plumbing $2,270 / Painting $2,464.
    Notably offers a 24-MONTH warranty (vs. Bud Studio's 12-month) and includes "sourcing and
    purchasing of items from online/offline stores" as a complimentary PM service.
  related_items: []
  source: "raw/drive/reno-studio-quotation-2026-06-07.md"
  confidence: high   # clean total + full section breakdown, single document, no OCR ambiguity on the headline figures
```

## Comparison summary (for the Compiler's eventual comparison page / table)

| Vendor | Quote ref/date | Total (SGD) | Status | Notable terms |
|--------|---------------|-------------|--------|---------------|
| **Bud Studio** | 26R532, signed 31/3/26 | **$72,805.00** | **SELECTED** | 12-mo warranty, 100-day completion, tiles "by owner" |
| Reno Studio (Good Rocket) | JN140326, 14/3/26 | $68,750.00 | Rejected | 24-mo warranty, complimentary sourcing/purchasing service |
| ZX Design / Kove | V2, 7-Feb-26 | ~$66,775 (uncaptured grand total — cross-ref figure) | Rejected | Lowest quoted; key collection target "July 2026"; some hacking subject to HDB/PE approval |
| Senso Studio | 26-Q0125--02, 1/2/26 | ~$106,000 (filename-derived; grand total not captured) | Rejected | Larger original scope incl. vinyl flooring + extensive wall demolition |
| Senso Studio (revised) | 26-Q0125--03, 1/2/26 | Not captured (reduced scope vs. above) | Rejected | Trimmed-down version of the same vendor's proposal |

Note: Bud Studio was NOT the cheapest quoted option — Reno Studio and ZX/Kove both quoted
lower. The decision rationale (design fit, designer rapport, scope completeness, etc.) is not
explicitly documented in any source file; if the human knows the "why Bud Studio" story it
would make a good `04 Decisions.md` entry.

## Human-judgment call-outs

1. **Combine into one note vs. three separate notes?** I propose THREE separate vendor notes
   (mirroring how Bud Studio gets one) for consistency and because each has distinct contacts/
   quotes/contract numbers — but a single "Vendor Comparison (Rejected Quotes)" note may better
   serve the "why Bud Studio" narrative use-case. Compiler/human judgment call.
2. **Two of the three rejected quotes have INCOMPLETE totals** (Senso Studio both revisions,
   ZX/Kove) — the OCR extraction truncated mid-carpentry-section before reaching the grand
   total line. I've used filename-derived ("106k") or cross-reference-note-derived (~$66,775)
   figures with explicit caveats; a human with Drive access could pull the exact final totals
   in under a minute by opening the PDFs directly — flagging this as a low-effort, high-value
   follow-up.
3. **"ZX Design" vs. "KOVE Interior Design"** naming ambiguity — same vendor or a rename/
   rebrand/parent-subsidiary relationship? I assumed "same vendor, two names" but this is an
   inference, not a documented fact.
4. Confidence: Reno Studio = high (complete, unambiguous); Senso Studio & ZX/Kove = medium
   (incomplete totals, name ambiguity for the latter).
