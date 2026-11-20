# Batch Editing (Android) — eBug drafts, run R3 (table v7, full run), PhotoDirector 20.19.0 build v202611111946 (90201900)

**Source:** spec-casebook run `library/phd/batch-editing/android/runs/2026-11-13-r3/` — phase R3 of draft `drafts/20261112-150000` (approved table v7, all 170 rows), 2026-11-13 on Samsung Galaxy S23 (SM-S9110, Android 16) through Appium / UiAutomator2, Test Server, Premium through the debug switch (Free for R3-g). Build 20.19.0.v202611111946, SR PHA261029-01, TR261111-0042. Tally: 144 Pass, 16 Fail, 10 Blocked, 0 Not run.

**Status:** nothing filed, uploaded or commented. Filing defaults: Creator WILLY_WU, [AIAgent], API from the newest filed batch (2026-11-10-r1, `ebug-defaults.ts`); TRCode TR261111-0042 (the build these findings were verified on; the 2026-11-10-r1 batch was on TR261106-0051). All for the reviewer to confirm. Dedupe is read-only, Android pool only (dedupe per OS): see `dedupe.txt`.

Rules: reviewer rules — one action per Repro step, a Spec Link on every entry (URL on its own line), at least one image per entry, no video; no failure-related entry, so no log. RD defects are `[AIAgent]`; open questions the run cannot settle go to PM (BugBelong PM): `[AIAgent][UX]` for user-experience decisions (rule restored 2026-11-13), `[AIAgent][UI]` for undecided text (never Doc, user 2026-11-11). Feature name `Batch_Editing:` (REQ-008). Spec basis check (REQ-055) done per entry.

