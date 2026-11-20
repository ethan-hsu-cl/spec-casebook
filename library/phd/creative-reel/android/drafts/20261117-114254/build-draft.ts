// Creative Reel Android update (user, 2026-11-17, REQ-009) on v2 (phda-willy, 2026-11-12 readability edit): the
// PDF-only analysis caught up with the PM Figma page (figma-pm, group p1). Figma adds the Reel Creator intro page
// (「Tutorial」, 【Demo video 調整】) and three clauses of the picker-memory note (only templates with photo input > 1;
// 「last picked」 = the set applied with Next; leaving the room ends the session and clears the memory), which answer
// Q-3, Q-4 and Q-7. Every approved row is kept; changed rows are `modified`, new rows sit after the row they extend
// (REQ-033) with the next free IDs. Text follows formats.md: one item per line in Precondition and Expected Result
// (REQ-008), one step per line in Action; a v2 row still running steps together on one line is split here too.
// Re-runnable: node library/phd/creative-reel/android/drafts/20261117-114254/build-draft.ts
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { DRAFT_COLUMNS, readTable, writeTable } from '../../../../../../scripts/lib/library.ts';

const HERE = dirname(fileURLToPath(import.meta.url));
const approved = readTable(join(HERE, '..', '..', 'cases.csv')) as Record<string, string>[];
const R = 'PM Figma catch-up (REQ-009)';
const L = (...xs: string[]) => xs.join('\n');
const N = (...xs: string[]) => xs.map((x, i) => `${i + 1}. ${x}`).join('\n');
const NEWSESSION = 'App relaunched (force-stop and launch) so a new session starts';

type Mod = Partial<Record<'Precondition' | 'Action' | 'Expected Result' | 'Priority' | 'Spec Ref' | 'Notes', string>> & { why: string };
const MODS: Record<string, Mod> = {
  'TC-005': { Precondition: N('Launcher open', 'The Reel Creator intro page already dismissed with 「Don’t show again」 (TC-130)'),
    why: `${R}: the intro page (R-118) shows on room entry until 「Don’t show again」` },
  'TC-054': { 'Spec Ref': 'R-051, R-052, R-115', Precondition: N(NEWSESSION, 'Picker of 「Top 5 of My Year」 with 7 photos picked', '「Next」 tapped', 'Back in the room (without leaving it)'),
    Notes: '「Last time」 = the set applied with Next (Figma, R-115; Q-3 answered).', why: `${R}: session = one visit to the room (R-051); Q-3 answered by R-115` },
  'TC-057': { Precondition: N(NEWSESSION, 'In the room, 4 photos picked on a 4-photo AI Transition template', '「Next」 tapped', 'Back in the room'),
    'Expected Result': L('4 photos imported', 'Tray red 「Select at least 5 photos (1 more)」', 'Next disabled until 1 more is picked'),
    Notes: 'Drawn flow (picker-a2). The mockup imports 3, but only a set applied with Next is remembered (R-115), so 4 from an AI Transition template is the smallest reachable.',
    why: `${R}: the memory holds the set applied with Next (R-115), within the same room visit (R-051)` },
  'TC-058': { Precondition: N(NEWSESSION, 'In the room, 10 photos picked on a Creative template', '「Next」 tapped', 'Back in the room'), why: `${R}: the memory holds the set applied with Next (R-115)` },
  'TC-059': { Precondition: N(NEWSESSION, 'In the room, 6 photos picked', '「Next」 tapped', 'Without leaving the room (switch apps with Recents), 2 of the 6 deleted from the Gallery'),
    why: `${R}: leaving the room clears the memory (R-114), so the Gallery is changed without leaving it` },
  'TC-060': { Precondition: N(NEWSESSION, 'In the room, only 1 photo picked (e.g. Cinematic Styles)', '「Next」 tapped', 'Back in the room'), why: `${R}: the memory holds the set applied with Next (R-115)` },
  'TC-062': { Action: N('Leave the room', 'Open another photo picker of the app (e.g. Collage, AI Replace) and look above its tray'),
    'Expected Result': L('No 「Use the … photos you picked last time?」 prompt', 'The memory exists only inside Reel Creator'), Priority: 'P2', 'Spec Ref': 'R-051, R-116',
    Notes: 'Q-4 answered by Figma (R-116). Domain K07: selection state leaking into another feature is a past bug class.', why: `${R}: Q-4 answered, memory only in Reel Creator (R-116)` },
  'TC-089': { Action: N('Read the tabs', 'Tap 「Image to Video」', 'Tap 「Reel Creator」'),
    'Expected Result': L('Step 1: tabs include 「Image to Video」, 「Reel Creator」, 「Character Motion Swap」', 'Step 1: no tab named 「Cinematic Reel Creator」', 'Steps 2–3: each tap selects that tab and shows its own items', 'Step 3: 「Reel Creator」 lists the reels'),
    why: `${R}: the Figma inventory lists the Artwork tabs as a control; the row now presses them (REQ-038)` },
  'TC-097': { Precondition: N(NEWSESSION, 'In the room, 7 photos picked on a Creative template', '「Next」 tapped', 'Back in the room'),
    'Expected Result': L('The Cinematic picker 「Select 1 photo」 shows no Import prompt', 'The prompt is only for templates with photo input > 1'), Priority: 'P2', 'Spec Ref': 'R-084, R-117',
    Notes: 'Q-7 answered by Figma (R-117).', why: `${R}: Q-7 answered, no prompt on 1-photo templates (R-117)` },
};

