# TR261118-0070 verify observations (Android) — eBug drafts, PhotoDirector 20.19.0 build 202611181947

**Source:** the *Other observations* of the TR261118-0070 bug verify run `library/phd/tr-verify/android/runs/2026-11-19-tr261118-0070-verify/` (verdicts-C, -D, -E), 2026-11-19 on Samsung Galaxy S23 (SM-S9110) / Android 16 through Appium / UiAutomator2, Test Server, not signed in (Free; Premium by the debug 「Set to subscriber」 switch for Swipe Collage C). QR261119-0040 carries the verdicts; these four were seen on the way and are not on it.

**Status:** nothing filed, uploaded or commented. Build 20.19.0.v202611181947 (versionCode 90201901), the build TR261118-0070 names. ECL product 「PhotoDirector Mobile for Android」. Creator WILLY_WU, `[AIAgent]`.

**One file for two features (user, 2026-11-19):** the user asked for the four observations as one draft, so Swipe Collage (entries 1–2) and AI Hair Color (entries 3–4) share this file; each Short Description names its feature. IDs continue each feature's series (ISS-SWC-49…, ISS-HCC-29…).

Rules: reviewer rules 2026-10-21 — one action per Repro step, a Spec Link on every entry (URL on its own line), at least one image per entry, the logcat excerpt on the crash entry, no video. PM decisions on user experience are `[AIAgent][UX]`, BugBelong PM; the rest `[AIAgent]` / `[AIAgent][UI]`, RD.

**Dedupe (per OS, PhotoDirector Mobile for Android, 2026-11-19):** every Swipe_Collage (36) and AI_Hair_Color (14) ticket read; no match. Related: PHA262026P0106 (no 「Continue editing?」 after a kill, RDResolved) for entry 1; PHA262026P0089 / P0117 / P0112 (closed by QR261119-0040) for entries 2–4.

Legend — Class: Functional / UI / UX · Severity: S1 critical and blocking only, S2 important, S3 moderate, S4 minor · Owner: RD / PM.

---

## 1. ISS-SWC-49 — Swipe Collage crashes on every open after the app was closed during editing  ·  Class: Functional  ·  Severity: S1  ·  Owner: RD

**Report step:** verdicts-C (P0085 Free check)  ·  **Reproduce:** 3/3 (each open after the one kill)  ·  **Verified on:** 20.19.0.202611181947

> **QA note — not pasted into eBug.** A Swipe Collage canvas with one photo was open (Premium); Removal on the image tool bar was tapped, the Object Removal room's ✕ tapped back to the canvas, and the app was then force-stopped (the run's `terminate`, needed to switch tier with the debug switch). After the relaunch, 「Try Swipe Collage!」 crashed the app every time (15:38:46, 15:39:30, 15:40:18): `ClassCastException: com.google.gson.internal.LinkedTreeMap cannot be cast to iw8` at `SwipeCollageDraftUseCase$load$2.invokeSuspend`. No 「Continue editing?」 dialog appeared first. The second crash showed Android's 「Clear cache for PhotoDirector?」 (Cancel tapped). Swipe Collage stayed unusable until `pm clear` (user-approved, 15:59); after the clear it opened normally (verdicts-E). This looks like the draft restore added for PHA262026P0106 (R-034) failing to read the saved draft, so the kill trigger was seen once (1/1) and the crash 3/3. Whether the Object Removal visit matters was not isolated; the steps keep it. S1: the feature cannot be opened at all until the user clears app data.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent] Swipe_Collage: App crashes on every open after it was closed with a canvas being edited
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap Collage on the Launcher
3. Tap the 「Try Swipe Collage!」 banner
4. Tap the Year-end Recap 「4 photos · 3 pages」 card
5. Tap Use Template
6. Tap the 「+」 of a page-1 frame
7. Select 1 photo
8. Tap Next
9. Tap the filled frame
10. Tap the same frame again
11. Tap Removal on the tool bar
12. Tap Try First
13. Tap ✕ in the Object Removal room
14. Force stop PhotoDirector
15. Launch the APP
16. Tap Collage on the Launcher
17. Tap the 「Try Swipe Collage!」 banner
18. Check the result

Result:
The app crashes at once (ClassCastException in SwipeCollageDraftUseCase), on every later try.
摘要：重開 App 後每次進入 Swipe Collage 都會閃退。
{20.19.0_swc49_crash_on_open.jpg} {20.19.0_swc49_crash_dialog.jpg} {20.19.0_swc49_crash_log.txt}

