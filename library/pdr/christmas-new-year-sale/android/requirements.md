# (MX) Christmas & New Year Sales — requirements (android)
Spec: Christmas New Year Sales - PM Figma 3226-21364.md, Christmas New Year Sales - Design Figma 2784-5280.md (Figma-only spec set 2026-11-20: PM page 3226:21364 in PDRM-MX, sections 「Christmas Sale」 and 「New Year Sale」; Design file [MX] Christmas & New Year, page 「2026」, sections 「Christmas」 2784:5280 and 「New year」 2844:5519), plus the two sheets the PM rules link: 「SKU 表」 (extracted/sku-table.md) and 「多國文案」 (extracted/multilang-copy.md).

Source order (formats.md): Design first; a newer PM item wins. The PM notes are dated 「1104 Update」 / 「Last Update: 1104」; the Design boards carry no date. Where the Design still draws what the PM 1104 notes removed (the 「Special Offer」 tag, 「67% OFF」, $31.99, the countdown under the subscription CTA), the 1104 PM wins and the Design version is in Notes. The Design interstitial already follows 1104 (「Christmas Special」, 「Save 57%」, no countdown), which dates the Design IAP plan card as older.
Both campaigns share one logic (PM: 「兩檔期Spec邏輯相同，但優惠及視覺會換」): every Christmas row has a New Year twin where the screen differs.
Android sells Pro, not Pro+ (KP-006; ruling Q-8, REQ-002).
Test setup (ruling Q-1, REQ-002): RD sets a test date on the stage server, and the app is tested against the stage server inside each window.

