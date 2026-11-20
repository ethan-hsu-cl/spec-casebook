// Requirements of the Android update draft (REQ-009): the approved v1 requirements plus the PM Figma catch-up.
// Re-runnable: node library/phd/creative-reel/android/drafts/20261117-114254/build-requirements.ts
import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url));
let s = readFileSync(join(HERE, '..', '..', 'requirements.md'), 'utf8').replace(/\r\n/g, '\n');
const rep = (a: string, b: string) => { if (!s.includes(a)) throw new Error(`missing: ${a.slice(0, 80)}`); s = s.replace(a, b); };

rep(`**PDF-only analysis** (\`extracted/figma-pending.json\`): Figma steps 8 and 10 are
owed.`, `**PM Figma caught up 2026-11-17 (REQ-009)**: the PDF's source, PM page 7238:8623
section 「spec」, read through figma-pm (group p1, \`extracted/figma-inventory-p1.json\`, board images in
\`extracted/figma/\`); it adds the intro page (\`[PM:tutorial]\`, R-118 – R-122) and three picker-memory clauses
(R-114 – R-117, R-051 reworded). The Design file is not readable yet (Q-23, \`extracted/figma-pending.json\`): UI
strings still come from the PM mockups.`);
rep(`Request ledger: REQ-001 (this table), REQ-003 (K75 / K76).`, `Request ledger: REQ-001 (this table), REQ-003 (K75 / K76), REQ-009 (PM Figma catch-up), REQ-010 (Android only; Design after access).`);
rep(`## Entry from Edit Room`, `## Intro page (Figma only)
- R-118 [PM:tutorial] Entering the room shows the Reel Creator intro page: a demo video at the top, the title 「Reel Creator」, the text 「Turn photos into post-worthy videos with trendy transitions, cinematic styles, and creative effects!」, the button 「Try Now」, the checkbox 「Don’t show again」 and 「‹」 at the top left. Its demo video and copy are the ones drawn (【Demo video 調整】 • 文案同左).
- R-119 [PM:tutorial] 「Try Now」 closes the intro page and shows the room.
- R-120 [PM:tutorial] With 「Don’t show again」 ticked, the intro page is not shown on later room entries, including after the app is relaunched.
- R-121 [PM:tutorial] Without the tick the intro page is shown again on the next room entry (when it shows is not stated: assumption, as today's Cinematic Reel Creator intro, Q-24).
- R-122 [PM:tutorial] 「‹」 on the intro page leaves the room to the page it was opened from (no arrow drawn, Q-8).

## Entry from Edit Room`);
rep(`- R-051 [PM:picker] A session runs from app launch to session end; within it, entering the picker again remembers the photos picked last time.`,
  `- R-051 [PM:picker] A session is one visit to the Reel Creator room (「App launch 到 session 結束」 and 「離開房間 = 離開 session」); within it, entering a picker again remembers the photos picked last time.`);
rep(`- R-059 [PM:picker] The memory applies across templates in the same session (any later picker entry, e.g. another template's).`,
  `- R-059 [PM:picker] The memory applies across templates in the same session (any later picker entry, e.g. another template's).
- R-114 [PM:picker] Leaving the room ends the session and clears the memory: entering the room again, the picker shows no Import prompt (Figma only).
- R-115 [PM:picker] 「Picked last time」 is the set last applied with 「Next」; a selection changed and left without Next does not replace it (Figma only; answers Q-3).
- R-116 [PM:picker] The memory exists only inside Reel Creator: the app's other pickers never show the Import prompt (Figma only; answers Q-4).
- R-117 [PM:picker] The prompt is shown only on templates whose photo input is more than 1: a Cinematic Styles picker (「Select 1 photo」) never shows it (Figma only; answers Q-7).`);
rep(`- Q-3 「Picked last time」 = the set last confirmed with Next, or the set last generated? R-051, R-052.
- Q-4 Is the memory only inside Reel Creator, or shared by the app's other pickers? R-051.`,
  `- Q-3 Answered by the PM Figma (2026-11-17, REQ-009): 「上次選的圖」 = the set last applied with Next. R-115.
- Q-4 Answered by the PM Figma (2026-11-17, REQ-009): 「記憶只在 Reel Creator 內」. R-116.`);
rep(`- Q-7 Cinematic picker: when the last pick had several photos, is the Import prompt shown (the import must then be cut to 1)? R-084.`,
  `- Q-7 Answered by the PM Figma (2026-11-17, REQ-009): 「圖片 input >1 的 template 再 show」, so the Cinematic picker shows no prompt. R-117. (The Cinematic note box still carries the old 待確認 line; the memory note is the newer rule.)`);
rep(`- Q-10 Figma not compared with the PDF: frames newer than the export may be missing (PDF-only analysis; no Figma links supplied).`,
  `- Q-10 Answered for the PM file (2026-11-17, REQ-009): the PM Figma was compared with the PDF; it adds the intro page (R-118 – R-122) and the memory clauses (R-114 – R-117). The Design file is Q-23.`);
