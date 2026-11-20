# Batch Editing (Android) — eBug drafts for TR261113-0038, PhotoDirector 20.19.0 build v202611132003 (90201901)

**Source:** re-verification run `library/phd/batch-editing/android/runs/2026-11-17-verify-tr261113-0038/` (verify.md) of the five R3 findings the user approved (`../2026-11-13-r3/decisions.md`), plus the new Crop & Rotate crash. Samsung Galaxy S23 (SM-S9110, Android 16), Test Server, Premium by the debug switch (Free for TC-135).

**Status:** nothing filed, uploaded or commented. Filing: Creator WILLY_WU, [AIAgent], API, TRCode TR261113-0038.

---

## 01. ISS-BEA-12 — 「All」 stays enabled on a photo with no change of its own while another photo has an unapplied change  ·  Class: Functional  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-162, TC-164  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.v202611132003 (90201901)

> **QA note — not pasted into eBug.** Reproduced on v202611132003 (TR261113-0038), 2026-11-17, Premium, Test Server. TC-164: on entering 「All」 is greyed (expected); Exposure 「0.43」 by one thumb drag on photo 1 → 「All」 normal (expected); photo 2 and photo 3 (Exposure 「0」, no change of their own) → 「All」 stays normal, `els` batchApplyToAllBtn with no `disabled` flag (fails R-234); photo 1 again → normal (expected). TC-162: Square on photo 1 (「640 x 640」, no 「All」 tap) → photo 2 (「960 x 640」, Original) and photo 3 (「960 x 1280」, Original) keep 「All」 normal. Square instead of R3's 3:2 because photo 1 of this set is natively 3:2. Same as R3 (v202611111946, TR261111-0042, run 2026-11-13-r3): TC-162 / TC-164 Fail there with 3:2 and Exposure 「0.6」 (R3 images 20.19.0_bea12_*.jpg).

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
7. Drag the Exposure slider to 0.43
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
Related: the same in the Crop & Rotate room (Square on photo 1, then photo 2)
Spec Link: Batch Editing PM Figma, pm-ui-3 board (Batch Edit Room · Crop & Rotate / Adjustment, 【NEW】 Apply to all normal / disabled states, DR-04: 切換照片依該張) -
https://www.figma.com/design/iWlQTjlmfykHfmlNvg9J4p/Batch-Editing?node-id=16-13767
<Claude Reviewed>
```

**Files:** `upload/20.19.0_bea12_adjust_photo2_no_change_all_enabled.jpg`, `upload/20.19.0_bea12_crop_photo2_no_change_all_enabled.jpg`

---

## 02. ISS-BEA-14 — PM decision: one Undo after an edit + 「All」 reverts the 11 other photos but keeps the current photo's own edit  ·  Class: UX  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-062, TC-076  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.v202611132003 (90201901)

> **QA note — not pasted into eBug.** Reproduced on v202611132003 (TR261113-0038), 2026-11-17. Crop TC-062: the room was on photo 3 (「960 x 1280」); Square (「960 x 960」) + 「All」, one Undo: photo 1 back to 「960 x 640」 Original and photo 4 「1280 x 851」 Original, photo 3 still 「960 x 960」 Square, Undo still enabled, 「All」 normal again. Adjustment TC-076: Exposure 「0.43」 + 「All」 (toast 「Applied to 11 photos」), one Undo (toast 「Undo: Apply to all」): photos 2–4 back to Exposure 「0」, photo 1 keeps 「0.43」, 「All」 normal again. Same as R3 (v202611111946, TR261111-0042, run 2026-11-13-r3) (TC-062 with 3:2, TC-076 with 「0.6」; R3 images 20.19.0_bea14_*.jpg). R-087 / R-105 say only that Apply to all is one step; R-099 makes a single edit that photo's own step: open question to PM, Type UX.

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
7. Tap Square
8. Tap All
9. Tap Undo
10. Check the current photo
11. Tap another photo's thumbnail

Result:
One Undo reverts the 11 other photos only; the current photo keeps Square (「960 x 960」) until a 2nd Undo.
摘要：一次 Undo 只還原其他 11 張，目前這張保留 Square，需再按一次。
{20.19.0_bea14_crop_undo1_current_keeps_square.jpg} {20.19.0_bea14_crop_undo1_other_photo_original.jpg} {20.19.0_bea14_adjust_undo_photo1_keeps_exposure.jpg}

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

**Files:** `upload/20.19.0_bea14_crop_undo1_current_keeps_square.jpg`, `upload/20.19.0_bea14_crop_undo1_other_photo_original.jpg`, `upload/20.19.0_bea14_adjust_undo_photo1_keeps_exposure.jpg`

---

## 03. ISS-BEA-15 — PM decision: Crop & Rotate sizes a large photo from a 2560 px copy and accepts 147 px, not Section 3's original-size range  ·  Class: UX  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-049, TC-057, TC-058  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.v202611132003 (90201901)

> **QA note — not pasted into eBug.** Partly re-verified on v202611132003 (TR261113-0038), 2026-11-17. The minimum part still fails Section 3: on stand-in ③ (800 × 800) the Custom resolution dialog accepts 237 × 237 (label 「237 x 237」, no toast; TC-058) and 3000 × 3000 is refused with 「Width should be between 50 and 800. Please try again.」 (TC-057) — the minimum is 50 here (147 on the 2730 px photo in R3), never 238. The 2560 px copy (TC-049, stand-in ④ 2730 × 1535 read as 「2560 x 1439」, 3:4 box 「1075 x 1435」) could not be re-checked: Crop & Rotate crashes when it shows ④ or ① on this build (ISS-BEA-20). R3 evidence for that part: R3 (v202611111946, TR261111-0042, run 2026-11-13-r3), images 20.19.0_bea15_*.jpg. Related: PHA262026P0060 (Square on a 2730 x 1535 photo saves 1434 x 1435). Short Description kept as approved; the reviewer may want to drop 「2560 px copy」 or wait for ISS-BEA-20's fix.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UX] Batch_Editing: Crop custom size accepts 237 x 237, below Section 3's 238 px minimum
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap Edit on the Launcher
3. Tap Batch
4. Select an 800 x 800 photo and a 1576 x 1970 photo (the 800 x 800 one first)
5. Tap Next
6. Tap Crop & Rotate
7. Tap the pencil next to the size
8. Tap the link icon
9. Enter 237 in Width
10. Enter 237 in Height
11. Tap OK
12. Check the size label

Result:
237 x 237 is accepted (「237 x 237」); the range toast reads 50 to 800 for this photo, not 238 px upwards.
摘要：237x237 可接受；此照片的範圍提示為 50 到 800，而非 238 px 起。
{20.19.0_bea15_crop_custom_237x237_accepted.jpg} {20.19.0_bea15_crop_custom_toast_50_800.jpg}

Expect Result:
PM to decide the range: Section 3 gives 238 px up to the photo's own size, computed from the original.
摘要：請 PM 決定範圍：Section 3 結論為 238 px 到照片原尺寸（依原圖計算）。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Related: on the TR261111-0042 build a 2730 x 1535 photo read 「2560 x 1439」 (3:4 box 「1075 x 1435」) and the toast read 「Width should be between 147 and 2560. Please try again.」; on this build that photo cannot be opened in Crop & Rotate (ISS-BEA-20, crash)
Spec Link: Batch Edit PM spec (Section 3 · 美圖 Apply to all 實測.pdf), meitu-conclusion (✅ 結論: PhD crop · Apply to all rules) and meitu-cases C12 board (238 px up to the photo's own width / height; box sizes from each original) - no Figma URL for this PDF
Spec Link: Batch Editing PM Figma, pm-ui-3 board (Batch Edit Room · Crop & Rotate · default, size label and pencil) -
https://www.figma.com/design/iWlQTjlmfykHfmlNvg9J4p/Batch-Editing?node-id=16-14279
<Claude Reviewed>
```

