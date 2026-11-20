# Creative Reel (Android) — what the phone needs before a run

What a run needs on the phone or the account, because none of it can be committed. Check it before the first segment;
a new row that needs a new photo or account state adds it here in the same draft.

## Phone, app and account (Pixel 8a, from round 1, probe 2026-11-17)
- Phone: Google **Pixel 8a** (akita), adb serial **42201JEKB02229**, Android 16, 1080 × 2400, on USB, Stay awake on
  (`stay_on_while_plugged_in` 15), no keyguard, system theme **dark** (`cmd uimode night` → yes), locale en-US.
  Always pass the serial; run device and adb commands with `MSYS_NO_PATHCONV=1` in Git Bash. The S23 (RFCW2198L7B)
  is also attached: never use it for this run.
- Build: **TR261113-0038**, PhotoDirector for Android 20.19.0, versionCode **90201901**, fresh install by the user
  2026-11-17 16:50:09 (`dumpsys package`: firstInstallTime = lastUpdateTime). Do not download or reinstall; eBugs
  from this run go to TR261113-0038. Launcher shows 「Test Server」.
- Entry on this build: Launcher shortcut grid, page 2 (`drag 900 1270 150 1270`) › 「Cinematic Reel Creator」 (the
  build still uses the old name; TC-002 checks it). The AI Videos tab also lists 「Cinematic Reel Creator」. The intro
  page (`reel_creator_tutorial_page`: 「Reel Creator」, 「Try Now」, unticked 「Don’t show again」) **shows on entry**
  (probe: entered once with 「Try Now」, box not ticked).
- Room on this build (Pixel, 2026-11-17): three sections with raw string keys as titles —
  `ReelCreator_Category_Cinestory` (**6** templates: Horror Movie, Micro Cinema, Fast Cut, One-Take Shot, Time Lapse,
  Handheld Camera; the S23 probe saw 5, no Fast Cut), `ReelCreator_Category_CreativeR` (2: 「single-color-fastcut」,
  「cinematic-grade」, now with pixel-game thumbnails), `ReelCreator_Category_AITransit` (2: 「Selfie Shake」,
  「Walking Shift」, grey placeholder thumbnails). **No Year-End Recap section and no 「Top 5 of My Year」.**
- Stand-in templates for rows written on 「Top 5 of My Year」 (5–15 photos): 「single-color-fastcut」 (1–30 on the
  S23) for the picker-memory, confirm-page and generation rows (7 photos fit); 「cinematic-grade」 (15–40 on the S23)
  for the range rows (below-minimum, minimum, maximum + 1). Re-read both ranges on the Pixel in R1-c; record the
  stand-in and its range in Actual; expected numbers that assume 5–15 are compared with the stand-in's own range, and
  the missing template is TC-023 / TC-024's finding.
- Tier: Free / Premium only by the About backdoor (KP-131): Launcher gear (`topToolBarSettingBtn`) › About › tap just
  below 「‹」 until the debug dialog › 「Set to subscriber」 ON (Premium) or OFF (Free) › OK › relaunch. Mine:
  「Hello VIP!」 / 「Upgrade to Premium!」. Never a sign-in. At the Pixel probe: **Free, signed out, 2000 credits**
  (Mine 「My Credits 2000」; Mine advertises 「Enjoy 50% off credit pricing」 for Premium, so prices may differ by
  tier: R1 generates on Free).
