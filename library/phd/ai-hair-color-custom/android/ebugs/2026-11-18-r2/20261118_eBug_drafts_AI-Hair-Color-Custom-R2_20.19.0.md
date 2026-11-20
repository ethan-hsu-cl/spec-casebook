# AI Hair Color Custom (Android) — eBug drafts, round R2 (table v3), PhotoDirector 20.19.0 build 90201901

**Source:** spec-casebook run `library/phd/ai-hair-color-custom/android/runs/2026-11-17-r2/` — round R2 of draft `drafts/20261117-151025` (table v3, 87 cases), 2026-11-17 16:50 → 2026-11-18 10:35 on Samsung Galaxy S23 (SM-S9110) / Android 16 through Appium / UiAutomator2, Test Server, Free (Premium only for R2-e and TC-071 via the debug 「Set to subscriber」 switch). Tally: 17 Blocked, 26 Fail, 44 Pass.

**Status:** nothing filed, uploaded or commented. Build 20.19.0 / versionCode 90201901 (R1 and the TR261111-0042 batch were 90201900): filing needs the TR whose header names 90201901, or the user's word that TR261111-0042 covers it. ECL product 「PhotoDirector Mobile for Android」. Creator WILLY_WU, [AIAgent], API prefilled from the R1 batch (filed 2026-11-13).

Rules: reviewer rules 2026-10-21 — one action per Repro step, a Spec Link on every entry (URL on its own line), at least one image per entry, the logcat excerpt on the generation entry, no video. UX findings and PM decisions are `[AIAgent][UX]`, BugBelong PM; text is `[AIAgent][UI]` (RD when the Design / PM states it); the rest `[AIAgent]` Functional, RD. Spec basis check (REQ-055) per entry against today's Design page 616:9324 and PM page 3287:89; QA rules (rule pass 8, system Back) named as such.

**What is drafted:** 13 new entries (ISS-HCC-16…28), of which 5 ask PM for a decision. Filed tickets PHA262026P0110–P0119 are rechecked below for information only (dedupe per OS: a still-failing filed ticket gets no new card and no comment).

Legend — Class: Functional / UI / UX · Severity: S1 critical and blocking only, S2 important, S3 moderate, S4 minor · Owner: RD / PM.

---

## 1. ISS-HCC-16 — Photo guide and picker labels differ from the Design  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-092  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-088 (Design 2-before_importing_photo 617:10539 draws 「Recommend」, 「Face too small」, two Avoid items and 「Don't show again.」; the picker tabs 「Photo」 / 「Stock」). The app shows 「Recommendation」, 「Face Too Small」, a third Avoid item 「Accessories」 (woman in a wide hat), 「Don’t show again」 without the period, and the picker tabs 「Camera ⌄」 / 「Stock」. The Design states the text and the app differs, so RD (text rule). The 「Accessories」 item may answer Q-20 (10/E D2-02 asks to avoid hats): the Note names it so RD / PM can keep it if intended. The guide's content is fetched from the server (O-4), so the fix may be server data.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] AI_Hair_Color: Photo guide reads 「Recommendation」, 「Face Too Small」, adds 「Accessories」 vs the Design
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Read the photo guide shown over the picker
5. Tap Continue
6. Read the picker's tabs
7. Check the result

Result:
The guide reads 「Recommendation」 and 「Face Too Small」, adds 「Accessories」; picker tabs are 「Camera」 / 「Stock」.
摘要：照片指引標題與項目文字和 Design 不同，多一個 Accessories，相簿分頁為 Camera / Stock。
{20.19.0_hcc16_guide_text.jpg} {20.19.0_hcc16_picker_tabs.jpg}

