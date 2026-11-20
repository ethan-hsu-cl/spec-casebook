# TR261111-0042 verify — PHD-A 20.19.0.v202611111946 (R3), 2026-11-13

- Device: Samsung Galaxy S23 (SM-S911), Android 16. App from Google Play internal testing, versionCode 90201900,
  installed 2026-11-12 10:28; About shows 20.19.0, SR PHA261029-01 (the TR's SR). The NAS APK of this TR
  (MD5 07114E6E…) is versionCode 90201901 per RD's note; the Play build is what Play Integrity needs.
- Server: Test Server. Account: not signed in (Free, 1916 credits at start; 1898 at the end: AI Background 6,
  AI Replace 6, AI Edit Agent 6).
- Tested by: AI agent (Claude Opus 5.5) driving the phone over Appium.
- Scope: the 13 bugs created by WILLY_WU in the verify list (PHA262026P0050 is ALBERT_CHANG's).

| Bug | Verdict | Evidence |
| --- | --- | --- |
| PHA252025-0178 / 0179 / 0185 / 0196, PHA262026-0350 | OK: AI Face Swap is gone from every entry (Launcher both pages, AI Photos, AI Videos, all Edit room tool categories) | `face-swap-entry-points.txt`, s1-*, s4-editroom |
| PHA252025-0328 | OK: no Inflate / Squish / Dollify in any of the 12 template categories (320 names, `i2v-all-templates.txt`); a template with a photo shows no settings | s3-templates, s3-squished-example |
| PHA262026P0036 | OK: Start/End sample photos (inspiration) have square bottom corners, no triangles | s3-insp-frames, s3-insp-corners-zoom |
| PHA262026-0409 | OK: after a Custom generation no second 「Custom」 tile; the prompt is in My Prompts (dated) | s5-generated, s5-myprompts |
| PHA262026P0014 | OK: the reference image page has no prompt box any more (spec R-011, RD: reference image only); Replace applies the reference (guitar), one 6-credit charge | s6-refpage, s6-result |
| PHA262026-0343 | OK: 「Transform into watercolor painting」 returns a watercolor image with a one-line reply | s7-typed, s7-resp3 |
| PHA262026-0335 | OK: Polish Launcher shortcut labels are full size, long names wrap to two lines | s8-pl-launcher, s8-pl-launcher2 |
| PHA252025-0516 | OK (tester, 2026-11-13: UI change): AI Anime Video still has no 「See all」; the style strip (Vivid … Elf) scrolls sideways with no See all at its end | s2-anime, s2-anime-end2 |
| PHA252025-0230 | OK (tester, 2026-11-13: old issue, spec change): Image to Video generates with credits (Generate 30 on the Custom tab); the slow-test-card purchase was not run | s3-i2v-room |

## Other observations
- AI Edit Agent: after importing a photo the first suggestion still reads 「Import a photo. I'll suggest edits!」
  (already filed as PHA262026P0108 on this TR).
- I2V Start/End: the sample photos sit inside a rounded box that shows a thin grey rounded band above and below
  each photo (s3-insp-frames). Not a triangle; may or may not match the latest guideline (Figma 4403-3320, not read).
- AI Replace: after Replace the result opened in My AI Artwork › AI Replace; one charge (1910 → 1904). (The agent's
  first tap hit the 「Replace Area」 title, not the button.)
- QR filed: QR261113-0020 (2026-11-13 14:50), OK=13, text only; all 13 Close (verified).
- Second QR: QR261113-0023 (phd-a template), PHA262026P0050 OK (verified by WILLY_WU by hand); all 14 verify-list bugs verified.
