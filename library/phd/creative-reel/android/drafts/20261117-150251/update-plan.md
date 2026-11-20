# Update plan — phd/creative-reel / android: approved v3 → draft 20261117-150251

Same spec set (2026-11-02, `Creative Reel.pdf` + PM Figma), now with the **Design Figma** (REQ-011, user
2026-11-17: access granted to qa-dm, Q-23). Built on v3 by `build-requirements.ts`, `build-draft.ts` and
`trace-controls.ts` (re-runnable, in this folder). No iOS table (REQ-010).

150 rows: 99 unchanged, 35 modified, 16 new, 0 removed. Requirements R-123 – R-133 added; R-006 – R-008, R-029,
R-031, R-033, R-035 – R-037, R-041 – R-044, R-049, R-052, R-060, R-061, R-064, R-067, R-068, R-073, R-074, R-078,
R-080, R-082, R-085, R-086 reworded to the Design; Q-23 answered, Q-10 / Q-12 updated, Q-27 – Q-36 new. Chinese copy
`draft.zh-Hant.csv` (150 rows) and `questions.zh-Hant.json` (Q-1 – Q-36) included. `check.ts`: 0 errors, 0 warnings.

## Spec files
- Unchanged: `Creative Reel.pdf`, PM Figma page 7238:8623 (group p1). New: Design Figma qdzVXIFZeYwcsa6fipmcLH.
- Design read through figma-design (qa-dm): page 933:4528 「261109_AI_transition_feature」 (the second link, node
  933-4528) holds section 「Design」 976:11727 (the first link), section 「PHD_spec」 933:4752 and frame 「PDR_SPEC」
  936:1971. One inventory call: group d1 = regions `ds-light` (7 iPhone screens + 3 Import-prompt cards) and `ds-dark`
  (the same 7 screens in dark), group d2 = `ds-pm-copy` (933:4752). Board images `extracted/figma/ds-light.png`,
  `ds-dark.png`, `ds-pm-copy.png` (1:1, cut from one section screenshot each). `figma-frames.json` has `files.design`
  with both links; `figma-pending.json` removed (nothing owed).
- `ds-pm-copy` is an **older copy of the PM 「spec」 section**: it still carries the 待確認 lines the PM page answers
  (R-114 – R-117) and has no intro page. Superseded by the PM page: its 3 arrows are `not_flow` (superseded), its one
  own control group n/a. `PDR_SPEC` is PowerDirector (other product, not read). The file's older pages (20260907,
  20260826, 260817, draft, result page) are earlier rounds, superseded by the 261109 page, not read.
- The Design draws screens only: no notes, no arrows. `figma-text.ts` has no baseline for these boards (compared by
  hand with the PM text); run `figma-text.ts --accept` once this draft is approved.

