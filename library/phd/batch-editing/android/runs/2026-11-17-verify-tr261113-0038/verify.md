# Batch Editing Android — re-verification on 20.19.0.v202611132003 (TR261113-0038), 2026-11-17

User 2026-11-17: 「有新版本了 請先在新版本上面驗證過 還是有問題就直接發去新版本上」. The five R3 findings approved for filing
(`ebugs/2026-11-13-r3/upload/bodies.json`) were re-run with the rows behind them (Precondition / Action / Expected
from `cases.csv`).

## Setup
- Phone: Samsung Galaxy S23 (SM-S9110, RFCW2198L7B, Android 16), Appium 4724, logcat captured for the whole run
  (`logs/verify-20261117-101034/`, crash buffer `logs/crash-buffer.txt`).
- Build: `device-android.ts build` → versionName 20.19.0, versionCode **90201901**, installed 2026-11-17 09:46; About
  shows 「Version : 20.19.0」, 「SR number PHA261029-01」 (About shows no build number) (`s01-about`).
- First launch: the app was already past the consent screen when the session started (Launcher shown, `s00-start`);
  the photo permission 「Allow PhotoDirector to access photos and videos on this device?」 → 「Allow all」.
- Server: Launcher shows 「NetworkManager Test Server」, debug dialog 「Test server」 on — **same as R3** (fixtures.md).
- Tier: after the fresh install 「Set to subscriber」 was off: Mine 「Upgrade to Premium!」 (`s03-mine-free`) → TC-135 ran
  first as Free; then 「Set to subscriber」 on, OK, relaunch: Mine 「Hello VIP!」 (`s04-debug-premium`,
  `s05-mine-premium`) for every other row. Ends on the Launcher as Premium (`s90-mine-end`, `s91-launcher-end`).
- Photos: 12-photo batches from the top of the All grid (photo 1 = 960 × 640, natively 3:2, so Crop rows used Square
  instead of 3:2); Section 3 stand-ins ①–④ from the Casebook album.

## Verdicts

| Finding | Rows | Verdict |
|---|---|---|
| ISS-BEA-12 | TC-162, TC-164 | **CONFIRMED** |
| ISS-BEA-14 | TC-062, TC-076 | **CONFIRMED** |
| ISS-BEA-15 | TC-049, TC-057, TC-058 | **CONFIRMED in part** (minimum); TC-049 / 2560 px copy **not re-verified** (crash) |
| ISS-BEA-16 | TC-057 | **CONFIRMED** (on ③ instead of ④) |
| ISS-BEA-19 | TC-135 (Free) | **CONFIRMED** (positive control: single save has the ad) |
| ISS-BEA-20 (new) | TC-049 / 057 / 058 precondition | **NEW crash, 4/4** |

