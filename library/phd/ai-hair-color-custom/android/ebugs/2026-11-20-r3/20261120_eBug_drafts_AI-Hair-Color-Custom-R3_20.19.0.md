# AI Hair Color Custom (Android) — eBug drafts, round R3 (table v4), PhotoDirector 20.19.0 build 90201901

**Source:** spec-casebook run `library/phd/ai-hair-color-custom/android/runs/2026-11-20-r3/` — round R3 of draft `drafts/20261118-120459` (table v4, 87 cases), 2026-11-20 10:06 → 11:30 on Google Pixel 8a / Android 16 through Appium / UiAutomator2, Test Server, Free (Premium only for R3-e via the debug 「Set to subscriber」 switch, KP-131). Credits: 2000 test-card pack bought for the run (REQ-011), 2000 → 1874. Tally: 13 Blocked, 18 Fail, 56 Pass.

**Filed by:** WILLY_WU on 2026-11-20 (IF3 API, TR261111-0042, Build 202611181947): entry 4 ISS-HCC-34 = [PHA262026P0151](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/PHA262026P0151); entries 1, 2, 3, 5, 6 held (decisions.md). Nothing commented.

**Status (at drafting):** nothing filed, uploaded or commented. Build 20.19.0 / versionCode 90201901, the build the user confirmed for TR261111-0042 on 2026-11-18 (R2 batch). ECL product 「PhotoDirector Mobile for Android」. Creator WILLY_WU, TR261111-0042, [AIAgent], API prefilled from the R2 batch (filed 2026-11-18) — confirm.

Rules: reviewer rules 2026-10-21 — one action per Repro step, a Spec Link on every entry (URL on its own line), at least one image per entry, the logcat excerpt on the generation entry, no video. UX findings and PM decisions are `[AIAgent][UX]`, BugBelong PM; text is `[AIAgent][UI]` (RD when the Design / PM states it); the rest `[AIAgent]` Functional, RD. Spec basis check (REQ-055) per entry against today's Design page 616:9324 and PM page 3287:89; QA rules (rule pass 8, system Back) named as such.

**What is drafted:** 6 new entries (ISS-HCC-31…36), of which 3 ask PM for a decision. Findings that repeat a filed Android ticket (PHA262026P0110, P0116, P0118, P0128, P0149) get no entry (dedupe per OS, overlay rule 7); they and the other rechecks are in `dedupe.txt` and the run's report.md, for information only (no comment). Entries 5 and 6 re-offer R2 drafts held without a reason (ISS-HCC-27, -28); R2's ISS-HCC-24 (panel collapses on Generate) is now PHA262026P0149 and gets no entry; R2 drafts held with a ruling (REQ-009) are not re-offered.

Legend — Class: Functional / UI / UX · Severity: S1 critical and blocking only, S2 important, S3 moderate, S4 minor · Owner: RD / PM.

---

## 1. ISS-HCC-31 — Intro Demo button reads 「Try now」, not the spec's 「Try Now」  ·  Class: UI  ·  Severity: S4  ·  Owner: RD

**Report step:** TC-001  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-002 (PM Spec - Flow, Intro Demo: 「AI Hair Color」, the description, 「Try Now」, 「Don't show again」, ‹). First time a run saw the Intro Demo (R1 / R2 never got it). Title, description, 「Don’t show again」 and ‹ match; only the button's casing differs. The spec states the text, so RD (text rule). PM-only: the Design does not draw the Intro Demo. The Launcher still has no 「AI Magic」 / 「Hair Color」 card (CMS layout, R2 O-2, not raised): the run entered from AI Photos.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] AI_Hair_Color: Intro Demo button reads 「Try now」, not 「Try Now」
```

**Description:**

```
Repro Steps:
1. Launch the APP on an install that has not opened AI Hair Color yet
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Read the button of the Intro Demo
5. Check the result

Result:
The Intro Demo's button reads 「Try now」 (lower-case n).
摘要：Intro Demo 按鈕文字為「Try now」，n 為小寫。
{20.19.0_hcc31_intro_try_now.jpg}

Expect Result:
The button reads 「Try Now」 as the PM spec's Intro Demo.
摘要：按鈕文字應為「Try Now」。

