# (MX) Christmas & New Year Sales — requirements (android)
Spec: Christmas New Year Sales - PM Figma 3226-21364.md, Christmas New Year Sales - Design Figma 2784-5280.md (Figma-only spec set 2026-11-20: PM page 3226:21364 in PDRM-MX, sections 「Christmas Sale」 and 「New Year Sale」; Design file [MX] Christmas & New Year, page 「2026」, sections 「Christmas」 2784:5280 and 「New year」 2844:5519), plus the two sheets the PM rules link: 「SKU 表」 (extracted/sku-table.md) and 「多國文案」 (extracted/multilang-copy.md).

Source order (formats.md): Design first; a newer PM item wins. The PM notes are dated 「1104 Update」 / 「Last Update: 1104」; the Design boards carry no date. Where the Design still draws what the PM 1104 notes removed (the 「Special Offer」 tag, 「67% OFF」, $31.99, the countdown under the subscription CTA), the 1104 PM wins and the Design version is in Notes. The Design interstitial already follows 1104 (「Christmas Special」, 「Save 57%」, no countdown), which dates the Design IAP plan card as older.
Both campaigns share one logic (PM: 「兩檔期Spec邏輯相同，但優惠及視覺會換」): every Christmas row has a New Year twin where the screen differs.
Android sells Pro, not Pro+ (KP-006).

