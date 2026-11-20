# AI Hair Color Custom Android — round R3 report

Table v4 (87 cases, draft 20261118-120459). Phone Google Pixel 8a (42201JEKB02229), Android 16, 1080 × 2400. Build
PhotoDirector 20.19.0 / versionCode 90201901 (= 20.19.0.v202611181947, the build TR261118-0070 names), Test Server.
Run 2026-11-20 10:06 – 11:30 (Asia/Taipei). Plan: `../RUN-PLAN-20261120-R3.md`.

## Totals
| Result | Cases |
|---|---|
| Pass | 56 |
| Fail | 18 (15 defect, 3 question) |
| Blocked | 13 (6 test-data, 4 observability, 3 defect upstream) |
| Not run | 0 |

| Segment | Pass | Fail | Blocked |
|---|---|---|---|
| R3-a Intro Demo and photo guide | 6 | 1 defect | — |
| R3-b Entry checks | 7 | 3 defect | 3 defect (upstream TC-005) |
| R3-c Custom panel, no credits | 19 | 6 defect, 2 question | — |
| R3-d Generate, wait and result | 12 | 5 defect, 1 question | 2 observability |
| R3-e Every style (Premium via KP-131) | 11 | — | — |
| R3-f Free and low balance | 1 | — | 3 test-data |
| R3-x parked at init | — | — | 2 observability, 3 test-data |

