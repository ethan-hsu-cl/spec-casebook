// Traces the Design page's control groups that controls.ts could not trace (2026-11-17). Run from the repo root.
import { readFileSync, writeFileSync } from 'node:fs';
const p = 'library/phd/ai-hair-color-custom/android/drafts/20261117-151025/control-trace.json';
const t = JSON.parse(readFileSync(p, 'utf8'));
const L = 'n/a: other feature: Launcher chrome (Home tabs, Premium, Settings, account), not part of AI Hair Color';
const E = 'n/a: other feature: Edit Room chrome (AI Art, more, download, home, photo library), not part of AI Hair Color';
const P = "n/a: other feature: the app's shared photo picker header (back / confirm), unchanged by AI Hair Color";
const m: Record<string, string> = {
  'K-a06f04': 'TC-077',
  'K-a3d8b6': "n/a: the template row's 10/E one-time free trial (the Design draws it with Platinum); a free trial for Custom is undecided (Q-7)",
  'K-d5ffd5': L, 'K-e81415': L, 'K-882ca2': L, 'K-5475e2': L, 'K-e74f30': L, 'K-6bd523': L, 'K-466c2e': L,
  'K-4cdeaf': P, 'K-f35385': P,
  'K-2976b6': 'TC-093',
  'K-ac3edc': 'TC-055',
  'K-1d961b': E, 'K-fa67fc': E, 'K-c5f949': E, 'K-426c43': E, 'K-617b93': E,
};
let n = 0;
for (const c of t.entries) if (m[c.group]) { c.press = m[c.group]; delete c.how; n++; }
writeFileSync(p, JSON.stringify(t, null, 1) + '\n');
console.log(`traced ${n}`);
