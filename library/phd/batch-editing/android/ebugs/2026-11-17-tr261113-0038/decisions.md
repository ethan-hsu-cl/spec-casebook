# Decisions — Batch Edit R3 (user, 2026-11-17)

Pasted from the review page: Account WILLY_WU · Source tag AIAgent · TRCode TR261111-0042 · Method API.

| ISS | Sev | Belong | Action | Short Description | Note |
|---|---|---|---|---|---|
| ISS-BEA-12 | 3 | RD | File | | |
| ISS-BEA-14 | 3 | PM | File | | |
| ISS-BEA-15 | 3 | PM | File | | |
| ISS-BEA-16 | 3 | PM | File | | |
| ISS-BEA-17 | | | Hold — not a bug (user) | | 「有更新就應該要跳這個dialog」: with changes, ✕ / Back after AI Enhance should ask 「Discard changes?」 (ruling on Q-19, user 2026-11-17) |
| ISS-BEA-18 | | | Hold (user) | | held by the user, no reason given |
| ISS-BEA-19 | 3 | PM | File | | |

## Re-verification on the new build (2026-11-17)

User 2026-11-17: 「有新版本了 請先在新版本上面驗證過 還是有問題就直接發去新版本上」. The five filed-approved findings were re-run
on PhotoDirector 20.19.0.v202611132003 (90201901, SR PHA261029-01) on the S23 (run
`runs/2026-11-17-verify-tr261113-0038/verify.md`); TRCode for this batch is **TR261113-0038** (its header names
v202611132003). Account WILLY_WU · Source tag AIAgent · Method API, as above.

| ISS | Verdict on v202611132003 | Sev | Belong | Action |
|---|---|---|---|---|
| ISS-BEA-12 | CONFIRMED (TC-162, TC-164) | 3 | RD | File on TR261113-0038 |
| ISS-BEA-14 | CONFIRMED (TC-062, TC-076) | 3 | PM | File on TR261113-0038 |
| ISS-BEA-15 | CONFIRMED in part (minimum: 237 accepted, range 50–800 on an 800 px photo); the 2560 px copy of the 2730 × 1535 photo not re-checked — Crop & Rotate crashes on it (ISS-BEA-20) | 3 | PM | File on TR261113-0038 (reviewer: confirm the Short Description still fits) |
| ISS-BEA-16 | CONFIRMED (toast 「Width should be between 50 and 800. Please try again.」, on the 800 px photo) | 3 | PM | File on TR261113-0038 |
| ISS-BEA-19 | CONFIRMED (Free, TC-135) | 3 | PM | File on TR261113-0038 |
| ISS-BEA-20 | NEW: Batch Crop & Rotate crash on 1706 × 2559 / 2730 × 1535 photos, 4/4 | **1** (user: 「這個crash要發S1」) | RD | File on TR261113-0038 (user approved once reproduced) |

ISS-BEA-17 and ISS-BEA-18 stay held (not re-run).

- 2026-11-17: ISS-BEA-15's Short Description narrowed to what this build showed (「Crop custom size accepts 237 x 237, below Section 3's 238 px minimum」): the 2560 px copy could not be checked (the 2730 × 1535 photo crashes Crop & Rotate, ISS-BEA-20) and the minimum on the 800 px photo is 50, not 147.