const TUT = 'Reel Creator intro page';
type Row = [id: string, after: string, section: string, pre: string, action: string, expected: string, prio: string, refs: string, notes: string];
const NEW: Row[] = [
  ['TC-128', 'TC-004', 'Room', N('Launcher open', 'The intro page not yet dismissed with 「Don’t show again」 (first entry on this install, or the box never ticked)'),
    'Tap the 「Reel Creator」 Launcher Shortcut',
    L(`The ${TUT} shows`, 'A demo video plays at the top', 'Title 「Reel Creator」', 'Text 「Turn photos into post-worthy videos with trendy transitions, cinematic styles, and creative effects!」', 'Button 「Try Now」', '「Don’t show again」 unticked', '「‹」 at the top left'),
    'P1', 'R-118', 'PM Figma 「Tutorial」 + 【Demo video 調整】 文案同左 (not in the PDF). When the page shows is not stated (Q-24). Design file not readable (Q-23): wording from the PM mockup.'],
  ['TC-129', 'TC-128', 'Room', N(`${TUT} shown`, '「Don’t show again」 not ticked'), N('Tap 「Try Now」', 'Tap 「‹」 to leave the room', 'Open the room again from the Launcher Shortcut'),
    L('Step 1: the intro closes and the room shows', 'Step 3: the intro page shows again'), 'P2', 'R-119, R-121', 'Assumption: unticked = shown on every entry, as the old Cinematic Reel Creator intro (Q-24).'],
  ['TC-130', 'TC-129', 'Room', `${TUT} shown`, N('Tap 「Don’t show again」', 'Tap 「Try Now」', 'Leave the room and open it again', 'Force-stop the app, launch it and open the room once more'),
    L('Step 1: the box shows ticked', 'Step 2: the room shows', 'Step 3: no intro page', 'Step 4: no intro page'), 'P1', 'R-119, R-120',
    'Run before the other Room rows on a state where the intro still shows; once ticked it cannot be brought back without clearing app data.'],
  ['TC-131', 'TC-130', 'Room', `${TUT} shown (opened from the Launcher Shortcut)`, 'Tap 「‹」 on the intro page', L('Leaves to the Launcher (the page the room was opened from)', 'The room is not shown'),
    'P3', 'R-122', 'No arrow drawn (Q-8): record where it goes.'],
  ['TC-132', 'TC-131', 'Room', `${TUT} shown`, 'Press the Android system Back', 'Same as 「‹」 on the intro page (TC-131), or recorded', 'P3', 'R-089, R-122', 'System Back is an exit of every page (REQ-051).'],
  ['TC-133', 'TC-054', 'Picker memory', N(NEWSESSION, 'In the room, 7 photos picked on 「Top 5 of My Year」', '「Next」 tapped', 'Back on the picker, the pick changed to 9 photos', 'Picker left with 「‹」 (no Next)'),
    'Open 「Top 5 of My Year」 › 「Use Template」 again', L('The prompt reads 「Use the 7 photos you picked last time?」 (the set applied with Next)', '「Import」 brings in those 7'),
    'P2', 'R-115', '「上次選的圖」 = 上次按 Next (apply 的那組) (Figma).'],
  ['TC-134', 'TC-061', 'Picker memory', N('In the room, 7 photos picked on 「Top 5 of My Year」', '「Next」 tapped'),
    N('Tap 「‹」 until the room is left', 'Open the room again (without relaunching the app)', 'Enter the 「Top 5 of My Year」 picker'),
    L('No Import prompt', 'Leaving the room ended the session and cleared the memory'), 'P1', 'R-051, R-114',
    '離開房間 = 離開 session, 記憶清除 (Figma). Opening My AI Artwork with the History button is not counted as leaving (Q-25): record it in Notes if the prompt is gone after it.'],
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
  out.splice(at + 1, 0, { ID: id, Section: section, Precondition: pre, Action: action, 'Expected Result': expected, Priority: prio, 'Spec Ref': refs, Notes: notes, Change: 'new', 'Change Reason': R });
}
// One step per line (team rule 2026-11-03): a v2 Action still chaining steps on one line is split at 「, then」 /
// 「; 」 / 「. 」 outside 「」 and brackets.
const split = (text: string) => {
  if (!text || text.includes('\n')) return text;
  const parts: string[] = []; let cur = '', depth = 0;
  for (let i = 0; i < text.length; i++) {
    const c = text[i], rest = text.slice(i);
    if ('「(['.includes(c)) depth++; else if ('」)]'.includes(c)) depth = Math.max(0, depth - 1);
    if (depth === 0) {
      const m = /^(?:,? then |; then |, and then |; (?=[a-z「])|\. (?=[A-Z「]))/.exec(rest);
      if (m && cur.trim()) { parts.push(cur.trim()); cur = ''; i += m[0].length - 1; continue; }
    }
    cur += c;
  }
  if (cur.trim()) parts.push(cur.trim());
  if (parts.length < 2) return text;
  for (let n = 1; n < parts.length; n++) if (/^(up|down)\b/i.test(parts[n])) parts[n] = `swipe ${parts[n]}`;
  return parts.map((p, n) => `${n + 1}. ${p.charAt(0).toUpperCase()}${p.slice(1).replace(/\.$/, '')}`).join('\n');
};
for (const r of out) {
  const v = split(r.Action);
  if (v !== r.Action) { r.Action = v; if (r.Change === 'unchanged') { r.Change = 'modified'; r['Change Reason'] = 'One step per line (team rule 2026-11-03); wording unchanged'; } }
}
writeTable(join(HERE, 'draft.csv'), DRAFT_COLUMNS, out);
console.log(`${out.length} rows: ${out.filter(r => r.Change === 'new').length} new, ${out.filter(r => r.Change === 'modified').length} modified: ${out.filter(r => /One step/.test(r['Change Reason'])).map(r => r.ID).join(', ')}`);
