# Ingestion Manifest

Last updated: 2026-06-07

## Google Drive folders

| Folder | ID | Status |
|--------|----|--------|
| 10. House Purchase | `13Ru3AGOD4i_UxIjDdvAtPnNCDMIqQHHE` | Identified (out of scope — not pulled) |
| 04 Renovation | `1cwShI6hqhG29f_zFnjZHHtSZnqrK6-yM` | **Pulled** (entire tree walked & content extracted) |
| 04 Renovation / 0 Archive | `1jcVhZckoY_G1CLpXNV6itF3fcUiBSNnr` | Pulled |
| 04 Renovation / 0 Archive / 01. By Luvina | `1X0gDPx3clK8SUxl_HAbWSiCRn7hYAT-8` | Explored — 9 photo-only JPEGs, metadata-only (no extractable text) |
| 04 Renovation / 0 Archive / 02. IDs Archive | *(parent ID not separately recorded — discovered & traversed via its 4 vendor subfolders below; all subfolders fully enumerated)* | Explored (vendor subfolders mapped & pulled) |
| 04 Renovation / 0 Archive / 02. IDs Archive / 1. Senso Studio | `1uKIlGE2L4pYzB5mc8AGKua9IARM38s5p` | Pulled (5/5 files) |
| 04 Renovation / 0 Archive / 02. IDs Archive / 2. ZX / Kove Design | `1683GFqkDPsA8bvpm5R4dB_5WQ4DM5e2z` | Pulled (2/2 files) |
| 04 Renovation / 0 Archive / 02. IDs Archive / 4. Reno Studio (The Good Rocket) | `1yZ8MQ41tAxpKU2DYj9bKjscCU3TAWrXX` | Pulled (1/1 file) |
| 04 Renovation / 0 Archive / 02. IDs Archive / 5. Curated Co | `1KmRbo1did3YeylgPWovHtjM7NNEqEx9n` | Explored — empty folder, nothing to pull |
| 04 Renovation / 01 Bud Studio | `1NAz0vf-3O-HuJfoIq83sZJk01l1bbl8b` | Pulled (subfolders walked) |
| 04 Renovation / 01 Bud Studio / 01 Archive | `16SVXW6p3FP7_eDuYI3-BuVV39lS7r4Ob` | Pulled (2/2 files) |
| 04 Renovation / 01 Bud Studio / 02 Signed Documents | `1ktjpRERCHkBMcTbDAcc7DN-yLsf7a-pr` | Pulled (2/2 files) |
| 04 Renovation / 01 Bud Studio / 03 Payments | `1GxhUGG4BJkw8bG5szNn549B_vLRYEgqE` | Pulled (2/2 files) |
| 04 Renovation / 01 Bud Studio / 04 Render Design | `1f0PYn98QEqUmQ4sZYhmFyICmXKmT5stS` | Pulled (2/2 files) |
| 04 Renovation / 02 Furnitures | `1wcva6H89tR3fXocLRpwSZSqP-pkq5EYc` | Pulled (subfolders walked) |
| 04 Renovation / 02 Furnitures / 01 Dining Table | `1dOADj19_f0R3YCpCJ0g5400k3L28jlc_` | Pulled (1/1 file) |
| 04 Renovation / 02 Furnitures / 02 Bed Frame + Mattress | `1E8Cn2uwGGjj2WSldhcB-vCzsF75NF6zI` | Pulled (1/1 file — photo-only, metadata recorded) |
| 04 Renovation / 02 Furnitures / 03 Fridge, Washer, Microwave | `1Vk08Xt4abS_ArULZxw33EwMRlZIDcFcg` | Pulled (2/2 files) |
| 04 Renovation / 02 Furnitures / 04 TV | `1qalFYiverZxQnp8q38FnX5rcuusAoYGx` | Pulled (1/1 file) |
| 04 Renovation / 02 Furnitures / 05 Aircon | `1gIWl_9AuZaaLLk1p3WgQGTSfwMAYj7BC` | Pulled (1/1 file) |

**Scope note:** Per the strict ingestion brief, ONLY the "04 Renovation" tree (and its full
descendant subfolder tree) was walked and pulled. "10. House Purchase" was left untouched
(Identified only, in a prior run) — do not pull it under the "Renovation" ingestion mandate.

