// Builds draft.csv and requirements.md for pdr/christmas-new-year-sale (android) from the rows below and
// requirements.base.md. Run: node library/pdr/christmas-new-year-sale/android/drafts/20261120-165128/build-draft.ts
// Update of v1 (draft 20261120-150930): the 2026-11-20 question answers (REQ-002). IDs come from v1-keys.json; the
// Change column is computed against the approved cases.csv, and every changed or new row names its reason (`why`).
import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const copy = JSON.parse(readFileSync(join(here, '../../../specs/2026-11-20/extracted/multilang-copy.json'), 'utf8'));

type Row = { k: string; sec: string; pre: string; act: string; exp: string; pri: string; refs: string; notes?: string; why?: string; removed?: string };
const rows: Row[] = [];
const add = (r: Row) => rows.push(r);
const lines = (...a: string[]) => a.join('\n');
const steps = (...a: string[]) => a.length === 1 ? a[0] : a.map((s, i) => `${i + 1}. ${s}`).join('\n');

const FREE = 'Free account (not subscribed) signed in';
const PRO = 'Pro account (subscribed) signed in';
// Q-1 ruling (REQ-002): RD sets a test date on the stage server; the app runs against the stage server.
const XMAS = 'Christmas window: stage server, RD test date 2026-12-15';
const NY = 'New Year window: stage server, RD test date 2026-12-30';
const DATE = (d: string) => `Stage server, RD test date ${d}`;
const US = 'Google Play account in the US store (Play Billing Lab)';
const W1 = 'Q-1 ruling (REQ-002): the campaign window is set by RD\'s test date on the stage server.';
const PILL = 'Try Pro 7 days for free';
const S = { xmas: { name: 'Christmas', pre: XMAS, title: 'Christmas Special', banner: 'Make Christmas magic with AI', treat: 'Christmas Treat' },
            ny: { name: 'New Year', pre: NY, title: 'New Year Special', banner: 'Bring New Year moments to life', treat: 'New Year Treat' } };
type Season = keyof typeof S;

// ---------- Campaign window ----------
add({ k: 'window-before', sec: 'Campaign window', pre: steps(FREE, DATE('2026-12-10 23:59')), act: steps('Launch the app', 'Open Mine', 'Open the IAP page'),
  exp: lines('No campaign interstitial', 'The Launcher top banner, the Mine tab icon and the IAP page are the regular ones (no 「Christmas Special」, no Christmas tag)', 'The New User Offer shows as usual'),
  pri: 'P1', refs: 'R-001, R-003, R-004', notes: 'Year 2026 (Q-2 ruling, REQ-002).', why: 'Q-1 / Q-2 rulings (REQ-002): RD test date on the stage server; the year is 2026.' });
add({ k: 'window-start', sec: 'Campaign window', pre: steps(FREE, 'Stage server'), act: steps('With the RD test date at 2026-12-10 23:59, launch the app', 'With the RD test date at 2026-12-11 00:00, close the app fully and launch it again'),
  exp: lines('Step 1: no campaign interstitial', 'Step 2: the Christmas interstitial 「Christmas Special」 shows', 'Step 2: behind it the Launcher shows the Christmas top banner'), pri: 'P1', refs: 'R-001, R-012', why: W1 });
add({ k: 'window-switch', sec: 'Campaign window', pre: steps(FREE, 'Stage server'), act: steps('With the RD test date at 2026-12-27 23:59, launch the app', 'With the RD test date at 2026-12-28 00:00, close the app fully and launch it again'),
  exp: lines('Step 1: the Christmas visuals show', 'Step 2: the interstitial is now 「New Year Special」', 'Step 2: the Launcher top banner reads 「Bring New Year moments to life」', 'Step 2: no Christmas visual is left on Launcher, Mine or IAP'), pri: 'P1', refs: 'R-002', why: W1 });
add({ k: 'window-end', sec: 'Campaign window', pre: steps(FREE, 'Stage server'), act: steps('With the RD test date at 2027-01-05 23:59, launch the app', 'With the RD test date at 2027-01-06 00:00, close the app fully and launch it again', 'Open Mine', 'Open the IAP page'),
  exp: lines('Step 1: the New Year visuals show', 'Steps 2–4: no campaign interstitial', 'Steps 2–4: the Launcher, Mine tab icon and IAP page are the regular ones', 'Steps 2–4: the New User Offer is back'), pri: 'P1', refs: 'R-002, R-003, R-004', why: W1 });
add({ k: 'window-tz', sec: 'Campaign window', pre: steps(FREE, 'Phone time zone UTC+8', DATE('2026-12-11 00:05 in UTC+8 (still 12/10 in UTC)')), act: 'Launch the app',
  exp: 'The Christmas campaign shows: the window follows the phone\'s local time, not UTC', pri: 'P2', refs: 'R-001', notes: 'PM: 「User Local Time」.', why: W1 });
for (const s of ['xmas', 'ny'] as Season[]) add({ k: `new-user-offer-${s}`, sec: 'Campaign window', pre: steps(FREE, S[s].pre, 'An account that would normally see the New User Offer (new install)'), act: steps('Launch the app', 'Open every subscription entry: interstitial, Launcher pill, Mine 「Claim Holiday Deal」'),
  exp: 'No New User Offer anywhere during the campaign', pri: 'P1', refs: 'R-004' });

// ---------- Interstitial ----------
add({ k: 'launch-new-1', sec: 'Interstitial', pre: steps('Fresh install (Android: uninstall, or `pm clear` after pulling logs)', XMAS), act: steps('Launch the app', 'Accept the GDPR screen (「Get Started」)'),
  exp: 'Right after GDPR the Christmas interstitial shows (before the Launcher)', pri: 'P1', refs: 'R-010' });
add({ k: 'launch-new-2', sec: 'Interstitial', pre: steps('The row above done (1st launch over)', XMAS), act: steps('Close the app fully', 'Launch it again (2nd launch)'),
  exp: lines('The Open intro shows first', 'After the intro the Christmas interstitial shows'), pri: 'P1', refs: 'R-011' });
add({ k: 'launch-new-3', sec: 'Interstitial', pre: steps('2nd launch over', 'RD test date moved to the next day inside the window (2026-12-16)'), act: steps('Close the app fully', 'Launch it again (3rd launch)', 'Close the app fully and launch it again the same day'),
  exp: lines('Step 2: the Christmas interstitial shows directly, with no intro', 'Step 3: no interstitial (once a day)', 'Step 3: the Launcher shows'), pri: 'P1', refs: 'R-012', notes: 'Q-4 ruling (REQ-002): once a day.', why: 'Q-4 ruling (REQ-002): the interstitial shows once a day; a same-day launch is now checked.' });
