#!/usr/bin/env python3
"""Build the AI Hair Color Custom Android eBug draft batch for round R2 (table v3, draft 20261117-151025) on 20.19.0 (90201901).

Writes ../20261118_eBug_drafts_AI-Hair-Color-Custom-R2_20.19.0.md, the sibling _images/ folder (one NN_ISS-ID folder per
entry: JPEGs named 20.19.0_hccNN_<slug>.jpg with a red box where it helps, plus the logcat excerpt where the finding has
a log cause) and logs/. Nothing is filed. Every Fail row of results.csv and every observation O-n is mapped (entry /
recheck of a filed ticket / not raised); the script stops when one is missing. Entry numbers continue R1's
(ISS-HCC-16 onward). Built from the R1 generator (../../2026-11-13-r1/generators/ebugs.py).
Run: python library/phd/ai-hair-color-custom/android/ebugs/2026-11-18-r2/generators/ebugs.py
"""
import csv, json, os, re, shutil, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(OUT, "..", ".."))           # library/phd/ai-hair-color-custom/android
RUN = f"{ROOT}/runs/2026-11-17-r2"
NAME = "20261118_eBug_drafts_AI-Hair-Color-Custom-R2_20.19.0"
V, B = "20.19.0", "90201901"
DAY = "2026-11-18"
PROD = "PHD-A"
FEAT = "AI_Hair_Color"
DEVICE = "Device: Samsung Galaxy S23 (SM-S9110) / Android 16"
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

OPEN_ROOM = ["Launch the APP", "Tap AI Photos on the Launcher", "Tap AI Hair Color", "Tap Continue on the photo tips sheet"]
PORTRAIT = OPEN_ROOM + ["Tap a portrait photo with one clear, front-facing face"]
PANEL = PORTRAIT + ["Tap Custom in the swatch row"]
PEXELS = OPEN_ROOM + ["Tap Stock", "Search 「woman portrait」 in Pexels", "Tap the portrait of a woman in a knitted hat"]
GEN = PEXELS + ["Tap Custom in the swatch row", "Tap Solid in Style", "Tap the green swatch in Base Color", "Tap Generate in the panel", "Wait for the result"]