**Files:** `upload/20.19.0_bea15_crop_custom_237x237_accepted.jpg`, `upload/20.19.0_bea15_crop_custom_toast_50_800.jpg`

---

## 04. ISS-BEA-16 — PM decision: the Custom resolution out-of-range toast names only the width, and PhD's copy is undecided (Q-6)  ·  Class: UI  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-057  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.v202611132003 (90201901)

> **QA note — not pasted into eBug.** Reproduced on v202611132003 (TR261113-0038), 2026-11-17, on stand-in ③ (800 × 800) because ④ (2730 × 1535) crashes Crop & Rotate on this build (ISS-BEA-20). Link off, 3000 × 3000, OK: refused, dialog stays, toast 「Width should be between 50 and 800. Please try again.」 (page source Toast node). In R3 (v202611111946, TR261111-0042, run 2026-11-13-r3) on ④ it read 「Width should be between 147 and 2560. Please try again.」 (image 20.19.0_bea16_crop_custom_toast_width_only.jpg). Q-6 still open; text the spec has not decided → PM, Class UI.

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
4. Select an 800 x 800 photo and a 1576 x 1970 photo (the 800 x 800 one first)
5. Tap Next
6. Tap Crop & Rotate
7. Tap the pencil next to the size
8. Tap the link icon
9. Enter 3000 in Width
10. Enter 3000 in Height
11. Tap OK
12. Check the toast

Result:
Toast 「Width should be between 50 and 800. Please try again.」; the height (also out of range) is not named.
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

**Files:** `upload/20.19.0_bea16_crop_custom_toast_width_only.jpg`

---

## 07. ISS-BEA-19 — PM decision: as a Free user the Batch Save page has no native ad card, while the single Save & Share page has one  ·  Class: UX  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-135  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.v202611132003 (90201901)

