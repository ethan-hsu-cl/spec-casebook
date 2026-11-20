// Builds this draft (v3 → v4) from the user's rulings on the R2 eBug review (REQ-009, 2026-11-18):
// requirements.md and draft.csv from the approved v3 files. Run from the repo root:
//   node library/phd/ai-hair-color-custom/android/drafts/20261118-120459/build-draft.ts
import { readFileSync, writeFileSync } from 'node:fs';
import { readRecords, writeRecords } from '../../../../../../scripts/lib/csv.ts';

const here = 'library/phd/ai-hair-color-custom/android/drafts/20261118-120459';
const base = 'library/phd/ai-hair-color-custom/android';

// ---- requirements.md
let t = readFileSync(`${base}/requirements.md`, 'utf8').replace(/\r\n/g, '\n');
const rep = (a: string | RegExp, b: string) => { const s = typeof a === 'string' ? a : (a.exec(t) ?? [''])[0]; if (!s || !t.includes(s)) throw new Error('anchor gone: ' + String(a).slice(0, 90)); t = t.replace(s, b); };
const line = (id: string) => new RegExp(`^- ${id} .*$`, 'm');

rep(line('R-088'), '- R-088 [DS:ds-hair-a 2-before_importing_photo 617:10539; Req: REQ-009] Before the photo picker, a guide shows 「For the best results, we recommend photos with the following:」, a recommend list and an avoid list with sample photos, a 「Continue」 button and 「Don\'t show again」. The headings are the app-wide ones (「Recommendation」 as in other features, ruling REQ-009, 2026-11-18, over the Design\'s 「Recommend」), and the items follow the feature (Design: 「Photo of One Female」, 「Full Upper Body」, 「Clear Face」; 「Face Coverings」, 「Face too small」; the app may add 「Accessories」, answers Q-20). The picker tab behind it shows the album name (not a fixed 「Photo」).');
rep(line('R-089'), "- R-089 [DS:ds-hair-a 1_edit_room 788:1354; Req: REQ-009] Edit Room's 「Quick Action」 row holds no 「Hair Color」 tool; the Design frame that draws one is not followed (ruling REQ-009, 2026-11-18) — NOT TESTABLE: an absence the entry rows already pass by (TC-015 enters through Portrait › Hair).");
rep('- R-010 [PM:pm-face-check] A photo with no face is blocked with 「No face detected. Face is required for this feature.」 (D2-01d).',
  '- R-010 [PM:pm-face-check; Req: REQ-009] A photo with no face is blocked with a no-face message (PM: 「No face detected. Face is required for this feature.」; the app\'s 「No face detected. A face is required for this feature.」 is accepted, ruling REQ-009) (D2-01d).');