add({ k: 'launch-upg-1', sec: 'Interstitial', pre: steps('Free account on the previous app build, already past its first launches', XMAS, 'Install the build under test over it (adb install -r)'), act: 'Launch the app (1st launch after the update)',
  exp: lines('The Open intro shows first', 'Then the Christmas interstitial'), pri: 'P1', refs: 'R-013' });
add({ k: 'launch-upg-2', sec: 'Interstitial', pre: steps('The row above done', 'RD test date moved to the next day inside the window'), act: steps('Close the app fully', 'Launch it again'),
  exp: 'The Christmas interstitial shows directly, with no intro', pri: 'P1', refs: 'R-014', why: W1 });
for (const s of ['xmas', 'ny'] as Season[]) {
  const t = S[s];
  add({ k: s === 'xmas' ? 'interstitial-look' : 'ny-interstitial-look', sec: 'Interstitial', pre: steps(FREE, US, t.pre, 'App language English'), act: 'Launch the app and look at the interstitial',
    exp: lines(`Title art 「${t.title}」 (never 「Sale」)`, '「SAVE」 「45」 「%」 is the largest element (computed from the US store prices: $45.99 vs $6.99 × 12)', '「vs. paying $6.99/mo × 12」 under it (the US monthly price)', '「$45.99/year」 (the US annual price)', 'Yellow CTA 「Get 7-Day Free Trial」', 'Trial terms, 「More subscription plan」, 「Terms of Service」 | 「Privacy Policy」 | 「Restore purchase」', 'No struck-through price and no countdown'),
    pri: 'P1', refs: s === 'xmas' ? 'R-018, R-022' : 'R-019, R-022', notes: `${s === 'xmas' ? 'Design 2749:17877' : 'Design 2844:27481'}; PM 1104 Update. Q-3 ruling (REQ-002): prices from the SKU table, the % computed; the mockups' 57% / $6.79 / $34.99 are not the US store's.`,
    why: 'Q-3 ruling (REQ-002): prices from the SKU table (US $45.99 / $6.99), 「Save xx%」 computed.' });
  add({ k: s === 'xmas' ? 'interstitial-terms' : 'ny-interstitial-terms', sec: 'Interstitial', pre: steps(FREE, US, t.pre), act: 'Read the trial terms under the CTA',
    exp: '「7 days free, then $45.99/year. Subscription renews automatically until canceled. Cancel in Google Play at any time before the trial ends to avoid being charged.」, the same annual price as the big price', pri: 'P2', refs: 'R-020', notes: 'Q-6 ruling (REQ-002): the SKU table price; the Design draws $31.99 under $34.99.',
    why: 'Q-6 ruling (REQ-002): the trial terms carry the SKU table\'s annual price.' });
  add({ k: s === 'xmas' ? 'interstitial-x' : 'ny-interstitial-x', sec: 'Interstitial', pre: steps(FREE, t.pre, 'Interstitial showing'), act: 'Tap X',
    exp: 'The interstitial closes and the Launcher shows', pri: 'P1', refs: s === 'xmas' ? 'R-015, R-065' : 'R-015, R-071' });
  add({ k: s === 'xmas' ? 'interstitial-back' : 'ny-interstitial-back', sec: 'Interstitial', pre: steps(FREE, t.pre, 'Interstitial showing'), act: 'Press system Back',
    exp: 'The interstitial closes and the Launcher shows, as X does', pri: 'P2', refs: 'R-025', notes: 'Q-5 ruling (REQ-002): Back acts like X.', why: 'Q-5 ruling (REQ-002): Back acts like X (was an assumption).' });
  if (s === 'xmas') add({ k: 'pro-no-interstitial', sec: 'Interstitial', pre: steps(PRO, XMAS), act: steps('Close the app fully', 'Launch the app', 'RD test date moved to 2026-12-30 (New Year window); launch the app again'),
    exp: lines('Step 2: no subscription interstitial', 'Step 2: the Launcher shows directly', 'Step 3: no subscription interstitial'), pri: 'P2', refs: 'R-077', notes: 'Q-5 ruling (REQ-002).', why: 'Q-5 ruling (REQ-002): a Pro user gets no subscription interstitial.' });
  add({ k: s === 'xmas' ? 'interstitial-cta' : 'ny-interstitial-cta', sec: 'Interstitial', pre: steps(FREE, t.pre, 'Interstitial showing', 'Logcat running'), act: 'Tap 「Get 7-Day Free Trial」',
    exp: lines('The Google Play payment panel opens for the annual plan with a 7-day free trial', `The panel is for SKU ${s === 'xmas' ? 'annualsubscription_christmas_2611' : 'annualsubscription_newyear_2611'} (logcat) at the store's campaign price (SKU table)`), pri: 'P1', refs: 'R-016, R-005, R-009' });
  add({ k: s === 'xmas' ? 'panel-back' : 'ny-panel-back', sec: 'Interstitial', pre: steps(FREE, t.pre, 'Payment panel opened from the interstitial CTA'), act: 'Press system Back',
    exp: lines('The panel closes with no purchase', 'The interstitial is still there'), pri: 'P2', refs: 'R-064' });
  add({ k: s === 'xmas' ? 'interstitial-more' : 'ny-interstitial-more', sec: 'Interstitial', pre: steps(FREE, t.pre, 'Interstitial showing'), act: 'Tap 「More subscription plan」',
    exp: `The IAP page opens in its ${t.name} version`, pri: 'P1', refs: s === 'xmas' ? 'R-017, R-066' : 'R-017, R-072' });
}
add({ k: 'interstitial-tos', sec: 'Interstitial', pre: steps(FREE, XMAS, 'Interstitial showing'), act: steps('Tap 「Terms of Service」', 'Go back', 'Tap 「Privacy Policy」', 'Go back'),
  exp: lines('Step 1: the Terms of Service page opens', 'Step 2: back on the interstitial', 'Step 3: the Privacy Policy page opens', 'Step 4: back on the interstitial'), pri: 'P3', refs: 'R-021' });
add({ k: 'interstitial-restore', sec: 'Interstitial', pre: steps(FREE, XMAS, 'Interstitial showing'), act: 'Tap 「Restore purchase」',
  exp: lines('The app checks Google Play for purchases', 'With none it says so and stays Free'), pri: 'P3', refs: 'R-021' });

