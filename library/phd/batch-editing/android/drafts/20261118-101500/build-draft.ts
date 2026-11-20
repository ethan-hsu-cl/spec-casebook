// Draft 20261118-101500 (android), REQ-019: approved v8 plus the Design Figma change read 2026-11-18 (new Launcher
// board 225:3699 drawing the 「Batch Edit」 shortcut in the Features grid): TC-022 modified; R-022, Q-15 reworded.
// Run from the repo root: node library/phd/batch-editing/android/drafts/20261118-101500/build-draft.ts
import { readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { readRecords, writeRecords } from '../../../../../../scripts/lib/csv.ts';

const and = 'library/phd/batch-editing/android';
const here = join(and, 'drafts/20261118-101500');
const COLS = ['ID', 'Section', 'Precondition', 'Action', 'Expected Result', 'Priority', 'Spec Ref', 'Notes', 'Change', 'Change Reason'];
const read = (p: string) => readFileSync(p, 'utf8').replace(/^﻿/, '').replace(/\r\n/g, '\n');

const rows = readRecords(read(join(and, 'cases.csv'))).map(r => ({ ...r, Change: 'unchanged', 'Change Reason': '' }));
const r22 = rows.find(r => r.ID === 'TC-022')!;
Object.assign(r22, {
  Precondition: '1. Signed in with a PhotoDirector Premium account\n2. Launcher open',
  Action: '1. On the Launcher look at the 「Features」 grid\n2. Tap 「Batch Edit」',
  'Expected Result': 'Step 1: 「Batch Edit」 with its own icon is in the second row of the Features grid, between 「AI Removal」 and 「Beautify」\n' +
    'Step 2: Batch Edit opens\nStep 2: The run records where it lands (assumed: the Photo Picker on 「Batch」, Q-15)',
  Priority: 'P2',
  Notes: 'Design Launcher board 225:3699 (read 2026-11-18) draws the shortcut and names it 「Batch Edit」; UI UX flow 2 still says its icon is to be designed. No arrow from it: landing still Q-15. Deeplink: TC-152.',
  Change: 'modified',
  'Change Reason': 'REQ-019: the Design now draws the Launcher 「Batch Edit」 shortcut in the Features grid (R-022); P3 → P2 now that it is drawn',
});
// REQ-020 (user, 2026-11-18: 「android要以figma為主」): the table's base becomes the Figma spec set 2026-11-09-figma.
// Tracing every Figma control (controls.ts) found Design Adjustment controls no row pressed (Auto, AI Exposure and the
// other slider tools, ⓘ, Curve compare / reset, the greyed 「Enhanced」); AI Exposure follows the Design (Design first).
const P = '1. Signed in with a PhotoDirector Premium account\n2. Batch Edit Room open with 12 photos (Launcher 「Edit」 › 「Batch」), no edit yet\n3. Adjustment room open on photo 1';
const mod = (id: string, f: Record<string, string>) => Object.assign(rows.find(r => r.ID === id)!, f, { Change: 'modified' });
mod('TC-070', {
  'Expected Result': 'Same as the 26\'10/E Adjustment room\nNo Subject Detection\n「AI Exposure」 is in the tool row between 「Exposure」 and 「Contrast」 (Design)\n「Apply to all」 (icon + 「All」, semi-transparent dark capsule) at the top right\nⓘ at the top left\nBatch strip at the bottom',
  'Spec Ref': 'R-090, R-091, R-097, R-239',
  Notes: 'Every Design Adjustment frame draws 「AI Exposure」; PM DR-06 says none (Q-18): rows follow the Design (Design first, 2026-11-13).',
  'Change Reason': 'REQ-020: Android follows the Figma; the Design draws 「AI Exposure」 and ⓘ in the batch Adjustment room (R-090, R-239; was: no AI Exposure, PM)',
});
mod('TC-157', {
  Action: '1. Tap 「AI Enhance」 again\n2. Tap 「Enhance」\n3. Tap 「Start」\n4. Tap 「Enhanced」',
  'Expected Result': 'Step 1: On the new visit the button reads 「Enhance」 (enabled)\nStep 2: The dialog reads 「Enhance 3 photos?」\nStep 3: All 3 are enhanced again from their enhanced results\nStep 3: Then the button reads 「Enhanced」 greyed\nStep 4: Nothing happens (no dialog, no processing)',
  'Change Reason': 'REQ-020: the greyed 「Enhanced」 button the Figma draws (pm-ui-5) is now pressed (R-116)',
});
const add = (after: string, r: Record<string, string>) => rows.splice(rows.findIndex(x => x.ID === after) + 1, 0, { Change: 'new', ...r });
add('TC-070', { ID: 'TC-175', Section: 'Adjustment', Precondition: P, Action: 'Tap ⓘ at the top left',
  'Expected Result': 'The existing help for Adjustment opens\nClosing it returns to the batch Adjustment room with nothing changed',
  Priority: 'P3', 'Spec Ref': 'R-239', Notes: 'Design-only icon; what it opens is not stated (Q-23).',
  'Change Reason': 'REQ-020: the Design draws ⓘ (top/ic_info) in the batch Adjustment room; no row pressed it' });
add('TC-175', { ID: 'TC-172', Section: 'Adjustment', Precondition: P,
  Action: '1. On 「Light」 tap Exposure, Contrast and Highlight in turn and move the slider for each\n2. Tap 「AI Exposure」',
  'Expected Result': 'Step 1: Each tool changes photo 1 only\nStep 1: Each tool enables 「All」\nStep 2: A Premium user gets the 「Try it」 dialog, and 「Try it」 opens the AI Exposure screen (KP-014)\nStep 2: Record what the batch room does after AI Exposure (whether its result comes back to photo 1)',
  Priority: 'P2', 'Spec Ref': 'R-090, R-095', Notes: 'AI Exposure in batch is Design-only (Q-18); its Android paid entry is KP-014.',
  'Change Reason': 'REQ-020: the Design draws Exposure, AI Exposure, Contrast and Highlight; no row pressed the tools one by one' });
add('TC-172', { ID: 'TC-173', Section: 'Adjustment',
  Precondition: '1. Signed in with a Free (non-Premium) account\n2. Batch Edit Room open with 12 photos (Launcher 「Edit」 › 「Batch」), no edit yet\n3. Adjustment room open on photo 1',
  Action: 'Tap 「AI Exposure」', 'Expected Result': 'The 「Upgrade to VIP」 dialog opens (no Try Before Buy)\n「Upgrade」 opens the IAP page\nClosing the IAP page returns to the batch Adjustment room',
  Priority: 'P2', 'Spec Ref': 'R-090', Notes: 'Free variant of TC-172 (KP-014); batch Crop / Adjustment stay free (TC-082).',
  'Change Reason': 'REQ-020: AI Exposure follows the Design; on Android it is paid-only (KP-014), so the Free variant gets its own row' });
add('TC-173', { ID: 'TC-174', Section: 'Adjustment', Precondition: P, Action: '1. Tap 「Auto」\n2. Tap 「All」',
  'Expected Result': 'Step 1: Auto adjusts photo 1\nStep 2: The toast 「Applied to 11 photos」 shows\nStep 2: Every other photo gets the same settings in the strip',
  Priority: 'P2', 'Spec Ref': 'R-240, R-092, R-093', Notes: '',
  'Change Reason': 'REQ-020: the Design and PM draw 「Auto」 (magic wand) first in the tool row; no row pressed it' });
add('TC-170', { ID: 'TC-176', Section: 'Adjustment', Precondition: P + '\n4. Color › Curve open with the RGB curve pulled up in the middle',
  Action: '1. Press and hold the compare button on the photo\n2. Release it\n3. Tap the reset button',
  'Expected Result': 'Step 1: The photo shows without the curve while held\nStep 2: The curve shows again\nStep 3: The curve goes back to a straight line and photo 1 to its look before the curve',
  Priority: 'P3', 'Spec Ref': 'R-230', Notes: '',
  'Change Reason': 'REQ-020: the Design Curve frame draws compare (btn_BA) and reset (ic_mask) buttons; TC-159 only looked at them' });
add('TC-092', { ID: 'TC-177', Section: 'AI Enhance',
  Precondition: '1. Signed in with a PhotoDirector Premium account\n2. Batch Edit Room open with 12 photos (Launcher 「Edit」 › 「Batch」), no edit yet\n3. AI Enhance page open',
  Action: '1. Tap 「Enhance」 › 「Start」 and let the batch finish\n2. Tap ✓',
  'Expected Result': 'Step 2: Batch Edit Room shows\nStep 2: Every photo in the strip shows its enhanced result',
  Priority: 'P1', 'Spec Ref': 'R-241', Notes: '',
  'Change Reason': 'REQ-020: the Design flow arrow 16:13763 (AI Enhance ✓ → Batch Edit Room) had no Android row' });
// REQ-021 (user's answers on the Cases page, 2026-11-18): Q-1, Q-3, Q-4, Q-5, Q-13
const rule = (id: string, f: Record<string, string>, why: string) => mod(id, { ...f, 'Change Reason': `REQ-021 ruling: ${why}` });
rule('TC-005', { 'Expected Result': 'The 「Batch」 tab is highlighted\nA bottom bar shows the hint 「Select 1 to 20 photos to continue. (0/20)」 and 「Next」\n「Next」 is grey (no photo selected)',
  Notes: 'Design copy (REQ-004). Ruling REQ-021 (Q-1, Q-13): 「Next」 is grey until a photo is selected.' }, '「Next」 is grey with no photo and lights up once one is selected (Q-1, Q-13)');
rule('TC-009', { 'Expected Result': 'Photo 2 is deselected\nPhoto 3 is renumbered to 2\nThe hint ends 「(2/20)」', Priority: 'P2', Notes: 'Ruling REQ-021 (Q-13).' },
  'the numbers after a deselected photo move up in order (Q-13; was: record whether they do)');
rule('TC-150', { 'Expected Result': 'Photo 2 leaves the tray and its tile loses the number\nThe hint ends 「(2/20)」\nPhoto 3 is renumbered to 2 on its tile and in the tray', Notes: 'Ruling REQ-021 (Q-13).' },
  'the numbers after a deselected photo move up in order (Q-13)');
rule('TC-151', { 'Expected Result': 'The album selection screen opens\nClosing it returns to the picker with nothing selected', Notes: 'Ruling REQ-021 (Q-13): the expand icon opens the album selection screen.' },
  'the tile\'s expand icon opens the album selection screen (Q-13; was: assumed to open the photo large)');
rule('TC-010', { 'Expected Result': '「Next」 is grey\nTapping it does nothing\nBatch Edit Room does not open', Priority: 'P2', Notes: 'Ruling REQ-021 (Q-13).' },
  '「Next」 is grey with no photo selected (Q-13; was: record)');
rule('TC-025', { 'Expected Result': 'The same Setting page as the single-photo Edit Room\'s Setting opens\nClosing it returns to Batch Edit Room with nothing changed', Notes: 'Ruling REQ-021 (Q-3).' },
  'Setting opens the same page as the Edit Room\'s Setting (Q-3; was: record what opens)');
rule('TC-026', { Notes: 'Ruling REQ-021 (Q-4): hold shows the original, as in Edit Room.' }, 'compare confirmed as in Edit Room (Q-4; was: assumed)');
writeFileSync(join(here, 'draft.csv'), '﻿' + writeRecords(COLS, rows));

let req = read(join(and, 'requirements.md'));
const line = (re: RegExp) => req.split('\n').find(l => re.test(l))!;
req = req.replace(line(/^- R-022 /),
  '- R-022 [PM:entry-batch-shortcut; DS:design-launcher 225:3699] The Launcher has a Batch Edit shortcut: the Design Figma (read 2026-11-18) draws 「Batch Edit」 with its own icon in the Launcher 「Features」 grid, second row between 「AI Removal」 and 「Beautify」 (UI UX flow 2: icon still to be designed, after Meitu; Design first). The deeplink `phd://navigate/page?name=batch_edit` opens Batch Edit; where the shortcut and the deeplink land is not stated (Q-15).');
req = req.replace(line(/^- Q-15 /),
  '- Q-15 Where do the Launcher 「Batch Edit」 shortcut and the deeplink `phd://navigate/page?name=batch_edit` land (Photo Picker on 「Batch」?), and is the shortcut in 26\'11/E? The Design Launcher board 225:3699 (2026-11-18) now draws the shortcut in the Features grid but no arrow from it, while D0-04 still says Batch Edit appears only in the two pickers. Assumption: both open the Photo Picker on 「Batch」; rows record it. (R-022, TC-022, TC-152)');
req = req.replace(/(\n\*\*Also read \(REQ-011, 2026-11-11\):\*\*)/,
  '\n**Re-read 2026-11-18 (REQ-019):** the Figma change check found the PM page unchanged and one new Design board, 225:3699 「launcher · Light · orange · rest」, with the 「Batch Edit」 shortcut in the Launcher Features grid (R-022, Q-15).\n$1');
req = req.replace(/(\| REQ-013 \| [^\n]*\n)/, '$1| REQ-019 | R-022 (Design Launcher board 225:3699 draws the 「Batch Edit」 shortcut; TC-022) |\n');
// REQ-020: Figma as the base
req = req.replace(/^Spec: [\s\S]*?\n\n/, 'Spec: **the PM and Design Figma (REQ-020, 2026-11-18)**: spec set 2026-11-09-figma (PM page 0:1 「26\'11/E Batch editing: AI enhance, crop & rotate, adjustments」, Design page 12:2321 「261104_design」), read through Figma (inventory, control trace, board text). The PDF set 2026-11-09 (UI UX flow 2.pdf, Section 3 · 美圖 Apply to all 實測.pdf, the per-frame `Design - *.pdf` exports) is an older export of the same pages: its `[PM:<board>]` / `[DS:ds-*]` tags below name the board the rule was first read from, and where the PDF and the Figma differ the Figma wins (KF-005). Design first over PM (AGENTS.md, 2026-11-13).\n\n');
req = req.replace(line(/^- R-090 /),
  '- R-090 [PM:adjust-default; D1-11, DR-03, DR-06; DS:design-light-adjust 「adjust」 41:923; REQ-020] The room matches the 26\'10/E Adjustment room (Light / Color / Details), without Subject Detection; the tool row has 「AI Exposure」 between 「Exposure」 and 「Contrast」 as every Design Adjustment frame draws (PM DR-06 says none: Q-18; Design first). On Android AI Exposure keeps its paid-only entry (KP-014).');
req = req.replace(line(/^- R-230 /), line(/^- R-230 /) +
  '\n- R-239 [DS:design-light-adjust 41:923 「top/ic_info」; REQ-020] ⓘ at the top left of the batch Adjustment room opens the existing help for Adjustment (Design-only; what it opens: Q-23).' +
  '\n- R-240 [DS:design-light-adjust 「adjust」 「ic_magic_wand」; PMF:pm-flow-2 「Auto」; REQ-020] The first tool, 「Auto」, adjusts the current photo automatically; like any setting of the room, 「All」 copies it to every other photo (R-092).');
const q12 = line(/^- Q-12 /);
req = req.replace(q12 + '\n', '');
req = req.replace(line(/^- Q-18 /),
  '- Q-18 PM (DR-06, also in the re-exported PDF) says the Adjustment room shows no AI Exposure; every Design Adjustment frame draws 「AI Exposure」 between 「Exposure」 and 「Contrast」. Which holds? Assumption (REQ-020, Design first): AI Exposure is shown, with its Android paid entry (KP-014); the rows record what the app shows. (R-090, TC-070, TC-172, TC-173)');
req = req.replace(line(/^- Q-22 /), line(/^- Q-22 /) +
  '\n- Q-23 The Design draws ⓘ at the top left of the batch Adjustment room; PM does not mention it. Does it open the existing Adjustment help? Assumption: yes; the row records what opens. (R-239, TC-175)');
req = req.replace('\n## Answered questions\n', '\n## Answered questions\n- Q-12 (Design read from PDF exports, not through Figma) — answered by REQ-020, 2026-11-18: the table is based on the Figma spec set 2026-11-09-figma, read through Figma (inventory of 102 control groups, all traced in control-trace.json); the four boards the old read missed are gone from the file.\n');
req = req.replace(line(/^\| KP-014 /), '| KP-014 | R-090 (AI Exposure shown per the Design: Premium 「Try it」 TC-172, Free 「Upgrade to VIP」 TC-173) |');
req = req.replace(line(/^\| KP-025 /), '| KP-025 | n/a (where an AI Exposure result from the batch room goes is recorded by TC-172; batch saves go to the gallery, R-150) |');
req = req.replace(/(\| R-013 \| Free user, 20 photos[^\n]*\n)/, '$1| R-090 | Premium user, AI Exposure (「Try it」, KP-014) | TC-172 |\n| R-090 | Free user, AI Exposure (「Upgrade to VIP」, KP-014) | TC-173 |\n');
req = req.replace(/(\| REQ-019 \| [^\n]*\n)/, '$1| REQ-020 | R-090, R-116, R-230, R-239, R-240, R-241 (Figma as the base: every Figma control and flow arrow traced; TC-070, TC-157 modified, TC-172 – TC-177 new) |\n');
// the Figma flow arrows (spec set 2026-11-09-figma arrows.json) on the PDF-read flow requirements they repeat
const FIGMA_ARROWS: Record<string, string[]> = {
  'R-200': ['16:10599'], 'R-201': ['16:10603'], 'R-202': ['16:10607'], 'R-203': ['16:10611'], 'R-204': ['16:10615'],
  'R-205': ['16:11038'], 'R-206': ['297:3116'], 'R-207': ['16:11042'], 'R-208': ['16:11813'], 'R-209': ['31:1858'],
  'R-210': ['16:11821'], 'R-211': ['31:1863'], 'R-212': ['16:11829'], 'R-214': ['16:12859'], 'R-215': ['16:12863'],
  'R-216': ['16:12867'], 'R-217': ['151:2352'], 'R-218': ['16:13109'], 'R-219': ['137:4368'], 'R-220': ['16:13426'],
  'R-221': ['16:13430'], 'R-222': ['141:2038'], 'R-223': ['141:2042'], 'R-224': ['141:2046'], 'R-225': ['16:13746'],
  'R-226': ['16:13750', '37:2034'], 'R-227': ['16:13754'], 'R-228': ['16:13758'], 'R-235': ['357:2620'],
};
for (const [id, ids] of Object.entries(FIGMA_ARROWS)) {
  const l = line(new RegExp(`^- ${id} \\[`));
  req = req.replace(l, l.replace(/ \] /, ` ; DS: ${ids.map(a => `flow arrow ${a} `).join('; ')}] `));
}
req = req.replace(line(/^- R-235 /), line(/^- R-235 /) +
  '\n- R-241 [DS: flow arrow 16:13763 ; REQ-020] AI Enhance ✓ → Batch Edit Room: ✓ returns with every photo enhanced. Walked by: TC-177.');