rep(line('R-027'), '- R-027 [PM:pm-ui panel_solid_color; Req: REQ-009] solid_color takes one colour: only the 「Base Color」 row shows; the 「Highlight Color」 row is hidden (D6-04; ruling REQ-009, 2026-11-18, 「隱藏就好」, over the Design\'s greyed row, answers Q-18).');
rep(line('R-029'), '- R-029 [PM:pm-ui panel_two_tone; Req: REQ-009] Every other style needs both colours: with only a Base Color or only a Highlight Color, Generate stays disabled (D6-04; ruling REQ-009, 2026-11-18, 「都要選才能生成」, replaces REQ-003 / REQ-007).');
rep(line('R-085'), '- R-085 [Req: REQ-009] No toast or message is required when a colour is missing: the disabled Generate is enough (ruling REQ-009, 2026-11-18, over the Design\'s toast 「Select both a base and highlight color.」); tapping the disabled Generate starts nothing and charges nothing.');
rep(line('R-068'), '- R-068 [PM:10/E D1-20b; Req: REQ-009] ✕ in the bottom row gives up this edit and lands in the Edit Room with the photo (ruling REQ-009, 2026-11-18: 「回到edit room是正常的」); whether a 「Discard changes?」 confirmation comes first is Q-22.');
rep(line('R-076'), '- R-076 [Rule pass 8: system Back] System Back in the room with the panel closed does what ✕ does (D1-20b, R-068).');
rep(line('Q-18'), '');
rep(line('Q-20'), '');
rep('| R-085 | only Highlight Color, Generate tapped (toast) | TC-027 |\n', '| R-085 | only Highlight Color, disabled Generate tapped | TC-027 |\n| R-029 | only Base Color filled, both required | TC-026 |\n');
rep('| R-027 | style=solid_color, Highlight row greyed | TC-024 |', '| R-027 | style=solid_color, Highlight row hidden | TC-024 |');
rep('- Q-21 ', '- Q-22 After ✕ or system Back on a result, the app asks 「Discard changes?」 / 「All your existing changes will be lost.」 (Keep / Discard) before landing in the Edit Room; the PM 10/E says no confirmation (D1-20b) and the ruling REQ-009 covered only the landing. Assumption: record the dialog, the row checks the landing. R-068, R-076, TC-079, TC-088.\n- Q-21 ');
rep('| REQ-006 | R-016, R-017, R-019, R-020, R-022, R-023, R-024, R-027, R-028, R-030, R-033, R-038, R-042, R-085–R-090',
  '| REQ-006 | R-016, R-017, R-019, R-020, R-022, R-023, R-024, R-027, R-028, R-030, R-033, R-038, R-042, R-085–R-088, R-090');