> **QA note — not pasted into eBug.** Reproduced on v202611132003 (TR261113-0038), 2026-11-17, Free tier (debug 「Set to subscriber」 off; Mine 「Upgrade to Premium!」). 1st batch save of 5 → 「PhotoDirector Premium」 IAP flyer (✕) → 「Saved 5 photos」 / 「Edit Next Batch」, no ad_container even after 10 s; 2nd batch save → 「Rate Us」 (Not Now) → 「Saved 5 photos」, no ad_container (DCIM/PhotoDirector 940 → 945 → 950). Positive control, single save (Edit › Single, Save): interstitial ad (Close) → 「Save & Share」 with a native AdMob card under 「Share to」 (ad_container / savePageAdMobNativeContentAdView, 「Ad Choices Icon」). Same as R3 (v202611111946, TR261111-0042, run 2026-11-13-r3) (images 20.19.0_bea19_*.jpg). Then back to Premium (「Hello VIP!」).

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
Related: the Premium IAP flyer and the Rate Us dialog do appear after batch saves
Spec Link: Batch Editing PM Figma, pm-ui-8 board (Batch Save Page · saved, R-158: IAP flyers and ads appear as usual; no ad slot drawn) -
https://www.figma.com/design/iWlQTjlmfykHfmlNvg9J4p/Batch-Editing?node-id=16-15383
<Claude Reviewed>
```

**Files:** `upload/20.19.0_bea19_batch_save_page_no_ad.jpg`, `upload/20.19.0_bea19_single_save_page_native_ad.jpg`

---

## 08. ISS-BEA-20 — The app crashes when the Batch Crop & Rotate room shows a large photo (1706 x 2559 or 2730 x 1535)  ·  Class: Functional  ·  Severity: S1  ·  Owner: RD

**Report step:** TC-049, TC-057, TC-058  ·  **Reproduce:** 4/4  ·  **Verified on:** 20.19.0.v202611132003 (90201901)

> **QA note — not pasted into eBug.** New on v202611132003 (TR261113-0038), 2026-11-17, Premium, Test Server; 4 of 4 tries, logcat -b crash: (1) 10:06:20 — 4 Section 3 stand-ins ① 1706×2559, ② 1576×1970, ③ 800×800, ④ 2730×1535 in that order (Casebook album), Next, tap Crop & Rotate (room opens on ①) → crash, 「Cannot coerce value to an empty range: maximum 104.21999999999991 is less than minimum 104.21999999999997.」; (2) 10:07:05 — the same again after relaunch → same exception, 「Clear cache for PhotoDirector?」; (3) 10:08:07 — ④ then ③, tap Crop & Rotate (room opens on ④) → crash, 「maximum 310.83187499999997 is less than minimum 310.831875」; (4) 10:08:52 — ③ then ④, Crop & Rotate opens fine on ③ (「800 x 800」), tap ④'s thumbnail → same crash (310.83…). Stack: BatchCropRoomFragment.showPhoto → BatchCropRoomFragment.b0/n0 → crop.a.g → CropRotateImageView.o/C/g → kotlin coerceIn (floating-point min > max). Photos that opened fine: ③ 800×800 and the phone's 960×640 / 960×1280 / 1280×851 gallery photos. In R3 (v202611111946) the same four stand-ins opened in Crop & Rotate (TC-049/057/058 recorded sizes), so a regression on this build. Severity 1 set by the user (「這個crash要發S1」, 2026-11-17); log excerpt scanned, no tokens.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] Batch_Editing: App crashes when Crop & Rotate shows a 2730 x 1535 or 1706 x 2559 photo
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap Edit on the Launcher
3. Tap Batch
4. Select a 2730 x 1535 photo and an 800 x 800 photo (the 2730 x 1535 one first)
5. Tap Next
6. Tap Crop & Rotate

Result:
PhotoDirector closes at once and the system shows 「Clear cache for PhotoDirector?」.
摘要：點 Crop & Rotate 後 App 立即閃退（IllegalArgumentException）。
{20.19.0_bea20_crop_room_crash_clear_cache_dialog.jpg} {20.19.0_bea20_batch_room_before_crop_tap.jpg} {20.19.0_bea20_crop_room_crash_log.txt}

Expect Result:
The Crop & Rotate room opens on the photo and shows its size label; no crash.
摘要：Crop & Rotate 正常開啟並顯示照片與尺寸，不閃退。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Related: also when the room opens on a 1706 x 2559 photo, and when the room is open on the 800 x 800 photo and the 2730 x 1535 photo's thumbnail is tapped
Related: the same photos opened without a crash on the TR261111-0042 build (v202611111946)
Spec Link: Batch Editing PM Figma, pm-ui-3 board (Batch Edit Room · Crop & Rotate · default, size label and pencil) -
https://www.figma.com/design/iWlQTjlmfykHfmlNvg9J4p/Batch-Editing?node-id=16-14279
<Claude Reviewed>
```

**Files:** `upload/20.19.0_bea20_crop_room_crash_clear_cache_dialog.jpg`, `upload/20.19.0_bea20_batch_room_before_crop_tap.jpg`, `upload/20.19.0_bea20_crop_room_crash_log.txt`

---