Expect Result:
As the Design: 「Recommend」, 「Face too small」 (two Avoid items), 「Don't show again.」, tabs 「Photo」 / 「Stock」.
摘要：應與 Design 文字一致（Recommend、Face too small、Photo / Stock）。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: AI Hair Color Design Figma (Hair, 261005_AI_hair_color page), 2-before_importing_photo frame (photo guide) -
https://www.figma.com/design/2VOqiPxBCISkob7wbM9hXD/Hair?node-id=617-10539
Related: Q-20 (is a hat item expected under Avoid?) is open on the casebook side
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_AI-Hair-Color-Custom-R2_20.19.0_images/01_ISS-HCC-16/`

---

## 2. ISS-HCC-17 — No-face dialog reads 「A face is required」, not the spec's 「Face is required」  ·  Class: UI  ·  Severity: S4  ·  Owner: RD

**Report step:** TC-009  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-010 (11/25 進房檢查 board quotes the 10/E string 「No face detected. Face is required for this feature.」). Re-offered: the same finding was drafted in R1 as ISS-HCC-02 and held by the user on 2026-11-13 with no reason; it still reproduces on 90201901. Owner RD (the spec states the text; the 2026-11-11 rule: never Doc). Hold again if the R1 decision stands.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] AI_Hair_Color: No-face dialog reads 「A face is required」, not 「Face is required」
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Tap Continue on the photo tips sheet
5. Tap a photo with no face (a teacup)
6. Check the result

Result:
The dialog body reads 「No face detected. A face is required for this feature.」
摘要：無臉提示文字多了「A」。
{20.19.0_hcc17_no_face_copy.jpg}

Expect Result:
The body reads 「No face detected. Face is required for this feature.」
摘要：文字應為「No face detected. Face is required for this feature.」

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: AI Hair Color Custom PM Figma (26 11E AI Hair Color Custom), Spec - 進房檢查 & Photo Picker board (11/25) -
https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3370-1666
Related: R1 draft ISS-HCC-02 (held 2026-11-13)
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_AI-Hair-Color-Custom-R2_20.19.0_images/02_ISS-HCC-17/`

---

## 3. ISS-HCC-18 — Edit Room's Quick Action row has no 「Hair Color」 tool  ·  Class: Functional  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-015  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-089 (Design 1_edit_room 788:1354 draws 「Hair Color」 in the Quick Action row after 「Hairstyle」; tapping it opens AI Hair Color with the photo being edited). The row walked end to end on 90201901: AI Edit Agent, AI Removal, Crop, Text, Cutout, Background, Mosaic, AI Expand, AI Replace, Add Photo, Sticker, InstaFill, Brush, Move, Clone, Frame, AI Scene; no Hair Color. The tool is reachable only under Portrait › Hair › AI Hair Color (O-6). TC-015's missing slanted-face warning is PHA262026P0110 (recheck, not this entry).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] AI_Hair_Color: Edit Room Quick Action row has no 「Hair Color」 tool
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Tap Continue on the photo tips sheet
5. Tap a portrait photo
6. Tap ✕ at the bottom left
7. Tap Discard
8. Swipe the Quick Action row to its end
9. Check the result

Result:
The Quick Action row has no 「Hair Color」; the tool is only under Portrait, then Hair.
摘要：Edit Room 的 Quick Action 列沒有 Hair Color。
{20.19.0_hcc18_quick_action_start.jpg} {20.19.0_hcc18_quick_action_end.jpg}

Expect Result:
「Hair Color」 sits in the Quick Action row after 「Hairstyle」 and opens AI Hair Color with the photo.
摘要：Quick Action 列應有 Hair Color（在 Hairstyle 之後）。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: AI Hair Color Design Figma (Hair, 261005_AI_hair_color page), 1_edit_room frame (Quick Action row) -
https://www.figma.com/design/2VOqiPxBCISkob7wbM9hXD/Hair?node-id=788-1354
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_AI-Hair-Color-Custom-R2_20.19.0_images/03_ISS-HCC-18/`

---

## 4. ISS-HCC-19 — PM decision: with Solid the Highlight row disappears (PM) or stays greyed (Design)?  ·  Class: UX  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-024, TC-029  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** Q-18, filed to PM for a decision (2026-11-11 rule). Design 4-hair_color_case2-1_toast 929:1901 keeps the 「Highlight Color」 row on screen greyed out for Solid; the PM page D6-04 (panel_two_tone) says it does not appear. 90201901 removes the row (title and swatches gone, the Base row moves down); switching back to a two-colour style brings it back with the colour kept (TC-029). The casebook assumed the Design (Design-first rule) but cannot tell which source is newer.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UX] AI_Hair_Color: Custom panel: Solid hides the Highlight Color row; Design greys it, PM hides it — which?
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Tap Continue on the photo tips sheet
5. Tap a portrait photo with one clear, front-facing face
6. Tap Custom in the swatch row
7. Tap Solid in Style
8. Check the result

Result:
The 「Highlight Color」 row disappears; only 「Base Color」 stays.
摘要：選 Solid 後 Highlight Color 列整列消失（Design 為灰階停用，PM 為不顯示）。
{20.19.0_hcc19_solid_no_highlight_row.jpg} {20.19.0_hcc19_ombre_row_back.jpg}

Expect Result:
PM to decide: keep the row greyed out (Design 929:1901) or hide it (PM D6-04), and align the other source.
摘要：請 PM 決定 Solid 時 Highlight 列應隱藏或灰階停用。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: AI Hair Color Design Figma (Hair, 261005_AI_hair_color page), 4-hair_color_case2-1_toast frame (Solid: Highlight row greyed) -
https://www.figma.com/design/2VOqiPxBCISkob7wbM9hXD/Hair?node-id=929-1901
Spec Link: AI Hair Color Custom PM Figma (26 11E AI Hair Color Custom), panel_two_tone (NEW) frame, Spec - UI (D6-04) -
https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3327-1077
Related: Q-18
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_AI-Hair-Color-Custom-R2_20.19.0_images/04_ISS-HCC-19/`