- Fresh state: the intro page and the first Preview swipe guide (TC-021) are both still unused on the Pixel (the
  probe opened no template). **`pm clear` loses the credits** (they belong to the install's UUID, KP-133): only before
  the top-up, and only on the user's decision. After a clear: 「Get Started」 on the consent screen, allow every
  permission, check Mine (the clear also resets 「Set to subscriber」).
- Credits: Generate prices read on the S23 (same build) — Creative 「Generate | 70」 (single-color-fastcut, 1 photo),
  Cinematic 「Generate | 48」 (Handheld Camera), AI Transition 「Generate | 72」 (Walking Shift, 6 photos); 「Selfie
  Shake」 (4 photos) not read; not re-read on the Pixel (it needs a Preview, which would spend TC-021's swipe guide).
  The table expects 60 / 40. The user tops credits up (2026-11-17) and generation rows run (record the balance before
  and after every generation). TC-072 (Free, below the price) and TC-073 (Premium, below the price) run while the
  balance is still below the price — at 2000 on the Pixel that needs the user's decision (run plan).
- Buying credits (user, 2026-11-17): when the balance is below the next generation's price, the run may buy a credit
  pack in the app's Credit Shop, only when Google Play's sheet names a **test card** (e.g. 「Test card, always
  approves」); any real card or a password prompt stops it. Before tapping Buy, the segment stops and the
  orchestrator asks the user in chat with the pack, price and card; it buys only on that yes. Never tap the Menu's
  QA consume / purchase rows.
- App language: `launch --lang zh-Hant|ja|ar|de|pt`, then a plain `launch` (per-app language on Android 16).
- Developer options › Don't keep activities (TC-116, `always_finish_activities` 0 at the probe): a system setting,
  only with the user's go-ahead; turn it off right after.
- Dark theme (TC-146 – TC-149): the Pixel is already dark; switching light / dark (`adb shell cmd uimode night
  yes|no`) only with the user's go-ahead; end on dark.
- Share apps on the Pixel: Facebook only (no Instagram, TikTok, LINE, X).

## Photos in the gallery (Pixel, checked 2026-11-17: 639 images, 178 videos)
| Need | Used by | On the Pixel 8a |
| --- | --- | --- |
| 41+ photos for the 15–40 stand-in and 30+ for 1–30 | TC-041, TC-042, TC-070 | yes (`PhotoDirector` 101, `1_Scene` 99, `1_Fashion` 76, `1_Headshot` 74) |
| 7 and 10 different photos, landscape and portrait | TC-044, TC-053 – TC-087 | yes (245 landscape, 366 portrait, 28 square) |
| 299 px short side; exactly 300 px and 4096 px; 4097 px+ long side | TC-045 – TC-047 | made by the run (exact sizes); near ones exist (13 under 300 px short side, e.g. `Jau15.jpg` 197 × 436; 213 over 4096 px long side, e.g. `IMG_5905_12m.jpg` 4212 × 2808) |
| JPEG 1200 × 1200 padded to 11,000,000 B and 9,900,000 B | TC-048, TC-126 | made by the run; fallbacks `10.jpg` 10,111,088 B (4896 × 3264), `Previous_Source (17).jpg` 9,714,273 B |
| NSFW test photo | TC-049 | **not on the Pixel**; push one from this computer: `~/Desktop/BUG/PHD/2026/2026 1月/PHD_0128/NSFW/` (local QA material) to `/sdcard/Pictures/Casebook-CR/nsfw/` in R1-c |
| Celebrity photo | TC-050 | **no** (Blocked up front) |
| 4 disposable photos per row (12 in all) | TC-137 – TC-139 (each deletes 1 / 2 / 3 of its 4 in the Gallery) | made by the run: copies pushed to `/sdcard/Pictures/Casebook-CR/disposable/` (`d137-1.jpg` … `d139-4.jpg`) at the start of R1-d |
| Album to open the picker on | TC-051 | no `Casebook` album on the Pixel; `Casebook-CR` appears once the run pushes its files |

Test photos the run makes: write them with Python (Pillow 9.5 on this computer) into the scratchpad, `adb -s
42201JEKB02229 push` to `/sdcard/Pictures/Casebook-CR/`, then `adb -s 42201JEKB02229 shell am broadcast -a
android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/Pictures/Casebook-CR/<file>` for each.

## Not available
- Deeplink URLs (old Cinematic Reel Creator link, Creative / AI Transition / CineStory template GUIDs, a bad GUID, a
  category link): TC-014 – TC-020, TC-114 (Q-15).
- Celebrity test photo: TC-050.

## Earlier phone: Samsung Galaxy S23 (probe only, 2026-11-17)
SM-S9110, serial RFCW2198L7B, Android 16, 1080 × 2340; same build 90201901 (installed 09:46:39). Probe in
`runs/_probe-2026-11-17/`: Free, 0 credits; Cinestory 5 templates (no Fast Cut); Creative 「single-color-fastcut」
1–30 and 「cinematic-grade」 15–40 with grey placeholders; prices 70 / 48 / 72 (above); no Text language row seen on
the confirm page; the S23 used up its first Preview swipe guide. Its gallery (2045 images) had the `NSFW` album and
the `Casebook` album the Pixel lacks. Not used for R1.
