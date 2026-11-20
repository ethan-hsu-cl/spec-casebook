// Builds this draft's requirements.md from the approved v2 one (user, 2026-11-17, REQ-006: re-analyse the PM page and
// the new Design page 616:9324). Run from this folder: node edit-requirements.ts. Fails on any edit whose anchor is gone.
import { readFileSync, writeFileSync } from 'node:fs';
let t = readFileSync('../../requirements.md', 'utf8').replace(/\r\n/g, '\n');
const rep = (a: string, b: string) => { if (!t.includes(a)) throw new Error('anchor gone: ' + a.slice(0, 80)); t = t.replace(a, b); };
const DS = 'https://www.figma.com/design/2VOqiPxBCISkob7wbM9hXD/Hair?node-id=616-9324';

rep(/^Spec: [\s\S]*?`\[PM:10\/E …\]`\.\n/m.exec(t)![0],
`Spec: AI Hair Color Custom - PM Figma 3287-89.md (text snapshot of PM Figma page 3287:89 「26 11E AI Hair Color Custom」,
https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3287-89, re-read 2026-11-17) and AI Hair Color - Design
Figma 616-9324.md (text snapshot of Design page 616:9324 「261005_AI_hair_color」, ${DS}, read 2026-11-17; boards
\`ds-hair-a\` / \`ds-hair-b\`, the same 13 screens in two themes). Figma-only. Rules the PM page cites from the 10/E Hair
Color spec (D1-xx, D2-xx, D3-xx) were read from page 3026:89 「26 10E AI Hair Color v2」 (\`extracted/hair-color-10e-rules.json\`)
and are tagged \`[PM:10/E …]\`.
Design vs PM (pass 7): the Design page is labelled 261005 and its Custom case frames (1)–(3) carry no date, so the dates
cannot tell which is newer: the Design wins by default (Design first, 2026-11-13) and each such row says 「check on
device」 in Notes; the PM's 2026-11-17 edit (8 recommended colours) is newer and wins. User rulings REQ-003 / REQ-004
stand until the user re-decides them.
`);

// Entry points drawn by the Design
rep('## Overview and Intro Demo\n', `## Overview and Intro Demo
- R-090 [DS:ds-hair-a 1-launcher 617:9493] The Launcher's 「AI Magic」 section has a 「Hair Color」 card; tapping it opens AI Hair Color.
- R-088 [DS:ds-hair-a 2-before_importing_photo 617:10539] Before the photo picker, a guide shows 「For the best results, we recommend photos with the following:」, under 「Recommend」 「Photo of One Female」, 「Full Upper Body」 and 「Clear Face」, under 「Avoid」 「Face Coverings」 and 「Face too small」, a 「Continue」 button and 「Don't show again.」 (10/E D2-02 also asks to avoid hats: Q-20).
`);
rep('- R-014 [PM:pm-face-check] Entering from Edit Room or a deeplink (photo already chosen), the four checks run in order at once (D2-01e, D1-10).',
  '- R-014 [PM:pm-face-check] Entering from Edit Room or a deeplink (photo already chosen), the four checks run in order at once (D2-01e, D1-10).\n- R-089 [DS:ds-hair-a 1_edit_room 788:1354] In Edit Room the 「Quick Action」 tool row holds 「Hair Color」 (after 「Hairstyle」); tapping it opens AI Hair Color with the photo being edited.');

// Custom cell
rep('- R-016 [PM:pm-ui custom_in_row] 「Custom」 is always the first cell',
  '- R-016 [PM:pm-ui custom_in_row; DS:ds-hair-a 4-hair_color 686:1427] 「Custom」 is always the first cell');
rep('- R-017 [PM:pm-ui custom_in_row] Before Custom is set, its cell shows a gradient background with ＋ and the label 「Custom」, and it is not selected; the first template stays selected (D6-01; the mockups draw a pencil icon, Q-2).',
  '- R-017 [DS:ds-hair-a 4-hair_color 686:1427; PM:pm-ui custom_in_row] Before Custom is set, its cell is an orange gradient tile with a magic-wand icon and the label 「Custom」, and it is not selected; the first template (「Platinum」) stays selected (Design; the PM note says gradient + ＋ and its mockups a pencil, Q-2).');