# Each entry: iss, title, cls (Functional / UI / UX), sev, owner, cases, rep, note, short, steps, res, res_zh, exp, exp_zh,
# links, imgs [(png, slug, box or None)], log (title, [(label, t0, t1)]) or None, rel [lines]
E = [
 dict(iss="ISS-HCC-16", title="Photo guide and picker labels differ from the Design", cls="UI", sev=3, owner="RD",
      cases=["TC-092"], rep=(1, 1),
      note="R-088 (Design 2-before_importing_photo 617:10539 draws 「Recommend」, 「Face too small」, two Avoid items and 「Don't show again.」; the picker tabs 「Photo」 / 「Stock」). The app shows 「Recommendation」, 「Face Too Small」, a third Avoid item 「Accessories」 (woman in a wide hat), 「Don’t show again」 without the period, and the picker tabs 「Camera ⌄」 / 「Stock」. The Design states the text and the app differs, so RD (text rule). The 「Accessories」 item may answer Q-20 (10/E D2-02 asks to avoid hats): the Note names it so RD / PM can keep it if intended. The guide's content is fetched from the server (O-4), so the fix may be server data.",
      short="Photo guide reads 「Recommendation」, 「Face Too Small」, adds 「Accessories」 vs the Design",
      steps=OPEN_ROOM[:3] + ["Read the photo guide shown over the picker", "Tap Continue", "Read the picker's tabs"],
      res="The guide reads 「Recommendation」 and 「Face Too Small」, adds 「Accessories」; picker tabs are 「Camera」 / 「Stock」.",
      res_zh="照片指引標題與項目文字和 Design 不同，多一個 Accessories，相簿分頁為 Camera / Stock。",
      exp="As the Design: 「Recommend」, 「Face too small」 (two Avoid items), 「Don't show again.」, tabs 「Photo」 / 「Stock」.",
      exp_zh="應與 Design 文字一致（Recommend、Face too small、Photo / Stock）。",
      links=[D_GUIDE],
      imgs=[("TC-092_guide", "guide_text", [(60, 865, 440, 925), (80, 1815, 1000, 1880), (370, 2050, 720, 2115)]),
            ("TC-092_picker", "picker_tabs", None)],
      log=None, rel=["Q-20 (is a hat item expected under Avoid?) is open on the casebook side"]),
 dict(iss="ISS-HCC-17", title="No-face dialog reads 「A face is required」, not the spec's 「Face is required」", cls="UI", sev=4, owner="RD",
      cases=["TC-009"], rep=(1, 1),
      note="R-010 (11/25 進房檢查 board quotes the 10/E string 「No face detected. Face is required for this feature.」). Re-offered: the same finding was drafted in R1 as ISS-HCC-02 and held by the user on 2026-11-13 with no reason; it still reproduces on 90201901. Owner RD (the spec states the text; the 2026-11-11 rule: never Doc). Hold again if the R1 decision stands.",
      short="No-face dialog reads 「A face is required」, not 「Face is required」",
      steps=OPEN_ROOM + ["Tap a photo with no face (a teacup)"],
      res="The dialog body reads 「No face detected. A face is required for this feature.」",
      res_zh="無臉提示文字多了「A」。",
      exp="The body reads 「No face detected. Face is required for this feature.」",
      exp_zh="文字應為「No face detected. Face is required for this feature.」",
      links=[FACEB],
      imgs=[("TC-009_dialog", "no_face_copy", None)], log=None, rel=["R1 draft ISS-HCC-02 (held 2026-11-13)"]),
 dict(iss="ISS-HCC-18", title="Edit Room's Quick Action row has no 「Hair Color」 tool", cls="Functional", sev=3, owner="RD",
      cases=["TC-015"], rep=(1, 1),
      note="R-089 (Design 1_edit_room 788:1354 draws 「Hair Color」 in the Quick Action row after 「Hairstyle」; tapping it opens AI Hair Color with the photo being edited). The row walked end to end on 90201901: AI Edit Agent, AI Removal, Crop, Text, Cutout, Background, Mosaic, AI Expand, AI Replace, Add Photo, Sticker, InstaFill, Brush, Move, Clone, Frame, AI Scene; no Hair Color. The tool is reachable only under Portrait › Hair › AI Hair Color (O-6). TC-015's missing slanted-face warning is PHA262026P0110 (recheck, not this entry).",
      short="Edit Room Quick Action row has no 「Hair Color」 tool",
      steps=OPEN_ROOM + ["Tap a portrait photo", "Tap ✕ at the bottom left", "Tap Discard", "Swipe the Quick Action row to its end"],
      res="The Quick Action row has no 「Hair Color」; the tool is only under Portrait, then Hair.",
      res_zh="Edit Room 的 Quick Action 列沒有 Hair Color。",
      exp="「Hair Color」 sits in the Quick Action row after 「Hairstyle」 and opens AI Hair Color with the photo.",
      exp_zh="Quick Action 列應有 Hair Color（在 Hairstyle 之後）。",
      links=[D_EDIT],
      imgs=[("TC-015_quick", "quick_action_start", None), ("TC-015_quick_end", "quick_action_end", None)], log=None, rel=[]),
 dict(iss="ISS-HCC-19", title="PM decision: with Solid the Highlight row disappears (PM) or stays greyed (Design)?", cls="UX", sev=3, owner="PM",
      cases=["TC-024", "TC-029"], rep=(2, 2),
      note="Q-18, filed to PM for a decision (2026-11-11 rule). Design 4-hair_color_case2-1_toast 929:1901 keeps the 「Highlight Color」 row on screen greyed out for Solid; the PM page D6-04 (panel_two_tone) says it does not appear. 90201901 removes the row (title and swatches gone, the Base row moves down); switching back to a two-colour style brings it back with the colour kept (TC-029). The casebook assumed the Design (Design-first rule) but cannot tell which source is newer.",
      short="Custom panel: Solid hides the Highlight Color row; Design greys it, PM hides it — which?",
      steps=PANEL + ["Tap Solid in Style"],
      res="The 「Highlight Color」 row disappears; only 「Base Color」 stays.",
      res_zh="選 Solid 後 Highlight Color 列整列消失（Design 為灰階停用，PM 為不顯示）。",
      exp="PM to decide: keep the row greyed out (Design 929:1901) or hide it (PM D6-04), and align the other source.",
      exp_zh="請 PM 決定 Solid 時 Highlight 列應隱藏或灰階停用。",
      links=[D_C21, P_TWO],
      imgs=[("TC-024_solid", "solid_no_highlight_row", (0, 1780, 1080, 2000)), ("TC-029_ombre", "ombre_row_back", None)],
      log=None, rel=["Q-18"]),
 dict(iss="ISS-HCC-20", title="PM decision: two-colour style with Base only keeps Generate disabled (ruling REQ-003 says it must generate)", cls="UX", sev=2, owner="PM",
      cases=["TC-026"], rep=(1, 1),
      note="The user's rulings REQ-003 (2026-11-13) and REQ-007 (2026-11-17, Q-19: 「只選Base應該也要可以生成」) say Base Color alone must enable Generate for a two-colour style. The PM page D6-04 (both colours required) and the Design cases 2 / 2-1 (Generate grey, toast) say the opposite, and 90201901 now follows them: Generate stays grey and 「Both Base Color and Highlight Color are required.」 shows under the rows (R1's 90201900 enabled Generate here; ISS-HCC-05 was held for that). Filed to PM so the spec and the app follow one rule. O-9: the grey line also shows when both colours are chosen.",
      short="Custom panel: two-colour style with only Base Color keeps Generate disabled — PM to decide",
      steps=PANEL + ["Tap Ombre in Style", "Tap the dark brown swatch in Base Color"],
      res="Generate stays grey (disabled) and 「Both Base Color and Highlight Color are required.」 shows.",
      res_zh="只選 Base Color 時 Generate 不可按，與「只選 Base 也要能生成」的裁示不同。",
      exp="PM to decide: Base alone generates (ruling) or both colours are required (D6-04, Design case 2).",
      exp_zh="請 PM 決定只選 Base 是否可生成，並統一 spec 與 app。",
      links=[P_TWO, D_TOAST],
      imgs=[("TC-026_base_only_crop", "base_only_generate_disabled", None)], log=None, rel=["REQ-003 / REQ-007 (casebook rulings), Q-19; R1 draft ISS-HCC-05 (held)"]),
 dict(iss="ISS-HCC-21", title="Highlight-only Generate shows no 「Select both a base and highlight color.」 toast", cls="Functional", sev=3, owner="RD",
      cases=["TC-027"], rep=(2, 2),
      note="R-029 / R-085 (Design 4-hair_color_case2-1 892:1796 draws the toast 「Select both a base and highlight color.」 over the photo when Generate is tapped without a Base Color; answers Q-16). Balayage with only a Highlight colour: Generate grey, two taps (one recorded at 2 fps): no toast, only the static grey line 「Both Base Color and Highlight Color are required.」 under the rows. No generation, no charge.",
      short="Custom panel: tapping grey Generate with Highlight only shows no 「Select both…」 toast",
      steps=PANEL + ["Tap Balayage in Style", "Tap the sand swatch in Highlight Color", "Tap Generate"],
      res="Nothing happens: no toast shows over the photo.",
      res_zh="只選 Highlight 時點 Generate 沒有任何 toast。",
      exp="The toast 「Select both a base and highlight color.」 shows over the photo; nothing is generated.",
      exp_zh="應顯示 toast「Select both a base and highlight color.」。",
      links=[D_TOAST],
      imgs=[("TC-027_hl_only_small", "highlight_only", None), ("TC-027_after_generate_small", "no_toast", None)], log=None, rel=["Q-16"]),
 dict(iss="ISS-HCC-22", title="A palette colour is not added to the row as a new circle", cls="Functional", sev=3, owner="RD",
      cases=["TC-032"], rep=(1, 1),
      note="R-034 / R-035 / R-086 (Design 4-hair_color_case3 894:2637: after 「Done」 the picked colour becomes a new circle right after the colour wheel, ringed, the recommended colours shift one place right). On 90201901 the wheel key itself takes the selection ring and stays a rainbow; no new circle, the 8 recommended colours do not move, and the picked colour is shown nowhere (O-10). The colour is kept as the row's value (the palette reopens at it) and generates correctly (R2-e). R1's 90201900 did add the circle.",
      short="Custom palette: colour picked with Done is not added to the row as a new circle",
      steps=PANEL + ["Tap Ombre in Style", "Tap the colour wheel in Base Color", "Drag the hue slider to blue", "Drag the cursor to the square's top right", "Tap Done"],
      res="The colour wheel gets the selection ring; no new circle with the blue appears and the recommended colours do not move.",
      res_zh="調色盤選色後沒有新增色圈，選中的是色輪本身，看不到所選顏色。",
      exp="The blue is added as a new ringed circle right after the colour wheel; the other colours move one place right.",
      exp_zh="所選顏色應新增為色輪右側的色圈並被選中。",
      links=[D_C3],
      imgs=[("TC-032_picked_crop", "palette_blue", None), ("TC-032_done", "no_new_circle", None)], log=None, rel=[]),
 dict(iss="ISS-HCC-23", title="PM decision: tapping the photo above the panel closes it and applies (ruling REQ-004 says it stays open)", cls="UX", sev=3, owner="PM",
      cases=["TC-039"], rep=(1, 1),
      note="The user's ruling REQ-004 (2026-11-13): tapping the photo above the Custom panel must not close it; nothing applied or cancelled. The PM page D6-08 (collapsed_applied) says tap outside = apply, and 90201901 now does that (R1's 90201900 kept the panel open; ISS-HCC-09 was held for that). Filed to PM so the spec and the app follow one rule. PM-only: the Design does not draw it.",
      short="Custom panel: tapping the photo closes the panel and applies — PM to decide",
      steps=PANEL + ["Tap Balayage in Style", "Tap the dark brown swatch in Base Color", "Tap the sand swatch in Highlight Color", "Tap the photo above the panel"],
      res="The panel closes and Custom is applied (swatch row back, Custom selected).",
      res_zh="點面板上方照片時面板收合並套用；與 2026-11-13 的裁示（不應關閉）不同。",
      exp="PM to decide: the panel stays open, nothing applied (ruling), or tap outside applies (D6-08).",
      exp_zh="請 PM 決定點照片時面板是否收合套用。",
      links=[P_COLL],
      imgs=[("TC-039_before_small", "before_photo_tap", None), ("TC-039_after_tap_small", "after_photo_tap", None)], log=None, rel=["REQ-004 (casebook ruling); R1 draft ISS-HCC-09 (held)"]),
 dict(iss="ISS-HCC-24", title="Generate in the panel collapses the panel instead of keeping it open", cls="Functional", sev=3, owner="RD",
      cases=["TC-045", "TC-047"], rep=(13, 13),
      note="R-041 (Spec - Flow, in-panel Generate D6-22 / D6-23: the panel stays open, the swatch row and Generate are disabled during the wait, then the result fills the photo, a 44 pt Intensity row appears above the panel's button, which reads 「Retry」). On 90201901 every in-panel Generate of R2-d / R2-e (13) collapsed the panel at once to the Solid / Multicolor template row with Custom selected; the result and Intensity show there (O-15). R1's 90201900 kept the panel open. The missing 「Applying your new hair color...」 in the same wait is PHA262026P0116 (recheck, not this entry).",
      short="Custom panel collapses as soon as Generate is tapped in it; it should stay open",
      steps=GEN[:-2] + ["Tap Generate in the panel"],
      res="The panel closes at once to the template row with Custom selected; the result shows there.",
      res_zh="在面板內按 Generate 後面板立即收合。",
      exp="The panel stays open and disabled while waiting; the result shows above it with Intensity and 「Retry」.",
      exp_zh="面板應保持展開，結果與 Intensity 顯示於上方，按鈕變 Retry。",
      links=[P_FLOW, P_RES],
      imgs=[("TC-045_before", "panel_before_generate", None), ("TC-045_wait1", "collapsed_on_generate", None), ("TC-047_result", "result_panel_closed", None)],
      log=("in-panel Custom generation (panel collapses at the tap)", [("TC-045", "09:55:30", "09:56:18")]), rel=[]),
 dict(iss="ISS-HCC-25", title="✕ and system Back on a result ask 「Discard changes?」 and land in the Edit Room", cls="Functional", sev=3, owner="RD",
      cases=["TC-079", "TC-088"], rep=(2, 2),
      note="R-068 (10/E D1-20b: ✕ gives up this edit and returns to the screen before entry with no second confirmation); R-076 is a QA rule (rule pass 8: system Back does what ✕ does). Entered from Launcher › AI Photos: ✕ and Back on a Custom result show 「Discard changes?」 / 「All your existing changes will be lost.」 / Keep / Discard; Discard lands in the Edit Room with the original photo, not the Launcher. The result is in My AI Artwork (holds). Re-offered: drafted in R1 as ISS-HCC-14 and held by the user on 2026-11-13 with no reason; still reproduces on 90201901.",
      short="✕ on a result asks 「Discard changes?」, then opens Edit Room, not the Launcher",
      steps=GEN + ["Tap ✕ at the bottom left", "Tap Discard"],
      res="「Discard changes?」 shows; Discard opens the Edit Room with the photo instead of the Launcher.",
      res_zh="按 ✕ 會跳「Discard changes?」確認，之後進入 Edit Room 而非回到 Launcher。",
      exp="✕ returns straight to the screen before entry (the Launcher) with no confirmation.",
      exp_zh="✕ 應不經確認直接回到進入前的畫面（Launcher）。",
      links=[E_X],
      imgs=[("TC-079_after", "x_discard_dialog", None), ("TC-079_discard", "discard_lands_edit_room", None), ("TC-088_after", "back_discard_dialog", None)],
      log=None, rel=["R1 draft ISS-HCC-14 (held 2026-11-13)"]),
 dict(iss="ISS-HCC-26", title="Subscriber without credits sees 「Get Credit Refilled!」 / 「GET CREDITS」, not 「More Credits Required!」 / 「Get Credit」", cls="UI", sev=3, owner="RD",
      cases=["TC-071"], rep=(1, 1),
      note="R-063 (10/E Credit not enough card 3031:293: subscriber → 「More Credits Required!」 → 「Get Credit」 → Credit Shop). VIP via the debug 「Set to subscriber」 switch (KP-131; Mine 「Hello VIP!」), 0 credits, Custom Ombre: the dialog reads 「Get Credit Refilled!」 / 「You don't have enough credits for this feature. Don’t worry, you have 50% off credit pricing.」 / 「GET CREDITS」. The button does open the Credit Shop (holds). The dialog may be the app's shared credit dialog; if so PM may update the card instead. Nothing bought (O-12: the shop issued the VIP daily 3 credits).",
      short="Subscriber out of credits sees 「Get Credit Refilled!」, not 「More Credits Required!」",
      steps=PANEL + ["Tap Ombre in Style", "Tap the brown swatch in Base Color", "Tap the sand swatch in Highlight Color", "Tap Generate"],
      res="A dialog 「Get Credit Refilled!」 with the button 「GET CREDITS」 shows.",
      res_zh="訂閱者點數不足時對話框標題為 Get Credit Refilled!、按鈕 GET CREDITS。",
      exp="「More Credits Required!」 with 「Get Credit」, which opens the Credit Shop.",
      exp_zh="應顯示「More Credits Required!」與「Get Credit」。",
      links=[E_CREDIT],
      imgs=[("TC-071_dialog.png", "credit_dialog_text", (130, 1240, 950, 1590))], log=None, rel=[]),
 dict(iss="ISS-HCC-27", title="PM decision: the first Solid template is 「Soft Black」, not the spec's 「Platinum」", cls="UI", sev=3, owner="PM",
      cases=["TC-017"], rep=(1, 1),
      note="R-016 / R-017 (the PM page and the Design 4-hair_color 686:1427 draw 「Custom」 then 「Platinum」 first, selected on entry). On 90201901 the Solid row is Custom, Soft Black (selected), Cocoa (crown), Hazelnut, Silver, Espresso…; no 「Platinum」 anywhere in the row. The template list comes from the CMS, so the mockup name may be a placeholder: filed to PM to confirm which first template ships (Q-2 covers the Custom cell's look, which now matches the Design).",
      short="Colour page: first Solid template is 「Soft Black」, no 「Platinum」 — PM to confirm",
      steps=PORTRAIT + ["Read the swatch row of the Solid tab"],
      res="The row is Custom, Soft Black (selected), Cocoa, Hazelnut, Silver, Espresso; there is no 「Platinum」.",
      res_zh="Solid 第一個模板為 Soft Black，沒有 spec 的 Platinum。",
      exp="PM to confirm the first template: 「Platinum」 (spec) or 「Soft Black」 (CMS today); the spec or the CMS then follow it.",
      exp_zh="請 PM 確認第一個模板應為 Platinum 或 Soft Black。",
      links=[D_ROOM],
      imgs=[("TC-017_room", "first_template_soft_black", (10, 1660, 1080, 1920))], log=None, rel=["Q-2"]),
 dict(iss="ISS-HCC-28", title="PM decision: the two split-dye styles have photo thumbnails, not plain-colour ones", cls="UI", sev=3, owner="PM",
      cases=["TC-022"], rep=(1, 1),
      note="R-025 (PM page: the split-dye styles get plain-colour thumbnails, placeholders until art). 「Half-and-half」 and 「Split-dye」 show model-photo thumbnails like the other 9 styles. R1 read the photos as finished art (R1 O-6, not raised); filed now to PM to confirm, as the row still names plain colour. The style list (11) and the crowns (Balayage, Face framing, Bangs, Half-and-half) hold.",
      short="Custom panel: split-dye styles show photo thumbnails, not plain-colour ones — PM to confirm",
      steps=PANEL + ["Swipe the Style row to its end"],
      res="「Half-and-half」 and 「Split-dye」 have model-photo thumbnails.",
      res_zh="兩個 split-dye style 縮圖為模特兒照片，非 spec 的純色縮圖。",
      exp="PM to confirm the thumbnails: plain-colour (spec) or the photos (app); the spec then follows it.",
      exp_zh="請 PM 確認 split-dye 縮圖應為純色或照片。",
      links=[D_C1],
      imgs=[("TC-022_style_end", "split_dye_thumbnails", None)], log=None, rel=["Q-6"]),
]

