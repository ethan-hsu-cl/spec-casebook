# Reel Creator / Creative Reel (Android) — eBug drafts, round R1 (table v4), PhotoDirector 20.19.0 build 90201901

**Source:** spec-casebook run `library/phd/creative-reel/android/runs/2026-11-17-r1/` — phase R1 of draft `drafts/20261117-150251` (table v4, 150 cases), 2026-11-18 08:48 → 15:45, TC-001 – TC-007 on Google Pixel 8a / Android 16, the rest on Samsung Galaxy S23 (SM-S9110) / Android 16, Appium / UiAutomator2, Test Server, Free. Tally: 16 Blocked, 42 Fail, 2 Not run, 90 Pass. TC-072 / TC-073 (R1-h) are Not run yet.

**Status:** nothing filed, uploaded or commented. TR261113-0038 (build 20.19.0.v202611132003, R4) names the build tested (versionCode 90201901). ECL product 「PhotoDirector Mobile for Android」. Creator WILLY_WU, [AIAgent], API — from the batch-editing batch on the same TR (no filed batch for this feature yet): confirm.

Rules: reviewer rules 2026-10-21 — one action per Repro step, a Spec Link on every entry (URL on its own line), at least one image per entry, the logcat excerpt on every failure / charge entry, no video. PM decisions are filed to PM (UX → `[AIAgent][UX]`, text `[AIAgent][UI]`, behaviour Functional); text and layout `[AIAgent][UI]`, RD when the Design / PM states it; the rest `[AIAgent]` Functional, RD. Spec basis per entry against PM page 7238:8623 (section spec) and Design page 933:4528 (section Design 976:11727); domain rules (KP-…) named as such. Creative rows ran on stand-in templates (no 「Top 5 of My Year」 on Test Server, ISS-CR-06).

**What is drafted:** 29 new entries (ISS-CR-01…29), of which 6 ask PM for a decision. Dedupe per OS: see dedupe.txt.

Legend — Class: Functional / UI / UX · Severity: S1 critical and blocking only, S2 important, S3 moderate, S4 minor · Owner: RD / PM.

---

## 1. ISS-CR-01 — Launcher shortcut and AI Videos card still read 「Cinematic Reel Creator」  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-002, TC-004  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-003 / R-005 (PM room board: the room formerly Cinematic Reel Creator is renamed 「Reel Creator」, incl. the Launcher Shortcut and the AI Video page entry). The Effects button already reads 「Reel Creator」 (TC-001 Pass). Seen on the Pixel 8a (TC-002 / TC-004) and again on the S23 (TC-113 entries 1–2). Localised shortcut names differ per language (zh-Hant 「AI電影感運鏡」, de 「Reel-Creator」; O-9).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] Reel_Creator: Launcher shortcut and AI Videos card still read 「Cinematic Reel Creator」
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Read the room's shortcut label
4. Tap the AI Videos tab
5. Read the room's card label
6. Check the result

Result:
The shortcut and the AI Videos card both read 「Cinematic Reel Creator」.
摘要：Launcher 捷徑與 AI Videos 卡片仍顯示舊名 Cinematic Reel Creator。
{20.19.0_cr01_launcher_shortcut.jpg} {20.19.0_cr01_ai_videos_card.jpg}

Expect Result:
Both entries read 「Reel Creator」 (the room is renamed).
摘要：兩個入口都應顯示「Reel Creator」。

Note:
Device: Google Pixel 8a / Android 16 and Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), Reel Creator room frame (rename notes, room board) -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7245-8672
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/01_ISS-CR-01/`

---

## 2. ISS-CR-02 — Reel Creator room has no 「Reel Creator」 title  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-005  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-001 (PM room frame titles the room 「Reel Creator」). The top bar has 「‹」, the credit pill and the history icon (R-008 OK) but no title text anywhere on the page. Pixel 8a (TC-005) and S23 (TC-113 room screenshots).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] Reel_Creator: Room shows no 「Reel Creator」 title in its top bar
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Tap Cinematic Reel Creator
4. Read the top bar
5. Check the result

Result:
The top bar shows 「‹」, the credit pill and the history icon, with no title.
摘要：房間上方沒有標題 Reel Creator。
{20.19.0_cr02_room_no_title.jpg}

Expect Result:
The room is titled 「Reel Creator」.
摘要：房間應有標題「Reel Creator」。

Note:
Device: Google Pixel 8a / Android 16 and Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), Reel Creator room frame (rename notes, room board) -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7245-8672
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/02_ISS-CR-02/`

---

## 3. ISS-CR-03 — Room section titles are raw string keys  ·  Class: UI  ·  Severity: S2  ·  Owner: RD

**Report step:** TC-006  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-006 (Design 01_Template_List: 「Cinematic Styles 🎬」, 「Year-End Recap 🎉」, 「Cool Transition 🎞️」; the PM drew 「Year-End Recap 📅」 / 「Cool Transitions 🤳🏻」; titles are CMS category names). The app shows 「ReelCreator_Category_Cinestory」, 「ReelCreator_Category_CreativeR」, 「ReelCreator_Category_AITransit」 — string keys that were never resolved. The missing Year-End Recap section is ISS-CR-06 (PM). Pixel 8a and S23; the keys also stay in zh-Hant / ja / de / pt (TC-123).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] Reel_Creator: Room section titles show raw keys 「ReelCreator_Category_…」
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Tap Cinematic Reel Creator
4. Scroll the room to the bottom
5. Check the result

Result:
The section titles read 「ReelCreator_Category_Cinestory」, 「…_CreativeR」 and 「…_AITransit」.
摘要：三個區塊標題顯示未轉換的字串 key。
{20.19.0_cr03_raw_section_keys.jpg} {20.19.0_cr03_room_bottom.jpg}

Expect Result:
Category names: 「Cinematic Styles 🎬」, 「Year-End Recap 🎉」, 「Cool Transition 🎞️」 (Design).
摘要：區塊標題應顯示分類名稱（如 Cinematic Styles）。

Note:
Device: Google Pixel 8a / Android 16 and Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator Design Figma (page 261109_AI_transition_feature, section Design), 01_Template_List frame -
https://www.figma.com/design/qdzVXIFZeYwcsa6fipmcLH/Cinematic-Reel-Creator--CineStory-?node-id=934-622
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), Reel Creator room frame (rename notes, room board) -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7245-8672
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/03_ISS-CR-03/`

---

## 4. ISS-CR-04 — Cinematic Styles cards carry no inset photo  ·  Class: UI  ·  Severity: S4  ·  Owner: RD

**Report step:** TC-007  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-007 (Design 01_Template_List draws a small inset photo at the bottom left of each Cinematic Styles card; Design-only, the PM room frame does not draw it). The cards are plain full-card thumbnails (One-Take Shot's is black). AI Transition cards show grey placeholders (CMS thumbnails; not filed, TC-029 recorded it).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] Reel_Creator: Room: Cinematic Styles cards have no inset photo
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Tap Cinematic Reel Creator
4. Swipe the first section left
5. Check the result

Result:
The Cinematic Styles cards are plain thumbnails with no inset photo.
摘要：Cinematic Styles 卡片左下沒有小圖。
{20.19.0_cr04_cine_cards_no_inset.jpg} {20.19.0_cr04_cine_row_left.jpg}

Expect Result:
Each Cinematic Styles card carries a small inset photo at its bottom left (Design).
摘要：卡片左下應有小張示意照片（Design）。

Note:
Device: Google Pixel 8a / Android 16 and Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator Design Figma (page 261109_AI_transition_feature, section Design), 01_Template_List frame -
https://www.figma.com/design/qdzVXIFZeYwcsa6fipmcLH/Cinematic-Reel-Creator--CineStory-?node-id=934-622
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/04_ISS-CR-04/`