// Panel layout
rep('- R-019 [PM:pm-ui panel_open_no_style] The Custom panel is a half-screen sheet titled 「Custom」 with a ⌄ collapse key at the top right and three areas from top to bottom: ① Style ② Color ③ Generate (D6-02).',
  '- R-019 [DS:ds-hair-a 4-hair_color_case1_no_style 894:1474; PM:pm-ui panel_open_no_style] The Custom panel is a bottom sheet with a grab handle at the top and three areas from top to bottom: 「Style」, the colour rows (「Base Color」, 「Highlight Color」) and Generate (D6-02). The Design draws no 「Custom」 title and no ⌄ key; the PM draws both (Q-17).');
rep('- R-020 [PM:pm-ui panel_open_no_style] The panel has no undo / redo and no ✕ / ✓ (D6-16).',
  '- R-020 [PM:pm-ui panel_open_no_style; DS:ds-hair-a 4-hair_color_case1_no_style 894:1474] The panel has no undo / redo and no ✕ / ✓ (D6-16; the Design draws none either).');
rep('- R-022 [PM:pm-ui panel_open_no_style] The Color area has two rows titled 「Base Color」 and 「Highlight Color」; each row starts with a rainbow colour-wheel key with a ＋ badge, followed by 7 recommended colours (40 pt circles) that scroll sideways (D6-21).',
  '- R-022 [PM:pm-ui panel_open_no_style] The Color area has two rows titled 「Base Color」 and 「Highlight Color」; each row starts with a rainbow colour-wheel key with a ＋ badge, followed by 8 recommended colours (40 pt circles) in this order: #5A3E2B, #A88B70, #B8AE98, #E3DCCB, #66735A, #5B6E85, #C9918A, #B5562A, and scrolls sideways (D6-21, PM edit of 2026-11-17: was 7 colours with no values; the Design draws white and neutral beige-to-brown swatches, Q-21).');
rep('- R-023 [PM:pm-ui panel_open_no_style] Before a style is chosen,',
  '- R-023 [PM:pm-ui panel_open_no_style; DS:ds-hair-a 4-hair_color_case1_no_style 894:1474] Before a style is chosen,');

// Style
rep('- R-024 [PM:pm-cms] The Style area lists',
  "- R-087 [DS:ds-hair-a 4-hair_color_case1_no_style 894:1474] A premium (purchase) style shows a crown badge at the top right of its thumbnail (the Design draws it on 「Balayage」); free styles have none (answers Q-6's icon question).\n- R-024 [PM:pm-cms; DS:ds-hair-a 4-hair_color_case1_no_style 894:1474] The Style area lists");
rep('split_dye_vertical and split_dye_horizontal (D6-10, D6-13).',
  'split_dye_vertical and split_dye_horizontal (D6-10, D6-13). The Design draws the names 「Face」, 「Bangs」, 「Highlight」, 「Balayage」, 「Ombre」, 「Solid」 (ui_name from CMS decides).');
rep('- R-027 [PM:pm-ui panel_solid_color] solid_color takes one colour: only the 「Base Color」 row shows; the 「Highlight Color」 row does not appear (D6-04).',
  '- R-027 [DS:ds-hair-a 4-hair_color_case2-1_toast 929:1901; PM:pm-ui panel_solid_color] solid_color takes one colour: the 「Highlight Color」 row stays on screen but disabled (greyed out) while 「Base Color」 is enabled (Design; the PM says the Highlight row does not appear, D6-04: Q-18).');
rep('- R-028 [PM:pm-ui panel_solid_color] With solid_color, choosing a Base Color enables Generate (D6-04).',
  '- R-028 [PM:pm-ui panel_solid_color; DS:ds-hair-a 4-hair_color_case2-1_toast 929:1901] With solid_color, choosing a Base Color enables Generate (D6-04; the Design draws the orange Generate with ⬤ 6).');
