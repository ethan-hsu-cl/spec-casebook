# TR261111-0042 verify plan — PHD-A 20.19.0.v202611111946 (R3)

Tester WILLY_WU, 13 own bugs (PHA262026P0050 is ALBERT_CHANG's: not in scope). Device SM-S911 (Galaxy S23), app from
Google Play internal testing, versionCode 90201900, installed 2026-11-12 10:28 (RD log: 90201900 is the build uploaded
to Play for this TR; Play Integrity needs a Play install). Raw bug bodies: `bugs-raw.txt`.

## What each bug needs (today's spec)

| Bug | Area | RD says | Check | Cost |
| --- | --- | --- | --- | --- |
| 0178, 0179, 0185, 0196, 0350 | AI Face Swap | feature taken down | every entry to Face Swap gone (Launcher, AI tools list, search, Edit room tool bar) | none |
| 0516 | AI Videos › AI Anime Video | gone in latest build | AI Anime Video has 「See all」 or no longer exists | none |
| 0328 | I2V Inflate / Squish / Dollify | content taken down | the three styles gone, or no settings on them | none |
| P0036 | I2V Start/End inspirations | corner radius removed (Figma 4403-3320) | no triangles at the sample photos' bottom corners; side effects on Custom | none |
| 0230 | I2V cash purchase, slow test card | gone in latest build | Play purchase with the slow test card, kill, re-enter, buy again | **Play test payment: user's step** |
| 0409 | AI Background Custom | Custom moved to My Prompts | no duplicate 「Custom」 tiles after a Custom generation; prompt in My Prompts | 1 generation |
| P0014 | AI Replace reference image | UI is reference image only (spec R-011) | reference image page has no prompt box; Generate works | 1 generation (6 cr) |
| 0343 | AI Agent watercolor | not reproduced after model update | 「Transform into watercolor painting」 returns an image | 1 agent turn |
| 0335 | Launcher shortcuts, Polish | translations wrapped / shortened (CMS) | Polish shortcut labels readable, 2 lines at most, not tiny | language change |

## Order (one journey)

1. Launcher (English): account and tier from ☰; Face Swap absent on Launcher, its AI tools list and search.
2. AI Videos: AI Anime Video (0516).
3. Image to Video: style list (0328), Start/End inspirations (P0036). 0230 stops at the purchase sheet: the payment is
   the user's (agent never completes a Play purchase).
4. Edit room with one photo: tool bar Face Swap absent (0196 entry), AI Background Custom (0409), AI Replace reference
   image (P0014).
5. AI Agent: watercolor (0343).
6. Last: app language Polish → Launcher shortcuts (0335), then restore the language.
