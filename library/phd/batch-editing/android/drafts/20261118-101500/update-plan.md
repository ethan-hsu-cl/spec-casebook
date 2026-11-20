# Update plan — phd/batch-editing / android: approved v8 → draft 20261118-101500

Requests: REQ-019 (「幫我用這兩個figma更新batch editing」, Android only) and REQ-020 (「android要以figma為主」), user,
2026-11-18. Rows: 177 (new 6, modified 3, unchanged 168, removed 0).

**Base changes from the PDF exports (spec set 2026-11-09) to the PM and Design Figma (spec set 2026-11-09-figma).** The
PDFs stay as the older export of the same pages; where they differ the Figma wins, and Design first over PM
(AGENTS.md, 2026-11-13). Because the Figma is read through Figma, this draft has the inventory and the control trace
the PDF-only table never had (102 control groups, 31 flow arrows), and `check.ts` no longer warns "PDF-only".

## What the Figma check found (2026-11-18)
- PM file (page 0:1, 25 boards): unchanged since the 2026-11-11 read.
- Design file (page 12:2321): a **new board 225:3699** draws the Launcher with the 「Batch Edit」 tile in the
  「Features」 grid (second row, between 「AI Removal」 and 「Beautify」). No other text, control or arrow changed.

## What moving to the Figma found
Tracing every Figma control and arrow to a row (instead of reading the PDF by eye) found what no Android row pressed:
- The batch Adjustment tools: 「Auto」 (magic wand), 「AI Exposure」, Exposure / Contrast / Highlight one by one, and
  ⓘ at the top left.
- Curve's compare and reset buttons (TC-159 only looked at them).
- The greyed 「Enhanced」 button.
- The Design arrow AI Enhance ✓ → Batch Edit Room (only ✕ had a row).
Every quoted UI string in the rows was compared with the Figma text: all match, or differ only by the photo count
(「(3/20)」, 「Enhancing k / 3」…) or by a typo already open as a question (「detaill」, Q-10).

## Requirement changes
| Requirement | Change | Before | After |
|---|---|---|---|
| R-022 | reworded | shortcut planned, not drawn | Design draws 「Batch Edit」 in the Features grid |
| R-090 | **changed** | no AI Exposure (PM) | 「AI Exposure」 between Exposure and Contrast (Design first); Android paid entry KP-014 |
| R-239 | new | | ⓘ opens the existing Adjustment help (Design-only, Q-23) |
| R-240 | new | | 「Auto」 adjusts the current photo; 「All」 copies it |
| R-241 | new | | Figma arrow 16:13763: AI Enhance ✓ → Batch Edit Room |
| R-200 – R-235 | Figma arrow added | PDF arrow only | each names the Figma arrow it repeats |

## Rows
- Modified: **TC-022** — Launcher 「Batch Edit」 at its drawn place, P3 → P2 (REQ-019).
- Modified: **TC-070** — expects 「AI Exposure」 and ⓘ (was: no AI Exposure).
- Modified: **TC-157** — also taps the greyed 「Enhanced」: nothing happens.
- New after TC-070: **TC-175** ⓘ, **TC-172** each slider tool and AI Exposure (Premium 「Try it」), **TC-173** AI
  Exposure as Free (「Upgrade to VIP」), **TC-174** 「Auto」 + 「All」.
- New after TC-170: **TC-176** Curve compare and reset.
- New after TC-092: **TC-177** AI Enhance ✓ returns with every photo enhanced.

## Open questions
- Q-12 (Design read from PDF exports) → answered: the table is now read through Figma.
- Q-15 reworded (the shortcut is drawn; its landing is still open).
- Q-18 (AI Exposure): assumption now the Design (was PM).
- Q-23 new: what ⓘ opens.

## Rulings (REQ-021, the user's answers on the Cases page, 2026-11-18)
| Question | Answer | Requirements | Rows |
|---|---|---|---|
| Q-1 | 「Next」 lights up once a photo is selected | R-015 | TC-005 modified |
| Q-3 | Setting = the Edit Room's Setting | R-039 | TC-025 modified |
| Q-4 | compare: hold shows the original | R-039 | TC-026 modified (Notes) |
| Q-5 | crop Apply to all follows 「✅ 結論」 (relative position), not DR-07's 「centred」 | R-061 | TC-047, TC-051 – TC-053 already followed it |
| Q-13 | numbers move up in order; 「Next」 grey with none; expand opens the album selection screen | R-015, R-019, R-233 | TC-009, TC-010 (both P3 → P2), TC-150, TC-151 modified |

Rows are now 177 (new 6, modified 10, unchanged 161).

## Not added
- Nothing left out: every Figma control is pressed by a row or n/a with a reason (the Launcher's other features, the
  PM's icon-option draft board, the unchanged single Edit Room, the credit pill / History of Q-19).

## After approval
- `specs/2026-11-09/extracted/figma-pending.json` (the PDF set's owed Figma reads) can be deleted: the reads are done in
  spec set 2026-11-09-figma.
- The rows that change what runs (TC-070, TC-157, TC-172 – TC-177, TC-022) go first in the next round (REQ-033).