// ---------- Interstitial languages (多國文案, 27 languages × 2 seasons) ----------
const LOC: Record<string, string> = { ENG: 'English (US)', CHT: '中文（台灣）', CHS: '中文（简体）', FRA: 'Français', DEU: 'Deutsch', Hindi: 'हिन्दी', IND: 'Bahasa Indonesia', ITA: 'Italiano', JPN: '日本語', KOR: '한국어', ESP: 'Español (España)',
  Malay: 'Bahasa Melayu', PTB: 'Português (Brasil)', RUS: 'Русский', Thai: 'ไทย', 'ESP (MX)': 'Español (México)', Viet: 'Tiếng Việt', Dutch: 'Nederlands', Turkish: 'Türkçe', Arabic: 'العربية', Polish: 'Polski', Persian: 'فارسی', Hebrew: 'עברית', SVE: 'Svenska', DAN: 'Dansk', NOR: 'Norsk bokmål', UKR: 'Українська' };
const langRows: Record<string, string[]> = {};
for (const s of ['xmas', 'ny'] as Season[]) copy.langs.forEach((l: string, i: number) => {
  const k = `lang-${s}-${l}`; (langRows[`${s}|${l}`] ??= []).push(k);
  add({ k, sec: 'Interstitial languages', pre: steps(FREE, S[s].pre, `App language ${LOC[l]} (phone or app language setting)`), act: 'Launch the app and look at the interstitial',
    exp: lines(`Title art reads 「${copy.L1[s][i]} ${copy.L2[s][i]}」`, `「${String(copy.SAVE[i]).replace(/57|۵۷/, '<xx>')}」, xx computed from the store's annual and monthly prices`, `「${String(copy.VS[i]).replace(/[$¥€]?\s?(6[.,]79|۶[.,٫]۷۹)\s?€?/, '<monthly price>')}」 with the store's monthly price`, `CTA 「${copy.CTA[i]}」`, 'No text clipped, overlapped or in another language'),
    pri: l === 'ENG' || l === 'CHT' || l === 'JPN' ? 'P2' : 'P3', refs: 'R-022', notes: `多國文案 sheet, ${S[s].name} Special, ${l}. All 27 languages ship (Q-16 ruling, REQ-002).${l === 'JPN' ? ' Sheet text 「通常月額 ¥6.79」: the app shows the store price (Q-3 ruling).' : ''}`,
    why: 'Q-1 / Q-3 / Q-16 rulings (REQ-002): RD test date; the % and monthly price come from the store; all 27 languages ship.' });
});

// ---------- Launcher ----------
for (const s of ['xmas', 'ny'] as Season[]) {
  const t = S[s];
  for (const mode of ['dark', 'light']) add({ k: `banner-${s}-${mode}`, sec: 'Launcher', pre: steps(FREE, t.pre, `Phone in ${mode} mode`), act: 'Close the interstitial and look at the Launcher top',
    exp: lines(`The ${t.name} top banner with the title 「${t.banner}」 ›`, `The banner reads well in ${mode} mode (no white-on-white or black-on-black text)`), pri: 'P1', refs: s === 'xmas' ? 'R-026' : 'R-027', notes: 'PM: 「請design確認可符合dark/light mode的設計」.' });
}
add({ k: 'launcher-pill', sec: 'Launcher', pre: steps(FREE, XMAS, 'Launcher showing'), act: steps('Look at the top pill', 'Tap it'),
  exp: lines(`The pill reads 「${PILL}」 (Pro, never 「Pro+」) with the Santa-hat icon`, 'The Christmas IAP page opens'), pri: 'P1', refs: 'R-028, R-067', notes: 'Q-8 ruling (REQ-002): Android says Pro; the Design and PM draw 「Try Pro+ 7 days for free」.',
  why: 'Q-8 ruling (REQ-002): Android shows Pro wording, no Pro+.' });
add({ k: 'ny-launcher-pill', sec: 'Launcher', pre: steps(FREE, NY, 'Launcher showing'), act: 'Tap the top pill',
  exp: 'The New Year IAP page opens', pri: 'P1', refs: 'R-073' });
add({ k: 'ny-countdown', sec: 'Launcher', pre: steps(FREE, DATE('2027-01-03 12:00')), act: steps('Look at the Launcher top pill', 'Wait 10 seconds', 'Open Mine and look at its top pill', 'Open the IAP page from Mine', 'Go back and open Mine › Credits'),
  exp: lines('Step 1: a clock icon and a countdown 「2D 11:59:59」 or a little less (counting to 2027-01-05 23:59:59, Q-18)', 'Step 2: the seconds count down', 'Step 3: Mine\'s pill shows the same countdown', 'Step 4: the same countdown under 「Get 7-Day Free Trial」', 'Step 5: the same countdown above the CTAs'), pri: 'P2', refs: 'R-029, R-038, R-049', notes: 'Q-9 / Q-11 rulings (REQ-003): the New Year campaign keeps its countdowns. The Design draws 「2D 23:56:18」, the PM 「6D 23:56:18」.',
  why: 'Q-9 / Q-11 rulings corrected (REQ-003): the New Year campaign keeps its countdowns (pill, IAP, credit page).' });
add({ k: 'ny-countdown-start', sec: 'Launcher', pre: steps(FREE, DATE('2026-12-28 00:05')), act: steps('Launch the app and close the interstitial', 'Look at the Launcher top pill'),
  exp: lines('Step 2: a clock icon and a countdown 「8D 23:54:59」 or a little less (to 2027-01-05 23:59:59, Q-18)', 'Step 2: if no countdown shows yet, record when it first appears (Q-18)'), pri: 'P3', refs: 'R-029', notes: 'The PM New Year rules say 「12/21 開始倒數 7天」 (Q-18).',
  why: 'Q-9 ruling (REQ-003): the New Year countdown is checked at the start of the window too.' });
add({ k: 'xmas-no-pill-countdown', sec: 'Launcher', pre: steps(FREE, XMAS), act: 'Look at the Launcher top pill',
  exp: `The pill reads 「${PILL}」 with no countdown`, pri: 'P3', refs: 'R-028, R-029', why: 'Q-8 / Q-9 rulings (REQ-002, REQ-003): Pro wording; no countdown at Christmas.' });
for (const s of ['xmas', 'ny'] as Season[]) add({ k: `mine-icon-${s}`, sec: 'Launcher', pre: steps(FREE, S[s].pre), act: steps('Look at the Mine tab icon in the bottom bar on Home', 'Tap Mine', 'Tap Home'),
  exp: lines(`Step 1: the ${S[s].name} Mine icon${s === 'xmas' ? ' (Santa hat)' : ''}, unselected state`, `Step 2: the ${S[s].name} icon in its selected state, and Mine opens`, 'Step 3: back to the unselected icon'), pri: 'P2', refs: s === 'xmas' ? 'R-030, R-031' : 'R-030, R-031', notes: 'Design santa_claus_select / santa_claus_unselect.' });