---

## 5. ISS-CR-05 — PM: no Reel Creator template row on the Launcher  ·  Class: Functional  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-003, TC-113  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-004 / R-108 (PM room board: the Launcher Template row of the room is labelled 「Reel Creator」, one of five entries). On Test Server the Launcher's template rows are New Hair Colors, Your Best Look Yet, Meme Generator, Cute Pet Moments, ID Photo, Minimalist Collage: no Reel Creator row, so its title and the fifth entry (TC-113) cannot be checked. Whether the row is CMS-scheduled for this server is not stated: filed to PM to confirm (2026-11-11 rule).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] Reel_Creator: No Reel Creator template row on the Launcher — PM to confirm
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Scroll the Launcher to the bottom
3. Check the result

Result:
No 「Reel Creator」 (or 「Cinematic Reel Creator」) template row on the Launcher.
摘要：Launcher 沒有 Reel Creator 的模板列。
{20.19.0_cr05_launcher_rows_mid.jpg} {20.19.0_cr05_launcher_rows_bottom.jpg}

Expect Result:
PM to confirm whether the Launcher shows a 「Reel Creator」 template row on this build, or when.
摘要：請 PM 確認 Launcher 是否應有「Reel Creator」模板列及上線時間。

Note:
Device: Google Pixel 8a / Android 16 and Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), Reel Creator room frame (rename notes, room board) -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7245-8672
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/05_ISS-CR-05/`

---

## 6. ISS-CR-06 — PM: no Year-End Recap section; Creative templates are bare test entries  ·  Class: Functional  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-023, TC-026  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-006 / R-020 / R-026 / R-027 (PM room and Preview frames: a Year-End Recap section with 「Top 5 of My Year」; every template carries its DisplayName, description, demo and tips). Test Server lists two Creative templates only, 「single-color-fastcut」 and 「cinematic-grade」: raw names, no description (TC-024), and both play the same demo (「MY YEAR QUEST 我的年度冒險」) so the swipe shows no template of its own (TC-026). All Creative rows ran on these stand-ins. Probably CMS test content: filed to PM to confirm the Creative content for this build (Q-19). TC-023's demo itself auto-plays full screen and loops (1080 × 2009 view on a 1080 × 2340 screen).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] Reel_Creator: No Year-End Recap; Creative templates have raw names, one demo — PM to confirm
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Tap Cinematic Reel Creator
4. Tap the single-color-fastcut card in the second section
5. Swipe up on the Preview
6. Read the template name and demo
7. Check the result

Result:
No Year-End Recap section; Creative templates have raw names, no description and one shared demo.
摘要：沒有 Year-End Recap；Creative 模板名稱為 key、無描述、共用同一支 demo。
{20.19.0_cr06_creative_preview.jpg} {20.19.0_cr06_swipe_same_demo.jpg}

Expect Result:
PM to confirm the Creative content: Year-End Recap with 「Top 5 of My Year」, names, descriptions, demos.
摘要：請 PM 確認 Creative 內容（Year-End Recap、模板名稱、描述與各自的 demo）。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), Reel Creator room frame (rename notes, room board) -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7245-8672
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), 1. Preview frame -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7336-618
Related: Q-19
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/06_ISS-CR-06/`

---

## 7. ISS-CR-07 — PM: photo tips entry — Design ⓘ vs 「View photo tips」 chip; Creative Previews have none  ·  Class: UI  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-033, TC-024  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-029 / R-036 / R-037 (Design 02 Preview draws an ⓘ next to 「‹」; the PM Preview frame draws a 「View photo tips」 text button and a tips sheet 「Photo tips」 / 「Got it」; Q-28 open). Cinestory Previews show 「💡 View photo tips」 (PM version) opening the app-wide guide (「Recommendation」 / 「Avoid」, 「Continue」; heading and items not filed, KP-135). Creative Previews (both stand-ins) have neither ⓘ nor the chip, so their tips cannot be opened — possibly no tips content in the CMS (ISS-CR-06). PM to decide the entry (ⓘ or chip), whether the sheet keeps the app-wide 「Continue」 or the PM's 「Photo tips」 / 「Got it」, and that every template has it.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] Reel_Creator: Preview: no photo tips entry on Creative; ⓘ vs 「View photo tips」 — PM to decide
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Tap Cinematic Reel Creator
4. Tap the single-color-fastcut card in the second section
5. Look for a photo tips entry at the top
6. Tap ‹
7. Tap the Horror Movie card in the first section
8. Tap 💡 View photo tips
9. Check the result

Result:
Creative Previews have no tips entry; Cinestory shows 「💡 View photo tips」 (Design: ⓘ).
摘要：Creative Preview 沒有照片提示入口；Cinestory 為文字按鈕（Design 為 ⓘ）。
{20.19.0_cr07_creative_no_tips_entry.jpg} {20.19.0_cr07_cine_view_photo_tips.jpg} {20.19.0_cr07_tips_sheet.jpg}

Expect Result:
PM to decide ⓘ (Design) or 「View photo tips」 (PM) on every Preview, and the sheet's title and button.
摘要：請 PM 決定提示入口形式（ⓘ 或文字），且所有模板都要有。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator Design Figma (page 261109_AI_transition_feature, section Design), 02_Template_Preview_SwipeHint_Peek frame -
https://www.figma.com/design/qdzVXIFZeYwcsa6fipmcLH/Cinematic-Reel-Creator--CineStory-?node-id=1101-4947
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), 2. View photo tips frame -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7336-643
Related: Q-28
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/07_ISS-CR-07/`

---

## 8. ISS-CR-08 — Preview count line has no image icon  ·  Class: UI  ·  Severity: S4  ·  Owner: RD

**Report step:** TC-030, TC-024  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-031 (Design 02 Preview: the count 「1 Photo」 with an image icon before it; the PM wrote 「1 photo」, Q-36). Cinestory 「Horror Movie」 reads 「1 photo」 and Creative 「single-color-fastcut」 「1–30 photos」, both without the icon. Design first for the wording (capital P) as well.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] Reel_Creator: Preview: photo count has no image icon (Design 「1 Photo」 with icon)
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Tap Cinematic Reel Creator
4. Tap the Horror Movie card in the first section
5. Read the count line above Use Template
6. Check the result

Result:
The count reads 「1 photo」 with no image icon (Creative: 「1–30 photos」, no icon).
摘要：張數文字前沒有圖片 icon，且為小寫 photo。
{20.19.0_cr08_count_no_icon.jpg}

Expect Result:
The count shows an image icon and 「1 Photo」 (Design).
摘要：應有圖片 icon 並顯示「1 Photo」。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator Design Figma (page 261109_AI_transition_feature, section Design), 02_Template_Preview_SwipeHint_Peek frame -
https://www.figma.com/design/qdzVXIFZeYwcsa6fipmcLH/Cinematic-Reel-Creator--CineStory-?node-id=1101-4947
Related: Q-36
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/08_ISS-CR-08/`

