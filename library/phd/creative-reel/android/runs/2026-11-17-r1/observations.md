# Observations — Creative Reel Android R1

- **O-1 (setup, before TC-001, 2026-11-17 18:43)** Phone state differed from the plan / probe at segment start: About ›
  debug dialog had 「Test server」 OFF and 「Set to subscriber」 ON; Mine 「Hello VIP!」, My Credits **1875**
  (log `totalRemain=1875`, creditSystemUUID 4dc0bf10-…-1b625508a4a7, the install's UUID). Probe at 17:04 had Test
  Server label on the Launcher, Free, 2000. The segment switched both back to the plan (Test server ON, subscriber OFF,
  OK, relaunch): Launcher shows 「Test Server」, Mine 「Upgrade to Premium!」, but My Credits **0** with a new
  creditSystemUUID d53bb270-e273-…-9fa04d6fdfff (`totalRemain=0`, history 0 records). Evidence:
  screenshots/seg-start-mine.png, debug-dialog-before.png, debug-dialog-after.png, seg-start-mine-free.png,
  logs/R1-a-setup-20261117-184608/. A launch interstitial ad (Face Me) showed after the relaunch; its Skip opened a
  Google Play sheet, closed with ×.
- **O-2 (device switch, before TC-008, 2026-11-18 12:07)** From TC-008 on, R1 runs on the **Samsung S23 (RFCW2198L7B,
  1080 × 2340)**, not the Pixel 8a (user, 2026-11-18). Same build 20.19.0 (90201901), reinstalled by the user
  09:43:36 today. At the switch: Launcher 「Test Server」, Mine Free 「Upgrade to Premium!」, **My Credits 52**
  (Pixel had 0), Wi-Fi on, app English; intro page shown on entry (ticked 「Don’t show again」 + 「Try Now」, the
  one-way state TC-130 already tested on the Pixel). My AI Artwork › Reel Creator already listed 4 works dated
  2026/11/18 (Handheld Camera, Time Lapse, One-Take Shot, Fast Cut) made before the run, and the S23 room shows 6
  Cinestory templates incl. Fast Cut. Evidence: screenshots/s23-setup-start.png, s23-setup-mine.png,
  s23-setup-entry.png, s23-setup-intro-ticked.png.
- **O-3 (before TC-021, 12:11–12:16) — `pm clear` on the S23; credits kept, contradicts KP-133.** Opening
  「single-color-fastcut」 on the S23 showed no swipe guide (already used on this install, screenshots/TC-021-probe-1.png),
  so `adb shell pm clear com.cyberlink.photodirector`, then 「Get Started」, notifications 「Allow」, three What's-new
  pages (NEXT / 「Let's go」), Premium page closed (×), debug dialog **Test server ON**, 「Set to subscriber」 OFF, OK,
  relaunch; a launch interstitial ad (Wink, Google Play 「Install」) closed with 「Close」, a 「New Content ✨」
  popup closed; photo access 「Allow all」 on the first room entry; intro shown again → 「Don’t show again」 ticked.
  Credits: on Production right after the clear a new creditSystemUUID be0565d8 with 0; after Test server ON the app
  went back to UUID **ce659cbc** with **52** (log 12:08 vs 12:12 vs 12:16, logs/R1-a-20261118-121916). So on Test
  Server the credit UUID survived `pm clear` on this phone — **contradicts KP-133** (credits lost with the install);
  matters for R1-h (TC-072 / TC-073 need a balance below the price after `pm clear`). Evidence:
  screenshots/s23-after-clear-1…6.png, s23-debug-before.png, s23-debug-after.png, s23-mine-after-clear.png,
  s23-clear-intro-ticked.png.
- **O-4 (R1-b, TC-024 / TC-033, 2026-11-18 12:20–12:27) — Creative and Cinestory Previews differ.** Cinestory
  Previews (Horror Movie, Micro Cinema, Fast Cut) carry a description line and the 「💡 View photo tips」 chip; the
  Creative stand-ins (single-color-fastcut, cinematic-grade) have neither, and their names are raw keys. AI Transition
  Previews (Selfie Shake, Walking Shift) play no demo: a grey file-icon placeholder only (TC-029). Every Preview opens
  muted. The S23's media volume is 0/15 (left alone); mute checks read the player's state in `dumpsys audio`.
  A slow 10-step `fingerdrag` does not page the Preview; `adb shell input swipe … 250` does.
- **O-5 (R1-b, TC-012, 12:30) — first 「Continue」 on the Edit Room jump dialog did nothing.** Edit Room (Vignette
  applied) › 「Reel Creator」 › 「Continue」 at 12:30:07: the dialog closed, the Edit Room stayed, no photo saved
  (Gallery still 2046). The second try at 12:30:47 (same steps) jumped to the room and saved the edited photo. Not
  reproduced further; log in logs/R1-b-*. Edit Room screenshots come out black on the S23 (secure surface).
- **O-6 (R1-c, TC-049 / TC-136 / TC-050, 2026-11-18 12:39–12:47) — the picker runs an online content check with one
  shared mark.** Every rejected photo gets the same dimmed tile and yellow 「!」 with no message: sizes (299 px,
  4097 px, 11,000,000 B; no content-check line, decided on the phone) and the content check
  (`LibraryPickerActivity: [startReelCreatorContentCheck] <id> failed: NSFW|CELEBRITY`). cr-nsfw-1 failed NSFW
  (12:47:17); cr-nsfw-3 (a screenshot of a grid of small nude thumbnails) and cr-nsfw-2 passed. Two ordinary gallery
  photos failed **CELEBRITY** (ids 148 at 12:39:11 and 131 at 12:40:19; 131 = a man sitting on a wall in a white
  jacket, `screenshots/TC-136-16.png`), so a celebrity-flagged photo exists on the S23: TC-050 (Blocked up front, no
  celebrity photo) could run with it if the user wants. Evidence: logs/R1-c-20261118-125009/by-case/TC-049.txt,
  TC-136.txt, screenshots/TC-049-nsfw.png.
- **O-7 (R1-c, picker handling, 12:36–12:50).** (a) `drag` on the grid was sometimes taken as a tap: one unpicked a
  photo (36 → 35, TC-042) and one dropped a pick (16 → 15, TC-136); taps right after a fling sometimes missed. Read
  the counter after every drag. (b) Reopening the picker from the Preview (「Use Template」) starts empty, but Back
  from the confirm page returns to the picker with the 7 picks kept (R1-d picker memory). (c) The picker keeps its
  grid scroll position between openings, and `drag` toward the top did not reach it; choosing 「All」 again in the
  album list does. (d) The full view opened by a tile's expand icon (TC-135) has 「‹」 and an add-photo icon.
- **O-8 (R1-d, 2026-11-18 12:52–13:14) — picker memory: imported photos lose their grid tick; deletions done by adb.**
  (a) After 「Import」 the tray and counter hold the whole remembered set, but some imported photos have no badge on
  their grid tile: TC-058 (10 into Selfie Shake's 「Select 4 photos」: badges 01–09, d139-2 unticked; tapping it gives
  「You can only select 4 photos.」) and TC-059 (after 2 of 6 deleted: d059-4 / d059-5 unticked; tapping d059-4 adds
  it a second time, 5/30 with a duplicate). TC-054 / TC-055 / TC-133 / TC-057 (no deletion, set within the limit)
  ticked every photo. Likely a photo-id / position mix-up (K03). (b) No 「+N」 on the third prompt thumbnail (TC-054)
  and no red under-/over-limit tray text after Import (TC-057 / TC-058). (c) Gallery deletions for TC-059 and
  TC-137 – TC-139 were done with `adb shell content delete` on the MediaStore rows of the disposable copies only
  (`Pictures/Casebook-CR/disposable/d059|d137|d138|d139/`, 2 + 1 + 2 + 3 files; files gone), with PhotoDirector sent
  Home and brought back with `activate` (no restart). Left on the phone: d059-3…6, d137-2…4, d138-3…4, d139-4.
  (d) Selfie Shake confirm page reads 「Generate | 48」 with 4 photos (first read of its price).
- **O-6 addendum (TC-050, 2026-11-18 13:18–13:21).** The picker's content-check ids are not MediaStore ids (the man in
  the white jacket was 131 in R1-c and 714 now). The man is `DCIM/PhotoDirector/2026-11-13-20-19-38-018.jpg`; a copy
  pushed to `Pictures/Casebook-CR/celeb/cr-celeb-1.jpg` failed CELEBRITY again (13:20:08). O-6's second photo (id 148,
  flagged during TC-042's batch taps) could not be identified: the red-top woman tried as cr-celeb-2.jpg (copy of
  `…-20-19-36-658.jpg`) passed the check. Both copies stay in `Pictures/Casebook-CR/celeb/` (first in All).
