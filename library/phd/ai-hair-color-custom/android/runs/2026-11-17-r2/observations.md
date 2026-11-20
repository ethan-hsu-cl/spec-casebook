# Observations — R2

- **O-1** (closest: TC-001; Q-8, R-002) No Intro Demo on this install either: PhotoDirector 90201901 was installed
  fresh today (firstInstallTime 2026-11-17 09:46:39), and the first AI Hair Color entry of this run went straight to
  the photo guide, which had never been dismissed. Other PhotoDirector sessions ran on the phone after the install, so
  it is not proved the feature was never opened; if nobody opened it, the build has no Intro Demo (Q-8: the 10/E page
  says no demo on first entry). Worth asking PM / RD whether the demo exists on Android. Screenshot:
  `screenshots/TC-001_entry.png`.
- **O-2** (closest: TC-001; R-090) The Launcher has no 「AI Magic」 section and no 「Hair Color」 card: Home shows a
  「New Hair Colors 💈」 row (View all) and the AI Photos tab an 「AI Hair Color」 card, which this run uses as the
  entry. Screenshots: `screenshots/r2a_start.png`, `screenshots/r2a_aiphotos.png`.
- **O-3** (closest: R2-d, R2-e; KP-133) Mine › My Credits reads **0** on this install (R1 ended at 1916 on the
  90201900 install): the reinstall dropped the not-signed-in credits as KP-133 says. Mine shows 「Upgrade to
  Premium!」 (Free). Every generation row (R2-d, R2-e, about 130 credits) needs credits first. Screenshot:
  `screenshots/r2a_mine.png`.
- **O-4** (closest: TC-001, TC-092) The guide's content is fetched from the server: each entry logs
  `actionUrl:/navigate/page?name=ai_hair_color` then `http response: 304 NOT MODIFIED, type = RECOMMEND_AVOID`, already
  304 on this run's first entry (16:51:35), so a copy was cached before the run (this or another feature's guide; it
  weakens O-1's 「never opened」). The guide's wording (「Recommendation」, 「Face Too Small」, 「Accessories」, TC-092)
  may therefore be CMS data rather than app strings: say so when filing. Log: `logs/R2-a-20261117-165429/logcat-live.txt`.
- **O-5** (closest: R2-d, R2-e; O-3) With 0 credits the colour page's Generate button reads 「1 Free Trial」 with the
  price struck through (6 → 0), on every photo opened in R2-b (Free tier). One generation may therefore run without
  credits; R2-b did not tap it. Whether the free trial covers Custom, and whether it is spent once per install, is for
  R2-d to check (do not waste it on a photo the server rejects: use the Pexels portrait). Screenshot:
  `screenshots/TC-005_tilted30.png`.
- **O-6** (closest: TC-015; R-089) The Edit Room's Quick Actions row has no 「Hair Color」 tool on 90201901 (walked end to
  end, `screenshots/TC-015_quick*.png`); AI Hair Color sits under Portrait › Hair (with the bubble 「Give your hair a new
  color!」 on Hair) beside AI Hairstyle and Hair Volume. Recorded on TC-015 as part of its Fail; new since R1 (the v3 row
  names Quick Action after the Design 788:1354).
- **O-7** (closest: TC-016) hc_wide16x9.jpg now shows the face-too-small dialog before the colour page (no ratio
  dialog, so TC-016 step 1 still holds); 「Continue Anyway」 opens the room. A wider fixture face would avoid it.
  Leaving the colour page: ✕ lands in the Edit Room, Back there opens the Edit Room's own picker (Single / Batch),
  Back again the Launcher; 「Cancel」 on the ratio dialog also lands in the Edit Room.
- **O-8** (closest: TC-039, TC-027) Selecting a crowned Custom style (Balayage) as a Free user shows a 「VIP」
  「FREE TRIAL」 banner at the photo's top right, and Generate switches from 「1 Free Trial」 | 6 → 0 to plain
  「Generate」 | ⬤ 6 (the free trial does not cover premium styles). No row covers the banner (R2-e / R2-f context).
  Screenshots TC-039_before_small.png, TC-027_hl_only_small.png.
- **O-9** (closest: TC-026, TC-028) With any two-colour style the grey line 「Both Base Color and Highlight Color
  are required.」 is shown under the rows at all times, also when both colours are chosen and Generate is enabled.
- **O-10** (closest: TC-032, TC-035) A colour picked in the palette (Done) is kept as the row's value (the palette
  reopens at it) but is shown nowhere: the colour-wheel key takes the selection ring and stays a rainbow; the Custom
  cell never shows chosen colours either (TC-038). The palette opens at the row's current colour (hue 59 for navy,
  1 for pink).