---

## 9. ISS-CR-09 — Picker has no 「Add photos」 title and its tray wording differs from the Design  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-037  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-041 / R-042 (Design 03_Photo_Picker: title 「Add photos」, tray 「Select {min} to {max} photos to continue.」; the PM drew 「Add Photos」 and 「Select 5–15 photos」; Design first). The picker shows 「‹」 and a camera icon with no title, and the tray reads 「Select 15–40 photos」 (cinematic-grade). The album tab 「All ⌄」 is the album name (KP-135, not filed).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] Reel_Creator: Photo picker: no 「Add photos」 title; tray wording differs from Design
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Tap Cinematic Reel Creator
4. Swipe the second section left
5. Tap the cinematic-grade card
6. Tap Use Template
7. Read the top bar and the tray
8. Check the result

Result:
No title; the tray reads 「Select 15–40 photos」.
摘要：選圖頁沒有 Add photos 標題，tray 文字與 Design 不同。
{20.19.0_cr09_picker_no_title.jpg}

Expect Result:
Title 「Add photos」; tray 「Select 15 to 40 photos to continue.」 (Design).
摘要：應有標題 Add photos，tray 為「Select 15 to 40 photos to continue.」。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator Design Figma (page 261109_AI_transition_feature, section Design), 03_Photo_Picker frame -
https://www.figma.com/design/qdzVXIFZeYwcsa6fipmcLH/Cinematic-Reel-Creator--CineStory-?node-id=950-5298
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/09_ISS-CR-09/`

---

## 10. ISS-CR-10 — Tray thumbnails have no 「×」: a photo cannot be removed from the tray  ·  Class: Functional  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-038, TC-136  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-042 / R-124 (Design 03_Photo_Picker draws 「×」 on every tray thumbnail; tapping it unpicks the photo). No 「×」 on any tray thumbnail; a tap and a 1.5 s long-press on a thumbnail do nothing (16/40 stays). A photo leaves only by tapping it again in the grid.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] Reel_Creator: Photo picker: tray thumbnails have no 「×」 and cannot be removed
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Tap Cinematic Reel Creator
4. Swipe the second section left
5. Tap the cinematic-grade card
6. Tap Use Template
7. Tap 16 photos in the grid, one after another
8. Tap the second thumbnail in the tray
9. Check the result

Result:
The tray thumbnails have no 「×」 and the tap does nothing (16/40 stays).
摘要：tray 縮圖沒有 ×，點擊也無法移除。
{20.19.0_cr10_tray_no_x.jpg} {20.19.0_cr10_tray_tap_nothing.jpg}

Expect Result:
Each tray thumbnail has 「×」; tapping it unpicks that photo (Design).
摘要：每張 tray 縮圖應有 ×，點擊即取消選取。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator Design Figma (page 261109_AI_transition_feature, section Design), 03_Photo_Picker frame -
https://www.figma.com/design/qdzVXIFZeYwcsa6fipmcLH/Cinematic-Reel-Creator--CineStory-?node-id=950-5298
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/10_ISS-CR-10/`

---

## 11. ISS-CR-11 — No red tray text when the picked or imported count is outside the range  ·  Class: Functional  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-057, TC-058, TC-038  ·  **Reproduce:** 3/3  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-054 / R-055 (PM frame 5: after Import, a count below min shows red 「Select at least {min} photos ({n} more)」, above max red text; Next disabled). Import of 4 into cinematic-grade (15–40) and of 10 into Selfie Shake (4) keep the white 「Select 15–40 photos」 / 「Select 4 photos」 with no count; Next is disabled (OK). TC-038 (manual pick of 3) is the same missing line (Q-30, PM shows it after Import; assumption: also for a manual pick).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] Reel_Creator: Photo picker: imported count out of range shows no red tray text
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Tap Cinematic Reel Creator
4. Tap the Selfie Shake card in the third section
5. Tap Use Template
6. Tap 4 photos in the grid, one after another
7. Tap Next
8. Tap ‹ three times
9. Swipe the second section left
10. Tap the cinematic-grade card
11. Tap Use Template
12. Tap Import on the prompt
13. Check the result

Result:
4 photos are imported and Next is disabled, but the tray still reads 「Select 15–40 photos」 in white.
摘要：匯入張數低於下限時 tray 沒有紅字提示。
{20.19.0_cr11_import_below_min.jpg} {20.19.0_cr11_import_above_max.jpg}

Expect Result:
The tray shows red 「Select at least 15 photos (11 more)」 (above max: red text), Next disabled until in range.
摘要：應顯示紅字「Select at least 15 photos (11 more)」。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), 5. Imported count out of range → red text frame -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7336-859
Related: Q-30
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/11_ISS-CR-11/`

---

## 12. ISS-CR-12 — Imported photos lose their grid tick; tapping one adds it twice  ·  Class: Functional  ·  Severity: S2  ·  Owner: RD

**Report step:** TC-058, TC-059  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-053 / R-056 (PM Import prompt: Import brings in the picked state). After Import the tray holds the whole set, but some imported photos have no badge in the grid: 10 into Selfie Shake left the 10th unticked (tap → 「You can only select 4 photos.」); after 2 of 6 were deleted from the Gallery, 2 of the 4 imported were unticked and tapping one added it a second time (5/30, the same photo twice in the tray). Likely a photo-id / position mix-up (KP-073 / K03). With no deletion and within the limit every photo was ticked (TC-055, TC-133).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] Reel_Creator: Photo picker Import: imported photos unticked; tapping one adds it twice
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Tap Cinematic Reel Creator
4. Tap the single-color-fastcut card in the second section
5. Tap Use Template
6. Tap 6 photos in the grid, one after another
7. Tap Next
8. Tap ‹ three times
9. Press Home
10. Delete the first 2 of the 6 photos in Gallery
11. Open PhotoDirector from Recents
12. Tap the single-color-fastcut card
13. Tap Use Template
14. Tap Import on the prompt
15. Tap the third picked photo in the grid
16. Check the result

Result:
4 photos are in the tray but 2 have no tick in the grid; tapping one adds it again (5/30, duplicate in the tray).
摘要：匯入後部分照片在格子上沒有勾選，點擊會重複加入同一張。
{20.19.0_cr12_import_unticked.jpg} {20.19.0_cr12_duplicate_added.jpg} {20.19.0_cr12_tenth_unticked_toast.jpg}

Expect Result:
Every imported photo is ticked in the grid with its number; tapping it unpicks it.
摘要：匯入的照片都應打勾編號，點擊應取消選取。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), 4. Photo picker – Import prompt frame (session memory) -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7336-785
Spec Link: Reel Creator Design Figma (page 261109_AI_transition_feature, section Design), 03-1_Photo_Picker_Reuse_Last_Photos frame -
https://www.figma.com/design/qdzVXIFZeYwcsa6fipmcLH/Cinematic-Reel-Creator--CineStory-?node-id=957-5859
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/12_ISS-CR-12/`

