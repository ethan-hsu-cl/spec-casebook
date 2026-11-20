#!/usr/bin/env python3
"""Build the AI Hair Color Custom Android eBug draft batch for round R3 (table v4, draft 20261118-120459) on 20.19.0 (90201901).

Writes ../20261120_eBug_drafts_AI-Hair-Color-Custom-R3_20.19.0.md, the sibling _images/ folder (one NN_ISS-ID folder per
entry: JPEGs named 20.19.0_hccNN_<slug>.jpg with a red box where it helps, plus the logcat excerpt where the finding has
a log cause) and logs/. Nothing is filed. Every Fail row of results.csv and every observation O-n is mapped (entry /
recheck of a filed ticket / not raised); the script stops when one is missing. Entry numbers continue R1's
(ISS-HCC-31 onward; 29 and 30 were used by the tr-verify TR261118-0070 batch, filed as PHA262026P0149 / P0150). Built from the R2 generator (../../2026-11-18-r2/generators/ebugs.py).
Run: python library/phd/ai-hair-color-custom/android/ebugs/2026-11-20-r3/generators/ebugs.py
"""
import csv, json, os, re, shutil, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(OUT, "..", ".."))           # library/phd/ai-hair-color-custom/android
RUN = f"{ROOT}/runs/2026-11-20-r3"
NAME = "20261120_eBug_drafts_AI-Hair-Color-Custom-R3_20.19.0"
V, B = "20.19.0", "90201901"
DAY = "2026-11-20"
PROD = "PHD-A"
FEAT = "AI_Hair_Color"
DEVICE = "Device: Google Pixel 8a / Android 16"
PM_URL = "https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair"
DS_URL = "https://www.figma.com/design/2VOqiPxBCISkob7wbM9hXD/Hair"


def pm(frame, node):
    return f"Spec Link: AI Hair Color Custom PM Figma (26 11E AI Hair Color Custom), {frame} -\n{PM_URL}?node-id={node}"


def tene(rule, node):
    return f"Spec Link: AI Hair Color PM Figma (26 10E AI Hair Color v2, cited by the Custom page), {rule} -\n{PM_URL}?node-id={node}"


def ds(frame, node):
    return f"Spec Link: AI Hair Color Design Figma (Hair, 261005_AI_hair_color page), {frame} -\n{DS_URL}?node-id={node}"


FACEB = pm("Spec - 進房檢查 & Photo Picker board (11/25)", "3370-1666")
P_TWO = pm("panel_two_tone (NEW) frame, Spec - UI (D6-04)", "3327-1077")
P_COLL = pm("collapsed_applied (NEW) frame, Spec - UI (D6-08)", "3330-512")
P_RES = pm("result_custom (NEW) frame, Spec - UI", "3330-718")
P_FLOW = pm("Spec - Flow board (in-panel Generate, D6-22 / D6-23)", "3287-93")
E_X = tene("Spec - UI rule D1-20b (✕ leaves with no confirmation)", "3030-296")
E_CREDIT = tene("Credit not enough card (subscriber → More Credits Required! → Get Credit)", "3031-293")
D_GUIDE = ds("2-before_importing_photo frame (photo guide)", "617-10539")
D_EDIT = ds("1_edit_room frame (Quick Action row)", "788-1354")
D_C1 = ds("4-hair_color_case1_no_style frame", "894-1474")
D_C21 = ds("4-hair_color_case2-1_toast frame (Solid: Highlight row greyed)", "929-1901")
D_TOAST = ds("4-hair_color_case2-1 frame (toast)", "892-1796")
D_C3 = ds("4-hair_color_case3 frame (palette colour added)", "894-2637")
D_ROOM = ds("4-hair_color frame (swatch row)", "686-1427")