Expect Result:
No crash: 「Continue editing?」 appears and restores the project, or Swipe Collage opens normally.
摘要：不應閃退，應出現「Continue editing?」還原專案或正常進入。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: Swipe Collage PhDM Spec.pdf (PM), leave-notes board (D1-10: 「Continue editing?」 after a kill restores the project)
Related: PHA262026P0106
<Claude Reviewed>
```

**Images:** `20261119_eBug_drafts_TR261118-0070-Observations_20.19.0_images/01_ISS-SWC-49/`

---

## 2. ISS-SWC-50 — Text colour cancelled with Back is still added as a recent swatch  ·  Class: UX  ·  Severity: S3  ·  Owner: PM

**Report step:** verdicts-C (P0089 side check)  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.202611181947

> **QA note — not pasted into eBug.** Text › STYLE › Color › colour wheel: red picked, system Back closed the picker and the text stayed white (the P0089 fix works), but the red was added as a recent swatch beside the colour wheel. Today's spec says Cancel does not apply the colour (R-085, as the Text color picker) and Back does what Cancel does (R-134), but no board says what the recent swatches hold, so whether a cancelled colour belongs there is a PM decision (`[AIAgent][UX]`, BugBelong PM). The Background picker was not checked for the same thing.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UX] Swipe_Collage: Text colour cancelled with Back is still added as a recent swatch
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap Collage on the Launcher
3. Tap the 「Try Swipe Collage!」 banner
4. Tap the Year-end Recap 「4 photos · 3 pages」 card
5. Tap Use Template
6. Tap the round 「+」
7. Tap Text
8. Tap ✓
9. Tap STYLE
10. Tap the colour wheel in Color
11. Tap a red in the colour square
12. Press system Back
13. Check the result

Result:
The text stays white, but the cancelled red is added as a recent swatch next to the colour wheel.
摘要：取消後文字仍為白色，但被取消的紅色仍加入最近使用色票。
{20.19.0_swc50_red_in_picker.jpg} {20.19.0_swc50_recent_after_back.jpg}

Expect Result:
PM to decide: should a colour cancelled with Cancel / Back be kept as a recent swatch? No sheet describes this.
摘要：請 PM 決定：取消的顏色是否應加入最近使用色票（規格未說明）。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: Swipe Collage Design Figma, 2_add_text board (text editor) -
https://www.figma.com/design/iUy5kOrVNG7IjcyxGGnp9t/Swipe_collage?node-id=54-1487
Basis: None — PM decision requested
<Claude Reviewed>
```

**Images:** `20261119_eBug_drafts_TR261118-0070-Observations_20.19.0_images/02_ISS-SWC-50/`

---

## 3. ISS-HCC-29 — Panel closes on Generate; no Intensity row inside the panel  ·  Class: UX  ·  Severity: S3  ·  Owner: PM

**Report step:** verdicts-D / verdicts-E (P0117)  ·  **Reproduce:** 3/3 (two in-panel Custom generations on 2026-11-19 plus the D run)  ·  **Verified on:** 20.19.0.202611181947

> **QA note — not pasted into eBug.** PHA262026P0117 was closed OK by QR261119-0040: the Custom result has an Intensity bar at 100 above Retry. But the panel now closes as soon as Generate is tapped in it, and reopened it has no Intensity row (Retry only). The 11E flow callout (R-041, D6-22 / D6-23) says the result fills the photo above with a 44 pt Intensity row above the panel's Generate, which becomes 「Retry」; it sends that state to 「result_in_panel」, a frame Spec - UI does not draw (Q-4 open). The PM comment RD cites (3287-93: panel first → close → Intensity) matches the build. A PM decision on which flow is wanted, so `[AIAgent][UX]`, BugBelong PM.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UX] AI_Hair_Color: Custom panel closes on Generate and has no Intensity row — PM to decide
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Tap Continue on the photo tips sheet
5. Tap a portrait photo
6. Tap Custom in the swatch row
7. Tap Ombre in Style
8. Tap the dark brown swatch in Base Color
9. Tap the blue swatch in Highlight Color
10. Tap Generate in the panel
11. Wait for the result
12. Tap Custom again
13. Check the result

Result:
The panel closes on Generate; reopened, it shows Retry but no Intensity row.
摘要：在面板內按 Generate 後面板自動收起，重新打開也沒有 Intensity 列。
{20.19.0_hcc29_result_panel_closed.jpg} {20.19.0_hcc29_panel_no_intensity.jpg}