Note:
Device: Google Pixel 8a / Android 16
Spec Link: AI Hair Color Custom PM Figma (26 11E AI Hair Color Custom), Spec - Flow board, Intro Demo -
https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3287-93
<Claude Reviewed>
```

**Images:** `20261120_eBug_drafts_AI-Hair-Color-Custom-R3_20.19.0_images/01_ISS-HCC-31/`

---

## 2. ISS-HCC-32 — With Solid the Highlight Color row stays on screen greyed out instead of being hidden  ·  Class: Functional  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-024, TC-029  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-027 (PM Spec - UI panel_solid_color 3327:950, D6-04: solid_color takes one colour, only the Base Color row shows) and the user's ruling REQ-009 (2026-11-18, R2 ISS-HCC-19: 「隱藏就好」, hide the row). On the Pixel 8a, same build 90201901, the Highlight row stays with its title and 8 dimmed circles (custom_highlight_title still in the page source); switching back to Ombre re-enables it with the pink kept (TC-029 holds otherwise). R2 on the S23 hid the row on the same build, so this may be server config or device-dependent (O-1). The Design 4-hair_color_case2-1_toast 929:1901 draws the greyed row; the ruling chose hiding over it, so RD should align the app (or PM change the ruling).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] AI_Hair_Color: Custom panel: Solid leaves the Highlight Color row greyed out instead of hiding it
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Tap a portrait photo with one clear, front-facing face
5. Tap Custom in the swatch row
6. Tap Ombre in Style
7. Tap the dark brown swatch in Base Color
8. Tap the pink swatch in Highlight Color
9. Tap Solid in Style
10. Check the result

Result:
The 「Highlight Color」 row stays on screen greyed out (title and dimmed circles), not hidden.
摘要：選 Solid 後 Highlight Color 列仍顯示（灰階停用），未隱藏。
{20.19.0_hcc32_solid_highlight_row_greyed.jpg} {20.19.0_hcc32_ombre_row_enabled_again.jpg}

Expect Result:
Only the 「Base Color」 row shows; the 「Highlight Color」 row is hidden (PM D6-04, ruling REQ-009).
摘要：選 Solid 時應只顯示 Base Color 列，Highlight Color 列隱藏。

Note:
Device: Google Pixel 8a / Android 16
Spec Link: AI Hair Color Custom PM Figma (26 11E AI Hair Color Custom), panel_solid_color (NEW) frame, Spec - UI (D6-04) -
https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3327-950
Related: R2 ISS-HCC-19 (held 2026-11-18 with the ruling 「隱藏就好」, when the app hid the row)
<Claude Reviewed>
```

**Images:** `20261120_eBug_drafts_AI-Hair-Color-Custom-R3_20.19.0_images/02_ISS-HCC-32/`

---

## 3. ISS-HCC-33 — PM decision: an applied Custom cell keeps its unset look instead of showing the chosen colours  ·  Class: UX  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-038, TC-041, TC-042  ·  **Reproduce:** 3/3  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-044 (PM Spec - UI collapsed_applied 3330:512, D6-08: after collapsing, the Custom cell shows the two colours the user chose) against the PM mockups (a pencil icon) and the Design (only the unset cell, orange gradient with a magic wand): Q-2, open. On 90201901 the applied Custom cell is selected but keeps the unset gradient + wand after every collapse (TC-038), after picking a template (TC-041) and after the user's own overwrite (TC-042); the settings themselves are kept and reopen correctly. PHA262026P0115 (closed 2026-11-19 to this build) fixed the selection and the Custom generation; its own QA note left the cell's look to Q-2, so this is not the closed ticket back but the open question, filed to PM for a decision (2026-11-11 rule). A user cannot tell from the row what Custom holds, so [UX].

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UX] AI_Hair_Color: Custom cell keeps its unset look after applying, not the chosen colours — PM to decide
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Tap a portrait photo with one clear, front-facing face
5. Tap Custom in the swatch row
6. Tap Solid in Style
7. Tap the sand swatch in Base Color
8. Drag the panel's grab handle down
9. Check the result

Result:
The panel closes and Custom is selected, but its cell still shows the unset orange gradient with the magic wand.
摘要：套用後 Custom 格仍為未設定外觀（漸層＋魔術棒），未顯示所選兩色。
{20.19.0_hcc33_custom_cell_unset_solid_sand.jpg} {20.19.0_hcc33_custom_cell_unset_ombre.jpg}

Expect Result:
PM to decide the applied cell's look: the two chosen colours (D6-08), a pencil (PM mockup) or unchanged (Design).
摘要：請 PM 決定套用後 Custom 格的外觀（顯示兩色、鉛筆圖示或不變）。