---

## 13. ISS-CR-13 — Import prompt shows no 「+N」 on its third thumbnail  ·  Class: UI  ·  Severity: S4  ·  Owner: RD

**Report step:** TC-054  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-125 (Design 03-1: with more than three photos remembered, the third thumbnail is covered by 「+{N−3}」, e.g. 8 photos → 「+5」). With 7 remembered the prompt reads 「Use the 7 photos you picked last time?」 (OK) but shows photos 1–3 plainly with no 「+4」.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] Reel_Creator: Import prompt: no 「+4」 on the third thumbnail for 7 photos
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Tap Cinematic Reel Creator
4. Tap the single-color-fastcut card in the second section
5. Tap Use Template
6. Tap 7 photos in the grid, one after another
7. Tap Next
8. Tap ‹ three times
9. Tap the single-color-fastcut card
10. Tap Use Template
11. Check the result

Result:
The prompt shows three thumbnails with no 「+4」 on the third.
摘要：匯入提示第三張縮圖沒有「+4」。
{20.19.0_cr13_prompt_no_plus.jpg}

Expect Result:
The third thumbnail is covered by 「+4」 (Design 03-1).
摘要：第三張縮圖應覆蓋「+4」。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator Design Figma (page 261109_AI_transition_feature, section Design), 03-1_Photo_Picker_Reuse_Last_Photos frame -
https://www.figma.com/design/qdzVXIFZeYwcsa6fipmcLH/Cinematic-Reel-Creator--CineStory-?node-id=957-5859
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/13_ISS-CR-13/`

---

## 14. ISS-CR-14 — PM decision: one remembered photo — Design shows a prompt, PM and app show none  ·  Class: UX  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-139  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** Q-27, filed to PM for a decision. Design 03-4 draws 「Use the photo you picked last time?」 with one thumbnail; the PM says no prompt when 1 photo was picked (R-057). After 3 of 4 remembered photos were deleted from the Gallery the app shows no prompt (it follows the PM). The casebook assumed the Design card shows (Design first).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UX] Reel_Creator: Import prompt for one remembered photo: Design shows it, app does not — PM
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Tap Cinematic Reel Creator
4. Tap the Selfie Shake card in the third section
5. Tap Use Template
6. Tap 4 photos in the grid, one after another
7. Tap Next
8. Tap ‹ three times
9. Press Home
10. Delete 3 of the 4 photos in Gallery
11. Open PhotoDirector from Recents
12. Tap the single-color-fastcut card in the second section
13. Tap Use Template
14. Check the result

Result:
No Import prompt; the picker opens plain.
摘要：只剩一張記憶照片時不顯示匯入提示（Design 有、PM 無）。
{20.19.0_cr14_no_prompt_one_left.jpg}

Expect Result:
PM to decide: 「Use the photo you picked last time?」 (Design 03-4) or no prompt (PM R-057).
摘要：請 PM 決定一張照片時是否顯示提示。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator Design Figma (page 261109_AI_transition_feature, section Design), 03-4_Toast_Reuse_Last_Photos_1 frame -
https://www.figma.com/design/qdzVXIFZeYwcsa6fipmcLH/Cinematic-Reel-Creator--CineStory-?node-id=960-6686
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), 4. Photo picker – Import prompt frame (session memory) -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7336-785
Related: Q-27
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/14_ISS-CR-14/`

---

## 15. ISS-CR-15 — Confirm page lacks the 9:16 ratio and the reorder hint; layout differs from the Design  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-063, TC-094, TC-100, TC-148  ·  **Reproduce:** 4/4  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-060 / R-061 / R-064 / R-085 (PM confirm frame: 「output 9:16」 and 「Long-press to reorder · tap × to remove」; Design 04: count with image icon, 「9:16」 with ratio icon, 「Your photos (7/15)」, 「+」 first). On Creative, Cinematic (Micro Cinema) and AI Transition (Selfie Shake) pages, light and dark: no 9:16, no reorder hint, no count icon, counter 「7/30」 at the right of 「Your photos」, 「+」 last. The hint and 9:16 are in both PM and Design; the other points follow the PM where the Design differs (Design first). Text Language is ISS-CR-16, prices ISS-CR-18 / -19.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] Reel_Creator: Confirm page: no 「9:16」, no reorder hint, 「+」 last
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Tap Cinematic Reel Creator
4. Tap the single-color-fastcut card in the second section
5. Tap Use Template
6. Tap 7 photos in the grid, one after another
7. Tap Next
8. Read the confirm page
9. Check the result

Result:
No 9:16 or count icon in the header; 「Your photos」 「7/30」 with no hint; 「+」 after the photos.
摘要：確認頁沒有 9:16、沒有排序提示文字，+ 在最後，張數不在標題括號內。
{20.19.0_cr15_creative_confirm.jpg} {20.19.0_cr15_micro_cinema_confirm.jpg} {20.19.0_cr15_selfie_shake_confirm.jpg}

Expect Result:
Header shows 「9:16」; 「Your photos (7/30)」 and the reorder hint; 「+」 tile first (Design).
摘要：應有 9:16、排序提示，「+」在第一格。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator Design Figma (page 261109_AI_transition_feature, section Design), 04_Generate_Settings frame -
https://www.figma.com/design/qdzVXIFZeYwcsa6fipmcLH/Cinematic-Reel-Creator--CineStory-?node-id=961-6760
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), 6. Confirm page frame (Generate | 60) -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7336-931
Related: Q-31
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/15_ISS-CR-15/`

---

## 16. ISS-CR-16 — Creative confirm page has no Text Language bar  ·  Class: Functional  ·  Severity: S2  ·  Owner: RD

**Report step:** TC-075, TC-076, TC-148  ·  **Reproduce:** 4/4  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-067 / R-073 / R-074 (Design 04 / 04-1: a 「Text Language」 bar above Generate opening a language sheet, default the device language; PM frame 8 「Text language English ▾」). No bar on either Creative template in English, zh-Hant or dark theme, and nowhere else (not on the Preview: Q-6 asked whether the menu moves there). The reel's text language therefore cannot be chosen; 8 rows are Blocked behind it (TC-077, 078, 140, 109, 079, 080, 081, 082) and TC-116 could not set it.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] Reel_Creator: Creative confirm page has no 「Text Language」 bar
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Tap Cinematic Reel Creator
4. Tap the single-color-fastcut card in the second section
5. Tap Use Template
6. Tap 7 photos in the grid, one after another
7. Tap Next
8. Look for Text Language above Generate
9. Check the result

Result:
No 「Text Language」 bar or sheet anywhere on the page.
摘要：Creative 確認頁沒有 Text Language 選項，無法選擇影片文字語言。
{20.19.0_cr16_no_text_language.jpg} {20.19.0_cr16_no_text_language_zh.jpg}

Expect Result:
A 「Text Language」 bar above Generate shows the device language and opens the language sheet.
摘要：Generate 上方應有 Text Language 列，預設裝置語言並可開啟語言清單。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator Design Figma (page 261109_AI_transition_feature, section Design), 04-1_Generate_Settings_Text_Language_Sheet frame -
https://www.figma.com/design/qdzVXIFZeYwcsa6fipmcLH/Cinematic-Reel-Creator--CineStory-?node-id=977-4343
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), 8. Text language frame -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7337-804
Related: Q-6
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/16_ISS-CR-16/`