# Filed tickets rechecked by this round (Android, TR261111-0042). Listed for information only: never commented on,
# reopened or rejected (AGENTS.md, No comments on existing eBugs).
RECHECK = [
 ("PHA262026P0110", "No slanted-face warning", "still failing", "TC-005, TC-012, TC-015 (tilted 30° / 45°, after Crop, from Edit Room › Portrait › Hair: no warning; faceNum 1)"),
 ("PHA262026P0111", "Custom panel ︽ / ✕ ↩ ↪ ✓ row / corners", "fixed", "TC-019: ⌄ + grab handle, ✕ ↺ ↻ ✓ row hidden"),
 ("PHA262026P0112", "Colour rows usable before a style", "symptom gone", "TC-019 / TC-021: no colour can be picked before a style, but the rows are hidden rather than drawn disabled as the Design 894:1474 does (informational; the fix is not rejected)"),
 ("PHA262026P0113", "No eyedropper in the palette", "fixed", "TC-031, TC-035"),
 ("PHA262026P0114", "Back in the palette leaves the room", "fixed", "TC-086 (Back closes only the palette)"),
 ("PHA262026P0115", "Collapse keeps Soft Black; Generate makes a template", "partly fixed", "TC-040: collapse keeps Custom and the outer Generate is a Custom generation; TC-038 / TC-041 / TC-042: the Custom cell still never shows the chosen colours"),
 ("PHA262026P0116", "No 「Applying your new hair color...」 text", "still failing", "TC-045, TC-046, TC-040 (scan bar only, 44–47 s)"),
 ("PHA262026P0117", "No Intensity bar on a Custom result", "fixed", "TC-047, TC-048, TC-049, TC-053"),
 ("PHA262026P0118", "No one-time My AI Artwork 100% dialog", "still failing", "TC-057"),
 ("PHA262026P0119", "Custom result not recalled after a template", "fixed", "TC-054"),
]
REMAP = {"TC-005": "recheck — PHA262026P0110 (still failing)", "TC-012": "recheck — PHA262026P0110 (still failing)",
         "TC-019": "recheck — PHA262026P0112 (rows hidden, not disabled) / P0111 fixed", "TC-021": "recheck — PHA262026P0112 (rows hidden, not disabled)",
         "TC-038": "recheck — PHA262026P0115 (cell colours still missing)", "TC-041": "recheck — PHA262026P0115 (cell colours still missing)",
         "TC-042": "recheck — PHA262026P0115 (cell colours still missing)", "TC-040": "recheck — PHA262026P0116 (still failing); P0115 template part fixed",
         "TC-046": "recheck — PHA262026P0116 (still failing)", "TC-057": "recheck — PHA262026P0118 (still failing)"}
