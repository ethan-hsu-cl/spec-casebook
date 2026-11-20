// Builds draft.csv from the approved v2 cases.csv (user, 2026-11-17, REQ-006: PM page re-read, Design page 616:9324
// read for the first time, filed eBugs rechecked). Run from the repo root:
//   node library/phd/ai-hair-color-custom/android/drafts/20261117-151025/build-draft.ts
import { readFileSync, writeFileSync } from 'node:fs';
import { readRecords, writeRecords } from '../../../../../../scripts/lib/csv.ts';

const here = 'library/phd/ai-hair-color-custom/android/drafts/20261117-151025';
const rows = readRecords(readFileSync('library/phd/ai-hair-color-custom/android/cases.csv', 'utf8'));
const OLD_NOTE = 'PM-only: no Design frame yet (no Design file supplied 2026-11-12)';
const PM_ONLY = 'PM-only: no Design frame yet (Design 616:9324, read 2026-11-17, does not draw it)';
const ROOM = 'In the AI Hair Color room with a portrait photo with one clear, front-facing face (passes every entry check)';
const bug = (code: string) => `Recheck ${code} (filed from run 2026-11-13-r1, TR261111-0042).`;

type Edit = { set?: Partial<Record<string, string>>; design?: string; note?: string; reason: string };
const edits: Record<string, Edit> = {
  'TC-001': { set: { Action: 'Tap the 「Hair Color」 card in the Launcher\'s 「AI Magic」 section', 'Spec Ref': 'R-002, R-090' },
    note: 'Launcher card: Design 1-launcher 617:9493; the Intro Demo itself is PM-only (the Design draws none: Q-8).',
    reason: 'Design now draws the Launcher entry (R-090)' },
  'TC-005': { note: bug('PHA262026P0110'), reason: 'Rule 3: recheck of PHA262026P0110' },
  'TC-015': { set: { Action: 'In Edit Room, tap 「Hair Color」 in the 「Quick Action」 tool row', 'Spec Ref': 'R-014, R-089' },
    design: 'Design 1_edit_room 788:1354 draws 「Hair Color」 in the Quick Action row.', reason: 'Design now draws the Edit Room entry (R-089)' },
  'TC-017': { set: { 'Expected Result': '「Custom」 is the first cell of the swatch row, before 「Platinum」; it is an orange gradient tile with a magic-wand icon and the label 「Custom」, and is not selected; the first template (「Platinum」) is selected' },
    design: 'Design 4-hair_color 686:1427; the PM note says gradient + ＋ (Q-2).', reason: 'Design now draws the unset Custom cell (R-017)' },
  'TC-018': { set: { Action: '1. Tap each other category tab in turn (the Design draws 「Highlights」 and 「Ombré」; the PM 「Multicolor」)\n2. Tap the 「Solid」 tab',
    'Expected Result': '1. 「Custom」 is the first cell of each tab\'s row\n2. 「Custom」 is first again in the Solid row' },
    design: 'Design 4-hair_color 686:1427 draws the tabs 「Solid」 「Highlights」 「Ombré」 and Custom only in Solid (Q-1).', reason: 'Design names the category tabs; the row no longer depends on the PM tab name' },
  'TC-019': { set: { 'Expected Result': 'A bottom sheet opens with a grab handle at the top, the 「Style」 area, the 「Base Color」 and 「Highlight Color」 rows and an orange-styled Generate with ⬤ 6 inside it; the ✕ ↺ ↻ ✓ row is not shown (record whether a 「Custom」 title or ⌄ key shows: the Design draws neither, Q-17)' },
    design: 'Design 4-hair_color_case1_no_style 894:1474. Check on device.', note: bug('PHA262026P0111') + ' Its ⌄ expectation conflicts with the Design (Q-17); its ✕ ↺ ↻ ✓ part stands.',
    reason: 'Design now draws the panel: grab handle, no title or ⌄ (R-019, Q-17); Rule 3 recheck' },
  'TC-021': { design: 'Design case (1) 894:1474 draws the rows and Generate disabled.', note: bug('PHA262026P0112'), reason: 'Design now draws it; Rule 3: recheck of PHA262026P0112' },
  'TC-022': { set: { 'Expected Result': 'Every published Custom style shows with its thumbnail and name (the Design draws 「Face」, 「Bangs」, 「Highlight」, 「Balayage」, 「Ombre」, 「Solid」, …), 11 on day 1 by the fallback; the two split-dye styles have plain-colour thumbnails; each premium style has a crown badge at the top right of its thumbnail and free styles have none', 'Spec Ref': 'R-024, R-025, R-087' },
    design: 'Design case (1) 894:1474 draws the crown on 「Balayage」. Day-1 list and premium styles: Q-6.', reason: 'Design now draws the style row and the premium crown (R-087)' },
  'TC-023': { set: { 'Expected Result': '「Ombré」 shows the selected frame (orange) and both colour rows become enabled' },
    design: 'Design case (2) 894:2060 draws an orange frame on the chosen style; PM token #ffbe98.', reason: 'Design now draws the selected style' },
  'TC-024': { set: { 'Expected Result': 'The 「Base Color」 row is enabled and the 「Highlight Color」 row stays on screen greyed out (disabled); tapping a Highlight colour does nothing' },
    design: 'Design case (2-1) 929:1901. The PM says the Highlight row does not appear (D6-04): Q-18, check on device.', reason: 'Design draws the Highlight row greyed for Solid (R-027, Q-18)' },
  'TC-026': { design: 'The Design draws Base-only as Generate grey with the toast 「Select both a base and highlight color.」 (cases 2, 2-1): Q-19; the ruling stands until the user re-decides.', reason: 'Design disagrees with REQ-003: Q-19 noted' },
  'TC-027': { set: { Action: '1. Tap a recommended colour in 「Highlight Color」 only\n2. Tap Generate', 'Expected Result': '1. Generate stays disabled (grey) while no Base Color is chosen\n2. The toast 「Select both a base and highlight color.」 shows over the photo; no generation starts and no credits are taken', 'Spec Ref': 'R-029, R-085' },
    design: 'Design case (2-1) 892:1796 draws the toast (answers Q-16).', reason: 'Design draws the missing-colour toast (R-085)' },
  'TC-029': { set: { 'Expected Result': '1. The 「Highlight Color」 row turns grey (disabled) (record whether Base stays chosen and Generate stays enabled)\n2. The 「Highlight Color」 row is enabled again (record whether its colour is kept)' },
    design: 'Design case (2-1) 929:1901 (Q-18). Q-3.', reason: 'Design draws the Highlight row greyed for Solid (R-027, Q-18)' },
  'TC-030': { set: { 'Expected Result': 'Each row starts with a rainbow colour-wheel key with a ＋ badge followed by 8 round recommended colours in this order: #5A3E2B, #A88B70, #B8AE98, #E3DCCB, #66735A, #5B6E85, #C9918A, #B5562A (sample each circle\'s colour from the screenshot), and scrolls sideways' } ,
    note: 'PM edit of 2026-11-17 (was 7 colours). The Design draws white and neutral swatches (Q-21).', reason: 'PM now gives 8 recommended colours with their values (R-022)' },
  'TC-031': { set: { 'Expected Result': 'The app\'s colour palette opens in the sheet: 「Cancel」 at the left and 「Done」 at the right on one line, a saturation-brightness square, a rainbow hue slider with a round handle and an eyedropper key right of the slider; no bottom ✕ ↩ ↪ ⊕ ✓ row' },
    design: 'Design 4-hair_color 841:1429.', note: bug('PHA262026P0113'), reason: 'Design now draws the palette (no bottom row, R-033); Rule 3 recheck' },
  'TC-032': { set: { 'Expected Result': 'The palette closes; the picked blue is added to the 「Base Color」 row as a new circle right after the colour wheel, before the recommended colours, with the selection ring; the recommended colours move one place right; 「Highlight Color」 is unchanged', 'Spec Ref': 'R-034, R-035, R-086' },
    design: 'Design case (3) 894:2637.', reason: 'Design now draws where a picked colour goes (R-086)' },
  'TC-035': { note: bug('PHA262026P0113'), reason: 'Rule 3: recheck of PHA262026P0113' },
  'TC-038': { set: { Action: 'Collapse the panel: drag its grab handle down (tap ⌄ instead if the build shows one)' },
    note: bug('PHA262026P0115') + ' Q-2: the PM mockup draws a pencil icon in the cell. How to collapse: Q-17.', reason: 'Design draws a grab handle, no ⌄ (R-042, Q-17); Rule 3 recheck' },
  'TC-040': { note: bug('PHA262026P0115'), reason: 'Rule 3: recheck of PHA262026P0115' },
  'TC-045': { note: bug('PHA262026P0116'), reason: 'Rule 3: recheck of PHA262026P0116' },
  'TC-047': { note: bug('PHA262026P0117'), reason: 'Rule 3: recheck of PHA262026P0117' },
  'TC-048': { note: bug('PHA262026P0117'), reason: 'Rule 3: recheck of PHA262026P0117' },
  'TC-054': { set: { Action: '1. Tap 「Platinum」\n2. Tap 「Custom」 and collapse the panel (drag the handle down, or ⌄ if shown)' },
    note: bug('PHA262026P0119'), reason: 'Collapse by the Design\'s handle (Q-17); Rule 3: recheck of PHA262026P0119' },
  'TC-057': { note: bug('PHA262026P0118'), reason: 'Rule 3: recheck of PHA262026P0118' },
  'TC-069': { set: { Action: '1. Choose the premium style (crown badge on its thumbnail) and its colours\n2. Tap Generate', 'Spec Ref': 'R-061, R-087' },
    design: 'Design case (1) 894:1474 draws the crown. Which styles are premium: Q-6.', reason: 'Design draws the premium crown (R-087)' },
  'TC-086': { note: bug('PHA262026P0114'), reason: 'Rule 3: recheck of PHA262026P0114' },
};

