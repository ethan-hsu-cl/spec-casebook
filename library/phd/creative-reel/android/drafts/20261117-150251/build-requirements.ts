// Requirements of the Android update draft (REQ-011, 2026-11-17): the approved v3 requirements plus the Design Figma,
// read once qa-dm was given access (Q-23). Design file qdzVXIFZeYwcsa6fipmcLH, page 933:4528
// 「261109_AI_transition_feature」: section 「Design」 976:11727 read as regions ds-light / ds-dark (group d1), section
// 「PHD_spec」 933:4752 (an older copy of the PM 「spec」 section) as ds-pm-copy (group d2, superseded).
// Design vs PM follows pass 7 with the Design-first rule (user, 2026-11-13): the Design (dated by its page label,
// 2026-11-09) wins wherever its frames cover the case; the PM items that are not on the Design stay as PM-only.
// Re-runnable: node library/phd/creative-reel/android/drafts/20261117-150251/build-requirements.ts
import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url));
let s = readFileSync(join(HERE, '..', '..', 'requirements.md'), 'utf8').replace(/\r\n/g, '\n');
const rep = (a: string, b: string) => { if (!s.includes(a)) throw new Error(`missing: ${a.slice(0, 90)}`); s = s.replace(a, b); };
const line = (id: string, text: string) => { // replace the whole requirement line of an id
  const re = new RegExp(`^- ${id} .*$`, 'm');
  if (!re.test(s)) throw new Error(`no line ${id}`);
  s = s.replace(re, `- ${id} ${text}`);
};
const after = (id: string, text: string) => { // insert lines after a requirement line
  const re = new RegExp(`^- ${id} .*$`, 'm'), m = s.match(re);
  if (!m) throw new Error(`no line ${id}`);
  s = s.replace(m[0], `${m[0]}\n${text}`);
};

// ---- header -------------------------------------------------------------------------------------------------------
rep(`Source tags: \`[PM:<board>]\`, board IDs from \`specs/2026-11-02/extracted/boards.json\`. The file is one PM-owned Figma
export carrying both the mockups (UI strings) and the rule boxes; there is no separate Design or MX file.`,
`Source tags: \`[PM:<board>]\`, board IDs from \`specs/2026-11-02/extracted/boards.json\`; \`[DS:ds-light]\` / \`[DS:ds-dark]\`
for the Design Figma boards (below). The PDF is one PM-owned Figma export carrying both the mockups and the rule boxes;
there is no MX file.`);
rep(`The Design file is not readable yet (Q-23, \`extracted/figma-pending.json\`): UI
strings still come from the PM mockups.`,
`**Design Figma read 2026-11-17 (REQ-011)** once qa-dm was given access (Q-23 answered): file
qdzVXIFZeYwcsa6fipmcLH, page 933:4528 「261109_AI_transition_feature」 (dated 2026-11-09), section 「Design」 976:11727
read as two region boards, \`ds-light\` (7 iPhone screens and 3 Import-prompt variants) and \`ds-dark\` (the same 7
screens in dark), group d1; the page's 「PHD_spec」 section (933:4752) is an older copy of the PM 「spec」 section (it
still has the 待確認 lines the PM page answers and no intro page) and is superseded (\`ds-pm-copy\`, group d2); the
page's 「PDR_SPEC」 frame is PowerDirector and not read. The Design draws screens only (no notes, no arrows). Where it and
the PM disagree the Design wins (pass 7, Design first, 2026-11-13: the PM items are undated and none cites a bug): UI
strings, the picker tray, the Import prompt, the confirm page layout, the Text Language sheet and My AI Artwork now
follow the Design, with the PM version in the requirement or the row's Notes. What the Design does not draw (intro
page, Edit Room jump, deeplink, photo tips sheet, the red tray line, the toast, Cinematic and AI Transition specifics)
stays PM-only.`);
rep(`REQ-010 (Android only; Design after access).`, `REQ-010 (Android only; Design after access), REQ-011 (Design Figma analysed).`);

