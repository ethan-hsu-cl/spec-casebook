// Builds phases.json for round R2 of AI Hair Color Custom on Android (table v3, draft 20261117-151025).
// Usage: node library/phd/ai-hair-color-custom/android/drafts/20261117-151025/build-phases.ts
// User, 2026-11-17: 「請你在S23上面跑新版測試」 — run table v3 on the Samsung S23 (SM-S9110) with the build installed
// there today, 20.19.0 / 90201901 (R1 ran 90201900). A full round: every row, by journey stage; the rows v3 added or
// changed (TC-092, TC-093 and 26 modified, among them the rechecks of PHA262026P0110–P0119) sit in their own stage
// segments (REQ-033). The photo guide's 「Don't show again.」 (TC-093) is one-way, so it runs last in its segment
// and later recipes must not expect the guide (AGENTS.md, one-way state).
// Premium styles (crown) were Blocked on the Free account in R1: R2-e turns 「Set to subscriber」 ON (KP-131 backdoor,
// AGENTS.md *PHD Premium by the backdoor*) for them, and R2-f turns it OFF again for the Free rows.
import { writeFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const dir = dirname(fileURLToPath(import.meta.url));
const origin: Record<string, string> = { 'TC-092': 'P9', 'TC-093': 'P9' };
const phases = [
  { id: 'R2', name: 'Full run of v3 on the S23 (build 20.19.0 / 90201901)', round: true, origin,
    note: 'Account with credits; read the credit chip before and after every generation (6 credits each, R-040). Rows changed in v3 follow the Design 616:9324 (rows say 「check on device」 where the Design and PM disagree).',
    segments: [
      { id: 'R2-a', name: 'Intro Demo and photo guide', note: 'If the Intro Demo never shows (feature already opened on this phone), record its rows Blocked --as test-data: app data may not be cleared. TC-092 needs the photo guide (R1 saw it as the picker\'s recommendation sheet); TC-093 ticks 「Don\'t show again.」 and runs last (one-way): after it, recipes must not wait for the guide.',
        cases: ['TC-001', 'TC-090', 'TC-003', 'TC-002', 'TC-004', 'TC-092', 'TC-093'] },
      { id: 'R2-b', name: 'Entry checks', note: 'Photos in /sdcard/Pictures/HairColor (fixtures.md). TC-005 rechecks PHA262026P0110; TC-015 now enters through Edit Room › Quick Action › 「Hair Color」.',
        cases: ['TC-005', 'TC-006', 'TC-087', 'TC-007', 'TC-008', 'TC-009', 'TC-010', 'TC-011', 'TC-012', 'TC-013', 'TC-014', 'TC-015', 'TC-016'] },
      { id: 'R2-c', name: 'Custom cell, panel, style, palette and collapse (no credits)', note: 'hc_portrait_4x5.jpg. Nothing generated. Collapse by dragging the panel handle down (⌄ if the build shows one, Q-17). Rechecks P0111 (TC-019), P0112 (TC-021), P0113 (TC-031, TC-035), P0114 (TC-086), P0115 (TC-038).',
        cases: ['TC-017', 'TC-018', 'TC-019', 'TC-020', 'TC-030', 'TC-022', 'TC-021', 'TC-023', 'TC-024', 'TC-025', 'TC-026', 'TC-027', 'TC-028', 'TC-029',
          'TC-031', 'TC-032', 'TC-033', 'TC-034', 'TC-035', 'TC-086', 'TC-038', 'TC-039', 'TC-041', 'TC-042', 'TC-043', 'TC-085', 'TC-077'] },
      { id: 'R2-d', name: 'Generate, wait and result (credits)', note: 'Pexels portrait (recipes/pick-pexels-portrait*.steps; the hc_* photos are rejected as content). TC-057 rides on the first result (TC-045). Rechecks P0115 (TC-040), P0116 (TC-045), P0117 (TC-047, TC-048), P0118 (TC-057), P0119 (TC-054). About 10 generations.',
        cases: ['TC-045', 'TC-057', 'TC-046', 'TC-047', 'TC-050', 'TC-040', 'TC-048', 'TC-053', 'TC-049', 'TC-054', 'TC-055', 'TC-056', 'TC-079', 'TC-088', 'TC-089',
          'TC-078', 'TC-051', 'TC-052', 'TC-036', 'TC-037'] },
      { id: 'R2-e', name: 'Every style generated (credits)', note: 'One generation per style, 11 in all. The crowned styles need Premium: turn 「Set to subscriber」 ON first (KP-131), record the tier, and leave it ON for R2-f to switch off.',
        cases: ['TC-062', 'TC-063', 'TC-061', 'TC-060', 'TC-058', 'TC-059', 'TC-064', 'TC-065', 'TC-066', 'TC-067', 'TC-068'] },
      { id: 'R2-f', name: 'Free and low balance', note: 'Turn 「Set to subscriber」 OFF (Free) for TC-069. TC-070 / TC-071 / TC-073 need a balance under 6: run them only if it already is; otherwise Blocked --as test-data with the balance seen (no credit reset without the user).',
        cases: ['TC-069', 'TC-073', 'TC-070', 'TC-071'] },
      { id: 'R2-x', name: 'Parked fixtures', note: 'Recorded Blocked at init from `unavailable`.',
        cases: ['TC-075', 'TC-076', 'TC-081', 'TC-082', 'TC-084'] },
    ] },
];
const needs: Record<string, string[]> = {
  'TC-075': ['failure-fixture'], 'TC-076': ['failure-fixture'],
  'TC-081': ['deeplink'], 'TC-082': ['deeplink'], 'TC-084': ['cms'],
};
const unavailable: Record<string, string> = {
  'failure-fixture': 'observability: no fault switch forces a server failure on PhotoDirector Android',
  'deeplink': 'RD has not given the Custom deeplink format (Q-11)',
  'cms': 'the CMS list of PhDM_AIHairColor_CustomStyle was not provided (Q-13)',
};
const all = phases.flatMap(p => p.segments.flatMap(s => s.cases));
if (new Set(all).size !== all.length) throw new Error('a case is in two segments');
for (const p of phases) for (const s of p.segments) for (const c of s.cases) origin[c] ??= 'R1';
writeFileSync(join(dir, 'phases.json'), JSON.stringify({ draft: '20261117-151025', current: ['R2'], needs, unavailable, phases }, null, 2) + '\n');
console.log(`phases.json: ${all.length} cases; ${phases.map(p => p.segments.map(s => `${s.id} ${s.cases.length}`).join(', ')).join(' · ')}`);