rep('Highlight alone keeps Generate disabled (its message: Q-16).',
  'Highlight alone keeps Generate disabled. The Design draws the opposite for Base alone (Generate grey, the toast of R-085): Q-19; the ruling stands until the user re-decides.');
rep('- R-030 [PM:pm-ui panel_two_tone] The chosen colour in each row has a 2 pt #FFBE98 ring (D6-21).',
  `- R-085 [DS:ds-hair-a 4-hair_color_case2-1_toast 892:1796] With a two-colour style and a required colour missing, Generate looks disabled (grey) and tapping it shows the toast 「Select both a base and highlight color.」 over the photo, with no generation and no charge. Under REQ-003 this is the Highlight-only case (answers Q-16); the Design draws it for Base only (Q-19).
- R-030 [PM:pm-ui panel_two_tone; DS:ds-hair-a 4-hair_color_case3_custom_color 894:2637] The chosen colour in each row has a ring (PM: 2 pt #FFBE98; the Design draws an orange ring) (D6-21).`);

// Palette
rep("- R-033 [PM:pm-ui panel_palette] The colour-wheel key opens the app's existing colour palette: 「Cancel」 / 「Done」 on one line, a saturation-brightness square with a round cursor, a rainbow hue slider with a round handle, an eyedropper key right of the slider and a bottom row ✕ ↩ ↪ ⊕ ✓ (the bottom row is described but not drawn) (D6-05).",
  "- R-033 [DS:ds-hair-a 4-hair_color 841:1429; PM:pm-ui panel_palette] The colour-wheel key opens the app's existing colour palette in the sheet: 「Cancel」 at the left and 「Done」 at the right on one line, a saturation-brightness square, a rainbow hue slider with a round handle and an eyedropper key right of the slider (D6-05). The Design draws no bottom ✕ ↩ ↪ ⊕ ✓ row (the PM only described it).");
rep('- R-034 [PM:pm-ui panel_palette] The palette edits one slot at a time: the row whose wheel opened it receives the colour (D6-05).',
  '- R-034 [PM:pm-ui panel_palette] The palette edits one slot at a time: the row whose wheel opened it receives the colour (D6-05).\n- R-086 [DS:ds-hair-a 4-hair_color_case3_custom_color 894:2637] A colour picked in the palette is added to its row as a new circle right after the colour wheel, before the recommended colours, and is the chosen one (ring); the recommended colours move one place right.');

// Ready
rep('- R-038 [PM:pm-ui panel_ready] With a style', '- R-038 [PM:pm-ui panel_ready; DS:ds-hair-a 4-hair_color_case3_custom_color 894:2637] With a style');

// Collapse
rep('- R-042 [PM:pm-ui collapsed_applied; Req: REQ-004] The ⌄ key collapses the panel and applies the settings, never cancels (D6-08).',
  "- R-042 [PM:pm-ui collapsed_applied; Req: REQ-004] Collapsing the panel applies the settings, never cancels (D6-08): with the PM's ⌄ key, or, as the Design draws only a grab handle, by dragging the handle down (Q-17).");

// Questions
rep("- Q-2 How does the Custom cell look? The notes say a gradient with ＋ before it is set and the user's two colours after Apply; every mockup (flow and UI) draws a pencil icon instead. Assumption: the notes. R-017, R-044, TC-017, TC-038.",
  "- Q-2 How does the Custom cell look once applied? The PM note says it shows the user's two colours; the PM mockups draw a pencil icon and the Design draws only the unset cell (orange gradient with a magic-wand icon, now R-017). Assumption: the PM note (two colours). R-044, TC-038.");
rep("- Q-15 No Design file was supplied; every row is written from the PM page (PM-only) and the UI strings are the PM's. Rows change when the Design arrives.",
  '- Q-15 The Design page 616:9324 (read 2026-11-17) draws the room, the Custom panel states (1)–(3), the toast and the palette; everything else (Intro Demo, face checks, generating, result, deeplink, credits) is still PM-only and changes when the Design draws it.');
