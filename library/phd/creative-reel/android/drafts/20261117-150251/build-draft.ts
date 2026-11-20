// Creative Reel Android update (REQ-011, 2026-11-17) on v3: the Design Figma, read once qa-dm had access (Q-23).
// Design first (pass 7, user 2026-11-13): rows whose screen the Design draws now quote the Design (picker 「Add photos」,
// 「Recent ⌄」, badges 1, 2, 3, tray 「Select {min} to {max} photos to continue.」 with no count, the Import prompt card
// with thumbnails, the confirm page header, 「Your photos (n/max)」 and 「+」 first, the Text Language sheet, Artwork
// 「Create more」), with the PM version in Notes. New rows press what only the Design draws (picker expand icon, tray
// 「×」, prompt variants for 3 / 2 / 1 photos, the sheet's dimmed page, Artwork 「Select」 / ⓘ / 「Expires on」 /
// 「Almost done」 / 「Resume to Upload」, the dark theme) and sit after the row they extend (REQ-033).
// Re-runnable: node library/phd/creative-reel/android/drafts/20261117-150251/build-draft.ts
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { DRAFT_COLUMNS, readTable, writeTable } from '../../../../../../scripts/lib/library.ts';

const HERE = dirname(fileURLToPath(import.meta.url));
const approved = readTable(join(HERE, '..', '..', 'cases.csv')) as Record<string, string>[];
const D = 'Design Figma (REQ-011), Design first';
const L = (...xs: string[]) => xs.join('\n');
const N = (...xs: string[]) => xs.map((x, i) => `${i + 1}. ${x}`).join('\n');
const NEWSESSION = 'App relaunched (force-stop and launch) so a new session starts';
const PK = 'Picker of 「Top 5 of My Year」 (opened by 「Use Template」), nothing picked';
const CONF = 'Confirm page of 「Top 5 of My Year」 reached with 7 photos picked';
const DARK = 'Phone in dark theme (Android Settings › Display › Dark theme on; ask the user before switching it)';