## Campaign period, offers and SKUs
- R-001 [PM:pm-xmas-rules] The Christmas campaign runs 12/11 – 12/27 in the user's local time (17 days, 408 hr); its visuals and offers show only inside that window.
- R-002 [PM:pm-ny-rules] The New Year campaign runs 12/28 – 1/5 in the user's local time (9 days, 216 hr); at local midnight between 12/27 and 12/28 every Christmas visual and offer changes to its New Year version.
- R-003 [PM:pm-xmas-rules] Outside both windows (before 12/11 00:00 and from 1/6 00:00 local time) no campaign visual or offer shows: the Launcher, Mine, IAP and credit pages are the regular ones.
- R-004 [PM:pm-xmas-rules] During the promotion the New User Offer is not shown; it comes back when the promotion ends.
- R-005 [PM:pm-xmas-rules; SKU 表] Android annual plan: Pro Annual at its original price with a 7-day free trial, sold under SKU annualsubscription_christmas_2611 (Christmas) / annualsubscription_newyear_2611 (New Year); the SKU table prices it US $45.99, JP ¥6,100, FR/DE €37.99, UK £31.99, TW NT$1,210 (Q-3).
- R-006 [PM:pm-xmas-rules; SKU 表] Android monthly plan: 15% off, sold under SKU monthlysubscription_christmas_2611 / monthlysubscription_newyear_2611; the SKU table prices it US $6.99, JP ¥1190, FR/DE €7.49, UK £5.99, TW NT$240 (Q-3).
- R-007 [PM:pm-xmas-rules] In India, Indonesia and the Philippines the IAP page keeps its default landing on the monthly plan; elsewhere it lands on the annual plan (Design IAP_year: the annual card selected).
- R-008 [PM:pm-xmas-rules] Credit sale SKUs: a paid user is offered pdrm_2000_credit_paiduser_christmas, a free user pdrm_500_credit_freeuser_christmas; the New Year campaign uses the same two SKUs (PM New Year rules).
- R-009 [SKU 表] The Play purchase sheet a campaign CTA opens is for the campaign SKU of R-005 / R-006 / R-008 (observed in the Play sheet's product name and price, and in logcat), not the regular plan.

## Interstitial (subscription campaign page)
- R-010 [PM:pm-xmas-rules ➋] New free user, 1st launch: GDPR → the campaign interstitial.
- R-011 [PM:pm-xmas-rules ➋] New free user, 2nd launch: Open intro → the campaign interstitial.
- R-012 [PM:pm-xmas-rules ➋] New free user, 3rd and later (daily) launch: the campaign interstitial first (Q-4: once a day or every launch).
- R-013 [PM:pm-xmas-rules ➋] Upgrade free user (an existing free user who updates the app), 1st launch: Open intro → the campaign interstitial.
- R-014 [PM:pm-xmas-rules ➋] Upgrade free user, 2nd (daily) launch: the campaign interstitial.
- R-015 [PM:pm-xmas-rules ➋] On the interstitial, X returns to the Launcher.
- R-016 [PM:pm-xmas-rules ➋] On the interstitial, the CTA 「Get 7-Day Free Trial」 opens the Google Play payment panel for the annual campaign plan with its 7-day free trial.
- R-017 [PM:pm-xmas-rules ➋; DS:ds-xmas-interstitial] On the interstitial, 「More subscription plan」 opens the IAP page.
- R-018 [DS:ds-xmas-interstitial; PM:pm-xmas-launch 1104 Update] The Christmas interstitial shows the title art 「Christmas Special」 (never 「Sale」), 「SAVE」 「57」 「%」 as the largest element, 「vs. paying $6.79/mo × 12」, 「$34.99/year」, the CTA 「Get 7-Day Free Trial」, the trial terms, 「More subscription plan」 and 「Terms of Service」 | 「Privacy Policy」 | 「Restore purchase」; no struck-through original price and no countdown (1104). Prices follow the store (Q-3).
- R-019 [DS:ds-ny-interstitial; PM:pm-ny-launch 1104 Update] The New Year interstitial has the same layout with the title art 「New Year Special」 (fireworks, navy) and the same texts.
- R-020 [DS:ds-xmas-interstitial; PM:pm-xmas-launch] The trial terms read 「7 days free, then <annual price>/year. Subscription renews automatically until canceled. Cancel in Google Play at any time before the trial ends to avoid being charged.」 with the same annual price as the big price (the Design draws $31.99 under $34.99: Q-6).
- R-021 [DS:ds-xmas-interstitial] 「Terms of Service」 opens the Terms of Service page, 「Privacy Policy」 the Privacy Policy page, 「Restore purchase」 runs the restore (PM silent on targets: the app's existing pages).
- R-022 [PM:pm-xmas-rules 底圖 & 價格; 多國文案] The title art is a localized image made by Design (two seasons) and the lines under it (Save, vs., CTA) are localized text made by RD, per the 多國文案 sheet for each language (PM: 11 languages; the sheet and the Design: 27, Q-16).
- R-023 [DS:ds-xmas-iap-credit 短裝置] On a short Android screen (Design 「短裝置」, Pixel 2 411×731) the interstitial, IAP and credit pages show every element without overlap or clipping.
- R-024 [DS:ds-xmas-landscape] In landscape (tablet) the interstitial shows the 「Save 57%」 art on the left and the price, CTA, terms and 「More subscription plan」 on the right (Design 「Interstitial」 landscape).
- R-025 [Rule: Android system Back] System Back on the interstitial does what X does: back to the Launcher (spec silent: Q-5).

## Launcher (➌)
- R-026 [DS:ds-xmas-launcher-dialog; PM:pm-xmas-rules ➌] The Launcher top banner is the Christmas banner with the title 「Make Christmas magic with AI」 ›, drawn for both dark and light mode.
- R-027 [DS:ds-ny-launcher-dialog] In the New Year campaign the Launcher top banner title is 「Bring New Year moments to life」 ›, dark and light.
- R-028 [DS:ds-xmas-launcher-dialog; PM: flow arrow 3226-43005] For a free user the Launcher top pill reads 「Try Pro+ 7 days for free」 with a Santa-hat icon and opens the IAP page (Android sells Pro: Q-8).
- R-029 [DS:ds-ny-launcher-dialog; PM:pm-ny-launch] In the New Year campaign the Launcher and Mine top pill shows a clock icon and a countdown 「<d>D hh:mm:ss」 (Design 「2D 23:56:18」, PM 「6D 23:56:18」) that counts down; Q-9 asks what it counts to (assumption: the end of the New Year campaign).
- R-030 [PM:pm-xmas-rules ➌; DS:ds-xmas-launcher-dialog santa_claus_select / _unselect] The bottom bar's Mine tab icon is the Christmas icon (Santa hat) in both its selected and unselected states; the New Year campaign uses the New Year icon.
- R-031 [PM: flow arrow 3252-72047] Mine tab on the Launcher opens Mine.

## Mine tab and IAP page (➍)
- R-032 [DS:ds-xmas-launcher-dialog mine_free; PM: flow arrow 3252-72051] A free user's Mine card shows 「Free」, 「20+ Benefits」 and the button 「Claim Holiday Deal」, which opens the IAP page.
- R-033 [PM: flow arrow 3252-72045] A free user's Mine top pill opens the IAP page.
- R-034 [PM:pm-xmas-rules ➍; DS:ds-xmas-iap-credit] The IAP page top banner is a static Christmas banner 「Christmas Special」 (gift, decorations), the same image in every language (不出多國); New Year: 「New Year Special」.
- R-035 [PM:pm-xmas-launch 1104 Update; DS:ds-xmas-iap-credit] The annual plan card has the seasonal background image, a top-right tag with a small decoration reading 「Christmas Treat」 (New Year: 「New Year Treat」), and on its right half 「Save <xx>%」; no copy on the campaign pages uses 「Offer」 (Design still draws 「Special Offer」 / 「67% OFF」: older, Q-10).
- R-036 [PM:pm-xmas-rules ➍] The plan card's 「Save <xx>%」 is the difference between the campaign annual price and the campaign monthly price × 12, in % (PM 「Xmas 年價格 vs 月價格*12個月的價差%」; mockups: 57%).
- R-037 [PM:pm-xmas-launch 1104 Update] The monthly plan shows the original monthly price struck through and the discounted price next to it (mockup 「$7.99/Month」 struck, 「$6.79/Month」).
- R-038 [PM:pm-xmas-launch 1104 Update] The IAP page shows no countdown on or under 「Get 7-Day Free Trial」 (the Design draws 「2D 23:56:18」 there: older; the PM New Year rules still ask for one from 12/21: Q-11).
- R-039 [DS:ds-xmas-iap-credit] Above the CTA the IAP page reads 「Receive 35 credits during free trial」.
- R-040 [DS:ds-xmas-iap-credit; PM:pm-xmas-launch] The IAP page shows 「PowerDirector Pro」, 「No Watermark. Unlimited  Assets. No Ads. 50% Off Credit Pack.」, the feature cards 「Auto Edit」, 「4K Output」, 「Remove Watermark」, the trial terms with the annual price, and 「Terms of Service」 | 「Privacy Policy」 | 「Restore purchase」.
- R-041 [DS:ds-xmas-iap-credit] On the IAP page 「Get 7-Day Free Trial」 opens the Google Play panel for the selected campaign plan; choosing the monthly card first opens the monthly campaign plan.
- R-042 [DS:ds-xmas-iap-credit] The IAP page's back arrow ‹ returns to the page it was opened from.
- R-043 [PM:pm-xmas-rules ➍; PM:pm-xmas-launch JP / US] A paid user's VIP Benefits page (VIP Welcome Banner) carries Christmas decoration, in two versions: JP (「Merry Christmas! Enjoy...」 banner, 「20+ VIP features, 1000+ templates, and 250 free credits every month.」) and US (decorated VIP card); New Year decoration in the New Year campaign.
- R-044 [DS:ds-xmas-launcher-dialog mine_vip] A paid user's Mine top pill reads 「Credit Special Offer」 with a gift icon (Q-12: where it leads; assumption: the credit purchase page).

## Credit purchase page (➎)
- R-045 [PM:pm-xmas-rules ➎; DS:ds-xmas-iap-credit] The credit purchase page top banner is a static Christmas banner 「Christmas Special」, the same in every language (PM text 「Christmas Sale」, renamed by the 1104 update); New Year: 「New Year Special」.
- R-046 [PM:pm-xmas-rules ➎; DS:ds-xmas-iap-credit] For a paid user the Special Offer pack shows 「1000+1000」 (white 1000, green +1000) and 「$166.99」, and the CTA 「Get 2000 credits for $166.99」 buys it (pdrm_2000_credit_paiduser_christmas).
- R-047 [PM:pm-xmas-rules ➎] For a free user the Special Offer pack shows only a white 「500」 with the original price struck through and the sale price (PM-only: no Design frame yet; the sale price is not given, Q-13).
- R-048 [PM:pm-xmas-rules ➎; PM:pm-xmas-credit] A user without Credit Auto Pass sees the Auto Pass credit sale; a user with Auto Pass (「Auto Pass activated」) sees the 2000-credit pack sale (Q-14: what each one shows).
- R-049 [DS:ds-xmas-iap-credit; PM:pm-ny-rules ➎] A countdown 「⏱ <d>D hh:mm:ss」 shows above the credit page CTAs, from 12/21 for 7 days (PM New Year rules; Design draws 「2D 23:56:18」; Q-11).
- R-050 [DS:ds-xmas-iap-credit] For a paid user the regular packs show the original price struck through and the member price: 50 $9.99 → $4.99, 100 $17.99 → $8.99, 200 $31.99 → $15.99, 500 $69.99 → $34.99, 1000 $119.99 → $59.99, 2000 $199.99 → $99.99 (US mockup prices; the store sets the local ones).
- R-051 [DS:ds-xmas-iap-credit] 「Subscribe for 3000 free credits!」 opens the Credit Auto Pass subscription panel.
- R-052 [DS:ds-xmas-iap-credit] The credit page shows 「Each credit for about $0.1」, 「The expiration period for consumed credits is one year.」 and 「Privacy Policy」 | 「Terms of Use」, and its back arrow ‹ returns to the page it was opened from.

## Not Enough Credit dialog (➏)
- R-053 [PM:pm-xmas-rules ➏; PM:pm-xmas-credit; DS:ds-xmas-launcher-dialog I2V_Custom] A paid user who starts an AI feature without enough credits gets the dialog 「More Credits Needed!」 / 「You don’t have enough credits to use this feature. Get credits now!」 / 「Grab Discount Now!」 on the campaign background and image.
- R-054 [PM:pm-xmas-credit] For a paid user 「Grab Discount Now!」 opens the credit purchase page (the campaign version).
- R-055 [PM:pm-xmas-credit] A free user without enough credits gets 「Upgrade to Pro」 / 「You don’t have enough credits to use this feature. Upgrade to Pro to get free bonus credits every month.」 / 「Grab Discount Now!」 on the campaign background, and the CTA opens the campaign IAP page.
- R-056 [PM:pm-xmas-credit 「If點數夠」] With enough credits the feature starts generating; no dialog.
- R-057 [PM:pm-xmas-credit] The dialog's ⓧ closes it, back on the feature page with nothing charged.
- R-058 [PM:pm-ny-credit] In the New Year campaign the dialog background and image are the New Year theme (the PM New Year frames still read 「CHRISTMAS SALE」: Q-15).

## Landscape (Design 「Landscape」)
- R-059 [DS:ds-xmas-landscape] In landscape the Launcher shows the campaign top banner and pill over the regular landscape Launcher (My Projects, tool row).
- R-060 [DS:ds-xmas-landscape] In landscape the IAP page shows the 「Christmas Special」 art on the left and the plans, 「Receive 35 credits during free trial」, the CTA and the links on the right.

## Android system Back
- R-061 [Rule: Android system Back] System Back on the IAP page and on the credit purchase page does what their back arrow does (R-042, R-052).
- R-062 [Rule: Android system Back] System Back on the Not Enough Credit dialog closes it like ⓧ (R-057).
- R-063 [Rule: Android system Back] System Back on the VIP Benefits page returns to Mine.
- R-064 [Rule: Android system Back] System Back on the Google Play payment panel closes it without a purchase, back on the page that opened it.

## Flow arrows walked by existing rows
- R-065 [PM: flow arrow 3226-31539 https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-31539] Interstitial X → Launcher. Walked by: {{interstitial-x}}.
- R-066 [PM: flow arrow 3226-31190 https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-31190] Interstitial 「More subscription plan」 → IAP. Walked by: {{interstitial-more}}.
- R-067 [PM: flow arrow 3226-43005 https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-43005] Launcher top pill → IAP. Walked by: {{launcher-pill}}.
- R-068 [PM: flow arrow 3252-72047 https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3252-72047] Launcher Mine tab → Mine (the inventory names the tail 「USA Cam」; the geometry puts it on the Mine tab). Walked by: {{mine-tab}}.
- R-069 [PM: flow arrow 3252-72045 https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3252-72045] Mine top pill → IAP. Walked by: {{mine-pill}}.
- R-070 [PM: flow arrow 3252-72051 https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3252-72051] Mine 「Claim Holiday Deal」 → IAP. Walked by: {{claim-deal}}.
- R-071 [PM: flow arrow 3430-21182 https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3430-21182] New Year interstitial X → Launcher. Walked by: {{ny-interstitial-x}}.
- R-072 [PM: flow arrow 3430-25927 https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3430-25927] New Year interstitial 「More subscription plan」 → IAP. Walked by: {{ny-interstitial-more}}.
- R-073 [PM: flow arrow 3430-25851 https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3430-25851] New Year Launcher top pill → IAP. Walked by: {{ny-launcher-pill}}.
- R-074 [PM: flow arrow 3430-25926 https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3430-25926] New Year Launcher Mine tab → Mine. Walked by: {{ny-mine-tab}}.
- R-075 [PM: flow arrow 3430-27745 https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3430-27745] New Year Mine top pill → IAP. Walked by: {{ny-mine-pill}}.
- R-076 [PM: flow arrow 3430-27744 https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3430-27744] New Year Mine 「Claim Holiday Deal」 → IAP. Walked by: {{ny-claim-deal}}.

## Open questions
- Q-1 How does QA put the app into each campaign window before 12/11? Assumption: set the phone date and time by hand (Settings › Date & time, automatic off) to a day inside the window; if the window is server-checked, RD gives a test switch or server. Rows: every row with a 「Campaign」 precondition.
- Q-2 The PM notes give 「2025/12/11 – 12/27」 and 「2025/12/28 – 2025/01/05」 on a page named 「26 16.9」. Assumption: 2026-12-11 – 2026-12-27 and 2026-12-28 – 2027-01-05 (17 and 9 days, as the notes count). R-001, R-002, R-003.
- Q-3 Prices: the SKU table prices the Android US store at $45.99/year and $6.99/month (TW NT$1,210 / NT$240), while the Design and PM mockups and the 多國文案 sheet use $34.99/year, $6.79/month (15% off $7.99) and a fixed 「Save 57%」 / 「vs. $6.79/mo」. With the SKU table's US prices the PM formula gives 45%, with TW 58%. Which is right, and are 「57%」 and 「$6.79」 fixed text or computed from the store price? Assumption: the app shows the store's prices for the campaign SKUs, and 「Save xx%」 follows the PM formula on those prices; a fixed 57% that disagrees is recorded, not filed. R-005, R-006, R-018, R-036, R-037.
- Q-4 「3rd (Daily) Launch」 / 「2nd (Daily) Launch」: does the interstitial show once a day (the first launch of each day) or on every launch? Assumption: once a day. R-012, R-014.
- Q-5 What do system Back on the interstitial and a paid (Pro) user's launch do? The PM lists free users only. Assumption: Back acts like X; a Pro user gets no subscription interstitial (no row asserts the second). R-025.
- Q-6 The Design interstitial says 「7 days free, then $31.99/year」 under 「$34.99/year」 (PM 1104 frame: $34.99 in both). Assumption: the same annual price in both places. R-020.
- Q-7 Where does the Launcher top banner title 「Make Christmas magic with AI ›」 (New Year: 「Bring New Year moments to life ›」) lead? Not drawn. Assumption: the campaign's existing banner target; rows only check the banner.
- Q-8 Android sells Pro (KP-006), but the Launcher and Mine pill read 「Try Pro+ 7 days for free」 (Design and PM); the interstitial and IAP say 「PowerDirector Pro」. Assumption: Android shows the Pro wording the app already uses on this pill; the Design text is recorded. R-028.
- Q-9 The New Year Launcher and Mine pill shows a countdown (Design 「2D 23:56:18」, PM 「6D 23:56:18」): to what moment does it count, and is there one in the Christmas campaign? Assumption: to the end of the New Year campaign (1/5 23:59:59 local), New Year only. R-029.
- Q-10 The Design IAP plan card still draws 「Special Offer」, 「67% OFF」, $31.99/year and $7.99/month, which the PM 1104 update replaced (「Christmas Treat」, 「Save 57%」, struck monthly price, no 「Offer」 wording). Assumption: the PM 1104 version. R-035, R-037.
- Q-11 Countdowns: 1104 removed the countdown from the subscription CTA (both seasons), but the PM New Year rules (Last Update 1104) still say 「CTA BTN Get 7-day Free Trial 下方加上倒數鐘，12/21 開始倒數 7天」 and 「(Credit IAP) CTA BTN 上方加上倒數鐘，12/21 開始倒數 7天」; the Christmas rules say neither, while the Design draws one on the credit page. Assumption: no countdown on the IAP CTA; on the credit page a countdown from 12/21 counting to the end of the Christmas campaign (12/27 23:59:59). R-038, R-049.
- Q-12 Where does a paid user's 「Credit Special Offer」 pill lead? Assumption: the campaign credit purchase page. R-044.
- Q-13 The free user's 500-credit Special Offer has no Design frame and no sale price (「右側原價劃掉，顯示原價」 reads as 「show the original price」 twice). Assumption: the original price struck through and the Play price of pdrm_500_credit_freeuser_christmas beside it. R-047.
- Q-14 「未訂閱 Auto Pass 的用戶會看到 Auto Pass 的 Credit Sales；若已訂閱 Auto Pass，則會看到 2000 Credit Pack 的 Credit Sales」: the two PM frames show the same pack and the same two CTAs. What differs? Assumption: without Auto Pass the page leads with 「Subscribe for 3000 free credits!」; with Auto Pass it shows 「Auto Pass activated」 and the 2000-pack offer. R-048.
- Q-15 The PM New Year 「Not Enough Credit Dialog」 frames still read 「CHRISTMAS SALE」. Assumption: the New Year theme (PM: every Christmas visual becomes New Year). R-058.
- Q-16 The PM says Design makes 11 languages (ENG, CHT, CHS, FRA, DEU, Hindi, IND, ITA, JPN, KOR, ESP); the Design draws 27 title images and the 多國文案 sheet holds 27 (its 「ESP」 column appears twice, word for word). Assumption: all 27 ship. Also the JPN line 「通常月額 ¥6.79」 puts a yen sign on a dollar amount. R-022.
- Q-17 India, Indonesia and the Philippines (R-007) need a Play account in that country; the run marks those rows Blocked as test-data until one exists.
