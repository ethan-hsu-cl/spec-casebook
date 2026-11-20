# Creative Reel (Reel Creator room) — requirements (android)
Spec: Creative Reel.pdf ("Reel Creator（原 Cinematic Reel Creator）— Room & Template Preview", spec set 2026-11-02)

Source tags: `[PM:<board>]`, board IDs from `specs/2026-11-02/extracted/boards.json`; `[DS:ds-light]` / `[DS:ds-dark]`
for the Design Figma boards (below). The PDF is one PM-owned Figma export carrying both the mockups and the rule boxes;
there is no MX file. Mockups are
iPhone frames; Android differences are in "System back". Red note lines are pending items (待決 / 待確認) and are Open
questions unless they state a rule. **PM Figma caught up 2026-11-17 (REQ-009)**: the PDF's source, PM page 7238:8623
section 「spec」, read through figma-pm (group p1, `extracted/figma-inventory-p1.json`, board images in
`extracted/figma/`); it adds the intro page (`[PM:tutorial]`, R-118 – R-122) and three picker-memory clauses
(R-114 – R-117, R-051 reworded). **Design Figma read 2026-11-17 (REQ-011)** once qa-dm was given access (Q-23 answered): file
qdzVXIFZeYwcsa6fipmcLH, page 933:4528 「261109_AI_transition_feature」 (dated 2026-11-09), section 「Design」 976:11727
read as two region boards, `ds-light` (7 iPhone screens and 3 Import-prompt variants) and `ds-dark` (the same 7
screens in dark), group d1; the page's 「PHD_spec」 section (933:4752) is an older copy of the PM 「spec」 section (it
still has the 待確認 lines the PM page answers and no intro page) and is superseded (`ds-pm-copy`, group d2); the
page's 「PDR_SPEC」 frame is PowerDirector and not read. The Design draws screens only (no notes, no arrows). Where it and
the PM disagree the Design wins (pass 7, Design first, 2026-11-13: the PM items are undated and none cites a bug): UI
strings, the picker tray, the Import prompt, the confirm page layout, the Text Language sheet and My AI Artwork now
follow the Design, with the PM version in the requirement or the row's Notes. What the Design does not draw (intro
page, Edit Room jump, deeplink, photo tips sheet, the red tray line, the toast, Cinematic and AI Transition specifics)
stays PM-only. Product: PhotoDirector (the language note says 「PhD 支援的所有語言」; credit pill, AI Creative Studio).
"Creative" = the Opus 5.5 reel templates (Year-End Recap, Christmas Time …); "AI Transition" = Cool Transitions;
"CineStory" = Cinematic Styles. Request ledger: REQ-001 (this table), REQ-003 (K75 / K76), REQ-009 (PM Figma catch-up), REQ-010 (Android only; Design after access), REQ-011 (Design Figma analysed). PHD domain knowledge (`library/phd/knowledge/`, standing input 6; imported K ids kept as `aka`) is applied (REQ-003 K75 / K76, REQ-004 K01–K74): rules that fit the feature are R-101 – R-113 citing `[KB: KP-…]`; the rest are listed in update-plan.md › Not added.

## Room
- R-001 [PM:room] The room formerly called 「Cinematic Reel Creator」 is titled 「Reel Creator」.
- R-002 [PM:room] The Effects button that opens the room is labelled 「Reel Creator」.
- R-003 [PM:room] The Launcher Shortcut for the room is labelled 「Reel Creator」.
- R-004 [PM:room] The Launcher Template row for the room is labelled 「Reel Creator」.
- R-005 [PM:room] The AI Video Page entry for the room is labelled 「Reel Creator」.
- R-006 [PM:room; DS:ds-light] The room has no tabs: one page of sections from top to bottom, the three features mixed. Section titles as the Design draws them: 「Cinematic Styles 🎬」 = CineStory, 「Year-End Recap 🎉」 = Creative (Opus 5.5; further Creative sections such as 「Christmas Time 🎄」 per the PM), 「Cool Transition 🎞️」 = AI Transition. (The PM drew 「Year-End Recap 📅」 and 「Cool Transitions 🤳🏻」; Design first. Titles are CMS category names.)
- R-007 [PM:room; DS:ds-light] Each section is a category (CMS category = section) showing its template cards in a horizontal row; Cinematic Styles cards carry a small inset of a photo at their bottom left (Design).
- R-008 [PM:room; DS:ds-light; KB: KP-020] The room's top bar shows 「‹」, the credit pill and the History button (as drawn). The credit pill shows a blue diamond icon, the account's current credit balance and 「⊕」; tapping it opens the Buy Credit page.
- R-101 [PM:room; KB: KP-026] The History button (a sheet of paper with a clock at its bottom right) opens My AI Artwork with the feature's own tab, 「Reel Creator」, selected.
- R-009 [PM:room] Section order is pending (Meg / CMS, Q-1); the room shows every section whatever the order.

