# Update plan — draft 20261120-165128 (updates v1)

Same spec set (2026-11-20). The changes come from the question answers saved on the Cases page (REQ-002).

## Summary
- Rows: 152 (149 modified, 2 new, 1 removed, 0 unchanged). Nearly every row changed only its campaign precondition (Q-1).
- Requirements changed: R-001, R-002, R-005, R-006, R-007, R-012, R-018, R-020, R-022, R-025, R-028, R-029, R-035, R-036, R-038, R-044, R-048, R-049, R-058; new R-077.
- Open questions left: Q-7 (where the Launcher banner leads), Q-13 (the free user's 500-credit sale price), new Q-18 (what the New Year countdown counts to and when it starts).

## Changes by answer
- Q-1: every 「phone date … automatic date off」 precondition is now the RD test date on the stage server; the boundary rows (TC-002 – TC-004) set the date before and after midnight instead of waiting for the clock.
- Q-2: years 2026-12-11 – 2026-12-27 and 2026-12-28 – 2027-01-05 (R-001, R-002).
- Q-3 / Q-6: the interstitial, terms and IAP % rows expect the US store's SKU table prices ($45.99/year, $6.99/month) and 「Save 45%」 computed by the PM formula; language rows expect the % and monthly price from the store (the sheet's fixed 57% / $6.79 replaced by <xx> / <monthly price>).
- Q-4: TC-010 adds a same-day launch with no interstitial.
- Q-5: TC-016 / TC-023 cite the ruling; new TC-151 checks a Pro user gets no interstitial (R-077), placed after the Christmas Back row.
- Q-8: the pill reads 「Try Pro 7 days for free」 (TC-087, TC-089, TC-090, TC-095).
- Q-9 / Q-11 (corrected in chat, REQ-003): only the Christmas campaign drops the countdowns; New Year keeps them. TC-089 checks the New Year countdown on the Launcher and Mine pill, under the IAP CTA and above the credit page CTAs (value to 2027-01-05 23:59:59, Q-18); new TC-152 checks it at the window start; the IAP and credit look rows expect a countdown in New Year (TC-102, TC-121) and none at Christmas (TC-100, TC-120); TC-090 and TC-129 keep no countdown at Christmas; TC-128 (no Christmas countdown before 12/21) is removed.
- Q-10, Q-12, Q-14, Q-15, Q-16: assumptions confirmed; notes and requirement texts cite the rulings.
- Q-17: the India / Indonesia / Philippines rows set the country with Play Billing Lab instead of being Blocked.

## Not added
- Nothing left out by the value check.