**What is drafted:** 7 entries (ISS-BEA-12, 14…19; R2's ISS-BEA-12 and 14 were never filed and are carried forward, ISS-BEA-13 is fixed on this build) from 11 Fail rows: 1 RD defect (2 rows), 6 PM decisions. 5 Fail rows repeat existing Android tickets and are only in `dedupe.txt`.

Legend — Class: Functional / UI / UX · Severity: S1 critical and blocking only, S2 important, S3 moderate · Owner: RD / PM.

---

## 1. ISS-BEA-12 — 「All」 stays enabled on a photo with no change of its own while another photo has an unapplied change  ·  Class: Functional  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-162, TC-164  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.v202611111946 (90201900)

> **QA note — not pasted into eBug.** Carried from R2's unfiled ISS-BEA-12, narrowed to the part that still fails on the TR261111-0042 build. Fixed on this build (Pass in R3): 「All」 greyed on entering (TC-153, TC-164 step 1), after the apply with no toast on a disabled tap (TC-042, TC-075), after Redo (TC-063, TC-165) and after a size-only change (TC-163). Still failing: on a photo with no change of its own, while another photo has an unapplied change, 「All」 stays normal — white icon and text, `els` batchApplyToAllBtn with no `disabled` flag (TC-164 step 3 Adjustment, photo 1 Exposure 「0.6」 by thumb drag; TC-162 Crop & Rotate, photo 1 3:2 「910 x 605」, photo 2 「1067 x 1600」). Back on photo 1 it is normal, as expected. R-234 (PM Figma DR-04 【NEW】 「切換照片依該張」). Spec basis checked: the 【NEW】 list on pm-ui-3 is the decided rule (Q-16 answered, REQ-011); no newer frame draws otherwise. Not in PHA262026P0057–P0061.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] Batch_Editing: 「All」 stays enabled on a photo with no change of its own after switching photos
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap Edit on the Launcher
3. Tap Batch
4. Select 12 photos
5. Tap Next
6. Tap Adjustments
7. Drag the Exposure slider to 0.6
8. Tap photo 2's thumbnail
9. Check 「All」 at the top right

Result:
On photo 2 (Exposure 0, no change of its own) 「All」 stays enabled; it follows photo 1's unapplied change.
摘要：切到沒有任何修改的第 2 張時，All 仍為可按，跟著第 1 張未套用的修改走。
{20.19.0_bea12_adjust_photo2_no_change_all_enabled.jpg} {20.19.0_bea12_crop_photo2_no_change_all_enabled.jpg}

Expect Result:
On switching photos 「All」 is set by that photo's own unapplied changes: disabled on photo 2.
摘要：切換照片時 All 依該張自己的未套用修改決定：第 2 張沒有修改，All 應為停用。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Related: the same in the Crop & Rotate room (3:2 on photo 1, then photo 2)
Spec Link: Batch Editing PM Figma, pm-ui-3 board (Batch Edit Room · Crop & Rotate / Adjustment, 【NEW】 Apply to all normal / disabled states, DR-04: 切換照片依該張) -
https://www.figma.com/design/iWlQTjlmfykHfmlNvg9J4p/Batch-Editing?node-id=16-13767
<Claude Reviewed>
```

**Images:** `20261113_eBug_drafts_Batch-Edit-R3_20.19.0_images/01_ISS-BEA-12/`

---

## 2. ISS-BEA-14 — PM decision: one Undo after an edit + 「All」 reverts the 11 other photos but keeps the current photo's own edit  ·  Class: UX  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-062, TC-076  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.v202611111946 (90201900)

> **QA note — not pasted into eBug.** Carried from R2's unfiled ISS-BEA-14 (R1 held it as a PM question); same on the TR261111-0042 build on the S23. Crop TC-062: 3:2 + 「All」 (「Applied to 11 photos」), one Undo: photo 2 「1067 x 1600」 and photo 4 「1600 x 1066」 back, photo 1 still 「910 x 605」, Undo still enabled. Adjustment TC-076: Exposure 「0.6」 + 「All」, one Undo (「Undo: Apply to all」): photos 2–6 back to their entry values, photo 1 keeps 「0.6」. R-087 / R-105 say only that Apply to all is one step; R-099 makes a single edit that photo's own step, so the app may be intended: an open question, filed to PM (user, 2026-11-11), Type UX (how Undo feels). R2's empty first Undo from a no-change 「All」 is gone on this build. The TC-076 image shows photo 1 (selected, still bright) beside photo 2 (back to its original).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UX] Batch_Editing: One Undo after an edit and 「All」 keeps the current photo's own edit
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap Edit on the Launcher
3. Tap Batch
4. Select 12 photos
5. Tap Next
6. Tap Crop & Rotate
7. Tap 3:2
8. Tap All
9. Tap Undo
10. Check photo 1 and photo 2

Result:
One Undo reverts the 11 other photos only; photo 1 keeps 3:2 (「910 x 605」) until a 2nd Undo.
摘要：一次 Undo 只還原其他 11 張，目前這張保留 3:2，需再按一次。
{20.19.0_bea14_crop_undo1_photo1_keeps_3x2.jpg} {20.19.0_bea14_adjust_undo_photo1_keeps_exposure.jpg}

Expect Result:
PM to decide whether one Undo also reverts the current photo's own edit (all 12 together) or not.
摘要：請 PM 決定一次 Undo 是否連目前這張的修改一起還原（12 張同時）。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Related: the same in the Adjustment room (Exposure, then All, then Undo)
Spec Link: Batch Editing PM Figma, pm-ui-3 board (Batch Edit Room · Crop & Rotate / Adjustment · applied, DR-05b) -
https://www.figma.com/design/iWlQTjlmfykHfmlNvg9J4p/Batch-Editing?node-id=16-13767
<Claude Reviewed>
```

**Images:** `20261113_eBug_drafts_Batch-Edit-R3_20.19.0_images/02_ISS-BEA-14/`

---

## 3. ISS-BEA-15 — PM decision: Crop & Rotate sizes a large photo from a 2560 px copy and accepts 147 px, not Section 3's original-size range  ·  Class: UX  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-049, TC-057, TC-058  ·  **Reproduce:** 3/3  ·  **Verified on:** 20.19.0.v202611111946 (90201900)

> **QA note — not pasted into eBug.** Held as a PM question in R1 (O-5, O-7) and never filed; same on the TR261111-0042 build. Stand-in ④ (2730 × 1535, 16:9) is held in the Crop room as 「2560 x 1439」 (a 2560 px long-side cap): its 3:4 box reads 「1075 x 1435」 (TC-049; the position rule holds), the Custom resolution dialog refuses 3000 × 3000 with 「Width should be between 147 and 2560. Please try again.」 (TC-057) and accepts 237 × 237 (TC-058, minimum 147). Section 3's 「✅ 結論」 (R-066, R-060) computes from the original: 238 px up to the photo's own width / height, 3:4 box 1151 × 1535. Whether PhD keeps the 2560 cap and the 147 minimum is a product decision: filed to PM (open questions to PM, user 2026-11-11), Type UX. The toast copy itself is Q-6, ISS-BEA-16. The saved Square 1434 × 1435 is PHA262026P0060 (TC-060, deduped).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UX] Batch_Editing: Crop sizes use a 2560 px copy and a 147 px minimum, not Section 3's range
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap Edit on the Launcher
3. Tap Batch
4. Select 4 photos (the last one 2730 x 1535, 16:9)
5. Tap Next
6. Tap Crop & Rotate
7. Tap photo 4's thumbnail
8. Check the size label
9. Tap the pencil next to the size
10. Tap the link icon
11. Enter 237 in Width
12. Enter 237 in Height
13. Tap OK
14. Check the size label