---

## 5. ISS-HCC-20 — PM decision: two-colour style with Base only keeps Generate disabled (ruling REQ-003 says it must generate)  ·  Class: UX  ·  Severity: S2  ·  Owner: PM

**Report step:** TC-026  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** The user's rulings REQ-003 (2026-11-13) and REQ-007 (2026-11-17, Q-19: 「只選Base應該也要可以生成」) say Base Color alone must enable Generate for a two-colour style. The PM page D6-04 (both colours required) and the Design cases 2 / 2-1 (Generate grey, toast) say the opposite, and 90201901 now follows them: Generate stays grey and 「Both Base Color and Highlight Color are required.」 shows under the rows (R1's 90201900 enabled Generate here; ISS-HCC-05 was held for that). Filed to PM so the spec and the app follow one rule. O-9: the grey line also shows when both colours are chosen.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UX] AI_Hair_Color: Custom panel: two-colour style with only Base Color keeps Generate disabled — PM to decide
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Tap Continue on the photo tips sheet
5. Tap a portrait photo with one clear, front-facing face
6. Tap Custom in the swatch row
7. Tap Ombre in Style
8. Tap the dark brown swatch in Base Color
9. Check the result

Result:
Generate stays grey (disabled) and 「Both Base Color and Highlight Color are required.」 shows.
摘要：只選 Base Color 時 Generate 不可按，與「只選 Base 也要能生成」的裁示不同。
{20.19.0_hcc20_base_only_generate_disabled.jpg}

Expect Result:
PM to decide: Base alone generates (ruling) or both colours are required (D6-04, Design case 2).
摘要：請 PM 決定只選 Base 是否可生成，並統一 spec 與 app。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: AI Hair Color Custom PM Figma (26 11E AI Hair Color Custom), panel_two_tone (NEW) frame, Spec - UI (D6-04) -
https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3327-1077
Spec Link: AI Hair Color Design Figma (Hair, 261005_AI_hair_color page), 4-hair_color_case2-1 frame (toast) -
https://www.figma.com/design/2VOqiPxBCISkob7wbM9hXD/Hair?node-id=892-1796
Related: REQ-003 / REQ-007 (casebook rulings), Q-19; R1 draft ISS-HCC-05 (held)
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_AI-Hair-Color-Custom-R2_20.19.0_images/05_ISS-HCC-20/`

---

## 6. ISS-HCC-21 — Highlight-only Generate shows no 「Select both a base and highlight color.」 toast  ·  Class: Functional  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-027  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-029 / R-085 (Design 4-hair_color_case2-1 892:1796 draws the toast 「Select both a base and highlight color.」 over the photo when Generate is tapped without a Base Color; answers Q-16). Balayage with only a Highlight colour: Generate grey, two taps (one recorded at 2 fps): no toast, only the static grey line 「Both Base Color and Highlight Color are required.」 under the rows. No generation, no charge.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] AI_Hair_Color: Custom panel: tapping grey Generate with Highlight only shows no 「Select both…」 toast
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Tap Continue on the photo tips sheet
5. Tap a portrait photo with one clear, front-facing face
6. Tap Custom in the swatch row
7. Tap Balayage in Style
8. Tap the sand swatch in Highlight Color
9. Tap Generate
10. Check the result

Result:
Nothing happens: no toast shows over the photo.
摘要：只選 Highlight 時點 Generate 沒有任何 toast。
{20.19.0_hcc21_highlight_only.jpg} {20.19.0_hcc21_no_toast.jpg}

Expect Result:
The toast 「Select both a base and highlight color.」 shows over the photo; nothing is generated.
摘要：應顯示 toast「Select both a base and highlight color.」。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: AI Hair Color Design Figma (Hair, 261005_AI_hair_color page), 4-hair_color_case2-1 frame (toast) -
https://www.figma.com/design/2VOqiPxBCISkob7wbM9hXD/Hair?node-id=892-1796
Related: Q-16
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_AI-Hair-Color-Custom-R2_20.19.0_images/06_ISS-HCC-21/`