req = req.replace('The PDF has no Figma links, so arrows are read from the drawn flows (`arrows.json`, node = `<board>-a<n>`).',
  'Read first from the PDF\'s drawn flows (node = `<board>-a<n>`); since REQ-020 each also names the Figma arrow it repeats (`DS: flow arrow <node>`, spec set 2026-11-09-figma `arrows.json`).');
// REQ-021 rulings (Q-1, Q-3, Q-4, Q-5, Q-13)
const set = (re: RegExp, text: string) => { req = req.replace(line(re), text); };
set(/^- R-015 /, '- R-015 [PM:picker-batch, entry-enhance-shortcut; DR-01; DS:ds-photo-picker; ruling REQ-021] The bottom bar of the Batch tab shows the hint with the count, 「Select 1 to 20 photos to continue. (n/20)」, and 「Next」 (Design copy; PM draws 「n selected (max 20)」 and 「Done」); 「Next」 is grey with no photo selected and lights up as soon as one is selected (Q-1, Q-13 answered).');
set(/^- R-019 /, '- R-019 [DS:ds-photo-picker; ruling REQ-021] On the Batch tab a tray under the bottom bar lists the selected photos in selection order, each with ✕; ✕ (or tapping the tile again) deselects that photo: the tile loses its number, the count drops and the numbers of the photos after it move up in order (Q-13 answered).');
set(/^- R-233 /, '- R-233 [DS:ds-photo-picker; ruling REQ-021] Every picker tile carries an expand icon at its bottom right; it opens the album selection screen (Q-13 answered).');
set(/^- R-039 /, '- R-039 [PM:room-default; ruling REQ-021] The Setting button opens the same Setting page as the single-photo Edit Room (Q-3 answered); the compare button drawn on the photo works as in Edit Room: hold shows the original (Q-4 answered).');
set(/^- R-061 /, line(/^- R-061 /).replace('(DR-07 says boxes default to centred on each photo: Q-5.)', '(DR-07\'s 「boxes default to centred」 is superseded by the 「✅ 結論」 board: ruling REQ-021, Q-5 answered.)'));
for (const q of ['Q-1', 'Q-3', 'Q-4', 'Q-5', 'Q-13']) req = req.replace(line(new RegExp(`^- ${q} `)) + '\n', '');
req = req.replace('\n## Answered questions\n', '\n## Answered questions\n' +
  '- Q-1 (「Next」 state on the picker) — answered by the user, 2026-11-18 (REQ-021): 「Next」 lights up once a photo is selected; the copy stays the Design\'s (REQ-004): R-015; TC-005, TC-007.\n' +
  '- Q-3 (Setting in the Batch Edit Room) — answered by the user, 2026-11-18 (REQ-021): the same Setting as the Edit Room: R-039; TC-025.\n' +
  '- Q-4 (compare on the photo) — answered by the user, 2026-11-18 (REQ-021): hold shows the original: R-039; TC-026.\n' +
  '- Q-5 (crop Apply to all placement) — answered by the user, 2026-11-18 (REQ-021): follow the 「✅ 結論」 board (largest box at the current photo\'s relative position), not DR-07\'s 「centred」: R-060, R-061, R-073; TC-047, TC-051, TC-052, TC-053.\n' +
  '- Q-13 (deselect, empty 「Next」, the tile\'s expand icon) — answered by the user, 2026-11-18 (REQ-021): the numbers move up in order, 「Next」 is grey with nothing selected, expand opens the album selection screen: R-015, R-019, R-233; TC-009, TC-010, TC-150, TC-151.\n');
writeFileSync(join(here, 'requirements.md'), req);
console.log(`${rows.length} rows; changed: ${rows.filter(r => r.Change !== 'unchanged').map(r => `${r.ID} ${r.Change}`).join(', ')}`);