Result:
Photo 4 (2730 x 1535) reads 「2560 x 1439」, its 3:4 box 「1075 x 1435」; 237 x 237 is accepted (minimum 147).
摘要：2730x1535 的照片顯示為 2560x1439，3:4 框 1075x1435；237x237 可接受。
{20.19.0_bea15_crop_photo4_3x4_1075x1435.jpg} {20.19.0_bea15_crop_custom_237x237_accepted.jpg} {20.19.0_bea15_crop_custom_toast_147_2560.jpg}

Expect Result:
PM to decide the range: Section 3 gives 238 px up to the photo's own size (3:4 box 1151 x 1535).
摘要：請 PM 決定範圍：Section 3 結論為 238 px 到照片原尺寸（3:4 框 1151 x 1535）。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Related: the out-of-range toast reads 「Width should be between 147 and 2560. Please try again.」 (3000 x 3000 refused)
Related: PHA262026P0060 (Square on this photo saves 1434 x 1435)
Spec Link: Batch Edit PM spec (Section 3 · 美圖 Apply to all 實測.pdf), meitu-conclusion (✅ 結論: PhD crop · Apply to all rules) and meitu-cases C12 board (238 px up to the photo's own width / height; box sizes from each original) - no Figma URL for this PDF
Spec Link: Batch Editing PM Figma, pm-ui-3 board (Batch Edit Room · Crop & Rotate · default, size label and pencil) -
https://www.figma.com/design/iWlQTjlmfykHfmlNvg9J4p/Batch-Editing?node-id=16-14279
<Claude Reviewed>
```

**Images:** `20261113_eBug_drafts_Batch-Edit-R3_20.19.0_images/03_ISS-BEA-15/`

---

## 4. ISS-BEA-16 — PM decision: the Custom resolution out-of-range toast names only the width, and PhD's copy is undecided (Q-6)  ·  Class: UI  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-057  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.v202611111946 (90201900)

> **QA note — not pasted into eBug.** Q-6 (PhD toast copy for an out-of-range pixel value) is still open in table v7; Section 3 quotes only Meitu's 「Width and height exceed the range」. The app names only the width although both values (3000 × 3000, link off) are out of range. Text the spec has not decided → PM, Class UI (text rule, user 2026-11-11). Not answered by any ruling or ticket (PHA262026P0061 is the 21st-photo toast).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] Batch_Editing: Custom resolution out-of-range toast names only the width
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap Edit on the Launcher
3. Tap Batch
4. Select 4 photos (the last one 2730 x 1535, 16:9)
5. Tap Next
6. Tap Crop & Rotate
7. Tap photo 4's thumbnail
8. Tap the pencil next to the size
9. Tap the link icon
10. Enter 3000 in Width
11. Enter 3000 in Height
12. Tap OK
13. Check the toast

Result:
Toast 「Width should be between 147 and 2560. Please try again.」; the height (also out of range) is not named.
摘要：提示只寫 Width 的範圍，高度同樣超出卻沒提到。
{20.19.0_bea16_crop_custom_toast_width_only.jpg}

Expect Result:
PM to decide the toast copy for width and height (Meitu: 「Width and height exceed the range」, range under the field).
摘要：請 PM 決定寬高超出範圍時的提示文案（Q-6）。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Related: ISS-BEA-15 (the range itself)
Spec Link: Batch Edit PM spec (Section 3 · 美圖 Apply to all 實測.pdf), meitu-cases C12 board (Meitu toast 「Width and height exceed the range」; PhD copy open, Q-6) - no Figma URL for this PDF
<Claude Reviewed>
```

**Images:** `20261113_eBug_drafts_Batch-Edit-R3_20.19.0_images/04_ISS-BEA-16/`

---

## 5. ISS-BEA-17 — PM decision: ✕ or Back after a finished batch AI Enhance asks 「Discard changes?」 instead of returning with the results kept  ·  Class: UX  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-100, TC-142  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.v202611111946 (90201900)

> **QA note — not pasted into eBug.** Held as a PM question in R1 and never filed; same on the TR261111-0042 build. After the 12-photo batch finished, ✕ (TC-100) and system Back (TC-142) open 「Discard changes?」 「All your existing changes will be lost.」 「Keep」 / 「Discard」; 「Keep」 stays on AI Enhance with the results, only ✓ returns with them. R-130 (PM flow-ai-enhance) says ✕ returns to Batch Edit Room keeping the results; the Design draws the Discard Dialog over the AI Enhance page (Q-19, open). Design-first (user, 2026-11-13) would favour the dialog, but the Design frames carry no date (Q-12), so the order cannot be settled from the files: filed to PM, Type UX. The second Back not closing the dialog is the open-ticket behaviour of PHA262026P0059 (not drafted again).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UX] Batch_Editing: ✕ after batch AI Enhance asks 「Discard changes?」, not keep the results
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap Edit on the Launcher
3. Tap Batch
4. Select 12 photos
5. Tap Next
6. Tap AI Enhance
7. Tap Enhance
8. Tap Enhance in the dialog
9. Wait until all 12 photos finish
10. Tap ✕
11. Check the result