---

## 17. ISS-CR-17 — Count below min is not shown in red on the confirm page  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-066  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-069 (PM frame 7: removing photos below min turns the count red and disables Generate). cinematic-grade (15–40): 15 → 14 keeps 「14/40」 orange like an in-range count; Generate is disabled (OK).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] Reel_Creator: Confirm page: count below min (14/40) is not red
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Tap Cinematic Reel Creator
4. Swipe the second section left
5. Tap the cinematic-grade card
6. Tap Use Template
7. Tap 15 photos in the grid, one after another
8. Tap Next
9. Tap × on photo 1
10. Check the result

Result:
「14/40」 stays orange; Generate is disabled.
摘要：低於下限時張數未變紅。
{20.19.0_cr17_count_not_red.jpg}

Expect Result:
「14/40」 turns red and Generate is disabled.
摘要：張數應顯示紅色。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), 7. Confirm page below min frame -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7336-989
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/17_ISS-CR-17/`

---

## 18. ISS-CR-18 — PM: Creative prices 70 / 90 and AI Transition 48 vs the drawn Creative 60  ·  Class: Functional  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-063, TC-074, TC-118, TC-148  ·  **Reproduce:** 4/4  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-068 / R-071 (PM confirm frame: 「Generate | 60」 for 「Top 5 of My Year」; other templates' prices not stated, Q-9). Top 5 of My Year is not on Test Server (ISS-CR-06). single-color-fastcut charges a flat 70 (1 and 7 photos; Detail 「Reel Creator -70」, balance 1052 → 982), cinematic-grade 90 (15–40), Selfie Shake 48. The charge equals the button each time. Filed to PM to confirm the Creative / AI Transition price table (Q-9).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] Reel_Creator: Creative 70 / 90 and AI Transition 48 credits vs drawn 60 — PM to confirm
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Tap Cinematic Reel Creator
4. Tap the single-color-fastcut card in the second section
5. Tap Use Template
6. Tap 7 photos in the grid, one after another
7. Tap Next
8. Read the Generate button
9. Tap Generate
10. Tap the credit pill in the room
11. Tap Detail
12. Check the result

Result:
「Generate | 70」; 70 credits charged (1052 → 982), Detail 「Reel Creator -70」.
摘要：Creative 收 70 點（另有 90、48），spec 只畫了 60。
{20.19.0_cr18_generate_70.jpg} {20.19.0_cr18_detail_minus_70.jpg} {20.19.0_cr18_log.txt}

Expect Result:
PM to confirm each template's price (spec draws 60 for 「Top 5 of My Year」 only).
摘要：請 PM 確認各模板價格。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), 6. Confirm page frame (Generate | 60) -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7336-931
Related: Q-9
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/18_ISS-CR-18/`

---

## 19. ISS-CR-19 — Micro Cinema charges 48 credits, spec 40  ·  Class: Functional  ·  Severity: S2  ·  Owner: RD

**Report step:** TC-094, TC-096, TC-119  ·  **Reproduce:** 3/3  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-084 (PM C3 Cinematic confirm frame: 「Generate | 40」 on Micro Cinema). The button reads 「Generate | 48」 and 48 is charged (842 → 794 at 14:58:37; Detail -48). Second Micro Cinema (TC-122) 48 again. The price may be server data.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] Reel_Creator: Micro Cinema shows and charges 48 credits instead of 40
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Tap Cinematic Reel Creator
4. Tap the Micro Cinema card in the first section
5. Tap Use Template
6. Tap 1 photo
7. Tap Next
8. Read the Generate button
9. Tap Generate
10. Check the result

Result:
「Generate | 48」; the balance drops by 48 (842 → 794).
摘要：Micro Cinema 顯示並扣 48 點，spec 為 40。
{20.19.0_cr19_generate_48.jpg} {20.19.0_cr19_detail_minus_48.jpg} {20.19.0_cr19_log.txt}

Expect Result:
「Generate | 40」 and 40 deducted.
摘要：應為 40 點。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), C3. Cinematic confirm page frame (Generate | 40) -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7337-1042
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/19_ISS-CR-19/`

---

## 20. ISS-CR-20 — PM: Credit Detail names Cinematic and AI Transition uses only 「Reel Creator」  ·  Class: UI  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-119, TC-120  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-102 (KP-017: Detail lists each use under the right feature name; the feature name is not fixed, Q-2). Every Reel Creator use — Creative, Micro Cinema, Selfie Shake — is listed as 「Reel Creator / PhotoDirector (Android)」 with no time, so the three features cannot be told apart. PM to decide whether one name is intended.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] Reel_Creator: Credit Detail names every Reel Creator use 「Reel Creator」 — PM to decide
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Tap Cinematic Reel Creator
4. Tap the Selfie Shake card in the third section
5. Tap Use Template
6. Tap 4 photos in the grid, one after another
7. Tap Next
8. Tap Generate
9. Tap the credit pill in the room
10. Tap Detail
11. Check the result

Result:
The entry reads 「Reel Creator」 -48, like the Micro Cinema and Creative entries.
摘要：Credit Detail 中三種功能都顯示 Reel Creator，無法分辨。
{20.19.0_cr20_detail_names.jpg}

Expect Result:
PM to decide: one 「Reel Creator」 name for all three, or Cinematic Styles / AI Transition named separately.
摘要：請 PM 決定 Detail 中的功能名稱。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), My AI Artwork - Reel Creator tab frame -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7271-352
Related: Q-2
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/20_ISS-CR-20/`

---

## 21. ISS-CR-21 — Reel Creator strings stay English in other app languages  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-123, TC-076, TC-125  ·  **Reproduce:** 4/4  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-105 / R-107 (localised strings in every app language; PM frames carry the strings; PHD supports zh-Hant, ja, de, pt …). In zh-Hant, ja, de and pt the tray 「Select 4 photos」, the prompt 「Use the 4 photos you picked last time?」, the hint 「Please upload at least 4 photos」, 「Your photos」, 「N photos」 and 「Use Template」 stay English; only shared buttons (下一步, 匯入, 生成 …) are translated. Numbers and placeholders are right, no crash.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] Reel_Creator: Picker, Import prompt and confirm strings stay English in zh-Hant / ja / de / pt
```

**Description:**

```
Repro Steps:
1. Set the phone language to 繁體中文 (Taiwan)
2. Launch the APP
3. Swipe the Launcher shortcut grid left to page 2
4. Tap AI電影感運鏡
5. Tap the Selfie Shake card in the third section
6. Tap Use Template
7. Tap 3 photos in the grid, one after another
8. Check the result

