# Image to Video Reuse Android — R1 report (run 2026-11-19-r1)

Table v3 (50 rows), PhotoDirector 20.19.0 (90201901) v202611181947 from TR261118-0070 (MD5 b94f353f…, installed
10:58), Test Server; Google Pixel 8a (42201JEKB02229), dark theme. Plan: `runs/RUN-PLAN-20261119-R1.md`. Nothing filed,
uploaded or commented.

## Tally

| Segment | Area | Pass | Fail | Blocked | Test time |
|---|---|---|---|---|---|
| R1-setup | Fixture videos A, B, C, D, F (G not possible) | – | – | – | – |
| R1-a | My AI Artwork tile and Save & Share | 12 | 3 | 2 (up front) | 1h 29m |
| R1-b | Reuse into the Custom room | 10 | 5 | 5 (2 up front) | 0h 18m |
| R1-c | Generate from Reuse | 7 | 2 | 4 (3 up front) | 0h 23m |
| **Total** | | **29** | **10** | **11** | **2h 11m** |

Fail dispositions: 10 defect. Blocked: 2 defect (TC-046, TC-016: the sheet and the toast never show), 9 test-data
(TC-019, 029–031, 034–036, 041, 042). Inconclusive queue: empty.

## Time, credits, usage

- Wall 3h 48m (11:02 – 14:50 CST), test time 2h 11m, idle 1h 38m (12:40 – 14:01 the 5-hour usage limit stopped R1-a).
- Credits 1839 → 1113 (fixtures ≈ 341 incl. a 120 Seedance 2.5 slip, P 30, R1-c 160; the account is shared and another
  device also spent). Tier Free at the end (Premium only for the fixture probe in R1-setup).
- Plan usage (`runs/usage.jsonl`, 1.25× Team seat, shared account): 58% → 95% over R1-setup; after the 14:00 reset
  8% → 20% (R1-a rest) → 63% (R1-b + R1-c + wrap-up); weekly 10% → 27%.

## Findings (10 eBug drafts: 8 RD, 2 PM)

Drafts: `ebugs/2026-11-19-r1/20261119_eBug_drafts_I2V-Reuse-R1_20.19.0.md`; review page
`ebugs/2026-11-19-r1/20261119_eBug_review_I2V-Reuse-R1_20.19.0.html`. Format check 0 errors; dedupe (Android pool): no
same-OS match.

1. ISS-IR-01 (S3, RD) No 「Settings applied」 toast after Reuse — TC-010, TC-013, TC-015; blocks TC-016.
2. ISS-IR-02 (S4, RD) Reuse skips the Image to Video explanation sheet — TC-015; blocks TC-046.
3. ISS-IR-03 (S3, RD) ‹ and system Back in the reused room go to My AI Artwork, not Save & Share — TC-020, TC-043.
4. ISS-IR-04 (S4, RD) Quality chip lower case 「pro」 / 「std」 — TC-006, TC-024.
5. ISS-IR-05 (S3, RD) 「Prompts & Settings」 right under 「Save」, no 「More Video Editing Tools」 — TC-049.
6. ISS-IR-06 (S4, PM) Create More placeholder and 「0/2500」 counter differ from the mockup — TC-028.
7. ISS-IR-07 (S3, RD) Reuse logs Artwork_Reuse_Click without model, not ImageToVideo_Reuse_Click — TC-037.
8. ISS-IR-08 (S3, RD) Switching the system theme on Save & Share drops to the Launcher — O-1.
9. ISS-IR-09 (S4, RD) Reuse transition draws the room rotated for a moment — O-2.
10. ISS-IR-10 (S4, PM, UX) First tap in a reused prompt selects the whole prompt — O-5.

Not raised: O-3 (same as ISS-IR-03), O-4 (‹ from Create More via room history to Launcher; recorded in
`observations.md`).

## For the next draft

- phases.json marks TC-037–040 Blocked for lack of an event log, but the app writes Mixpanel events to logcat
  (`[PHD-A][Mixpanel]`); R1-c ran them (TC-038–040 Pass). Drop that block reason.
- TC-032: no model has a 500-character limit on this build (lowest 2000: Vidu Q2/Q3, Pixverse V6); ran on Vidu Q2.
- TC-034: no model shows the real-person message on Test Server (all 18 tried); stays test-data.
- The sound row is 「Generate Background Sound」 in the app, 「Generate Sound by AI」 in the table.
- Knowledge added by the inbox subagent: KP-140, KP-141, KF-001 – KF-011 (observed).
