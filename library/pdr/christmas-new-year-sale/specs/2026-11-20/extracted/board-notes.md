# Board notes — pdr/christmas-new-year-sale, spec set 2026-11-20 (Figma-only)

## PM — pm-xmas-rules / pm-ny-rules (PDRM-MX 3226:21364, 「Last Update: 1104」)
- Goal: sub revenue (free users) and credit revenue (paid users). Christmas 2025/12/11–12/27, New Year 2025/12/28–2025/01/05, user local time, 17 / 9 days (year: Q-2). Both seasons share the logic; visuals and offers switch.
- ➊ New User Offer hidden during the promotion. Android: Pro Annual original price with 7-day trial, Monthly 15% off; SKUs annualsubscription_christmas_2611 / monthlysubscription_christmas_2611 (New Year: _newyear_2611). India / Indonesia / Philippines land on monthly. Links 「SKU 表」 (sku-table.md) and 「多國文案」 (multilang-copy.md). Credit sale: paid pdrm_2000_credit_paiduser_christmas, free pdrm_500_credit_freeuser_christmas (New Year reuses them).
- ➋ Interstitial logic: new free user 1st GDPR → interstitial, 2nd Open intro → interstitial, 3rd daily interstitial; upgrade free user 1st Open intro → interstitial, 2nd daily. X → Launcher, CTA → payment panel, More subscription plans → IAP. Design makes the title art (11 languages × 2 seasons = 22 images), RD the localized text below.
- ➌ Launcher top banner (dark / light), Mine footer icon in the seasonal theme.
- ➍ Free: static gift top banner on IAP (not localized); annual card background, 「xx% Off」 kept, tag with decoration (text later changed by 1104), formula annual vs monthly × 12. New Year only: countdown under 「Get 7-day Free Trial」 from 12/21 (conflicts with 1104: Q-11). Paid: VIP Welcome Banner decorated, US and JP versions.
- ➎ Credit IAP: static top banner 「Christmas Sale」 (renamed Special by 1104), not localized; Special Offer pack 500 (free: white 500, original struck) / 1000+1000 (paid); New Year only: countdown above the CTA from 12/21 for 7 days; Auto Pass subscribers see the 2000-pack sale, others the Auto Pass sale (Q-14).
- ➏ Not Enough Credit dialog: seasonal background and image, CTA 「Grab Discount Now!」.

## PM — pm-xmas-launch / pm-ny-launch
- 1104 Update (interstitial): 「Christmas Sale」 → 「Christmas Special」 (no annual discount, so no 「Sale」), 「Save 57%」 stressed, struck original price and countdown removed.
- 1104 Update (IAP): tag 「Christmas Treat」 (no 「Offer」 wording anywhere), monthly struck original + discounted price, countdown removed from the CTA (it read as a countdown on the annual discount).
- Arrows: interstitial X → Launcher; 「More subscription plan」 → IAP_T1; Launcher top pill → IAP; Launcher Mine tab → mine_free (tail mislabelled 「USA Cam」); Mine top pill → IAP; 「Claim Holiday Deal」 → IAP. Free User 1st / 2nd / Daily launch images → interstitial.
- VIP Benefits page JP (「Merry Christmas! Enjoy...」) and US (decorated VIP card). New Year mine_free pill shows 「6D 23:56:18」.

## PM — pm-xmas-credit / pm-ny-credit / *-iap
- If credits short: paid → 「More Credits Needed!」 dialog → Grab Discount Now! → credit purchase page (無訂閱 / 已訂閱 Credit Auto Pass versions); free → 「Upgrade to Pro」 dialog → IAP_T1 (Christmas Treat, Save 57%, $6.79/Month). If enough: 開始gen. New Year frames still read 「CHRISTMAS SALE」 (Q-15). Credit IAP_Android (free) shows regular prices and 2D countdown.

## PM — pm-loose (older)
- Copies outside the sections: earlier interstitials (「Save 66% vs. Monthly」, $31.99, 「More subscription plans」, countdown) and a full older screen set. Traced older.

## Design — ds-xmas-* / ds-ny-* ([MX] Christmas & New Year, page 2026)
- Interstitial: 「Christmas Special」 / 「New Year Special」, SAVE 57%, 「vs. paying $6.79/mo × 12」, $34.99/year, Get 7-Day Free Trial, terms say $31.99 (Q-6), More subscription plan, ToS | Privacy | Restore. 27 language title frames.
- IAP & Credit: IAP_year (dark, light, short device) — Christmas Special banner, 「Special Offer」 tag, 67% OFF, $31.99/Year, $7.99/Month, Receive 35 credits during free trial, 2D 23:56:18 under the CTA (older than 1104). Credit purchase page — Christmas Special banner, 100 balance, Special Offer 1000+1000 $166.99, packs struck + member price, 2D 23:56:18 above CTAs, Subscribe for 3000 free credits!, Get 2000 credits for $166.99.
- Launcher & dialog: Launcher dark / light with 「Make Christmas magic with AI」 (New Year 「Bring New Year moments to life」), top pill 「Try Pro+ 7 days for free」 with Santa hat (New Year: clock + 2D countdown); mine_free 「Claim Holiday Deal」; mine_vip 「Credit Special Offer」 pill; I2V_Custom with 「More Credits Needed!」 dialog; Santa-claus select / unselect icons.
- Landscape: Launcher, interstitial (art left, price right), IAP.
- Note: 「由於設計只有一次性, 部分顏色&字級不做 color mapping & text style」 (one-off design; some colours and sizes are not tokens).