Note:
Device: Google Pixel 8a / Android 16
Spec Link: AI Hair Color Custom PM Figma (26 11E AI Hair Color Custom), collapsed_applied (NEW) frame, Spec - UI (D6-08) -
https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3330-512
Basis: External — the PM note (two colours), the PM mockups (pencil) and the Design (unset cell) disagree, Q-2; PM to decide
Related: Q-2; PHA262026P0115 (closed 2026-11-19; its note left the cell's look to Q-2)
<Claude Reviewed>
```

**Images:** `20261120_eBug_drafts_AI-Hair-Color-Custom-R3_20.19.0_images/03_ISS-HCC-33/`

---

## 4. ISS-HCC-34 — A Solid template generation takes about 35 s, not the spec's about 15 s  ·  Class: Functional  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-078  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-048 (10/E Spec - UI 3030:300, D1-03: sync short task, about 15 s, the user waits in place). 「Soft Black」 (first template; no 「Platinum」 on this build, ISS-HCC-35) on the Pexels portrait: 34.4 s and 36.0 s from Generate to AIHairColor_Generate_Status succeed (O-3). R2 on the S23 timed the same template at 16.2 s on the same build two days earlier, so the slowdown is server-side or in the template model (Test Server; KP-070). A wait is RD (overlay rule 5); the run queued it as a question because the cause may be the test server's load.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] AI_Hair_Color: Solid template 「Soft Black」 takes about 35 s to generate, not about 15 s
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Tap Stock
5. Tap Pexels
6. Search 「woman portrait」
7. Tap the portrait of a woman in a knitted hat
8. Tap Soft Black in the Solid row
9. Tap Generate
10. Wait for the result
11. Check the result

Result:
The result shows after 34.4 s (second try 36.0 s).
摘要：Soft Black 模板生成約 35 秒（34.4 / 36.0 秒），非 spec 的約 15 秒。
{20.19.0_hcc34_soft_black_result_1.jpg} {20.19.0_hcc34_soft_black_result_2.jpg} {20.19.0_hcc34_log.txt}

Expect Result:
A template result shows after about 15 s (10/E D1-03).
摘要：模板生成應約 15 秒完成。

Note:
Device: Google Pixel 8a / Android 16
Spec Link: AI Hair Color PM Figma (26 10E AI Hair Color v2, cited by the Custom page), Spec - UI, sync short task D1-03 (about 15 s) -
https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3030-300
Related: O-3; R2 TC-078 16.2 s on the S23
<Claude Reviewed>
```

**Images:** `20261120_eBug_drafts_AI-Hair-Color-Custom-R3_20.19.0_images/04_ISS-HCC-34/`

---

## 5. ISS-HCC-35 — PM decision: the first Solid template is 「Soft Black」, not the spec's 「Platinum」  ·  Class: UI  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-017  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-016 / R-017 (the PM page and the Design 4-hair_color 686:1427 draw 「Custom」 then 「Platinum」 first, selected on entry). On the Pixel 8a the Solid row is Custom, Soft Black (selected), Cocoa (crown), Hazelnut, Silver, Espresso…; no 「Platinum」. The template list comes from the CMS, so the mockup name may be a placeholder. Re-offered: R2 ISS-HCC-27 was held on 2026-11-18 with no reason; hold again if that decision stands (then the table's TC-017 / TC-078 should name the first template, not Platinum).

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
4. Tap a portrait photo with one clear, front-facing face
5. Read the swatch row of the Solid tab
6. Check the result

Result:
The row is Custom, Soft Black (selected), Cocoa, Hazelnut, Silver, Espresso; there is no 「Platinum」.
摘要：Solid 第一個模板為 Soft Black，沒有 spec 的 Platinum。
{20.19.0_hcc35_first_template_soft_black.jpg}

Expect Result:
PM to confirm the first template: 「Platinum」 (spec) or 「Soft Black」 (CMS today); the spec or the CMS then follow it.
摘要：請 PM 確認第一個模板應為 Platinum 或 Soft Black。

Note:
Device: Google Pixel 8a / Android 16
Spec Link: AI Hair Color Design Figma (Hair, 261005_AI_hair_color page), 4-hair_color frame (swatch row) -
https://www.figma.com/design/2VOqiPxBCISkob7wbM9hXD/Hair?node-id=686-1427
Related: Q-2; R2 draft ISS-HCC-27 (held 2026-11-18, no reason)
<Claude Reviewed>
```

**Images:** `20261120_eBug_drafts_AI-Hair-Color-Custom-R3_20.19.0_images/05_ISS-HCC-35/`

---

## 6. ISS-HCC-36 — PM decision: the two split-dye styles have photo thumbnails, not plain-colour ones  ·  Class: UI  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-022  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-025 (PM page: the split-dye styles get plain-colour thumbnails, placeholders until art). 「Half-and-half」 and 「Split-dye」 show model-photo thumbnails like the other 9 styles; the 11 styles and the crowns (Balayage, Face framing, Bangs, Half-and-half) hold. Re-offered: R2 ISS-HCC-28 was held on 2026-11-18 with no reason; hold again if that decision stands (then the row should accept the photos).

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
4. Tap a portrait photo with one clear, front-facing face
5. Tap Custom in the swatch row
6. Swipe the Style row to its end
7. Check the result

Result:
「Half-and-half」 and 「Split-dye」 have model-photo thumbnails.
摘要：兩個 split-dye style 縮圖為模特兒照片，非 spec 的純色縮圖。
{20.19.0_hcc36_split_dye_thumbnails.jpg}

Expect Result:
PM to confirm the thumbnails: plain-colour (spec) or the photos (app); the spec then follows it.
摘要：請 PM 確認 split-dye 縮圖應為純色或照片。

Note:
Device: Google Pixel 8a / Android 16
Spec Link: AI Hair Color Design Figma (Hair, 261005_AI_hair_color page), 4-hair_color_case1_no_style frame -
https://www.figma.com/design/2VOqiPxBCISkob7wbM9hXD/Hair?node-id=894-1474
Related: Q-6; R2 draft ISS-HCC-28 (held 2026-11-18, no reason)
<Claude Reviewed>
```

**Images:** `20261120_eBug_drafts_AI-Hair-Color-Custom-R3_20.19.0_images/06_ISS-HCC-36/`

---

# Not raised (observations, for the record)

| Item | What was seen | Why not raised |
|---|---|---|
| O-1 | Custom panel differs from R2 on the same build: rows disabled before a style, no ⌄, no 「Both … required.」 hint, palette pick adds a ringed circle. | Solid's greyed row is ISS-HCC-32; the rest matches the Design / rulings (P0112, P0127 symptoms gone; Q-17; ruling: no toast or hint needed). |
| O-2 | First eyedropper sample on the hair edge set a near-white colour; the second read the hair correctly. | 1 of 2 samples, on an edge pixel; R2 saw something similar. Watch next round; not raised. |
| O-3 | Soft Black template wait 34.4 / 36.0 s. | ISS-HCC-34. |
| O-4 | After ✓, the new Edit Room's Home asks 「Discard changes?」. | Edit Room behaviour, outside this feature. |
| O-5 | During a regeneration the disabled button keeps the text 「Retry」. | Script note (waits use the log). |
| O-6 | One extra Bangs generation from a script mis-step. | Test-run slip, not the app. |
| O-7 | Every Custom generation logs the same Mixpanel style Style_010_Custom_HairColor_gpt-image-2.5-sunburst. | No tracking rule in the spec for the pattern; noted for RD in report.md. |
| Blocked (13) | 3 defect, 4 observability, 6 test-data | No verdict; reasons in report.md. TC-006 / TC-087 / TC-007 are blocked upstream of TC-005 (filed PHA262026P0110). |

# Reconciliation against the run

18 Fail (15 defect, 3 question), 13 Blocked, 0 Not run, 7 observations (O-1 … O-7).

| Item | Result | Disposition | Became |
|---|---|---|---|
| TC-001 | Fail | defect | 1. ISS-HCC-31 |
| TC-005 | Fail | defect | dedupe — PHA262026P0110 (still failing) |
| TC-012 | Fail | defect | dedupe — PHA262026P0110 (still failing) |
| TC-015 | Fail | defect | dedupe — PHA262026P0110 (still failing) |
| TC-017 | Fail | question | 5. ISS-HCC-35 |
| TC-022 | Fail | question | 6. ISS-HCC-36 |
| TC-024 | Fail | defect | 2. ISS-HCC-32 |
| TC-029 | Fail | defect | 2. ISS-HCC-32 |
| TC-038 | Fail | defect | 3. ISS-HCC-33 |
| TC-039 | Fail | defect | dedupe — PHA262026P0128 (filed R2, PM deciding) |
| TC-041 | Fail | defect | 3. ISS-HCC-33 |
| TC-042 | Fail | defect | 3. ISS-HCC-33 |
| TC-045 | Fail | defect | dedupe — PHA262026P0116 (no text) and PHA262026P0149 (panel collapses on Generate) |
| TC-057 | Fail | defect | dedupe — PHA262026P0118 (still failing) |
| TC-046 | Fail | defect | dedupe — PHA262026P0116 (still failing) |
| TC-047 | Fail | defect | dedupe — PHA262026P0149 (panel collapses on Generate, PM) |
| TC-040 | Fail | defect | dedupe — PHA262026P0116 (still failing); P0115 generation part fixed |
| TC-078 | Fail | question | 4. ISS-HCC-34 |
| O-1 | observation | — | not raised |
| O-2 | observation | — | not raised |
| O-3 | observation | — | not raised |
| O-4 | observation | — | not raised |
| O-5 | observation | — | not raised |
| O-6 | observation | — | not raised |
| O-7 | observation | — | not raised |

Filing order by severity: **2**, **3**, **4**, **5**, **6**, **1**. Nothing is filed until the review page's decisions come back.
