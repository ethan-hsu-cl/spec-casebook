// REQ-020: control trace of the Android draft against the Figma inventory (spec set 2026-11-09-figma), written for
// this table's own row IDs (controls.ts carried presses from main's Android v1 draft 20261109-164126, whose numbering
// differs). Run after `node scripts/controls.ts phd/batch-editing android --draft 20261118-101500`:
// node library/phd/batch-editing/android/drafts/20261118-101500/trace-controls.ts
import { readFileSync, writeFileSync } from 'node:fs';
const p = 'library/phd/batch-editing/android/drafts/20261118-101500/control-trace.json';
const inv = JSON.parse(readFileSync('library/phd/batch-editing/specs/2026-11-09-figma/extracted/inventory.json', 'utf8'));
const ct = JSON.parse(readFileSync(p, 'utf8'));
const PRESS: Record<string, string> = {
  'C-472204': 'TC-022', 'K-68a175': 'TC-001',
  'K-471aa6': 'TC-040, TC-071', 'C-e0011e': 'TC-170', 'K-767df6': 'TC-080', 'K-42ab79': 'TC-081', 'K-14866f': 'TC-174',
  'K-55ae2a': 'TC-176', 'K-0dafc6': 'TC-165', 'K-f474c6': 'TC-076', 'K-b56a6b': 'TC-176', 'K-67b0a7': 'TC-172',
  'K-68ce29': 'TC-172, TC-072', 'K-66b151': 'TC-071', 'K-3978a7': 'TC-154', 'K-14ddab': 'TC-071, TC-046',
  'C-745d29': 'TC-170', 'C-fcde4f': 'TC-029, TC-069, TC-083', 'K-161aa5': 'TC-172, TC-173', 'K-407daa': 'TC-122',
  'K-fddfa3': 'TC-113, TC-132', 'K-90a9b5': 'TC-175', 'K-9b8db7': 'TC-114', 'K-55d5ba': 'TC-025',
  'K-0816be': 'TC-086', 'K-a03f73': 'TC-103', 'K-027f5f': 'TC-089', 'K-6ddcb1': 'TC-087', 'C-e2a31f': 'TC-150',
  'K-768f43': 'TC-008', 'K-32efa4': 'TC-001, TC-005', 'C-4f0857': 'TC-040, TC-041', 'K-8d5d5a': 'TC-007',
  'K-0ea28f': 'TC-048', 'K-e7543f': 'TC-056', 'K-0e44a5': 'TC-045', 'K-464eb7': 'TC-155, TC-131',
  'K-960eab': 'TC-016, TC-017', 'K-71e5cc': 'TC-118', 'K-6e1204': 'TC-133', 'K-457d02': 'TC-116, TC-117',
  'K-1599a8': 'TC-113, TC-132', 'K-a60d7d': 'TC-001', 'K-e61079': 'TC-026', 'K-5062a6': 'TC-031', 'K-6ffd14': 'TC-030',
  'K-efb427': 'TC-029', 'C-69394e': 'TC-074, TC-159', 'K-6b58e4': 'TC-080', 'C-a494aa': 'TC-172', 'K-57b6f8': 'TC-072',
  'K-93d18f': 'TC-071', 'C-aa3629': 'TC-174, TC-071', 'K-e1af9c': 'TC-086, TC-098', 'K-849da8': 'TC-103',
  'K-2fe040': 'TC-006', 'K-8372f2': 'TC-157',
};
const LAUNCHER = 'n/a: other feature: Launcher (Design board 225:3699 draws the whole Launcher; only 「Edit」 and 「Batch Edit」 lead into this feature)';
const label = Object.fromEntries(inv.controls.map((c: any) => [c.id, c.label]));
let traced = 0, na = 0;
for (const e of ct.entries) {
  if (PRESS[e.group]) { e.press = PRESS[e.group]; e.how = 'trace'; traced++; }
  else if (e.boards.includes('design-launcher')) { e.press = LAUNCHER; e.how = 'n/a'; na++; }
  else if (/^n\/a:/.test(e.press ?? '')) { e.press = e.press.replace('whether they show is Q-17', 'whether they show is Q-19'); na++; }
  else throw new Error(`no Android trace for ${e.group} ${e.name} 「${e.label}」`);
  if (e.group === 'C-472204') e.other = e.controls.filter((id: string) => label[id] !== 'Batch Edit');
}
writeFileSync(p, JSON.stringify(ct, null, 1) + '\n');
console.log(`${ct.entries.length} groups: ${traced} pressed by rows, ${na} n/a`);