OPEN_ROOM = ["Launch the APP", "Tap AI Photos on the Launcher", "Tap AI Hair Color"]
PORTRAIT = OPEN_ROOM + ["Tap a portrait photo with one clear, front-facing face"]
PANEL = PORTRAIT + ["Tap Custom in the swatch row"]
PEXELS = OPEN_ROOM + ["Tap Stock", "Tap Pexels", "Search 「woman portrait」", "Tap the portrait of a woman in a knitted hat"]
GEN = PEXELS + ["Tap Custom in the swatch row", "Tap Solid in Style", "Tap the green swatch in Base Color", "Tap Generate in the panel", "Wait for the result"]

FIRST = 31
P_SOLID = pm("panel_solid_color (NEW) frame, Spec - UI (D6-04)", "3327-950")
P_INTRO = pm("Spec - Flow board, Intro Demo", "3287-93")
E_WAIT = tene("Spec - UI, sync short task D1-03 (about 15 s)", "3030-300")

# Each entry: iss, title, cls (Functional / UI / UX), sev, owner, cases, rep, note, short, steps, res, res_zh, exp, exp_zh,
# links, imgs [(png, slug, box or None)], log (title, [(label, t0, t1)]) or None, rel [lines]
E = [
 dict(iss="ISS-HCC-31", title="Intro Demo button reads 「Try now」, not the spec's 「Try Now」", cls="UI", sev=4, owner="RD",
      cases=["TC-001"], rep=(1, 1),
      note="R-002 (PM Spec - Flow, Intro Demo: 「AI Hair Color」, the description, 「Try Now」, 「Don't show again」, ‹). First time a run saw the Intro Demo (R1 / R2 never got it). Title, description, 「Don’t show again」 and ‹ match; only the button's casing differs. The spec states the text, so RD (text rule). PM-only: the Design does not draw the Intro Demo. The Launcher still has no 「AI Magic」 / 「Hair Color」 card (CMS layout, R2 O-2, not raised): the run entered from AI Photos.",
      short="Intro Demo button reads 「Try now」, not 「Try Now」",
      steps=["Launch the APP on an install that has not opened AI Hair Color yet", "Tap AI Photos on the Launcher", "Tap AI Hair Color", "Read the button of the Intro Demo"],
      res="The Intro Demo's button reads 「Try now」 (lower-case n).",
      res_zh="Intro Demo 按鈕文字為「Try now」，n 為小寫。",
      exp="The button reads 「Try Now」 as the PM spec's Intro Demo.",
      exp_zh="按鈕文字應為「Try Now」。",
      links=[P_INTRO],
      imgs=[("TC-001_entry", "intro_try_now", (40, 1960, 1040, 2140))], log=None, rel=[]),
 dict(iss="ISS-HCC-32", title="With Solid the Highlight Color row stays on screen greyed out instead of being hidden", cls="Functional", sev=3, owner="RD",
      cases=["TC-024", "TC-029"], rep=(2, 2),
      note="R-027 (PM Spec - UI panel_solid_color 3327:950, D6-04: solid_color takes one colour, only the Base Color row shows) and the user's ruling REQ-009 (2026-11-18, R2 ISS-HCC-19: 「隱藏就好」, hide the row). On the Pixel 8a, same build 90201901, the Highlight row stays with its title and 8 dimmed circles (custom_highlight_title still in the page source); switching back to Ombre re-enables it with the pink kept (TC-029 holds otherwise). R2 on the S23 hid the row on the same build, so this may be server config or device-dependent (O-1). The Design 4-hair_color_case2-1_toast 929:1901 draws the greyed row; the ruling chose hiding over it, so RD should align the app (or PM change the ruling).",
      short="Custom panel: Solid leaves the Highlight Color row greyed out instead of hiding it",
      steps=PANEL + ["Tap Ombre in Style", "Tap the dark brown swatch in Base Color", "Tap the pink swatch in Highlight Color", "Tap Solid in Style"],
      res="The 「Highlight Color」 row stays on screen greyed out (title and dimmed circles), not hidden.",
      res_zh="選 Solid 後 Highlight Color 列仍顯示（灰階停用），未隱藏。",
      exp="Only the 「Base Color」 row shows; the 「Highlight Color」 row is hidden (PM D6-04, ruling REQ-009).",
      exp_zh="選 Solid 時應只顯示 Base Color 列，Highlight Color 列隱藏。",
      links=[P_SOLID],
      imgs=[("TC-024_solid", "solid_highlight_row_greyed", (20, 1880, 1060, 2060)), ("TC-029_ombre_again", "ombre_row_enabled_again", None)],
      log=None, rel=["R2 ISS-HCC-19 (held 2026-11-18 with the ruling 「隱藏就好」, when the app hid the row)"]),
 dict(iss="ISS-HCC-33", title="PM decision: an applied Custom cell keeps its unset look instead of showing the chosen colours", cls="UX", sev=3, owner="PM",
      cases=["TC-038", "TC-041", "TC-042"], rep=(3, 3),
      note="R-044 (PM Spec - UI collapsed_applied 3330:512, D6-08: after collapsing, the Custom cell shows the two colours the user chose) against the PM mockups (a pencil icon) and the Design (only the unset cell, orange gradient with a magic wand): Q-2, open. On 90201901 the applied Custom cell is selected but keeps the unset gradient + wand after every collapse (TC-038), after picking a template (TC-041) and after the user's own overwrite (TC-042); the settings themselves are kept and reopen correctly. PHA262026P0115 (closed 2026-11-19 to this build) fixed the selection and the Custom generation; its own QA note left the cell's look to Q-2, so this is not the closed ticket back but the open question, filed to PM for a decision (2026-11-11 rule). A user cannot tell from the row what Custom holds, so [UX].",
      short="Custom cell keeps its unset look after applying, not the chosen colours — PM to decide",
      steps=PANEL + ["Tap Solid in Style", "Tap the sand swatch in Base Color", "Drag the panel's grab handle down"],
      res="The panel closes and Custom is selected, but its cell still shows the unset orange gradient with the magic wand.",
      res_zh="套用後 Custom 格仍為未設定外觀（漸層＋魔術棒），未顯示所選兩色。",
      exp="PM to decide the applied cell's look: the two chosen colours (D6-08), a pencil (PM mockup) or unchanged (Design).",
      exp_zh="請 PM 決定套用後 Custom 格的外觀（顯示兩色、鉛筆圖示或不變）。",
      links=[P_COLL],
      imgs=[("TC-042_collapsed", "custom_cell_unset_solid_sand", (10, 1700, 200, 1960)), ("TC-038_collapsed", "custom_cell_unset_ombre", (10, 1700, 200, 1960))],
      basis="Basis: External — the PM note (two colours), the PM mockups (pencil) and the Design (unset cell) disagree, Q-2; PM to decide", log=None, rel=["Q-2; PHA262026P0115 (closed 2026-11-19; its note left the cell's look to Q-2)"]),
 dict(iss="ISS-HCC-34", title="A Solid template generation takes about 35 s, not the spec's about 15 s", cls="Functional", sev=3, owner="RD",
      cases=["TC-078"], rep=(2, 2),
      note="R-048 (10/E Spec - UI 3030:300, D1-03: sync short task, about 15 s, the user waits in place). 「Soft Black」 (first template; no 「Platinum」 on this build, ISS-HCC-35) on the Pexels portrait: 34.4 s and 36.0 s from Generate to AIHairColor_Generate_Status succeed (O-3). R2 on the S23 timed the same template at 16.2 s on the same build two days earlier, so the slowdown is server-side or in the template model (Test Server; KP-070). A wait is RD (overlay rule 5); the run queued it as a question because the cause may be the test server's load.",
      short="Solid template 「Soft Black」 takes about 35 s to generate, not about 15 s",
      steps=PEXELS + ["Tap Soft Black in the Solid row", "Tap Generate", "Wait for the result"],
      res="The result shows after 34.4 s (second try 36.0 s).",
      res_zh="Soft Black 模板生成約 35 秒（34.4 / 36.0 秒），非 spec 的約 15 秒。",
      exp="A template result shows after about 15 s (10/E D1-03).",
      exp_zh="模板生成應約 15 秒完成。",
      links=[E_WAIT],
      imgs=[("TC-078_result", "soft_black_result_1", None), ("TC-078_result2", "soft_black_result_2", None)],
      log=("Soft Black template generations", [("TC-078 first", "10:54:20", "10:54:58"), ("TC-078 second (Retry)", "10:55:08", "10:55:46")]), rel=["O-3; R2 TC-078 16.2 s on the S23"]),
 dict(iss="ISS-HCC-35", title="PM decision: the first Solid template is 「Soft Black」, not the spec's 「Platinum」", cls="UI", sev=3, owner="PM",
      cases=["TC-017"], rep=(1, 1),
      note="R-016 / R-017 (the PM page and the Design 4-hair_color 686:1427 draw 「Custom」 then 「Platinum」 first, selected on entry). On the Pixel 8a the Solid row is Custom, Soft Black (selected), Cocoa (crown), Hazelnut, Silver, Espresso…; no 「Platinum」. The template list comes from the CMS, so the mockup name may be a placeholder. Re-offered: R2 ISS-HCC-27 was held on 2026-11-18 with no reason; hold again if that decision stands (then the table's TC-017 / TC-078 should name the first template, not Platinum).",
      short="Colour page: first Solid template is 「Soft Black」, no 「Platinum」 — PM to confirm",
      steps=PORTRAIT + ["Read the swatch row of the Solid tab"],
      res="The row is Custom, Soft Black (selected), Cocoa, Hazelnut, Silver, Espresso; there is no 「Platinum」.",
      res_zh="Solid 第一個模板為 Soft Black，沒有 spec 的 Platinum。",
      exp="PM to confirm the first template: 「Platinum」 (spec) or 「Soft Black」 (CMS today); the spec or the CMS then follow it.",
      exp_zh="請 PM 確認第一個模板應為 Platinum 或 Soft Black。",
      links=[D_ROOM],
      imgs=[("TC-017_room", "first_template_soft_black", None)], log=None, rel=["Q-2; R2 draft ISS-HCC-27 (held 2026-11-18, no reason)"]),
 dict(iss="ISS-HCC-36", title="PM decision: the two split-dye styles have photo thumbnails, not plain-colour ones", cls="UI", sev=3, owner="PM",
      cases=["TC-022"], rep=(1, 1),
      note="R-025 (PM page: the split-dye styles get plain-colour thumbnails, placeholders until art). 「Half-and-half」 and 「Split-dye」 show model-photo thumbnails like the other 9 styles; the 11 styles and the crowns (Balayage, Face framing, Bangs, Half-and-half) hold. Re-offered: R2 ISS-HCC-28 was held on 2026-11-18 with no reason; hold again if that decision stands (then the row should accept the photos).",
      short="Custom panel: split-dye styles show photo thumbnails, not plain-colour ones — PM to confirm",
      steps=PANEL + ["Swipe the Style row to its end"],
      res="「Half-and-half」 and 「Split-dye」 have model-photo thumbnails.",
      res_zh="兩個 split-dye style 縮圖為模特兒照片，非 spec 的純色縮圖。",
      exp="PM to confirm the thumbnails: plain-colour (spec) or the photos (app); the spec then follows it.",
      exp_zh="請 PM 確認 split-dye 縮圖應為純色或照片。",
      links=[D_C1],
      imgs=[("TC-022_end", "split_dye_thumbnails", None)], log=None, rel=["Q-6; R2 draft ISS-HCC-28 (held 2026-11-18, no reason)"]),
]

