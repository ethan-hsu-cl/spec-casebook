# Creative Reel (Reel Creator) Android — R1 report

Round R1 of table v4 (150 rows, draft 20261117-150251) on PhotoDirector for Android 20.19.0 (90201901), TR261113-0038
(20.19.0.v202611132003, R4). Test Server, Free, signed out. TC-001 – TC-007 on the Google Pixel 8a / Android 16
(2026-11-18 08:48–08:55); from TC-008 on the Samsung Galaxy S23 (SM-S9110) / Android 16 (O-2). Plan:
../RUN-PLAN-20261117-R1.md. Written at the phase wrap-up 2026-11-18; R1-h (TC-072, TC-073) added 2026-11-19: all 150 rows recorded.

## Tally (150 of 150 recorded)
| Result | Rows | Disposition |
|---|---|---|
| Pass | 92 | |
| Fail | 42 | 39 defect, 3 question (TC-003, TC-113, TC-139) |
| Blocked | 16 | 8 test-data (deeplink URLs, Q-15: TC-014 – TC-020, TC-114); 8 defect upstream of TC-075 (no Text Language bar): TC-077, 078, 140, 109, 079, 080, 081, 082 |

| Segment | Rows | Pass | Fail | Blocked | Test time |
|---|---|---|---|---|---|
| R1-a Room, entries, intro, swipe guide, deeplinks | 27 | 12 | 7 | 8 | 0h 26m |
| R1-b Preview, tips, Edit Room jump | 22 | 17 | 5 | 0 | 0h 13m |
| R1-c Picker (TC-050 later, Pass) | 22 | 18 | 4 | 0 | 0h 24m |
| R1-d Picker memory | 16 | 11 | 5 | 0 | 0h 25m |
| R1-e Confirm page, Text Language, languages | 21 | 9 | 6 | 6 | 0h 21m |
| R1-f Creative generations | 19 | 10 | 7 | 2 | 1h 11m |
| R1-g Cinematic, AI Transition, Artwork, system settings | 21 | 12 | 9 | 0 | 0h 52m |
| R1-h Out of credits (2026-11-19) | 2 | 2 | 0 | 0 | — |

Time: wall 24h 33m (2026-11-17 18:42 → 2026-11-18 19:14), test time 4h 05m, idle 20h 28m in three gaps. Tokens in
tokens.jsonl (232 messages, lower bound): input 526, cache write 389,732, cache read 33,458,312, output 90,409. No
usage-card snapshots logged for R1. Credits: S23 52 → 1052 (user-approved 1000-credit Play test purchase, O-10) → 842
after R1-f (3 × 70, one never refunded) → 650 after R1-g (4 × 48). System settings (user-approved): theme dark → light →
dark, Don't keep activities on → off; both restored.

## R1-h: TC-072 / TC-073 (2026-11-19)
pm clear 15:46 (2026-11-18) kept the Test Server UUID with 650 (O-3, KP-136). While paused, the S23 was used by someone
else (O-13, 2026-11-18 15:54 → 19:11 and later): debug dialog changed, new credit UUIDs, purchases and AI Transition / AI
Background jobs, and three PhotoDirector crashes at 17:28:38, 17:31:49, 17:37:07 (IllegalStateException … RecyclerView
is computing a layout, logs/R1-h-blocked-20261118-191445/). These came from that use, not a casebook row: not drafted.
(PHA262026P0130 「crashes after tapping [Import]」 was filed on this TR at 17:50 — the crashes may be its reproduction;
not checked.) On 2026-11-19 the user spent the credits, reset them to 0 and set the app back to Free (UUID b3a561f0).
- TC-072 Pass: Free, 0 credits, single-color-fastcut 7 photos, 「Generate | 70」 → PhotoDirector Premium paywall; closed
  → confirm page, still 0, nothing generated.
- TC-073 Pass: 「Set to subscriber」 ON, 0 credits → 「More Credits Required!」; 「GET CREDITS」 → Credit Shop (daily
  「3 Free Credits」 issued there); nothing bought. Flag back OFF (Mine 「Upgrade to Premium!」), end balance 3.
- Noticed 2026-11-19: the room now shows real section names (「Cinematic Styles 📽️」, 「Year-End Recap ✏️」, 「Cool
  Transitions 🎞️」) — finding 3 (raw string keys, TC-006) should be re-checked before filing; still no 「Top 5 of My
  Year」. Logs R1-h-20261119-095154, no new crash.

## eBug drafts (nothing filed, uploaded or commented)
../../ebugs/2026-11-18-r1/20261118_eBug_drafts_Reel-Creator-R1_20.19.0.md; review page
../../ebugs/2026-11-18-r1/20261118_eBug_review_Reel-Creator-R1_20.19.0.html. 29 entries: 23 RD, 6 PM; S2 ×6, S3 ×19,
S4 ×4. Format check 0 errors / 9 warnings; verify_ebug_drafts.py hangs on Windows (not run); dedupe: no same-OS
duplicate (dedupe.txt).