- **O-9 (R1-e, 2026-11-18 13:21–13:42).** (a) First 「Next」 from the single-color-fastcut picker with 7 photos showed a
  loading spinner (`loadingPanel`) for ≈ 2.5 min (13:21:40 → ≈ 13:24:10) before the confirm page opened; later Nexts
  took 1–9 s (46 s with 40 photos). No error in the log. (b) Generate prices: single-color-fastcut 70 with 1 and with
  7 photos; cinematic-grade **90** with 15, 16 and 40 photos; Selfie Shake 48 with 4 — flat per template, not per photo.
  (c) The Import prompt is offered only after a 「Next」 in the same launch: after relaunching in another language it
  did not appear for cinematic-grade or Selfie Shake until a set went through Next (cinematic-grade's had also been
  dismissed with 「×」 in TC-066). (d) Launcher shortcut names by language: zh-Hant 「AI電影感運鏡」, ja 「AI シネマ動画」,
  ar 「منشئ الريلز」, de 「Reel-Creator」, pt 「Criador de Reels」 (English still 「Cinematic Reel Creator」, TC-002).
  (e) In zh-Hant / ja the Launcher shows CMS banners in another language (「染出你的風格」 on ja, 「Färb deinen Style」 on pt,
  a Japanese line on ar) — CMS content, not this feature. (f) No crash; app back in English (`launch`, locale en-US).