rep("- Q-16 With a two-colour style and only a Highlight Color chosen, Generate stays disabled (REQ-003), but which message (if any) tells the user a Base Color is needed? The ruling does not say. Assumption: no message is required; the row records what shows. R-029, TC-027.\n",
  `- Q-17 How is the Custom panel collapsed (applied)? The PM draws a 「Custom」 title with a ⌄ key at the top right; the Design draws only a grab handle and no title (filed PHA262026P0111 asked for ⌄). Assumption: the Design: dragging the handle down collapses and applies; a ⌄ is not required. R-019, R-042, TC-019, TC-038.
- Q-18 With 「Solid」, does the 「Highlight Color」 row disappear (PM D6-04) or stay greyed out (Design case 2-1)? Assumption: the Design (greyed out), check on device. R-027, TC-024, TC-029.
- Q-19 With a two-colour style and only a Base Color, the user ruled that Generate works (REQ-003, 2026-11-13), but the Design draws Generate grey and the toast 「Select both a base and highlight color.」 (cases 2 and 2-1). Which is right? Assumption: the ruling stands. R-029, R-085, TC-026.
- Q-20 The photo guide (Design) lists 「Face Coverings」 and 「Face too small」 under 「Avoid」; the 10/E rule D2-02 adds avoiding hats. Is a hat item expected? Assumption: the Design's list. R-088, TC-092.
- Q-21 The recommended colours: the PM (edited 2026-11-17) gives 8 HEX values starting #5A3E2B; the Design draws white and neutral beige-to-brown swatches. Assumption: the PM's list (newer). R-022, TC-030.
`);

// Exit × stage, Variants
rep('| Stage | ⌄ collapse |', '| Stage | Collapse (handle / ⌄, Q-17) |');
rep('| R-042 | ⌄ key | TC-038 |', '| R-042 | collapse (handle drag / ⌄) | TC-038 |');
rep('| R-029 | only Highlight Color filled | TC-027 |', '| R-029 | only Highlight Color filled | TC-027 |\n| R-085 | only Highlight Color, Generate tapped (toast) | TC-027 |\n| R-027 | style=solid_color, Highlight row greyed | TC-024 |');

// Domain rules new since v2
rep('| KP-050 | n/a (the spec states no locale scope; RTL not in scope) |',
  '| KP-050 | n/a (the spec states no locale scope; RTL not in scope) |\n| KP-134 | n/a (Adjustment room only; AI Hair Color has no Adjustment tabs) |');

// Ledger
rep('| REQ-005 | run entry (filing decisions); no table requirement |',
  '| REQ-005 | run entry (filing decisions); no table requirement |\n| REQ-006 | R-016, R-017, R-019, R-020, R-022, R-023, R-024, R-027, R-028, R-030, R-033, R-038, R-042, R-085–R-090 (Design read, PM re-read); filed eBugs PHA262026P0110–P0119 named in the rows that recheck them (Rule 3) |');

t += `
### eBug rechecks (Rule 3, REQ-006)
Filed from run 2026-11-13-r1 (TR261111-0042); each is rechecked by the row that found it, named in its Notes.
| BugCode | Rows |
|---|---|
| PHA262026P0110 | TC-005 |
| PHA262026P0111 | TC-019 (its ⌄ expectation conflicts with the Design: Q-17) |
| PHA262026P0112 | TC-021 |
| PHA262026P0113 | TC-031, TC-035 |
| PHA262026P0114 | TC-086 |
| PHA262026P0115 | TC-038, TC-040 |
| PHA262026P0116 | TC-045 |
| PHA262026P0117 | TC-047, TC-048 |
| PHA262026P0118 | TC-057 |
| PHA262026P0119 | TC-054 |
`;
writeFileSync('requirements.md', t);
console.log('requirements.md written');
