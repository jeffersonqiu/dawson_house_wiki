# Proposal: Bud Studio — chosen ID/contractor vendor note (+ quotation reconciliation)

**Date:** 2026-06-07
**Proposed by:** Extractor
**Status:** ✅ APPROVED (2026-06-08, by Jefferson)

**Human decision notes:**
- Approved as proposed — single combined vendor note for Bud Studio Pte Ltd + Fruit Design
  Practice Pte Ltd (billing entity), with both registration numbers documented in the body.
- Approved seeding `04 Decisions.md` with the candidate row provided below.
- Quotation reconciliation ($77,725 → $75,700 → $72,805) accepted as written; the signed
  contract figure (S$72,805.00) is the sole authoritative current fact; the other two are
  historical-evolution context only.

## What to change

Create a new compiled vendor note:

- `Dawson's wiki/wiki/Vendors/Bud Studio.md`

Trigger: "Real vendor" per `system/constitution/note-creation.md` — Bud Studio is the SIGNED,
engaged interior-design/renovation contractor for 86 Dawson Rd #05-03 (contract executed
31 March 2026, deposit paid 2 April 2026, work in progress). This is the highest-confidence
vendor record in the whole corpus.

(Optionally also seed `Dawson's wiki/wiki/04 Decisions.md` with one log row recording "Bud
Studio selected as ID contractor, $72,805 signed 31/3/26" — leaving that to the Compiler's
judgment per the single-master-log rule; a candidate row is included below for convenience.)

## Why / cited sources

- `raw/drive/signed-renovation-contract-marcella-jefferson-2026-06-07.md` — the executed
  Renovation Agreement (31 Mar 2026), Appendix A quotation (ref 26R532, Contract Sum
  S$72,805.00), Appendix B payment schedule. **Authoritative for all current facts.**
- `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` — live "02 Reno Sheet x Bud Studio
  [External]" Google Sheet; matches the signed contract's summary/line items exactly
  ($72,805.00 total, A–L section subtotals, furniture/appliance tracker, payment milestone
  status).
- `raw/drive/fruit-design-invoice-fd-inv-0079-2026-06-07.md` + `fruit-design-receipt-fd-inv-0079-2026-06-07.md`
  — Milestone-1 deposit invoice (FD-INV-0079, $7,280.50, issued 1 Apr 2026, due 8 Apr) and
  receipt confirming full payment 2 Apr 2026 (sent 6 Apr).
- `raw/drive/skyville-dawson-bud-studio-first-draft-2026-06-07.md` +
  `skyville-dawson-bud-studio-first-draft-comments-2026-06-07.md` — first-draft 3D
  visualization package (drawing A.01, dated 01/04/26) and the client's marked-up review
  comments (21 pages of room-by-room feedback).
- Superseded drafts (for historical trace only — see reconciliation below):
  `raw/drive/bud-studio-quotation-handwritten-2026-06-07.md` (13/3/26 draft, ~$77,725),
  `raw/drive/marcella-rev2-bud-studio-2026-06-07.md` ("rev2", 27/3/26, $75,700.00),
  `raw/sheets/claude-marcella-quotation-26r532-2026-06-07.md` (reformatted sheet, $75,700.00).

## ⚠️ Reconciliation — THREE Bud Studio quotation totals found

