# Domain knowledge for pdr/christmas-new-year-sale (android), for analysis

## rule

### KP-007 A failed generation refunds its credits (authority team)
A failed item costs nothing net; a partial failure costs only the items that succeeded. A missing or wrong refund is
a defect with its own eBug, even when the failure itself is already filed.

### KP-066 Android text is held to the Android equivalent of the iOS font (android, authority spec, unverified)
The Design Figma is drawn for iOS in SF Pro. On Android the standard is Roboto: SF Pro Regular 400 → Roboto Regular
400, Medium 500 → Roboto Medium 500, Semibold 600 → Roboto Medium 500 (the board labels it 「Semibold/500」). Figma's
variable SF Pro weights between these (Medium 510) count as the nearest named weight. The board gives no size mapping,
so a size in pt is the same number in sp. The design check (`scripts/design.ts`, `ANDROID_WEIGHT`) judges Android
weights this way.

## risk

### KP-077 AI Style Transfer turns portrait photos sideways (android)
AI Cartoon (Elf) and AI Sketch (Oil Painting) on an upright portrait photo (DSC_0047.JPG) return the image turned 90°
in the preview and the export; likely EXIF orientation. Use portrait photos with EXIF rotation when testing them.

## question

### KP-028 No Design for the notification centre
No Design sheet covers the notification centre. Open for PM/Design: what 「Try Now」 may open (external sites, a mark
or confirmation), per-entry unread state, multi-open accordions, refresh frequency and paging.

### KP-037 VIP or Pro+
The top tier is called 「VIP」 on the Mine card and in Design F13 but 「Pro+」 on the My Cloud storage badge, the
paywall and Design F14/F17 (which also draw the subscribed bottom tab as 「Pro+」; the build keeps 「Mine」). Whether
they are one tier is for PM (ISS-MP-25); don't file the mix as a defect meanwhile.

### KP-061 Completion and error states the specs leave open
CineStory F17 says inform users 「when the task is done」 without saying server-done or downloaded. The banner button
is 「View」 in CineStory F02 and 「View Result」 in Video Object Removal F116 (the build says View). The F15 error
states 「Retry」 and 「View Details」 were never reached.

## quirk

### KP-069 The Sony XQ-BT52 cannot play 4K 60fps (android)
The Sony XQ-BT52 (Xperia 10 III, Snapdragon 690) hardware decoders stop at 3840×2160 30 fps (4096×2160 24, 1080p
120); a 4K 60 H.264 clip fails at decoder setup (`InsufficientResources`, 「Failed to initialize decoder」) in any
player, while 4K 30 plays. A 4K 60/120 result that will not play on it is a phone limit, not an app bug; check
4K 60 playback on the Samsung SM-A5360. Whether the app should offer 4K 60 on such phones is a PM question.

## fact

### KP-003 Android debug controls (android)
Android has no Pink, no fault switches, no tier switch, no Write Log and no developer-server switch. Launcher ☰ ›
Menu ends with a QA block (download all contents, scoped-storage migration, 「QA: consume all non-consumables」, 「QA:
show all subscription plans」, 「QA: purchase SKU test」, region): never tap the consume or purchase rows. Fault
switches are planned for a later build (user, 2026-10-28): recheck on each new build.

### KP-006 Android tiers and chat limits (android)
Android sells Pro, not Pro+, through Google Play billing; the tier comes from the signed-in account. Daily chat limits
are server-configured: Free 10, Pro 100.

### KP-011 Design 8/E is the leading Launcher sheet (unverified)
Of the Launcher Design sheets, 「Template Page - Launcher supports banner (TBD) (8_E)」 matches the build (three content
rows, five bottom tabs, 「View more」). Older sheets drawing 「See All」, four tabs or two rows are superseded: never
file against them. The big-shortcut list follows 8/E F14 (…Video Enhance), not F04 (…Cinematic Reel Creator).

### KP-012 Shortcut tiles come from the CMS (unverified)
Which tools the Launcher's small shortcuts show (and in what order) is set on the CMS (Design: 「Shortcut on CMS」), up to
16 tiles over two pages. A tile list that differs from the Design is not a defect; reach a tool through AI Magic when
it is not on the first page.

### KP-041 Daily free credits (unverified)
My Credits carries 「Complimentary daily credits / Claim once every 24 hours / Claim」; a claim gives 5 credits
(toast 「5 Credits Received · valid for 7 days」). Yet 「Expiring within 7 days」 stays 「0 credit」 after it
(ISS-MP-27, DRI261893-0042). Android's Mine › Credit page shows the same 「Complimentary daily credits ‹Claim›」
offer (16.9.0 build 2611091); its amount there is unchecked.

