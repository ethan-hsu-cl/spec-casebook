# Image to Video Reuse (Android) — eBug drafts, round R1 (table v3), PhotoDirector 20.19.0 build 90201901

**Source:** spec-casebook run `library/phd/i2v-reuse/android/runs/2026-11-19-r1/` — phase R1 of draft `drafts/20261106-115758` (table v3, 50 cases), 2026-11-19 11:05 → 14:50, Google Pixel 8a / Android 16, Appium / UiAutomator2, Test Server, Free (Premium only for the R1-setup model probes). Tally: 11 Blocked, 10 Fail, 29 Pass.

**Status:** nothing filed, uploaded or commented. TR261118-0070 names build 20.19.0.v202611181947 (versionCode 90201901), the build tested. ECL product 「PhotoDirector Mobile for Android」. No filed batch for this feature yet: Creator, source tag and method to confirm on the review page.

Rules: reviewer rules 2026-10-21 — one action per Repro step, a Spec Link on every entry (URL on its own line), at least one image per entry, the logcat excerpt on failure / tracking entries, no video. UX decisions to PM as `[AIAgent][UX]`; text and layout `[AIAgent][UI]` (RD when the Design / PM states the text, PM when the spec's text must be confirmed); behaviour `[AIAgent]` Functional, RD. Spec basis per entry against the PM page 6336:3478 (section Spec) and the Design page 4701:15518 (four frames).

**What is drafted:** 10 new entries (ISS-IR-01…10), of which 2 ask PM for a decision. Dedupe per OS: see dedupe.txt.

Legend — Class: Functional / UI / UX · Severity: S1 critical and blocking only, S2 important, S3 moderate, S4 minor · Owner: RD / PM.

---

## 1. ISS-IR-01 — No 「Settings applied」 toast after Reuse  ·  Class: Functional  ·  Severity: S3  ·  Owner: RD

**Filed by:** WILLY_WU · [PHA262026P0141](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/PHA262026P0141) · TR261118-0070 · 2026-11-19

**Report step:** TC-010, TC-013, TC-015  ·  **Reproduce:** 4/4  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-025 / R-026 (PM Spec - UI, From Save & Share Reuse D1-04 / D1-04b: entering the reused Custom page shows the toast 「Settings applied」). Reuse fills the room correctly (model, Start/End, prompt, empty photo; TC-010 / TC-013 / TC-012 Pass), but no toast: screenshots at ~0.6 s and ~2.6 s, a 9 s recording at 2 fps (TC-010), an 8 s recording (TC-015) and waitfor 「Settings applied」 7 s (TC-010, TC-013) found none. Seen on video A (Kling 2.6) and video C (Kling 3.0, Start/End). Blocks TC-016 (toast over a panel) and TC-046. The PM drew the toast only; no Design frame for it (PM-only).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] Image_to_Video: No 「Settings applied」 toast when Reuse opens the Custom page
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos
3. Tap My Artwork
4. Tap the All categories button
5. Tap Image to Video
6. Tap a finished Custom video made with Kling 2.6 (10s, Pro, Sound on)
7. Tap Reuse
8. Watch the Custom page for 8 seconds
9. Check the result

Result:
The Custom page opens with the video's settings and prompt, but the toast 「Settings applied」 never shows.
摘要：Reuse 進入 Custom 頁設定已帶入，但沒有出現「Settings applied」toast。
{20.19.0_ir01_reuse_room_no_toast.jpg} {20.19.0_ir01_recording_frames_no_toast.jpg} {20.19.0_ir01_start_end_room_no_toast.jpg} {20.19.0_ir01_log.txt}

Expect Result:
On entering the Custom page the toast 「Settings applied」 shows (PM D1-04).
摘要：進入 Custom 頁時應顯示 toast「Settings applied」。

