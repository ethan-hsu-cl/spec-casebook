# Run state — R1 Round 1: full run of table v3 on 20.19.0.v202611181947 (TR261118-0070), Pixel 8a

Table: library/phd/i2v-reuse/android/cases.csv
Started: 2026-11-19T03:02:04.232Z

## Environment
(build, server, device, tier, credit balance, Pink toggles, Log stage timings, Write Log)

## Checkpoints

## R1-setup fixtures (2026-11-19, Pixel 8a, Test Server, credits read on the Custom tab pill)
Path: Launcher › AI Videos (bottom tab) › Image to Video (first visit showed the 「Image To Video」 intro and a 「Steps」
page: 「Try now」 / 「Continue」 tapped, 「Don't show again」 NOT tapped). Custom tab default model on this build:
**Kling 3.0** (price 30 with no settings changed). Settings sit below Inspiration (scroll the Custom tab): Duration
(Seconds), Video Quality, and the sound row is labelled **「Generate Background Sound」** (Off / On, ⓘ) on Kling 2.6,
not 「Generate Sound by AI」 as the table says. Generate jumps straight to My AI Artwork › Image to Video.
Photos: the picker's 「Sample Photos」 album has faces (3 women, woman with yellow background, man…) and non-face
photos (croissant, tram street); nothing pushed.

| Video | Settings | Price on Generate | Balance before → after | Started → finished |
|---|---|---|---|---|
| A | Custom, Kling 2.6, 10s, Pro, Generate Background Sound On, Start/End Off, sample photo woman on yellow, prompt 「Fixture A: the woman smiles and waves at the camera, gentle breeze in her hair」 | 80 (25 with 5s / Sound Off) | 1839 → 1759 | 11:05:28 → ~11:22:40 (1007 s; tile said 17 min) |
| B | Custom, **Kling 2.5 Turbo**, **5s**, **Standard**, Generate Background Sound **Off**, Start/End Off, woman on yellow, prompt 「Fixture B: the woman turns her head slowly and laughs」 | 25 | 1759 → 1734 | 11:24:19 → done by 11:40 |
| Failed job (TC-004) | Custom, Kling 2.5 Turbo, 5s, Standard, Sound Off, **Start/End On** (first: woman in straw hat, last: dark-haired woman in brown jacket), prompt 「Fixture C: the first woman turns into the second woman with a smooth transition」 | 15 | 1734 → (refunded: pill 1704 after D's 30) | 11:25:27 → **failed naturally** 11:38:41, tile shows 「View Detail」 (log: `status=Error … desc=External Error, errorCode=4000 … errorCode=4001 general error`, packID image_to_video_credit_create_1795058730647). Not opened yet. |
| D | Custom, **Kling 3.0** (default), inspiration 「A dog is happily running toward its owner with excitement.」 (3rd thumbnail; tapping it asked 「Use Another Inspiration?」 → Continue; it fills the prompt only, the photo stayed: woman in straw hat), 5s, Standard, Sound On | 30 | 1734 → 1704 | 11:26:34 → done by 11:40 |
| C | Custom, Kling 3.0, 5s, Standard, Sound Off, **Start/End On** (first: man with hot-air balloons, last: man sitting on white steps), prompt 「Fixture C: the man looks around and smiles as the scene changes」 (Premium by then) | 20 | 1674 → 1654 | 11:43:26 → see below |
| F | Custom, **Wan 3.0** (limit 20000), 5s, Standard, Sound On, dark-haired woman, prompt 「Fixture F long prompt. Sentence 1: … END」 = **2129 characters** (set with `setval`; counter 2129/20000) | 20 | 1654 → 1634 | 11:44:15 → see below |


Video A Save & Share (tile tap): 「Prompts & Settings」 card shows Kling 2.6, chips 「10s」 「pro」 (lowercase) 「Sound on」,
the prompt, and 「Reuse」 (top right of the card). **Feature present in this build.** Screenshot setup-a-saveshare.png.

C (Kling 3.0, Start/End) and F (Wan 3.0, 2129 characters) finished by 12:06; D, B finished by 11:40.

### Video G (TC-034): cannot be made on this build
Tier was **Free** at segment start (Mine 「Upgrade to Premium!」). Seedance 2.0 on Free opened the 「PhotoDirector Premium」
paywall on Generate (closed with Back, nothing charged), so the tier was switched to **Premium** with the About debug
dialog (「Set to subscriber」 On, KP-131; Mine 「Hello VIP!」, screenshot setup-mine-premium.png) at ~11:37.
Every model in the list was then given a photo with a face (sample photos) and Generate: **none showed 「The photo you
uploaded includes a real person…」**; all 18 started (Seedance 2.0 / 2.5, Veo 3.1, Gemini Omni Flash 1.2,
Vidu Q2 / Q3 / Q4, Pixverse V6, Kling O1 / O3, Happy Horse 1.1, Wan 2.7, and Kling 4.0, which started and then failed
at 12:23:54 with the same `External Error 4000 / 4001 general error` as the first C (no real-person message; its 45
was refunded: balance 1303 before and after); plus Kling 2.6, 2.5 Turbo, 3.0 and
Wan 3.0 from the fixtures). The string exists in the APK resources. So no model on this build/Test Server refuses a real
person at Generate → **TC-034 Blocked test-data** ("no model refuses a real-person photo on 20.19.0.v202611181947, all
18 tried 2026-11-19"; Q-12). Probe videos (prompt 「Probe G: the woman blinks」 / 「Check G: the woman smiles」) stay in
the tab; any of them is a Custom video for other rows. Probe prices: Seedance 2.0 30 (5s Std Off), Seedance 2.5 **120**
(default 10s/Pro, by mistake), Veo 3.1 20 (4s Std Off), Gemini 25, Vidu Q2 15, Vidu Q3 16, Pixverse V6 20, Kling O1
20, Kling O3 20, Happy Horse 25, Vidu Q4 25, Wan 2.7 25, Kling 4.0 45 (5s Std On).

### Notes for the rows
- **TC-032**: no model on this build has a 500-character limit. Limits (counter): Kling 4.0 3000, Pixverse V6 2000,
  Kling O3 2500, Seedance 2.5 / 2.0 20000, Gemini Omni Flash 1.2 20000, Vidu Q4 5000, Wan 3.0 20000, Happy Horse 2500,
  Veo 3.1 4000, Kling 3.0 / 2.6 / 2.5 Turbo / O1 2500, Vidu Q3 / Q2 2000, Wan 2.7 5000. F (2129 characters) therefore
  goes over the 2000 of **Pixverse V6 / Vidu Q3 / Vidu Q2**: already seen in the room, Vidu Q2 with F's prompt showed
  counter 2129/2000 and Generate disabled. Run TC-032 with Vidu Q2 (or Pixverse) as "the model whose limit is lower".
- **Start/End switch** is disabled for Vidu Q4 and Happy Horse 1.1.
- Duration chips differ per model (Veo 3.1 4/6/8, Vidu Q3 4/8/16, Vidu Q2 / Wan 2.7 5/8, Kling 3.0 / O3 / 4.0, Seedance,
  Pixverse, Happy Horse, Vidu Q4 5/10/15, Kling 2.6 / 2.5 Turbo / O1, Gemini 5/10); Kling 2.6 has only 「Pro」; Gemini
  only 「Standard」.
- The Custom room keeps the last model, photo and prompt after Generate → Back; the first-entry intro (「Image To
  Video」 Try now + 「Steps」 Continue) shows at **every** entry from AI Videos (「Don't show again」 never tapped).
- Template video for TC-007: the tab already holds template videos 「Santa Squad」 and 「Santa」 (2026/11/18).
- Prices on Free vs Premium for the same settings were not compared.
- The account is shared: the credit history shows AI Creative Studio charges at 09:34–09:41 (09:34–09:41 local) from
  another device; compare balances by ledger rows, not by difference.

### End of R1-setup (12:25)
- Tier restored to **Free** (「Set to subscriber」 Off, OK, relaunch; Mine 「Upgrade to Premium!」, setup-mine-free-end.png).
  Test server still On. No other debug option changed.
- Credits **1303** (Mine, 12:25). Spent net 536 since 1839 (fixtures A 80, B 25, D 30, C 20, F 20; probes 341; two
  failed jobs refunded); part of the difference may be the other device (shared account).
- My AI Artwork › Image to Video now holds, newest first: Kling 4.0 probe (**failed**, 「View Detail」), Wan 2.7,
  Vidu Q4, Happy Horse 1.1, Kling O3, Kling O1, Pixverse V6, Vidu Q3, Vidu Q2, Gemini Omni Flash 1.2, Veo 3.1,
  Seedance 2.5 (probes 「Probe G: the woman blinks」), F (Wan 3.0), C (Kling 3.0, 「Fixture C: the man…」), Seedance 2.0
  (「Check G: the woman smiles」), D (Kling 3.0, dog inspiration), first C (Kling 2.5 Turbo, **failed**, 「View
  Detail」), B (Kling 2.5 Turbo), A (Kling 2.6), template videos Santa Squad / Santa (2026/11/18). TC-004 can use either
  failed tile; none of the 「View Detail」 pages was opened. No processing job (TC-005 starts its own in R1-a).
- App left on Mine (Launcher), relaunched at 12:24 for the tier change.

### 2026-11-19T04:25:18.061Z · next TC-001 (R1-a)
{"Not run":39,"Blocked":11}

R1-setup done 12:25: Reuse/Prompts & Settings present (video A). Fixtures A,B,C,D,F made; failed jobs: first C (Kling 2.5T start/end) and Kling 4.0 probe, both refunded, View Detail unopened; G impossible (no model refuses a real person, 18 tried) -> TC-034 Blocked test-data; TC-032: no 500-limit model, use Vidu Q2/Pixverse (2000) with F (2129 chars). Tier Free (restored), Test server On, credits 1303 (Mine 12:25), app on Mine. Logs pulled R1-setup.

### 2026-11-19T06:09:11.502Z · next TC-011 (R1-b)
{"Pass":12,"Fail":3,"Blocked":11,"Not run":24}

R1-a done 14:09 (paused ~12:50-14:00 for the 5-hour usage limit): 12 Pass, 3 Fail (TC-006 chip 「pro」 lower-case, also 「std」 on C; TC-049 order: Prompts & Settings right under Save, no 「More Video Editing Tools」; TC-010 no 「Settings applied」 toast), TC-041/042 Blocked (policy). New fixture P: Kling 3.0 5s Std, croissant photo, prompt 「Fixture P: steam rises slowly from the coffee cup」, 30 cr (1303 -> 1273), started 12:38, finished by ~14:09 (used for TC-005 while processing). Kling 4.0 probe 「View Detail」 opened (error dialog); first-C failed tile still unopened. Observations O-1 (theme switch drops Save & Share to Launcher), O-2 (Reuse transition draws room rotated), O-3 (‹ in Reuse room -> My AI Artwork, not Save & Share; Q-5: ‹ from Recent-opened page -> Recent). Tier Free, Test server On, credits 1273 (room pill 14:07), phone theme dark (restored), app on My AI Artwork › Recent › Video. Logs pulled R1-a-20261119-140859.

### 2026-11-19T06:27:20.123Z · next TC-023 (R1-c)
{"Pass":22,"Fail":8,"Blocked":14,"Not run":6}

R1-b done 14:27 (14:08-14:27): 10 Pass, 5 Fail (TC-043 system Back and TC-020 ‹ from the Reuse room go to My AI Artwork, not Save & Share; TC-013 and TC-015 no 「Settings applied」 toast (TC-015 also: the intro sheet never shows on Reuse, though it shows from AI Videos and fresh Create More); TC-028 Create More placeholder 「Describe the subject and how they move in the scene, e.g. A dancer spins and jumps under stage lights.」 and 「0/2500」 vs mockup), 5 Blocked (TC-046/TC-016 defect upstream: no sheet / no toast; TC-034 test-data; TC-019/036 policy). No Generate tapped, no credits spent: 1273 (room pill 14:26). Wi-Fi back on (CL-WiFi). Tier Free, Test server On, theme dark. Observations O-4 (‹ from a Create More room reached via history button → Launcher), O-5 (first tap in a reused prompt selects all). Lowercase 「std」 chip also on B and C (TC-006). Room's Create More resets to Kling 3.0 each time. App on My AI Artwork › Image to Video. Logs pulled R1-b-20261119-142649, sliced.

### 2026-11-19T06:57:36.484Z · all recorded
{"Pass":29,"Fail":10,"Blocked":11}

R1-c done 14:50 and R1 wrap-up: 7 Pass, 2 Fail (TC-024 chip pro = TC-006; TC-037 Artwork_Reuse_Click without model), 4 Blocked (TC-029-031 no removed model; TC-035 Free 1113 >= 80). TC-037-040 ran on logcat [PHD-A][Mixpanel] lines (KP-140). Generations: TC-023 Kling 2.6 10s Pro Sound on 80; TC-027 Kling 2.6 5s Off 25; TC-039 25; TC-040 Kling 3.0 30; all four finished by 14:48. Credits 1113 (room pill 14:50). Tier Free, Test server On, theme dark, Wi-Fi on. TC-023 video saved to DCIM/PhotoDirector/Video/2026-11-19-14-48-55-536.mp4 (copy in media/, git-ignored). App on Save & Share of TC-023's video. Logs pulled R1-c-20261119-145015, sliced. eBug drafts + review page in android/ebugs/2026-11-19-r1 (10 entries), nothing filed.
