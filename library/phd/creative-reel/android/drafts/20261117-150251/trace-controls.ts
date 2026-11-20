// Control trace of the Design groups (pass 11, REQ-038) after `node scripts/controls.ts phd/creative-reel android
// --draft 20261117-150251`: presses for the Design controls the auto trace left open, and corrections of label
// matches that named rows which only mention the text. Re-runnable after controls.ts.
// Usage: node library/phd/creative-reel/android/drafts/20261117-150251/trace-controls.ts
import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url));
const p = join(HERE, 'control-trace.json'), t = JSON.parse(readFileSync(p, 'utf8'));
const H = 'by hand 2026-11-17 (Design, REQ-011)';
const PRESS: Record<string, string> = {
  'K-db055e': 'TC-008',                 // credit pill
  'C-e85bec': 'TC-136, TC-065',         // 「×」 on tray thumbnails (picker) and on confirm photos: two roles, one row each
  'K-a8bd56': 'n/a: an empty layer at the picker\'s top right; the board image draws nothing there',
  'K-3676ec': 'n/a: the 「!」 icon inside the tooltip 「Upload at leat 2 photos」, not a button (tooltip: Q-29)',
  'K-36e23c': 'TC-038, TC-043',         // pick-order badges: shown on pick, a picked photo tapped again unpicks
  'K-fa2ff4': 'TC-112',                 // History
  'K-d0626d': 'TC-135, TC-150',         // expand icon on grid photos
  'K-a73b60': 'TC-056',                 // prompt 「×」
  'K-286bec': 'TC-140',                 // dimmed page behind the Text Language sheet
  'K-56bf54': 'TC-023',                 // template card
  'K-c44d9a': 'TC-064',                 // confirm photo tile, long-press drag
  'K-48cd04': 'TC-078',                 // language row
  'K-6ecdc6': 'TC-086',                 // Artwork card
  'K-3aeda7': 'TC-068',                 // 「+」 tile
  'K-8cad01': 'n/a: status icon on an interrupted card, not a button (TC-143 checks it)',
  'K-00fb1f': 'TC-075',                 // 「⌄」 of the Text Language bar
  'K-e3f9c3': 'n/a: icon beside the photo count, decorative',
  'K-2f1a34': 'TC-145',                 // Artwork ⓘ
  'K-f7cf82': 'n/a: icon beside 「9:16」, decorative',
  'K-313574': 'TC-025',                 // mute
  'K-72e947': 'TC-009, TC-031, TC-071', // 「‹」 on room, Preview, confirm page
  'K-ab50f0': 'TC-052, TC-088',         // 「‹」 on picker and My AI Artwork
  'K-504a32': 'TC-033',                 // the Preview's ⓘ (layer named top/ic_back_n, drawn as ⓘ next to 「‹」)
  'K-6a3aa8': 'TC-051',                 // 「Recent ⌄」
  'K-7dd672': 'n/a: superseded: older copy of the PM spec in the Design file (933:4752); the PM page 7238:8623 is read as p1',
  // label matches corrected to the rows that press the control
  'C-274035': 'TC-089',
  'K-15574a': 'TC-038, TC-043',
  'K-a5f8a0': 'TC-037',
  'K-4fe9cb': 'TC-053, TC-039',
  'K-2d6b08': 'TC-055, TC-137',
  'K-fa0824': 'TC-074, TC-067',
  'K-3056bc': 'TC-075, TC-148',
};
let n = 0;
for (const e of t.entries) if (PRESS[e.group]) { e.press = PRESS[e.group]; e.how = H; n++; }
const left = t.entries.filter((e: any) => !e.press).map((e: any) => `${e.group} ${e.name} ${e.label}`);
writeFileSync(p, JSON.stringify(t, null, 1) + '\n');
console.log(`${n} traced; untraced: ${left.length ? left.join(', ') : 'none'}`);
