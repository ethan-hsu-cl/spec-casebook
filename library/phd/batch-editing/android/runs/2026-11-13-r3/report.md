# Batch Editing Android — Phase R3 report (table v7, full run on the TR261111-0042 build) — final

Plan `runs/RUN-PLAN-20261113-R3.md` · approved table v7 (170 rows, `drafts/20261112-150000/phases.json` R3) · run folder `runs/2026-11-13-r3/` · 2026-11-13. Nothing filed, uploaded, commented or committed.

## Environment
- PhotoDirector for Android 20.19.0.v202611111946 (versionCode 90201900), SR PHA261029-01, TR261111-0042 — About read in R3-a (20.19.0, PHA261029-01) and again in R3-g · Google Play internal testing build · Test Server
- Samsung Galaxy S23 (SM-S9110, RFCW2198L7B), Android 16, 1080 × 2340, USB, Stay awake · Appium / UiAutomator2 port 4724 (a second server on 4726 was running throughout; left alone)
- Tier: Premium through About › debug 「Set to subscriber」 (KP-131), checked at every segment start (Mine 「Hello VIP!」, 1886 credits all run); R3-g switched to Free (「Upgrade to Premium!」) and back to Premium at its end. No other debug option changed; the dialog view shows no UUID / token.
- Photos: Sample Photos and 00PHDa_Testing_Material albums (recipes `pick12-sample.steps`, `pick12-testing.steps`), Section 3 stand-ins ① – ④ in album 「Casebook」 (`pick4-casebook.steps`)

## Results — 170: 144 Pass · 16 Fail · 10 Blocked · 0 Not run (Fail = 7 defect, 9 question)
| Segment | Area | Cases | Pass | Fail | Blocked |
|---|---|---|---|---|---|
| R3-a | Photo Picker and entry | 26 | 24 | 1 (defect) | 1 (observability) |
| R3-b | Batch Edit Room main, Crop & Rotate | 35 | 33 | 2 (1 defect, 1 question) | 0 |
| R3-c | Crop rules, Section 3 | 16 | 12 | 4 (1 defect, 3 question) | 0 |
| R3-d | Adjustment room | 23 | 21 | 2 (1 defect, 1 question) | 0 |
| R3-e | AI Enhance | 36 | 24 | 4 (2 defect, 2 question) | 8 (observability) |
| R3-f | Leaving, Save, Batch Save page | 29 | 26 | 2 (1 defect, 1 question) | 1 (test-data) |
| R3-g | Free user | 5 | 4 | 1 (question) | 0 |
| Total | | 170 | 144 | 16 | 10 |

### Every Fail, its disposition and reason
| Case | Disposition | Reason | Where |
|---|---|---|---|
| TC-012 | defect | 21st photo toast 「You can only select 20 photos.」, not 「Please pick at most 20 photos.」 | repeats PHA262026P0061 (Assigned): dedupe.txt |
| TC-162 | defect | Crop 「All」 stays enabled on photo 2, which has no change of its own (R-234 per photo) | ISS-BEA-12 (RD) |
| TC-164 | defect | Adjustment: the same on photo 2 | ISS-BEA-12 (RD) |
| TC-062 | question | One Undo after 3:2 + 「All」 reverts the 11 others; photo 1 keeps its own 3:2 | ISS-BEA-14 (PM, UX) |
| TC-076 | question | Adjustment: the same (photo 1 keeps Exposure 「0.6」) | ISS-BEA-14 (PM, UX) |
| TC-049 | question | ④ (2730 × 1535) is held as 「2560 x 1439」: 3:4 box 「1075 x 1435」 vs Section 3's 1151 × 1535 | ISS-BEA-15 (PM, UX) |
| TC-057 | question | 3000 × 3000 refused with 「Width should be between 147 and 2560. Please try again.」: range and width-only copy (Q-6) | ISS-BEA-15 and ISS-BEA-16 (PM, UI) |
| TC-058 | question | 237 × 237 accepted (minimum 147, Section 3 says 238) | ISS-BEA-15 |
| TC-060 | defect | Square + 「All」 saves ④ as 1434 × 1435 | repeats PHA262026P0060 (RDResolved, still fails): dedupe.txt |
| TC-100 | question | ✕ after a finished batch AI Enhance opens 「Discard changes?」 (Q-19) | ISS-BEA-17 (PM, UX) |
| TC-142 | question | System Back does the same; a 2nd Back leaves the dialog open (as P0059) | ISS-BEA-17 |
| TC-144 | defect | System Back leaves 「Enhance 12 photos?」 open | repeats PHA262026P0058 (RDResolved, still fails): dedupe.txt |
| TC-110 | defect | Home 30 s during AI Enhance → 「3 completed, 9 failed」 (UnknownHostException in the background) | repeats PHA262026P0057 (RDResolved, still fails): dedupe.txt |
| TC-145 | defect | System Back leaves 「Discard changes?」 (from Home) open | repeats PHA262026P0059 (RDResolved, still fails): dedupe.txt |
| TC-128 | question | Batch Save title 「Saved 12 photos」 vs Design 「Save 12 photos」 (Q-20) | ISS-BEA-18 (PM, UI) |
| TC-135 | question | Free: interstitial on the 1st batch save, IAP flyer on the 2nd, but no native ad card on the Batch Save page (single Save & Share has one) | ISS-BEA-19 (PM, UX) |