add({ k: 'mine-tab', sec: 'Launcher', pre: steps(FREE, XMAS, 'Launcher showing'), act: 'Tap Mine in the bottom bar', exp: 'Mine opens with the Free card', pri: 'P1', refs: 'R-031, R-068' });
add({ k: 'ny-mine-tab', sec: 'Launcher', pre: steps(FREE, NY, 'Launcher showing'), act: 'Tap Mine in the bottom bar', exp: 'Mine opens with the Free card', pri: 'P2', refs: 'R-074' });

// ---------- Mine and IAP ----------
add({ k: 'mine-free-card', sec: 'Mine and IAP', pre: steps(FREE, XMAS), act: 'Open Mine',
  exp: lines('The Free card shows 「Free」 and 「20+ Benefits」', 'A yellow 「Claim Holiday Deal」 button on the card', `The top pill 「${PILL}」`), pri: 'P1', refs: 'R-032, R-028', why: 'Q-8 ruling (REQ-002): the pill says Pro, no Pro+.' });
add({ k: 'claim-deal', sec: 'Mine and IAP', pre: steps(FREE, XMAS, 'Mine showing'), act: 'Tap 「Claim Holiday Deal」', exp: 'The Christmas IAP page opens', pri: 'P1', refs: 'R-032, R-070' });
add({ k: 'ny-claim-deal', sec: 'Mine and IAP', pre: steps(FREE, NY, 'Mine showing'), act: 'Tap 「Claim Holiday Deal」', exp: 'The New Year IAP page opens', pri: 'P1', refs: 'R-076' });
add({ k: 'mine-pill', sec: 'Mine and IAP', pre: steps(FREE, XMAS, 'Mine showing'), act: 'Tap the top pill', exp: 'The Christmas IAP page opens', pri: 'P2', refs: 'R-033, R-069' });
add({ k: 'ny-mine-pill', sec: 'Mine and IAP', pre: steps(FREE, NY, 'Mine showing'), act: 'Tap the top pill', exp: 'The New Year IAP page opens', pri: 'P2', refs: 'R-075' });
for (const s of ['xmas', 'ny'] as Season[]) {
  const t = S[s];
  add({ k: `iap-look-${s}`, sec: 'Mine and IAP', pre: steps(FREE, t.pre, 'IAP page open from Mine'), act: 'Look at the whole IAP page',
    exp: lines(`Top banner 「${t.title}」, the same image in every language`, '「PowerDirector Pro」 and 「No Watermark. Unlimited  Assets. No Ads. 50% Off Credit Pack.」', 'Feature cards 「Auto Edit」, 「4K Output」, 「Remove Watermark」', 'The annual card is selected', `Annual card: seasonal background, top-right tag 「${t.treat}」 with a small decoration, 「Save <xx>%」 on its right half, 「<annual price>/Year」 and 「with 7-day free trial」`, 'Monthly card: the original price struck through and the discounted price', '「Receive 35 credits during free trial」 above the CTA', s === 'xmas' ? 'No countdown on or under 「Get 7-Day Free Trial」' : 'Under 「Get 7-Day Free Trial」 a clock icon and a countdown 「<d>D hh:mm:ss」 (TC-089 checks its value)', 'No 「Offer」 wording anywhere on the page'),
    pri: 'P1', refs: 'R-034, R-035, R-037, R-038, R-039, R-040, R-007', notes: `Q-10 ruling (REQ-002): the PM 1104 version; the Design plan card draws Special Offer, 67% OFF and $31.99. Q-11 ruling (REQ-003): ${s === 'xmas' ? 'no countdown in the Christmas campaign' : 'the New Year campaign keeps the countdown the Design draws under the CTA (the PM 1104 note removing it is overruled)'}.`,
    why: s === 'xmas' ? 'Q-1 / Q-10 / Q-11 rulings (REQ-002, REQ-003): RD test date; PM 1104 version; no countdown at Christmas.' : 'Q-1 / Q-10 / Q-11 rulings (REQ-002, REQ-003): RD test date; PM 1104 version; the New Year IAP keeps its countdown.' });
  add({ k: `iap-percent-${s}`, sec: 'Mine and IAP', pre: steps(FREE, US, t.pre, 'IAP page open'), act: steps('Note the annual price A and the discounted monthly price M on the cards', 'Read 「Save <xx>%」'),
    exp: lines('A = $45.99 and M = $6.99 (SKU table, US store)', 'xx = (M × 12 − A) ÷ (M × 12) × 100, rounded: 「Save 45%」', 'A fixed 「Save 57%」 (the mockups) is wrong'), pri: 'P1', refs: 'R-036, R-005, R-006', notes: 'Q-3 ruling (REQ-002): prices from the SKU table, the % computed. Another store follows its own SKU table prices (TW NT$1,210 / NT$240 → 58%).',
    why: 'Q-3 ruling (REQ-002): SKU table prices and a computed %.' });
}
add({ k: 'iap-cta-annual', sec: 'Mine and IAP', pre: steps(FREE, XMAS, 'IAP page open, annual card selected', 'Logcat running'), act: 'Tap 「Get 7-Day Free Trial」',
  exp: lines('The Google Play panel opens for the annual plan with a 7-day free trial', 'SKU annualsubscription_christmas_2611 (logcat) at the store\'s price'), pri: 'P1', refs: 'R-041, R-009' });
add({ k: 'iap-cta-monthly', sec: 'Mine and IAP', pre: steps(FREE, XMAS, 'IAP page open', 'Logcat running'), act: steps('Tap the monthly card', 'Tap the CTA'),
  exp: lines('Step 1: the monthly card is selected', 'Step 2: the Google Play panel opens for SKU monthlysubscription_christmas_2611 (logcat) at the store\'s discounted price'), pri: 'P1', refs: 'R-041, R-006, R-009' });
add({ k: 'ny-iap-cta-monthly', sec: 'Mine and IAP', pre: steps(FREE, NY, 'IAP page open', 'Logcat running'), act: steps('Tap the monthly card', 'Tap the CTA'),
  exp: 'The Google Play panel opens for SKU monthlysubscription_newyear_2611 (logcat)', pri: 'P2', refs: 'R-041, R-006, R-009' });
add({ k: 'ny-iap-cta-annual', sec: 'Mine and IAP', pre: steps(FREE, NY, 'IAP page open', 'Logcat running'), act: 'Tap 「Get 7-Day Free Trial」',
  exp: 'The Google Play panel opens for SKU annualsubscription_newyear_2611 (logcat)', pri: 'P2', refs: 'R-041, R-005, R-009' });