// ---- room ---------------------------------------------------------------------------------------------------------
line('R-006', `[PM:room; DS:ds-light] The room has no tabs: one page of sections from top to bottom, the three features mixed. Section titles as the Design draws them: 「Cinematic Styles 🎬」 = CineStory, 「Year-End Recap 🎉」 = Creative (Opus 5.5; further Creative sections such as 「Christmas Time 🎄」 per the PM), 「Cool Transition 🎞️」 = AI Transition. (The PM drew 「Year-End Recap 📅」 and 「Cool Transitions 🤳🏻」; Design first. Titles are CMS category names.)`);
line('R-007', `[PM:room; DS:ds-light] Each section is a category (CMS category = section) showing its template cards in a horizontal row; Cinematic Styles cards carry a small inset of a photo at their bottom left (Design).`);
line('R-008', `[PM:room; DS:ds-light; KB: KP-020] The room's top bar shows 「‹」, the credit pill and the History button (as drawn). The credit pill shows a blue diamond icon, the account's current credit balance and 「⊕」; tapping it opens the Buy Credit page.`);

// ---- preview ------------------------------------------------------------------------------------------------------
line('R-029', `[PM:preview; DS:ds-light] The Preview's top bar has 「‹」, an ⓘ icon next to it and the credit pill (Design; the PM drew a 「View photo tips」 text button at the top left); a mute button sits on the right side above the template text.`);
line('R-031', `[PM:preview; DS:ds-light] At the bottom: template name, description and the photo count with an image icon (Design: 「1 Photo」; a range template's count 「5–15 photos」 is PM-only, wording Q-36), then the CTA 「Use Template」.`);
line('R-033', `[PM:preview; DS:ds-light] The first time the room is entered a finger animation (a hand with up arrows over the demo, Design 「SwipeHint」) guides swiping up / down; it is not shown again.`);
line('R-035', `[PM:preview; DS:ds-light] The Preview has 「‹」, ⓘ and the credit pill at the top (as drawn); 「‹」 returns to the room (no arrow drawn, Q-8).`);
line('R-036', `[PM:preview; DS:ds-light] The photo tips open from the Preview's top-left ⓘ (Design; the PM's 「View photo tips」 label; that ⓘ opens the tips is assumed, Q-28) only when tapped; they never pop up by themselves.`);
line('R-037', `[PM:preview] The tips sheet shows 「Photo tips」, 「✓ Recommended」 with example images and bullets, 「✕ Avoid」 with example images and bullets, and 「Got it」. PM-only: no Design frame yet (Design 2026-11-09).`);