rep(`- Q-22 Is 「≤ 10 MB」`, `- Q-23 The Design spec (Figma 「Cinematic Reel Creator (CineStory)」, node 976:11727) is not shared with the QA Design account (qa-dm@cyberlink.com): please share it (view or Dev). Until then UI strings, the intro page and button labels come from the PM mockups, and the Design screens' controls are not inventoried. All rows.
- Q-24 When does the intro page show? Assumption: on every room entry until 「Don’t show again」 is ticked and 「Try Now」 tapped (as today's Cinematic Reel Creator intro); also unknown whether a template deeplink (R-015) shows it first. R-118, R-120, R-121, TC-128 – TC-130.
- Q-25 The memory ends when the room is left (R-114): does opening My AI Artwork (History button, or Generate) count as leaving? Assumption: no, only leaving the room with 「‹」 / Back; TC-134 records it. R-051, R-114.
- Q-26 Should Reel Creator results appear in the Launcher's Recent (domain KP-027: new features' works reach Recent when they are meant to)? The spec is silent; no row. R-079.
- Q-22 Is 「≤ 10 MB」`);
rep(`- KP-015 (K36e), KP-018 (K36d), KP-027 (K47c) → not reviewed in REQ-004 (missing from its lists); the next draft
  decides them. KP-027 (new features' works reach Recent) likely applies to Reel Creator.`,
  `- KP-015 (K36e) → n/a (Mine entitlement after buying Premium: not in this flow). KP-018 (K36d) → n/a (Credit Auto
  Pass naming: no Auto Pass in this flow). KP-027 (K47c) → Q-26 (spec silent on Recent). KP-134 → n/a (Adjustment room Undo: no editing in this flow). Decided 2026-11-17 (REQ-009).`);
rep(`- R-100 [PM:cinematic flow arrow cinematic-a2 ] Cinematic 「Next」 → Cinematic confirm page. Walked by: TC-094.`,
  `- R-100 [PM:cinematic flow arrow cinematic-a2 ] Cinematic 「Next」 → Cinematic confirm page. Walked by: TC-094.

Since the Figma catch-up each arrow carries its Figma node id in \`arrows.json\` (room-a1 7252-463, preview-a1 7337-1142, preview-a2 7337-1195, picker-a1 7337-1197, picker-a2 7337-1199, picker-a3 7337-1201, confirm-a1 7337-1203, text-language-a1 7271-490, cinematic-a1 7337-1205, cinematic-a2 7337-1207); the intro page draws no arrow.`);
rep(`| Room | TC-009 | TC-103 |`, `| Intro page | TC-131 | TC-132 |
| Room | TC-009 | TC-103 |`);
rep(`- Reel Creator room → leaves the room: TC-103`, `- Reel Creator intro page → as 「‹」: TC-132
- Reel Creator room → leaves the room: TC-103`);
rep(`| R-075 | the chosen language code is passed to the engine | language of the text in the finished reel | TC-081, TC-082, TC-083 |`,
  `| R-075 | the chosen language code is passed to the engine | language of the text in the finished reel | TC-081, TC-082, TC-083 |
| R-114 | leaving the room clears the memory | no Import prompt after leaving and re-entering the room | TC-134 |
| R-115 | the remembered set is the one applied with Next | the N in the prompt after a pick changed without Next | TC-133 |
| R-120 | the 「Don’t show again」 choice is stored | intro page absent on re-entry and after relaunch | TC-130 |`);
rep(`| R-016 | CineStory GUID | TC-017 |`, `| R-016 | CineStory GUID | TC-017 |
| R-120 | ticked (not shown again) | TC-130 |
| R-121 | not ticked (shown again) | TC-129 |`);
rep(`- cinematic: R-084 – R-086; 待確認 Import → Q-7.`, `- cinematic: R-084 – R-086; 待確認 Import → Q-7 (answered by the memory note, R-117).
- Figma-only texts (2026-11-17, group p1): memory note 「圖片input >1 的 template 再 show」 → R-117; 「「上次選的圖」= 上次按 Next (apply 的那組)」 → R-115; 「記憶只在 Reel Creator 內」 → R-116 (red 待確認 in the PDF); 「離開房間 = 離開 session, 記憶清除」 → R-114, R-051. tutorial: 「【 Demo video 調整】 • 文案同左」 → R-118; mockup 「Reel Creator」 / 「Turn photos into …」 / 「Try Now」 / 「Don’t show again」 → R-118 – R-121 (ui).`);
rep(`Cinematic confirm: photo tap TC-095. Artwork: tabs TC-089 · card TC-086 · Create More TC-091. No inputs with a keyboard.`,
  `Cinematic confirm: photo tap TC-095. Artwork: tabs TC-089 · card TC-086 · Create More TC-091. Intro page: Try Now TC-129 · Don’t show again TC-130 · ‹ TC-131. No inputs with a keyboard. Since 2026-11-17 the Figma inventory (\`inventory.json\`; buttons the PM mockups draw as plain frames added by hand in \`inventory-overrides.json\`) is traced in \`control-trace.json\`.`);
rep(`| REQ-006 | R-023, R-045 (Q-21, Q-22) |`, `| REQ-006 | R-023, R-045 (Q-21, Q-22) |
| REQ-009 | R-051, R-114 – R-122 (Q-23 – Q-26) |
| REQ-010 | Android table only (no iOS table); Design analysis waits for access (Q-23) |`);

writeFileSync(join(HERE, 'requirements.md'), s);
console.log('ok');