Result:
The tray reads 「Select 4 photos」 (English); the prompt, 「Your photos」 and the upload hint are English too.
摘要：切換為中文／日文／德文／葡文時，Reel Creator 的文字仍為英文。
{20.19.0_cr21_zh_tray_english.jpg} {20.19.0_cr21_zh_prompt_english.jpg} {20.19.0_cr21_ja_hint_english.jpg}

Expect Result:
All Reel Creator strings are shown in the app language.
摘要：所有 Reel Creator 文字應依 App 語言翻譯。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), 3. Photo picker frame -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7336-704
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), 4. Photo picker – Import prompt frame (session memory) -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7336-785
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/21_ISS-CR-21/`

---

## 22. ISS-CR-22 — German Import button is cut off as 「Importie…」  ·  Class: UI  ·  Severity: S4  ·  Owner: RD

**Report step:** TC-125  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-107 (KP-101: long translations stay readable; PM Import prompt frame). In German the prompt's button reads 「Importie…」; Portuguese 「Importar」 fits.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] Reel_Creator: Import prompt button truncated to 「Importie…」 in German
```

**Description:**

```
Repro Steps:
1. Set the phone language to Deutsch
2. Launch the APP
3. Swipe the Launcher shortcut grid left to page 2
4. Tap Reel-Creator
5. Tap the Selfie Shake card in the third section
6. Tap Use Template
7. Tap 4 photos in the grid, one after another
8. Tap Weiter
9. Tap ‹ three times
10. Tap the Selfie Shake card
11. Tap Use Template
12. Check the result

Result:
The prompt button reads 「Importie…」.
摘要：德文匯入按鈕文字被截斷。
{20.19.0_cr22_de_import_cut.jpg}

Expect Result:
The button shows the full word (「Importieren」) without truncation.
摘要：按鈕文字應完整顯示。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), 4. Photo picker – Import prompt frame (session memory) -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7336-785
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/22_ISS-CR-22/`

---

## 23. ISS-CR-23 — Creative processing card shows no time estimate, 「Almost Done」 from the start  ·  Class: Functional  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-085, TC-141  ·  **Reproduce:** 3/3  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-078 / R-130 (Design 05 My AI Artwork: 「9 minutes remaining ...」 with a progress bar; 「Almost done」 once the estimate runs out). Creative cards read 「Almost Done」 5 s after Generate with an indeterminate bar, for the whole ≈ 9.5 min job (three jobs). Cinestory and AI Transition cards do show 「N minutes remaining…」 (TC-096), though 14 min shown vs 6.4 min taken (O-12).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] Reel_Creator: Creative card shows 「Almost Done」 at once, no remaining time
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Tap Cinematic Reel Creator
4. Tap the single-color-fastcut card in the second section
5. Tap Use Template
6. Tap 7 photos in the grid, one after another
7. Tap Next
8. Tap Generate
9. Read the new card in My AI Artwork
10. Check the result

Result:
The card reads 「Processing...」 / 「Almost Done」 from 5 s in, with a back-and-forth bar and no remaining time.
摘要：Creative 生成卡片一開始就顯示 Almost Done，沒有剩餘時間。
{20.19.0_cr23_almost_done_at_start.jpg} {20.19.0_cr23_cinestory_has_estimate.jpg}

Expect Result:
The card shows 「… minutes remaining ...」 with a progress bar, 「Almost done」 only after the estimate runs out.
摘要：應顯示剩餘時間與進度條，時間到才顯示 Almost done。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator Design Figma (page 261109_AI_transition_feature, section Design), 05_Result_My_AI_Artwork frame -
https://www.figma.com/design/qdzVXIFZeYwcsa6fipmcLH/Cinematic-Reel-Creator--CineStory-?node-id=970-4457
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), My AI Artwork - Reel Creator tab frame -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7271-352
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/23_ISS-CR-23/`

---

## 24. ISS-CR-24 — Completion notification opens a stale My AI Artwork page still 「Processing」  ·  Class: Functional  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-121  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-104 (KP-029: the done notification opens the finished result in My AI Artwork). The notification 「Reel Creator Ready!」 / 「Tap to see your Reel Creator.」 (phd://navigate/page?name=cinematic_reel_creator_done) brought back the old My AI Artwork page from before Home: the card stayed 「Processing… / Almost Done」 for 2.5 min until the page was reopened (status Done 14:39:38 only then). Same stale card seen at 15:18 and 15:33 (O-11 / O-12). PHA262026-0373 (closed: 「APP version does not support feature」) is not back.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] Reel_Creator: 「Reel Creator Ready!」 notification opens a stale 「Processing」 card
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Tap Cinematic Reel Creator
4. Tap the single-color-fastcut card in the second section
5. Tap Use Template
6. Tap 7 photos in the grid, one after another
7. Tap Next
8. Tap Generate
9. Press Home
10. Wait for the notification 「Reel Creator Ready!」
11. Tap the notification
12. Check the result

Result:
My AI Artwork shows the card still 「Processing…」; it updates only after reopening the page.
摘要：點完成通知後 My AI Artwork 仍顯示處理中，需重新進入才更新。
{20.19.0_cr24_notification.jpg} {20.19.0_cr24_stale_processing.jpg} {20.19.0_cr24_after_reopen.jpg} {20.19.0_cr24_log.txt}

Expect Result:
The notification opens My AI Artwork on the finished reel.
摘要：點通知應開到已完成的影片。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), My AI Artwork - Reel Creator tab frame -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7271-352
Related: PHA262026-0373 (closed; not reproduced)
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/24_ISS-CR-24/`

---

## 25. ISS-CR-25 — Interrupted upload: 70 credits charged, not refunded although the dialog says so; Retry does nothing  ·  Class: Functional  ·  Severity: S2  ·  Owner: RD

**Report step:** TC-143  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-132 (Design 05: an interrupted upload shows ⚠ 「Resume to Upload」, resuming charges no second time) and run step 8 (a failed job costs nothing net). Wi-Fi cut 0.1 s after the pack reached UploadFile: the dialog says 「Unsuccessful, please try again. Credits refunded.」, but Detail lists 「Reel Creator -70」 and no refund (912 → 842 kept at 14:51–14:52). The card is ⚠ 「Retry」 (not 「Resume to Upload」); after Wi-Fi is back, Retry only logs 「longTask retry click」 and nothing runs; the card returns to ⚠ Retry. Net 70 lost, no reel. One attempt (credits). Severity proposal S2; S1 if lost credits count as data loss.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] Reel_Creator: Wi-Fi lost during upload: 70 charged, 「Credits refunded」 but no refund
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Tap Cinematic Reel Creator
4. Tap the single-color-fastcut card in the second section
5. Tap Use Template
6. Tap 7 photos in the grid, one after another
7. Tap Next
8. Tap Generate
9. Turn Wi-Fi off right after
10. Tap OK on the error dialog
11. Turn Wi-Fi on
12. Tap the room's history icon
13. Tap Retry on the ⚠ card
14. Wait 6 minutes
15. Tap the credit pill in the room
16. Tap Detail
17. Check the result