add({ k: 'iap-back', sec: 'Mine and IAP', pre: steps(FREE, XMAS, 'IAP page opened from Mine'), act: 'Tap the back arrow ‹', exp: 'Back on Mine', pri: 'P2', refs: 'R-042' });
add({ k: 'iap-sysback', sec: 'Mine and IAP', pre: steps(FREE, XMAS, 'IAP page opened from the interstitial 「More subscription plan」'), act: 'Press system Back', exp: 'Back where the IAP page was opened from, as the back arrow does', pri: 'P2', refs: 'R-061, R-042' });
add({ k: 'iap-links', sec: 'Mine and IAP', pre: steps(FREE, XMAS, 'IAP page open'), act: steps('Tap 「Terms of Service」', 'Go back', 'Tap 「Privacy Policy」', 'Go back', 'Tap 「Restore purchase」'),
  exp: lines('Step 1: the Terms of Service page opens', 'Step 3: the Privacy Policy page opens', 'Step 5: the restore runs and, with no purchase, the account stays Free'), pri: 'P3', refs: 'R-040' });
for (const c of ['India', 'Indonesia', 'Philippines']) add({ k: `landing-${c}`, sec: 'Mine and IAP', pre: steps(FREE, `Play Billing Lab sets the test account's country to ${c}`, XMAS), act: 'Open the IAP page from Mine',
  exp: lines('The monthly card is selected when the page opens', 'The campaign tag and prices still show'), pri: 'P2', refs: 'R-007', notes: 'Q-17 ruling (REQ-002): the country comes from Play Billing Lab.',
  why: 'Q-17 ruling (REQ-002): Play Billing Lab sets the test account country.' });
add({ k: 'vip-jp', sec: 'Mine and IAP', pre: steps(PRO, XMAS, 'App language 日本語, Play country Japan'), act: steps('Open Mine', 'Open the VIP Benefits page'),
  exp: lines('The JP layout: a Christmas banner 「Merry Christmas! Enjoy...」 with 「20+ VIP features, 1000+ templates, and 250 free credits every month.」', 'Christmas decoration on the welcome banner'), pri: 'P2', refs: 'R-043', notes: 'PM frame 3226:37164 (JP).' });
add({ k: 'vip-us', sec: 'Mine and IAP', pre: steps(PRO, XMAS, 'App language English, Play country US'), act: steps('Open Mine', 'Open the VIP Benefits page'),
  exp: 'The US layout: the VIP card with Christmas decoration', pri: 'P2', refs: 'R-043', notes: 'PM frame 3271:3807 (US).' });
add({ k: 'vip-ny', sec: 'Mine and IAP', pre: steps(PRO, NY), act: steps('Open Mine', 'Open the VIP Benefits page'), exp: 'The welcome banner carries New Year decoration, no Christmas decoration', pri: 'P2', refs: 'R-043' });
add({ k: 'vip-back', sec: 'Mine and IAP', pre: steps(PRO, XMAS, 'VIP Benefits page open'), act: 'Press system Back', exp: 'Back on Mine', pri: 'P3', refs: 'R-063' });
add({ k: 'banner-not-localized', sec: 'Mine and IAP', pre: steps(PRO, XMAS, 'App language 日本語'), act: steps('Open the IAP page', 'Open Mine › Credits'),
  exp: lines('Step 1: the IAP top banner 「Christmas Special」 is the same English image as in English', 'Step 2: the credit page top banner 「Christmas Special」 is the same English image as in English'), pri: 'P3', refs: 'R-034, R-045', notes: 'PM: 「不出多國」.' });
add({ k: 'credit-pill', sec: 'Mine and IAP', pre: steps(PRO, XMAS), act: steps('Open Mine', 'Tap the top pill 「Credit Special Offer」'),
  exp: lines('Step 1: the top pill reads 「Credit Special Offer」 with a gift icon', 'Step 2: the Christmas credit purchase page opens'), pri: 'P2', refs: 'R-044', notes: 'Q-12 ruling (REQ-002).', why: 'Q-12 ruling (REQ-002): the pill opens the campaign credit purchase page.' });

// ---------- Credit purchase page ----------
for (const s of ['xmas', 'ny'] as Season[]) {
  const t = S[s];
  add({ k: `credit-look-${s}`, sec: 'Credit purchase page', pre: steps(PRO, t.pre, 'No Credit Auto Pass', 'Credit purchase page open (Mine › Credits)'), act: 'Look at the whole page',
    exp: lines(`Top banner 「${t.title}」, the same image in every language`, 'Special Offer pack: white 「1000」 and green 「+1000」, 「$166.99」', 'Packs 50, 100, 200, 500, 1000, 2000 credits, each with its original price struck through and the member price', '「Subscribe for 3000 free credits!」 and 「Get 2000 credits for $166.99」', '「Each credit for about $0.1」 and 「The expiration period for consumed credits is one year.」', '「Privacy Policy」 | 「Terms of Use」', s === 'xmas' ? 'No countdown above the CTAs' : 'Above the CTAs a clock icon and a countdown 「<d>D hh:mm:ss」 (TC-089 checks its value)'),
    pri: 'P1', refs: 'R-045, R-046, R-050, R-052, R-049', notes: `US mockup prices: $9.99→$4.99, $17.99→$8.99, $31.99→$15.99, $69.99→$34.99, $119.99→$59.99, $199.99→$99.99. ${s === 'xmas' ? 'No countdown in the Christmas campaign' : 'The New Year campaign keeps the countdown'}: Q-11 ruling (REQ-003).`,
    why: s === 'xmas' ? 'Q-1 / Q-11 rulings (REQ-002, REQ-003): RD test date; the Christmas credit page has no countdown.' : 'Q-1 / Q-11 rulings (REQ-002, REQ-003): RD test date; the New Year credit page keeps its countdown.' });
}
add({ k: 'credit-buy-2000', sec: 'Credit purchase page', pre: steps(PRO, XMAS, 'Credit purchase page open', 'Logcat running'), act: 'Tap 「Get 2000 credits for $166.99」',
  exp: 'The Google Play panel opens for SKU pdrm_2000_credit_paiduser_christmas (logcat), 2000 credits at the store\'s price', pri: 'P1', refs: 'R-046, R-008, R-009' });
add({ k: 'ny-credit-buy-2000', sec: 'Credit purchase page', pre: steps(PRO, NY, 'Credit purchase page open', 'Logcat running'), act: 'Tap 「Get 2000 credits for $166.99」',
  exp: 'The Google Play panel opens for the same SKU pdrm_2000_credit_paiduser_christmas (logcat)', pri: 'P2', refs: 'R-008, R-009' });