## Intro page (Figma only)
- R-118 [PM:tutorial] Entering the room shows the Reel Creator intro page: a demo video at the top, the title 「Reel Creator」, the text 「Turn photos into post-worthy videos with trendy transitions, cinematic styles, and creative effects!」, the button 「Try Now」, the checkbox 「Don’t show again」 and 「‹」 at the top left. Its demo video and copy are the ones drawn (【Demo video 調整】 • 文案同左).
- R-119 [PM:tutorial] 「Try Now」 closes the intro page and shows the room.
- R-120 [PM:tutorial] With 「Don’t show again」 ticked, the intro page is not shown on later room entries, including after the app is relaunched.
- R-121 [PM:tutorial] Without the tick the intro page is shown again on the next room entry (when it shows is not stated: assumption, as today's Cinematic Reel Creator intro, Q-24).
- R-122 [PM:tutorial] 「‹」 on the intro page leaves the room to the page it was opened from (no arrow drawn, Q-8).

## Entry from Edit Room
- R-010 [PM:room] Entering Reel Creator from the Edit Room first shows a dialog asking whether to jump (as Image to Video), and the photo being edited is saved automatically.
- R-011 [PM:room] Declining the jump dialog keeps the user in the Edit Room with the edit intact (the dialog's cancel branch; copy as I2V, Q-13).
- R-012 [PM:room] After the jump the Reel Creator room opens without carrying the photo in: no template has it preselected, CineStory included (different from today).

## Deeplink
- R-013 [PM:deeplink] The old Cinematic Reel Creator deeplink opens the Reel Creator room.
- R-014 [PM:deeplink] With no parameter the deeplink opens the room.
- R-015 [PM:deeplink] With template = content GUID the deeplink opens that template's Preview page directly, with no photo selected.
- R-016 [PM:deeplink] A CineStory (Cinematic Styles) GUID is supported.
- R-017 [PM:deeplink] A GUID of the new CMS type (AI Transition / Creative) is supported.
- R-018 [PM:deeplink] A GUID that is not found opens the room.
- R-019 [PM:deeplink] The category parameter is not supported (no tabs): a deeplink with only a category opens the room.

## CMS and template data
- R-020 [PM:room] Each template carries DisplayName, description, demo, View photo tips content (Recommend / Avoid) and Photo min / max; the Preview, tips and picker show them.
- R-021 [PM:room] AI Transition templates have min = max, fixed at 4 or 6 photos.
- R-022 [PM:room] Creative templates have min < max per template, possibly more than 10 (e.g. 「5–15 photos」).
- R-023 [PM:room] The output ratio is fixed at 9:16 for every feature (Creative, Cinematic Styles, AI Transition): confirm page 「output 9:16」, and the generated video file is 9:16 in pixels.
- R-024 [PM:room] Creative feature_id is pending (Meg, early November) — NOT TESTABLE: an analytics id with no app-visible effect (Q-2).
- R-025 [PM:room] Schedule: Android 11/E, iOS 12/B, the three features ship together — NOT TESTABLE: release plan.

## Preview
- R-026 [PM:preview] Tapping any template in the room opens a full-screen 9:16 demo that auto-plays and loops.
- R-027 [PM:preview] Swiping up / down on the Preview switches template like Reels.
- R-028 [PM:preview] The swipe range is the template's own category, looping endlessly (after the last comes the first, before the first comes the last).
- R-029 [PM:preview; DS:ds-light] The Preview's top bar has 「‹」, an ⓘ icon next to it and the credit pill (Design; the PM drew a 「View photo tips」 text button at the top left); a mute button sits on the right side above the template text.
- R-030 [PM:preview] The mute button turns the demo's sound off and on.
- R-031 [PM:preview; DS:ds-light] At the bottom: template name, description and the photo count with an image icon (Design: 「1 Photo」; a range template's count 「5–15 photos」 is PM-only, wording Q-36), then the CTA 「Use Template」.
- R-032 [PM:preview] The text lies over the demo with the bottom darkened.
- R-033 [PM:preview; DS:ds-light] The first time the room is entered a finger animation (a hand with up arrows over the demo, Design 「SwipeHint」) guides swiping up / down; it is not shown again.
- R-034 [PM:preview] 「Use Template」 opens the photo picker directly.
- R-035 [PM:preview; DS:ds-light] The Preview has 「‹」, ⓘ and the credit pill at the top (as drawn); 「‹」 returns to the room (no arrow drawn, Q-8).

## View photo tips
- R-036 [PM:preview; DS:ds-light] The photo tips open from the Preview's top-left ⓘ (Design; the PM's 「View photo tips」 label; that ⓘ opens the tips is assumed, Q-28) only when tapped; they never pop up by themselves.
- R-037 [PM:preview] The tips sheet shows 「Photo tips」, 「✓ Recommended」 with example images and bullets, 「✕ Avoid」 with example images and bullets, and 「Got it」. PM-only: no Design frame yet (Design 2026-11-09).
- R-038 [PM:preview] Tips content comes from the CMS and is written per template (Recommended / Avoid text + example images).
- R-039 [PM:preview] The portrait-photo advice is under Recommended (「Portrait (vertical) photos work best」).
- R-040 [PM:preview] 「Got it」 closes the sheet back to the Preview (drawn).

## Photo picker
- R-041 [PM:picker; DS:ds-light] 「Use Template」 goes straight to the picker 「Add photos」 (「‹」, album 「Recent ⌄」); several photos can be picked and the pick order is shown as orange number badges 1, 2, 3 … at each picked photo's top right, with an orange frame round it (Design; the PM drew 「Add Photos」, 「Recents ▾」 and 01, 02 …).
- R-042 [PM:picker; DS:ds-light] The bottom tray shows 「Select {min} to {max} photos to continue.」, 「Next」 and the picked thumbnails in pick order, each with 「×」 (horizontal scroll). The picker shows no 「{picked}/{max}」 count (Design; the PM drew 「Select 5–15 photos」 and 「7/15」).
- R-043 [PM:picker; DS:ds-light] 「Next」 works only when the count is within min–max: below min it is grey (disabled), as the Design draws it with nothing picked. With photos picked but fewer than min, the PM draws the red line 「Select at least {min} photos ({n} more)」 under the tray text (the Design draws no such state; whether the red line shows for a manual pick is Q-30, assumption yes).
- R-044 [PM:picker] When min = max the tray says 「Select N photos」 (「Select 1 photo」, AI Transition 4 or 6). PM-only: the Design draws only a range template's tray (wording Q-36).
- R-045 [PM:picker] Each photo is checked when picked: 300–4096 px, ≤ 10 MB, NSFW, celebrity; a photo that fails is marked. 「10 MB」 does not say decimal or binary (Q-22): rows test below 10,000,000 bytes (accepted) and above 10,485,760 bytes (marked), which hold under both readings.
- R-046 [PM:picker] Both landscape and portrait photos are accepted.
- R-047 [PM:picker] Picking more than max photos is not allowed (Next works only within the range); how a pick past max is refused is not drawn (Q-11).
- R-048 [PM:picker] Tapping a picked photo again unpicks it; the count and tray follow (renumbering not stated, Q-11).
- R-049 [PM:picker; DS:ds-light] 「Recent ⌄」 switches the album (drawn control).
- R-050 [PM:picker] The picker 「‹」 returns to the Preview (no arrow drawn, Q-8).
- R-123 [DS:ds-light] Every photo in the picker grid has an expand icon at its bottom right; tapping it opens that photo in a full view without picking it (what opens is not stated: assumption a full-screen view that Back or 「‹」 closes, Q-29).
- R-124 [DS:ds-light] 「×」 on a tray thumbnail unpicks that photo: the thumbnail leaves the tray and the photo's badge and frame go on the grid (renumbering: Q-11); below min 「Next」 turns grey again.

## Picker memory (NEW)
- R-051 [PM:picker] A session is one visit to the Reel Creator room (「App launch 到 session 結束」 and 「離開房間 = 離開 session」); within it, entering a picker again remembers the photos picked last time.
- R-052 [PM:picker; DS:ds-light] Above the tray the picker shows a prompt card: thumbnails of the remembered photos, the text 「Use the N photos you picked last time?」, 「×」 at the top right and 「Import」 (Design 03-1 – 03-4; the PM drew the text, 「Import」 and 「×」 without thumbnails).
- R-053 [PM:picker] 「Import」 brings in the picked state and stays in the picker (does not leave it).
- R-054 [PM:picker] When the imported count is above the template's max, the tray shows red text and Next stays disabled until photos are removed down to the range.
- R-055 [PM:picker] When the imported count is below the template's min, the tray shows red text 「Select at least {min} photos ({n} more)」 and Next stays disabled until enough are added.
- R-056 [PM:picker] Photos no longer in the phone gallery are not brought in.
- R-057 [PM:picker] When only 1 photo was picked last time, the prompt is not shown.
- R-058 [PM:picker] After the app is relaunched (new session) the prompt is not shown.
- R-059 [PM:picker] The memory applies across templates in the same session (any later picker entry, e.g. another template's).
- R-114 [PM:picker] Leaving the room ends the session and clears the memory: entering the room again, the picker shows no Import prompt (Figma only).
- R-115 [PM:picker] 「Picked last time」 is the set last applied with 「Next」; a selection changed and left without Next does not replace it (Figma only; answers Q-3).
- R-116 [PM:picker] The memory exists only inside Reel Creator: the app's other pickers never show the Import prompt (Figma only; answers Q-4).
- R-117 [PM:picker] The prompt is shown only on templates whose photo input is more than 1: a Cinematic Styles picker (「Select 1 photo」) never shows it (Figma only; answers Q-7).
- R-125 [DS:ds-light] With more than three photos remembered the prompt shows three thumbnails, the third covered by 「+{N−3}」 (「Use the 8 photos you picked last time?」 with 「+5」); with three or fewer it shows one thumbnail per photo.
- R-126 [DS:ds-light] The prompt text follows N: 「Use the 3 photos you picked last time?」, 「Use the 2 photos you picked last time?」 and, for one photo, 「Use the photo you picked last time?」 (Design 03-2 – 03-4). A remembered set of 1 – 3 photos on a template with photo input > 1 arises when the other remembered photos were deleted from the Gallery (R-056); the PM says a set of 1 photo shows no prompt (R-057), which the Design's one-photo card contradicts (Q-27, assumption: the Design card shows when one remembered photo is left; R-057 still holds for a set applied with 1 photo).

## Confirm-generate page (NEW)
- R-060 [PM:confirm; DS:ds-light] Top: template thumbnail, name, the photo count with an image icon and 「9:16」 with a ratio icon, a divider below, with 「‹」 and the credit pill at the top (Design; the PM drew 「{min}–{max} photos · output 9:16」; the Design shows 「9:16」 on one of its two frames, Q-31).
- R-061 [PM:confirm; DS:ds-light] 「Your photos ({n}/{max})」 (the count in brackets after the title, Design; the PM drew it at the right) with the hint 「Long-press to reorder · tap × to remove」, then every input image with 「×」.
- R-062 [PM:confirm] Long-press and drag reorders the photos (as AI Creative Studio).
- R-063 [PM:confirm] 「×」 on a photo removes it and the count goes down.
- R-064 [PM:confirm; DS:ds-light] The 「+」 tile, the first tile of the photo grid with a dashed orange frame (Design; the PM drew it last), returns to the picker carrying the current selection.
- R-065 [PM:confirm] AI Transition: the order on this page is the order the photos appear in the output.
- R-066 [PM:confirm] Creative: the output does not have to follow the user's order, but every input photo is used (content team), with no extra notice on the page.
- R-067 [PM:confirm; DS:ds-light] Creative only: a 「Text Language」 bar above Generate (grey bar, the chosen language and 「⌄」, Design; the PM wrote 「Text language」 「English ▾」), default the device language. AI Transition and Cinematic pages have no Text Language.
- R-068 [PM:confirm; DS:ds-light] The button reads 「Generate」 with the credit icon and 「60」 on the Creative template drawn (「Top 5 of My Year」); the credit number is binding (other templates' prices: Q-9).
- R-069 [PM:confirm] Removing photos below min turns the count red and disables Generate; tapping it shows the toast 「Please upload at least %d photos」 (「Please upload at least 5 photos」).
- R-070 [PM:confirm] With too few credits a free user gets the paywall; a subscribed user gets 「More Credits Required」, which leads to the Credit Shop.
- R-071 [PM:confirm] Generate charges the credits on the button (balance drops by 60 for 「Top 5 of My Year」).
- R-072 [PM:confirm] 「‹」 on the confirm page goes back (to the picker; no arrow drawn, Q-8).

## Text language (Creative only)
- R-073 [PM:text-language; DS:ds-light] The default is the device language: its row is highlighted with 「Device Language」 beside the name and a ✓ (Design; the PM wrote 「(Device language)」).
- R-074 [PM:text-language; DS:ds-light] The list is a bottom sheet (handle, page dimmed behind) listing each language in its own script with its English name: 「English」, 「繁體中文 Chinese (Traditional)」, 「简体中文 Chinese (Simplified)」, 「日本語 Japanese」, 「한국어 Korean」, 「Español Spanish」, 「Français French」, 「Deutsch German」 (Design); it holds every language PhD supports, the same list on iOS and Android, and scrolls (PM, which also lists 「Português」, 「Italiano」, 「ภาษาไทย」 …; Q-32).
- R-075 [PM:text-language] The chosen language code is passed to the engine: the reel's text comes out in that language (Opus 5.5 pipeline supports them all).
- R-076 [PM:text-language] The choice is kept within the session and reset when the room is left.
- R-077 [PM:text-language] Text in the generated reel cannot be edited afterwards.
- R-127 [DS:ds-light] The Text Language sheet closes without a change when the dimmed page is tapped or the handle dragged down (the Design draws a handle and a dimmed page; not stated, Q-32).

## Generation and My AI Artwork
- R-078 [PM:artwork; DS:ds-light] After Generate the app shows My AI Artwork on the 「Reel Creator」 tab with the new item: a grey tile 「Processing...」, its date and template name, and a time estimate (「9 minutes remaining ...」) with a progress bar (Design; the PM drew 「Processing…」 and 「3 minutes remaining…」).
- R-079 [PM:artwork] Results of all three features go to the (former Cinematic Reel Creator) Artwork page.
- R-080 [PM:artwork; DS:ds-light] The Artwork tab is named 「Reel Creator」, second after 「Image to Video」, followed by the app's other feature tabs in a scrolling row (Design: 「AI Face Swap」, 「AI …」; the PM drew 「Character Motion Swap」).
- R-081 [PM:artwork] The tab has no sub tabs and no feature split; items are sorted by time (newest first), each showing its date and template name.
- R-082 [PM:artwork; DS:ds-light] 「Create more」 returns to the Reel Creator room (Design wording; the PM wrote 「Create More」).
- R-083 [PM:artwork] The finished item can be opened and plays the 9:16 reel (R-023).
- R-128 [DS:ds-light] My AI Artwork shows 「‹」, the title 「My AI Artwork」 and an ⓘ at the top right; what ⓘ opens is not stated (Q-33).
- R-129 [DS:ds-light] 「Select」 at the top right of the list switches the list to selection (what it then offers is not stated, Q-33).
- R-130 [DS:ds-light] When the estimate has run out before the job ends, the processing card shows 「Almost done」 in place of the remaining time.
- R-131 [DS:ds-light] A finished card shows the result's thumbnail, its date, the template name and 「Expires on {date}」 (how long results are kept is not stated, Q-33).
- R-132 [DS:ds-light] A job whose upload was interrupted shows a ⚠ tile and 「Resume to Upload」; tapping it resumes the job, which then charges no second time (Design; answers part of Q-12).

## Cinematic Styles (CineStory, 1 photo)
- R-084 [PM:cinematic] Cinematic Styles follows the same flow: Preview → Use Template → single-photo picker 「Select 1 photo」 → confirm page → 「Generate | 40」.
- R-085 [PM:cinematic; DS:ds-light] The Cinematic confirm page shows 「1 Photo」 and 「9:16」 in the header (Design format), 「Your photos (1/1)」 and 「Tap the photo to replace」 (PM); tapping the photo replaces it.
- R-086 [PM:cinematic] The Cinematic confirm page has no Text Language (PM; the Design's one confirm frame pairs the sample name 「Micro Cinema」 with 7/15 photos and Text Language, read as sample content, Q-35).

## AI Transition (Cool Transitions)
- R-087 [PM:room, PM:confirm] An AI Transition template's picker needs exactly its fixed count (4 or 6): 「Select 4 photos」 / 「Select 6 photos」, Next only at that count.
- R-088 [PM:confirm] The AI Transition confirm page has no Text language and its Generate charges the price shown (price not drawn, Q-9).

## Dark theme
- R-133 [DS:ds-dark] Every screen of the flow (room, Preview, picker, Import prompt, confirm page, Text Language sheet, My AI Artwork) has a dark version with the same content and controls, legible on the dark background (Design ds-dark). What turns it on is not stated (Q-34, assumption: the phone's dark theme).

## Android
- R-089 [Rule: Android system Back, REQ-051] System Back on every screen and sheet of the feature behaves as its own 「‹」 / 「×」 / 「Got it」, closes the keyboard or dropdown first, or (where the spec gives no exit) is recorded (Q-8).

## PHD domain knowledge (standing input 6, REQ-004)
- R-102 [KB: KP-017] After a Generate of each feature (Creative, Cinematic Styles, AI Transition) ends, Buy Credit › 「Detail」 lists the use with the right feature name and the credits actually deducted, and any refund with its amount.
- R-103 [KB: KP-019] Once the first Generate tap is accepted, further taps are blocked: a burst of taps charges once and makes one result.
- R-104 [KB: KP-029] A finished reel job (a long video job, as Cinematic Reel Creator) sends a completion notification with a title and message whose tap opens the right page (the result in My AI Artwork). The spec is silent (Q-12).
- R-105 [KB: KP-049] Localised strings that carry numbers (tray 「Select {min}–{max} photos」 and 「({n} more)」, the Import prompt N, the toast 「Please upload at least %d photos」) show the right numbers in every app language and never crash the screen.
- R-106 [KB: KP-050, KP-048] In an RTL app language (Arabic) the room, Preview, picker, confirm page and Text language list mirror their layout and stay in bounds; Western digits are acceptable.
- R-107 [KB: KP-101] Long translations (e.g. German, Portuguese) on the picker tray, Import prompt and confirm page stay readable and every button stays reachable.
- R-108 [KB: KP-072] Every entry to the room (Effects button, Launcher Shortcut, Launcher Template row, AI Video page, My AI Artwork 「Create More」) opens it, and its 「‹」 returns to the page of that entry.
- R-109 [PM:room; KB: KP-032] The photo saved automatically on the Edit Room jump is the current edited image, not the original file.
- R-110 [KB: KP-074] A template deeplink opened while the app is already running (warm start) opens the same Preview as from a cold start, without a crash before the template data has loaded.
- R-111 [KB: KP-091] The Preview's mute state stays when swiping to another template.
- R-112 [KB: KP-097] After Activity re-creation (Don't keep activities) the confirm page keeps its photos, order, count and Text language.
- R-113 [KB: KP-083] After 「Create More」 from My AI Artwork, a new generation from the room runs normally and Back from the room works (no stale resource).

### Domain rules
Cited above: KP-020, KP-026, KP-017, KP-019, KP-029, KP-049, KP-050, KP-048, KP-101, KP-072, KP-032, KP-074, KP-091,
KP-097, KP-083. The rest, carried over from update-plan.md › Not added (REQ-004; K ids are the entries' `aka`, moved
from `library/phd/domain/` to `library/phd/knowledge/` on 2026-11-05):
- KP-012 (K36b) → n/a as a row (noted on TC-073).
- KP-014 (K36c), KP-025 (K47b) → n/a (the feature has no AI Exposure).
- KP-016 (K31) → n/a (no free trial in this flow).
- KP-021 (K44), KP-039 (K42) → n/a (no AI Agent in this flow).
- KP-024 (K47a) → n/a (images only; Reel Creator outputs are videos, R-079 covers Artwork).
- KP-028 (K46) → n/a (a filter rule; the Reel Creator tab is a feature tab, not a filter).
- KP-030 (K50) → n/a (no editing in this flow).
- KP-033 (K04) → n/a as a row (noted on TC-015).
- KP-034 (K05) → n/a (the Discover tip bubble is not in this flow; K05's warm-start risk is KP-074, R-110).
- KP-035 (K08), KP-036 (K11), KP-037 (K12), KP-038 (K14) → n/a (no prompt or reference inputs in this flow).
- KP-040 (K20), KP-041 (K21), KP-042 (K22), KP-046 (K27), KP-047 (K29) → n/a (no edit tools in this flow).
- KP-043 (K24), KP-044 (K25), KP-045 (K26) → n/a (no Video Editing in this flow).
- KP-015 (K36e) → n/a (Mine entitlement after buying Premium: not in this flow). KP-018 (K36d) → n/a (Credit Auto
  Pass naming: no Auto Pass in this flow). KP-027 (K47c) → Q-26 (spec silent on Recent). KP-134 → n/a (Adjustment room Undo: no editing in this flow). Decided 2026-11-17 (REQ-009).

## Flow arrows
- R-090 [PM:room flow arrow room-a1 ] Room template card → Preview. Walked by: TC-023.
- R-091 [PM:preview flow arrow preview-a1 ] Preview 「View photo tips」 → Photo tips sheet. Walked by: TC-033.
- R-092 [PM:preview flow arrow preview-a2 ] Preview 「Use Template」 → picker. Walked by: TC-037.
- R-093 [PM:picker flow arrow picker-a1 ] Picker entered again in the session → Import prompt. Walked by: TC-054.
- R-094 [PM:picker flow arrow picker-a2 ] 「Import」 → picker with the photos selected and the red tray. Walked by: TC-057.
- R-095 [PM:picker flow arrow picker-a3 ] Picker 「Next」 (in range) → confirm page. Walked by: TC-053.
- R-096 [PM:confirm flow arrow confirm-a1 ] Remove below min → Generate disabled and toast. Walked by: TC-066, TC-067.
- R-097 [PM:text-language flow arrow text-language-a1 ] 「Generate」 → My AI Artwork Processing card. Walked by: TC-085.
- R-098 [PM:artwork flow arrow artwork-a1 ] 「Create More」 → room. Walked by: TC-091.
- R-099 [PM:cinematic flow arrow cinematic-a1 ] Cinematic 「Use Template」 → 「Select 1 photo」 picker. Walked by: TC-092.
- R-100 [PM:cinematic flow arrow cinematic-a2 ] Cinematic 「Next」 → Cinematic confirm page. Walked by: TC-094.

Since the Figma catch-up each arrow carries its Figma node id in `arrows.json` (room-a1 7252-463, preview-a1 7337-1142, preview-a2 7337-1195, picker-a1 7337-1197, picker-a2 7337-1199, picker-a3 7337-1201, confirm-a1 7337-1203, text-language-a1 7271-490, cinematic-a1 7337-1205, cinematic-a2 7337-1207); the intro page draws no arrow.

## Open questions
- Q-1 Section order in the room is pending (Meg and CMS: can CineStory move to the new CMS type). R-009.
- Q-2 Creative feature_id pending (leaning to CineStory's; Meg, early November; fallback CineStory feature_id with action_id vendor Opus 5.5). R-024.
- Q-3 Answered by the PM Figma (2026-11-17, REQ-009): 「上次選的圖」 = the set last applied with Next. R-115.
- Q-4 Answered by the PM Figma (2026-11-17, REQ-009): 「記憶只在 Reel Creator 內」. R-116.
- Q-5 After closing the prompt with 「×」, does it come back on the next picker entry in the same session? R-052.
- Q-6 The language menu moving from the Preview to the confirm page is still to be confirmed. R-067.
- Q-7 Answered by the PM Figma (2026-11-17, REQ-009): 「圖片 input >1 的 template 再 show」, so the Cinematic picker shows no prompt. R-117. (The Cinematic note box still carries the old 待確認 line; the memory note is the newer rule.)
- Q-8 Back paths (Preview, picker, confirm 「‹」 and Android system Back) are drawn as buttons but no arrow says where they go; rows record the result.
- Q-9 Credit prices: only 「Generate | 60」 (Top 5 of My Year) and 「Generate | 40」 (Micro Cinema) are drawn. Per-template Creative prices and AI Transition prices are not stated.
- Q-10 Answered (2026-11-17): the PM Figma was compared with the PDF (REQ-009; intro page R-118 – R-122, memory clauses R-114 – R-117) and the Design Figma read (REQ-011; R-123 – R-133 and the Design-first changes).
- Q-11 Picker: how a pick past max is refused, whether numbers renumber after an unpick, and how a failed check (size, NSFW, celebrity) is marked and worded are not drawn. R-045, R-047, R-048.
- Q-12 Generation failure (copy, refund) and leaving during processing are not stated; the Design's Artwork page answers the interrupted-upload case (⚠, 「Resume to Upload」, R-132). The done notice is not in the spec either; rows follow domain K48 (R-104).
- Q-13 The Edit Room jump dialog copy and buttons are 「as I2V」 but not drawn. R-010, R-011.
- Q-14 Answered (user, 2026-11-03, REQ-003): the spec does not say where the credit button and History button lead; PHD domain knowledge K75 (Buy Credit) and K76 (My AI Artwork on the feature's tab) does. R-008, R-101.
- Q-15 The deeplink URLs (old Cinematic Reel Creator link, parameter names) must come from RD. R-013 – R-019.
- Q-16 Does the 「+」 tile on the confirm page stay when the count is at max? Not drawn. R-064.
- Q-17 Does the Import prompt's N count only photos still in the gallery? R-056.
- Q-18 The processing card in the mockup shows the template's art; PHD domain K48 (PHA262026-0375) says long-task processing tiles show the source photo's thumbnail. Which one is expected? R-078.
- Q-19 Template names, descriptions and photo tips come from the CMS: are they localised per app language, and do they refresh after a language switch (domain open question, PHA262026-0342 / -0243)? R-020, R-038.
- Q-20 Does 「Create More」 keep anything (template, photos, Text language), or open a clean room? Domain lists 「Create More keeps inputs」 as an open question (PHA262026-0390, -0413). R-082.
- Q-21 The board title says the spec follows the ledger 「spec-draft/reel-creator.decisions.md」, which was not supplied. Please send it (or access): decisions in it may settle Q-1 – Q-7 or add rules. (Found by the rdqe comparison, 2026-11-03, REQ-006.)
- Q-23 Answered (user, 2026-11-17, REQ-011): access to the Design file was granted to qa-dm; read 2026-11-17 (groups d1, d2). R-123 – R-133 and the rows marked 「Design first」.
- Q-24 When does the intro page show? Assumption: on every room entry until 「Don’t show again」 is ticked and 「Try Now」 tapped (as today's Cinematic Reel Creator intro); also unknown whether a template deeplink (R-015) shows it first. R-118, R-120, R-121, TC-128 – TC-130.
- Q-25 The memory ends when the room is left (R-114): does opening My AI Artwork (History button, or Generate) count as leaving? Assumption: no, only leaving the room with 「‹」 / Back; TC-134 records it. R-051, R-114.
- Q-26 Should Reel Creator results appear in the Launcher's Recent (domain KP-027: new features' works reach Recent when they are meant to)? The spec is silent; no row. R-079.
- Q-27 The Design draws a one-photo Import prompt 「Use the photo you picked last time?」 (and 2- and 3-photo ones), while the PM says the prompt is not shown when only 1 photo was picked last time (R-057). On a template with photo input > 1 a set of 1 – 3 is reachable only when remembered photos were deleted from the Gallery. Assumption: the Design cards show with the photos still in the Gallery (1, 2 or 3); R-057 holds for a set applied with 1 photo. R-057, R-126, TC-137 – TC-139.
- Q-28 The Design replaces the Preview's 「View photo tips」 text with an ⓘ icon next to 「‹」 and draws no tips sheet. Assumption: ⓘ opens the photo tips sheet the PM describes. R-029, R-036, TC-024, TC-033, TC-035.
- Q-29 Picker: what does each photo's expand icon open (assumption: a full-size view, closed by Back or 「‹」, the photo not picked)? And the Design draws a tooltip 「Upload at leat 2 photos」 (typo 「leat」, and 2 does not match the 5–10 drawn) over the grid: when does it show and what is its wording? No row tests the tooltip until answered. R-123, TC-135, TC-150.
- Q-30 Picking fewer than min by hand: the Design draws only the empty picker (grey 「Next」, plain tray text), the PM the red 「Select at least {min} photos ({n} more)」 after an Import. Assumption: the red line shows after a manual pick below min too. R-043, TC-038.
- Q-31 Confirm page header: the Design shows 「9:16」 with a ratio icon on 04-1 (light, with the language sheet) but not on 04 or the dark frames, and shows the template's count 「1 Photo」 where the PM wrote 「5–15 photos · output 9:16」. Assumption: the header shows the count as on the Preview and 「9:16」. R-060, TC-063, TC-094.
- Q-32 Text Language: the Design's sheet shows 8 languages ending at 「Deutsch German」; the PM lists every PhD language (also Português, Italiano, ภาษาไทย …). Assumption: the full PhD list, scrolling, in the Design's format. How the sheet closes without a choice (dimmed page, handle) is not stated. R-074, R-127, TC-075, TC-077, TC-140.
- Q-33 My AI Artwork: the Design draws the generic Artwork page (ⓘ, 「Select」, 「Expires on」, 「Resume to Upload」, sample 「Image to Video - A Template Name 2」). What do ⓘ and 「Select」 offer on the Reel Creator tab, and how long are results kept? Rows record them. R-128, R-129, R-131, TC-142, TC-144, TC-145.
- Q-34 The Design draws every screen in light and dark. What turns dark on (the phone's dark theme, an app setting)? Assumption: the phone's dark theme; switching it needs the user's go-ahead on the QA phone. R-133, TC-146 – TC-149.
- Q-35 The Design's only confirm frame pairs 「Micro Cinema」 「1 Photo」 (a Cinematic template) with 7/15 photos, the 「+」 tile and Text Language. Assumption: sample content; the Cinematic confirm page stays as the PM draws it (1/1, Tap the photo to replace, no Text Language). R-085, R-086, TC-094.
- Q-36 Count wording: the Design writes 「1 Photo」 (capital P, image icon) and 「Select 5 to 10 photos to continue.」; the PM 「5–15 photos」, 「1 photo」 and, for min = max, 「Select N photos」. The Design draws no range count on the Preview and no min = max tray. Assumption: Design wording where drawn, PM wording elsewhere. R-031, R-042, R-044, TC-030, TC-092, TC-098.
- Q-22 Is 「≤ 10 MB」 10,000,000 bytes or 10 MiB (10,485,760 bytes)? Rows avoid the gap between the two (TC-048, TC-126); a photo inside it is untested until PM answers. R-045.

## Added 2026-11-02 — coverage passes and standing inputs

### Job states
| Job | Start / loading | Success | Failure | Retry | Leave and return | Longest wait | Done notice |
|---|---|---|---|---|---|---|---|
| Photo check on pick (size, NSFW, celebrity) | n/a (spec silent: checked when picked) | TC-046 | TC-045, TC-047, TC-048, TC-049, TC-050 | n/a (spec silent) | n/a (spec silent) | n/a (spec silent) | n/a (no notice) |
| Creative generation | TC-085, TC-117 | TC-086, TC-087, TC-118, TC-142 | TC-143 (upload interrupted: ⚠ 「Resume to Upload」) | TC-143 (「Resume to Upload」) | TC-088, TC-116 | TC-085 (「… minutes remaining ...」 shown), TC-141 (「Almost done」) | TC-121 |
| Cinematic Styles generation | TC-096 | TC-090, TC-119, TC-122 | n/a (spec silent, Q-12) | n/a (spec silent, Q-12) | n/a (same Artwork card as TC-088) | n/a (spec silent) | n/a (spec silent, Q-12) |
| AI Transition generation | TC-101 | TC-101, TC-120 | n/a (spec silent, Q-12) | n/a (spec silent, Q-12) | n/a (same Artwork card as TC-088) | n/a (spec silent) | n/a (spec silent, Q-12) |

### Error classes
| Job | Error classes |
|---|---|
| All jobs | n/a (the spec names no error classes or failure copy) |

### Exit × stage
| Stage | ‹ / × / Got it | System Back |
|---|---|---|
| Intro page | TC-131 | TC-132 |
| Room | TC-009 | TC-103 |
| Preview | TC-031, TC-020 | TC-104 |
| Photo tips sheet | TC-034, TC-036 | TC-105 |
| Picker | TC-052 | TC-106 |
| Full photo view (expand icon) | TC-135 | TC-150 |
| Picker with Import prompt | TC-056 | TC-107 |
| Confirm page | TC-071 | TC-108; Activity re-created: TC-116 |
| Text Language sheet | TC-078 (closed by choosing), TC-140 (dimmed page, handle) | TC-109 |
| Edit Room jump dialog | TC-011 | TC-110 |
| My AI Artwork | TC-088 | TC-111 |

### System back
- Reel Creator intro page → as 「‹」: TC-132
- Reel Creator room → leaves the room: TC-103
- Preview → room: TC-104
- Photo tips sheet → closes as 「Got it」: TC-105
- Picker → Preview: TC-106; with the Import prompt shown: TC-107
- Full photo view (picker expand icon) → back to the picker, picks unchanged: TC-150
- Confirm page → picker: TC-108
- Text Language sheet → closes, language unchanged: TC-109
- Edit Room jump dialog → as cancel: TC-110
- Paywall / More Credits Required / Credit Shop → n/a (existing pages outside this spec)
- My AI Artwork → recorded: TC-111

### Hidden clauses
| Requirement | Hidden clause | Observed through | Rows |
|---|---|---|---|
| R-010 | the Edit Room photo is saved automatically on the jump | Gallery photo count before and after the jump | TC-012 |
| R-109 | the saved photo carries the Edit Room edit | the photo saved to the Gallery, compared with the original | TC-012 |
| R-102 | the credit use is recorded with its feature name and amount | Buy Credit › Detail after each Generate | TC-118, TC-119, TC-120 |
| R-103 | a burst of taps is charged once | credit balance and the number of new Artwork cards | TC-117 |
| R-105 | the %d / {n} placeholders are filled in every language | the numbers on the tray, prompt and toast in zh-Hant and ja | TC-123 |
| R-012 | the room opens without the photo | picker of each feature shows 0 picked | TC-013 |
| R-056 | photos no longer in the gallery are not imported | imported count after deleting 2 photos from the Gallery | TC-059 |
| R-065 | AI Transition output order = page order | order of the photos in the finished video | TC-101 |
| R-066 | every input photo is used in a Creative reel | each input photo seen in the finished reel | TC-087 |
| R-069 | below min nothing is generated or charged | credit balance and My AI Artwork after tapping the disabled Generate | TC-067 |
| R-071 | Generate charges the credits on the button | credit balance before and after | TC-074, TC-096, TC-101 |
| R-075 | the chosen language code is passed to the engine | language of the text in the finished reel | TC-081, TC-082, TC-083 |
| R-114 | leaving the room clears the memory | no Import prompt after leaving and re-entering the room | TC-134 |
| R-115 | the remembered set is the one applied with Next | the N in the prompt after a pick changed without Next | TC-133 |
| R-120 | the 「Don’t show again」 choice is stored | intro page absent on re-entry and after relaunch | TC-130 |
| R-132 | a resumed upload charges no second time | credit balance before Generate and after the resumed job | TC-143 |
| R-126 | N counts only the remembered photos still in the Gallery | the N and thumbnails after deleting remembered photos | TC-137, TC-138, TC-139 |

### Variants
| Requirement | Variant | Rows |
|---|---|---|
| R-074 | English (device language, default) | TC-075, TC-083 |
| R-074 | 繁體中文 | TC-076, TC-082 |
| R-074 | 日本語 | TC-078, TC-081 |
| R-074 | rest of the list (scrolled) | TC-077 |
| R-075 | English | TC-083 |
| R-075 | 繁體中文 | TC-082 |
| R-075 | 日本語 | TC-081 |
| R-070 | free user (paywall) | TC-072 |
| R-070 | subscribed user (More Credits Required) | TC-073 |
| R-084 | Creative (60 credits, Text language) | TC-063, TC-074 |
| R-084 | Cinematic Styles (40 credits, 1 photo) | TC-094, TC-096 |
| R-084 | AI Transition (fixed 4 / 6, no Text language) | TC-100, TC-101 |
| R-021 | 4 photos | TC-098, TC-099 |
| R-021 | 6 photos | TC-102 |
| R-102 | Creative | TC-118 |
| R-102 | Cinematic Styles | TC-119 |
| R-102 | AI Transition | TC-120 |
| R-105 | 繁體中文 | TC-123 |
| R-105 | 日本語 | TC-123 |
| R-023 | Creative | TC-086 |
| R-023 | Cinematic Styles | TC-127 |
| R-023 | AI Transition | TC-101 |
| R-016 | CineStory GUID | TC-017 |
| R-120 | ticked (not shown again) | TC-130 |
| R-121 | not ticked (shown again) | TC-129 |
| R-017 | Creative GUID | TC-015 |
| R-017 | AI Transition GUID | TC-016 |
| R-126 | more than 3 remembered (3 thumbnails, 「+N−3」) | TC-054 |
| R-126 | 3 remembered | TC-137 |
| R-126 | 2 remembered | TC-138 |
| R-126 | 1 remembered (「Use the photo …」) | TC-139 |
| R-133 | light theme | TC-005, TC-024, TC-037, TC-054, TC-063, TC-075, TC-085 |
| R-133 | dark theme | TC-146, TC-147, TC-148, TC-149 |

### Annotation trace (manual, PDF-only)
No `boards/` OCR on this Windows machine, so `annotations.ts` cannot run; every bullet of the PDF note boxes was traced by hand:
- room (board title): 「spec 依帳本 spec-draft/reel-creator.decisions.md」 → Q-21 (linked file not supplied; added 2026-11-03, REQ-006).
- room: 房間改名 → R-001 – R-005; 不分 tab / 三個 feature 混排 → R-006, R-007; 待決 section 排序 → Q-1; 從 Edit Room 進入 → R-010 – R-012; CMS fields → R-020; min / max → R-021, R-022; 輸出 9:16 → R-023; 待決 feature_id → Q-2, R-024; Cinematic Styles 沿用 CineStory CMS type → Q-1 (label: CMS setup); 時程 → R-025.
- deeplink: R-013 – R-019, Q-15.
- preview: R-026 – R-034; red lines 上下刷範圍 → R-028, 文字疊在 demo 上 → R-032, 手指動畫 → R-033.
- tips: R-036 – R-039.
- picker: R-041 – R-046; memory R-051 – R-058; 待確認 → Q-3, Q-4, Q-5.
- confirm: R-060 – R-071; 待確認 語言選單 → Q-6.
- text-language: R-073 – R-077.
- artwork: R-078 – R-082 (RD 注意 tab rename → R-080).
- cinematic: R-084 – R-086; 待確認 Import → Q-7 (answered by the memory note, R-117).
- Figma-only texts (2026-11-17, group p1): memory note 「圖片input >1 的 template 再 show」 → R-117; 「「上次選的圖」= 上次按 Next (apply 的那組)」 → R-115; 「記憶只在 Reel Creator 內」 → R-116 (red 待確認 in the PDF); 「離開房間 = 離開 session, 記憶清除」 → R-114, R-051. tutorial: 「【 Demo video 調整】 • 文案同左」 → R-118; mockup 「Reel Creator」 / 「Turn photos into …」 / 「Try Now」 / 「Don’t show again」 → R-118 – R-121 (ui).

- Design (2026-11-17, groups d1 / d2): the Design boards carry no notes, only screen text, traced to R-006 – R-008, R-029, R-031, R-033, R-035, R-036, R-041 – R-043, R-049, R-052, R-060, R-061, R-064, R-067, R-068, R-073, R-074, R-078, R-080, R-082, R-085, R-123 – R-133 (ui); the tooltip 「Upload at leat 2 photos」 → Q-29; sample texts (「Micro Cinema」 on the confirm page, 「Image to Video - A Template Name 2」, 「10 Outfits」 on Artwork cards) → label. ds-pm-copy (933:4752) → older: PM page 7238:8623 (its 待確認 lines are answered there, R-114 – R-117; it has no intro page).

### Controls (PDF-read) → rows
Room: ‹ TC-009 · credit button TC-008 · History button TC-112 · template card TC-023 · section row swipe TC-007. Preview: ‹ TC-031 · View photo tips TC-033 · mute TC-025 · Use Template TC-037 · swipe TC-026. Tips: Got it TC-034. Picker: ‹ TC-052 · Recents ▾ TC-051 · photo cell TC-038 / TC-043 · Next TC-053 · tray thumbnails TC-041 · Import TC-055 · prompt × TC-056. Confirm: ‹ TC-071 · photo × TC-065 · long-press drag TC-064 · + tile TC-068 · Text language ▾ TC-075 · language item TC-078 · Generate TC-074 / TC-067. Cinematic confirm: photo tap TC-095. Artwork: tabs TC-089 · card TC-086 · Create More TC-091. Intro page: Try Now TC-129 · Don’t show again TC-130 · ‹ TC-131. No inputs with a keyboard. Since 2026-11-17 the Figma inventory (`inventory.json`; buttons the PM mockups draw as plain frames added by hand in `inventory-overrides.json`) is traced in `control-trace.json`, the Design controls (ds-light, ds-dark; image cards, grid photos, tabs and 「Select」 added by hand) included; the controls of the superseded PM copy (ds-pm-copy) are traced n/a.

### Request ledger coverage
| Ledger entry | Requirements |
|---|---|
| REQ-001 | R-001 – R-101 (this table) |
| REQ-003 | R-008, R-101 |
| REQ-004 | R-102 – R-113 |
| REQ-006 | R-023, R-045 (Q-21, Q-22) |
| REQ-009 | R-051, R-114 – R-122 (Q-23 – Q-26) |
| REQ-010 | Android table only (no iOS table); Design analysed after access (REQ-011) |
| REQ-011 | R-006 – R-008, R-029 – R-037, R-041 – R-044, R-049, R-052, R-060 – R-068, R-073, R-074, R-078, R-080, R-082, R-085, R-086, R-123 – R-133 (Q-23 answered; Q-27 – Q-36) |