## O-10 Credit Shop balance stale after a purchase (closest case: none; R1 top-up, 2026-11-18 14:01)
After the 1000-credit test purchase succeeded (log: `[purchase] success credits: phd_1000_credit_freeuser`, `totalRemain=1052` at 14:01:34) and Play's 50%-off follow-up offer was dismissed, the Credit Shop page still showed 「52」 under My Credits (`screenshots/topup-08-balance.png`). Leaving the page, Mine showed 1052. Back from Mine also opened 「Do you want to close PhotoDirector?」 with an ad (Cancel).

## O-11 R1-f generations: timing, upload, charges and a lost refund (TC-083 / TC-117 / TC-143, 2026-11-18 14:03–14:52)
- **Jobs** (all single-color-fastcut stand-in, 7 photos d137-2/3/4, d138-3/4, d139-4, d059-3, Free, Test Server): (1) Generate 14:04:41 → charged 70 at 14:04:44 (1052 → 982), notification 「Reel Creator Ready!」 14:14:16, Done 14:14:22 (≈ 9.5 min); used for TC-083 / 074 / 085 / 141 / 086 / 142 / 087 / 088 / 111 / 118 / 084. (2) triple-tap Generate 14:25:31 → one pack, charged 70 once (982 → 912), notification 14:36:00 (≈ 10.5 min); TC-117 / TC-121. (3) TC-143 14:40:52 → charged 70 at 14:40:55 (912 → 842), Wi-Fi cut 0.1 s later, job never ran, **no refund** although the dialog said 「Unsuccessful, please try again. Credits refunded.」 (Detail: three 「Reel Creator -70」, no refund row; log totalRemain=842 at 14:51:47 and 14:52:47). An earlier TC-143 try (14:40:20) cut Wi-Fi before the credit check: 「Network Error」, no job, no charge. **Credits: 1052 → 842, 210 spent, 70 of it for no reel.** No credits bought in R1-f.
- **Photos upload while picking**, not at Generate: `uploadFile: true` lines run as each photo is ticked (14:04:07–14:04:29); at Generate the pack's UploadFile step lasts ≈ 1 s before Apply, so cutting Wi-Fi 「while the photos upload」 needs a device-side trigger on the `column value: UploadFile` log line (`adb shell "input tap …; logcat -T 1 | grep -m1 'column value: UploadFile'; svc wifi disable"`).
- **Card states:** a processing card reads 「Almost Done」 from its first seconds, with no remaining-time text; its progress segment sits left at 14:04:46 and right at 14:08:48. A failed job's card is a ⚠ tile with 「Retry」 (no 「Resume to Upload」); 「Retry」 flips it to 「Processing… / Almost Done」 with no network call in the log, and reopening My AI Artwork shows ⚠ 「Retry」 again.
- **Stale pages:** after a background job finishes, an open My AI Artwork (resumed from Home or by the notification) is not refreshed; reopening it from the room's history icon updates the card within 1 s. The room's credit pill also stayed at 912 after the TC-143 charge until the Credit Shop refreshed the balance (as O-10).
- **Output:** 1080 × 1920 H.264, 30 fps, 40.0 s, AAC (Save → `DCIM/PhotoDirector/Video/2026-11-18-14-21-01-123.mp4`, kept on the phone). Reel text English (「You made it」, 「Color Trip · 7 of 7 stops」, 「Saved to Color Trip」). Save & Share offers Save, Add Text / Add Sticker / Add Music, 「Make It Reel-Ready」 and Instagram / Snapchat / TikTok / Pinterest. My AI Artwork ⓘ: 「Your creations will only be kept for 1 year. Please download your creations to keep them permanently.」; cards say 「Expires on 2027/11/18」.
- Evidence: screenshots/TC-085-artwork-1.png, TC-088-reopen2.png, TC-117-artwork.png, TC-121-*.png, TC-143-*.png, TC-118-detail.png; recordings/TC-087-play.mp4; logs/R1-f-20261118-145255/.