| # | Finding | Owner | Sev | Rows |
|---|---|---|---|---|
| 1 | Shortcut and AI Videos card still 「Cinematic Reel Creator」 | RD | S3 | TC-002, 004 |
| 2 | Room has no 「Reel Creator」 title | RD | S3 | 005 |
| 3 | Section titles are raw string keys | RD | S2 | 006 |
| 4 | Cinematic Styles cards have no inset photo | RD | S4 | 007 |
| 5 | No Launcher template row (PM to confirm) | PM | S3 | 003, 113 |
| 6 | No Year-End Recap; Creative test templates raw names, one shared demo | PM | S3 | 023, 026 |
| 7 | Photo tips entry: Design ⓘ vs 「View photo tips」; Creative Previews have none | PM | S3 | 033, 024 |
| 8 | Preview photo count has no image icon | RD | S4 | 030, 024 |
| 9 | Picker has no 「Add photos」 title; tray wording differs | RD | S3 | 037 |
| 10 | Tray thumbnails have no 「×」 | RD | S3 | 038, 136 |
| 11 | No red tray text when out of range | RD | S3 | 057, 058, 038 |
| 12 | Imported photos unticked; tapping one adds a duplicate | RD | S2 | 058, 059 |
| 13 | Import prompt has no 「+4」 | RD | S4 | 054 |
| 14 | [UX] one-photo Import prompt, Design vs PM | PM | S3 | 139 |
| 15 | Confirm page: no 9:16, no reorder hint, 「+」 last | RD | S3 | 063, 094, 100, 148 |
| 16 | No Text Language bar | RD | S2 | 075, 076, 148 + 8 Blocked |
| 17 | Count below the minimum not red | RD | S3 | 066 |
| 18 | Prices 70 / 90 / 48 vs drawn 60 | PM | S3 | 063, 074, 118, 148 |
| 19 | Micro Cinema charges 48, spec 40 | RD | S2 | 094, 096, 119 |
| 20 | Credit Detail names every use 「Reel Creator」 | PM | S3 | 119, 120 |
| 21 | Strings stay English in zh-Hant, ja, de, pt | RD | S3 | 123, 076, 125 |
| 22 | German Import button cut to 「Importie…」 | RD | S4 | 125 |
| 23 | Creative card 「Almost Done」 at once, no time estimate | RD | S3 | 085, 141 |
| 24 | Notification opens a stale Processing card | RD | S3 | 121 |
| 25 | Upload cut: 70 charged, 「Credits refunded」 shown, no refund; Retry does nothing | RD | S2 (S1 candidate) | 143 |
| 26 | My AI Artwork tab order | RD | S3 | 089 |
| 27 | Micro Cinema reel is 3:4, not 9:16 | RD | S2 | 127, 122 |
| 28 | Create More job: download timeout, ⚠ Retry, no notification | RD | S3 | 122 |
| 29 | Don't keep activities loses the confirm page | RD | S3 | 116 |

Merges: prices TC-063/074/118/148 → one PM entry (only Top 5 of My Year's 60 is drawn, Q-9; Micro Cinema's drawn 40 →
RD entry 19); credit-detail naming TC-119/120 → one PM entry (Q-2); no Text Language bar → one entry for TC-075/076/148
and the 8 Blocked rows.
Not raised: O-5 (once), O-9 (2.5-min first Next, once), O-10 (Credit Shop stale balance: not this feature — worth a
separate look), O-6 (CELEBRITY flags not judgeable), O-13 (not this run's actions).

## Coverage
coverage-page.ts … --draft 20261117-150251 --runs 2026-11-17-r1 → ../../coverage.html (local): controls 28 run, 29 not
run, 6 n/a; arrows 3 n/a, 3 none; images 10/11. Taps 0: no taps.jsonl in the run folder, so counts come from results only.

## Knowledge (fresh subagent)
KP-133 superseded by KP-136 (Test Server credit UUID from ANDROID_ID survives pm clear); KP-137 (Test server on again
after pm clear; supersedes swipe-collage KF-002); KP-138, KP-139 (S23 quirks); new creative-reel/knowledge KF-001 –
KF-004; verified: KP-131, 135, 017, 019, 020, 026, 032. Left: KP-029, 083, 073, 097 (defects seen, not facts). --check OK.

## Blocked reasons
All readable; TC-081 / TC-082 added to blocked-reasons.json as upstream.

## Needs the user
1. Finding 3 (raw section keys): titles looked right on 2026-11-19 — re-check TC-006 or drop it before filing.
2. Review page decisions (TR261113-0038, WILLY_WU, [AIAgent], API prefilled from the batch-editing batch).
3. Deeplink URLs (Q-15); whether Test Server gets 「Top 5 of My Year」.
