# Update plan — phd/ai-hair-color-custom / android: approved v2 → draft 20261117-151025

## Spec files
- New spec set `specs/2026-11-17` (Figma-only):
  - Changed: AI Hair Color Custom - PM Figma 3287-89.md — the PM page re-read on 2026-11-17: board pm-ui changed
    (`figma-text.ts`: D6-21 now 8 recommended colours instead of 7, with their values #5A3E2B, #A88B70, #B8AE98,
    #E3DCCB, #66735A, #5B6E85, #C9918A, #B5562A). The other six PM boards are unchanged.
  - New: AI Hair Color - Design Figma 616-9324.md — the Design page 「261005_AI_hair_color」 of the Hair guideline file
    (given with the Kanban item), read for the first time: 13 screens drawn twice (two themes), boards `ds-hair-a` /
    `ds-hair-b`: Launcher, Edit Room, photo guide, photo picker, the room, free-user room, palette, and the Custom panel
    cases (1) no style, (2) Base Color only, (2-1) Generate → toast (two-colour style and Solid), (3) custom colour.
- Standing inputs: REQ-006 (this request); the 10 eBugs filed from run 2026-11-13-r1 (Rule 3); knowledge KP-134 (n/a).

## Design vs PM
The Design page is labelled 261005 and its Custom case frames carry no date, so the dates cannot tell which is newer:
the Design wins by default (Design first) and those rows say 「check on device」; the PM's 2026-11-17 colour edit is
newer and wins. The user rulings REQ-003 / REQ-004 stand until the user re-decides.

## Requirement changes
| Requirement | Change | Before | After |
|---|---|---|---|
| R-016 | source added | PM only | Design 686:1427 draws Custom first in the Solid row |
| R-017 | modified | Unset Custom cell: gradient with ＋ | Orange gradient tile with a magic-wand icon, label 「Custom」 (Design) |
| R-019 | modified | Half-screen sheet titled 「Custom」 with ⌄ at the top right | Bottom sheet with a grab handle; no title or ⌄ drawn (Q-17) |
| R-020, R-023, R-028, R-030, R-038 | source added | PM only | The Design draws the same |
| R-022 | modified | 7 recommended colours | 8 recommended colours, in the PM's HEX order (Q-21: the Design draws other swatches) |
| R-024 | modified | CMS list | + the Design's style names (「Ombre」 without accent; CMS decides) |
| R-027 | modified | Solid: the Highlight row does not appear | Solid: the Highlight row stays, greyed out (Design; Q-18) |
| R-029 | note | — | The Design disagrees with REQ-003 for Base only (Q-19); the ruling stands |
| R-033 | modified | Palette with a bottom ✕ ↩ ↪ ⊕ ✓ row (described) | No bottom row (Design 841:1429) |
| R-042 | modified | ⌄ collapses | Collapsing (Design: drag the handle down; PM: ⌄) applies (Q-17) |
| R-085 | new | — | A missing required colour: Generate grey, tap → toast 「Select both a base and highlight color.」 (answers Q-16) |
| R-086 | new | — | A palette colour is added as a new circle right after the wheel, selected |
| R-087 | new | — | Premium styles show a crown badge on the thumbnail (answers Q-6's icon part) |
| R-088 | new | — | Photo guide before the picker: Recommend / Avoid items, 「Continue」, 「Don't show again.」 |
| R-089 | new | — | Edit Room 「Quick Action」 row holds 「Hair Color」 |
| R-090 | new | — | Launcher 「AI Magic」 holds a 「Hair Color」 card |
| Q-2, Q-15 | modified | — | Narrowed by the Design |
| Q-16 | answered | — | By the Design's toast (R-085) |
| Q-17 – Q-21 | new | — | Collapse control, Solid's Highlight row, Base-only vs REQ-003, guide's hat item, swatch colours |

## Case changes
- New (2):
  - TC-092 (after TC-002): the photo guide's texts and 「Continue」 → photo picker (R-088).
  - TC-093: 「Don't show again.」 stops the guide on the next entry (R-088).
- Modified (26):
  - TC-001: entered from the Launcher 「Hair Color」 card (R-090).
  - TC-015: Edit Room entry through 「Hair Color」 in the Quick Action row (R-089).
  - TC-017: the unset Custom cell is the orange tile with a magic wand (R-017).
  - TC-018: taps every other category tab (Design 「Highlights」 / 「Ombré」, PM 「Multicolor」) instead of 「Multicolor」.
  - TC-019: bottom sheet with a grab handle; title / ⌄ recorded (Q-17); recheck PHA262026P0111.
  - TC-022: + the premium crown on style thumbnails (R-087).
  - TC-023: selected frame described as the Design's orange frame.
  - TC-024, TC-029: Solid greys out the Highlight row instead of hiding it (R-027, Q-18).
  - TC-026: Notes name the Design's disagreement (Q-19); expectation unchanged (REQ-003).
  - TC-027: Highlight only, then Generate → the toast, no charge (R-085).
  - TC-030: 8 recommended colours in the PM's HEX order (R-022).
  - TC-031: palette with no bottom row (R-033); recheck PHA262026P0113.
  - TC-032: the picked colour becomes a new selected circle right after the wheel (R-086).
  - TC-038, TC-054: collapse by dragging the handle down (⌄ if the build has one) (Q-17); rechecks P0115, P0119.
  - TC-069: the premium style is the one with the crown (R-087).
  - TC-021: Design reference; recheck PHA262026P0112.
  - Notes only (eBug recheck, Rule 3): TC-005 (P0110), TC-035 (P0113), TC-040 (P0115), TC-045 (P0116), TC-047 and
    TC-048 (P0117), TC-057 (P0118), TC-086 (P0114).
- Removed (0)
- Unchanged: 59 (their Notes now say the Design 616:9324 does not draw them).

## Found by the analysis
- The Design draws a toast for a missing colour where the PM drew an inline hint; with REQ-003 it shows for Highlight
  only (TC-027). The Design also draws Base-only as blocked: Q-19 for the user.
- Controls: 18 Design control groups traced (credit chip → TC-077, Artwork key → TC-055, 「Don't show again.」 →
  TC-093; Launcher, Edit Room and shared photo picker chrome n/a as other features; 「1 Free Trial」 n/a, Q-7).
  The Design draws the Custom tile, style thumbnails, swatches and wheels as plain frames: they are the same control
  groups the PM overrides already hold, traced to the same rows.
- Annotations: the Design boards carry no notes; their 118 phone-text blocks and the changed pm-ui block are traced.
- board-lint could not OCR the board images on this Windows machine (macOS Vision); its 8 pm-ui note-off warnings
  are the same as on 2026-11-12.
- 59 unchanged rows keep the older 「;」-joined Preconditions / Expected Results (check.ts warns); every row this
  draft changes or adds has one item per line.

## Not added (value check)
- The Design's colours and spacing (orange rings, sheet radius, swatch size): design-check items (figma skill
  conformance), not functional rows.
- 「1 Free Trial」 on the template row (Design free-user room): the 10/E template trial, not Custom (Q-7).