Note:
Device: Google Pixel 8a / Android 16, Test Server, Free account (build 20.19.0.v202611181947)
Spec Link: Image to Video Reuse PM Figma (page 26'11/E support to reuse model settings in My artwork), Spec - UI board (From Save & Share Reuse, D1-04 / D1-04b toast 「Settings applied」) -
https://www.figma.com/design/lSk4JUgbXG3DjauMLS9Et7/Image-to-Video?node-id=6366-5664
<Claude Reviewed>
```

**Images:** `20261119_eBug_drafts_I2V-Reuse-R1_20.19.0_images/01_ISS-IR-01/`

---

## 2. ISS-IR-02 — Reuse skips the Image to Video explanation sheet  ·  Class: Functional  ·  Severity: S4  ·  Owner: RD

**Filed by:** WILLY_WU · [PHA262026P0142](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/PHA262026P0142) · TR261118-0070 · 2026-11-19

**Report step:** TC-015  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-026 (PM Spec - UI D1-04b: when Image to Video would show its Android explanation sheet, it shows first as today, then the toast). 「Don't show again」 was never tapped: entering Image to Video from AI Videos (14:14) and from a fresh My AI Artwork 「Create More」 (TC-028) still shows the 「Image To Video」 intro (Try now / Don't show again) and the 「Steps」 page, but 「Reuse」 opens the Custom page directly, every time (R1-a, R1-b, R1-c). TC-046 (Back on that sheet) is Blocked behind it.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] Image_to_Video: Reuse opens Custom without the Image to Video explanation sheet shown elsewhere
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Videos
3. Tap Image to Video
4. Check the explanation sheet shows
5. Tap the device Back button
6. Tap AI Photos
7. Tap My Artwork
8. Tap the All categories button
9. Tap Image to Video
10. Tap a finished Custom video made with Kling 2.6
11. Tap Reuse
12. Check the result

Result:
From AI Videos the 「Image To Video」 explanation sheet shows; from 「Reuse」 the Custom page opens directly with no sheet.
摘要：從 AI Videos 進入會出現說明頁，但從 Reuse 進入直接到 Custom 頁，沒有說明頁。
{20.19.0_ir02_ai_videos_entry_sheet.jpg} {20.19.0_ir02_reuse_no_sheet.jpg}

Expect Result:
When Image to Video would show its explanation sheet, Reuse shows it first as today, then the Custom page (PM D1-04b).
摘要：說明頁應照常先出現，關閉後才進入 Custom 頁。

Note:
Device: Google Pixel 8a / Android 16, Test Server, Free account (build 20.19.0.v202611181947)
Spec Link: Image to Video Reuse PM Figma (page 26'11/E support to reuse model settings in My artwork), Spec - UI board (From Save & Share Reuse, D1-04b explanation sheet first) -
https://www.figma.com/design/lSk4JUgbXG3DjauMLS9Et7/Image-to-Video?node-id=6366-5664
<Claude Reviewed>
```

**Images:** `20261119_eBug_drafts_I2V-Reuse-R1_20.19.0_images/02_ISS-IR-02/`

---

## 3. ISS-IR-03 — ‹ and system Back in the reused room skip the Save & Share page  ·  Class: Functional  ·  Severity: S3  ·  Owner: RD

**Filed by:** WILLY_WU · [PHA262026P0143](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/PHA262026P0143) · TR261118-0070 · 2026-11-19

**Report step:** TC-020, TC-043  ·  **Reproduce:** 3/3  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-033 (PM Spec - UI From Save & Share Reuse D1-05: ‹ Back in the reused room returns to the Save & Share page) and R-058 / R-064 (system Back acts as ‹). Both ‹ (top_back_btn) and system Back land on My AI Artwork › Image to Video (the list), never on the video's Save & Share page. First seen as O-3 (R1-a), then TC-020 / TC-043 (R1-b).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] Image_to_Video: ‹ / Back in the room opened by Reuse go to My AI Artwork, not Save & Share
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos
3. Tap My Artwork
4. Tap the All categories button
5. Tap Image to Video
6. Tap a finished Custom video made with Kling 2.6 (10s, Pro, Sound on)
7. Tap Reuse
8. Tap ‹ at the top left
9. Tap the same video
10. Tap Reuse
11. Tap the device Back button
12. Check the result

Result:
Both ‹ and system Back return to the My AI Artwork Image to Video list; the video's Save & Share page is skipped.
摘要：Reuse 房間按 ‹ 或返回鍵都回到 My AI Artwork 列表，未回到 Save & Share 頁。
{20.19.0_ir03_back_arrow_to_artwork.jpg} {20.19.0_ir03_system_back_to_artwork.jpg}

Expect Result:
‹ (and system Back) in the reused room return to the video's Save & Share page (PM D1-05).
摘要：應回到該影片的 Save & Share 頁。

Note:
Device: Google Pixel 8a / Android 16, Test Server, Free account (build 20.19.0.v202611181947)
Spec Link: Image to Video Reuse PM Figma (page 26'11/E support to reuse model settings in My artwork), Spec - UI board (From Save & Share Reuse, D1-05 ‹ Back returns to Save & Share) -
https://www.figma.com/design/lSk4JUgbXG3DjauMLS9Et7/Image-to-Video?node-id=6366-5664
<Claude Reviewed>
```

**Images:** `20261119_eBug_drafts_I2V-Reuse-R1_20.19.0_images/03_ISS-IR-03/`

---

## 4. ISS-IR-04 — Quality chip is lower case: 「pro」 / 「std」  ·  Class: UI  ·  Severity: S4  ·  Owner: RD

**Not filed:** held by the reviewer (2026-11-19, no reason given).

**Report step:** TC-006, TC-024  ·  **Reproduce:** 4/4  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-012 (Design Save & Share light: chips 「10s」 「Pro」 「Sound on」; the Custom room's own Video Quality options read 「Pro」 / 「Standard」). Video A and the video generated from its Reuse (TC-024) show 「pro」, videos B and C show 「std」 (TC-013 saw 「std」 on C). Q-13 asked for the chip wording of each quality; the Design sample 「Pro」 states it for Pro, so this is RD (text differs from the stated spec). For Standard the Design has no sample: 「std」 vs 「Standard」 / 「Std」 is noted in the Expect.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] Image_to_Video: Save & Share: quality chip reads lower-case 「pro」 / 「std」 (Design 「Pro」)
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos
3. Tap My Artwork
4. Tap the All categories button
5. Tap Image to Video
6. Tap a finished Custom video made with Kling 2.6 (10s, Pro, Sound on)
7. Read the chips on the Prompts & Settings card
8. Check the result

Result:
The quality chip reads 「pro」 (Kling 2.6 Pro video); on Standard videos it reads 「std」.
摘要：畫質 chip 顯示小寫 pro／std。
{20.19.0_ir04_chip_pro_lowercase.jpg} {20.19.0_ir04_chip_std_lowercase.jpg}

Expect Result:
The chip reads 「Pro」 as the Design draws it (Standard capitalised the same way, e.g. 「Standard」 as in the room).
摘要：應顯示「Pro」（Standard 亦應首字大寫）。

Note:
Device: Google Pixel 8a / Android 16, Test Server, Free account (build 20.19.0.v202611181947)
Spec Link: Image to Video Reuse Design Figma (page 261105_support to reuse model settings), Save & Share light frame (Prompts & Settings card, chips 「10s」 「Pro」 「Sound on」, section order) -
https://www.figma.com/design/VU8bgYiFHTWhYddg7ciqtL/Image-to-video---Character-motion-swap?node-id=4702-20032
Related: Q-13
<Claude Reviewed>
```

**Images:** `20261119_eBug_drafts_I2V-Reuse-R1_20.19.0_images/04_ISS-IR-04/`

---

## 5. ISS-IR-05 — Save & Share order: 「Prompts & Settings」 right under 「Save」, no 「More Video Editing Tools」  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Not filed:** held by the reviewer (2026-11-19, no reason given).

**Report step:** TC-049  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-067 (Design Save & Share light / dark: 「Save」, 「More Video Editing Tools」, 「Add Text」 「Add Sticker」 「Add Music」, 「Prompts & Settings」, 「Share to」). The app places the 「Prompts & Settings」 card directly under 「Save」, above the editing buttons, and has no 「More Video Editing Tools」 heading; 「Make It Reel-Ready」 sits between the editing buttons and 「Share to」 (not drawn; other feature).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] Image_to_Video: Save & Share: 「Prompts & Settings」 sits under 「Save」; no 「More Video Editing Tools」
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos
3. Tap My Artwork
4. Tap the All categories button
5. Tap Image to Video
6. Tap a finished Custom video made with Kling 2.6 (10s, Pro, Sound on)
7. Scroll the page from top to bottom
8. Check the result

Result:
「Prompts & Settings」 sits right under 「Save」, above the editing buttons; no 「More Video Editing Tools」 heading.
摘要：設定卡片在 Save 正下方，且缺少 More Video Editing Tools 標題。
{20.19.0_ir05_order_card_under_save.jpg} {20.19.0_ir05_order_bottom.jpg}

Expect Result:
Order (Design): Save, More Video Editing Tools, Add Text / Sticker / Music, Prompts & Settings, Share to.
摘要：順序應為 Save、More Video Editing Tools、編輯按鈕、Prompts & Settings。

Note:
Device: Google Pixel 8a / Android 16, Test Server, Free account (build 20.19.0.v202611181947)
Spec Link: Image to Video Reuse Design Figma (page 261105_support to reuse model settings), Save & Share light frame (Prompts & Settings card, chips 「10s」 「Pro」 「Sound on」, section order) -
https://www.figma.com/design/VU8bgYiFHTWhYddg7ciqtL/Image-to-video---Character-motion-swap?node-id=4702-20032
Spec Link: Image to Video Reuse Design Figma (page 261105_support to reuse model settings), Save & Share dark frame (Save & Share page in dark mode) -
https://www.figma.com/design/VU8bgYiFHTWhYddg7ciqtL/Image-to-video---Character-motion-swap?node-id=4720-469
<Claude Reviewed>
```

**Images:** `20261119_eBug_drafts_I2V-Reuse-R1_20.19.0_images/05_ISS-IR-05/`

---

## 6. ISS-IR-06 — PM: Create more placeholder and counter differ from the Reuse spec mockup  ·  Class: UI  ·  Severity: S4  ·  Owner: PM

**Not filed:** held by the reviewer (2026-11-19, no reason given).

**Report step:** TC-028  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-041 (PM Spec - UI My AI Artwork D1-03 / Spec - Flow mockup: placeholder 「Describe the subject, action, and overall scene, e.g. A woman walking in a park on a sunny afternoon.」, counter 「0/2,500」; the reuse mockup also writes 「58/2,500」). The app's Create more room reads 「Describe the subject and how they move in the scene, e.g. A dancer spins and jumps under stage lights.」 and 「0/2500」. Create more is meant to be unchanged by this feature, so the mockup may simply copy an older string; filed to PM to confirm which text is current (text rule: PM when the spec's own text must change).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] Image_to_Video: Create more: placeholder and 「0/2500」 differ from the PM mockup — PM to confirm
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos
3. Tap My Artwork
4. Tap the All categories button
5. Tap Image to Video
6. Tap Create More
7. Tap Try now
8. Tap Continue
9. Read the prompt box
10. Check the result

Result:
Placeholder reads 「Describe the subject and how they move in the scene, e.g. A dancer spins…」; counter 「0/2500」.
摘要：Create more 的提示文字與計數格式和 PM 稿不同。
{20.19.0_ir06_create_more_placeholder.jpg}

Expect Result:
PM to confirm the text: the mockup shows 「Describe the subject, action, and overall scene, e.g. …」 and 「0/2,500」.
摘要：請 PM 確認正確提示文字與計數格式（稿上為 0/2,500）。

Note:
Device: Google Pixel 8a / Android 16, Test Server, Free account (build 20.19.0.v202611181947)
Spec Link: Image to Video Reuse PM Figma (page 26'11/E support to reuse model settings in My artwork), Spec - UI board (My AI Artwork, D1-03 Create more mockup) -
https://www.figma.com/design/lSk4JUgbXG3DjauMLS9Et7/Image-to-Video?node-id=6366-5664
Spec Link: Image to Video Reuse PM Figma (page 26'11/E support to reuse model settings in My artwork), Spec - Flow board (Reuse flow and Create more mockup) -
https://www.figma.com/design/lSk4JUgbXG3DjauMLS9Et7/Image-to-Video?node-id=6366-4241
<Claude Reviewed>
```

**Images:** `20261119_eBug_drafts_I2V-Reuse-R1_20.19.0_images/06_ISS-IR-06/`

---

## 7. ISS-IR-07 — Reuse sends Artwork_Reuse_Click without model, not ImageToVideo_Reuse_Click  ·  Class: Functional  ·  Severity: S3  ·  Owner: RD

**Filed by:** WILLY_WU · [PHA262026P0144](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/PHA262026P0144) · TR261118-0070 · 2026-11-19

**Report step:** TC-037  ·  **Reproduce:** 3/3  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** R-051 (PM 【Tracking Event】 D4-05: new event ImageToVideo_Reuse_Click with parameter model). Observed in the app's logcat Mixpanel lines (Q-8: a log pull): each 「Reuse」 tap logs 「logEvent name=Artwork_Reuse_Click」 (the form used for events without parameters; events with parameters print JSON) and 「[setCurFrom] from = artwork_reuse」. Three taps, 14:29:36, 14:32:52, 14:36:21. Generate after Reuse sends ImageToVideo_Result_Generate with from = artwork_reuse (TC-038 / TC-039 Pass) and Create more from = Artwork (TC-040 Pass).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] Image_to_Video: Tracking: Reuse logs Artwork_Reuse_Click without model, not ImageToVideo_Reuse_Click
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos
3. Tap My Artwork
4. Tap the All categories button
5. Tap Image to Video
6. Tap a finished Custom video made with Kling 2.6 (10s, Pro, Sound on)
7. Tap Reuse
8. Pull the app's logcat
9. Find the Mixpanel event logged at the Reuse tap
10. Check the result

Result:
The Reuse tap logs 「logEvent name=Artwork_Reuse_Click」 with no parameters.
摘要：點 Reuse 送出的事件為 Artwork_Reuse_Click，且沒有 model 參數。
{20.19.0_ir07_reuse_room.jpg} {20.19.0_ir07_log.txt}

Expect Result:
ImageToVideo_Reuse_Click is sent with parameter model = the video's model value (PM D4-05).
摘要：應送出 ImageToVideo_Reuse_Click 並帶 model 參數。

Note:
Device: Google Pixel 8a / Android 16, Test Server, Free account (build 20.19.0.v202611181947)
Spec Link: Image to Video Reuse PM Figma (page 26'11/E support to reuse model settings in My artwork), 【Tracking Event】 board (D4-05 ImageToVideo_Reuse_Click, parameter model) -
https://www.figma.com/design/lSk4JUgbXG3DjauMLS9Et7/Image-to-Video?node-id=6394-586
<Claude Reviewed>
```

**Images:** `20261119_eBug_drafts_I2V-Reuse-R1_20.19.0_images/07_ISS-IR-07/`

---

## 8. ISS-IR-08 — Switching the system theme on Save & Share drops the page to the Launcher  ·  Class: Functional  ·  Severity: S3  ·  Owner: RD

**Not filed:** held by the reviewer (2026-11-19, no reason given).

**Report step:** O-1  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** Observation O-1 (TC-050 setup, R1-a). With video A's Save & Share page open, the phone's system theme was switched dark → light: the app recreated and showed the Launcher's AI Videos tab; the Save & Share page was lost. The app follows the system theme (it turned light). Expected: an activity recreated by a configuration change keeps the page the user was on. Seen once (theme change is a system setting; restored after).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] Image_to_Video: Save & Share: changing the system theme sends the app back to the Launcher
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos
3. Tap My Artwork
4. Tap the All categories button
5. Tap Image to Video
6. Tap a finished Custom video made with Kling 2.6 (10s, Pro, Sound on)
7. Open Android Settings from the quick settings panel
8. Turn Dark theme off
9. Return to PhotoDirector
10. Check the result

Result:
PhotoDirector shows the Launcher's AI Videos tab in light mode; the Save & Share page is gone.
摘要：在 Save & Share 頁切換系統深淺色後，App 回到 Launcher，原頁面消失。
{20.19.0_ir08_saveshare_dark_before.jpg} {20.19.0_ir08_launcher_after_theme.jpg}

Expect Result:
The Save & Share page stays open and redraws in the new theme.
摘要：應停留在 Save & Share 頁並以新主題重繪。

Note:
Device: Google Pixel 8a / Android 16, Test Server, Free account (build 20.19.0.v202611181947)
Spec Link: Image to Video Reuse Design Figma (page 261105_support to reuse model settings), Save & Share dark frame (Save & Share page in dark mode) -
https://www.figma.com/design/VU8bgYiFHTWhYddg7ciqtL/Image-to-video---Character-motion-swap?node-id=4720-469
<Claude Reviewed>
```

**Images:** `20261119_eBug_drafts_I2V-Reuse-R1_20.19.0_images/08_ISS-IR-08/`

---

## 9. ISS-IR-09 — Reuse transition draws the room rotated for a moment  ·  Class: UI  ·  Severity: S4  ·  Owner: RD

**Filed by:** WILLY_WU · [PHA262026P0145](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/PHA262026P0145) · TR261118-0070 · 2026-11-19

**Report step:** O-2  ·  **Reproduce:** 3/3  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** Observation O-2 (TC-010, again TC-015). The 9 s screen recording of 「Reuse」 shows the Custom room drawn rotated 90° (landscape layout) for one or two frames before it settles portrait (frames 3–4 of the grid). Phone in portrait, auto-rotate unchanged.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] Image_to_Video: Reuse: Custom room flashes rotated (landscape) before settling portrait
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos
3. Tap My Artwork
4. Tap the All categories button
5. Tap Image to Video
6. Tap a finished Custom video made with Kling 2.6 (10s, Pro, Sound on)
7. Tap Reuse
8. Watch the transition into the Custom page
9. Check the result

Result:
For one or two frames the Custom room is drawn rotated (landscape) before it shows portrait.
摘要：Reuse 轉場時房間短暫以橫向（旋轉）畫面出現。
{20.19.0_ir09_rotated_frames.jpg} {20.19.0_ir09_rotated_frames_again.jpg}

Expect Result:
The Custom room opens in portrait without a rotated frame.
摘要：應直接以直向開啟，不閃現旋轉畫面。

Note:
Device: Google Pixel 8a / Android 16, Test Server, Free account (build 20.19.0.v202611181947)
Spec Link: Image to Video Reuse PM Figma (page 26'11/E support to reuse model settings in My artwork), Spec - UI board (From Save & Share Reuse, D1-04 / D1-04b toast 「Settings applied」) -
https://www.figma.com/design/lSk4JUgbXG3DjauMLS9Et7/Image-to-Video?node-id=6366-5664
<Claude Reviewed>
```

**Images:** `20261119_eBug_drafts_I2V-Reuse-R1_20.19.0_images/09_ISS-IR-09/`

---

## 10. ISS-IR-10 — PM: first tap in a reused prompt selects the whole prompt  ·  Class: UX  ·  Severity: S4  ·  Owner: PM

**Filed by:** WILLY_WU · [PHA262026P0146](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/PHA262026P0146) · TR261118-0070 · 2026-11-19

**Report step:** O-5  ·  **Reproduce:** 2/2  ·  **Verified on:** 20.19.0.90201901

> **QA note — not pasted into eBug.** Observation O-5 (TC-045, TC-032). The first tap into the prompt box of a room opened by Reuse highlights the whole reused prompt; a Backspace or a typed letter then replaces all of it. The spec says nothing about the selection; R-022 brings the prompt back for editing. Filed to PM to decide (UX decision rule 2026-11-11).

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UX] Image_to_Video: Reused room: first tap selects the whole prompt (one key erases it) — PM to decide
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos
3. Tap My Artwork
4. Tap the All categories button
5. Tap Image to Video
6. Tap a finished Custom video made with Kling 2.6 (10s, Pro, Sound on)
7. Tap Reuse
8. Tap inside the prompt box
9. Check the result

Result:
The whole reused prompt is highlighted; the next key press replaces it.
摘要：第一次點擊提示詞欄位會全選整段文字，再按一鍵即全部被取代。
{20.19.0_ir10_prompt_all_selected.jpg} {20.19.0_ir10_prompt_all_selected_2.jpg}

Expect Result:
PM to decide: the tap places the cursor (keeping the prompt) or selects all on purpose.
摘要：請 PM 決定第一次點擊應放置游標或刻意全選。

Note:
Device: Google Pixel 8a / Android 16, Test Server, Free account (build 20.19.0.v202611181947)
Spec Link: Image to Video Reuse PM Figma (page 26'11/E support to reuse model settings in My artwork), Spec - UI board (From Save & Share Reuse, D1-04 / D1-04b toast 「Settings applied」) -
https://www.figma.com/design/lSk4JUgbXG3DjauMLS9Et7/Image-to-Video?node-id=6366-5664
Basis: None — neither the PM spec nor the Design states how the first tap treats the reused prompt; PM to decide
<Claude Reviewed>
```

**Images:** `20261119_eBug_drafts_I2V-Reuse-R1_20.19.0_images/10_ISS-IR-10/`

---

# Not raised (observations, for the record)

| Item | What was seen | Why not raised |
|---|---|---|
| O-3 | ‹ in the Reuse room goes to My AI Artwork. | In ISS-IR-03 (TC-020 / TC-043). |
| O-4 | ‹ in a Create More room reached via the room's history button → Reuse → ‹ → Create More went to the Launcher. | Existing Image to Video navigation through the history button, outside this feature's spec; not compared with a pre-feature build. |
| Blocked (11) | 2 defect, 9 test-data | TC-041, TC-042, TC-046, TC-016, TC-034, TC-019, TC-036, TC-029, TC-030, TC-031, TC-035. |

# Reconciliation against the run

10 Fail, 11 Blocked, 0 Not run, 5 observations (O-1 … O-5).

| Item | Result | Disposition | Became |
|---|---|---|---|
| TC-006 | Fail | defect | 4. ISS-IR-04 |
| TC-049 | Fail | defect | 5. ISS-IR-05 |
| TC-010 | Fail | defect | 1. ISS-IR-01 |
| TC-043 | Fail | defect | 3. ISS-IR-03 |
| TC-013 | Fail | defect | 1. ISS-IR-01 |
| TC-015 | Fail | defect | 1. ISS-IR-01; 2. ISS-IR-02 |
| TC-020 | Fail | defect | 3. ISS-IR-03 |
| TC-028 | Fail | defect | 6. ISS-IR-06 |
| TC-024 | Fail | defect | 4. ISS-IR-04 |
| TC-037 | Fail | defect | 7. ISS-IR-07 |
| O-1 | observation | — | 8. ISS-IR-08 |
| O-2 | observation | — | 9. ISS-IR-09 |
| O-3 | observation | — | In ISS-IR-03 (TC-020 / TC-043) |
| O-4 | observation | — | not raised |
| O-5 | observation | — | 10. ISS-IR-10 |

Filing order by severity: **1**, **3**, **5**, **7**, **8**, **2**, **4**, **6**, **9**, **10**. Nothing is filed until the review page's decisions come back.