## Requirement changes (Design vs PM, pass 7 Design first)
The Design page is dated 2026-11-09; the PM items are undated and none cites a bug, so the Design wins wherever its
frames cover the case. The PM version is kept in the requirement or the row's Notes.
| Requirement | Change | Before (PM) | After (Design) |
|---|---|---|---|
| R-006 | reworded | 「Year-End Recap 📅」, 「Cool Transitions 🤳🏻」 | 「Year-End Recap 🎉」, 「Cool Transition 🎞️」 (「Christmas Time 🎄」 kept PM-only) |
| R-007 | reworded | cards in a row | + Cinematic Styles cards carry a small inset photo |
| R-008 | reworded | blue credit button | credit pill: blue diamond, balance, 「⊕」 |
| R-029, R-035, R-036 | reworded | 「View photo tips」 text at top left | ⓘ icon next to 「‹」 (that it opens the tips: Q-28) |
| R-031 | reworded | 「1 photo」 / 「5–15 photos」 | 「1 Photo」 with an image icon (range wording PM-only, Q-36) |
| R-041 | reworded | 「Add Photos」, 「Recents ▾」, 01, 02 … | 「Add photos」, 「Recent ⌄」, orange badges 1, 2, 3 and frame |
| R-042 | reworded | 「Select 5–15 photos」 + 「7/15」 | 「Select {min} to {max} photos to continue.」, no count, 「×」 on tray thumbnails |
| R-043 | reworded | red line, Next disabled | Next grey below min; red line PM-only (Q-30) |
| R-052 | reworded | text + Import + × | prompt card with thumbnails |
| R-060, R-061 | reworded | 「5–15 photos · output 9:16」, count at the right | count + 「9:16」 with icons (Q-31); 「Your photos (7/15)」 |
| R-064 | reworded | 「+」 last | 「+」 first, dashed orange frame |
| R-067, R-068 | reworded | 「Text language English ▾」, 「Generate | 60」 | 「Text Language」 bar with 「⌄」; Generate with credit icon |
| R-073, R-074 | reworded | dropdown, 「(Device language)」 | bottom sheet, 「Device Language」, English names (full list PM, Q-32) |
| R-078, R-080, R-082 | reworded | 「Processing…」, 「Character Motion Swap」, 「Create More」 | 「Processing...」, other tabs recorded, 「Create more」 |
| R-085, R-086 | reworded | 「1 photo · output 9:16」 | Design header format; Cinematic specifics stay PM (Q-35) |
| R-123 – R-124 | new | — | picker expand icon; tray 「×」 unpicks |
| R-125 – R-126 | new | — | prompt thumbnails and 「+N」; text variants for 3 / 2 / 1 photos (vs R-057: Q-27) |
| R-127 | new | — | Text Language sheet closes by the dimmed page / handle |
| R-128 – R-132 | new | — | Artwork ⓘ, 「Select」, 「Almost done」, 「Expires on」, 「Resume to Upload」 |
| R-133 | new | — | dark version of every screen (Q-34) |

## Case changes
- New (16): TC-136 tray 「×」 (after TC-041); TC-135 expand icon (after TC-051); TC-137 – TC-139 prompt for 3 / 2 / 1
  remembered photos (after TC-059); TC-140 sheet closed by the dimmed page / handle (after TC-078); TC-141 「Almost
  done」 (after TC-085); TC-142 「Expires on」 (after TC-086); TC-143 interrupted upload → 「Resume to Upload」 (after
  TC-088); TC-144 「Select」, TC-145 Artwork ⓘ (after TC-089); TC-146 – TC-149 dark theme (new section after App
  language); TC-150 system Back on the full photo view (after TC-106).
- Modified (35): TC-006, 007, 008 (room); TC-024, 030, 033, 035 (Preview / tips: ⓘ, 「1 Photo」); TC-037, 038, 040,
  042, 043, 051, 055, 068, 092, 093, 098, 099 (picker: 「Add photos」, 「Recent ⌄」, badges 1, 2, 3, tray wording, no
  count); TC-054 (prompt card with 「+4」); TC-063, 069, 094, 100 (confirm layout, 「Your photos (n/max)」; TC-069
  also checks Generate enabled again, pass 10b); TC-075, 076, 077, 078, 109 (Text Language sheet; TC-078 checks the
  tick follows the choice, pass 10b); TC-085, 089, 091, 113, 122 (Artwork: 「Processing...」, tabs, 「Create more」);
  TC-128 (Notes: PM-only, no Design frame).
- Removed: 0. Unchanged: 99.

## Found by the analysis
- Annotation trace: the Design boards have no notes; their screen text is traced in requirements.md › Annotation trace
  (ui), the tooltip 「Upload at leat 2 photos」 to Q-29, sample texts as labels; ds-pm-copy traced older.
- Pass 1 arrows: the Design draws none; the copy's 3 arrows are superseded (`not_flow`).
- Pass 2 job states: Creative generation now has Failure / Retry (TC-143) and a longest-wait state (TC-141).
- Pass 8 exits: full photo view (TC-135, TC-150) and the sheet's dimmed page (TC-140) added to Exit × stage and
  System back.