### ISS-BEA-12 — 「All」 enabled on a photo with no change of its own — CONFIRMED
- TC-162 (Crop & Rotate, room on photo 1 「960 x 640」, 「All」 disabled on entry): Square on photo 1 → 「640 x 640」,
  「All」 normal (expected). Photo 2 (「960 x 640」, Original) → 「All」 normal, no `disabled` flag (fails R-234); photo 3
  (「960 x 1280」, Original) → normal (fails); photo 1 again → normal (expected). A first try with 3:2 on photo 1 gave the
  same (3:2 is photo 1's own ratio, so redone with Square). Shots: `TC-162-p1`, `TC-162-p2`, `TC-162-p3`, `TC-162-p1-again`.
- TC-164 (Adjustment): entry 「All」 disabled (expected); Exposure 「0.43」 by thumb drag → normal (expected); photo 3 and
  photo 2 (Exposure 「0」) → normal (fails); photo 1 (「0.43」) → normal (expected). Shots: `tc164-1-entry`, `tc164-2-p1`,
  `tc164-3-p3`, `tc164-3-p2`, `tc164-4-p1`.

### ISS-BEA-14 — one Undo keeps the current photo's own edit — CONFIRMED
- TC-062: the room opened on photo 3 (「960 x 1280」, current from TC-162). Square → 「960 x 960」, 「All」; one Undo: photo 3
  still 「960 x 960」 Square, Undo still enabled, 「All」 normal; photo 1 「960 x 640」 Original, photo 4 「1280 x 851」 Original.
  Shots: `TC-062-undo1-p3`, `TC-062-undo1-p1`, `TC-062-undo1-p4`.
- TC-076: Exposure 「0.43」 on photo 1 + 「All」 → toast 「Applied to 11 photos」, photo 3 「0.43」, 「All」 disabled; one Undo →
  toast 「Undo: Apply to all」, photo 1 keeps 「0.43」, photos 2–4 「0」, 「All」 normal. Shots: `tc076-applied-p3`,
  `tc076-undo1`, `tc076-undo1-p1`, `tc076-undo1-p4`.

### ISS-BEA-15 — Crop range from a 2560 px copy, 147 px minimum — CONFIRMED in part
- TC-049 (④ 2730 × 1535 read as 「2560 x 1439」, 3:4 box 「1075 x 1435」): **not re-verified** — Crop & Rotate crashes
  whenever it shows ④ or ① on this build (ISS-BEA-20).
- TC-057 / TC-058 on ③ (800 × 800; room ③ then ②): link off, 3000 × 3000, OK → refused, toast
  「Width should be between 50 and 800. Please try again.」; then 237 × 237, OK → accepted, label 「237 x 237」, no toast.
  The minimum is still below Section 3's 238 px (50 for this photo; 147 for ④ in R3). Shots: `tc057-toast`, `tc058-after`.

### ISS-BEA-16 — out-of-range toast names only the width — CONFIRMED
- Same TC-057 step on ③: 「Width should be between 50 and 800. Please try again.」 although height 3000 is also out of
  range. Shot: `tc057-toast` (toast also in the page source).

### ISS-BEA-19 — Free Batch Save page has no native ad — CONFIRMED
- Free (「Upgrade to Premium!」), 5 photos, Save: 「PhotoDirector Premium」 IAP flyer (✕) → 「Saved 5 photos」, 「Edit Next
  Batch」, no ad element after 10 s (`tc135-b1-after`, `tc135-b1-savepage`, `tc135-b1-savepage-10s`). Second save: 「Rate
  Us」 「Your photo looks perfect! Enjoying PhotoDirector?」 (Not Now) → 「Saved 5 photos」, no ad (`tc135-b2-after`,
  `tc135-b2-savepage`). DCIM/PhotoDirector 940 → 945 → 950.
- Positive control, single save (Edit › Single, Save): interstitial (AI Photo Generator, Close) → 「Save & Share」 with
  the native AdMob card under 「Share to」 (`ad_container`, `savePageAdMobNativeContentAdView`, 「Ad Choices Icon」)
  (`tc135-single-1`, `tc135-single-2`).

### ISS-BEA-20 (new) — Batch Crop & Rotate crashes on large photos — 4/4
`logcat -b crash` (`logs/crash-buffer.txt`; excerpt `logs/crash-excerpt-bca.txt`, scanned: no tokens):
`java.lang.IllegalArgumentException: Cannot coerce value to an empty range: maximum … is less than minimum …` at
`CropRotateImageView.g` ← `crop.a.g` ← `BatchCropRoomFragment.n0 / b0` ← `BatchCropRoomFragment$showPhoto$1`.
1. 10:06:20 — row TC-049 (precondition): Batch with ① ② ③ ④ (Casebook, in that order), Next, tap 「Crop & Rotate」
   (room opens on ① 1706 × 2559) → crash, max 104.21999999999991 < min 104.21999999999997 (`waitfor-timeout-20261117-100631`).
2. 10:07:05 — same steps after relaunch → same crash, system 「Clear cache for PhotoDirector?」 (`s30-room4` just
   before the tap, `crash2-dialog`).
3. 10:08:07 — ④ then ③, tap 「Crop & Rotate」 (room opens on ④ 2730 × 1535) → crash, max 310.83187499999997 < min 310.831875.
4. 10:08:52 — ③ then ④, Crop & Rotate opens on ③ (「800 x 800」, `crash-ctrl-p3-open`), tap ④'s thumbnail → same crash
   (310.83…) (`crash4-after-p4-tap`).
Opened fine: ③ 800 × 800 and the gallery's 960 × 640 / 960 × 1280 / 1280 × 851 photos. The same stand-ins opened in R3
(v202611111946), so this is new on v202611132003. Drafted as ISS-BEA-20, Functional, RD, Severity 1 (user, 2026-11-17).

## Other observations
- The single-photo save on Free showed an interstitial before the Save & Share page (R3 showed Rate Us first): ad
  frequency is account-side, not compared.
- Selecting one photo in the Batch tab and tapping Next opens the single Edit room (not the Batch room).