// ---- picker -------------------------------------------------------------------------------------------------------
line('R-041', `[PM:picker; DS:ds-light] 「Use Template」 goes straight to the picker 「Add photos」 (「‹」, album 「Recent ⌄」); several photos can be picked and the pick order is shown as orange number badges 1, 2, 3 … at each picked photo's top right, with an orange frame round it (Design; the PM drew 「Add Photos」, 「Recents ▾」 and 01, 02 …).`);
line('R-042', `[PM:picker; DS:ds-light] The bottom tray shows 「Select {min} to {max} photos to continue.」, 「Next」 and the picked thumbnails in pick order, each with 「×」 (horizontal scroll). The picker shows no 「{picked}/{max}」 count (Design; the PM drew 「Select 5–15 photos」 and 「7/15」).`);
line('R-043', `[PM:picker; DS:ds-light] 「Next」 works only when the count is within min–max: below min it is grey (disabled), as the Design draws it with nothing picked. With photos picked but fewer than min, the PM draws the red line 「Select at least {min} photos ({n} more)」 under the tray text (the Design draws no such state; whether the red line shows for a manual pick is Q-30, assumption yes).`);
line('R-044', `[PM:picker] When min = max the tray says 「Select N photos」 (「Select 1 photo」, AI Transition 4 or 6). PM-only: the Design draws only a range template's tray (wording Q-36).`);
line('R-049', `[PM:picker; DS:ds-light] 「Recent ⌄」 switches the album (drawn control).`);
after('R-050', `- R-123 [DS:ds-light] Every photo in the picker grid has an expand icon at its bottom right; tapping it opens that photo in a full view without picking it (what opens is not stated: assumption a full-screen view that Back or 「‹」 closes, Q-29).
- R-124 [DS:ds-light] 「×」 on a tray thumbnail unpicks that photo: the thumbnail leaves the tray and the photo's badge and frame go on the grid (renumbering: Q-11); below min 「Next」 turns grey again.`);
line('R-052', `[PM:picker; DS:ds-light] Above the tray the picker shows a prompt card: thumbnails of the remembered photos, the text 「Use the N photos you picked last time?」, 「×」 at the top right and 「Import」 (Design 03-1 – 03-4; the PM drew the text, 「Import」 and 「×」 without thumbnails).`);
after('R-117', `- R-125 [DS:ds-light] With more than three photos remembered the prompt shows three thumbnails, the third covered by 「+{N−3}」 (「Use the 8 photos you picked last time?」 with 「+5」); with three or fewer it shows one thumbnail per photo.
- R-126 [DS:ds-light] The prompt text follows N: 「Use the 3 photos you picked last time?」, 「Use the 2 photos you picked last time?」 and, for one photo, 「Use the photo you picked last time?」 (Design 03-2 – 03-4). A remembered set of 1 – 3 photos on a template with photo input > 1 arises when the other remembered photos were deleted from the Gallery (R-056); the PM says a set of 1 photo shows no prompt (R-057), which the Design's one-photo card contradicts (Q-27, assumption: the Design card shows when one remembered photo is left; R-057 still holds for a set applied with 1 photo).`);

// ---- confirm page -------------------------------------------------------------------------------------------------
line('R-060', `[PM:confirm; DS:ds-light] Top: template thumbnail, name, the photo count with an image icon and 「9:16」 with a ratio icon, a divider below, with 「‹」 and the credit pill at the top (Design; the PM drew 「{min}–{max} photos · output 9:16」; the Design shows 「9:16」 on one of its two frames, Q-31).`);
line('R-061', `[PM:confirm; DS:ds-light] 「Your photos ({n}/{max})」 (the count in brackets after the title, Design; the PM drew it at the right) with the hint 「Long-press to reorder · tap × to remove」, then every input image with 「×」.`);
line('R-064', `[PM:confirm; DS:ds-light] The 「+」 tile, the first tile of the photo grid with a dashed orange frame (Design; the PM drew it last), returns to the picker carrying the current selection.`);
line('R-067', `[PM:confirm; DS:ds-light] Creative only: a 「Text Language」 bar above Generate (grey bar, the chosen language and 「⌄」, Design; the PM wrote 「Text language」 「English ▾」), default the device language. AI Transition and Cinematic pages have no Text Language.`);
line('R-068', `[PM:confirm; DS:ds-light] The button reads 「Generate」 with the credit icon and 「60」 on the Creative template drawn (「Top 5 of My Year」); the credit number is binding (other templates' prices: Q-9).`);

// ---- text language ------------------------------------------------------------------------------------------------
line('R-073', `[PM:text-language; DS:ds-light] The default is the device language: its row is highlighted with 「Device Language」 beside the name and a ✓ (Design; the PM wrote 「(Device language)」).`);
line('R-074', `[PM:text-language; DS:ds-light] The list is a bottom sheet (handle, page dimmed behind) listing each language in its own script with its English name: 「English」, 「繁體中文 Chinese (Traditional)」, 「简体中文 Chinese (Simplified)」, 「日本語 Japanese」, 「한국어 Korean」, 「Español Spanish」, 「Français French」, 「Deutsch German」 (Design); it holds every language PhD supports, the same list on iOS and Android, and scrolls (PM, which also lists 「Português」, 「Italiano」, 「ภาษาไทย」 …; Q-32).`);
after('R-077', `- R-127 [DS:ds-light] The Text Language sheet closes without a change when the dimmed page is tapped or the handle dragged down (the Design draws a handle and a dimmed page; not stated, Q-32).`);