type Mod = Partial<Record<'Precondition' | 'Action' | 'Expected Result' | 'Priority' | 'Spec Ref' | 'Notes', string>> & { why: string };
const MODS: Record<string, Mod> = {
  'TC-006': { 'Expected Result': L('No tabs', 'One page of sections including 「Cinematic Styles 🎬」, 「Year-End Recap 🎉」 and 「Cool Transition 🎞️」 (Design), plus any further Creative section such as 「Christmas Time 🎄」 (PM)', 'The three features mixed'),
    Notes: 'Section order is pending (Q-1): record the order shown. Titles are CMS category names; the PM drew 「Year-End Recap 📅」 and 「Cool Transitions 🤳🏻」.', why: `${D}: section titles as the Design draws them (R-006)` },
  'TC-007': { 'Expected Result': L('Each section scrolls horizontally through its own template cards', 'Cinematic Styles cards carry a small inset photo at their bottom left'), why: `${D}: the Design's Cinematic Styles cards (R-007)` },
  'TC-008': { Action: N('Read the credit pill at the top right', 'Tap it'), 'Expected Result': L('The pill shows a blue diamond icon, the account\'s current balance and 「⊕」', 'Tapping it opens the Buy Credit page'),
    why: `${D}: the credit pill as drawn (R-008)` },
  'TC-024': { 'Expected Result': L('「‹」, an ⓘ icon and the credit pill at the top', 'A mute button on the right above the text', 'At the bottom the name 「Top 5 of My Year」, the description 「Rank your year\'s best moments in one reel」, the photo count with an image icon and 「Use Template」', 'Text over a darkened bottom of the demo'),
    'Spec Ref': 'R-029, R-031, R-032, R-020, R-035', Notes: 'Design: ⓘ in place of the PM\'s 「View photo tips」 text (Q-28). The Design draws no range count: record the wording (PM 「5–15 photos」, Q-36).', why: `${D}: Preview top bar and count (R-029, R-031)` },
  'TC-030': { 'Expected Result': 'The count reads 「1 Photo」 with an image icon', Notes: 'Design wording (the PM wrote 「1 photo」, Q-36).', why: `${D}: 「1 Photo」 (R-031)` },
  'TC-033': { Action: 'Tap the ⓘ icon at the top left', 'Expected Result': L('The 「Photo tips」 sheet opens', '「✓ Recommended」 with example images and bullets (incl. 「Portrait (vertical) photos work best」)', '「✕ Avoid」 with example images and bullets', '「Got it」'),
    Notes: 'Design: ⓘ in place of 「View photo tips」, assumed to open the tips (Q-28). The sheet is PM-only: no Design frame yet (Design 2026-11-09).', why: `${D}: the tips open from ⓘ (R-036, Q-28)` },
  'TC-035': { Action: 'Swipe to another template and tap its ⓘ', why: `${D}: the tips open from ⓘ (R-036)` },
  'TC-037': { 'Expected Result': L('The picker 「Add photos」 opens directly (「‹」, 「Recent ⌄」)', 'The tray shows 「Select 5 to 15 photos to continue.」 and a grey 「Next」', 'No 「0/15」 count on the picker'),
    Notes: 'Design first: the PM drew 「Add Photos」, 「Recents ▾」, 「Select 5–15 photos」 and 「0/15」. The Design sample reads 「Select 5 to 10 …」 for a 5–10 template.', why: `${D}: picker title, album and tray (R-041, R-042)` },
  'TC-038': { 'Expected Result': L('They show orange badges 1, 2, 3 in pick order, each photo framed in orange', 'The tray shows the 3 thumbnails, each with 「×」', 'Red 「Select at least 5 photos (2 more)」', '「Next」 grey (disabled)'),
    Notes: 'Design: badges 1, 2, 3 (PM 01, 02, 03) and no count. The red line is drawn only by the PM, after an Import (Q-30): record it if missing.', why: `${D}: badges and tray without count (R-041 – R-043)` },
  'TC-040': { 'Expected Result': L('The red line is gone', '「Next」 enabled (orange)'), why: `${D}: no count on the picker (R-042)` },
  'TC-042': { 'Expected Result': L('The 16th cannot be picked (or 「Next」 turns grey)', '15 badges is the most allowed'), why: `${D}: no count on the picker (R-042)` },
  'TC-043': { Precondition: N(PK, '4 photos picked (badges 1–4)'), Action: 'Tap photo 2 again',
    'Expected Result': L('It is unpicked: its badge and frame are gone and its thumbnail leaves the tray', '3 thumbnails left in the tray', 'Record whether badges 3 / 4 renumber'), why: `${D}: badges 1, 2, 3 and no count (R-041, R-042)` },
  'TC-051': { Action: 'Tap 「Recent ⌄」 and choose another album', why: `${D}: album 「Recent ⌄」 (R-049)` },
  'TC-054': { 'Expected Result': L('Above the tray a prompt card: three thumbnails, the third covered by 「+4」', 'Text 「Use the 7 photos you picked last time?」', '「×」 at the top right and 「Import」', 'Nothing is picked yet (no badges, 「Next」 grey)'),
    'Spec Ref': 'R-051, R-052, R-115, R-125, R-126', Notes: 'Design 03-1 (8 photos → 「+5」). 「Last time」 = the set applied with Next (Figma, R-115; Q-3 answered).', why: `${D}: the prompt card with thumbnails (R-052, R-125)` },
  'TC-055': { 'Expected Result': L('The 7 photos are picked in the picker, badges 1–7, and shown in the tray', 'The picker stays open (does not jump to the confirm page)'), why: `${D}: badges, no count (R-041, R-042)` },
  'TC-063': { 'Expected Result': L('Top: template thumbnail, 「Top 5 of My Year」, the photo count with an image icon, 「9:16」 with a ratio icon, 「‹」 and the credit pill', '「Your photos (7/15)」 with 「Long-press to reorder · tap × to remove」', 'The 「+」 tile first (dashed orange frame), then the 7 photos, each with 「×」', 'A 「Text Language」 bar reading 「English」 with 「⌄」', '「Generate」 with the credit icon and 「60」'),
    Notes: 'Design first: the PM drew 「5–15 photos · output 9:16」, the count at the right, 「+」 last and 「Text language English ▾」. Header count and 9:16: Q-31.', why: `${D}: confirm page layout (R-060, R-061, R-064, R-067, R-068)` },
  'TC-068': { 'Expected Result': 'The picker opens with the 4 current photos picked (badges 1–4, 4 thumbnails in the tray)', why: `${D}: badges, no count on the picker (R-042)` },
  'TC-069': { 'Expected Result': L('The confirm page shows the 6 photos (the 4 kept plus 2 new)', '「Your photos (6/15)」', '「Generate」 enabled again'), 'Spec Ref': 'R-064, R-069',
    why: `${D}: count format (R-061); pass 10b, Generate's state when the count is back in range` },
  'TC-075': { Action: 'Tap the 「Text Language」 bar', 'Expected Result': L('A bottom sheet with a handle opens over the dimmed page', 'First row 「English」 「Device Language」, highlighted and ticked ✓', 'Then 「繁體中文 Chinese (Traditional)」, 「简体中文 Chinese (Simplified)」, 「日本語 Japanese」, 「한국어 Korean」, 「Español Spanish」, 「Français French」, 「Deutsch German」', 'The list scrolls on to further languages (PM: 「Português」, 「Italiano」, 「ภาษาไทย」 …)'),
    Notes: 'Design first (sheet, 「Device Language」, English names); the full list is the PM rule (Q-32).', why: `${D}: the Text Language sheet (R-073, R-074)` },
  'TC-076': { Action: 'Read the Text Language value and open the sheet', 'Expected Result': 'The default is 「繁體中文」, highlighted with 「Device Language」 and ✓', why: `${D}: 「Device Language」 (R-073)` },
  'TC-077': { Precondition: 'Text Language sheet open', why: `${D}: the list is a bottom sheet (R-074)` },
  'TC-078': { Precondition: 'Text Language sheet open', Action: N('Choose 「日本語」', 'Open the sheet again'),
    'Expected Result': L('Step 1: the sheet closes', 'Step 1: the bar shows 「日本語」', 'Step 2: 「日本語」 is highlighted and ticked'), why: `${D}: the sheet (R-074); pass 10b, the ticked row follows the choice` },
  'TC-085': { 'Expected Result': L('My AI Artwork opens on the 「Reel Creator」 tab with a new 「Top 5 of My Year」 card at the top', 'A grey tile 「Processing...」, the date, a time estimate (「… minutes remaining ...」) and a progress bar'),
    why: `${D}: the processing card (R-078)` },
  'TC-089': { 'Expected Result': L('Step 1: 「Image to Video」 first and 「Reel Creator」 second, then the app\'s other feature tabs, scrolling sideways', 'Step 1: no tab named 「Cinematic Reel Creator」', 'Steps 2–3: each tap selects that tab and shows its own items', 'Step 3: 「Reel Creator」 lists the reels'),
    Notes: 'The Design draws 「AI Face Swap」 third, the PM 「Character Motion Swap」: record the tabs after 「Reel Creator」.', why: `${D}: Artwork tabs (R-080)` },
  'TC-091': { Action: 'Tap 「Create more」', Notes: 'Design wording (PM 「Create More」).', why: `${D}: 「Create more」 (R-082)` },
  'TC-092': { 'Expected Result': L('The Preview shows 「1 Photo」', '「Use Template」 opens the picker with 「Select 1 photo」'),
    Notes: 'Design 「1 Photo」; 「Select 1 photo」 is PM-only (Q-36). No count on the picker (Design).', why: `${D}: 「1 Photo」, no picker count (R-031, R-042)` },
  'TC-093': { 'Expected Result': L('The first shows badge 1 and 「Next」 is enabled', 'A second cannot be added (or 「Next」 turns grey)'), why: `${D}: badges, no count (R-041, R-042)` },
  'TC-094': { 'Expected Result': L('Confirm page: 「Micro Cinema」 with 「1 Photo」 and 「9:16」 in the header', '「Your photos (1/1)」 and 「Tap the photo to replace」', '「Generate」 with the credit icon and 「40」', 'No Text Language'),
    Notes: 'Design header and count format; 1/1, replace and no Text Language from the PM (Q-35).', why: `${D}: confirm header and count format (R-060, R-085)` },
  'TC-098': { 'Expected Result': L('The Preview shows a fixed count (4 or 6 photos; record the wording, Q-36)', 'The picker tray reads 「Select 4 photos」 (or 6) with 「Next」 grey'), why: `${D}: no picker count (R-042)` },
  'TC-099': { 'Expected Result': L('「Next」 grey at 3', 'Enabled at 4', 'A 5th cannot be picked'), why: `${D}: no picker count (R-042)` },
  'TC-100': { 'Expected Result': L('Confirm page with 「Your photos (4/4)」, the reorder hint and 「Generate」 with the price', 'No Text Language'), why: `${D}: count format (R-061)` },
  'TC-109': { Precondition: 'Text Language sheet open on the confirm page', 'Expected Result': L('The sheet closes and the language is unchanged', 'The confirm page stays'), why: `${D}: the list is a bottom sheet (R-074)` },
  'TC-113': { why: `${D}: 「Create more」 (R-082)` },
  'TC-122': { why: `${D}: 「Create more」 (R-082)` },
  'TC-128': { Notes: 'PM Figma 「Tutorial」 + 【Demo video 調整】 文案同左 (not in the PDF). When the page shows is not stated (Q-24). PM-only: no Design frame yet (Design 2026-11-09).',
    why: `${D}: the Design draws no intro page (PM-only, pass 7)` },
};
// 「Create More」 → 「Create more」 in rows that only name the button
for (const id of ['TC-113', 'TC-122']) {
  const r = approved.find(x => x.ID === id)!;
  for (const k of ['Precondition', 'Action'] as const) if (r[k].includes('「Create More」')) (MODS[id] as any)[k] = r[k].replaceAll('「Create More」', '「Create more」');
}