const added: { after: string; row: Record<string, string> }[] = [
  { after: 'TC-002', row: { ID: 'TC-092', Section: 'Photo guide', Precondition: 'Fresh install (or app data cleared); the photo guide never dismissed; entering AI Hair Color from the Launcher card',
    Action: '1. Look at the screen shown before the photo picker\n2. Tap 「Continue」',
    'Expected Result': '1. The guide shows 「For the best results, we recommend photos with the following:」, under 「Recommend」 「Photo of One Female」, 「Full Upper Body」 and 「Clear Face」 with sample photos, under 「Avoid」 「Face Coverings」 and 「Face too small」 with sample photos, a 「Continue」 button and 「Don\'t show again.」\n2. The guide closes and the photo picker (「Photo」 / 「Stock」 tabs) shows',
    Priority: 'P2', 'Spec Ref': 'R-088', Notes: 'Design 2-before_importing_photo 617:10539. 10/E D2-02 also asks to avoid hats: Q-20.' } },
  { after: 'TC-092', row: { ID: 'TC-093', Section: 'Photo guide', Precondition: 'The photo guide shown (TC-092)',
    Action: '1. Tick 「Don\'t show again.」\n2. Tap 「Continue」\n3. Leave AI Hair Color\n4. Open AI Hair Color again from the Launcher card',
    'Expected Result': '2. The photo picker shows\n4. The photo picker shows straight away; the guide does not show again',
    Priority: 'P3', 'Spec Ref': 'R-088', Notes: 'Design 2-before_importing_photo 617:10539.' } },
];