# Same-OS filed tickets this round matched (dedupe per OS, overlay rule 7): no entry, kept in dedupe.txt and report.md.
RECHECK = [  # (ticket, filed for, ECL status 2026-11-20, R3 on 90201901, rows)
 ("PHA262026P0110", "No slanted-face warning", "Propose Postpone", "still failing", "TC-005, TC-012, TC-015 (TC-006 / TC-087 / TC-007 Blocked upstream)"),
 ("PHA262026P0111", "Custom panel ⌄ / ✕ ↩ ↪ ✓ row / corners", "RDResolved", "no ⌄ (handle only)", "TC-019 Pass: grab handle only (R2 on the S23 had ⌄); Q-17 assumes the Design, so not a finding"),
 ("PHA262026P0112", "Colour rows usable before a style", "Close", "fixed as drawn", "TC-019 / TC-021: rows drawn disabled before a style, as the Design 894:1474"),
 ("PHA262026P0113", "No eyedropper in the palette", "Close", "fixed", "TC-031, TC-035"),
 ("PHA262026P0114", "Back in the palette leaves the room", "Close", "fixed", "TC-086"),
 ("PHA262026P0115", "Collapse keeps Soft Black; Generate makes a template", "Close", "fixed", "TC-038 / TC-040 / TC-041: collapse selects Custom, outer Generate is Custom; the cell's look (Q-2) is ISS-HCC-33"),
 ("PHA262026P0116", "No 「Applying your new hair color...」 text (PM)", "NewCreated", "still failing", "TC-045, TC-046, TC-040 (scan bar only)"),
 ("PHA262026P0117", "No Intensity bar on a Custom result", "Close", "fixed", "TC-047, TC-048, TC-049, TC-053"),
 ("PHA262026P0118", "No one-time My AI Artwork 100% dialog", "Assigned", "still failing", "TC-057"),
 ("PHA262026P0119", "Custom result not recalled after a template", "Close", "fixed", "TC-054"),
 ("PHA262026P0127", "Palette colour not added as a new circle", "RDResolved", "fixed", "TC-032 Pass: the picked colour is added as a ringed circle after the wheel"),
 ("PHA262026P0128", "Tapping the photo closes and applies the panel (PM)", "NewCreated", "unchanged", "TC-039 (ruling REQ-004 vs PM D6-08)"),
 ("PHA262026P0149", "Panel closes on Generate, no Intensity row (PM; TR261118-0070)", "NewCreated", "unchanged", "TC-045, TC-047 (R2 ISS-HCC-24's finding; not re-offered)"),
 ("PHA262026P0150", "Colour-wheel keys bright while rows disabled (TR261118-0070)", "Assigned", "not judged", "No R3 row checks the wheel key's brightness (TC-019 Pass on the rows)"),
]
REMAP = {"TC-005": "dedupe — PHA262026P0110 (still failing)", "TC-012": "dedupe — PHA262026P0110 (still failing)", "TC-015": "dedupe — PHA262026P0110 (still failing)",
         "TC-040": "dedupe — PHA262026P0116 (still failing); P0115 generation part fixed",
         "TC-046": "dedupe — PHA262026P0116 (still failing)", "TC-057": "dedupe — PHA262026P0118 (still failing)",
         "TC-039": "dedupe — PHA262026P0128 (filed R2, PM deciding)"}
