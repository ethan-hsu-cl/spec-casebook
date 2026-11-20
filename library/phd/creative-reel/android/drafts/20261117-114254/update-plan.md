# Update plan — phd/creative-reel / android: v2 → draft 20261117-114254

Same spec set (2026-11-02, `Creative Reel.pdf`), caught up with the PM Figma it was exported from (REQ-009, user
2026-11-17): PM page 7238:8623 section 「spec」, read through figma-pm in one inventory call (group p1), 9 board images
committed. Built on v2 (branch `phda-willy`, 2026-11-12 readability edit, REQ-008) by `build-draft.ts` and
`build-requirements.ts` (re-runnable). The Design Figma (node 976:11727) cannot be opened with the QA Design account
(qa-dm): it is analysed once access is given (Q-23, REQ-010). No iOS table (REQ-010).

134 rows: 121 unchanged, 13 modified, 7 new, 0 removed. Requirements R-114 – R-122 added, R-051 reworded; Q-3, Q-4,
Q-7, Q-10 answered; Q-23 – Q-26 new. Chinese reading copy `draft.zh-Hant.csv` (134 rows) and
`questions.zh-Hant.json` included.

## What the Figma has that the PDF did not
- **Intro page** (「Tutorial」 phone + note 【Demo video 調整】 • 文案同左): the room's intro with a new demo video,
  「Reel Creator」, 「Turn photos into post-worthy videos with trendy transitions, cinematic styles, and creative
  effects!」, 「Try Now」, 「Don’t show again」, 「‹」 → R-118 – R-122.
- **Picker memory note, three new clauses**: only templates with photo input > 1 show the prompt (R-117, answers
  Q-7); 「last picked」 = the set last applied with Next (R-115, answers Q-3); leaving the room ends the session and
  clears the memory (R-114, R-051 reworded). 「記憶只在 Reel Creator 內」 was red 待確認 in the PDF and is now a rule
  (R-116, answers Q-4).
- Arrows: the 10 drawn arrows now carry their Figma node ids (`arrows.json`); 7 the extractor took for pointers are
  kept as flows (`flow: true`).
- Controls: `inventory.json` has 59 controls (13 read from layers, 46 added by hand because the PM mockups draw
  buttons as plain frames); every one is pressed by a row (`control-trace.json`).

## New rows
- TC-128 – TC-132 (after TC-004): intro page shown, Try Now, Don’t show again (kept, also after relaunch), 「‹」,
  system Back.
- TC-133 (after TC-054): the remembered set is the one applied with Next.
- TC-134 (after TC-061): leaving the room clears the memory.

## Modified rows
- TC-054, TC-057 – TC-060: preconditions now apply the set with 「Next」 and stay in the room (R-115, R-114).
  TC-057 imports 4 (from a 4-photo AI Transition template) instead of the mockup's 3, because a 3-photo set cannot be
  applied with Next on any drawn template.
- TC-062: Q-4 answered: other pickers show no prompt (was 「record」, now an expected result, P2).
- TC-097: Q-7 answered: the Cinematic picker shows no prompt (P2).
- TC-005: the intro page must be dismissed first.
- TC-089: also taps the Artwork tabs (the Figma inventory lists them as a control).
- TC-013, TC-056, TC-113, TC-123: only re-split into one step per line (team rule 2026-11-03), wording unchanged.

## Order of the run
The intro rows run first, on a state where the intro still shows (TC-130 ticks 「Don’t show again」 for good; TC-005
and every later room entry assume it is ticked). The memory rows stay in their segment, TC-133 after TC-054 and
TC-134 after TC-061.

## Open questions
- Q-23 Design file not shared with qa-dm@cyberlink.com: UI strings still from the PM mockups.
- Q-24 When the intro page shows (assumed: every entry until ticked), and whether a template deeplink shows it.
- Q-25 Does opening My AI Artwork count as leaving the room for the memory?
- Q-26 Should Reel Creator results reach the Launcher's Recent (KP-027)?

## Not added (value check)
- The Figma's hidden layers (「Cloud backup expired …」 banner, 「Free credits here!」 tooltip in the room mockup):
  hidden in Figma, not drawn.
- KP-015, KP-018, KP-134: not in this flow (requirements.md › Domain rules).
- `board-lint.ts`: needs macOS Vision OCR, not available on this Windows machine; run it on a Mac before the run.
- Carried from v1: R-024 feature_id, R-025 schedule, CMS type split, generation failure (Q-12).