// ---- artwork ------------------------------------------------------------------------------------------------------
line('R-078', `[PM:artwork; DS:ds-light] After Generate the app shows My AI Artwork on the 「Reel Creator」 tab with the new item: a grey tile 「Processing...」, its date and template name, and a time estimate (「9 minutes remaining ...」) with a progress bar (Design; the PM drew 「Processing…」 and 「3 minutes remaining…」).`);
line('R-080', `[PM:artwork; DS:ds-light] The Artwork tab is named 「Reel Creator」, second after 「Image to Video」, followed by the app's other feature tabs in a scrolling row (Design: 「AI Face Swap」, 「AI …」; the PM drew 「Character Motion Swap」).`);
line('R-082', `[PM:artwork; DS:ds-light] 「Create more」 returns to the Reel Creator room (Design wording; the PM wrote 「Create More」).`);
after('R-083', `- R-128 [DS:ds-light] My AI Artwork shows 「‹」, the title 「My AI Artwork」 and an ⓘ at the top right; what ⓘ opens is not stated (Q-33).
- R-129 [DS:ds-light] 「Select」 at the top right of the list switches the list to selection (what it then offers is not stated, Q-33).
- R-130 [DS:ds-light] When the estimate has run out before the job ends, the processing card shows 「Almost done」 in place of the remaining time.
- R-131 [DS:ds-light] A finished card shows the result's thumbnail, its date, the template name and 「Expires on {date}」 (how long results are kept is not stated, Q-33).
- R-132 [DS:ds-light] A job whose upload was interrupted shows a ⚠ tile and 「Resume to Upload」; tapping it resumes the job, which then charges no second time (Design; answers part of Q-12).`);

// ---- cinematic ----------------------------------------------------------------------------------------------------
line('R-085', `[PM:cinematic; DS:ds-light] The Cinematic confirm page shows 「1 Photo」 and 「9:16」 in the header (Design format), 「Your photos (1/1)」 and 「Tap the photo to replace」 (PM); tapping the photo replaces it.`);
line('R-086', `[PM:cinematic] The Cinematic confirm page has no Text Language (PM; the Design's one confirm frame pairs the sample name 「Micro Cinema」 with 7/15 photos and Text Language, read as sample content, Q-35).`);

// ---- dark ---------------------------------------------------------------------------------------------------------
rep(`## Android
- R-089`, `## Dark theme
- R-133 [DS:ds-dark] Every screen of the flow (room, Preview, picker, Import prompt, confirm page, Text Language sheet, My AI Artwork) has a dark version with the same content and controls, legible on the dark background (Design ds-dark). What turns it on is not stated (Q-34, assumption: the phone's dark theme).

## Android
- R-089`);