type Row = [id: string, after: string, section: string, pre: string, action: string, expected: string, prio: string, refs: string, notes: string];
const NEW: Row[] = [
  ['TC-136', 'TC-041', 'Photo picker', N(PK, '6 photos picked'), N('Tap 「×」 on the 2nd thumbnail in the tray', 'Tap 「×」 on one more thumbnail'),
    L('Step 1: the thumbnail leaves the tray and photo 2 on the grid loses its badge and frame', 'Step 1: 5 stay picked and 「Next」 stays enabled', 'Step 1: record whether the later badges renumber', 'Step 2: 4 left and 「Next」 turns grey'),
    'P2', 'R-124, R-043', 'Design draws 「×」 on every tray thumbnail. Renumbering: Q-11.'],
  ['TC-135', 'TC-051', 'Photo picker', N(PK, '2 photos picked'), N('Tap the expand icon at the bottom right of a third photo', 'Tap 「‹」 (or the view\'s close control)'),
    L('Step 1: the photo opens in a full view', 'Step 2: back on the picker, the third photo is not picked and the 2 picks are unchanged'),
    'P3', 'R-123', 'Design draws the icon on every grid photo; what it opens is not stated (Q-29): record the view.'],
  ['TC-137', 'TC-059', 'Picker memory', N(NEWSESSION, 'In the room, 4 photos picked on a 4-photo AI Transition template', '「Next」 tapped', 'Without leaving the room (switch apps with Recents), 1 of the 4 deleted from the Gallery'),
    'Open 「Top 5 of My Year」 › 「Use Template」', L('The prompt reads 「Use the 3 photos you picked last time?」', 'Three thumbnails, no 「+」'),
    'P3', 'R-126, R-125, R-056', 'Design 03-2. needs: 4 disposable photos. N counted from the photos still in the Gallery (Q-17).'],
  ['TC-138', 'TC-137', 'Picker memory', N(NEWSESSION, 'In the room, 4 photos picked on a 4-photo AI Transition template', '「Next」 tapped', 'Without leaving the room, 2 of the 4 deleted from the Gallery'),
    'Open 「Top 5 of My Year」 › 「Use Template」', L('The prompt reads 「Use the 2 photos you picked last time?」', 'Two thumbnails'),
    'P3', 'R-126, R-056', 'Design 03-3. needs: 4 disposable photos.'],
  ['TC-139', 'TC-138', 'Picker memory', N(NEWSESSION, 'In the room, 4 photos picked on a 4-photo AI Transition template', '「Next」 tapped', 'Without leaving the room, 3 of the 4 deleted from the Gallery'),
    'Open 「Top 5 of My Year」 › 「Use Template」', L('The prompt reads 「Use the photo you picked last time?」', 'One thumbnail'),
    'P3', 'R-126, R-056, R-057', 'Design 03-4. The PM says no prompt for a set of 1 (R-057, Q-27): if none shows, record it. needs: 4 disposable photos.'],
  ['TC-140', 'TC-078', 'Text language', 'Text Language sheet open (「English」 chosen)', N('Tap the dimmed page above the sheet', 'Open the sheet again and drag its handle down'),
    L('Step 1: the sheet closes and the bar still reads 「English」', 'Step 2: the sheet closes and the bar still reads 「English」'),
    'P3', 'R-127', 'Not stated (Q-32): the Design draws a handle and a dimmed page.'],
  ['TC-141', 'TC-085', 'Generation and My AI Artwork', 'A Creative reel processing in My AI Artwork', 'Watch the card until its time estimate runs out',
    L('The remaining time counts down with the progress bar', 'If the job is still running when the estimate ends, the card shows 「Almost done」'),
    'P3', 'R-130', 'Design Artwork card states.'],
  ['TC-142', 'TC-086', 'Generation and My AI Artwork', 'A Creative reel finished (TC-086)', 'Read its card on the 「Reel Creator」 tab',
    L('The card shows the reel\'s thumbnail, the date and 「Top 5 of My Year」', '「Expires on」 with a date (record it)'),
    'P2', 'R-131', 'Retention not stated (Q-33).'],
  ['TC-143', 'TC-088', 'Generation and My AI Artwork', N('Credits ≥ 60 (note the balance)', CONF, 'Phone on USB (Wi-Fi may be toggled)'),
    N('Tap 「Generate」', 'Turn Wi-Fi off at once, while the photos upload', 'Open My AI Artwork', 'Turn Wi-Fi on', 'Tap 「Resume to Upload」 on the card'),
    L('Step 3: the card shows a ⚠ tile and 「Resume to Upload」', 'Step 5: the job resumes (「Processing...」) and finishes', 'The balance dropped by 60 once in total'),
    'P2', 'R-132', 'Design Artwork page (answers part of Q-12). If the upload ends before Wi-Fi is off, record Blocked and retry on a slower network.'],
  ['TC-144', 'TC-089', 'Generation and My AI Artwork', 'My AI Artwork on the 「Reel Creator」 tab with at least one finished reel', N('Tap 「Select」', 'Leave selection without acting (its cancel control or Back)'),
    L('Step 1: the list switches to selection (record what it offers)', 'Step 2: the list is back as before, nothing changed'),
    'P3', 'R-129', 'What Select offers is not stated (Q-33).'],
  ['TC-145', 'TC-144', 'Generation and My AI Artwork', 'My AI Artwork open', N('Tap the ⓘ at the top right', 'Close what it opened'),
    L('Step 1: an information page or popup opens (record its content)', 'Step 2: back on My AI Artwork'),
    'P3', 'R-128', 'Not stated (Q-33).'],
  ['TC-146', 'TC-125', 'Dark theme', N(DARK, 'Reel Creator room open'), N('Read the room', 'Open 「Top 5 of My Year」'),
    L('Step 1: the room is dark with light text', 'Step 1: the credit pill and History icon are legible', 'Step 1: section titles and cards as in the light theme', 'Step 2: the Preview\'s top bar (「‹」, ⓘ, credit pill) and its bottom text are legible'),
    'P3', 'R-133, R-006, R-029', 'Design ds-dark. What turns dark on is assumed (Q-34). Turn the dark theme off afterwards.'],
  ['TC-147', 'TC-146', 'Dark theme', N(DARK, 'In this room visit, 7 photos picked on 「Top 5 of My Year」 and 「Next」 tapped (TC-054 setup)', 'Back in the room'),
    N('Open 「Top 5 of My Year」 › 「Use Template」', 'Pick 3 photos'),
    L('Step 1: the picker is dark', 'Step 1: 「Add photos」 and 「Recent ⌄」 are legible', 'Step 1: the prompt card is dark with light text, 「×」 and an orange 「Import」', 'Step 2: orange badges and frames, the tray text and 「Next」 are legible'),
    'P3', 'R-133, R-041, R-052', 'Design ds-dark (Q-34).'],
  ['TC-148', 'TC-147', 'Dark theme', N(DARK, CONF), N('Read the page', 'Tap the 「Text Language」 bar'),
    L('Step 1: the page is dark', 'Step 1: 「Your photos (7/15)」, the hint, the 「+」 tile, each 「×」 and the Text Language bar are legible', 'Step 1: 「Generate」 is orange with the credit icon and 「60」', 'Step 2: the sheet is dark', 'Step 2: the 「English」 row is highlighted with an orange frame and ✓'),
    'P3', 'R-133, R-061, R-074', 'Design ds-dark (Q-34).'],
  ['TC-149', 'TC-148', 'Dark theme', N(DARK, 'My AI Artwork on the 「Reel Creator」 tab with a processing and a finished card'), 'Read the page',
    L('The page is dark', 'The tabs, 「Select」, the cards\' text and the progress bar are legible', '「Create more」 is orange'),
    'P3', 'R-133, R-078', 'Design ds-dark (Q-34).'],
  ['TC-150', 'TC-106', 'Android Back', N(PK, '2 photos picked', 'A third photo opened in the full view with its expand icon'), 'Press system Back',
    L('The full view closes back to the picker', 'Still 2 picked', 'The third is not picked'),
    'P3', 'R-089, R-123', 'System Back is an exit of every page (REQ-051).'],
];