---

## 7. ISS-HCC-22 — A palette colour is not added to the row as a new circle  ·  Class: Functional  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-032  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-034 / R-035 / R-086 (Design 4-hair_color_case3 894:2637: after 「Done」 the picked colour becomes a new circle right after the colour wheel, ringed, the recommended colours shift one place right). On 90201901 the wheel key itself takes the selection ring and stays a rainbow; no new circle, the 8 recommended colours do not move, and the picked colour is shown nowhere (O-10). The colour is kept as the row's value (the palette reopens at it) and generates correctly (R2-e). R1's 90201900 did add the circle.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] AI_Hair_Color: Custom palette: colour picked with Done is not added to the row as a new circle
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Tap Continue on the photo tips sheet
5. Tap a portrait photo with one clear, front-facing face
6. Tap Custom in the swatch row
7. Tap Ombre in Style
8. Tap the colour wheel in Base Color
9. Drag the hue slider to blue
10. Drag the cursor to the square's top right
11. Tap Done
12. Check the result

Result:
The colour wheel gets the selection ring; no new circle with the blue appears and the recommended colours do not move.
摘要：調色盤選色後沒有新增色圈，選中的是色輪本身，看不到所選顏色。
{20.19.0_hcc22_palette_blue.jpg} {20.19.0_hcc22_no_new_circle.jpg}

Expect Result:
The blue is added as a new ringed circle right after the colour wheel; the other colours move one place right.
摘要：所選顏色應新增為色輪右側的色圈並被選中。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: AI Hair Color Design Figma (Hair, 261005_AI_hair_color page), 4-hair_color_case3 frame (palette colour added) -
https://www.figma.com/design/2VOqiPxBCISkob7wbM9hXD/Hair?node-id=894-2637
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_AI-Hair-Color-Custom-R2_20.19.0_images/07_ISS-HCC-22/`

---

## 8. ISS-HCC-23 — PM decision: tapping the photo above the panel closes it and applies (ruling REQ-004 says it stays open)  ·  Class: UX  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-039  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** The user's ruling REQ-004 (2026-11-13): tapping the photo above the Custom panel must not close it; nothing applied or cancelled. The PM page D6-08 (collapsed_applied) says tap outside = apply, and 90201901 now does that (R1's 90201900 kept the panel open; ISS-HCC-09 was held for that). Filed to PM so the spec and the app follow one rule. PM-only: the Design does not draw it.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UX] AI_Hair_Color: Custom panel: tapping the photo closes the panel and applies — PM to decide
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Tap Continue on the photo tips sheet
5. Tap a portrait photo with one clear, front-facing face
6. Tap Custom in the swatch row
7. Tap Balayage in Style
8. Tap the dark brown swatch in Base Color
9. Tap the sand swatch in Highlight Color
10. Tap the photo above the panel
11. Check the result

Result:
The panel closes and Custom is applied (swatch row back, Custom selected).
摘要：點面板上方照片時面板收合並套用；與 2026-11-13 的裁示（不應關閉）不同。
{20.19.0_hcc23_before_photo_tap.jpg} {20.19.0_hcc23_after_photo_tap.jpg}

Expect Result:
PM to decide: the panel stays open, nothing applied (ruling), or tap outside applies (D6-08).
摘要：請 PM 決定點照片時面板是否收合套用。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: AI Hair Color Custom PM Figma (26 11E AI Hair Color Custom), collapsed_applied (NEW) frame, Spec - UI (D6-08) -
https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3330-512
Related: REQ-004 (casebook ruling); R1 draft ISS-HCC-09 (held)
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_AI-Hair-Color-Custom-R2_20.19.0_images/08_ISS-HCC-23/`