- Pass 9 hidden clauses: R-132 (a resumed upload charges once, TC-143), R-126 (N counts photos still in the Gallery,
  TC-137 – TC-139).
- Pass 9 one-way state: TC-137 – TC-139 delete photos from the Gallery (disposable photos, a fixture); TC-146 – TC-149
  switch the phone's theme (system setting: ask the user first, then switch back). No new 「Don't show again」 state.
- Pass 10 variants: R-126 × 4+ / 3 / 2 / 1 remembered; R-133 × light / dark (appearance, not combined with other
  settings; no `name=value` settings, so no Combinations grid).
- Pass 10b control states: 「Next」 grey / enabled on pick, unpick (badge, tray 「×」) and Import; 「Generate」 enabled
  again after 「+」 (TC-069); the sheet's tick follows the choice (TC-078).
- Pass 11 controls: `inventory.json` now 179 controls (Design 84 read + adds for template cards, grid photos, expand
  icon, prompt 「×」, photo tiles, Text Language bar, language rows, sheet backdrop, Artwork tabs / 「Select」 / cards,
  light and dark); `control-trace.json` 63 groups, all traced (32 by hand in `trace-controls.ts`: decorative icons,
  the tooltip icon, an empty layer and the superseded copy n/a). The tray 「×」 and the confirm photo 「×」 share a
  component but are traced to their own rows (TC-136, TC-065).
- Standing inputs: request ledger (REQ-011 added), domain knowledge (`knowledge.md`, same 108 entries as v3: no new
  rule applies), no new tickets or build notes for this table.

## Not added (value check)
- The tooltip 「Upload at leat 2 photos」: when it shows is not stated (Q-29); no row until answered.
- `ds-pm-copy` content: superseded by the PM page (already in the table).
- The Design's sample texts (「Micro Cinema」 on the confirm frame with 7/15, 「Image to Video - A Template Name 2」,
  「10 Outfits」, 2025 dates): mockup content.
- The Design's 「SwipeHint_Peek」 frame: same rule as TC-021 (R-033), no new row.
- `board-lint.ts`: needs macOS Vision OCR (read nothing on this Windows machine); run it on a Mac before the run.

## PM-only rows (no Design frame yet, Design 2026-11-09)
- Intro page TC-128 – TC-132; Edit Room jump TC-010 – TC-013; deeplink TC-014 – TC-020, TC-114; photo tips sheet
  TC-033 – TC-036; red tray line after Import TC-057, TC-058 (and TC-038, Q-30); confirm toast TC-067; Cinematic
  confirm specifics TC-094, TC-095; AI Transition 「Select N photos」 TC-098 – TC-102.

## Order of the run
New rows run in their segments right after the rows they extend (REQ-033); changed rows are re-run in the next round.
TC-137 – TC-139 each need their own 4 disposable photos. The dark-theme rows (TC-146 – TC-149) run together at the end
of a segment, after the user's go-ahead to switch the phone's theme, and switch it back.

## Questions for PM / Design
- Q-27 1-photo Import prompt (Design) vs no prompt for 1 (PM R-057).
- Q-28 Is the Preview's ⓘ the photo tips entry?
- Q-29 Picker expand icon target; the 「Upload at leat 2 photos」 tooltip.
- Q-30 Red tray line for a manual pick below min.
- Q-31 「9:16」 in the confirm header (drawn on one frame only) and its count wording.
- Q-32 Text Language: 8 languages (Design) vs every PhD language (PM); closing the sheet without a choice.
- Q-33 Artwork ⓘ, 「Select」 and the 「Expires on」 retention on the Reel Creator tab.
- Q-34 What turns on the dark version.
- Q-35 The Design confirm frame's Cinematic sample with 7/15 and Text Language.
- Q-36 Count wording: 「1 Photo」 / 「Select 5 to 10 photos to continue.」 (Design) vs PM wording where Design is silent.

## Questions for you
- None blocking. Switching the QA phone to dark theme for TC-146 – TC-149 needs your go-ahead at run time.
