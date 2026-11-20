# AI Hair Color Custom Android — round R2 report

Table v3 (87 cases, draft 20261117-151025). Phone Samsung S23 SM-S9110 (RFCW2198L7B), Android 16. Build PhotoDirector
20.19.0 / versionCode 90201901 (installed 2026-11-17; reinstalled by the user 2026-11-18 09:43 with the same
versionCode before R2-d), Test Server. Run 2026-11-17 16:50 – 2026-11-18 10:34 (Asia/Taipei).

## Totals
| Result | Cases |
|---|---|
| Pass | 44 |
| Fail | 26 (22 defect, 4 question) |
| Blocked | 17 (10 test-data, 4 observability, 3 defect) |
| Not run | 0 |

Segments: R2-a Intro Demo and photo guide (1 Pass, 1 Fail, 5 Blocked) · R2-b Entry checks (6 Pass, 4 Fail, 3 Blocked)
· R2-c Custom panel (14 Pass, 13 Fail) · R2-f Free and low balance (1 Pass, 1 Fail, 2 Blocked) · R2-d Generate, wait
and result (11 Pass, 7 Fail, 2 Blocked) · R2-e Every style (11 Pass) · R2-x parked (5 Blocked).

Time: test 1 h 26 m (wall 17 h 44 m; idle 15 h 23 m overnight waiting for credits, 56 m for the reinstall).
Tokens: 751 messages, 137.3 M tokens processed. Credits: 0 at start (the 2026-11-17 install dropped R1's 1916);
the user bought credits after reinstalling (166); 166 → 52 after R2-d and R2-e (19 generations × 6 = 114; one extra
Face framing generation by a helper mis-tap, O-17). R2-f received the VIP daily bonus of 3 credits (O-12).

## Filed eBugs rechecked on 90201901 (information only; nothing commented on)
| BugCode | Row | Now |
|---|---|---|
| PHA262026P0110 | TC-005, TC-012, TC-015 | Still failing: no slanted-face warning |
| PHA262026P0111 | TC-019 | Fixed: ✕ ↺ ↻ ✓ row gone, grab handle and ⌄ |
| PHA262026P0112 | TC-021 | Symptom gone; the colour rows are now hidden before a style instead of disabled (Design) |
| PHA262026P0113 | TC-031, TC-035 | Fixed: eyedropper present and working |
| PHA262026P0114 | TC-086 | Fixed: system Back closes only the palette |
| PHA262026P0115 | TC-038, TC-040 | Partly: collapse now selects Custom and generates Custom; the Custom cell still never shows the colours |
| PHA262026P0116 | TC-045, TC-046, TC-040 | Still failing: no 「Applying your new hair color...」 (wait 44–48 s) |
| PHA262026P0117 | TC-047, TC-048 | Fixed: Intensity bar at 100 and 「Retry」 6 |
| PHA262026P0118 | TC-057 | Still failing: no one-time 「100% only」 dialog |
| PHA262026P0119 | TC-054 | Fixed: switching back to Custom recalls its result |

## New findings → eBug drafts (13, nothing filed)
Drafts and review page: `../../ebugs/2026-11-18-r2/` (ISS-HCC-16 … 28; format check 0 errors; read-only ECL dedupe:
no same-OS duplicate).
- ISS-HCC-16 Photo guide and picker labels differ from the Design (TC-092)
- ISS-HCC-17 No-face dialog 「A face is required」 (TC-009; R1's held ISS-HCC-02)
- ISS-HCC-18 Edit Room's Quick Action row has no 「Hair Color」 (TC-015)
- ISS-HCC-19 PM decision: Solid hides the Highlight row (PM) vs greys it (Design) (TC-024, TC-029; Q-18)
- ISS-HCC-20 PM decision: Base only keeps Generate disabled against REQ-003 / REQ-007 (TC-026; R1 enabled it)
- ISS-HCC-21 Highlight-only Generate shows no toast 「Select both a base and highlight color.」 (TC-027)
- ISS-HCC-22 A palette colour is not added as a new circle (TC-032; R1 added it)
- ISS-HCC-23 PM decision: tapping the photo closes and applies the panel against REQ-004 (TC-039; R1 kept it open)
- ISS-HCC-24 Generate in the panel collapses the panel (TC-047)
- ISS-HCC-25 ✕ and system Back on a result ask 「Discard changes?」 and land in the Edit Room (TC-079, TC-088)
- ISS-HCC-26 Subscriber without credits sees 「Get Credit Refilled!」 / 「GET CREDITS」 (TC-071)
- ISS-HCC-27 PM decision: first Solid template is 「Soft Black」, not 「Platinum」 (TC-017)
- ISS-HCC-28 PM decision: split-dye styles have photo thumbnails (TC-022)

ISS-HCC-20 and ISS-HCC-23 exist because 90201901 now follows the PM page / Design where the user's rulings REQ-003 /
REQ-007 and REQ-004 say otherwise: the user decides whether they are filed or the rulings change.

## Blocked
- Intro Demo (TC-001, 090, 003, 002, 004): never shown on this install (test-data).
- Slanted-face dialog rows (TC-006, TC-087, TC-007): no dialog to act on (defect, upstream TC-005).
- TC-070, TC-073: Generate offered the one-time 「1 Free Trial」, kept for generations (test-data).
- TC-036, TC-037: logcat carries no request body (observability).
- TC-075, TC-076 (no fault switch), TC-081, TC-082 (deeplink format, Q-11), TC-084 (CMS list, Q-13).

## Open points
- Build vs TR: TR261111-0042 names versionCode 90201900; this round tested 90201901. Confirm the TR before filing.
- The Launcher has no 「AI Magic」 section or 「Hair Color」 card (entry is AI Photos › 「AI Hair Color」, O-2).
- Credits Details shows Reel Creator charges this run did not make (shared account, O-13).
- Coverage: the Android client writes no taps.jsonl, so no tap is proven on the coverage page.
- Observations O-1 … O-17: `observations.md`.

## Review and filing (user, 2026-11-18)
- Filed on TR261111-0042 (the user confirmed it for 90201901): ISS-HCC-22 → PHA262026P0127 (Sev 3, RD, two images,
  read back). `../../ebugs/2026-11-18-r2/filed_bugcodes.md`.
- ISS-HCC-23 → PHA262026P0128 (Sev 3, PM, `[AIAgent][UX]`, filed after the user's UX check; two images, read back).
- Held with rulings (requests.md REQ-009, knowledge KF-001 … KF-006, KP-135): 16 (app-wide 「Recommendation」 guide),
  17 (no-face wording accepted), 18 (no Quick Action entry), 19 (Solid hides the Highlight row), 20 (both colours
  required; supersedes REQ-003 / REQ-007), 21 (no toast needed), 25 (landing in the Edit Room is correct). Table
  draft 20261118-120459 (v4) moves TC-009, 015, 024, 026, 027, 029, 079, 088 and 092 to these rulings; under them
  R2's results for those rows match the build (TC-079 / TC-088 apart from the 「Discard changes?」 dialog, Q-22).
- Held without reason: 24, 26, 27, 28.