---

## 9. ISS-HCC-24 — Generate in the panel collapses the panel instead of keeping it open  ·  Class: Functional  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-045, TC-047  ·  **Reproduce:** 13/13  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-041 (Spec - Flow, in-panel Generate D6-22 / D6-23: the panel stays open, the swatch row and Generate are disabled during the wait, then the result fills the photo, a 44 pt Intensity row appears above the panel's button, which reads 「Retry」). On 90201901 every in-panel Generate of R2-d / R2-e (13) collapsed the panel at once to the Solid / Multicolor template row with Custom selected; the result and Intensity show there (O-15). R1's 90201900 kept the panel open. The missing 「Applying your new hair color...」 in the same wait is PHA262026P0116 (recheck, not this entry).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] AI_Hair_Color: Custom panel collapses as soon as Generate is tapped in it; it should stay open
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Tap Continue on the photo tips sheet
5. Tap Stock
6. Search 「woman portrait」 in Pexels
7. Tap the portrait of a woman in a knitted hat
8. Tap Custom in the swatch row
9. Tap Solid in Style
10. Tap the green swatch in Base Color
11. Tap Generate in the panel
12. Check the result

Result:
The panel closes at once to the template row with Custom selected; the result shows there.
摘要：在面板內按 Generate 後面板立即收合。
{20.19.0_hcc24_panel_before_generate.jpg} {20.19.0_hcc24_collapsed_on_generate.jpg} {20.19.0_hcc24_result_panel_closed.jpg} {20.19.0_hcc24_log.txt}

Expect Result:
The panel stays open and disabled while waiting; the result shows above it with Intensity and 「Retry」.
摘要：面板應保持展開，結果與 Intensity 顯示於上方，按鈕變 Retry。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: AI Hair Color Custom PM Figma (26 11E AI Hair Color Custom), Spec - Flow board (in-panel Generate, D6-22 / D6-23) -
https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3287-93
Spec Link: AI Hair Color Custom PM Figma (26 11E AI Hair Color Custom), result_custom (NEW) frame, Spec - UI -
https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3330-718
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_AI-Hair-Color-Custom-R2_20.19.0_images/09_ISS-HCC-24/`

---

## 10. ISS-HCC-25 — ✕ and system Back on a result ask 「Discard changes?」 and land in the Edit Room  ·  Class: Functional  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-079, TC-088  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-068 (10/E D1-20b: ✕ gives up this edit and returns to the screen before entry with no second confirmation); R-076 is a QA rule (rule pass 8: system Back does what ✕ does). Entered from Launcher › AI Photos: ✕ and Back on a Custom result show 「Discard changes?」 / 「All your existing changes will be lost.」 / Keep / Discard; Discard lands in the Edit Room with the original photo, not the Launcher. The result is in My AI Artwork (holds). Re-offered: drafted in R1 as ISS-HCC-14 and held by the user on 2026-11-13 with no reason; still reproduces on 90201901.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] AI_Hair_Color: ✕ on a result asks 「Discard changes?」, then opens Edit Room, not the Launcher
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Tap Continue on the photo tips sheet
5. Tap Stock
6. Search 「woman portrait」 in Pexels
7. Tap the portrait of a woman in a knitted hat
8. Tap Custom in the swatch row
9. Tap Solid in Style
10. Tap the green swatch in Base Color
11. Tap Generate in the panel
12. Wait for the result
13. Tap ✕ at the bottom left
14. Tap Discard
15. Check the result

Result:
「Discard changes?」 shows; Discard opens the Edit Room with the photo instead of the Launcher.
摘要：按 ✕ 會跳「Discard changes?」確認，之後進入 Edit Room 而非回到 Launcher。
{20.19.0_hcc25_x_discard_dialog.jpg} {20.19.0_hcc25_discard_lands_edit_room.jpg} {20.19.0_hcc25_back_discard_dialog.jpg}

Expect Result:
✕ returns straight to the screen before entry (the Launcher) with no confirmation.
摘要：✕ 應不經確認直接回到進入前的畫面（Launcher）。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: AI Hair Color PM Figma (26 10E AI Hair Color v2, cited by the Custom page), Spec - UI rule D1-20b (✕ leaves with no confirmation) -
https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3030-296
Related: R1 draft ISS-HCC-14 (held 2026-11-13)
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_AI-Hair-Color-Custom-R2_20.19.0_images/10_ISS-HCC-25/`