const out: Record<string, string>[] = [];
for (const r of rows) {
  const e = edits[r.ID];
  const notes = r.Notes.replace(OLD_NOTE, e?.design ? '' : PM_ONLY).replace(/\s+$/, '').replace(/\.\s*$/, '.');
  if (!e) { out.push({ ...r, Notes: notes, Change: 'unchanged', 'Change Reason': '' }); }
  else {
    const n = [notes.replace(/\s*$/, ''), e.design ?? '', e.note ?? ''].filter(Boolean).join(' ').replace(/\s+/g, ' ').trim();
    out.push({ ...r, ...(e.set as Record<string, string> ?? {}), Notes: n, Change: 'modified', 'Change Reason': e.reason });
  }
  for (const a of added.filter(a => a.after === r.ID)) {
    out.push({ ...a.row, Change: 'new', 'Change Reason': 'Design 616:9324 draws the photo guide (R-088, REQ-006)' });
    for (const b of added.filter(b => b.after === a.row.ID)) out.push({ ...b.row, Change: 'new', 'Change Reason': 'Design 616:9324 draws the photo guide (R-088, REQ-006)' });
  }
}
const missing = Object.keys(edits).filter(id => !rows.some(r => r.ID === id));
if (missing.length) throw new Error('edits for unknown rows: ' + missing.join(', '));
// One item per line (team rule 2026-11-12) on every row this draft changes or adds: Precondition items numbered,
// Expected Result checks one per line with the step prefix repeated.
const splitTop = (s: string) => { const out: string[] = []; let depth = 0, cur = '';
  for (let i = 0; i < s.length; i++) { const ch = s[i]; if (ch === '(') depth++; if (ch === ')') depth--;
    if (depth === 0 && ch === ';' && s[i + 1] === ' ') { out.push(cur.trim()); cur = ''; i++; continue; }
    if (depth === 0 && ch === '.' && s[i + 1] === ' ' && /[A-Z「]/.test(s[i + 2] ?? '') && !/\b(e\.g|i\.e|vs)$/.test(cur)) { out.push(cur.trim()); cur = ''; i++; continue; }
    cur += ch; }
  if (cur.trim()) out.push(cur.trim().replace(/\.$/, '')); return out.map(x => x.replace(/\.$/, '')).map(x => x[0].toUpperCase() + x.slice(1)); };
for (const r of out) {
  if (r.Change === 'unchanged') continue;
  const pre = r.Precondition.split(/\r?\n/).flatMap(l => splitTop(l.replace(/^\d+\.\s*/, '')));
  r.Precondition = pre.length > 1 ? pre.map((x, i) => `${i + 1}. ${x}`).join('\n') : pre.join('');
  r['Expected Result'] = r['Expected Result'].split(/\r?\n/).flatMap(l => { const m = /^(\d+\.\s*)?(.*)$/.exec(l)!; return splitTop(m[2]).map(x => (m[1] ?? '') + x); }).join('\n');
}
const cols = ['ID', 'Section', 'Precondition', 'Action', 'Expected Result', 'Priority', 'Spec Ref', 'Notes', 'Change', 'Change Reason'];
for (const r of out) for (const c of ['Action', 'Expected Result', 'Precondition']) r[c] = r[c].replace(/\r?\n/g, '\r\n');
writeFileSync(`${here}/draft.csv`, writeRecords(cols, out));
const count = (c: string) => out.filter(r => r.Change === c).length;
console.log(`draft.csv: ${out.length} rows — new ${count('new')}, modified ${count('modified')}, unchanged ${count('unchanged')}`);
void ROOM;