ALSO = {}
REMAP.update({"TC-045": "dedupe — PHA262026P0116 (no text) and PHA262026P0149 (panel collapses on Generate)", "TC-047": "dedupe — PHA262026P0149 (panel collapses on Generate, PM)"})

HELD = []
OBS_NOT = [
 ("O-1", "Custom panel differs from R2 on the same build: rows disabled before a style, no ⌄, no 「Both … required.」 hint, palette pick adds a ringed circle.", "Solid's greyed row is ISS-HCC-32; the rest matches the Design / rulings (P0112, P0127 symptoms gone; Q-17; ruling: no toast or hint needed)."),
 ("O-2", "First eyedropper sample on the hair edge set a near-white colour; the second read the hair correctly.", "1 of 2 samples, on an edge pixel; R2 saw something similar. Watch next round; not raised."),
 ("O-3", "Soft Black template wait 34.4 / 36.0 s.", "ISS-HCC-34."),
 ("O-4", "After ✓, the new Edit Room's Home asks 「Discard changes?」.", "Edit Room behaviour, outside this feature."),
 ("O-5", "During a regeneration the disabled button keeps the text 「Retry」.", "Script note (waits use the log)."),
 ("O-6", "One extra Bangs generation from a script mis-step.", "Test-run slip, not the app."),
 ("O-7", "Every Custom generation logs the same Mixpanel style Style_010_Custom_HairColor_gpt-image-2.5-sunburst.", "No tracking rule in the spec for the pattern; noted for RD in report.md."),
]