---

## 11. ISS-HCC-26 — Subscriber without credits sees 「Get Credit Refilled!」 / 「GET CREDITS」, not 「More Credits Required!」 / 「Get Credit」  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-071  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-063 (10/E Credit not enough card 3031:293: subscriber → 「More Credits Required!」 → 「Get Credit」 → Credit Shop). VIP via the debug 「Set to subscriber」 switch (KP-131; Mine 「Hello VIP!」), 0 credits, Custom Ombre: the dialog reads 「Get Credit Refilled!」 / 「You don't have enough credits for this feature. Don’t worry, you have 50% off credit pricing.」 / 「GET CREDITS」. The button does open the Credit Shop (holds). The dialog may be the app's shared credit dialog; if so PM may update the card instead. Nothing bought (O-12: the shop issued the VIP daily 3 credits).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] AI_Hair_Color: Subscriber out of credits sees 「Get Credit Refilled!」, not 「More Credits Required!」
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Tap Continue on the photo tips sheet
5. Tap a portrait photo with one clear, front-facing face
6. Tap Custom in the swatch row
7. Tap Ombre in Style
8. Tap the brown swatch in Base Color
9. Tap the sand swatch in Highlight Color
10. Tap Generate
11. Check the result

Result:
A dialog 「Get Credit Refilled!」 with the button 「GET CREDITS」 shows.
摘要：訂閱者點數不足時對話框標題為 Get Credit Refilled!、按鈕 GET CREDITS。
{20.19.0_hcc26_credit_dialog_text.jpg}

Expect Result:
「More Credits Required!」 with 「Get Credit」, which opens the Credit Shop.
摘要：應顯示「More Credits Required!」與「Get Credit」。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: AI Hair Color PM Figma (26 10E AI Hair Color v2, cited by the Custom page), Credit not enough card (subscriber → More Credits Required! → Get Credit) -
https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3031-293
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_AI-Hair-Color-Custom-R2_20.19.0_images/11_ISS-HCC-26/`

---

## 12. ISS-HCC-27 — PM decision: the first Solid template is 「Soft Black」, not the spec's 「Platinum」  ·  Class: UI  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-017  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-016 / R-017 (the PM page and the Design 4-hair_color 686:1427 draw 「Custom」 then 「Platinum」 first, selected on entry). On 90201901 the Solid row is Custom, Soft Black (selected), Cocoa (crown), Hazelnut, Silver, Espresso…; no 「Platinum」 anywhere in the row. The template list comes from the CMS, so the mockup name may be a placeholder: filed to PM to confirm which first template ships (Q-2 covers the Custom cell's look, which now matches the Design).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] AI_Hair_Color: Colour page: first Solid template is 「Soft Black」, no 「Platinum」 — PM to confirm
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Tap Continue on the photo tips sheet
5. Tap a portrait photo with one clear, front-facing face
6. Read the swatch row of the Solid tab
7. Check the result

Result:
The row is Custom, Soft Black (selected), Cocoa, Hazelnut, Silver, Espresso; there is no 「Platinum」.
摘要：Solid 第一個模板為 Soft Black，沒有 spec 的 Platinum。
{20.19.0_hcc27_first_template_soft_black.jpg}

Expect Result:
PM to confirm the first template: 「Platinum」 (spec) or 「Soft Black」 (CMS today); the spec or the CMS then follow it.
摘要：請 PM 確認第一個模板應為 Platinum 或 Soft Black。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: AI Hair Color Design Figma (Hair, 261005_AI_hair_color page), 4-hair_color frame (swatch row) -
https://www.figma.com/design/2VOqiPxBCISkob7wbM9hXD/Hair?node-id=686-1427
Related: Q-2
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_AI-Hair-Color-Custom-R2_20.19.0_images/12_ISS-HCC-27/`

---