Result:
「Discard changes?」 「All your existing changes will be lost.」 Keep / Discard opens; system Back does the same.
摘要：✕ 或系統返回鍵開出「Discard changes?」對話框，而不是保留結果回到 Batch Edit Room。
{20.19.0_bea17_enhance_done_x_discard_dialog.jpg} {20.19.0_bea17_enhance_done_back_discard_dialog.jpg}

Expect Result:
PM to decide: PM says ✕ returns to Batch Edit Room with the results kept; the Design draws this dialog (Q-19).
摘要：請 PM 決定：PM 寫 ✕ 保留結果返回，Design 畫了 Discard 對話框（Q-19）。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Related: a second system Back leaves the dialog open, as PHA262026P0059 (Discard dialog from Home)
Spec Link: Batch Editing PM Figma, pm-ui-5 board (Batch Edit Room · AI Enhance · result_success, R-130: ✕ returns with the results kept) -
https://www.figma.com/design/iWlQTjlmfykHfmlNvg9J4p/Batch-Editing?node-id=16-15034
Spec Link: Batch Edit Design Figma, Discard dialog frame (Discard Dialog drawn over the AI Enhance page) -
https://www.figma.com/design/qZXJfrM5gb5g4tFoCIS1YU/Batch-Edit?node-id=110-4532
<Claude Reviewed>
```

**Images:** `20261113_eBug_drafts_Batch-Edit-R3_20.19.0_images/05_ISS-BEA-17/`

---

## 6. ISS-BEA-18 — PM decision: Batch Save page title reads 「Saved 12 photos」 (PM) while the Design draws 「Save 12 photos」 (Q-20)  ·  Class: UI  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-128  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.v202611111946 (90201900)

> **QA note — not pasted into eBug.** Held as a PM question in R1 (O-16) and never filed; same on this build. The two sheets disagree and the Design frames carry no date (Q-12), so the Design-first order (user, 2026-11-13) cannot be applied from the files; text whose spec source disagrees goes to PM, never Doc (user, 2026-11-11). Class UI.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] Batch_Editing: Batch Save title 「Saved 12 photos」 differs from Design 「Save 12 photos」
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap Edit on the Launcher
3. Tap Batch
4. Select 12 photos
5. Tap Next
6. Tap Save at the top right
7. Check the page title

Result:
The Batch Save page title reads 「Saved 12 photos」.
摘要：批次儲存頁標題為「Saved 12 photos」。
{20.19.0_bea18_save_page_title_saved_12.jpg}

Expect Result:
PM to decide the title: Design save2 draws 「Save 12 photos」, the PM board writes 「Saved 12 photos」 (Q-20).
摘要：請 PM 決定標題：Design 為 Save，PM 為 Saved（Q-20）。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: Batch Edit Design Figma, save2 frame (Batch Save page title 「Save 12 photos」) -
https://www.figma.com/design/qZXJfrM5gb5g4tFoCIS1YU/Batch-Edit?node-id=57-6001
Spec Link: Batch Editing PM Figma, pm-ui-8 board (Batch Save Page · saved, 「Saved 12 photos」, D1-07) -
https://www.figma.com/design/iWlQTjlmfykHfmlNvg9J4p/Batch-Editing?node-id=16-15383
<Claude Reviewed>
```

**Images:** `20261113_eBug_drafts_Batch-Edit-R3_20.19.0_images/06_ISS-BEA-18/`

---

## 7. ISS-BEA-19 — PM decision: as a Free user the Batch Save page has no native ad card, while the single Save & Share page has one  ·  Class: UX  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-135  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.v202611111946 (90201900)