KEEP = re.compile(r"GenAI_Feature_Generate|AIHairColor_Generate_Status|generate error|CONTENT_REJECTED|getMemberCreditRemain|"
                  r"Monetize_Subscription_Appear|doClairFaceDetect2 faceNum|getCreditHistory", re.I)
DROP = re.compile(r"memberToken|access_?token|authorization|bearer|signature=|purchaseToken|creditSystemUUID|uuid", re.I)


def log_lines(t0, t1):
    got, last = [], None
    for f in sorted(os.listdir(f"{RUN}/logs")):
        p = f"{RUN}/logs/{f}/logcat-live.txt"
        if not os.path.exists(p):
            continue
        for line in open(p, encoding="utf-8", errors="replace"):
            parts = line.split(" ", 2)
            if len(parts) < 3 or parts[0] != DAY or not (t0 <= parts[1][:8] <= t1):
                continue
            if not KEEP.search(line) or DROP.search(line):
                continue
            m = re.search(r"totalRemain=(\d+)", line)
            if "getMemberCreditRemain" in line:
                if not m or m.group(1) == last:
                    continue
                last = m.group(1)
                line = f"{parts[0]} {parts[1]} CreditSystem: totalRemain={last}"
            if "getCreditHistory" in line:
                continue
            line = re.sub(r"^(\S+ \S+) +\d+ +\d+ [VDIWE] ", r"\1 ", line.rstrip())
            line = re.sub(r"(https?://[^\s'\"?]+)\?\S*", r"\1?…", line)
            if line not in got:
                got.append(line[:400])
    return sorted(got), f


