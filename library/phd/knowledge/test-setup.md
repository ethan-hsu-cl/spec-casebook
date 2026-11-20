# Round-start setup

## KP-104 A round starts as a free user with 0 credits
- kind: howto · platform: both · use: run · tags: setup, account, credits
- source: PHD domain test-setup.md (user, 2026-10-16; the source labels it K36) · aka: K36

Check once per round, before its first case and separately for each platform's round: free user and balance 0. Do
not redo it per case, nor when the round's plan later switches the subscription or buys test credits.

## KP-105 Resetting the account through the debug dialog
- kind: howto · platform: both · use: run · tags: setup, debug, account
- source: PHD domain test-setup.md (user, 2026-10-16)

Edit Room › Settings › About: tap the backdoor button under [<] until the debug dialog opens. Turn 「set to
subscriber」 off, reset UUID and member token each with the 「rest」 button in its own row, tap OK, close and reopen
the app (never clear app data). Check again; if it cannot be confirmed, record the setup Blocked `--as test-data`.
On Android 20.19.0 Settings is the Launcher gear (top right), and the dialog is reached as in KP-131. There (S23,
batch-editing R3-g, 2026-11-13) the dialog view showed only switches (Test server, Set to subscriber, Support
ScreenShot for free user, Show landmark for Muse, Force fetch remote config value, Force show UGC tab), no UUID or
member token rows; where the reset rows are on Android is not known yet.

## KP-106 The account reset is setup, not a row
- kind: howto · platform: both · use: run · tags: setup, privacy
- source: PHD domain test-setup.md (user, 2026-10-16)

Never a table row or a per-case cleanup, never a mid-round recovery after works, spends or a pending payment. Keep
before / after screenshots and a log line; mask UUID and member token. Change no other debug option. On the QA
iPhone it replaces reinstalling.

## KP-131 Switching Free / Premium on Android with 「Set to subscriber」
- kind: howto · platform: android · use: run · tags: setup, debug, tier, subscription
- source: user 2026-11-09 (chat; inbox I-002); batch-editing run 2026-11-13-r3 R3-a, R3-g (S23); creative-reel run 2026-11-17-r1 O-1, O-3, O-13 (Pixel 8a, S23); i2v-reuse run 2026-11-19-r1 R1-setup (Pixel 8a); ai-hair-color-custom run 2026-11-20-r3 R3-e, R3-f (Pixel 8a, on and off) · verified: 20.19.0 (90201901) (2026-11-20)

No sign-in needed. Launcher gear (top right, `topToolBarSettingBtn`) › About: tap repeatedly just below the ‹ button
until the debug dialog opens; turn 「Set to subscriber」 on (Premium) or off (Free), tap OK, then relaunch the app.
Mine shows 「Hello VIP!」 for Premium, 「Upgrade to Premium!」 for Free; the credit balance is unchanged. Change no
other debug option (KP-106).

## KP-132 TR builds cannot update a Play Store install
- kind: quirk · platform: android · use: run · tags: setup, install
- source: orchestrator, i2v-reuse R1 setup 2026-11-09 (inbox I-001) · verified: 20.19.0.v202611061839 (2026-11-09)

A PhotoDirector installed from the Play Store (20.18.0 on the SM-A5360) is signed with a different key from a TR
build: `adb install` fails 「INSTALL_FAILED_UPDATE_INCOMPATIBLE」 and the store app has to be uninstalled first.

## KP-133 Credits do not survive an uninstall without sign-in
- kind: quirk · platform: android · use: run · tags: setup, credits, install, uuid
- source: orchestrator, i2v-reuse R1 setup 2026-11-09 (inbox I-001; second-hand, one occurrence) · verified: 20.19.0.v202611061839 (2026-11-09)
- status: superseded by KP-136

6,000 test credits added on a not-signed-in install were gone after uninstall and reinstall: the Image to Video pill
and Buy Credit › My Credits both read 0, with no sign-in prompt on the way. The balance looks tied to the install's
UUID, not an account (not confirmed). Plan credits again after any reinstall.

## KP-136 Each server keeps its own credit UUID, and `pm clear` does not reset it
- kind: quirk · platform: android · use: run · tags: setup, credits, install, uuid, server, pm-clear
- source: creative-reel run 2026-11-17-r1 O-1 (Pixel 8a), O-3 and O-13 (S23, two `pm clear`s); corrects KP-133; ai-hair-color-custom run 2026-11-20-r3 R3-a (Pixel 8a Test Server 0 again) · verified: 20.19.0 (90201901) (2026-11-20)

The credit balance belongs to a creditSystemUUID per server, not to the install. Turning 「Test server」 on or off
switches to that server's UUID and balance (Pixel 8a: Production 1875 → Test Server 0). On Test Server the UUID is
derived from the device (log `method=ANDROID_ID`): after `pm clear` the S23 got back the same UUID and balance (52,
then 650), and its Production UUID was also the same after both clears. So a clear (and likely a reinstall of the same
build) never brings a balance below a price; spend it down instead. KP-133's loss after a Play Store → TR reinstall
stays one unexplained occurrence (different signing key or server, not known).

## KP-137 After `pm clear`, turn 「Test server」 on again
- kind: howto · platform: android · use: run, ebug · tags: setup, server, pm-clear
- source: user, swipe-collage eBug review R1 2026-11-12 (F-46; inbox I-005, was swipe-collage KF-002); creative-reel run 2026-11-17-r1 O-3, O-13 · verified: 20.19.0 (90201901) (2026-11-18)

`pm clear` puts the app back on Production with the debug switches reset. Before going on, open the debug dialog
(KP-131), turn 「Test server」 on (and 「Set to subscriber」 as the plan needs), OK, relaunch; the Launcher then shows
「Test Server」. Otherwise templates may open blank or say No connection (Swipe Collage). On the way the cleared app
shows consent 「Get Started」, notifications, three What's-new pages, a Premium page (×), on a Free relaunch often an
interstitial ad (its Skip / Install opens Google Play: close it) and a 「New Content」 popup; photo access and feature
intros are asked again.

## KP-138 「Don't keep activities」 from Developer options, not `settings put`
- kind: howto · platform: android · use: run · tags: lifecycle, setup, adb
- source: creative-reel run 2026-11-17-r1 O-12, TC-116 (S23) · verified: 20.19.0 (90201901) (2026-11-18)

On the S23 `adb shell settings put global always_finish_activities 1` alone did not destroy PhotoDirector's
activities (same instance after Home and back). Turn the switch on in Settings › Developer options and check that the
Activity is re-created before judging a row (KP-011); turn it off again after.

## KP-139 Edit Room screenshots are black on the S23
- kind: quirk · platform: android · use: run · tags: screenshot, edit-room, evidence
- source: creative-reel run 2026-11-17-r1 O-5 (S23) · verified: 20.19.0 (90201901) (2026-11-18)

`adb` screenshots of the Edit Room come out black on the S23 (secure surface); the screens around it capture
normally. Record the Edit Room state from the page source or the log, or by what the next screen shows.
