# Run state — R3 Round 3: full run of table v7 on the TR261111-0042 build (S23)

Table: library/phd/batch-editing/android/cases.csv
Started: 2026-11-13T07:59:45.246Z

## Environment
(build, server, device, tier, credit balance, Pink toggles, Log stage timings, Write Log)

## Checkpoints

### 2026-11-13T08:17:33.153Z · next TC-023 (R3-b)
{"Pass":24,"Fail":1,"Blocked":10,"Not run":135}

R3-a done (26/26). Build check: About 20.19.0, SR PHA261029-01 (versionCode 90201900, updated 2026-11-13 14:32) = TR261111-0042 build. Tier was Free at start; switched to Premium via About debug dialog 「Set to subscriber」 ON (only that switch), relaunched; Mine 「Hello VIP!」, credits 1886 (16:02). Picker album left on 「All」. App on the Launcher, nothing half-done. Logs pulled 16:17 (logs/R3-a-20261113-161712). Note: device-android hold takes seconds (a 1200 s hold hung UiAutomator2 once; session restarted, no case affected). Batch save copies sit first in 「All」 (KF-002).

### 2026-11-13T08:38:33.706Z · next TC-048 (R3-c)
{"Pass":57,"Fail":3,"Blocked":10,"Not run":100}

R3-b done (35/35): 33 Pass, 2 Fail (TC-162 「All」 not greyed on a photo with no change of its own, repeats R2 draft ISS-BEA-12 part; TC-062 one Undo keeps photo 1's own 3:2, question, R2 draft ISS-BEA-14). Tier Premium at start (Mine 「Hello VIP!」, credits 1886, 16:17). Build changes vs R1/R2: Crop & Rotate now has ‹ (backBtn), and 「All」 is greyed on entry / after apply / after Redo (TC-153, TC-042, TC-063 Pass). Photos: 12 = Sample Photos (8) + 00PHDa_Testing_Material tiles 2-5 (recipe recipes/pick12-sample.steps); the 「Casebook」 album was not found in the picker's album list (scrollto / visible list) this segment; TC-041 used a 3-photo batch. App left on the Launcher, nothing half-done, no Batch Save done. Logs pulled 16:38 (logs/R3-b-20261113-163812), no errors in Fail windows.

### 2026-11-13T11:24:24.889Z · next TC-069 (R3-d)
{"Pass":69,"Fail":7,"Blocked":10,"Not run":84}

R3-c done (16/16): 12 Pass, 4 Fail (TC-049 / TC-057 / TC-058 questions as R1: 2560 px room cap of ④, min 147 px and width-only toast 「Width should be between 147 and 2560. Please try again.」; TC-060 defect repeats PHA262026P0060, ④ saved 1434×1435). TC-163 now Pass (「All」 stays greyed after a size-only change; R2 ISS-BEA-12 part fixed). Segment paused ~2.5 h for a usage-limit reset after the tier check (session restarted 19:11, nothing recorded before). Tier Premium (Mine 「Hello VIP!」, credits 1886, 16:39; 1886 in the 19:23 log). 「Casebook」 album found in the picker: alphabetical, after Camera, 4 drags down (recipe recipes/pick4-casebook.steps); new recipe recipes/crop-reopen.steps. Never scrollto in Crop & Rotate (it swept the rotate slider to 45° once; cancelled, no case affected). One batch save done (4 files 2026-11-13-19-23-*.jpg, now first in 「All」, KF-002; no Rate Us). App on the Launcher, nothing half-done. Logs pulled 19:24 (logs/R3-c-20261113-192401), Fail windows only CacheDao noise. status shows two Appium servers (4724, 4726): left alone, reported.

### 2026-11-13T11:42:46.636Z · next TC-083 (R3-e)
{"Pass":90,"Fail":9,"Blocked":10,"Not run":61}

R3-d done (23/23): 21 Pass, 2 Fail (TC-164 defect: 「All」 not greyed on photo 2 with no change of its own, repeats R2 draft ISS-BEA-12 open part, same as TC-162; TC-076 question: one Undo keeps photo 1's own Exposure, R2 draft ISS-BEA-14). Fixed on this build vs R2: TC-166 / TC-168 (strip hidden while Curve / HSL open), TC-075 / TC-165 (「All」 greyed after apply and after Redo, disabled tap gives no toast). Tier Premium (Mine 「Hello VIP!」, credits 1886 at 19:12, 1886 in the 19:42 log). Picker: Sample Photos is the first album in the list (scroll the album list to the top), then recipes/pick12-sample.steps. Setting a slider value directly (setval) shows the label but makes no history step on Light sliders (HSL ones did); use thumb drags. Batch discarded (Discard changes? › Discard), no save; app on the Launcher, nothing half-done. Logs pulled 19:42 (logs/R3-d-20261113-194230), no errors in the Fail windows. O-1: Help (i) hidden on the Details tab. Two Appium servers (4724, 4726) left alone.

### 2026-11-13T12:08:18.720Z · next TC-113 (R3-f)
{"Pass":114,"Fail":13,"Blocked":10,"Not run":33}

R3-e done (28 run + 8 fault rows Blocked observability by init): 24 Pass, 4 Fail (TC-144 defect repeats PHA262026P0058: system Back does not close 「Enhance 12 photos?」; TC-110 defect repeats PHA262026P0057: Home for 30 s → 「3 completed, 9 failed」 Connection lost, UnknownHostException in the background; TC-100 / TC-142 questions as R1, Q-19: ✕ and Back open 「Discard changes?」 after the batch finished, a 2nd Back does not close that dialog). TC-107 toast 「No Internet connection」 recorded Pass per the user's R1 ruling (ISS-BEA-11 not a bug). No fault switch seen on this build (fault rows stay Blocked). Tier Premium (Mine 「Hello VIP!」), credits 1886 at 19:44, 19:52 and 20:07: AI Enhance charged nothing. Wi-Fi off 20:04:46 for TC-106/107, back on 20:05 and connected (17F_QA_Wifi_5G). One batch save (3 files 2026-11-13-19-58-58-*.jpg, first in 「All」 now, KF-002; 「Rate Us」 came up after it, Not Now). App killed once from Recents (TC-111) and relaunched; logcat capture kept running. App on the Launcher (Home tab), no batch open, nothing half-done. Logs pulled 20:07 (logs/R3-e-20261113-200751). Album list: names were missing from the page source; pick12-sample.steps comment updated. Two Appium servers (4724, 4726) left alone.

### 2026-11-13T12:26:06.822Z · next TC-156 (R3-g)
{"Pass":140,"Fail":15,"Blocked":10,"Not run":5}

R3-f done (28 run + TC-136 Blocked test-data by init): 26 Pass, 2 Fail (TC-145 defect repeats PHA262026P0059: system Back does not close 「Discard changes?」; TC-128 question as R1, Q-20: title 「Saved 12 photos」 vs Design 「Save 12 photos」). TC-115 (「Keep」 not 「Keep Editing」) and TC-122 (dimmed feedback button while saving) recorded Pass per the user's R1 rulings on ISS-BEA-08 / ISS-BEA-07. Tier Premium (Mine 「Hello VIP!」, credits 1886 at 20:08). Photos: album 00PHDa_Testing_Material (the picker opens on it now), new recipe recipes/pick12-testing.steps (its first 12 tiles; check the grid is scrolled to the top: once it kept a one-row scroll and TC-128's batch was tiles 4-15). Saves: 20 ×4 and 12 ×2 (DCIM/PhotoDirector 825 → 929); 「Rate Us」 after the 3rd 20-save and the 2nd 12-save, Not Now both times. Saving takes ~3 s for 20: captures by adb screencap in one shell command. App killed once from Recents (TC-121), relaunched; logcat capture kept running. App on the Launcher, batch discarded, nothing half-done. Logs pulled 20:25 (logs/R3-f-20261113-202548), no errors in the Fail windows. O-4: picker tray thumbnail mismatch once (TC-119). Two Appium servers (4724, 4726) left alone.

### 2026-11-13T12:36:25.256Z · all recorded
{"Pass":144,"Fail":16,"Blocked":10}

R3-g done (5/5): 4 Pass (TC-156, TC-082, TC-098, TC-099), 1 Fail question (TC-135: no native ad card on the Batch Save page while the single Save & Share page has one; interstitial on the 1st batch save, IAP flyer on the 2nd; O-19 as R1). Tier: Free at 20:28 via About debug dialog 「Set to subscriber」 OFF only (Mine 「Upgrade to Premium!」, 1886 credits; no UUID / token shown in the dialog view), back to Premium at 20:36 (「Set to subscriber」 ON, relaunch, Mine 「Hello VIP!」, 1886). Saves: 5 ×2 batch + 1 single (DCIM/PhotoDirector 929 → 940). App on the Launcher, nothing half-done. Logs pulled 20:36 (logs/R3-g-20261113-203614), TC-135 window only ad MediaCodec noise. Phase R3 all rows recorded.