def excerpt(n, iss, title, secs):
    L = [f"# {iss} {title}", f"# PhotoDirector Android {V} ({B}), Google Pixel 8a / Android 16, logcat of the app captured by the casebook run",
         "# Lines about generations, failures and the credit balance (shown only when it changes); tokens and IDs dropped.", ""]
    for label, t0, t1 in secs:
        got, _ = log_lines(t0, t1)
        if not got:
            sys.exit(f"empty log window {label} {t0}-{t1}")
        L.append(f"## {label} ({DAY} {t0}–{t1})")
        L.extend(got)
        L.append("")
    txt = "\n".join(L)
    if re.search(r"eyJ[A-Za-z0-9_-]{10,}|Bearer |ya29\.|memberToken|purchaseToken", txt):
        sys.exit(f"token-like text in {iss} log")
    os.makedirs(f"{OUT}/logs", exist_ok=True)
    path = f"{OUT}/logs/{V}_hcc{n:02d}_log.txt"
    open(path, "w", encoding="utf-8").write(txt)
    return path


def jpg(src, dst, box):
    im = Image.open(src).convert("RGB")
    if box:
        d = ImageDraw.Draw(im)
        for b in (box if isinstance(box, list) else [box]):
            d.rectangle(b, outline=(255, 0, 0), width=8)
    im.thumbnail((1400, 1400))
    im.save(dst, "JPEG", quality=82)