const out: Record<string, string>[] = [];
for (const r of approved) {
  const m = MODS[r.ID];
  if (m) { const { why, ...f } = m; out.push({ ...r, ...f, Change: 'modified', 'Change Reason': why }); }
  else out.push({ ...r, Change: 'unchanged', 'Change Reason': '' });
}
for (const [id, after, section, pre, action, expected, prio, refs, notes] of NEW) {
  const at = out.findIndex(r => r.ID === after);
  if (at < 0) throw new Error(`anchor ${after} missing`);
  out.splice(at + 1, 0, { ID: id, Section: section, Precondition: pre, Action: action, 'Expected Result': expected, Priority: prio, 'Spec Ref': refs, Notes: notes, Change: 'new', 'Change Reason': D });
}
// a modified row must differ from v3
for (const r of out) if (r.Change === 'modified') {
  const a = approved.find(x => x.ID === r.ID)!;
  if (['Precondition', 'Action', 'Expected Result', 'Priority', 'Spec Ref', 'Notes'].every(k => a[k] === r[k])) throw new Error(`${r.ID} marked modified but unchanged`);
}
writeTable(join(HERE, 'draft.csv'), DRAFT_COLUMNS, out);
const n = (c: string) => out.filter(r => r.Change === c).length;
console.log(`${out.length} rows: ${n('unchanged')} unchanged, ${n('modified')} modified, ${n('new')} new, ${n('removed')} removed`);