## Campaign period, offers and SKUs
- R-001 [PM:pm-xmas-rules; ruling Q-2, REQ-002] The Christmas campaign runs 2026-12-11 – 2026-12-27 in the user's local time (17 days, 408 hr); its visuals and offers show only inside that window.
- R-002 [PM:pm-ny-rules; ruling Q-2, REQ-002] The New Year campaign runs 2026-12-28 – 2027-01-05 in the user's local time (9 days, 216 hr); at local midnight between 12/27 and 12/28 every Christmas visual and offer changes to its New Year version.
- R-003 [PM:pm-xmas-rules] Outside both windows (before 12/11 00:00 and from 1/6 00:00 local time) no campaign visual or offer shows: the Launcher, Mine, IAP and credit pages are the regular ones.
- R-004 [PM:pm-xmas-rules] During the promotion the New User Offer is not shown; it comes back when the promotion ends.
- R-005 [PM:pm-xmas-rules; SKU 表] Android annual plan: Pro Annual at its original price with a 7-day free trial, sold under SKU annualsubscription_christmas_2611 (Christmas) / annualsubscription_newyear_2611 (New Year); the SKU table prices it US $45.99, JP ¥6,100, FR/DE €37.99, UK £31.99, TW NT$1,210; the app shows the store's SKU table price (ruling Q-3, REQ-002).
- R-006 [PM:pm-xmas-rules; SKU 表] Android monthly plan: 15% off, sold under SKU monthlysubscription_christmas_2611 / monthlysubscription_newyear_2611; the SKU table prices it US $6.99, JP ¥1190, FR/DE €7.49, UK £5.99, TW NT$240; the app shows the store's SKU table price (ruling Q-3, REQ-002).
- R-007 [PM:pm-xmas-rules] In India, Indonesia and the Philippines the IAP page keeps its default landing on the monthly plan; elsewhere it lands on the annual plan (Design IAP_year: the annual card selected). Testers set the account's country with Play Billing Lab (ruling Q-17, REQ-002).
- R-008 [PM:pm-xmas-rules] Credit sale SKUs: a paid user is offered pdrm_2000_credit_paiduser_christmas, a free user pdrm_500_credit_freeuser_christmas; the New Year campaign uses the same two SKUs (PM New Year rules).
- R-009 [SKU 表] The Play purchase sheet a campaign CTA opens is for the campaign SKU of R-005 / R-006 / R-008 (observed in the Play sheet's product name and price, and in logcat), not the regular plan.

## Interstitial (subscription campaign page)
- R-010 [PM:pm-xmas-rules ➋] New free user, 1st launch: GDPR → the campaign interstitial.
- R-011 [PM:pm-xmas-rules ➋] New free user, 2nd launch: Open intro → the campaign interstitial.
- R-012 [PM:pm-xmas-rules ➋] New free user, 3rd and later (daily) launch: the campaign interstitial first, once a day: a later launch the same day goes straight to the Launcher (ruling Q-4, REQ-002).
- R-013 [PM:pm-xmas-rules ➋] Upgrade free user (an existing free user who updates the app), 1st launch: Open intro → the campaign interstitial.
- R-014 [PM:pm-xmas-rules ➋] Upgrade free user, 2nd (daily) launch: the campaign interstitial.
- R-015 [PM:pm-xmas-rules ➋] On the interstitial, X returns to the Launcher.
- R-016 [PM:pm-xmas-rules ➋] On the interstitial, the CTA 「Get 7-Day Free Trial」 opens the Google Play payment panel for the annual campaign plan with its 7-day free trial.
- R-017 [PM:pm-xmas-rules ➋; DS:ds-xmas-interstitial] On the interstitial, 「More subscription plan」 opens the IAP page.
- R-018 [DS:ds-xmas-interstitial; PM:pm-xmas-launch 1104 Update] The Christmas interstitial shows the title art 「Christmas Special」 (never 「Sale」), 「SAVE」 「<xx>」 「%」 as the largest element, 「vs. paying <monthly price>/mo × 12」, 「<annual price>/year」, the CTA 「Get 7-Day Free Trial」, the trial terms, 「More subscription plan」 and 「Terms of Service」 | 「Privacy Policy」 | 「Restore purchase」; no struck-through original price and no countdown (1104). Prices are the store's SKU table prices (US $45.99/year, $6.99/month) and xx is computed from them as in R-036 (US: 45%); the mockups' 57% / $6.79 / $34.99 do not apply (ruling Q-3, REQ-002).
- R-019 [DS:ds-ny-interstitial; PM:pm-ny-launch 1104 Update] The New Year interstitial has the same layout with the title art 「New Year Special」 (fireworks, navy) and the same texts.
- R-020 [DS:ds-xmas-interstitial; PM:pm-xmas-launch] The trial terms read 「7 days free, then <annual price>/year. Subscription renews automatically until canceled. Cancel in Google Play at any time before the trial ends to avoid being charged.」 with the same annual price as the big price, the SKU table price (ruling Q-6, REQ-002; the Design draws $31.99 under $34.99).
- R-021 [DS:ds-xmas-interstitial] 「Terms of Service」 opens the Terms of Service page, 「Privacy Policy」 the Privacy Policy page, 「Restore purchase」 runs the restore (PM silent on targets: the app's existing pages).
- R-022 [PM:pm-xmas-rules 底圖 & 價格; 多國文案] The title art is a localized image made by Design (two seasons) and the lines under it (Save, vs., CTA) are localized text made by RD, per the 多國文案 sheet for each language All 27 languages of the sheet and the Design ship (ruling Q-16, REQ-002; the PM listed 11); the % and monthly price in the lines are the store's (ruling Q-3).
- R-023 [DS:ds-xmas-iap-credit 短裝置] On a short Android screen (Design 「短裝置」, Pixel 2 411×731) the interstitial, IAP and credit pages show every element without overlap or clipping.
- R-024 [DS:ds-xmas-landscape] In landscape (tablet) the interstitial shows the 「Save 57%」 art on the left and the price, CTA, terms and 「More subscription plan」 on the right (Design 「Interstitial」 landscape).
- R-025 [Rule: Android system Back] System Back on the interstitial does what X does: back to the Launcher (ruling Q-5, REQ-002).
- R-077 [ruling Q-5, REQ-002] A paid (Pro) user gets no subscription interstitial in either campaign.

## Launcher (➌)
- R-026 [DS:ds-xmas-launcher-dialog; PM:pm-xmas-rules ➌] The Launcher top banner is the Christmas banner with the title 「Make Christmas magic with AI」 ›, drawn for both dark and light mode.
- R-027 [DS:ds-ny-launcher-dialog] In the New Year campaign the Launcher top banner title is 「Bring New Year moments to life」 ›, dark and light.
- R-028 [DS:ds-xmas-launcher-dialog; PM: flow arrow 3226-43005] For a free user the Launcher top pill reads 「Try Pro 7 days for free」 (Pro, never Pro+: ruling Q-8, REQ-002; the Design and PM draw 「Try Pro+ 7 days for free」) with a Santa-hat icon and opens the IAP page.
- R-029 [DS:ds-ny-launcher-dialog; PM:pm-ny-launch; ruling Q-9, REQ-003] In the New Year campaign the Launcher and Mine top pill show a clock icon and a countdown 「<d>D hh:mm:ss」 that counts down (Design 「2D 23:56:18」, PM 「6D 23:56:18」; what it counts to and when it starts: Q-18, assumption the end of the New Year campaign, 2027-01-05 23:59:59 local, for the whole window); the Christmas pill has no countdown.
- R-030 [PM:pm-xmas-rules ➌; DS:ds-xmas-launcher-dialog santa_claus_select / _unselect] The bottom bar's Mine tab icon is the Christmas icon (Santa hat) in both its selected and unselected states; the New Year campaign uses the New Year icon.
- R-031 [PM: flow arrow 3252-72047] Mine tab on the Launcher opens Mine.

## Mine tab and IAP page (➍)
- R-032 [DS:ds-xmas-launcher-dialog mine_free; PM: flow arrow 3252-72051] A free user's Mine card shows 「Free」, 「20+ Benefits」 and the button 「Claim Holiday Deal」, which opens the IAP page.
- R-033 [PM: flow arrow 3252-72045] A free user's Mine top pill opens the IAP page.
- R-034 [PM:pm-xmas-rules ➍; DS:ds-xmas-iap-credit] The IAP page top banner is a static Christmas banner 「Christmas Special」 (gift, decorations), the same image in every language (不出多國); New Year: 「New Year Special」.
- R-035 [PM:pm-xmas-launch 1104 Update; DS:ds-xmas-iap-credit] The annual plan card has the seasonal background image, a top-right tag with a small decoration reading 「Christmas Treat」 (New Year: 「New Year Treat」), and on its right half 「Save <xx>%」; no copy on the campaign pages uses 「Offer」 (the Design still draws 「Special Offer」 / 「67% OFF」: the PM 1104 version applies, ruling Q-10, REQ-002).
- R-036 [PM:pm-xmas-rules ➍] The plan card's 「Save <xx>%」 is the difference between the campaign annual price and the campaign monthly price × 12, in % (PM 「Xmas 年價格 vs 月價格*12個月的價差%」), computed by the app from the store's SKU table prices: US $45.99 vs $6.99 × 12 → 45% (ruling Q-3, REQ-002; the mockups' fixed 57% does not apply).
- R-037 [PM:pm-xmas-launch 1104 Update] The monthly plan shows the original monthly price struck through and the discounted price next to it (mockup 「$7.99/Month」 struck, 「$6.79/Month」).
- R-038 [PM:pm-xmas-launch 1104 Update; ruling Q-11, REQ-003] In the Christmas campaign the IAP page shows no countdown on or under 「Get 7-Day Free Trial」; in the New Year campaign it shows the countdown under the CTA as the Design draws it (the PM 1104 note removing it is overruled; its value as R-029, Q-18).
- R-039 [DS:ds-xmas-iap-credit] Above the CTA the IAP page reads 「Receive 35 credits during free trial」.
- R-040 [DS:ds-xmas-iap-credit; PM:pm-xmas-launch] The IAP page shows 「PowerDirector Pro」, 「No Watermark. Unlimited  Assets. No Ads. 50% Off Credit Pack.」, the feature cards 「Auto Edit」, 「4K Output」, 「Remove Watermark」, the trial terms with the annual price, and 「Terms of Service」 | 「Privacy Policy」 | 「Restore purchase」.
- R-041 [DS:ds-xmas-iap-credit] On the IAP page 「Get 7-Day Free Trial」 opens the Google Play panel for the selected campaign plan; choosing the monthly card first opens the monthly campaign plan.
- R-042 [DS:ds-xmas-iap-credit] The IAP page's back arrow ‹ returns to the page it was opened from.
- R-043 [PM:pm-xmas-rules ➍; PM:pm-xmas-launch JP / US] A paid user's VIP Benefits page (VIP Welcome Banner) carries Christmas decoration, in two versions: JP (「Merry Christmas! Enjoy...」 banner, 「20+ VIP features, 1000+ templates, and 250 free credits every month.」) and US (decorated VIP card); New Year decoration in the New Year campaign.
- R-044 [DS:ds-xmas-launcher-dialog mine_vip] A paid user's Mine top pill reads 「Credit Special Offer」 with a gift icon and opens the campaign credit purchase page (ruling Q-12, REQ-002).

## Credit purchase page (➎)
- R-045 [PM:pm-xmas-rules ➎; DS:ds-xmas-iap-credit] The credit purchase page top banner is a static Christmas banner 「Christmas Special」, the same in every language (PM text 「Christmas Sale」, renamed by the 1104 update); New Year: 「New Year Special」.
- R-046 [PM:pm-xmas-rules ➎; DS:ds-xmas-iap-credit] For a paid user the Special Offer pack shows 「1000+1000」 (white 1000, green +1000) and 「$166.99」, and the CTA 「Get 2000 credits for $166.99」 buys it (pdrm_2000_credit_paiduser_christmas).
- R-047 [PM:pm-xmas-rules ➎] For a free user the Special Offer pack shows only a white 「500」 with the original price struck through and the sale price (PM-only: no Design frame yet; the sale price is not given, Q-13).
- R-048 [PM:pm-xmas-rules ➎; PM:pm-xmas-credit] A user without Credit Auto Pass sees the Auto Pass credit sale; a user with Auto Pass (「Auto Pass activated」) sees 「Auto Pass activated」 and the 2000-credit pack sale (ruling Q-14, REQ-002).
- R-049 [DS:ds-xmas-iap-credit; DS:ds-ny-iap-credit; PM:pm-ny-rules ➎; ruling Q-11, REQ-003] In the New Year campaign a countdown 「⏱ <d>D hh:mm:ss」 shows above the credit page CTAs (value as R-029, Q-18); the Christmas credit page has no countdown (the Design draws one there).
- R-050 [DS:ds-xmas-iap-credit] For a paid user the regular packs show the original price struck through and the member price: 50 $9.99 → $4.99, 100 $17.99 → $8.99, 200 $31.99 → $15.99, 500 $69.99 → $34.99, 1000 $119.99 → $59.99, 2000 $199.99 → $99.99 (US mockup prices; the store sets the local ones).
- R-051 [DS:ds-xmas-iap-credit] 「Subscribe for 3000 free credits!」 opens the Credit Auto Pass subscription panel.
- R-052 [DS:ds-xmas-iap-credit] The credit page shows 「Each credit for about $0.1」, 「The expiration period for consumed credits is one year.」 and 「Privacy Policy」 | 「Terms of Use」, and its back arrow ‹ returns to the page it was opened from.

## Not Enough Credit dialog (➏)
- R-053 [PM:pm-xmas-rules ➏; PM:pm-xmas-credit; DS:ds-xmas-launcher-dialog I2V_Custom] A paid user who starts an AI feature without enough credits gets the dialog 「More Credits Needed!」 / 「You don’t have enough credits to use this feature. Get credits now!」 / 「Grab Discount Now!」 on the campaign background and image.
- R-054 [PM:pm-xmas-credit] For a paid user 「Grab Discount Now!」 opens the credit purchase page (the campaign version).
- R-055 [PM:pm-xmas-credit] A free user without enough credits gets 「Upgrade to Pro」 / 「You don’t have enough credits to use this feature. Upgrade to Pro to get free bonus credits every month.」 / 「Grab Discount Now!」 on the campaign background, and the CTA opens the campaign IAP page.
- R-056 [PM:pm-xmas-credit 「If點數夠」] With enough credits the feature starts generating; no dialog.
- R-057 [PM:pm-xmas-credit] The dialog's ⓧ closes it, back on the feature page with nothing charged.
- R-058 [PM:pm-ny-credit] In the New Year campaign the dialog background and image are the New Year theme as the Design draws it (ruling Q-15, REQ-002; the PM New Year frames still read 「CHRISTMAS SALE」).

## Landscape (Design 「Landscape」)
- R-059 [DS:ds-xmas-landscape] In landscape the Launcher shows the campaign top banner and pill over the regular landscape Launcher (My Projects, tool row).
- R-060 [DS:ds-xmas-landscape] In landscape the IAP page shows the 「Christmas Special」 art on the left and the plans, 「Receive 35 credits during free trial」, the CTA and the links on the right.

## Android system Back
- R-061 [Rule: Android system Back] System Back on the IAP page and on the credit purchase page does what their back arrow does (R-042, R-052).
- R-062 [Rule: Android system Back] System Back on the Not Enough Credit dialog closes it like ⓧ (R-057).
- R-063 [Rule: Android system Back] System Back on the VIP Benefits page returns to Mine.
- R-064 [Rule: Android system Back] System Back on the Google Play payment panel closes it without a purchase, back on the page that opened it.

## Flow arrows walked by existing rows
- R-065 [PM: flow arrow 3226-31539 https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-31539] Interstitial X → Launcher. Walked by: TC-015.
- R-066 [PM: flow arrow 3226-31190 https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-31190] Interstitial 「More subscription plan」 → IAP. Walked by: TC-019.
- R-067 [PM: flow arrow 3226-43005 https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-43005] Launcher top pill → IAP. Walked by: TC-087.
- R-068 [PM: flow arrow 3252-72047 https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3252-72047] Launcher Mine tab → Mine (the inventory names the tail 「USA Cam」; the geometry puts it on the Mine tab). Walked by: TC-093.
- R-069 [PM: flow arrow 3252-72045 https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3252-72045] Mine top pill → IAP. Walked by: TC-098.
- R-070 [PM: flow arrow 3252-72051 https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3252-72051] Mine 「Claim Holiday Deal」 → IAP. Walked by: TC-096.
- R-071 [PM: flow arrow 3430-21182 https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3430-21182] New Year interstitial X → Launcher. Walked by: TC-022.
- R-072 [PM: flow arrow 3430-25927 https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3430-25927] New Year interstitial 「More subscription plan」 → IAP. Walked by: TC-026.
- R-073 [PM: flow arrow 3430-25851 https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3430-25851] New Year Launcher top pill → IAP. Walked by: TC-088.
- R-074 [PM: flow arrow 3430-25926 https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3430-25926] New Year Launcher Mine tab → Mine. Walked by: TC-094.
- R-075 [PM: flow arrow 3430-27745 https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3430-27745] New Year Mine top pill → IAP. Walked by: TC-099.
- R-076 [PM: flow arrow 3430-27744 https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3430-27744] New Year Mine 「Claim Holiday Deal」 → IAP. Walked by: TC-097.

## Added 2026-11-20 — coverage passes and standing inputs

### Job states
| Job | Start/loading | Success | Failure | Retry | Stop | Leave and return | Done notice |
|---|---|---|---|---|---|---|---|
| Subscription purchase (campaign SKU) | TC-017, TC-104 | TC-147 | n/a (Google Play's own errors; the spec names none) | n/a (spec silent) | TC-018 | n/a (spec silent) | n/a (spec silent) |
| Credit pack purchase (campaign SKU) | TC-122, TC-124 | TC-149, TC-148 | n/a (Google Play's own errors; the spec names none) | n/a (spec silent) | n/a (spec silent) | n/a (spec silent) | n/a (spec silent) |

### Exit × stage
| Stage | Close / back control | System Back (Android) |
|---|---|---|
| Interstitial open | TC-015, TC-022 | TC-016, TC-023 |
| IAP page open | TC-108 | TC-109 |
| Credit purchase page open | TC-130 | TC-130 |
| Not Enough Credit dialog open | TC-141 | TC-142 |
| VIP Benefits page open | n/a (no close control drawn) | TC-117 |
| Google Play payment panel open | n/a (Google Play's own panel) | TC-018, TC-025 |

### Error classes
| Job | Any error class |
|---|---|
| Subscription and credit purchases | n/a (the spec names no error classes; payment errors are Google Play's) |

### System back
- Interstitial: TC-016, TC-023 (like X; Q-5 ruling, REQ-002)
- IAP page: TC-109 (like the back arrow)
- Credit purchase page: TC-130 (like the back arrow)
- Not Enough Credit dialog: TC-142 (like ⓧ)
- VIP Benefits page: TC-117 (back to Mine)
- Google Play payment panel: TC-018, TC-025 (closes, no purchase)
- Terms of Service / Privacy Policy / Terms of Use pages: n/a (the app's existing pages, not part of this feature)

### Hidden clauses
| Requirement | Hidden clause | Observed through | Rows |
|---|---|---|---|
| R-009 | the purchase is made on the campaign SKU | logcat (billing SKU) and the Play panel's product | TC-017, TC-024, TC-104, TC-105, TC-107, TC-106, TC-122, TC-123, TC-124, TC-147 |
| R-001 | the window follows local time | phone time zone set ahead of UTC | TC-005 |

### Variants
| Requirement | Variant | Rows |
|---|---|---|
| R-022 | Christmas · ENG | TC-029 |
| R-022 | Christmas · CHT | TC-030 |
| R-022 | Christmas · CHS | TC-031 |
| R-022 | Christmas · FRA | TC-032 |
| R-022 | Christmas · DEU | TC-033 |
| R-022 | Christmas · Hindi | TC-034 |
| R-022 | Christmas · IND | TC-035 |
| R-022 | Christmas · ITA | TC-036 |
| R-022 | Christmas · JPN | TC-037 |
| R-022 | Christmas · KOR | TC-038 |
| R-022 | Christmas · ESP | TC-039 |
| R-022 | Christmas · Malay | TC-040 |
| R-022 | Christmas · PTB | TC-041 |
| R-022 | Christmas · RUS | TC-042 |
| R-022 | Christmas · Thai | TC-043 |
| R-022 | Christmas · ESP (MX) | TC-044 |
| R-022 | Christmas · Viet | TC-045 |
| R-022 | Christmas · Dutch | TC-046 |
| R-022 | Christmas · Turkish | TC-047 |
| R-022 | Christmas · Arabic | TC-048 |
| R-022 | Christmas · Polish | TC-049 |
| R-022 | Christmas · Persian | TC-050 |
| R-022 | Christmas · Hebrew | TC-051 |
| R-022 | Christmas · SVE | TC-052 |
| R-022 | Christmas · DAN | TC-053 |
| R-022 | Christmas · NOR | TC-054 |
| R-022 | Christmas · UKR | TC-055 |
| R-022 | New Year · ENG | TC-056 |
| R-022 | New Year · CHT | TC-057 |
| R-022 | New Year · CHS | TC-058 |
| R-022 | New Year · FRA | TC-059 |
| R-022 | New Year · DEU | TC-060 |
| R-022 | New Year · Hindi | TC-061 |
| R-022 | New Year · IND | TC-062 |
| R-022 | New Year · ITA | TC-063 |
| R-022 | New Year · JPN | TC-064 |
| R-022 | New Year · KOR | TC-065 |
| R-022 | New Year · ESP | TC-066 |
| R-022 | New Year · Malay | TC-067 |
| R-022 | New Year · PTB | TC-068 |
| R-022 | New Year · RUS | TC-069 |
| R-022 | New Year · Thai | TC-070 |
| R-022 | New Year · ESP (MX) | TC-071 |
| R-022 | New Year · Viet | TC-072 |
| R-022 | New Year · Dutch | TC-073 |
| R-022 | New Year · Turkish | TC-074 |
| R-022 | New Year · Arabic | TC-075 |
| R-022 | New Year · Polish | TC-076 |
| R-022 | New Year · Persian | TC-077 |
| R-022 | New Year · Hebrew | TC-078 |
| R-022 | New Year · SVE | TC-079 |
| R-022 | New Year · DAN | TC-080 |
| R-022 | New Year · NOR | TC-081 |
| R-022 | New Year · UKR | TC-082 |
| R-043 | JP version | TC-114 |
| R-043 | US version | TC-115 |
| R-043 | New Year | TC-116 |
| R-007 | India | TC-111 |
| R-007 | Indonesia | TC-112 |
| R-007 | Philippines | TC-113 |
| R-007 | other countries (annual) | TC-100 |
| R-026 | dark mode | TC-083 |
| R-026 | light mode | TC-084 |
| R-027 | dark mode | TC-085 |
| R-027 | light mode | TC-086 |
| R-034 | English | TC-100, TC-102 |
| R-034 | another language (日本語) | TC-118 |
| R-045 | English | TC-120, TC-121 |
| R-045 | another language (日本語) | TC-118 |
| R-030 | Christmas | TC-091 |
| R-030 | New Year | TC-092 |
| R-053 | Christmas | TC-132 |
| R-053 | New Year | TC-136 |
| R-055 | Christmas | TC-134 |
| R-055 | New Year | TC-138 |
| R-008 | Paid user (2000 pack) | TC-122, TC-149 |
| R-008 | Free user (500 pack) | TC-124, TC-148 |
| R-008 | New Year (same SKUs) | TC-123 |
| R-005 | Christmas SKU | TC-017, TC-104 |
| R-005 | New Year SKU | TC-024, TC-107 |
| R-006 | Christmas SKU | TC-105 |
| R-006 | New Year SKU | TC-106 |
| R-048 | without Auto Pass | TC-125 |
| R-048 | with Auto Pass | TC-126 |

### Domain rules
| Entry | Requirements |
|---|---|
| KP-007 A failed generation refunds its credits | n/a (this feature starts no generation of its own; the dialog row only checks that a generation starts) |
| KP-066 Android text against the Android font | n/a (design check only, figma skill) |

### Request ledger coverage
| Ledger entry | Requirements |
|---|---|
| REQ-001 | R-001 – R-076 (this table) |
| REQ-003 | Correction of Q-9 / Q-11: the New Year campaign keeps its countdowns, only Christmas drops them: R-029, R-038, R-049 |
| REQ-002 | Question answers 2026-11-20 (Q-1 – Q-6, Q-8 – Q-12, Q-14 – Q-17): R-001, R-002, R-005, R-006, R-012, R-018, R-020, R-022, R-025, R-028, R-029, R-035, R-036, R-038, R-044, R-048, R-049, R-058, R-007, R-077 |

## Answered questions
- Q-1 How does QA put the app into each campaign window before 12/11? Assumption: set the phone date and time by hand (Settings › Date & time, automatic off) to a day inside the window; if the window is server-checked, RD gives a test switch or server. Rows: every row with a 「Campaign」 precondition. Answer (2026-11-20, REQ-002, Cases page): RD sets a test date on the stage server; inside that window the app is tested on the stage server. Every row's campaign precondition is the RD test date.
- Q-2 The PM notes give 「2025/12/11 – 12/27」 and 「2025/12/28 – 2025/01/05」 on a page named 「26 16.9」. Assumption: 2026-12-11 – 2026-12-27 and 2026-12-28 – 2027-01-05 (17 and 9 days, as the notes count). R-001, R-002, R-003. Answer (2026-11-20, REQ-002, Cases page): 2026-12-11 – 2026-12-27 Christmas sale, 2026-12-28 – 2027-01-05 New Year sale. R-001, R-002.
- Q-3 Prices: the SKU table prices the Android US store at $45.99/year and $6.99/month (TW NT$1,210 / NT$240), while the Design and PM mockups and the 多國文案 sheet use $34.99/year, $6.79/month (15% off $7.99) and a fixed 「Save 57%」 / 「vs. $6.79/mo」. With the SKU table's US prices the PM formula gives 45%, with TW 58%. Which is right, and are 「57%」 and 「$6.79」 fixed text or computed from the store price? Assumption: the app shows the store's prices for the campaign SKUs, and 「Save xx%」 follows the PM formula on those prices; a fixed 57% that disagrees is recorded, not filed. R-005, R-006, R-018, R-036, R-037. Answer (2026-11-20, REQ-002, Cases page): prices follow the SKU table, and the discount % is computed by the app. R-005, R-006, R-018, R-022, R-036.
- Q-4 「3rd (Daily) Launch」 / 「2nd (Daily) Launch」: does the interstitial show once a day (the first launch of each day) or on every launch? Assumption: once a day. R-012, R-014. Answer (2026-11-20, REQ-002, Cases page): once a day. R-012.
- Q-5 What do system Back on the interstitial and a paid (Pro) user's launch do? The PM lists free users only. Assumption: Back acts like X; a Pro user gets no subscription interstitial (no row asserts the second). R-025. Answer (2026-11-20, REQ-002, Cases page): Back acts like X; a Pro user gets no subscription interstitial. R-025, new R-077.
- Q-6 The Design interstitial says 「7 days free, then $31.99/year」 under 「$34.99/year」 (PM 1104 frame: $34.99 in both). Assumption: the same annual price in both places. R-020. Answer (2026-11-20, REQ-002, Cases page): the SKU table price. R-020.
- Q-8 Android sells Pro (KP-006), but the Launcher and Mine pill read 「Try Pro+ 7 days for free」 (Design and PM); the interstitial and IAP say 「PowerDirector Pro」. Assumption: Android shows the Pro wording the app already uses on this pill; the Design text is recorded. R-028. Answer (2026-11-20, REQ-002, Cases page): Android uses the word Pro, never Pro+. R-028.
- Q-9 The New Year Launcher and Mine pill shows a countdown (Design 「2D 23:56:18」, PM 「6D 23:56:18」): to what moment does it count, and is there one in the Christmas campaign? Assumption: to the end of the New Year campaign (1/5 23:59:59 local), New Year only. R-029. Answer (2026-11-20, REQ-002, Cases page): every countdown is removed. Corrected (2026-11-20, REQ-003): the New Year campaign keeps its countdown; only Christmas drops it. R-029 (open part: Q-18).
- Q-10 The Design IAP plan card still draws 「Special Offer」, 「67% OFF」, $31.99/year and $7.99/month, which the PM 1104 update replaced (「Christmas Treat」, 「Save 57%」, struck monthly price, no 「Offer」 wording). Assumption: the PM 1104 version. R-035, R-037. Answer (2026-11-20, REQ-002, Cases page): the PM 1104 version. R-035.
- Q-11 Countdowns: 1104 removed the countdown from the subscription CTA (both seasons), but the PM New Year rules (Last Update 1104) still say 「CTA BTN Get 7-day Free Trial 下方加上倒數鐘，12/21 開始倒數 7天」 and 「(Credit IAP) CTA BTN 上方加上倒數鐘，12/21 開始倒數 7天」; the Christmas rules say neither, while the Design draws one on the credit page. Assumption: no countdown on the IAP CTA; on the credit page a countdown from 12/21 counting to the end of the Christmas campaign (12/27 23:59:59). R-038, R-049. Answer (2026-11-20, REQ-002, Cases page): every countdown is removed. Corrected (2026-11-20, REQ-003): the New Year campaign keeps its countdowns (IAP CTA and credit page); only Christmas drops them. R-038, R-049 (open part: Q-18).
- Q-12 Where does a paid user's 「Credit Special Offer」 pill lead? Assumption: the campaign credit purchase page. R-044. Answer (2026-11-20, REQ-002, Cases page): the campaign credit purchase page. R-044.
- Q-14 「未訂閱 Auto Pass 的用戶會看到 Auto Pass 的 Credit Sales；若已訂閱 Auto Pass，則會看到 2000 Credit Pack 的 Credit Sales」: the two PM frames show the same pack and the same two CTAs. What differs? Assumption: without Auto Pass the page leads with 「Subscribe for 3000 free credits!」; with Auto Pass it shows 「Auto Pass activated」 and the 2000-pack offer. R-048. Answer (2026-11-20, REQ-002, Cases page): with Auto Pass the page shows 「Auto Pass activated」. R-048.
- Q-15 The PM New Year 「Not Enough Credit Dialog」 frames still read 「CHRISTMAS SALE」. Assumption: the New Year theme (PM: every Christmas visual becomes New Year). R-058. Answer (2026-11-20, REQ-002, Cases page): the New Year theme, as the Design spec draws it. R-058.
- Q-16 The PM says Design makes 11 languages (ENG, CHT, CHS, FRA, DEU, Hindi, IND, ITA, JPN, KOR, ESP); the Design draws 27 title images and the 多國文案 sheet holds 27 (its 「ESP」 column appears twice, word for word). Assumption: all 27 ship. Also the JPN line 「通常月額 ¥6.79」 puts a yen sign on a dollar amount. R-022. Answer (2026-11-20, REQ-002, Cases page): all 27 languages ship. R-022.
- Q-17 India, Indonesia and the Philippines (R-007) need a Play account in that country; the run marks those rows Blocked as test-data until one exists. Answer (2026-11-20, REQ-002, Cases page): testers set the test account's country with Play Billing Lab. R-007.

## Open questions
- Q-7 Where does the Launcher top banner title 「Make Christmas magic with AI ›」 (New Year: 「Bring New Year moments to life ›」) lead? Not drawn. Assumption: the campaign's existing banner target; rows only check the banner.
- Q-13 The free user's 500-credit Special Offer has no Design frame and no sale price (「右側原價劃掉，顯示原價」 reads as 「show the original price」 twice). Assumption: the original price struck through and the Play price of pdrm_500_credit_freeuser_christmas beside it. R-047.
- Q-18 The New Year countdowns (Launcher and Mine pill, IAP under the CTA, credit page above the CTAs): what do they count to, and from when do they show? The PM New Year rules say 「12/21 開始倒數 7天」, a date before the New Year window opens (12/28), so it reads as copied from Christmas. Assumption: they count to the end of the New Year campaign (2027-01-05 23:59:59 local) and show for the whole window. R-029, R-038, R-049 (TC-089, TC-152).