def main():
    rows = list(csv.DictReader(open(f"{RUN}/results.csv", encoding="utf-8-sig")))
    tally = {}
    for r in rows:
        tally[r["Result"]] = tally.get(r["Result"], 0) + 1
    fails = [r["ID"] for r in rows if r["Result"] == "Fail"]
    disp = {r["ID"]: r["Disposition"] for r in rows}
    blocked = [r for r in rows if r["Result"] == "Blocked"]
    obs = re.findall(r"\*\*(O-\d+)\b", open(f"{RUN}/observations.md", encoding="utf-8").read())
    MAP = {}
    for n, e in enumerate(E, FIRST):
        for c in e["cases"]:
            MAP[c] = f"{n - FIRST + 1}. {e['iss']}"
    for k, v in REMAP.items():
        MAP.setdefault(k, v)
    for k, v in ALSO.items():
        MAP[k] = MAP[k] + " " + v
    for k, _, _ in OBS_NOT:
        MAP.setdefault(k, "not raised")
    missing = [k for k in fails + obs if k not in MAP]
    extra = [k for k in MAP if k not in fails and k not in obs]
    if missing or extra:
        sys.exit(f"reconciliation incomplete: missing {missing}, extra {extra}")
    for e in E:
        for c in e["cases"]:
            if c.startswith("TC-") and c not in fails:
                sys.exit(f"{e['iss']} cites {c}, which is not a Fail")

    img_root = f"{OUT}/{NAME}_images"
    if os.path.isdir(img_root):
        shutil.rmtree(img_root)
    os.makedirs(img_root)
    L = []
    w = L.append
    w(f"# AI Hair Color Custom (Android) — eBug drafts, round R3 (table v4), PhotoDirector {V} build {B}")
    w("")
    w(f"**Source:** spec-casebook run `library/phd/ai-hair-color-custom/android/runs/2026-11-20-r3/` — round R3 of draft `drafts/20261118-120459` (table v4, {len(rows)} cases), 2026-11-20 10:06 → 11:30 on Google Pixel 8a / Android 16 through Appium / UiAutomator2, Test Server, Free (Premium only for R3-e via the debug 「Set to subscriber」 switch, KP-131). Credits: 2000 test-card pack bought for the run (REQ-011), 2000 → 1874. Tally: " + ", ".join(f"{v} {k}" for k, v in sorted(tally.items())) + ".")
    w("")
    w("**Status:** nothing filed, uploaded or commented. Build 20.19.0 / versionCode 90201901, the build the user confirmed for TR261111-0042 on 2026-11-18 (R2 batch). ECL product 「PhotoDirector Mobile for Android」. Creator WILLY_WU, TR261111-0042, [AIAgent], API prefilled from the R2 batch (filed 2026-11-18) — confirm.")
    w("")
    w("Rules: reviewer rules 2026-10-21 — one action per Repro step, a Spec Link on every entry (URL on its own line), at least one image per entry, the logcat excerpt on the generation entry, no video. UX findings and PM decisions are `[AIAgent][UX]`, BugBelong PM; text is `[AIAgent][UI]` (RD when the Design / PM states it); the rest `[AIAgent]` Functional, RD. Spec basis check (REQ-055) per entry against today's Design page 616:9324 and PM page 3287:89; QA rules (rule pass 8, system Back) named as such.")
    w("")
    w(f"**What is drafted:** {len(E)} new entries (ISS-HCC-31…{FIRST - 1 + len(E)}), of which {sum(1 for e in E if e['owner'] == 'PM')} ask PM for a decision. Findings that repeat a filed Android ticket (PHA262026P0110, P0116, P0118, P0128, P0149) get no entry (dedupe per OS, overlay rule 7); they and the other rechecks are in `dedupe.txt` and the run's report.md, for information only (no comment). Entries 5 and 6 re-offer R2 drafts held without a reason (ISS-HCC-27, -28); R2's ISS-HCC-24 (panel collapses on Generate) is now PHA262026P0149 and gets no entry; R2 drafts held with a ruling (REQ-009) are not re-offered.")
    w("")
    w("Legend — Class: Functional / UI / UX · Severity: S1 critical and blocking only, S2 important, S3 moderate, S4 minor · Owner: RD / PM.")
    w("")
    for n, e in enumerate(E, FIRST):
        folder = f"{n - FIRST + 1:02d}_{e['iss']}"
        os.makedirs(f"{img_root}/{folder}")
        names = []
        for png, slug, box in e["imgs"]:
            src = f"{RUN}/screenshots/{png}.png"
            if not os.path.exists(src):
                sys.exit(f"missing screenshot {src}")
            name = f"{V}_hcc{n:02d}_{slug}.jpg"
            jpg(src, f"{img_root}/{folder}/{name}", box)
            names.append(name)
        if e.get("log"):
            title, secs = e["log"]
            p = excerpt(n, e["iss"], title, secs)
            shutil.copy(p, f"{img_root}/{folder}/")
            names.append(os.path.basename(p))
        tag = "[AIAgent]" + ("" if e["cls"] == "Functional" else f"[{e['cls']}]")
        short = f"{PROD} {V} - {tag} {FEAT}: {e['short']}"
        if len(short) > 140:
            sys.exit(f"{e['iss']} short description {len(short)} > 140")
        e["_short"] = short
        w("---"); w("")
        w(f"## {n - FIRST + 1}. {e['iss']} — {e['title']}  ·  Class: {e['cls']}  ·  Severity: S{e['sev']}  ·  Owner: {e['owner']}")
        w("")
        w(f"**Report step:** {', '.join(e['cases'])}  ·  **Reproduce:** {e['rep'][0]}/{e['rep'][1]}  ·  **Verified on:** {V}.{B}")
        w("")
        w(f"> **QA note — not pasted into eBug.** {e['note']}")
        w("")
        w("**Short Description:**"); w(""); w("```"); w(short); w("```"); w("")
        w("**Description:**"); w(""); w("```"); w("Repro Steps:")
        for i, s in enumerate(e["steps"], 1):
            w(f"{i}. {s}")
        w(f"{len(e['steps']) + 1}. Check the result")
        w(""); w("Result:"); w(e["res"]); w(f"摘要：{e['res_zh']}"); w(" ".join("{" + x + "}" for x in names))
        w(""); w("Expect Result:"); w(e["exp"]); w(f"摘要：{e['exp_zh']}")
        w(""); w("Note:"); w(DEVICE)
        for l in e["links"]:
            w(l)
        if e.get("basis"):
            w(e["basis"])
        for r in e.get("rel", []):
            w(f"Related: {r}")
        w("<Claude Reviewed>"); w("```"); w("")
        w(f"**Images:** `{NAME}_images/{folder}/`"); w("")

    w("---"); w("")
    w("# Not raised (observations, for the record)")
    w("")
    w("| Item | What was seen | Why not raised |")
    w("|---|---|---|")
    for k, a, b in OBS_NOT:
        w(f"| {k} | {a} | {b} |")
    bd = {}
    for r in blocked:
        bd[r["Disposition"]] = bd.get(r["Disposition"], 0) + 1
    w(f"| Blocked ({len(blocked)}) | " + ", ".join(f"{v} {k}" for k, v in sorted(bd.items())) + " | No verdict; reasons in report.md. TC-006 / TC-087 / TC-007 are blocked upstream of TC-005 (filed PHA262026P0110). |")
    w("")
    w("# Reconciliation against the run")
    w("")
    nq = sum(1 for f in fails if disp[f] == "question")
    w(f"{len(fails)} Fail ({len(fails) - nq} defect, {nq} question), {len(blocked)} Blocked, {tally.get('Not run', 0)} Not run, {len(obs)} observations (O-1 … O-{len(obs)}).")
    w("")
    w("| Item | Result | Disposition | Became |")
    w("|---|---|---|---|")
    for k in fails:
        w(f"| {k} | Fail | {disp[k]} | {MAP[k]} |")
    for k in obs:
        w(f"| {k} | observation | — | {MAP[k]} |")
    w("")
    w("Filing order by severity: " + ", ".join(f"**{i - FIRST + 1}**" for s in (1, 2, 3, 4) for i, e in enumerate(E, FIRST) if e["sev"] == s) + ". Nothing is filed until the review page's decisions come back.")
    w("")
    open(f"{OUT}/{NAME}.md", "w", encoding="utf-8").write("\n".join(L))
    json.dump({e["iss"]: {"cases": e["cases"], "why": e["title"]} for e in E}, open(f"{OUT}/entries.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"wrote {len(E)} entries → {OUT}/{NAME}.md")


if __name__ == "__main__":
    main()