Result:
The dialog says 「Credits refunded」 but 70 stays deducted (no refund row); Retry never runs the job.
摘要：上傳中斷後提示已退點，實際扣 70 點未退；Retry 無作用。
{20.19.0_cr25_credits_refunded_dialog.jpg} {20.19.0_cr25_retry_card.jpg} {20.19.0_cr25_detail_no_refund.jpg} {20.19.0_cr25_balance_842.jpg} {20.19.0_cr25_log.txt}

Expect Result:
「Resume to Upload」 finishes the job with one charge; a failed job refunds the 70 credits.
摘要：應可續傳完成且只扣一次；失敗時應確實退點。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator Design Figma (page 261109_AI_transition_feature, section Design), 05_Result_My_AI_Artwork frame -
https://www.figma.com/design/qdzVXIFZeYwcsa6fipmcLH/Cinematic-Reel-Creator--CineStory-?node-id=970-4457
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/25_ISS-CR-25/`

---

## 26. ISS-CR-26 — My AI Artwork tabs: 「Image to Video」 is not first and 「Reel Creator」 not second  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-089  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-080 (PM artwork frame and Design 05: 「Image to Video」 first, 「Reel Creator」 second, then the other feature tabs). The tab row is 「Recent」 then alphabetical (AI Anime Video, AI Art …, Character Motion Swap, Image to Video, Reel Creator, Style Transfer). The Reel Creator tab and its items are right; no 「Cinematic Reel Creator」 tab.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] Reel_Creator: My AI Artwork: 「Image to Video」 / 「Reel Creator」 not first and second
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Tap Cinematic Reel Creator
4. Tap the history icon
5. Swipe the tab row right to its start
6. Check the result

Result:
Tabs start 「Recent」, 「AI Anime Video」, 「AI Art」 …; 「Image to Video」 and 「Reel Creator」 come late.
摘要：My AI Artwork 分頁依字母排序，Image to Video 與 Reel Creator 不在最前。
{20.19.0_cr26_tabs_start.jpg} {20.19.0_cr26_tabs_entry.jpg}

Expect Result:
「Image to Video」 first and 「Reel Creator」 second.
摘要：Image to Video 第一、Reel Creator 第二。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), My AI Artwork - Reel Creator tab frame -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7271-352
Spec Link: Reel Creator Design Figma (page 261109_AI_transition_feature, section Design), 05_Result_My_AI_Artwork frame -
https://www.figma.com/design/qdzVXIFZeYwcsa6fipmcLH/Cinematic-Reel-Creator--CineStory-?node-id=970-4457
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/26_ISS-CR-26/`

---

## 27. ISS-CR-27 — Cinematic Styles reel is 3:4, not 9:16  ·  Class: Functional  ·  Severity: S2  ·  Owner: RD

**Report step:** TC-127, TC-122  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-023 / R-083 (PM room board: output fixed at 9:16 for every feature). Two Micro Cinema reels: 1244 × 1660 and 1176 × 1760 (ffprobe), ≈ 3:4; the Save & Share preview box is 3:4. Creative (1080 × 1920) and Selfie Shake (720 × 1280) are 9:16.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] Reel_Creator: Micro Cinema reel is 1244 × 1660 (3:4), not 9:16
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Tap Cinematic Reel Creator
4. Tap the Micro Cinema card in the first section
5. Tap Use Template
6. Tap 1 photo
7. Tap Next
8. Tap Generate
9. Wait for the reel to finish
10. Tap the Micro Cinema card
11. Tap Save
12. Check the result

Result:
The saved file is 1244 × 1660 (3:4).
摘要：Micro Cinema 輸出為 3:4，非 9:16。
{20.19.0_cr27_preview_3_4.jpg} {20.19.0_cr27_saved.jpg}

Expect Result:
The reel is 9:16 in pixels.
摘要：輸出應為 9:16。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), Reel Creator room frame (rename notes, room board) -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7245-8672
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/27_ISS-CR-27/`

---

## 28. ISS-CR-28 — After 「Create More」 a Micro Cinema result download timed out: ⚠ Retry, no notification  ·  Class: Functional  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-122  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-113 (KP-083: after Create More a new generation runs normally). From the room opened by 「Create More」, Micro Cinema (48 charged, 698 → 650): server Done at 15:41:28, then `downloadVideo Exception: java.net.SocketTimeoutException: timeout` → `DOWNLOAD_FAILED`, status DownloadFail; the card became ⚠ 「Retry」, no notification, Wi-Fi up. One Retry downloaded it in 5 s at no charge. Seen once; whether Create More or a network stall causes it is not known (the first Micro Cinema from a normal room downloaded fine).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] Reel_Creator: 「Create More」 Micro Cinema: result download times out, ⚠ Retry, no notification
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Swipe the Launcher shortcut grid left to page 2
3. Tap Cinematic Reel Creator
4. Tap the history icon
5. Tap a finished reel
6. Tap Create More
7. Tap the Micro Cinema card in the first section
8. Tap Use Template
9. Tap 1 photo
10. Tap Next
11. Tap Generate
12. Wait 15 minutes
13. Check the result

Result:
The card turns ⚠ 「Retry」 with no notification; the log shows the result download timing out.
摘要：Create More 後生成完成但下載逾時，卡片變為 Retry 且沒有通知。
{20.19.0_cr28_retry_card.jpg} {20.19.0_cr28_after_retry.jpg} {20.19.0_cr28_log.txt}

Expect Result:
The job finishes normally: the reel downloads, the card shows it and the notification arrives.
摘要：應正常完成並通知。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), My AI Artwork - Reel Creator tab frame -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7271-352
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/28_ISS-CR-28/`

---

## 29. ISS-CR-29 — Activity re-creation drops the confirm page back to the room  ·  Class: Functional  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-116  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-112 (KP-097: after Activity re-creation the confirm page keeps its photos, order and count; PM confirm frame). With Developer options 「Don’t keep activities」 ON: back from Home on the confirm page re-creates AICineStoryActivity on the room (photos, order and count lost); opening the picker destroys it too, so 「Next」 lands on the room and the confirm page cannot be reached at all. No crash. A system theme switch on a Preview also re-created the page on the room (TC-146).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] Reel_Creator: 「Don’t keep activities」: confirm page lost, 「Next」 lands on the room
```

**Description:**

```
Repro Steps:
1. Turn on Developer options, Don’t keep activities
2. Launch the APP
3. Swipe the Launcher shortcut grid left to page 2
4. Tap Cinematic Reel Creator
5. Tap the single-color-fastcut card in the second section
6. Tap Use Template
7. Tap 7 photos in the grid, one after another
8. Tap Next
9. Press Home
10. Open PhotoDirector from Recents
11. Check the result