// ---- open questions -----------------------------------------------------------------------------------------------
rep(`- Q-10 Answered for the PM file (2026-11-17, REQ-009): the PM Figma was compared with the PDF; it adds the intro page (R-118 – R-122) and the memory clauses (R-114 – R-117). The Design file is Q-23.`,
`- Q-10 Answered (2026-11-17): the PM Figma was compared with the PDF (REQ-009; intro page R-118 – R-122, memory clauses R-114 – R-117) and the Design Figma read (REQ-011; R-123 – R-133 and the Design-first changes).`);
rep(`- Q-12 Generation failure (copy, refund, retry) and leaving during processing are not stated.`,
`- Q-12 Generation failure (copy, refund) and leaving during processing are not stated; the Design's Artwork page answers the interrupted-upload case (⚠, 「Resume to Upload」, R-132).`);
rep(/- Q-23 The Design spec[^\n]*/.exec(s)![0],
`- Q-23 Answered (user, 2026-11-17, REQ-011): access to the Design file was granted to qa-dm; read 2026-11-17 (groups d1, d2). R-123 – R-133 and the rows marked 「Design first」.`);
rep(`- Q-22 Is 「≤ 10 MB」`, `- Q-27 The Design draws a one-photo Import prompt 「Use the photo you picked last time?」 (and 2- and 3-photo ones), while the PM says the prompt is not shown when only 1 photo was picked last time (R-057). On a template with photo input > 1 a set of 1 – 3 is reachable only when remembered photos were deleted from the Gallery. Assumption: the Design cards show with the photos still in the Gallery (1, 2 or 3); R-057 holds for a set applied with 1 photo. R-057, R-126, TC-137 – TC-139.
- Q-28 The Design replaces the Preview's 「View photo tips」 text with an ⓘ icon next to 「‹」 and draws no tips sheet. Assumption: ⓘ opens the photo tips sheet the PM describes. R-029, R-036, TC-024, TC-033, TC-035.
- Q-29 Picker: what does each photo's expand icon open (assumption: a full-size view, closed by Back or 「‹」, the photo not picked)? And the Design draws a tooltip 「Upload at leat 2 photos」 (typo 「leat」, and 2 does not match the 5–10 drawn) over the grid: when does it show and what is its wording? No row tests the tooltip until answered. R-123, TC-135, TC-150.
- Q-30 Picking fewer than min by hand: the Design draws only the empty picker (grey 「Next」, plain tray text), the PM the red 「Select at least {min} photos ({n} more)」 after an Import. Assumption: the red line shows after a manual pick below min too. R-043, TC-038.
- Q-31 Confirm page header: the Design shows 「9:16」 with a ratio icon on 04-1 (light, with the language sheet) but not on 04 or the dark frames, and shows the template's count 「1 Photo」 where the PM wrote 「5–15 photos · output 9:16」. Assumption: the header shows the count as on the Preview and 「9:16」. R-060, TC-063, TC-094.
- Q-32 Text Language: the Design's sheet shows 8 languages ending at 「Deutsch German」; the PM lists every PhD language (also Português, Italiano, ภาษาไทย …). Assumption: the full PhD list, scrolling, in the Design's format. How the sheet closes without a choice (dimmed page, handle) is not stated. R-074, R-127, TC-075, TC-077, TC-140.
- Q-33 My AI Artwork: the Design draws the generic Artwork page (ⓘ, 「Select」, 「Expires on」, 「Resume to Upload」, sample 「Image to Video - A Template Name 2」). What do ⓘ and 「Select」 offer on the Reel Creator tab, and how long are results kept? Rows record them. R-128, R-129, R-131, TC-142, TC-144, TC-145.
- Q-34 The Design draws every screen in light and dark. What turns dark on (the phone's dark theme, an app setting)? Assumption: the phone's dark theme; switching it needs the user's go-ahead on the QA phone. R-133, TC-146 – TC-149.
- Q-35 The Design's only confirm frame pairs 「Micro Cinema」 「1 Photo」 (a Cinematic template) with 7/15 photos, the 「+」 tile and Text Language. Assumption: sample content; the Cinematic confirm page stays as the PM draws it (1/1, Tap the photo to replace, no Text Language). R-085, R-086, TC-094.
- Q-36 Count wording: the Design writes 「1 Photo」 (capital P, image icon) and 「Select 5 to 10 photos to continue.」; the PM 「5–15 photos」, 「1 photo」 and, for min = max, 「Select N photos」. The Design draws no range count on the Preview and no min = max tray. Assumption: Design wording where drawn, PM wording elsewhere. R-031, R-042, R-044, TC-030, TC-092, TC-098.
- Q-22 Is 「≤ 10 MB」`);