(The plan's Log counted TC-040 under R3-c; results.csv records it in R3-d.)

Time: test 1 h 24 m, wall 1 h 24 m, no idle gap (`run-log.ts time`). Tokens: 535 messages, 87.6 M tokens processed
(1.40 M cache-write, 85.9 M cache-read, 261 k out; `token-usage.ts --since 2026-11-20T01:50Z`, 9 transcripts naming the
run). Credits: 0 at start (KP-136); the orchestrator bought the 2000 pack on the Google Play test card (REQ-011: one
test order phd_2000_credit_freeuser, no charge; the 1000-credit upsell declined); 2000 → 1874 = 21 generations × 6
(9 in R3-d, 12 in R3-e incl. one extra Bangs regeneration from a script mis-step, O-6). R3-f: no credit taken.

## Defects vs questions
- Defects (15 Fail): TC-001 (「Try now」 casing) · TC-005 / TC-012 / TC-015 (no slanted-face warning, P0110) · TC-024 /
  TC-029 (Solid greys the Highlight row) · TC-038 / TC-041 / TC-042 (applied Custom cell keeps its unset look) · TC-039
  (tap outside applies, P0128) · TC-045 / TC-046 / TC-040 (no wait text, P0116; panel collapses, P0149) · TC-047 (panel
  collapses on Generate, P0149) · TC-057 (no 100% notice, P0118).
- Questions (3 Fail): TC-017 (first template Soft Black, not Platinum) · TC-022 (split-dye photo thumbnails) · TC-078
  (template wait 34–36 s, not about 15 s).

## Filed eBugs rechecked on 90201901 (information only; nothing commented on)
ECL status read 2026-11-20 (`ecl_query.py bugs`).

| BugCode | ECL status | Rows | R3 |
|---|---|---|---|
| PHA262026P0110 | Propose Postpone | TC-005, TC-012, TC-015 | Still failing (TC-006 / TC-087 / TC-007 Blocked upstream) |
| PHA262026P0111 | RDResolved | TC-019 | Handle only, no ⌄ (R2 on the S23 had ⌄); Q-17 assumes the Design, Pass |
| PHA262026P0112 | Close | TC-019, TC-021 | Rows drawn disabled before a style, as the Design |
| PHA262026P0113 | Close | TC-031, TC-035 | Fixed |
| PHA262026P0114 | Close | TC-086 | Fixed |
| PHA262026P0115 | Close (2026-11-19) | TC-038, TC-040, TC-041 | Fixed: collapse selects Custom, outer Generate is Custom; the cell's look is Q-2 (draft ISS-HCC-33) |
| PHA262026P0116 | NewCreated (PM) | TC-045, TC-046, TC-040 | Still failing: scan bar only, no text |
| PHA262026P0117 | Close | TC-047, TC-048, TC-049, TC-053 | Fixed |
| PHA262026P0118 | Assigned | TC-057 | Still failing |
| PHA262026P0119 | Close | TC-054 | Fixed |
| PHA262026P0127 | RDResolved | TC-032 | Fixed: the picked colour is added as a ringed circle |
| PHA262026P0128 | NewCreated (PM) | TC-039 | Unchanged (tap outside applies) |
| PHA262026P0149 | NewCreated (PM; TR261118-0070) | TC-045, TC-047 | Unchanged (panel collapses on Generate) |
| PHA262026P0150 | Assigned (TR261118-0070) | — | Not judged: no row checks the wheel key's brightness |

## Differences from R2 (S23, same build 90201901)
- Solid now greys the Highlight Color row instead of hiding it (TC-024 / TC-029 Fail against REQ-009; O-1, KF-007).
- Custom panel: colour rows drawn disabled before a style (R2: hidden); no ⌄ collapse key, collapse by dragging the
  handle (R2 had `custom_collapse_btn`); no 「Both Base Color and Highlight Color are required.」 hint; a palette pick
  adds a ringed circle after the wheel (TC-032 Pass; R2 Fail, P0127).
- Longer waits: Soft Black template 34.4 / 36.0 s (R2 16.2 s; O-3, KP-070); Custom 41.8–69.2 s (R2 44–48 s).
- The Intro Demo showed for the first time (TC-001 run, not Blocked); 「Discard changes?」 still shows before the Edit
  Room on ✕ / Back (Q-22 recorded; TC-079 / TC-088 Pass on the landing, REQ-009).
- Pixel recipes: pick-haircolor.steps and back-to-picker.steps added; Pexels recipes fixed to Pixel pixels.

## Observations
O-1 panel differences (above) · O-2 first eyedropper sample on the hair edge read near-white (1 of 2) · O-3 template
wait · O-4 after ✓ the new Edit Room's Home asks 「Discard changes?」 · O-5 the disabled regeneration button keeps
「Retry」 (waits use the log) · O-6 one extra Bangs generation (script) · O-7 every Custom generation logs the same
Mixpanel style `Style_010_Custom_HairColor_gpt-image-2.5-sunburst` (note for RD: the event does not say which pattern).

## eBug drafts (6, nothing filed)
`../../ebugs/2026-11-20-r3/` — drafts `20261120_eBug_drafts_AI-Hair-Color-Custom-R3_20.19.0.md`, review page
`20261120_eBug_review_AI-Hair-Color-Custom-R3_20.19.0.html`, `dedupe.txt`. Format check 0 errors, 5 warnings; read-only
ECL dedupe over the 16 Android AI_Hair_Color tickets: no same-OS duplicate among the 6.

| # | ID | Owner | Sev | Finding | Rows |
|---|---|---|---|---|---|
| 1 | ISS-HCC-31 | RD, UI | 4 | Intro Demo button 「Try now」, not 「Try Now」 | TC-001 |
| 2 | ISS-HCC-32 | RD | 3 | Solid greys the Highlight row instead of hiding it (ruling REQ-009) | TC-024, TC-029 |
| 3 | ISS-HCC-33 | PM, UX | 3 | Applied Custom cell keeps its unset look — Q-2 decision | TC-038, TC-041, TC-042 |
| 4 | ISS-HCC-34 | RD | 3 | Soft Black template wait about 35 s, not about 15 s | TC-078 |
| 5 | ISS-HCC-35 | PM, UI | 3 | First Solid template Soft Black, not Platinum (re-offers R2 ISS-HCC-27) | TC-017 |
| 6 | ISS-HCC-36 | PM, UI | 3 | Split-dye styles have photo thumbnails (re-offers R2 ISS-HCC-28) | TC-022 |

Not drafted: R2's held ISS-HCC-24 (panel collapses on Generate) is now PHA262026P0149; R2 drafts held with a ruling
(REQ-009) are not re-offered; ISS-HCC-29 / -30 were taken by the tr-verify TR261118-0070 batch (P0149 / P0150).
TRCode to confirm: the default is TR261111-0042 (R2 batch); TR261118-0070 names the tested build.

## Blocked
- Upstream of P0110 (3): TC-006, TC-087, TC-007 — the slanted-face dialog never shows.
- Test-data (6): TC-073, TC-070, TC-071 — balance 1874, not under 6 (no credit reset without the user); TC-081, TC-082
  deeplink format (Q-11); TC-084 CMS list (Q-13).
- Observability (4): TC-036, TC-037 — no request body in logcat; TC-075, TC-076 — no fault switch on PhotoDirector
  Android.

## Coverage
`node scripts/coverage-page.ts phd/ai-hair-color-custom android --draft 20261118-120459 --runs 2026-11-20-r3` →
`../../coverage.html`: controls 31 ran, 17 n/a, 1 blocked, 2 not run; arrows 5/5 ran; board notes 71/119 traced
(37 ran, 34 n/a); board images 8/9. Taps 0: the Android device script wrote no `taps.jsonl`, so there is no
tap-screenshot proof (as R2); coverage is by rows.

## Knowledge
Inbox had 0 open items; one subagent processed the observations: KF-003 and KP-070 corrected (device difference /
Test Server timing added, ruling kept); verified stamps on KF-001, KF-002, KF-004, KF-006, KP-131, KP-135, KP-136; new
KF-007 (panel differs between phones), KF-008 (「Retry」 during regeneration, wait on the log), KF-009 (first
eyedropper sample), KF-010 (one Mixpanel style for every Custom generation). `knowledge.ts --check` OK. Open: why the
panel differs between phones.