add({ k: 'credit-free-500', sec: 'Credit purchase page', pre: steps(FREE, XMAS, 'Logcat running'), act: steps('Open Mine › Credits', 'Look at the Special Offer pack', 'Tap its CTA'),
  exp: lines('Step 2: the pack shows only a white 「500」', 'Step 2: the original price is struck through and the sale price is shown beside it (Q-13)', 'Step 3: the Google Play panel opens for SKU pdrm_500_credit_freeuser_christmas (logcat)'), pri: 'P1', refs: 'R-047, R-008, R-009', notes: 'PM-only: no Design frame yet (Design 2026-11-20).' });
add({ k: 'credit-autopass-no', sec: 'Credit purchase page', pre: steps(PRO, XMAS, 'No Credit Auto Pass subscription'), act: 'Open the credit purchase page',
  exp: lines('The Auto Pass credit sale leads: 「Subscribe for 3000 free credits!」', 'The balance line has no 「Auto Pass activated」'), pri: 'P1', refs: 'R-048', notes: 'Q-14 ruling (REQ-002).', why: 'Q-14 ruling (REQ-002) confirms what each Auto Pass state shows.' });
add({ k: 'credit-autopass-yes', sec: 'Credit purchase page', pre: steps(PRO, XMAS, 'Credit Auto Pass subscribed'), act: 'Open the credit purchase page',
  exp: lines('The balance line reads 「Auto Pass activated」', 'The 2000-credit pack sale shows: 「1000+1000」 「$166.99」 and 「Get 2000 credits for $166.99」'), pri: 'P1', refs: 'R-048', notes: 'Run after the Auto Pass purchase row. Q-14 ruling (REQ-002): with Auto Pass the page shows 「Auto Pass activated」.', why: 'Q-14 ruling (REQ-002): with Auto Pass the page shows 「Auto Pass activated」.' });
add({ k: 'credit-subscribe', sec: 'Credit purchase page', pre: steps(PRO, XMAS, 'No Credit Auto Pass', 'Credit purchase page open'), act: 'Tap 「Subscribe for 3000 free credits!」',
  exp: 'The Google Play panel opens for the Credit Auto Pass subscription', pri: 'P2', refs: 'R-051' });
add({ k: 'credit-countdown-before', sec: 'Credit purchase page', pre: steps(PRO, 'Phone date 2026-12-20 12:00 local, automatic date off'), act: 'Open the credit purchase page',
  exp: 'No countdown above the CTAs', pri: 'P2', refs: 'R-049', notes: 'PM: countdown from 12/21 for 7 days (Q-11).', removed: 'Q-11 ruling (REQ-002, corrected by REQ-003): the Christmas campaign has no countdown, so there is no start date to check; TC-129 checks the date the PM had asked for one.' });
add({ k: 'credit-countdown', sec: 'Credit purchase page', pre: steps(PRO, DATE('2026-12-25 00:03')), act: 'Open the credit purchase page',
  exp: 'No clock icon and no countdown above the CTAs (the PM New Year rules had asked for one from 12/21)', pri: 'P2', refs: 'R-049', notes: 'Q-11 ruling (REQ-003): only the Christmas campaign drops the countdown; the Design draws 「2D 23:56:18」 here.',
  why: 'Q-11 ruling (REQ-003): the Christmas credit page has no countdown.' });
add({ k: 'credit-back', sec: 'Credit purchase page', pre: steps(PRO, XMAS, 'Credit purchase page open from Mine'), act: steps('Tap the back arrow ‹', 'Open the page again', 'Press system Back'),
  exp: lines('Step 1: back on Mine', 'Step 3: back on Mine, as the arrow does'), pri: 'P2', refs: 'R-052, R-061' });
add({ k: 'credit-links', sec: 'Credit purchase page', pre: steps(PRO, XMAS, 'Credit purchase page open'), act: steps('Tap 「Privacy Policy」', 'Go back', 'Tap 「Terms of Use」'),
  exp: lines('Step 1: the Privacy Policy page opens', 'Step 3: the Terms of Use page opens'), pri: 'P3', refs: 'R-052' });

// ---------- Not Enough Credit dialog ----------
for (const s of ['xmas', 'ny'] as Season[]) {
  const t = S[s];
  add({ k: `nec-paid-${s}`, sec: 'Not Enough Credit dialog', pre: steps(PRO, t.pre, 'Credit balance below the price of Image to Video (Custom)'), act: steps('Open Image to Video › Custom', 'Enter a prompt', 'Tap 「Generate」'),
    exp: lines('The dialog 「More Credits Needed!」', '「You don’t have enough credits to use this feature. Get credits now!」', 'CTA 「Grab Discount Now!」', `${t.name} background and image`), pri: 'P1', refs: s === 'xmas' ? 'R-053' : 'R-053, R-058', notes: s === 'ny' ? 'Q-15 ruling (REQ-002): the New Year theme as the Design draws it; the PM New Year frames still say 「CHRISTMAS SALE」.' : 'Design I2V_Custom 2754:6631.',
    why: s === 'ny' ? 'Q-1 / Q-15 rulings (REQ-002): RD test date; the New Year theme from the Design.' : undefined });
  add({ k: `nec-paid-cta-${s}`, sec: 'Not Enough Credit dialog', pre: steps(PRO, t.pre, 'The dialog above open'), act: 'Tap 「Grab Discount Now!」', exp: `The ${t.name} credit purchase page opens`, pri: 'P1', refs: 'R-054' });
  add({ k: `nec-free-${s}`, sec: 'Not Enough Credit dialog', pre: steps(FREE, t.pre, 'Credit balance below the price of Image to Video (Custom)'), act: steps('Open Image to Video › Custom', 'Enter a prompt', 'Tap 「Generate」'),
    exp: lines('The dialog 「Upgrade to Pro」', '「You don’t have enough credits to use this feature. Upgrade to Pro to get free bonus credits every month.」', 'CTA 「Grab Discount Now!」', `${t.name} background and image`), pri: 'P1', refs: s === 'xmas' ? 'R-055' : 'R-055, R-058' });
  add({ k: `nec-free-cta-${s}`, sec: 'Not Enough Credit dialog', pre: steps(FREE, t.pre, 'The dialog above open'), act: 'Tap 「Grab Discount Now!」', exp: `The ${t.name} IAP page opens`, pri: 'P1', refs: 'R-055' });
}
add({ k: 'nec-enough', sec: 'Not Enough Credit dialog', pre: steps(PRO, XMAS, 'Credit balance above the price of Image to Video (Custom)'), act: steps('Open Image to Video › Custom', 'Enter a prompt', 'Tap 「Generate」'),
  exp: lines('No dialog', 'The generation starts and the credits are charged once'), pri: 'P1', refs: 'R-056' });