Expect Result:
PM to decide: the flow note's in-panel result (Intensity row at 100% above 「Retry」) or close-then-Intensity.
摘要：請 PM 決定：面板內顯示 Intensity 列，或收起後才顯示 Intensity。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: AI Hair Color Custom PM Figma (26 11E AI Hair Color Custom), Spec - Flow board (in-panel Generate, D6-22 / D6-23) -
https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3287-93
Basis: None — PM decision requested (the flow note's result_in_panel frame is not drawn)
Related: PHA262026P0117
<Claude Reviewed>
```

**Images:** `20261119_eBug_drafts_TR261118-0070-Observations_20.19.0_images/03_ISS-HCC-29/`

---

## 4. ISS-HCC-30 — Colour-wheel keys stay bright while the colour rows are disabled  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Report step:** verdicts-D (P0112 side effect)  ·  **Reproduce:** 1/1  ·  **Verified on:** 20.19.0.202611181947

> **QA note — not pasted into eBug.** With no style chosen, both colour rows and Generate are disabled (R-023, the P0112 fix works: taps do nothing), and the swatches and Generate are dimmed. The two colour-wheel keys keep almost full colour, so they look tappable while they are not. The Design draws the no-style state in 4-hair_color_case1_no_style (894:1474); the board image is not in the repo, so the Expect Result rests on R-023 (disabled) and the row's own dimmed swatches (in-product basis). RD, UI.

**Short Description:**

```
PHD-A 20.19.0 - [AIAgent][UI] AI_Hair_Color: Custom panel colour-wheel keys stay bright while the rows are disabled
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Tap Continue on the photo tips sheet
5. Tap a portrait photo
6. Tap Custom in the swatch row
7. Check the result

Result:
Swatches and Generate are dimmed, but both colour-wheel keys stay bright and look tappable.
摘要：未選 Style 時色票與 Generate 已變暗，但兩個色輪鍵仍是亮的，看起來可點。
{20.19.0_hcc30_wheel_bright_disabled.jpg}

Expect Result:
Before a style is chosen, the colour-wheel keys are dimmed like the rest of the disabled rows.
摘要：未選 Style 前，色輪鍵應與其他停用色票一樣變暗。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: AI Hair Color Design Figma (Hair, 261005_AI_hair_color page), 4-hair_color_case1_no_style frame -
https://www.figma.com/design/2VOqiPxBCISkob7wbM9hXD/Hair?node-id=894-1474
<Claude Reviewed>
```

**Images:** `20261119_eBug_drafts_TR261118-0070-Observations_20.19.0_images/04_ISS-HCC-30/`

---

## Not raised (for the record)

| Observation | Why not |
|---|---|
| P0084: no literal 「Image locked」 text; floating icons Delete / Replace / Lock | Spec reads 「Image locked」 as a state name; not asked for |
| P0097: no 「Hold ≡ & drag to reorder」 hint | Already part of PHA262026P0097 (Fail on QR261119-0040) |
| P0085: FLAG_SECURE on the Swipe Collage window for Free after the Removal room | Free screenshot policy (「Support ScreenShot for free user」 OFF); not a product defect |
| Soft Black template result has no Intensity row | Template results are the 10/E table's scope, not checked against that spec |
| Custom cell shows a generic icon, not the chosen colours | Open question Q-2 |
| 「Discard」 tap by label did nothing | Driver tapped the dialog title; a tap on the button works |

## Reconciliation against the report

The user asked for four observations; four entries.

| Step | Count |
|---|---|
| Observations the user named | 4 |
| Entries in this file | 4 |

### Row-by-row map

| Observation | Entry |
|---|---|
| Swipe Collage draft crash | ISS-SWC-49 (entry 1) |
| Text Color picker: cancelled colour added to recents | ISS-SWC-50 (entry 2) |
| Hair Color Custom: no Intensity row in the panel | ISS-HCC-29 (entry 3) |
| Hair Color Custom: colour-wheel key bright while disabled | ISS-HCC-30 (entry 4) |

### Owner split

| Owner | Entries |
|---|---|
| RD | 1, 4 |
| PM | 2, 3 |

### Filing order

| Order | Entry |
|---|---|
| 1 | ISS-SWC-49 |
| 2 | ISS-SWC-50 |
| 3 | ISS-HCC-29 |
| 4 | ISS-HCC-30 |