## O-12 R1-g generations, stale cards, re-creation and test photos (2026-11-18 14:57–15:4x)
- **Jobs** (Free, Test Server, S23): (1) Micro Cinema 14:58:32, d137-3, charged 48 (842 → 794), card 「14 minutes remaining…」, notification 15:04:58 (≈ 6.4 min), 1244 × 1660 (3:4), 8.04 s — TC-096 / 127 / 119. (2) Selfie Shake 15:00:47, dot images d139-4 / d138-4 / d138-3 / d137-4, charged 48 (794 → 746), notification 15:04:35 (≈ 3.8 min), 720 × 1280, 4.06 s: shows an AI-made woman in pink over colour backgrounds, none of the photos recognisable (a selfie template given no-face photos) — not used to judge order. (3) Selfie Shake 15:26:26, people photos s2-A…D in order D, C, B, A, charged 48 (746 → 698), notification 15:31:12, 720 × 1280 — order D, C, B, A visible (TC-101). (4) Micro Cinema 15:27:21 from the room opened by 「Create More」, s2-B, charged 48 (698 → 650), server Done 15:41:28 (≈ 14 min) but the result download timed out (`SocketTimeoutException` → `DOWNLOAD_FAILED`, status DownloadFail, no notification) and the card became ⚠ 「Retry」; one Retry re-downloaded it in 5 s at no charge; 1176 × 1760, 8.04 s — TC-122. Saved …-15-43-32-972.mp4. **Credits 842 → 650, 192 spent (4 × 48), nothing refunded or bought.** Flat price 48 for both Cinestory and AI Transition (spec 40 / button price).
- **Time estimate differs by section:** Cinestory and AI Transition cards show 「N minutes remaining…」 (14 → 12 → 9 min) and a progress bar; the Creative cards in R1-f showed only 「Almost Done」 (TC-085). The estimate was well above the real time (14 min shown, 6.4 min taken).
- **Stale cards after the notification:** at ≈ 15:18 My AI Artwork, opened twice from the room's history icon, still showed both 15:0x jobs as 「Processing… / Almost Done」 although their notifications came at 15:04; the third opening (15:19:30) showed them finished. Again at 15:33 the 15:26 Selfie Shake read 「Almost Done」 after its 15:31 notification until reopened. Adds to O-11's stale pages.
- **Activity re-creation loses the flow:** with Don’t keep activities ON, leaving the app on the confirm page and coming back re-created AICineStoryActivity on the room; opening the picker destroys it, so 「Next」 also lands on the room and the confirm page cannot be reached (TC-116). Switching the system theme (dark → light) while on a Preview likewise re-created the page on the room (TC-146). `settings put global always_finish_activities 1` alone did not apply on this S23 (no re-creation); the Developer options switch did.
- **Picker rejects large people photos:** 3456 × 5184 … 4000 × 6000 JPEGs (1–2 MB) from DCIM/1_Fashion got the 「!」 mark (over the 4096 px long side, TC-047); 1600 px copies were accepted. Copies stay in `Pictures/Casebook-CR/selfie/` (s2-A…D, first in All); the 6000 px ss-A…D copies were deleted again (MediaStore row + file).
- **Import prompt thumbnails** for Selfie Shake's set followed the pick order (d137-4, d138-3, d138-4), not the reordered confirm order (TC-102).
- **Saved to the phone (kept):** DCIM/PhotoDirector/Video/2026-11-18-15-20-49-868.mp4 (Micro Cinema), …-15-22-14-120.mp4 (Selfie Shake run 1), …-15-33-08-881.mp4 (Selfie Shake run 2). The screen recording `recordings/TC-127-play.mp4` came out empty (34 KB); playback was judged from the saved file.
- System settings: theme read **dark** at 14:57 (`cmd uimode night` yes, ui_night_mode 2), light 15:29–15:30 for the TC-146 comparison, back to dark; Don’t keep activities read **0**, ON 15:10–15:18 (TC-116), OFF again (0).