Result:
The Reel Creator room shows instead of the confirm page; picks and order are lost.
摘要：Activity 重建後回到房間，確認頁的照片與順序遺失。
{20.19.0_cr29_confirm_before.jpg} {20.19.0_cr29_room_after.jpg} {20.19.0_cr29_next_lands_room.jpg} {20.19.0_cr29_log.txt}

Expect Result:
The confirm page comes back with the same photos, order and count.
摘要：應回到原確認頁並保留照片、順序與張數。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account
Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), 6. Confirm page frame (Generate | 60) -
https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory?node-id=7336-931
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_Reel-Creator-R1_20.19.0_images/29_ISS-CR-29/`

---

# Not raised (observations, for the record)

| Item | What was seen | Why not raised |
|---|---|---|
| O-1 | Pixel at R1-a setup: Production + subscriber on; Test Server Free showed 0 credits (new UUID). | Setup state. |
| O-2 | Device switch to the S23 from TC-008. | Setup. |
| O-3 | `pm clear` keeps the Test Server credit UUID and balance (contradicts KP-133). | Test setup; knowledge corrected (KP-136). |
| O-4 | Creative Previews lack description / tips; AI Transition plays no demo. | In ISS-CR-06 / -07. |
| O-5 | First 「Continue」 on the Edit Room jump dialog did nothing; second worked. | Seen once (1/2), not reproduced. |
| O-6 | Picker content check marks rejects with one 「!」 and no message; two ordinary photos flagged CELEBRITY. | No spec wording (Q-11); celebrity flag not verifiable. |
| O-7 | Drags taken as taps; picker keeps scroll position. | Test-tool handling. |
| O-8 | Imported photos lose their tick; no 「+N」; no red tray text. | ISS-CR-11 / -12 / -13. |
| O-9 | First 「Next」 took ≈ 2.5 min; later 1–46 s. Flat prices; Import prompt only after a Next in the same launch. | Spinner seen once; prices in ISS-CR-18 / -19. |
| O-10 | Credit Shop showed 52 after the 1000 top-up until reopened. | Credit Shop, not this feature; listed in report.md. |
| O-11 | R1-f jobs, upload while picking, stale pages, lost refund. | ISS-CR-23 / -24 / -25. |
| O-12 | R1-g jobs, stale cards, re-creation, large photos rejected. | ISS-CR-24 / -27 / -28 / -29; 6000 px rejection is the spec's 4096 px limit. |
| O-13 | Phone used outside the run 16:26–19:11 (subscriber on, AI Background, three crashes 17:28–17:37). | Not from a casebook row: not drafted (report.md). |
| Blocked (16) | 8 defect, 8 test-data | 8 deeplink rows (no URLs, Q-15); 8 rows behind ISS-CR-16 (no Text Language bar): TC-077, TC-078, TC-140, TC-109, TC-079, TC-080, TC-081, TC-082. |

# Reconciliation against the run

42 Fail (39 defect, 3 question), 16 Blocked, 2 Not run (TC-072, TC-073), 13 observations (O-1 … O-13).

| Item | Result | Disposition | Became |
|---|---|---|---|
| TC-002 | Fail | defect | 1. ISS-CR-01 |
| TC-003 | Fail | question | 5. ISS-CR-05 |
| TC-004 | Fail | defect | 1. ISS-CR-01 |
| TC-005 | Fail | defect | 2. ISS-CR-02 |
| TC-006 | Fail | defect | 3. ISS-CR-03 |
| TC-007 | Fail | defect | 4. ISS-CR-04 |
| TC-113 | Fail | question | 5. ISS-CR-05 |
| TC-023 | Fail | defect | 6. ISS-CR-06 |
| TC-024 | Fail | defect | 7. ISS-CR-07; 8. ISS-CR-08 |
| TC-026 | Fail | defect | 6. ISS-CR-06 |
| TC-030 | Fail | defect | 8. ISS-CR-08 |
| TC-033 | Fail | defect | 7. ISS-CR-07 |
| TC-037 | Fail | defect | 9. ISS-CR-09 |
| TC-038 | Fail | defect | 10. ISS-CR-10; 11. ISS-CR-11 |
| TC-136 | Fail | defect | 10. ISS-CR-10 |
| TC-054 | Fail | defect | 13. ISS-CR-13 |
| TC-057 | Fail | defect | 11. ISS-CR-11 |
| TC-058 | Fail | defect | 11. ISS-CR-11; 12. ISS-CR-12 |
| TC-059 | Fail | defect | 12. ISS-CR-12 |
| TC-139 | Fail | question | 14. ISS-CR-14 |
| TC-063 | Fail | defect | 15. ISS-CR-15; 18. ISS-CR-18 |
| TC-066 | Fail | defect | 17. ISS-CR-17 |
| TC-075 | Fail | defect | 16. ISS-CR-16 |
| TC-076 | Fail | defect | 16. ISS-CR-16; 21. ISS-CR-21 |
| TC-123 | Fail | defect | 21. ISS-CR-21 |
| TC-125 | Fail | defect | 21. ISS-CR-21; 22. ISS-CR-22 |
| TC-074 | Fail | defect | 18. ISS-CR-18 |
| TC-085 | Fail | defect | 23. ISS-CR-23 |
| TC-141 | Fail | defect | 23. ISS-CR-23 |
| TC-118 | Fail | defect | 18. ISS-CR-18 |
| TC-121 | Fail | defect | 24. ISS-CR-24 |
| TC-143 | Fail | defect | 25. ISS-CR-25 |
| TC-089 | Fail | defect | 26. ISS-CR-26 |
| TC-094 | Fail | defect | 15. ISS-CR-15; 19. ISS-CR-19 |
| TC-096 | Fail | defect | 19. ISS-CR-19 |
| TC-127 | Fail | defect | 27. ISS-CR-27 |
| TC-119 | Fail | defect | 19. ISS-CR-19; 20. ISS-CR-20 |
| TC-100 | Fail | defect | 15. ISS-CR-15 |
| TC-120 | Fail | defect | 20. ISS-CR-20 |
| TC-122 | Fail | defect | 27. ISS-CR-27; 28. ISS-CR-28 |
| TC-116 | Fail | defect | 29. ISS-CR-29 |
| TC-148 | Fail | defect | 15. ISS-CR-15; 16. ISS-CR-16; 18. ISS-CR-18 |
| O-1 | observation | — | not raised |
| O-2 | observation | — | not raised |
| O-3 | observation | — | not raised |
| O-4 | observation | — | not raised |
| O-5 | observation | — | not raised |
| O-6 | observation | — | not raised |
| O-7 | observation | — | not raised |
| O-8 | observation | — | not raised |
| O-9 | observation | — | not raised |
| O-10 | observation | — | not raised |
| O-11 | observation | — | not raised |
| O-12 | observation | — | not raised |
| O-13 | observation | — | not raised |

Filing order by severity: **3**, **12**, **16**, **19**, **25**, **27**, **1**, **2**, **5**, **6**, **7**, **9**, **10**, **11**, **14**, **15**, **17**, **18**, **20**, **21**, **23**, **24**, **26**, **28**, **29**, **4**, **8**, **13**, **22**. Nothing is filed until the review page's decisions come back.