## 13. ISS-HCC-28 — PM decision: the two split-dye styles have photo thumbnails, not plain-colour ones  ·  Class: UI  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-022  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-025 (PM page: the split-dye styles get plain-colour thumbnails, placeholders until art). 「Half-and-half」 and 「Split-dye」 show model-photo thumbnails like the other 9 styles. R1 read the photos as finished art (R1 O-6, not raised); filed now to PM to confirm, as the row still names plain colour. The style list (11) and the crowns (Balayage, Face framing, Bangs, Half-and-half) hold.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] AI_Hair_Color: Custom panel: split-dye styles show photo thumbnails, not plain-colour ones — PM to confirm
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Tap Continue on the photo tips sheet
5. Tap a portrait photo with one clear, front-facing face
6. Tap Custom in the swatch row
7. Swipe the Style row to its end
8. Check the result

Result:
「Half-and-half」 and 「Split-dye」 have model-photo thumbnails.
摘要：兩個 split-dye style 縮圖為模特兒照片，非 spec 的純色縮圖。
{20.19.0_hcc28_split_dye_thumbnails.jpg}

Expect Result:
PM to confirm the thumbnails: plain-colour (spec) or the photos (app); the spec then follows it.
摘要：請 PM 確認 split-dye 縮圖應為純色或照片。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: AI Hair Color Design Figma (Hair, 261005_AI_hair_color page), 4-hair_color_case1_no_style frame -
https://www.figma.com/design/2VOqiPxBCISkob7wbM9hXD/Hair?node-id=894-1474
Related: Q-6
<Claude Reviewed>
```

**Images:** `20261118_eBug_drafts_AI-Hair-Color-Custom-R2_20.19.0_images/13_ISS-HCC-28/`

---

# Rechecks of filed tickets (information only — no comment, reopen or reject)

| Ticket | Filed for | On 90201901 | Rows |
|---|---|---|---|
| PHA262026P0110 | No slanted-face warning | still failing | TC-005, TC-012, TC-015 (tilted 30° / 45°, after Crop, from Edit Room › Portrait › Hair: no warning; faceNum 1) |
| PHA262026P0111 | Custom panel ︽ / ✕ ↩ ↪ ✓ row / corners | fixed | TC-019: ⌄ + grab handle, ✕ ↺ ↻ ✓ row hidden |
| PHA262026P0112 | Colour rows usable before a style | symptom gone | TC-019 / TC-021: no colour can be picked before a style, but the rows are hidden rather than drawn disabled as the Design 894:1474 does (informational; the fix is not rejected) |
| PHA262026P0113 | No eyedropper in the palette | fixed | TC-031, TC-035 |
| PHA262026P0114 | Back in the palette leaves the room | fixed | TC-086 (Back closes only the palette) |
| PHA262026P0115 | Collapse keeps Soft Black; Generate makes a template | partly fixed | TC-040: collapse keeps Custom and the outer Generate is a Custom generation; TC-038 / TC-041 / TC-042: the Custom cell still never shows the chosen colours |
| PHA262026P0116 | No 「Applying your new hair color...」 text | still failing | TC-045, TC-046, TC-040 (scan bar only, 44–47 s) |
| PHA262026P0117 | No Intensity bar on a Custom result | fixed | TC-047, TC-048, TC-049, TC-053 |
| PHA262026P0118 | No one-time My AI Artwork 100% dialog | still failing | TC-057 |
| PHA262026P0119 | Custom result not recalled after a template | fixed | TC-054 |

# Not raised (observations, for the record)

| Item | What was seen | Why not raised |
|---|---|---|
| O-1 | No Intro Demo on this install. | Test data (app data may not be cleared); TC-001 group Blocked. |
| O-2 | No 「AI Magic」 section / 「Hair Color」 card on the Launcher. | Recorded on TC-001 (Blocked); Launcher layout is CMS. |
| O-3 | Credits 0 after the 2026-11-17 reinstall. | KP-133; account state, not the feature. |
| O-4 | The photo guide's content comes from the server. | Context for ISS-HCC-16. |
| O-5 | With 0 credits Generate offers 「1 Free Trial」. | Free-trial offer, as designed (KP-016). |
| O-6 | AI Hair Color sits under Portrait › Hair. | Part of ISS-HCC-18. |
| O-7 | hc_wide16x9 shows the face-too-small dialog first. | Fixture note. |
| O-8 | Free user on a crowned style sees a 「VIP FREE TRIAL」 banner. | No row or spec item; paywall works (TC-069 Pass). |
| O-9 | 「Both Base Color and Highlight Color are required.」 shows at all times for two-colour styles. | Folded into ISS-HCC-20. |
| O-10 | A palette colour is kept but shown nowhere. | Part of ISS-HCC-22. |
| O-11 | Custom panel changes since R1. | Summary; covered by the rechecks and entries. |
| O-12 | VIP daily bonus 3 credits issued by the shop. | Account bonus, not this feature. |
| O-13 | Reel Creator charges on the same balance. | Other use of the install. |
| O-14 | The photo guide shows again after the reinstall. | Expected after a reinstall. |
| O-15 | The panel collapses on Generate. | ISS-HCC-24. |
| O-16 | Style names differ from the CMS keys; Bangs ≈ Face framing on a no-fringe photo. | Names come from the CMS (Q-13); every style generated its pattern (R2-e Pass). |
| O-17 | One extra Face framing generation by the agent's helper. | Test-run slip, not the app. |
| O-18 | VIP pays 6 credits per Custom image although Premium advertises 50% off credit pricing. | The table expects 6 (R-040); the 50% applies to credit-pack prices in the shop (TC-071). Note for PM only. |
| O-19 | A Custom generation starts from the original photo. | As expected. |
| Blocked (17) | 3 defect, 4 observability, 10 test-data | No verdict; reasons in report.md. TC-006 / TC-087 / TC-007 are blocked by PHA262026P0110. |

# Reconciliation against the run

26 Fail (22 defect, 4 question), 17 Blocked, 0 Not run, 19 observations (O-1 … O-19).

| Item | Result | Disposition | Became |
|---|---|---|---|
| TC-092 | Fail | defect | 1. ISS-HCC-16 |
| TC-005 | Fail | defect | recheck — PHA262026P0110 (still failing) |
| TC-009 | Fail | defect | 2. ISS-HCC-17 |
| TC-012 | Fail | defect | recheck — PHA262026P0110 (still failing) |
| TC-015 | Fail | defect | 3. ISS-HCC-18 and recheck PHA262026P0110 (slant) |
| TC-017 | Fail | question | 12. ISS-HCC-27 |
| TC-019 | Fail | defect | recheck — PHA262026P0112 (rows hidden, not disabled) / P0111 fixed |
| TC-022 | Fail | question | 13. ISS-HCC-28 |
| TC-021 | Fail | defect | recheck — PHA262026P0112 (rows hidden, not disabled) |
| TC-024 | Fail | question | 4. ISS-HCC-19 |
| TC-026 | Fail | defect | 5. ISS-HCC-20 |
| TC-027 | Fail | defect | 6. ISS-HCC-21 |
| TC-029 | Fail | question | 4. ISS-HCC-19 |
| TC-032 | Fail | defect | 7. ISS-HCC-22 |
| TC-038 | Fail | defect | recheck — PHA262026P0115 (cell colours still missing) |
| TC-039 | Fail | defect | 8. ISS-HCC-23 |
| TC-041 | Fail | defect | recheck — PHA262026P0115 (cell colours still missing) |
| TC-042 | Fail | defect | recheck — PHA262026P0115 (cell colours still missing) |
| TC-045 | Fail | defect | 9. ISS-HCC-24 and recheck PHA262026P0116 (no text) |
| TC-057 | Fail | defect | recheck — PHA262026P0118 (still failing) |
| TC-046 | Fail | defect | recheck — PHA262026P0116 (still failing) |
| TC-047 | Fail | defect | 9. ISS-HCC-24 |
| TC-040 | Fail | defect | recheck — PHA262026P0116 (still failing); P0115 template part fixed |
| TC-079 | Fail | defect | 10. ISS-HCC-25 |
| TC-088 | Fail | defect | 10. ISS-HCC-25 |
| TC-071 | Fail | defect | 11. ISS-HCC-26 |
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
| O-14 | observation | — | not raised |
| O-15 | observation | — | not raised |
| O-16 | observation | — | not raised |
| O-17 | observation | — | not raised |
| O-18 | observation | — | not raised |
| O-19 | observation | — | not raised |

Filing order by severity: **5**, **1**, **3**, **4**, **6**, **7**, **8**, **9**, **10**, **11**, **12**, **13**, **2**. Nothing is filed until the review page's decisions come back.