## O-13 R1-h pm clear and the phone used by someone else (2026-11-18 15:46–19:14)
- **pm clear 15:46:31 on the S23:** consent, notifications, What's-new, Premium page, ad and New Content popup as in O-3. Production right after the clear: UUID be0565d8 with 0; after Test server ON: UUID **ce659cbc with 650** again (log 15:50:29–31). O-3 repeats: on Test Server the credit UUID (method=ANDROID_ID) survives `pm clear`, so a clear never brings the balance below a price. Intro shown again after the clear (ticked Don't show again); photo access asked again (Allow all). Evidence screenshots/r1h-*.png.
- **Phone used outside the run while R1-h was paused (15:54 → 19:11):** 16:26–16:46 debug dialog changed (isSubscribed(premium) at 16:32), new credit UUID **8a31d4be** with 0, a +50 purchase (16:34), two AI Background jobs -6 each → **38**; PhotoDirector crashed 17:28:38, 17:31:49, 17:37:07 (`IllegalStateException: Cannot call this method while RecyclerView is computing a layout or scrolling`, logs/R1-h-blocked-20261118-191445); at 19:13 the U app was in front (chat with Reel Creator recordings sent 17:38–17:39). Not this run's actions; R1-h stopped untouched.
- **Addendum 2026-11-19 09:06:** the user chose to use the 38 credits on UUID 8a31d4be, but at the restart the same UUID held **204** (purchase_cp50 12 + purchase_cp500 192). The history shows more use after 16:46, all outside the run: +500 purchase 16:57, AI Transition jobs (-72, -48 ×3, 17:31–17:36), +50 purchase 17:35, returns +72 / +120 / +72. The tier was Premium (「Hello VIP!」). R1-h stopped again before any case; the subscriber flag was left ON as found.
- **Addendum 2026-11-19 09:26:** after the user spent the credits and set Free (12 credits on 8a31d4be at 09:20:34), Test server was toggled off and on at 09:20:40–44 (`NetworkManager: enable get fake credit uuid`). Since then the app resolves no credit UUID (`creditSystemUUID=, method=UN_KNOWN`; `getCreditRemain error: creditSystemUUID = null`). Mine and the room pill show 「--」, and two relaunches did not bring it back. The debug dialog shows Test server ON, subscriber OFF, Support ScreenShot for free user ON. R1-h stopped again without running a case. (Possible finding for later: the app shows 「--」 with no credit account on Test Server after a server toggle.)
- **Addendum 2026-11-19 09:36–09:52, R1-h run:** the user reset the credits. The app is Free on Test Server with credit UUID b3a561f0 holding 0. TC-072 (Free, 0) opened the Premium paywall. TC-073 (subscriber ON, 0) showed 「More Credits Required!」, and 「GET CREDITS」 opened the Credit Shop. On that first Credit Shop entry the daily bonus issued 「3 Free Credits Have Been Issued to You」 (valid 1 day), followed by 「Check Backup Protection」 (Later). The balance is now 3. On this pass the room showed real section names (「Cinematic Styles 📽️」, 「Year-End Recap ✏️」, 「Cool Transitions 🎞️」), and the picker opened on 「Sample Photos」. While trying to reach Settings by blind adb taps I opened My AI Artwork by mistake: a failed outside-run card (Motion Hop, 2026-11-19) showed 「An Error Has Occurred — The credits have been refunded.」 and was dismissed with OK.