> **QA note — not pasted into eBug.** Held as a PM question in R1 (O-19) and never filed; same on this build. Free tier (debug 「Set to subscriber」 off): 1st batch save of 5 → interstitial (Dance AI) → 「Saved 5 photos」; 2nd → Premium IAP flyer → 「Saved 5 photos」; neither Batch Save page has an ad_container. Single save (Edit › Single): Rate Us, then 「Save & Share」 with a native AdMob card under 「Share to」 (savePageAdMobNativeContentAdView). R-158 says ads appear as usual; neither PM nor the Design draws an ad slot on the Batch Save page: filed to PM, Type UX (monetisation placement).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UX] Batch_Editing: Free user Batch Save page has no native ad card, unlike single save
```

**Description:**

```
Repro Steps:
1. Launch the APP as a Free user
2. Tap Edit on the Launcher
3. Tap Batch
4. Select 5 photos
5. Tap Next
6. Tap Save at the top right
7. Close the ad or IAP page
8. Check the Batch Save page

Result:
The Batch Save page shows the 5 photos and 「Edit Next Batch」 only; no native ad card (the single save page has one).
摘要：批次儲存頁只有照片與 Edit Next Batch，沒有原生廣告卡；單張儲存頁的 Share to 下方有。
{20.19.0_bea19_batch_save_page_no_ad.jpg} {20.19.0_bea19_single_save_page_native_ad.jpg}

Expect Result:
PM to decide whether the Batch Save page carries the save page's native ad (R-158: ads appear as usual).
摘要：請 PM 決定批次儲存頁是否要放單張儲存頁的原生廣告（R-158：廣告照常出現）。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Related: interstitial ads and the Premium IAP flyer do appear after batch saves
Spec Link: Batch Editing PM Figma, pm-ui-8 board (Batch Save Page · saved, R-158: IAP flyers and ads appear as usual; no ad slot drawn) -
https://www.figma.com/design/iWlQTjlmfykHfmlNvg9J4p/Batch-Editing?node-id=16-15383
<Claude Reviewed>
```

**Images:** `20261113_eBug_drafts_Batch-Edit-R3_20.19.0_images/07_ISS-BEA-19/`

---

## Deduped — repeats of existing Android tickets (not drafted; `dedupe.txt`)

| Case | Ticket |
|---|---|
| TC-012 | PHA262026P0061 (Assigned) |
| TC-060 | PHA262026P0060 (RDResolved) |
| TC-110 | PHA262026P0057 (RDResolved) |
| TC-144 | PHA262026P0058 (RDResolved) |
| TC-145 | PHA262026P0059 (RDResolved) |

## Not raised (observations, for the record)

- O-1: Help (i) hidden on the Adjustment Details tab (likely no tutorial for Details); not a row, not raised.
- O-2: No credit pill on the batch AI Enhance page (R-113 draws none; the Design's pill sits on the Discard frame, Q-19, ISS-BEA-17); not raised.
- O-3: One photo of a 7-photo retry failed with SocketTimeoutException on working Wi-Fi, as R1 O-13; the next retry finished it. Watch, not raised.
- O-4: Picker tray tile for selection #10 showed another picture once while the grid and the room were right; display-only, seen once, not raised.

## Reconciliation against the run (Fail rows)

| Case | Result | Where |
|---|---|---|
| TC-012 | Fail defect | dedupe.txt (PHA262026P0061 (Assigned)) |
| TC-162 | Fail defect | F-1 ISS-BEA-12 |
| TC-062 | Fail question | F-2 ISS-BEA-14 |
| TC-049 | Fail question | F-3 ISS-BEA-15 |
| TC-057 | Fail question | F-3 ISS-BEA-15, F-4 ISS-BEA-16 |
| TC-058 | Fail question | F-3 ISS-BEA-15 |
| TC-060 | Fail defect | dedupe.txt (PHA262026P0060 (RDResolved)) |
| TC-164 | Fail defect | F-1 ISS-BEA-12 |
| TC-076 | Fail question | F-2 ISS-BEA-14 |
| TC-144 | Fail defect | dedupe.txt (PHA262026P0058 (RDResolved)) |
| TC-100 | Fail question | F-5 ISS-BEA-17 |
| TC-142 | Fail question | F-5 ISS-BEA-17 |
| TC-110 | Fail defect | dedupe.txt (PHA262026P0057 (RDResolved)) |
| TC-145 | Fail defect | dedupe.txt (PHA262026P0059 (RDResolved)) |
| TC-128 | Fail question | F-6 ISS-BEA-18 |
| TC-135 | Fail question | F-7 ISS-BEA-19 |

Blocked rows (no verdict, not drafted): TC-152 (observability), TC-096 (observability), TC-101 (observability), TC-102 (observability), TC-160 (observability), TC-103 (observability), TC-104 (observability), TC-105 (observability), TC-109 (observability), TC-136 (test-data).