Blocked: TC-096, TC-101 … TC-105, TC-109, TC-160 (observability: no fault switch on this build; rechecked in R3-e); TC-152 (observability: no `phd://` VIEW intent filter, the deeplink cannot be fired by adb, Q-15); TC-136 (test-data: the rating-dialog trigger count needs RD).

Rows recorded Pass per earlier user rulings: TC-107 (toast 「No Internet connection」, ISS-BEA-11), TC-115 (「Keep」, ISS-BEA-08), TC-122 (dimmed feedback button while saving, ISS-BEA-07).

### What this build fixed against R1 / R2 (20.19.0 build 1106 → v202611111946)
- Crop & Rotate has ‹ at the top left (TC-037, TC-155 Pass; R1 ISS-BEA-02 gone).
- 「All」 greyed on entering both rooms, after the apply (a tap then gives no toast and changes nothing), after Redo and after a size-only change (TC-153, TC-042, TC-063, TC-163, TC-075, TC-165 Pass): R2's ISS-BEA-12 is fixed except the per-photo case (TC-162, TC-164).
- The thumbnail strip is hidden while Curve or HSL is open (TC-166, TC-168 Pass): R2's ISS-BEA-13 is fixed.
- R2's empty Undo step from a no-change 「All」 is gone (「All」 is disabled then).
- Not fixed although their tickets are RDResolved: PHA262026P0057 (TC-110), P0058 (TC-144), P0059 (TC-145, and TC-142's 2nd Back), P0060 (TC-060). P0061 (TC-012) is still Assigned.

Logs: R3-a … R3-g pulled and sliced (`logs/R3-<x>-*`); no app crash in any segment; Fail windows hold only CacheDao and ad MediaCodec noise, except TC-110's UnknownHostException (P0057). R3-c paused ~2.5 h for a usage-limit reset (the one idle gap).

## eBug drafts — `ebugs/2026-11-13-r3/` (7 entries, none filed)
| F | ISS | Cases | Finding | Proposed |
|---|---|---|---|---|
| 1 | ISS-BEA-12 | TC-162, TC-164 | 「All」 stays enabled on a photo with no change of its own after switching photos | Functional S3 RD |
| 2 | ISS-BEA-14 | TC-062, TC-076 | One Undo after an edit + 「All」 keeps the current photo's own edit | [UX] S3 PM |
| 3 | ISS-BEA-15 | TC-049, TC-057, TC-058 | Crop sizes come from a 2560 px copy with a 147 px minimum, not Section 3's original-size range | [UX] S3 PM |
| 4 | ISS-BEA-16 | TC-057 | Out-of-range toast names only the width; PhD copy undecided (Q-6) | [UI] S3 PM |
| 5 | ISS-BEA-17 | TC-100, TC-142 | ✕ / Back after a finished batch AI Enhance asks 「Discard changes?」 (Q-19) | [UX] S3 PM |
| 6 | ISS-BEA-18 | TC-128 | Batch Save title 「Saved 12 photos」 vs Design 「Save 12 photos」 (Q-20) | [UI] S3 PM |
| 7 | ISS-BEA-19 | TC-135 | Free: no native ad card on the Batch Save page (O-19) | [UX] S3 PM |

R2's ISS-BEA-12 and 14 were never filed and are carried forward (12 narrowed to what still fails); ISS-BEA-13 is fixed. R1's held PM questions are filed to PM now (open questions → PM, user 2026-11-11); no user ruling or ticket answers Q-6, Q-19, Q-20 or O-19. Q-19 and Q-20 could not be settled by the Design-first order (user, 2026-11-13) because the Design frames carry no date (Q-12). Format check (`check_ebug_format.py --product PHD-A --allow-agent-ux`): 0 errors, 0 warnings. `verify_ebug_drafts.py` hangs on Windows (walks up to '/'): not used, as in R1 / R2. Dedupe (read-only, PhotoDirector Mobile for Android): 5 Fail rows repeat P0057 – P0061 and are only in `dedupe.txt`; the one flagged candidate (ISS-BEA-17 vs P0059) is a different finding. Review page `ebugs/2026-11-13-r3/20261113_eBug_review_Batch-Edit-R3_20.19.0.html` (local), Creator / tag / method prefilled from 2026-11-10-r1 and TRCode TR261111-0042, each to confirm.

## Observations
- O-1: Help (i) hidden on the Adjustment Details tab; not raised.
- O-2: no credit pill on the batch AI Enhance page (the Design's pill is on the Discard frame, Q-19); not raised.
- O-3: one upload SocketTimeout on working Wi-Fi, retry finished it (as R1 O-13); not raised.
- O-4: picker tray tile #10 showed another picture once; display-only; not raised.

## Coverage
No coverage page for this run: `coverage-page.ts` reports the Android table is still PDF-only (`specs/2026-11-09/extracted/figma-pending.json`, no control trace), and `device-android.ts` wrote no `taps.jsonl`.

## Knowledge
The product inbox had 4 open items (I-004 … I-007, Swipe Collage, user 2026-11-12); a fresh subagent filed them as `library/phd/swipe-collage/knowledge/` KF-001 … KF-005 and closed them. From this run: KP-131, Batch Editing KF-001 … KF-004 stamped verified on 20.19.0 (2026-11-13; KF-003 gained 540 = 「0.6」 and 「setval on Light sliders makes no Undo step: use thumb drags」); KP-105 corrected: on Android 20.19.0 the debug dialog shows only six switches, no UUID / token rows. Left open: where Android's UUID / token reset is, and Swipe Collage KF-005. Both `--check` runs pass.

## Time and usage
run-log time: wall 4 h 37 m (07:59 → 12:36 UTC), test 2 h 05 m, idle 2 h 32 m in one gap (R3-c usage-limit pause). Per segment: R3-a 18 m, R3-b 20 m, R3-c 14 m, R3-d 18 m, R3-e 26 m, R3-f 18 m, R3-g 10 m.
Claude tokens (`tokens.jsonl` at 20:44, 850 messages, the segment subagents in full and the orchestrator inside the run's spans; the wrap-up after that point not yet counted): 152.5 M, weighted 18.4 M — R3-a 2.0 M, R3-b 4.1 M, R3-c 2.4 M, R3-d 2.9 M, R3-e 3.1 M, R3-f 2.4 M, R3-g 1.4 M weighted.
Plan usage: est. from token rate ≈ 149 % of a 1× Pro 5-hour window (≈ 24 % of the 6.25× Team seat), weekly ≈ 25 % of 1× Pro (≈ 4 % of the seat). No usage-card snapshot was logged for R3 (`runs/usage.jsonl` ends at R2), so there is no account-total figure.