- **O-11** (closest: TC-019) The S23 build 90201901 changed the Custom panel since R1 (90201900): grab handle + ⌄
  instead of title + ︽, ✕ ↺ ↻ ✓ hidden, colour rows hidden until a style is chosen, Highlight row hidden for Solid,
  eyedropper present, system Back collapses/applies the panel and closes only the palette, photo tap now applies,
  Base-only now disabled. Credits 0 all segment; no generation, free trial unused.
- **O-12** (closest: TC-071, TC-073; R-063, R-064) As VIP with 0 credits, 「GET CREDITS」 on the not-enough-credits
  dialog opened My Credits and popped 「3 Free Credits Have Been Issued to You」 (valid 1 day, claim again tomorrow;
  log `checkDailyBonus … dailyBonusCreditAmount: 3`, usage row category give_away 3), then 「Check Backup Protection」.
  The balance is now 3 (still under 6). No Quick Credit Refill (one-time 10-credit pack) was offered anywhere on the
  way. Back on Free the free trial button is expected to remain (not re-checked). Screenshots TC-071_shop.png.png,
  TC-071_shop3.png.png; log `logs/R2-f-20261118-085802/by-case/TC-071.txt`.
- **O-13** (closest: TC-050, TC-045) After the 2026-11-18 reinstall (Play-billing build, still 20.19.0 / 90201901,
  firstInstallTime 09:43:36, installer com.google.android.packageinstaller) the account held 166 credits from a
  `purchase_cp500` bonus item; Credits Details also lists six Reel Creator charges (-48 ×4, -72, -70) on 2026/11/18
  that this run did not make, and a 「Reel Creator Ready!」 notification arrived at 09:56 during TC-045. The balance is
  shared with other use of the install: match ledger rows by time and amount. Screenshot TC-050_detail.png.
- **O-14** (closest: TC-092, TC-093) The reinstall reset the photo guide: every AI Hair Color entry in R2-d showed it
  again before the picker (recipe `tapif Continue` got past it, 「Don't show again」 left unticked). TC-092 / TC-093 were
  not re-run.
- **O-15** (closest: TC-045, TC-047; R-041) On 90201901 (2026-11-18) the panel's Generate collapses the Custom panel at
  once to the Solid / Multicolor template row (Custom selected) and the result shows there; R1 (90201900) kept the
  panel open. Collapse now keeps Custom selected and the outer Generate runs a Custom generation (P0115's template
  generation gone), but the Custom cell still shows no colours (TC-038). A template result (Soft Black, TC-078) shows
  no Intensity row; Custom results do.
- **O-16** (closest: TC-059, TC-064, TC-067, TC-068) The build's Custom style names differ from the table's CMS keys
  and two pairs look alike on the Pexels hat portrait: 「Bangs」 on a no-fringe face colours the front pieces to the
  chin, close to 「Face framing」 (to the ends); 「Split-dye」 is the top / bottom split (line at mouth level) and
  「Dip-dye」 the ends below the chin; 「Half-and-half」 is the left / right split. Full list on 90201901: Solid, Ombre,
  Roots, Dip-dye, Balayage, Babylights, Face framing, Bangs, Earloop, Half-and-half, Split-dye (11). The log names no
  style key (every Custom generation logs `Style_010_Custom_HairColor_gpt-image-2.5-sunburst`), so the name → key map
  is inferred from the results (Q-13: CMS list not given). Screenshots TC-0xx_result.png.
- **O-17** (closest: TC-064) One extra Custom generation (Face framing, 10:25:17, 6 credits, chip 88 → 82) came from
  the agent's style-selection helper tapping the wrong cell before Dip-dye; not a case result and not an app fault.
  Screenshot r2e_extra_faceframing_result.png.
- **O-18** (closest: TC-062; R-040) As VIP (「Set to subscriber」 ON, Mine 「Hello VIP!」) every Custom style showed
  plain 「Generate」 | ⬤ 6 and took 6 credits, while Mine's Free card advertises 「Enjoy 50% off credit pricing」 for
  Premium. No crown badge showed on any style thumbnail while VIP. The table expects 6 credits (R-040), so no row
  fails; whether Premium should pay 3 is a question for PM, not a finding. Screenshots TC-062_before.png,
  r2e_mine_free_end.png.
- **O-19** (closest: TC-061) A Custom generation always starts from the original photo: after a red Solid result,
  Balayage produced a brown/copper result with no red left. The panel keeps the last Base / Highlight colours and the
  chosen style across collapse and re-open.
