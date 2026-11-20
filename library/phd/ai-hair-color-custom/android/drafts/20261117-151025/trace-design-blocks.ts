// Traces the annotation blocks of the Design boards (ds-hair-a / ds-hair-b: phone text only, no notes) and the
// changed pm-ui block (2026-11-17). First matching rule wins; each block's whole text was checked against these rules.
// Run from the repo root.
import { readFileSync, writeFileSync } from 'node:fs';
const p = 'library/phd/ai-hair-color-custom/android/drafts/20261117-151025/annotation-trace.json';
const t = JSON.parse(readFileSync(p, 'utf8'));
const rules: [RegExp, string][] = [
  [/#5A3E2B/, 'R-022'],
  [/Select both a base and highlight color/, 'R-085'],
  [/\(2-1\) Tap Generate/, 'R-085'],
  [/\(2\) Base Color only/, 'R-029'],
  [/\(1\) No style selected/, 'R-023'],
  [/\(3\) Custom color selected/, 'R-086'],
  [/For the best results|Photo of One Female|Clear Face|Face Coverings|Don.t show again/, 'R-088'],
  [/1 Free Trial/, 'Q-7'],
  [/Cancel|Done/, 'R-033'],
  [/Intensity|\b33\b/, 'R-052'],
  [/Hairstyle \/ \[phone\] Hair Color/, 'R-089'],
  [/^\[phone\] Hair Color$/, 'R-090'],
  [/Base Color|Highlight Color|Style/, 'R-019'],
  [/Balayage|Ombre\b|Bangs|Face\b/, 'R-024'],
  [/Platinum|Custom|Highlights|Champagne|Periwinkle|Sakura/, 'R-016'],
  [/Generate|\b6\b/, 'R-038'],
  [/^\[phone\] 100$/, 'R-067'],
  [/AI Agent|Beautify|Quick Action|AI Art|Portrait|Effect/, 'ui: Edit Room tool row of other features (Hair Color itself is R-089)'],
  [/Photo|Stock|Favorites|Instagram|Recents/, 'ui: the shared photo picker tabs and albums'],
  [/AI Enhance|AI Magic|AI Expand|Fashion Outfit|AI Face Swap|Business Outfit|AI Headshot|AI Videos|AI Photos|MIne|Camera|HOT|Edit|Home/, 'ui: Launcher cards and tabs of other features'],
  [/^\[phone\] 9:41$/, 'ui: status bar time'],
];
let n = 0; const left: string[] = [];
for (const b of t.blocks) {
  if (b.trace) continue;
  const hit = rules.find(([re]) => re.test(b.text));
  if (hit) { b.trace = hit[1]; n++; } else left.push(`${b.id} ${b.text}`);
}
writeFileSync(p, JSON.stringify(t, null, 1) + '\n');
console.log(`traced ${n}; left ${left.length}`); for (const l of left) console.log('  ' + l);