Three different "Appendix A / Bud Studio Quotation" totals exist in the source material for
project ref **26R532** (86 Dawson Rd #05-03, client Marcella Risye / Jefferson Qiu). They are
NOT competing current facts — they are sequential drafts of the same quotation evolving toward
the signed figure. Recommended treatment: record ONLY the signed figure as the vendor's
"current" contract sum, and capture the other two purely as historical/evolution notes.

| # | Total | Date | Document | Status |
|---|-------|------|----------|--------|
| 1 | ~$77,725 (handwritten OCR estimate) | 13/3/2026 | Handwritten/annotated earliest draft (`bud-studio-quotation-handwritten-...md`) — included draft-only line items later removed (e.g. "dismantle existing skirting" $35, "dismantle existing parquet flooring w/ screed" $1,250); draft Section B subtotal $8,095 vs. final $6,235 | **Superseded** — earliest working draft |
| 2 | $75,700.00 | 27/3/2026 | "rev2" PDF (`marcella-rev2-bud-studio-...md`) AND the reformatted spreadsheet `claude_Marcella_Quotation_26R532` (`claude-marcella-quotation-26r532-...md`) — both show identical section subtotals A–D matching the final contract, but a grand total $75,700.00 with NO discount applied | **Superseded** — pre-discount revision point (two documents independently agree on this figure, suggesting it was a real interim quotation state, not a typo) |
| 3 | **$72,805.00** | 30–31/3/2026 | **SIGNED Renovation Agreement, Appendix A** (`signed-renovation-contract-marcella-jefferson-...md`) — identical A–L section subtotals to rev2 ($5,000 / $6,235 / $6,370 / $12,080 / $2,955 / KIV / $3,320 / $5,880 / $700 / $26,595 / $4,070 / $600 = $73,805 gross) **minus a late "Less Discount: −$1,000.00"** = **$72,805.00 net** | **AUTHORITATIVE — current Contract Sum** |

**Conclusion:** $75,700 → $72,805 is explained entirely by a **−$1,000.00 discount** applied
between the 27/3/26 "rev2" point and the 30/3/26 signed Appendix A — all section subtotals
(A through L) are byte-identical across rev2, the reformatted sheet, and the signed contract.
The earliest ~$77,725 handwritten draft reflects an even earlier scope (extra hacking/dismantling
line items worth ~$1,860 more in Section B alone, later trimmed). This is a clean, traceable
evolution: **$77,725 (13 Mar, draft scope) → $75,700 (27 Mar, rev2/reformatted, trimmed scope,
pre-discount) → $72,805 (30/31 Mar, SIGNED, post −$1,000 discount).**

## Proposed vendor record

```yaml
name: Bud Studio
type: contractor
contact: "Jaslyn Lim (designer/PM), 65 8774 7331; admin@budstudio.com; enquiry@budstudioco.com; office +65 9670 0707 / +65 8133 7123"
location: "195 Pearl's Hill Terrace #02-06, Singapore 168976 (Bud Studio Pte Ltd, Co. Reg. 202114713D; billing entity Fruit Design Practice Pte Ltd, UEN 202429785E)"
notes: |
  CHOSEN interior-design/renovation contractor for 86 Dawson Rd #05-03 SkyVille @ Dawson.
  Renovation Agreement signed 31 March 2026 (project ref 26R532).

  Contract Sum: S$72,805.00 (inclusive of GST & service charges) — see reconciliation note;
  this is the AUTHORITATIVE figure (signed Appendix A, post a late −$1,000 discount). Two
  earlier quotation revisions exist with different totals ($75,700 "rev2"/reformatted-sheet,
  ~$77,725 earliest handwritten draft, both 27/3 and 13/3 respectively) — both superseded,
  retained only as historical trace of how scope/pricing evolved.

  Scope excludes: PE endorsement, electrical works, aircon works, sanitary fittings/accessories
  (light fixtures, curtains), tiles supply (tiles "by owner" throughout masonry sections).
  Completion target: 100 days from commencement. 12-month workmanship warranty from completion.

  Payment milestones (Appendix B): 10% deposit ($7,280.50, PAID 2 Apr 2026 — receipted against
  invoice FD-INV-0079) / 40% before commencement ($29,122.00) / 35% before millworks fabrication
  ($25,481.75) / 10% before millworks installation ($7,280.50) / 5% on completion / 21 days
  post-defects-list ($3,640.25). Payable to Fruit Design Practice Pte Ltd (DBS 072-123-408-4 /
  PayNow UEN 202429785E).

  Design package: first-draft 3D visualizations + schematic floor plan (drawing A.01, dated
  01/04/26) delivered; client (Marcella & Jeff) returned 21 pages of room-by-room review
  comments — see related TASK proposal for design-decision follow-ups extracted from those
  comments (e.g. dry pantry layout choice, no dishwasher, 75" TV consideration, dark-brown
  kitchen finish, wardrobe wood-vs-white finish).
related_items:
  - "Rooms/Kitchen/* (carpentry, masonry, plumbing scope per Appendix A sections B–L)"
  - "Rooms/Master Bedroom/* (wardrobes, headboard, partition wall, vanity per Appendix A section J)"
  - "Rooms/Master Bathroom/* (tiling, glass works, vanity cabinet per Appendix A sections D, H, I, J, K)"
source: "raw/drive/signed-renovation-contract-marcella-jefferson-2026-06-07.md; raw/sheets/reno-sheet-bud-studio-2026-06-07.md; raw/drive/fruit-design-invoice-fd-inv-0079-2026-06-07.md; raw/drive/fruit-design-receipt-fd-inv-0079-2026-06-07.md"
confidence: high
```

## Candidate `04 Decisions.md` log row (optional — Compiler's call whether to seed the log now)

| Date | Decision | Why | Source |
|------|----------|-----|--------|
| 2026-03-31 | Selected Bud Studio as ID/renovation contractor; signed Renovation Agreement, Contract Sum S$72,805.00 (incl. −$1,000 late discount) | Chosen over 3 other quotes (Senso Studio ~$106k & reduced-scope variant, ZX/Kove Design ~$66,775, Reno Studio/Good Rocket $68,750) — see vendor-comparison proposal | `raw/drive/signed-renovation-contract-marcella-jefferson-2026-06-07.md` |

## Human-judgment call-outs

1. **Two distinct legal entities are involved** — "Bud Studio Pte. Ltd." (Co. Reg. 202114713D,
   the contracting party per the signed Agreement) vs. "Fruit Design Practice Pte. Ltd."
   (UEN 202429785E, the billing/invoicing entity whose bank account payments are routed
   through). I've combined them into one vendor note (as the homeowner experiences "Bud
   Studio" as a single relationship) but flagged both registration numbers — a human may
   prefer two separate vendor stubs or a clearer "operates as" framing.
2. **"Jaslyn Lim" appears as both the design/PM contact AND the drawing preparer** ("DRAWING
   BY: JASLYN.L") — likely the primary point of contact; included as the vendor contact.
3. The render/comments PDFs contain rich room-level design-decision material (dry pantry
   choice, "no dishwasher" decision, 75" TV consideration, finish/colour choices for kitchen
   and wardrobes) that arguably belongs partly to per-room item notes once those rooms exist
   as compiled notes — for this first pass I've folded the headline decisions into the
   companion Tasks/Decisions proposal (`2026-06-07-tasks-and-design-decisions.md`) rather than
   inventing room notes prematurely (no room notes exist yet — note-creation.md says don't
   create room folders without real room data; I judge the Bud Studio scope itself to be
   "real room data" worth a future Compiler look, but defer that call).
4. Confidence is **high** across the board — the signed contract is an unambiguous, dated,
   signed legal document and is corroborated independently by the live Reno Sheet (identical
   figures) and the paid invoice/receipt pair.