add({ k: 'nec-close', sec: 'Not Enough Credit dialog', pre: steps(PRO, XMAS, 'The paid dialog open', 'Balance noted'), act: 'Tap ⓧ',
  exp: lines('The dialog closes, back on Image to Video', 'The balance is unchanged'), pri: 'P2', refs: 'R-057' });
add({ k: 'nec-sysback', sec: 'Not Enough Credit dialog', pre: steps(FREE, XMAS, 'The free dialog open'), act: 'Press system Back',
  exp: 'The dialog closes, back on Image to Video, as ⓧ does', pri: 'P2', refs: 'R-062' });

// ---------- Layout ----------
add({ k: 'short-screen', sec: 'Layout', pre: steps(FREE, XMAS, 'A short Android screen (about 411×731 dp, or display size set largest)'), act: steps('Look at the interstitial', 'Open the IAP page', 'Open Mine › Credits'),
  exp: lines('Steps 1–3: every element shows with nothing clipped or overlapped', 'Steps 1–3: CTA, terms and links can be reached (scroll where the Design allows)'), pri: 'P2', refs: 'R-023', notes: 'Design 「短裝置」 frames 2750:20070, 2750:20280.' });
add({ k: 'land-launcher', sec: 'Layout', pre: steps(FREE, XMAS, 'Tablet or a phone the app turns to landscape'), act: 'Look at the Launcher in landscape',
  exp: 'The Christmas top banner and pill over the landscape Launcher (My Projects, tool row), nothing cut off', pri: 'P3', refs: 'R-059' });
add({ k: 'land-interstitial', sec: 'Layout', pre: steps(FREE, XMAS, 'Tablet or a phone the app turns to landscape'), act: 'Launch the app in landscape',
  why: 'Q-1 / Q-3 rulings (REQ-002): RD test date; the Save % is computed from the store prices.',
  exp: lines('Left: the 「Save <xx>%」 art (xx from the store prices, as in portrait)', 'Right: price, 「Get 7-Day Free Trial」, terms, 「More subscription plan」 and the links'), pri: 'P3', refs: 'R-024' });
add({ k: 'land-iap', sec: 'Layout', pre: steps(FREE, XMAS, 'Tablet or a phone the app turns to landscape'), act: 'Open the IAP page in landscape',
  exp: lines('Left: the 「Christmas Special」 art', 'Right: the plans, 「Receive 35 credits during free trial」, the CTA and the links'), pri: 'P3', refs: 'R-060' });

// ---------- Purchases (test purchases, run last: they make the account Pro) ----------
add({ k: 'buy-annual', sec: 'Purchases', pre: steps('Free license-tester account (Play sheet shows 「Test card, always approves」)', XMAS, 'Logcat running', 'Run after every Free row'), act: steps('On the interstitial tap 「Get 7-Day Free Trial」', 'Subscribe in the Google Play panel'),
  exp: lines('The purchase completes on SKU annualsubscription_christmas_2611 with a 7-day trial (logcat)', 'The app turns Pro: Mine shows the VIP card and the Free-user campaign entries are gone', 'The interstitial does not show on the next launch'), pri: 'P1', refs: 'R-005, R-009, R-016' });
add({ k: 'buy-credit-500', sec: 'Purchases', pre: steps('Free license-tester account', XMAS, 'Balance noted', 'Logcat running'), act: steps('Open Mine › Credits', 'Buy the 500-credit Special Offer'),
  exp: lines('SKU pdrm_500_credit_freeuser_christmas (logcat)', 'The balance grows by 500'), pri: 'P2', refs: 'R-047, R-008' });
add({ k: 'buy-credit-2000', sec: 'Purchases', pre: steps('Pro license-tester account', XMAS, 'Balance noted', 'Logcat running'), act: steps('Open Mine › Credits', 'Tap 「Get 2000 credits for $166.99」 and buy'),
  exp: lines('SKU pdrm_2000_credit_paiduser_christmas (logcat)', 'The balance grows by 2000 (1000 + 1000)'), pri: 'P2', refs: 'R-046, R-008' });
add({ k: 'buy-autopass', sec: 'Purchases', pre: steps('Pro license-tester account without Auto Pass', XMAS), act: steps('Open Mine › Credits', 'Tap 「Subscribe for 3000 free credits!」 and subscribe'),
  exp: lines('The subscription completes', 'The page now shows 「Auto Pass activated」 (the next row checks its offer)'), pri: 'P2', refs: 'R-048, R-051' });