ALSO = {"TC-015": "and recheck PHA262026P0110 (slant)", "TC-045": "and recheck PHA262026P0116 (no text)"}

HELD = []
OBS_NOT = [
 ("O-1", "No Intro Demo on this install.", "Test data (app data may not be cleared); TC-001 group Blocked."),
 ("O-2", "No 「AI Magic」 section / 「Hair Color」 card on the Launcher.", "Recorded on TC-001 (Blocked); Launcher layout is CMS."),
 ("O-3", "Credits 0 after the 2026-11-17 reinstall.", "KP-133; account state, not the feature."),
 ("O-4", "The photo guide's content comes from the server.", "Context for ISS-HCC-16."),
 ("O-5", "With 0 credits Generate offers 「1 Free Trial」.", "Free-trial offer, as designed (KP-016)."),
 ("O-6", "AI Hair Color sits under Portrait › Hair.", "Part of ISS-HCC-18."),
 ("O-7", "hc_wide16x9 shows the face-too-small dialog first.", "Fixture note."),
 ("O-8", "Free user on a crowned style sees a 「VIP FREE TRIAL」 banner.", "No row or spec item; paywall works (TC-069 Pass)."),
 ("O-9", "「Both Base Color and Highlight Color are required.」 shows at all times for two-colour styles.", "Folded into ISS-HCC-20."),
 ("O-10", "A palette colour is kept but shown nowhere.", "Part of ISS-HCC-22."),
 ("O-11", "Custom panel changes since R1.", "Summary; covered by the rechecks and entries."),
 ("O-12", "VIP daily bonus 3 credits issued by the shop.", "Account bonus, not this feature."),
 ("O-13", "Reel Creator charges on the same balance.", "Other use of the install."),
 ("O-14", "The photo guide shows again after the reinstall.", "Expected after a reinstall."),
 ("O-15", "The panel collapses on Generate.", "ISS-HCC-24."),
 ("O-16", "Style names differ from the CMS keys; Bangs ≈ Face framing on a no-fringe photo.", "Names come from the CMS (Q-13); every style generated its pattern (R2-e Pass)."),
 ("O-17", "One extra Face framing generation by the agent's helper.", "Test-run slip, not the app."),
 ("O-18", "VIP pays 6 credits per Custom image although Premium advertises 50% off credit pricing.", "The table expects 6 (R-040); the 50% applies to credit-pack prices in the shop (TC-071). Note for PM only."),
 ("O-19", "A Custom generation starts from the original photo.", "As expected."),
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
    L = [f"# {iss} {title}", f"# PhotoDirector Android {V} ({B}), Samsung SM-S9110 / Android 16, logcat of the app captured by the casebook run",
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
    obs = re.findall(r"\*\*(O-\d+)\*\*", open(f"{RUN}/observations.md", encoding="utf-8").read())
    MAP = {}
    for n, e in enumerate(E, 16):
        for c in e["cases"]:
            MAP[c] = f"{n - 15}. {e['iss']}"
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
    w(f"# AI Hair Color Custom (Android) — eBug drafts, round R2 (table v3), PhotoDirector {V} build {B}")
    w("")
    w(f"**Source:** spec-casebook run `library/phd/ai-hair-color-custom/android/runs/2026-11-17-r2/` — round R2 of draft `drafts/20261117-151025` (table v3, {len(rows)} cases), 2026-11-17 16:50 → 2026-11-18 10:35 on Samsung Galaxy S23 (SM-S9110) / Android 16 through Appium / UiAutomator2, Test Server, Free (Premium only for R2-e and TC-071 via the debug 「Set to subscriber」 switch). Tally: " + ", ".join(f"{v} {k}" for k, v in sorted(tally.items())) + ".")
    w("")
    w("**Status:** nothing filed, uploaded or commented. Build 20.19.0 / versionCode 90201901 (R1 and the TR261111-0042 batch were 90201900): filing needs the TR whose header names 90201901, or the user's word that TR261111-0042 covers it. ECL product 「PhotoDirector Mobile for Android」. Creator WILLY_WU, [AIAgent], API prefilled from the R1 batch (filed 2026-11-13).")
    w("")
    w("Rules: reviewer rules 2026-10-21 — one action per Repro step, a Spec Link on every entry (URL on its own line), at least one image per entry, the logcat excerpt on the generation entry, no video. UX findings and PM decisions are `[AIAgent][UX]`, BugBelong PM; text is `[AIAgent][UI]` (RD when the Design / PM states it); the rest `[AIAgent]` Functional, RD. Spec basis check (REQ-055) per entry against today's Design page 616:9324 and PM page 3287:89; QA rules (rule pass 8, system Back) named as such.")
    w("")
    w(f"**What is drafted:** {len(E)} new entries (ISS-HCC-16…{15 + len(E)}), of which {sum(1 for e in E if e['owner'] == 'PM')} ask PM for a decision. Filed tickets PHA262026P0110–P0119 are rechecked below for information only (dedupe per OS: a still-failing filed ticket gets no new card and no comment).")
    w("")
    w("Legend — Class: Functional / UI / UX · Severity: S1 critical and blocking only, S2 important, S3 moderate, S4 minor · Owner: RD / PM.")
    w("")
    for n, e in enumerate(E, 16):
        folder = f"{n - 15:02d}_{e['iss']}"
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
        w(f"## {n - 15}. {e['iss']} — {e['title']}  ·  Class: {e['cls']}  ·  Severity: S{e['sev']}  ·  Owner: {e['owner']}")
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
        for r in e.get("rel", []):
            w(f"Related: {r}")
        w("<Claude Reviewed>"); w("```"); w("")
        w(f"**Images:** `{NAME}_images/{folder}/`"); w("")

    w("---"); w("")
    w("# Rechecks of filed tickets (information only — no comment, reopen or reject)")
    w("")
    w("| Ticket | Filed for | On 90201901 | Rows |")
    w("|---|---|---|---|")
    for k, a, s, r in RECHECK:
        w(f"| {k} | {a} | {s} | {r} |")
    w("")
    w("# Not raised (observations, for the record)")
    w("")
    w("| Item | What was seen | Why not raised |")
    w("|---|---|---|")
    for k, a, b in OBS_NOT:
        w(f"| {k} | {a} | {b} |")
    bd = {}
    for r in blocked:
        bd[r["Disposition"]] = bd.get(r["Disposition"], 0) + 1
    w(f"| Blocked ({len(blocked)}) | " + ", ".join(f"{v} {k}" for k, v in sorted(bd.items())) + " | No verdict; reasons in report.md. TC-006 / TC-087 / TC-007 are blocked by PHA262026P0110. |")
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
    w("Filing order by severity: " + ", ".join(f"**{i - 15}**" for s in (1, 2, 3, 4) for i, e in enumerate(E, 16) if e["sev"] == s) + ". Nothing is filed until the review page's decisions come back.")
    w("")
    open(f"{OUT}/{NAME}.md", "w", encoding="utf-8").write("\n".join(L))
    json.dump({e["iss"]: {"cases": e["cases"], "why": e["title"]} for e in E}, open(f"{OUT}/entries.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"wrote {len(E)} entries → {OUT}/{NAME}.md")


if __name__ == "__main__":
    main()