## Pulled snapshots

| File | Source ID | Pulled | Local path |
|------|-----------|--------|------------|
| 02 Reno Sheet x Bud Studio [External] | `1cFfCsIXtQXqY4kU2dRp13rjjI5XJjmovX8wiUKnvV78` | 2026-06-07 | `raw/sheets/reno-sheet-bud-studio-2026-06-07.md` |
| 86 Dawson Road - Ownership Valuation | `1hYXyGA9EUXbc4fO8JFanUfK6-zxc5Q03NNCRBGItKDE` | 2026-06-07 | `raw/sheets/ownership-valuation-2026-06-07.md` |
| claude_Marcella_Quotation_26R532 | `1nULbgkhTZkKi0MGkyYfzCMKTedhfLB19H7FFwg0HxtQ` | 2026-06-07 | `raw/sheets/claude-marcella-quotation-26r532-2026-06-07.md` |
| 01 Floor plan - Dawson 05-03@141086.pdf | `10mFh8uI1siDVMx-Go0Ibxq-icDT61HRl` | 2026-06-07 | `raw/drive/floor-plan-dawson-05-03-2026-06-07.md` |
| 01 Skyville@Dawson x BUD Studio First Draft.pdf | `1WHxBM9QJQaFRnxPz_upCMFsa6yJBABGf` | 2026-06-07 | `raw/drive/skyville-dawson-bud-studio-first-draft-2026-06-07.md` |
| 02 Skyville@Dawson x BUD Studio First Draft - Comments.pdf | `1ceeyiRe8qx0S27cmgUa06LQ0JejdHZpK` | 2026-06-07 | `raw/drive/skyville-dawson-bud-studio-first-draft-comments-2026-06-07.md` |
| Signed_Renovation Contract_Marcella & Jefferson.pdf | `18OfpFxh8MKOAdUeMtD7ImELxNRw1-dYP` | 2026-06-07 | `raw/drive/signed-renovation-contract-marcella-jefferson-2026-06-07.md` |
| v2. J&M House Moodboard | `188yqJXVH4r1zaKrUSPvm9H17gH2ZKyGRR6F19LdChbA` | 2026-06-07 | `raw/drive/jm-house-moodboard-v2-2026-06-07.md` |
| J&M House Moodboard (original/v1) | `1Pp_f9MKXTjegUfhHeEPixa-eTHqnlUAC9JXTiLbbBpg` | 2026-06-07 | `raw/drive/jm-house-moodboard-2026-06-07.md` |
| 01 Dining Table - Other Furniture | `1AlqvI4is-6QnsmYShh-ENDcOshgLrn9Q` | 2026-06-07 | `raw/drive/dining-table-other-furniture-2026-06-07.md` |
| WhatsApp Image 2026-02-07 at 3.17.30 PM (Bed Frame ref — empty content) | `165urO1lTRA6mVmz75xQAxCUIFLmZ5Njs` | 2026-06-07 | `raw/drive/whatsapp-image-2026-02-07-bed-frame-2026-06-07.md` |
| 01 Fridge, Washer Dryer, Microwave (Gain City SO-B0000296807) | `1bJ_0w8X0mjZ8ZKp5RpBPLnUgeg0YVnlo` | 2026-06-07 | `raw/drive/fridge-washer-dryer-microwave-2026-06-07.md` |
| 02 Gain City Denza Lucky Draw | `1pCQ9Bjpogj6xw8DRWVL0s08rFQ4-K49n` | 2026-06-07 | `raw/drive/gain-city-denza-lucky-draw-2026-06-07.md` |
| 01 TV Samsung (Gain City SO-B0000296814) | `105oIgyrTizeerkdiZKQlJFL8LIxHqYq2` | 2026-06-07 | `raw/drive/gain-city-tv-samsung-2026-06-07.md` |
| 01 Aircon LG (Gain City SO-B0000296812) | `17en_0VRAZOjgg3BD-F8ZcYOR2bGxUzpe` | 2026-06-07 | `raw/drive/gain-city-aircon-lg-2026-06-07.md` |
| 01 Invoice FD-INV-0079 (Fruit Design / Bud Studio deposit) | `1jz1OLCt1WecRy_cvSUpF7W9YVjmrp5Fw` | 2026-06-07 | `raw/drive/fruit-design-invoice-fd-inv-0079-2026-06-07.md` |
| 02 Receipt FD-INV-0079 (paid 02 Apr 2026) | `1kjnW-QAp4-Z_ag7moh96F6oxLepub162` | 2026-06-07 | `raw/drive/fruit-design-receipt-fd-inv-0079-2026-06-07.md` |
| WhatsApp Image 2026-02-07 at 3.17.30 PM (ZX Design layout plan) | `18mDV5eIeDnHE3O3XfoR-4UcZUVW9WZGI` | 2026-06-07 | `raw/drive/zx-design-layout-plan-2026-06-07.md` |
| 26-Q0125--03 (2) — Senso Studio Quotation | `1xkgCycbPQWimdWKHpx2sql64M9CaWePd` | 2026-06-07 | `raw/drive/senso-studio-quotation-26-q0125-03-2026-06-07.md` |
| Marcella & Jeff (Dawson Rd) — Senso Studio | `1d73oPLtLK5NYVehYY6JLUxFn8u2Fyc8f` | 2026-06-07 | `raw/drive/senso-studio-marcella-jeff-dawson-rd-2026-06-07.md` |
| Quotation 106k — Senso Studio (26-Q0125--02) | `1zQb_9-NO_P9q5UOMTgwbyZHuVikX8BvY` | 2026-06-07 | `raw/drive/senso-studio-quotation-106k-2026-06-07.md` |
| Senso Studio Name Cards (Emily Neo + Joshua Lee, combined) | `1NXVllAyZlUgiReq2fwp20mbskQn3Jauh` / `1V04XdSTcmVhkU3HeXnUhrR6XaD5-edcD` | 2026-06-07 | `raw/drive/senso-studio-namecards-2026-06-07.md` |
| Marcella & Jeff Quotation V2 — KOVE Interior Design (ZX Design) | `1LCNu3EsJ-0BmpeA6wo1ZtQVm20KdCI2H` | 2026-06-07 | `raw/drive/zx-kove-marcella-jeff-quotation-v2-2026-06-07.md` |
| Reno Studio Quotation (The Good Rocket Pte Ltd, JN140326) | `1e8eVZ6kfwSwwsC_dqPf8Xk_dk_yRyOqs` | 2026-06-07 | `raw/drive/reno-studio-quotation-2026-06-07.md` |
| BUD Studio Quotation (handwritten/annotated draft, 13/3/26) | `1Mibeisq2om1Pz8mvYCWdfFA9thVAj5cx` | 2026-06-07 | `raw/drive/bud-studio-quotation-handwritten-2026-06-07.md` |
| Marcella_rev2 — Bud Studio Appendix A revision (27/3/26) | `18RzVMh7wmeIldZc0GlIy7oKzQqBNEwIl` | 2026-06-07 | `raw/drive/marcella-rev2-bud-studio-2026-06-07.md` |
| 02 Reno Sheet.xlsm (binary — metadata only, not extractable) | `1u1VyORHiyh6bZEH2M-RMw5fzFmJbQTL-` | 2026-06-07 | `raw/drive/reno-sheet-xlsm-archive-2026-06-07.md` |
| 01. By Luvina — 9 WhatsApp images (photo-only batch, metadata only) | folder `1X0gDPx3clK8SUxl_HAbWSiCRn7hYAT-8` | 2026-06-07 | `raw/drive/by-luvina-whatsapp-images-2026-06-07.md` |

**Total: 27 snapshot rows covering 38 distinct Drive files** (some rows combine multiple
Drive files: namecards = 2 PDFs; By Luvina = 9 JPEGs listed in one metadata batch file).

## Key Drive files (not yet pulled)

*(none remaining in-scope — the entire "04 Renovation" tree has been walked and every file
either extracted to `raw/` or recorded as a metadata-only entry with documented reason)*

The "House Purchase 2026" spreadsheet (`1BbsrIVfoETvS1fj5ycjo3ePdiL_U8EgFzAmVyUxjiVM`) was
checked and found to contain HOUSE-PURCHASE-scoped content (loan/ABSD/BSD/valuation tables),
not renovation content — **out of scope for the "04 Renovation" mandate, intentionally NOT
pulled**. It likely belongs under the separate "10. House Purchase" tree (also out of scope
for this ingestion run).