// ---------- write ----------
const v1keys: Record<string, string> = JSON.parse(readFileSync(join(here, 'v1-keys.json'), 'utf8'));
const ids = new Map<string, string>(Object.entries(v1keys));
let next = Math.max(...Object.values(v1keys).map(v => Number(v.slice(3))));
for (const r of rows) if (!ids.has(r.k)) ids.set(r.k, `TC-${String(++next).padStart(3, '0')}`);
const id = (k: string) => { const v = ids.get(k); if (!v) throw new Error(`no row ${k}`); return v; };
const q = (s: string) => /[",\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s;
// the approved table (v1), parsed with a small CSV reader
const parseCsv = (t: string) => { const out: string[][] = []; let row: string[] = [], f = '', inq = false;
  for (let i = 0; i < t.length; i++) { const c = t[i];
    if (inq) { if (c === '"') { if (t[i + 1] === '"') { f += '"'; i++; } else inq = false; } else f += c; }
    else if (c === '"') inq = true; else if (c === ',') { row.push(f); f = ''; } else if (c === '\n') { row.push(f); out.push(row); row = []; f = ''; } else if (c !== '\r') f += c; }
  if (f || row.length) { row.push(f); out.push(row); } return out; };
const v1 = parseCsv(readFileSync(join(here, '../../cases.csv'), 'utf8').replace(/^﻿/, ''));
const v1rows = new Map(v1.slice(1).map(r => [r[0], r]));
const head = ['ID', 'Section', 'Precondition', 'Action', 'Expected Result', 'Priority', 'Spec Ref', 'Notes', 'Change', 'Change Reason'];
const counts: Record<string, number> = {};
const out = rows.map(r => {
  const cells = [id(r.k), r.sec, r.pre, r.act, r.exp, r.pri, r.refs, r.notes ?? ''];
  const old = v1rows.get(id(r.k));
  let change: string, reason = '';
  if (!old) { change = 'new'; reason = r.why ?? ''; if (!reason) throw new Error(`new row ${r.k} has no why`); }
  else if (r.removed) { change = 'removed'; reason = r.removed; }
  else if (old.slice(0, 8).every((v, i) => v === cells[i])) change = 'unchanged';
  else { change = 'modified'; reason = r.why ?? (/RD test date|Stage server/.test(r.pre) ? W1 : ''); if (!reason) throw new Error(`modified row ${r.k} has no why`); }
  counts[change] = (counts[change] ?? 0) + 1;
  return [...cells, change, reason].map(q).join(',');
});
for (const k of Object.keys(v1keys)) if (!rows.some(r => r.k === k)) throw new Error(`v1 row ${k} missing from the builder`);
writeFileSync(join(here, 'draft.csv'), [head.join(','), ...out].join('\n') + '\n');
console.log(counts);

const by = (...ks: string[]) => ks.map(id).join(', ');
let req = readFileSync(join(here, 'requirements.base.md'), 'utf8').replace(/\{\{([\w-]+)\}\}/g, (_, k) => id(k));
const variants: string[] = [];
for (const s of ['xmas', 'ny'] as Season[]) for (const l of copy.langs) variants.push(`| R-022 | ${S[s].name} · ${l} | ${by(`lang-${s}-${l}`)} |`);
variants.push(`| R-043 | JP version | ${by('vip-jp')} |`, `| R-043 | US version | ${by('vip-us')} |`, `| R-043 | New Year | ${by('vip-ny')} |`);
variants.push(`| R-007 | India | ${by('landing-India')} |`, `| R-007 | Indonesia | ${by('landing-Indonesia')} |`, `| R-007 | Philippines | ${by('landing-Philippines')} |`, `| R-007 | other countries (annual) | ${by('iap-look-xmas')} |`);
variants.push(`| R-026 | dark mode | ${by('banner-xmas-dark')} |`, `| R-026 | light mode | ${by('banner-xmas-light')} |`, `| R-027 | dark mode | ${by('banner-ny-dark')} |`, `| R-027 | light mode | ${by('banner-ny-light')} |`);
variants.push(`| R-034 | English | ${by('iap-look-xmas', 'iap-look-ny')} |`, `| R-034 | another language (日本語) | ${by('banner-not-localized')} |`, `| R-045 | English | ${by('credit-look-xmas', 'credit-look-ny')} |`, `| R-045 | another language (日本語) | ${by('banner-not-localized')} |`);
variants.push(`| R-030 | Christmas | ${by('mine-icon-xmas')} |`, `| R-030 | New Year | ${by('mine-icon-ny')} |`);
variants.push(`| R-053 | Christmas | ${by('nec-paid-xmas')} |`, `| R-053 | New Year | ${by('nec-paid-ny')} |`, `| R-055 | Christmas | ${by('nec-free-xmas')} |`, `| R-055 | New Year | ${by('nec-free-ny')} |`);
variants.push(`| R-008 | Paid user (2000 pack) | ${by('credit-buy-2000', 'buy-credit-2000')} |`, `| R-008 | Free user (500 pack) | ${by('credit-free-500', 'buy-credit-500')} |`, `| R-008 | New Year (same SKUs) | ${by('ny-credit-buy-2000')} |`);
variants.push(`| R-005 | Christmas SKU | ${by('interstitial-cta', 'iap-cta-annual')} |`, `| R-005 | New Year SKU | ${by('ny-interstitial-cta', 'ny-iap-cta-annual')} |`, `| R-006 | Christmas SKU | ${by('iap-cta-monthly')} |`, `| R-006 | New Year SKU | ${by('ny-iap-cta-monthly')} |`);
variants.push(`| R-048 | without Auto Pass | ${by('credit-autopass-no')} |`, `| R-048 | with Auto Pass | ${by('credit-autopass-yes')} |`);
const added = `
## Added 2026-11-20 — coverage passes and standing inputs

### Job states
| Job | Start/loading | Success | Failure | Retry | Stop | Leave and return | Done notice |
|---|---|---|---|---|---|---|---|
| Subscription purchase (campaign SKU) | ${by('interstitial-cta', 'iap-cta-annual')} | ${by('buy-annual')} | n/a (Google Play's own errors; the spec names none) | n/a (spec silent) | ${by('panel-back')} | n/a (spec silent) | n/a (spec silent) |
| Credit pack purchase (campaign SKU) | ${by('credit-buy-2000', 'credit-free-500')} | ${by('buy-credit-2000', 'buy-credit-500')} | n/a (Google Play's own errors; the spec names none) | n/a (spec silent) | n/a (spec silent) | n/a (spec silent) | n/a (spec silent) |

### Exit × stage
| Stage | Close / back control | System Back (Android) |
|---|---|---|
| Interstitial open | ${by('interstitial-x', 'ny-interstitial-x')} | ${by('interstitial-back', 'ny-interstitial-back')} |
| IAP page open | ${by('iap-back')} | ${by('iap-sysback')} |
| Credit purchase page open | ${by('credit-back')} | ${by('credit-back')} |
| Not Enough Credit dialog open | ${by('nec-close')} | ${by('nec-sysback')} |
| VIP Benefits page open | n/a (no close control drawn) | ${by('vip-back')} |
| Google Play payment panel open | n/a (Google Play's own panel) | ${by('panel-back', 'ny-panel-back')} |

### Error classes
| Job | Any error class |
|---|---|
| Subscription and credit purchases | n/a (the spec names no error classes; payment errors are Google Play's) |

### System back
- Interstitial: ${by('interstitial-back', 'ny-interstitial-back')} (like X; Q-5 ruling, REQ-002)
- IAP page: ${by('iap-sysback')} (like the back arrow)
- Credit purchase page: ${by('credit-back')} (like the back arrow)
- Not Enough Credit dialog: ${by('nec-sysback')} (like ⓧ)
- VIP Benefits page: ${by('vip-back')} (back to Mine)
- Google Play payment panel: ${by('panel-back', 'ny-panel-back')} (closes, no purchase)
- Terms of Service / Privacy Policy / Terms of Use pages: n/a (the app's existing pages, not part of this feature)

### Hidden clauses
| Requirement | Hidden clause | Observed through | Rows |
|---|---|---|---|
| R-009 | the purchase is made on the campaign SKU | logcat (billing SKU) and the Play panel's product | ${by('interstitial-cta', 'ny-interstitial-cta', 'iap-cta-annual', 'iap-cta-monthly', 'ny-iap-cta-annual', 'ny-iap-cta-monthly', 'credit-buy-2000', 'ny-credit-buy-2000', 'credit-free-500', 'buy-annual')} |
| R-001 | the window follows local time | phone time zone set ahead of UTC | ${by('window-tz')} |

### Variants
| Requirement | Variant | Rows |
|---|---|---|
${variants.join('\n')}

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
`;
req = req.replace('\n## Answered questions', added + '\n## Answered questions');
writeFileSync(join(here, 'requirements.md'), req);
console.log(`${rows.length} rows`);