### KP-071 Buying credits is followed by an offer and a backup dialog (android)
After a 500-credit test purchase the app offered 「Want to get 50 Credits, too?」 (「NT$170.00」, 「Not now」); 「Not
now」 then opened 「Check Backup Protection」 over My Credits (「Back up now」, 「Later」, 「Don't show again」 unticked).
Neither is in a feature spec; close both before the next step.

### KP-072 What a Pro purchase or sign-in changes on Android (android)
A Pro purchase adds 「Monthly Credit Bonus (for Pro Subscribers) +100」 (iOS: +50, KP-043), turns the Launcher's last
tab into 「Pro」 with a VIP icon instead of 「Mine」, and the next Launcher shows a 「Use credits to enjoy AI features /
Congrats! 100 monthly credits have been added with your Pro subscription」 dialog (system Back closes it). The tier
follows the Play account, so after `pm clear` the app reads Pro before sign-in. Google-button sign-in opens
「Welcome! Enter your email to get started」 with a marketing box ticked by default and adds 「Loyalty Credit Bonus
(for PowerDirector Subscribers) +30」. Logcat's `acknowledgePurchaseResponse 2 Server error` at purchase has no
visible effect.

### KP-076 AI Anime Video from the editor is slow and adds a clip (android)
AI Anime Video started from the editor (Vivid 10 s) took about 22 minutes (「17 minutes left…」); 「Add to Timeline」
puts the result after the source clip, not in its place. Start it early in a segment.

### KP-079 Some tools save their result to the gallery by themselves (android)
Video Edit by Chat, Talking Avatar and AI Anime Video write the result to the gallery when the task finishes, with no
「Save」 tap. Character Motion Swap, Cinematic Reel Creator and Text to Video do not. Whether this is intended is not in
any spec.

### KP-080 What a second Save does (android)
A Text to Image result saved once is never written again: a second 「Save」 says 「Saved to Gallery」 and leaves the
first file as it was. AI Art, Image to Video and Text to Video write a new file on every Save. In Image to Video file
names the number after the date counts saves, not tasks.

### KP-082 Models and tools offered on Android (Free) (android)
Image to Video: Veo 3.1, Vidu Q2, Kling O3, Kling 4.0, Pixverse V6, Wan 2.7, Gemini Omni Flash 1.1, Happy Horse 1.1;
Seedance 2.0 and 2.5 are Pro (「Subscribe Pro to Unlock」); no Flux or Hailuo. Text to Video: Kling 4.0, Wan 3.0,
Seedance 2.5 / 2.0 (Pro), Gemini Omni Flash, Happy Horse 1.1, Wan 2.7, Veo 3.1, Kling O3; no Vidu, Pixverse, Hailuo
or Flux. Text to Image defaults to 「GPT-Image-2.6 Sunburst」. Video Object Removal is not offered on Android.

### KP-085 AI Storytelling results live in its own history (android)
AI Storytelling results are not in My Artwork: they are under AI Storytelling › history 「Generated Story」 and are
exported, not saved. A Free account gets one free story; more need Pro.

### KP-086 AI Music Generator on Android (android)
Android has AIMusicGeneratorV2 (log: Google Lyria 3 Pro): Genre / Mood / Theme chips, song length and number of songs
(default 2, 「Generate for ◆ 10」, 5 credits a song); no description box and no lyrics path, unlike the PM board
(「Generate for ◆ 6」). Opening it from AI Magic creates an editor project 「AI Music Generator <MM-DD>」 behind it.

### KP-088 AI Voice Changer on a Free account (android)
On Free only the 「Effect」 tab applies: Radio 1 / Radio 2 free, Telephone / Chipmunk Pro. Every Professional /
Mellow / Bright AI voice is Pro (a tap plays a 10 s preview with 「Unlock the 10-second limit now」). An Effect voice
charges nothing.

### KP-090 AI Art's result page has no 「Full Editor」
AI Art results cannot be opened in the editor: the result page has no 「Full Editor」 (Android shows feedback, share,
download and 「Turn the image into a video」). A spec rule for every image result that names 「Full Editor」 (AIGC
Watermark R-024) applies to AI Art without that step; Text to Image does have it.

### KP-091 Credit prices seen on Android (Free, Stage) (android)
Text to Image 3, AI Art 6, Text to Speech 2, Talking Avatar 10, AI Music Generator 5 a song; Image to Video Veo 3.1
4 s 32, Vidu Q2 15, Kling O3 25, Pixverse V6 20, Wan 2.7 40; Text to Video Kling O3 30, Veo 3.1 4 s Fast 28, Wan 2.7
720p 25; AI Anime Video Vivid 10 s 40; Video Edit by Chat Gemini Omni Flash 1.1 72, Kling O3 45; Character Motion Swap
Wan 2.2 Animate 39, Kling Motion Control 60; Cinematic Reel 70. AI Cartoon and AI Sketch charged nothing although the
feature list prices them at 1. Prices are server-set: recheck on each build.

## term

### KP-023 Meme Dance Creator
The Launcher's second row is 「Meme Dance Creator」 in the build. Design 8/E and the more-content-promotion sheet also
say 「Meme Dance Generator」; use the build's name and don't file the difference (a spec self-contradiction for PM).

### KP-038 Advanced Cutout and AI Smart Cutout
One capability: the Mine Free card calls it 「Advanced Cutout」, the paywall's Compare plans 「AI Smart Cutout」.

<!-- knowledge hash: b922a415a55fb670 -->