// ---- grids --------------------------------------------------------------------------------------------------------
rep(`| Creative generation | TC-085, TC-117 | TC-086, TC-087, TC-118 | n/a (spec silent, Q-12) | n/a (spec silent, Q-12) | TC-088, TC-116 | TC-085 (「… minutes remaining…」 shown) | TC-121 |`,
`| Creative generation | TC-085, TC-117 | TC-086, TC-087, TC-118, TC-142 | TC-143 (upload interrupted: ⚠ 「Resume to Upload」) | TC-143 (「Resume to Upload」) | TC-088, TC-116 | TC-085 (「… minutes remaining ...」 shown), TC-141 (「Almost done」) | TC-121 |`);
rep(`| Picker | TC-052 | TC-106 |`, `| Picker | TC-052 | TC-106 |
| Full photo view (expand icon) | TC-135 | TC-150 |`);
rep(`| Text language list | n/a (closed by choosing, TC-078) | TC-109 |`, `| Text Language sheet | TC-078 (closed by choosing), TC-140 (dimmed page, handle) | TC-109 |`);
rep(`- Picker → Preview: TC-106; with the Import prompt shown: TC-107`, `- Picker → Preview: TC-106; with the Import prompt shown: TC-107
- Full photo view (picker expand icon) → back to the picker, picks unchanged: TC-150`);
rep(`- Text language list → closes, language unchanged: TC-109`, `- Text Language sheet → closes, language unchanged: TC-109`);
rep(`| R-120 | the 「Don’t show again」 choice is stored | intro page absent on re-entry and after relaunch | TC-130 |`,
`| R-120 | the 「Don’t show again」 choice is stored | intro page absent on re-entry and after relaunch | TC-130 |
| R-132 | a resumed upload charges no second time | credit balance before Generate and after the resumed job | TC-143 |
| R-126 | N counts only the remembered photos still in the Gallery | the N and thumbnails after deleting remembered photos | TC-137, TC-138, TC-139 |`);
rep(`| R-017 | AI Transition GUID | TC-016 |`, `| R-017 | AI Transition GUID | TC-016 |
| R-126 | more than 3 remembered (3 thumbnails, 「+N−3」) | TC-054 |
| R-126 | 3 remembered | TC-137 |
| R-126 | 2 remembered | TC-138 |
| R-126 | 1 remembered (「Use the photo …」) | TC-139 |
| R-133 | light theme | TC-005, TC-024, TC-037, TC-054, TC-063, TC-075, TC-085 |
| R-133 | dark theme | TC-146, TC-147, TC-148, TC-149 |`);

// ---- traces -------------------------------------------------------------------------------------------------------
rep(`### Controls (PDF-read) → rows`, `- Design (2026-11-17, groups d1 / d2): the Design boards carry no notes, only screen text, traced to R-006 – R-008, R-029, R-031, R-033, R-035, R-036, R-041 – R-043, R-049, R-052, R-060, R-061, R-064, R-067, R-068, R-073, R-074, R-078, R-080, R-082, R-085, R-123 – R-133 (ui); the tooltip 「Upload at leat 2 photos」 → Q-29; sample texts (「Micro Cinema」 on the confirm page, 「Image to Video - A Template Name 2」, 「10 Outfits」 on Artwork cards) → label. ds-pm-copy (933:4752) → older: PM page 7238:8623 (its 待確認 lines are answered there, R-114 – R-117; it has no intro page).

### Controls (PDF-read) → rows`);
rep(`Since 2026-11-17 the Figma inventory (\`inventory.json\`; buttons the PM mockups draw as plain frames added by hand in \`inventory-overrides.json\`) is traced in \`control-trace.json\`.`,
`Since 2026-11-17 the Figma inventory (\`inventory.json\`; buttons the PM mockups draw as plain frames added by hand in \`inventory-overrides.json\`) is traced in \`control-trace.json\`, the Design controls (ds-light, ds-dark; image cards, grid photos, tabs and 「Select」 added by hand) included; the controls of the superseded PM copy (ds-pm-copy) are traced n/a.`);
rep(`| REQ-010 | Android table only (no iOS table); Design analysis waits for access (Q-23) |`,
`| REQ-010 | Android table only (no iOS table); Design analysed after access (REQ-011) |
| REQ-011 | R-006 – R-008, R-029 – R-037, R-041 – R-044, R-049, R-052, R-060 – R-068, R-073, R-074, R-078, R-080, R-082, R-085, R-086, R-123 – R-133 (Q-23 answered; Q-27 – Q-36) |`);

writeFileSync(join(HERE, 'requirements.md'), s);
console.log('requirements.md written');