rep('| REQ-003 | R-029 (Base required, Highlight optional) → TC-026, TC-027 |\n', '');
rep('### Answered questions\n', `### Answered questions
- Q-18 (answered 2026-11-18, REQ-009): Solid hides the Highlight Color row. R-027, TC-024, TC-029.
- Q-20 (answered 2026-11-18, REQ-009): the guide's items follow the feature; an 「Accessories」 (hat) item is fine. R-088, TC-092.
- Q-19 superseded 2026-11-18 by REQ-009: both colours are required.
`);
rep(/^- Q-19 \(answered 2026-11-17[^\n]*\n/m, '');
rep('| REQ-005 | run entry (filing decisions); no table requirement |',
  '| REQ-005 | run entry (filing decisions); no table requirement |\n| REQ-009 | R-010, R-027, R-029, R-068, R-085, R-088 (R-089 removed) → TC-009, TC-015, TC-024, TC-026, TC-027, TC-029, TC-079, TC-088, TC-092 |\n| REQ-010 | run entry (filing decisions); no table requirement |');
t = t.replace(/\n{3,}/g, '\n\n').replace(/^\n(?=- )/gm, '');
writeFileSync(`${here}/requirements.md`, t);

// ---- draft.csv
const rows = readRecords(readFileSync(`${base}/cases.csv`, 'utf8'));
const R = 'Ruling REQ-009 (user, 2026-11-18, R2 eBug review)';
const edits: Record<string, { set: Record<string, string>; reason: string }> = {
  'TC-092': { reason: `${R}: app-wide 「Recommendation」 heading, items per feature, album-name tab (ISS-HCC-16 held)`, set: {
    'Expected Result': '1. The guide shows 「For the best results, we recommend photos with the following:」, a recommend list and an avoid list with sample photos (headings as in other features, e.g. 「Recommendation」), a 「Continue」 button and 「Don\'t show again」\n1. Record the items (Design: 「Photo of One Female」, 「Full Upper Body」, 「Clear Face」; 「Face Coverings」, 「Face too small」)\n2. The guide closes and the photo picker shows (its first tab is the album name)',
    Notes: 'Design 2-before_importing_photo 617:10539. REQ-009: the heading is app-wide, the items follow the feature, the tab is the album name; an 「Accessories」 item is fine (Q-20 answered).' } },
  'TC-009': { reason: `${R}: 「A face is required」 accepted (ISS-HCC-17 held)`, set: {
    'Expected Result': 'A no-face message shows (「No face detected. A face is required for this feature.」 or the PM\'s 「No face detected. Face is required for this feature.」)\nThe room does not open',
    Notes: 'REQ-009: the wording difference is accepted. PM-only: no Design frame yet (Design 616:9324, read 2026-11-17, does not draw it)' } },
  'TC-015': { reason: `${R}: no 「Hair Color」 in Edit Room's Quick Action; the entry is Portrait › Hair (R-089 removed, ISS-HCC-18 held)`, set: {
    Action: 'Open Portrait › Hair › AI Hair Color from Edit Room', 'Spec Ref': 'R-014',
    Notes: 'REQ-009: Quick Action gets no 「Hair Color」 (the Design\'s Edit Room frame is not followed). Recheck PHA262026P0110.' } },
  'TC-024': { reason: `${R}: Solid hides the Highlight row (Q-18 answered, ISS-HCC-19 held)`, set: {
    'Expected Result': 'Only the 「Base Color」 row shows\nNo 「Highlight Color」 row', Notes: 'REQ-009 「隱藏就好」 over the Design\'s greyed row (case 2-1 929:1901).' } },
  'TC-029': { reason: `${R}: Solid hides the Highlight row (Q-18 answered)`, set: {
    'Expected Result': '1. The 「Highlight Color」 row disappears (record whether Base stays chosen and Generate stays enabled)\n2. The 「Highlight Color」 row comes back (record whether its colour is kept)',
    Notes: 'Q-3. REQ-009 (Solid hides the Highlight row).' } },
  'TC-026': { reason: `${R}: both colours are required (replaces REQ-003 / REQ-007, ISS-HCC-20 held)`, set: {
    'Expected Result': 'Generate stays disabled (grey): a two-colour style needs both colours\nRecord any hint under the rows (the PM page draws 「Both Base Color and Highlight Color are required.」)',
    Notes: 'REQ-009 「都要選才能生成」 replaces REQ-003 / REQ-007; agrees with PM D6-04 and Design case 2.' } },
  'TC-027': { reason: `${R}: no toast needed, the disabled Generate is enough (ISS-HCC-21 held)`, set: {
    'Expected Result': '1. Generate stays disabled (grey) while no Base Color is chosen\n2. No generation starts and no credits are taken (no toast is required)',
    Notes: 'REQ-009: no toast; the Design\'s 「Select both a base and highlight color.」 toast (case 2-1 892:1796) is not required.' } },
  'TC-079': { reason: `${R}: landing in the Edit Room is correct (ISS-HCC-25 held); the confirmation is Q-22`, set: {
    'Expected Result': 'Record whether 「Discard changes?」 asks first (Q-22); after 「Discard」 the Edit Room shows with the original photo\nThe result is still in My AI Artwork',
    Notes: 'REQ-009 「回到edit room是正常的」. PM 10/E D1-20b says no confirmation: Q-22.' } },
  'TC-088': { reason: `${R}: landing in the Edit Room is correct; the confirmation is Q-22`, set: {
    'Expected Result': 'Same as ✕: record whether 「Discard changes?」 asks first (Q-22); after 「Discard」 the Edit Room shows with the original photo',
    Notes: 'REQ-009 「回到edit room是正常的」; Q-22.' } },
};
const out = rows.map(r => {
  const e = edits[r.ID];
  if (!e) return { ...r, Change: 'unchanged', 'Change Reason': '' };
  const n = { ...r, ...e.set, Change: 'modified', 'Change Reason': e.reason };
  for (const c of ['Precondition', 'Action', 'Expected Result']) n[c] = n[c].replace(/\r?\n/g, '\r\n');
  return n;
});
const missing = Object.keys(edits).filter(id => !rows.some(r => r.ID === id));
if (missing.length) throw new Error('unknown rows: ' + missing.join(', '));
writeFileSync(`${here}/draft.csv`, writeRecords(['ID', 'Section', 'Precondition', 'Action', 'Expected Result', 'Priority', 'Spec Ref', 'Notes', 'Change', 'Change Reason'], out));
console.log(`draft.csv: ${out.length} rows, modified ${out.filter(r => r.Change === 'modified').length}`);
