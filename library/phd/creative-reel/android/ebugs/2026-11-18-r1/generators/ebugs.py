#!/usr/bin/env python3
"""Build the Creative Reel (Reel Creator) Android eBug draft batch for round R1 (table v4, draft 20261117-150251) on
20.19.0 (90201901), TR261113-0038.

Writes ../20261118_eBug_drafts_Reel-Creator-R1_20.19.0.md, the sibling _images/ folder (one NN_ISS-ID folder per entry:
JPEGs named 20.19.0_crNN_<slug>.jpg, a red box where it helps, plus the logcat excerpt where the finding has a log
cause), logs/ and entries.json. Nothing is filed. Every Fail row of results.csv and every observation O-n is mapped
(entry / not raised); the script stops when one is missing. Built from the AI Hair Color Custom R2 generator.
Run: python library/phd/creative-reel/android/ebugs/2026-11-18-r1/generators/ebugs.py
"""
import csv, json, os, re, shutil, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(OUT, "..", ".."))           # library/phd/creative-reel/android
RUN = f"{ROOT}/runs/2026-11-17-r1"
NAME = "20261118_eBug_drafts_Reel-Creator-R1_20.19.0"
V, B = "20.19.0", "90201901"
DAY = "2026-11-18"
PROD = "PHD-A"
FEAT = "Reel_Creator"
S23 = "Device: Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account"
PIX = "Device: Google Pixel 8a / Android 16 and Samsung Galaxy S23 (SM-S9110) / Android 16, Test Server, Free account"
SRV = "Server: Test Server, Free account (Reel Creator intro page dismissed earlier with 「Don’t show again」)"
PM_URL = "https://www.figma.com/design/m0AHKf3UhHVYlf8kcXPoU0/CineStory"
DS_URL = "https://www.figma.com/design/qdzVXIFZeYwcsa6fipmcLH/Cinematic-Reel-Creator--CineStory-"


def pm(frame, node):
    return f"Spec Link: Reel Creator PM Figma (26 11E Reel Creator, section spec = Creative Reel.pdf), {frame} -\n{PM_URL}?node-id={node}"


def ds(frame, node):
    return f"Spec Link: Reel Creator Design Figma (page 261109_AI_transition_feature, section Design), {frame} -\n{DS_URL}?node-id={node}"


P_ROOM = pm("Reel Creator room frame (rename notes, room board)", "7245-8672")
P_PREV = pm("1. Preview frame", "7336-618")
P_TIPS = pm("2. View photo tips frame", "7336-643")
P_PICK = pm("3. Photo picker frame", "7336-704")
P_PROMPT = pm("4. Photo picker – Import prompt frame (session memory)", "7336-785")
P_RED = pm("5. Imported count out of range → red text frame", "7336-859")
P_CONF = pm("6. Confirm page frame (Generate | 60)", "7336-931")
P_CMIN = pm("7. Confirm page below min frame", "7336-989")
P_LANG = pm("8. Text language frame", "7337-804")
P_ART = pm("My AI Artwork - Reel Creator tab frame", "7271-352")
P_C1 = pm("C1. Cinematic preview frame", "7337-889")
P_C3 = pm("C3. Cinematic confirm page frame (Generate | 40)", "7337-1042")
D_LIST = ds("01_Template_List frame", "934-622")
D_PREV = ds("02_Template_Preview_SwipeHint_Peek frame", "1101-4947")
D_PICK = ds("03_Photo_Picker frame", "950-5298")
D_PROMPT = ds("03-1_Photo_Picker_Reuse_Last_Photos frame", "957-5859")
D_P1 = ds("03-4_Toast_Reuse_Last_Photos_1 frame", "960-6686")
D_CONF = ds("04_Generate_Settings frame", "961-6760")
D_LANG = ds("04-1_Generate_Settings_Text_Language_Sheet frame", "977-4343")
D_ART = ds("05_Result_My_AI_Artwork frame", "970-4457")

ROOM = ["Launch the APP", "Swipe the Launcher shortcut grid left to page 2", "Tap Cinematic Reel Creator"]
SCF = ROOM + ["Tap the single-color-fastcut card in the second section", "Tap Use Template"]
SCF7 = SCF + ["Tap 7 photos in the grid, one after another", "Tap Next"]
MC = ROOM + ["Tap the Micro Cinema card in the first section", "Tap Use Template", "Tap 1 photo", "Tap Next"]
SS = ROOM + ["Tap the Selfie Shake card in the third section", "Tap Use Template", "Tap 4 photos in the grid, one after another", "Tap Next"]
CG = ROOM + ["Swipe the second section left", "Tap the cinematic-grade card", "Tap Use Template"]
ROOMBOX = [(40, 265, 920, 345), (40, 1075, 920, 1150), (40, 1885, 920, 1960)]

# Each entry: iss, title, cls (Functional / UI / UX), sev, owner, cases, rep, note (QA note, not pasted), short, steps,
# res, res_zh, exp, exp_zh, links, dev, imgs [(png, slug, box or None)], log (title, [(label, t0, t1)]) or None, rel
E = [
 dict(iss="ISS-CR-01", title="Launcher shortcut and AI Videos card still read 「Cinematic Reel Creator」", cls="UI", sev=3, owner="RD",
      cases=["TC-002", "TC-004"], rep=(2, 2),
      note="R-003 / R-005 (PM room board: the room formerly Cinematic Reel Creator is renamed 「Reel Creator」, incl. the Launcher Shortcut and the AI Video page entry). The Effects button already reads 「Reel Creator」 (TC-001 Pass). Seen on the Pixel 8a (TC-002 / TC-004) and again on the S23 (TC-113 entries 1–2). Localised shortcut names differ per language (zh-Hant 「AI電影感運鏡」, de 「Reel-Creator」; O-9).",
      short="Launcher shortcut and AI Videos card still read 「Cinematic Reel Creator」",
      steps=["Launch the APP", "Swipe the Launcher shortcut grid left to page 2", "Read the room's shortcut label", "Tap the AI Videos tab", "Read the room's card label"],
      res="The shortcut and the AI Videos card both read 「Cinematic Reel Creator」.",
      res_zh="Launcher 捷徑與 AI Videos 卡片仍顯示舊名 Cinematic Reel Creator。",
      exp="Both entries read 「Reel Creator」 (the room is renamed).",
      exp_zh="兩個入口都應顯示「Reel Creator」。",
      links=[P_ROOM], dev=PIX,
      imgs=[("TC-002-shortcut", "launcher_shortcut", None), ("TC-004-aivideos", "ai_videos_card", None)], log=None, rel=[]),
 dict(iss="ISS-CR-02", title="Reel Creator room has no 「Reel Creator」 title", cls="UI", sev=3, owner="RD",
      cases=["TC-005"], rep=(2, 2),
      note="R-001 (PM room frame titles the room 「Reel Creator」). The top bar has 「‹」, the credit pill and the history icon (R-008 OK) but no title text anywhere on the page. Pixel 8a (TC-005) and S23 (TC-113 room screenshots).",
      short="Room shows no 「Reel Creator」 title in its top bar",
      steps=ROOM + ["Read the top bar"],
      res="The top bar shows 「‹」, the credit pill and the history icon, with no title.",
      res_zh="房間上方沒有標題 Reel Creator。",
      exp="The room is titled 「Reel Creator」.",
      exp_zh="房間應有標題「Reel Creator」。",
      links=[P_ROOM], dev=PIX,
      imgs=[("TC-113-1-shortcut-room", "room_no_title", (0, 95, 1080, 220))], log=None, rel=[]),
 dict(iss="ISS-CR-03", title="Room section titles are raw string keys", cls="UI", sev=2, owner="RD",
      cases=["TC-006"], rep=(2, 2),
      note="R-006 (Design 01_Template_List: 「Cinematic Styles 🎬」, 「Year-End Recap 🎉」, 「Cool Transition 🎞️」; the PM drew 「Year-End Recap 📅」 / 「Cool Transitions 🤳🏻」; titles are CMS category names). The app shows 「ReelCreator_Category_Cinestory」, 「ReelCreator_Category_CreativeR」, 「ReelCreator_Category_AITransit」 — string keys that were never resolved. The missing Year-End Recap section is ISS-CR-06 (PM). Pixel 8a and S23; the keys also stay in zh-Hant / ja / de / pt (TC-123).",
      short="Room section titles show raw keys 「ReelCreator_Category_…」",
      steps=ROOM + ["Scroll the room to the bottom"],
      res="The section titles read 「ReelCreator_Category_Cinestory」, 「…_CreativeR」 and 「…_AITransit」.",
      res_zh="三個區塊標題顯示未轉換的字串 key。",
      exp="Category names: 「Cinematic Styles 🎬」, 「Year-End Recap 🎉」, 「Cool Transition 🎞️」 (Design).",
      exp_zh="區塊標題應顯示分類名稱（如 Cinematic Styles）。",
      links=[D_LIST, P_ROOM], dev=PIX,
      imgs=[("TC-113-1-shortcut-room", "raw_section_keys", ROOMBOX), ("TC-006-bottom", "room_bottom", None)], log=None, rel=[]),
 dict(iss="ISS-CR-04", title="Cinematic Styles cards carry no inset photo", cls="UI", sev=4, owner="RD",
      cases=["TC-007"], rep=(2, 2),
      note="R-007 (Design 01_Template_List draws a small inset photo at the bottom left of each Cinematic Styles card; Design-only, the PM room frame does not draw it). The cards are plain full-card thumbnails (One-Take Shot's is black). AI Transition cards show grey placeholders (CMS thumbnails; not filed, TC-029 recorded it).",
      short="Room: Cinematic Styles cards have no inset photo",
      steps=ROOM + ["Swipe the first section left"],
      res="The Cinematic Styles cards are plain thumbnails with no inset photo.",
      res_zh="Cinematic Styles 卡片左下沒有小圖。",
      exp="Each Cinematic Styles card carries a small inset photo at its bottom left (Design).",
      exp_zh="卡片左下應有小張示意照片（Design）。",
      links=[D_LIST], dev=PIX,
      imgs=[("TC-113-1-shortcut-room", "cine_cards_no_inset", (30, 380, 1080, 1040)), ("TC-007-cine-left", "cine_row_left", None)], log=None, rel=[]),
 dict(iss="ISS-CR-05", title="PM: no Reel Creator template row on the Launcher", cls="Functional", sev=3, owner="PM",
      cases=["TC-003", "TC-113"], rep=(1, 1),
      note="R-004 / R-108 (PM room board: the Launcher Template row of the room is labelled 「Reel Creator」, one of five entries). On Test Server the Launcher's template rows are New Hair Colors, Your Best Look Yet, Meme Generator, Cute Pet Moments, ID Photo, Minimalist Collage: no Reel Creator row, so its title and the fifth entry (TC-113) cannot be checked. Whether the row is CMS-scheduled for this server is not stated: filed to PM to confirm (2026-11-11 rule).",
      short="No Reel Creator template row on the Launcher — PM to confirm",
      steps=["Launch the APP", "Scroll the Launcher to the bottom"],
      res="No 「Reel Creator」 (or 「Cinematic Reel Creator」) template row on the Launcher.",
      res_zh="Launcher 沒有 Reel Creator 的模板列。",
      exp="PM to confirm whether the Launcher shows a 「Reel Creator」 template row on this build, or when.",
      exp_zh="請 PM 確認 Launcher 是否應有「Reel Creator」模板列及上線時間。",
      links=[P_ROOM], dev=PIX,
      imgs=[("TC-003-mid", "launcher_rows_mid", None), ("TC-003-bottom", "launcher_rows_bottom", None)], log=None, rel=[]),
 dict(iss="ISS-CR-06", title="PM: no Year-End Recap section; Creative templates are bare test entries", cls="Functional", sev=3, owner="PM",
      cases=["TC-023", "TC-026"], rep=(2, 2),
      note="R-006 / R-020 / R-026 / R-027 (PM room and Preview frames: a Year-End Recap section with 「Top 5 of My Year」; every template carries its DisplayName, description, demo and tips). Test Server lists two Creative templates only, 「single-color-fastcut」 and 「cinematic-grade」: raw names, no description (TC-024), and both play the same demo (「MY YEAR QUEST 我的年度冒險」) so the swipe shows no template of its own (TC-026). All Creative rows ran on these stand-ins. Probably CMS test content: filed to PM to confirm the Creative content for this build (Q-19). TC-023's demo itself auto-plays full screen and loops (1080 × 2009 view on a 1080 × 2340 screen).",
      short="No Year-End Recap; Creative templates have raw names, one demo — PM to confirm",
      steps=ROOM + ["Tap the single-color-fastcut card in the second section", "Swipe up on the Preview", "Read the template name and demo"],
      res="No Year-End Recap section; Creative templates have raw names, no description and one shared demo.",
      res_zh="沒有 Year-End Recap；Creative 模板名稱為 key、無描述、共用同一支 demo。",
      exp="PM to confirm the Creative content: Year-End Recap with 「Top 5 of My Year」, names, descriptions, demos.",
      exp_zh="請 PM 確認 Creative 內容（Year-End Recap、模板名稱、描述與各自的 demo）。",
      links=[P_ROOM, P_PREV], dev=S23,
      imgs=[("TC-023-1", "creative_preview", None), ("TC-026-up", "swipe_same_demo", None)], log=None, rel=["Q-19"]),
 dict(iss="ISS-CR-07", title="PM: photo tips entry — Design ⓘ vs 「View photo tips」 chip; Creative Previews have none", cls="UI", sev=3, owner="PM",
      cases=["TC-033", "TC-024"], rep=(2, 2),
      note="R-029 / R-036 / R-037 (Design 02 Preview draws an ⓘ next to 「‹」; the PM Preview frame draws a 「View photo tips」 text button and a tips sheet 「Photo tips」 / 「Got it」; Q-28 open). Cinestory Previews show 「💡 View photo tips」 (PM version) opening the app-wide guide (「Recommendation」 / 「Avoid」, 「Continue」; heading and items not filed, KP-135). Creative Previews (both stand-ins) have neither ⓘ nor the chip, so their tips cannot be opened — possibly no tips content in the CMS (ISS-CR-06). PM to decide the entry (ⓘ or chip), whether the sheet keeps the app-wide 「Continue」 or the PM's 「Photo tips」 / 「Got it」, and that every template has it.",
      short="Preview: no photo tips entry on Creative; ⓘ vs 「View photo tips」 — PM to decide",
      steps=ROOM + ["Tap the single-color-fastcut card in the second section", "Look for a photo tips entry at the top", "Tap ‹", "Tap the Horror Movie card in the first section", "Tap 💡 View photo tips"],
      res="Creative Previews have no tips entry; Cinestory shows 「💡 View photo tips」 (Design: ⓘ).",
      res_zh="Creative Preview 沒有照片提示入口；Cinestory 為文字按鈕（Design 為 ⓘ）。",
      exp="PM to decide ⓘ (Design) or 「View photo tips」 (PM) on every Preview, and the sheet's title and button.",
      exp_zh="請 PM 決定提示入口形式（ⓘ 或文字），且所有模板都要有。",
      links=[D_PREV, P_TIPS], dev=S23,
      imgs=[("TC-023-1", "creative_no_tips_entry", (0, 80, 1080, 260)), ("TC-030", "cine_view_photo_tips", None), ("TC-033-cine-sheet", "tips_sheet", None)],
      log=None, rel=["Q-28"]),
 dict(iss="ISS-CR-08", title="Preview count line has no image icon", cls="UI", sev=4, owner="RD",
      cases=["TC-030", "TC-024"], rep=(2, 2),
      note="R-031 (Design 02 Preview: the count 「1 Photo」 with an image icon before it; the PM wrote 「1 photo」, Q-36). Cinestory 「Horror Movie」 reads 「1 photo」 and Creative 「single-color-fastcut」 「1–30 photos」, both without the icon. Design first for the wording (capital P) as well.",
      short="Preview: photo count has no image icon (Design 「1 Photo」 with icon)",
      steps=ROOM + ["Tap the Horror Movie card in the first section", "Read the count line above Use Template"],
      res="The count reads 「1 photo」 with no image icon (Creative: 「1–30 photos」, no icon).",
      res_zh="張數文字前沒有圖片 icon，且為小寫 photo。",
      exp="The count shows an image icon and 「1 Photo」 (Design).",
      exp_zh="應有圖片 icon 並顯示「1 Photo」。",
      links=[D_PREV], dev=S23,
      imgs=[("TC-030", "count_no_icon", None)], log=None, rel=["Q-36"]),
 dict(iss="ISS-CR-09", title="Picker has no 「Add photos」 title and its tray wording differs from the Design", cls="UI", sev=3, owner="RD",
      cases=["TC-037"], rep=(1, 1),
      note="R-041 / R-042 (Design 03_Photo_Picker: title 「Add photos」, tray 「Select {min} to {max} photos to continue.」; the PM drew 「Add Photos」 and 「Select 5–15 photos」; Design first). The picker shows 「‹」 and a camera icon with no title, and the tray reads 「Select 15–40 photos」 (cinematic-grade). The album tab 「All ⌄」 is the album name (KP-135, not filed).",
      short="Photo picker: no 「Add photos」 title; tray wording differs from Design",
      steps=CG + ["Read the top bar and the tray"],
      res="No title; the tray reads 「Select 15–40 photos」.",
      res_zh="選圖頁沒有 Add photos 標題，tray 文字與 Design 不同。",
      exp="Title 「Add photos」; tray 「Select 15 to 40 photos to continue.」 (Design).",
      exp_zh="應有標題 Add photos，tray 為「Select 15 to 40 photos to continue.」。",
      links=[D_PICK], dev=S23,
      imgs=[("TC-037-picker", "picker_no_title", None)], log=None, rel=[]),
 dict(iss="ISS-CR-10", title="Tray thumbnails have no 「×」: a photo cannot be removed from the tray", cls="Functional", sev=3, owner="RD",
      cases=["TC-038", "TC-136"], rep=(2, 2),
      note="R-042 / R-124 (Design 03_Photo_Picker draws 「×」 on every tray thumbnail; tapping it unpicks the photo). No 「×」 on any tray thumbnail; a tap and a 1.5 s long-press on a thumbnail do nothing (16/40 stays). A photo leaves only by tapping it again in the grid.",
      short="Photo picker: tray thumbnails have no 「×」 and cannot be removed",
      steps=CG + ["Tap 16 photos in the grid, one after another", "Tap the second thumbnail in the tray"],
      res="The tray thumbnails have no 「×」 and the tap does nothing (16/40 stays).",
      res_zh="tray 縮圖沒有 ×，點擊也無法移除。",
      exp="Each tray thumbnail has 「×」; tapping it unpicks that photo (Design).",
      exp_zh="每張 tray 縮圖應有 ×，點擊即取消選取。",
      links=[D_PICK], dev=S23,
      imgs=[("TC-136-16b", "tray_no_x", None), ("TC-136-traytap", "tray_tap_nothing", None)], log=None, rel=[]),
 dict(iss="ISS-CR-11", title="No red tray text when the picked or imported count is outside the range", cls="Functional", sev=3, owner="RD",
      cases=["TC-057", "TC-058", "TC-038"], rep=(3, 3),
      note="R-054 / R-055 (PM frame 5: after Import, a count below min shows red 「Select at least {min} photos ({n} more)」, above max red text; Next disabled). Import of 4 into cinematic-grade (15–40) and of 10 into Selfie Shake (4) keep the white 「Select 15–40 photos」 / 「Select 4 photos」 with no count; Next is disabled (OK). TC-038 (manual pick of 3) is the same missing line (Q-30, PM shows it after Import; assumption: also for a manual pick).",
      short="Photo picker: imported count out of range shows no red tray text",
      steps=ROOM + ["Tap the Selfie Shake card in the third section", "Tap Use Template", "Tap 4 photos in the grid, one after another", "Tap Next", "Tap ‹ three times", "Swipe the second section left", "Tap the cinematic-grade card", "Tap Use Template", "Tap Import on the prompt"],
      res="4 photos are imported and Next is disabled, but the tray still reads 「Select 15–40 photos」 in white.",
      res_zh="匯入張數低於下限時 tray 沒有紅字提示。",
      exp="The tray shows red 「Select at least 15 photos (11 more)」 (above max: red text), Next disabled until in range.",
      exp_zh="應顯示紅字「Select at least 15 photos (11 more)」。",
      links=[P_RED], dev=S23,
      imgs=[("TC-057-import", "import_below_min", None), ("TC-058-import", "import_above_max", None)], log=None, rel=["Q-30"]),
 dict(iss="ISS-CR-12", title="Imported photos lose their grid tick; tapping one adds it twice", cls="Functional", sev=2, owner="RD",
      cases=["TC-058", "TC-059"], rep=(2, 2),
      note="R-053 / R-056 (PM Import prompt: Import brings in the picked state). After Import the tray holds the whole set, but some imported photos have no badge in the grid: 10 into Selfie Shake left the 10th unticked (tap → 「You can only select 4 photos.」); after 2 of 6 were deleted from the Gallery, 2 of the 4 imported were unticked and tapping one added it a second time (5/30, the same photo twice in the tray). Likely a photo-id / position mix-up (KP-073 / K03). With no deletion and within the limit every photo was ticked (TC-055, TC-133).",
      short="Photo picker Import: imported photos unticked; tapping one adds it twice",
      steps=ROOM + ["Tap the single-color-fastcut card in the second section", "Tap Use Template", "Tap 6 photos in the grid, one after another", "Tap Next", "Tap ‹ three times", "Press Home", "Delete the first 2 of the 6 photos in Gallery", "Open PhotoDirector from Recents", "Tap the single-color-fastcut card", "Tap Use Template", "Tap Import on the prompt", "Tap the third picked photo in the grid"],
      res="4 photos are in the tray but 2 have no tick in the grid; tapping one adds it again (5/30, duplicate in the tray).",
      res_zh="匯入後部分照片在格子上沒有勾選，點擊會重複加入同一張。",
      exp="Every imported photo is ticked in the grid with its number; tapping it unpicks it.",
      exp_zh="匯入的照片都應打勾編號，點擊應取消選取。",
      links=[P_PROMPT, D_PROMPT], dev=S23,
      imgs=[("TC-059-import", "import_unticked", None), ("TC-059-tap-d0594", "duplicate_added", None), ("TC-058-tap10th", "tenth_unticked_toast", None)],
      log=None, rel=[]),
 dict(iss="ISS-CR-13", title="Import prompt shows no 「+N」 on its third thumbnail", cls="UI", sev=4, owner="RD",
      cases=["TC-054"], rep=(1, 1),
      note="R-125 (Design 03-1: with more than three photos remembered, the third thumbnail is covered by 「+{N−3}」, e.g. 8 photos → 「+5」). With 7 remembered the prompt reads 「Use the 7 photos you picked last time?」 (OK) but shows photos 1–3 plainly with no 「+4」.",
      short="Import prompt: no 「+4」 on the third thumbnail for 7 photos",
      steps=SCF7 + ["Tap ‹ three times", "Tap the single-color-fastcut card", "Tap Use Template"],
      res="The prompt shows three thumbnails with no 「+4」 on the third.",
      res_zh="匯入提示第三張縮圖沒有「+4」。",
      exp="The third thumbnail is covered by 「+4」 (Design 03-1).",
      exp_zh="第三張縮圖應覆蓋「+4」。",
      links=[D_PROMPT], dev=S23,
      imgs=[("TC-054-prompt-crop", "prompt_no_plus", None)], log=None, rel=[]),
 dict(iss="ISS-CR-14", title="PM decision: one remembered photo — Design shows a prompt, PM and app show none", cls="UX", sev=3, owner="PM",
      cases=["TC-139"], rep=(1, 1),
      note="Q-27, filed to PM for a decision. Design 03-4 draws 「Use the photo you picked last time?」 with one thumbnail; the PM says no prompt when 1 photo was picked (R-057). After 3 of 4 remembered photos were deleted from the Gallery the app shows no prompt (it follows the PM). The casebook assumed the Design card shows (Design first).",
      short="Import prompt for one remembered photo: Design shows it, app does not — PM",
      steps=SS + ["Tap ‹ three times", "Press Home", "Delete 3 of the 4 photos in Gallery", "Open PhotoDirector from Recents", "Tap the single-color-fastcut card in the second section", "Tap Use Template"],
      res="No Import prompt; the picker opens plain.",
      res_zh="只剩一張記憶照片時不顯示匯入提示（Design 有、PM 無）。",
      exp="PM to decide: 「Use the photo you picked last time?」 (Design 03-4) or no prompt (PM R-057).",
      exp_zh="請 PM 決定一張照片時是否顯示提示。",
      links=[D_P1, P_PROMPT], dev=S23,
      imgs=[("TC-139-prompt", "no_prompt_one_left", None)], log=None, rel=["Q-27"]),
 dict(iss="ISS-CR-15", title="Confirm page lacks the 9:16 ratio and the reorder hint; layout differs from the Design", cls="UI", sev=3, owner="RD",
      cases=["TC-063", "TC-094", "TC-100", "TC-148"], rep=(4, 4),
      note="R-060 / R-061 / R-064 / R-085 (PM confirm frame: 「output 9:16」 and 「Long-press to reorder · tap × to remove」; Design 04: count with image icon, 「9:16」 with ratio icon, 「Your photos (7/15)」, 「+」 first). On Creative, Cinematic (Micro Cinema) and AI Transition (Selfie Shake) pages, light and dark: no 9:16, no reorder hint, no count icon, counter 「7/30」 at the right of 「Your photos」, 「+」 last. The hint and 9:16 are in both PM and Design; the other points follow the PM where the Design differs (Design first). Text Language is ISS-CR-16, prices ISS-CR-18 / -19.",
      short="Confirm page: no 「9:16」, no reorder hint, 「+」 last",
      steps=SCF7 + ["Read the confirm page"],
      res="No 9:16 or count icon in the header; 「Your photos」 「7/30」 with no hint; 「+」 after the photos.",
      res_zh="確認頁沒有 9:16、沒有排序提示文字，+ 在最後，張數不在標題括號內。",
      exp="Header shows 「9:16」; 「Your photos (7/30)」 and the reorder hint; 「+」 tile first (Design).",
      exp_zh="應有 9:16、排序提示，「+」在第一格。",
      links=[D_CONF, P_CONF], dev=S23,
      imgs=[("TC-063-confirm", "creative_confirm", None), ("TC-094", "micro_cinema_confirm", None), ("TC-100", "selfie_shake_confirm", None)],
      log=None, rel=["Q-31"]),
 dict(iss="ISS-CR-16", title="Creative confirm page has no Text Language bar", cls="Functional", sev=2, owner="RD",
      cases=["TC-075", "TC-076", "TC-148"], rep=(4, 4),
      note="R-067 / R-073 / R-074 (Design 04 / 04-1: a 「Text Language」 bar above Generate opening a language sheet, default the device language; PM frame 8 「Text language English ▾」). No bar on either Creative template in English, zh-Hant or dark theme, and nowhere else (not on the Preview: Q-6 asked whether the menu moves there). The reel's text language therefore cannot be chosen; 8 rows are Blocked behind it (TC-077, 078, 140, 109, 079, 080, 081, 082) and TC-116 could not set it.",
      short="Creative confirm page has no 「Text Language」 bar",
      steps=SCF7 + ["Look for Text Language above Generate"],
      res="No 「Text Language」 bar or sheet anywhere on the page.",
      res_zh="Creative 確認頁沒有 Text Language 選項，無法選擇影片文字語言。",
      exp="A 「Text Language」 bar above Generate shows the device language and opens the language sheet.",
      exp_zh="Generate 上方應有 Text Language 列，預設裝置語言並可開啟語言清單。",
      links=[D_LANG, P_LANG], dev=S23,
      imgs=[("TC-063-confirm", "no_text_language", (0, 1900, 1080, 2250)), ("TC-076-zh-confirm", "no_text_language_zh", None)], log=None, rel=["Q-6"]),
 dict(iss="ISS-CR-17", title="Count below min is not shown in red on the confirm page", cls="UI", sev=3, owner="RD",
      cases=["TC-066"], rep=(1, 1),
      note="R-069 (PM frame 7: removing photos below min turns the count red and disables Generate). cinematic-grade (15–40): 15 → 14 keeps 「14/40」 orange like an in-range count; Generate is disabled (OK).",
      short="Confirm page: count below min (14/40) is not red",
      steps=CG + ["Tap 15 photos in the grid, one after another", "Tap Next", "Tap × on photo 1"],
      res="「14/40」 stays orange; Generate is disabled.",
      res_zh="低於下限時張數未變紅。",
      exp="「14/40」 turns red and Generate is disabled.",
      exp_zh="張數應顯示紅色。",
      links=[P_CMIN], dev=S23,
      imgs=[("TC-066-14", "count_not_red", None)], log=None, rel=[]),
 dict(iss="ISS-CR-18", title="PM: Creative prices 70 / 90 and AI Transition 48 vs the drawn Creative 60", cls="Functional", sev=3, owner="PM",
      cases=["TC-063", "TC-074", "TC-118", "TC-148"], rep=(4, 4),
      note="R-068 / R-071 (PM confirm frame: 「Generate | 60」 for 「Top 5 of My Year」; other templates' prices not stated, Q-9). Top 5 of My Year is not on Test Server (ISS-CR-06). single-color-fastcut charges a flat 70 (1 and 7 photos; Detail 「Reel Creator -70」, balance 1052 → 982), cinematic-grade 90 (15–40), Selfie Shake 48. The charge equals the button each time. Filed to PM to confirm the Creative / AI Transition price table (Q-9).",
      short="Creative 70 / 90 and AI Transition 48 credits vs drawn 60 — PM to confirm",
      steps=SCF7 + ["Read the Generate button", "Tap Generate", "Tap the credit pill in the room", "Tap Detail"],
      res="「Generate | 70」; 70 credits charged (1052 → 982), Detail 「Reel Creator -70」.",
      res_zh="Creative 收 70 點（另有 90、48），spec 只畫了 60。",
      exp="PM to confirm each template's price (spec draws 60 for 「Top 5 of My Year」 only).",
      exp_zh="請 PM 確認各模板價格。",
      links=[P_CONF], dev=S23,
      imgs=[("TC-083-confirm", "generate_70", None), ("TC-118-detail", "detail_minus_70", None)],
      log=("Creative charge 70", [("Generate tapped 14:04:41", "14:04:30", "14:04:50")]), rel=["Q-9"]),
 dict(iss="ISS-CR-19", title="Micro Cinema charges 48 credits, spec 40", cls="Functional", sev=2, owner="RD",
      cases=["TC-094", "TC-096", "TC-119"], rep=(3, 3),
      note="R-084 (PM C3 Cinematic confirm frame: 「Generate | 40」 on Micro Cinema). The button reads 「Generate | 48」 and 48 is charged (842 → 794 at 14:58:37; Detail -48). Second Micro Cinema (TC-122) 48 again. The price may be server data.",
      short="Micro Cinema shows and charges 48 credits instead of 40",
      steps=MC + ["Read the Generate button", "Tap Generate"],
      res="「Generate | 48」; the balance drops by 48 (842 → 794).",
      res_zh="Micro Cinema 顯示並扣 48 點，spec 為 40。",
      exp="「Generate | 40」 and 40 deducted.",
      exp_zh="應為 40 點。",
      links=[P_C3], dev=S23,
      imgs=[("TC-094", "generate_48", None), ("TC-119-detail", "detail_minus_48", None)],
      log=("Micro Cinema charge 48", [("Generate tapped 14:58:32", "14:58:25", "14:58:45")]), rel=[]),
 dict(iss="ISS-CR-20", title="PM: Credit Detail names Cinematic and AI Transition uses only 「Reel Creator」", cls="UI", sev=3, owner="PM",
      cases=["TC-119", "TC-120"], rep=(2, 2),
      note="R-102 (KP-017: Detail lists each use under the right feature name; the feature name is not fixed, Q-2). Every Reel Creator use — Creative, Micro Cinema, Selfie Shake — is listed as 「Reel Creator / PhotoDirector (Android)」 with no time, so the three features cannot be told apart. PM to decide whether one name is intended.",
      short="Credit Detail names every Reel Creator use 「Reel Creator」 — PM to decide",
      steps=SS + ["Tap Generate", "Tap the credit pill in the room", "Tap Detail"],
      res="The entry reads 「Reel Creator」 -48, like the Micro Cinema and Creative entries.",
      res_zh="Credit Detail 中三種功能都顯示 Reel Creator，無法分辨。",
      exp="PM to decide: one 「Reel Creator」 name for all three, or Cinematic Styles / AI Transition named separately.",
      exp_zh="請 PM 決定 Detail 中的功能名稱。",
      links=[P_ART], dev=S23,
      imgs=[("TC-120-detail", "detail_names", None)], log=None, rel=["Q-2"]),
 dict(iss="ISS-CR-21", title="Reel Creator strings stay English in other app languages", cls="UI", sev=3, owner="RD",
      cases=["TC-123", "TC-076", "TC-125"], rep=(4, 4),
      note="R-105 / R-107 (localised strings in every app language; PM frames carry the strings; PHD supports zh-Hant, ja, de, pt …). In zh-Hant, ja, de and pt the tray 「Select 4 photos」, the prompt 「Use the 4 photos you picked last time?」, the hint 「Please upload at least 4 photos」, 「Your photos」, 「N photos」 and 「Use Template」 stay English; only shared buttons (下一步, 匯入, 生成 …) are translated. Numbers and placeholders are right, no crash.",
      short="Picker, Import prompt and confirm strings stay English in zh-Hant / ja / de / pt",
      steps=["Set the phone language to 繁體中文 (Taiwan)", "Launch the APP", "Swipe the Launcher shortcut grid left to page 2", "Tap AI電影感運鏡", "Tap the Selfie Shake card in the third section", "Tap Use Template", "Tap 3 photos in the grid, one after another"],
      res="The tray reads 「Select 4 photos」 (English); the prompt, 「Your photos」 and the upload hint are English too.",
      res_zh="切換為中文／日文／德文／葡文時，Reel Creator 的文字仍為英文。",
      exp="All Reel Creator strings are shown in the app language.",
      exp_zh="所有 Reel Creator 文字應依 App 語言翻譯。",
      links=[P_PICK, P_PROMPT], dev=S23,
      imgs=[("TC-123-zh-tray3", "zh_tray_english", None), ("TC-123-zh-prompt", "zh_prompt_english", None), ("TC-123-ja-hint", "ja_hint_english", None)],
      log=None, rel=[]),
 dict(iss="ISS-CR-22", title="German Import button is cut off as 「Importie…」", cls="UI", sev=4, owner="RD",
      cases=["TC-125"], rep=(1, 1),
      note="R-107 (KP-101: long translations stay readable; PM Import prompt frame). In German the prompt's button reads 「Importie…」; Portuguese 「Importar」 fits.",
      short="Import prompt button truncated to 「Importie…」 in German",
      steps=["Set the phone language to Deutsch", "Launch the APP", "Swipe the Launcher shortcut grid left to page 2", "Tap Reel-Creator", "Tap the Selfie Shake card in the third section", "Tap Use Template", "Tap 4 photos in the grid, one after another", "Tap Weiter", "Tap ‹ three times", "Tap the Selfie Shake card", "Tap Use Template"],
      res="The prompt button reads 「Importie…」.",
      res_zh="德文匯入按鈕文字被截斷。",
      exp="The button shows the full word (「Importieren」) without truncation.",
      exp_zh="按鈕文字應完整顯示。",
      links=[P_PROMPT], dev=S23,
      imgs=[("TC-125-de-prompt", "de_import_cut", None)], log=None, rel=[]),
 dict(iss="ISS-CR-23", title="Creative processing card shows no time estimate, 「Almost Done」 from the start", cls="Functional", sev=3, owner="RD",
      cases=["TC-085", "TC-141"], rep=(3, 3),
      note="R-078 / R-130 (Design 05 My AI Artwork: 「9 minutes remaining ...」 with a progress bar; 「Almost done」 once the estimate runs out). Creative cards read 「Almost Done」 5 s after Generate with an indeterminate bar, for the whole ≈ 9.5 min job (three jobs). Cinestory and AI Transition cards do show 「N minutes remaining…」 (TC-096), though 14 min shown vs 6.4 min taken (O-12).",
      short="Creative card shows 「Almost Done」 at once, no remaining time",
      steps=SCF7 + ["Tap Generate", "Read the new card in My AI Artwork"],
      res="The card reads 「Processing...」 / 「Almost Done」 from 5 s in, with a back-and-forth bar and no remaining time.",
      res_zh="Creative 生成卡片一開始就顯示 Almost Done，沒有剩餘時間。",
      exp="The card shows 「… minutes remaining ...」 with a progress bar, 「Almost done」 only after the estimate runs out.",
      exp_zh="應顯示剩餘時間與進度條，時間到才顯示 Almost done。",
      links=[D_ART, P_ART], dev=S23,
      imgs=[("TC-085-artwork-1", "almost_done_at_start", None), ("TC-096-after", "cinestory_has_estimate", None)], log=None, rel=[]),
 dict(iss="ISS-CR-24", title="Completion notification opens a stale My AI Artwork page still 「Processing」", cls="Functional", sev=3, owner="RD",
      cases=["TC-121"], rep=(2, 2),
      note="R-104 (KP-029: the done notification opens the finished result in My AI Artwork). The notification 「Reel Creator Ready!」 / 「Tap to see your Reel Creator.」 (phd://navigate/page?name=cinematic_reel_creator_done) brought back the old My AI Artwork page from before Home: the card stayed 「Processing… / Almost Done」 for 2.5 min until the page was reopened (status Done 14:39:38 only then). Same stale card seen at 15:18 and 15:33 (O-11 / O-12). PHA262026-0373 (closed: 「APP version does not support feature」) is not back.",
      short="「Reel Creator Ready!」 notification opens a stale 「Processing」 card",
      steps=SCF7 + ["Tap Generate", "Press Home", "Wait for the notification 「Reel Creator Ready!」", "Tap the notification"],
      res="My AI Artwork shows the card still 「Processing…」; it updates only after reopening the page.",
      res_zh="點完成通知後 My AI Artwork 仍顯示處理中，需重新進入才更新。",
      exp="The notification opens My AI Artwork on the finished reel.",
      exp_zh="點通知應開到已完成的影片。",
      links=[P_ART], dev=S23,
      imgs=[("TC-121-shade", "notification", None), ("TC-121-after-tap", "stale_processing", None), ("TC-121-finished", "after_reopen", None)],
      log=("Notification and stale card", [("Notification and tap", "14:35:55", "14:36:40"), ("Status Done only after reopening", "14:39:30", "14:39:40")]),
      rel=["PHA262026-0373 (closed; not reproduced)"]),
 dict(iss="ISS-CR-25", title="Interrupted upload: 70 credits charged, not refunded although the dialog says so; Retry does nothing", cls="Functional", sev=2, owner="RD",
      cases=["TC-143"], rep=(1, 1),
      note="R-132 (Design 05: an interrupted upload shows ⚠ 「Resume to Upload」, resuming charges no second time) and run step 8 (a failed job costs nothing net). Wi-Fi cut 0.1 s after the pack reached UploadFile: the dialog says 「Unsuccessful, please try again. Credits refunded.」, but Detail lists 「Reel Creator -70」 and no refund (912 → 842 kept at 14:51–14:52). The card is ⚠ 「Retry」 (not 「Resume to Upload」); after Wi-Fi is back, Retry only logs 「longTask retry click」 and nothing runs; the card returns to ⚠ Retry. Net 70 lost, no reel. One attempt (credits). Severity proposal S2; S1 if lost credits count as data loss.",
      short="Wi-Fi lost during upload: 70 charged, 「Credits refunded」 but no refund",
      steps=SCF7 + ["Tap Generate", "Turn Wi-Fi off right after", "Tap OK on the error dialog", "Turn Wi-Fi on", "Tap the room's history icon", "Tap Retry on the ⚠ card", "Wait 6 minutes", "Tap the credit pill in the room", "Tap Detail"],
      res="The dialog says 「Credits refunded」 but 70 stays deducted (no refund row); Retry never runs the job.",
      res_zh="上傳中斷後提示已退點，實際扣 70 點未退；Retry 無作用。",
      exp="「Resume to Upload」 finishes the job with one charge; a failed job refunds the 70 credits.",
      exp_zh="應可續傳完成且只扣一次；失敗時應確實退點。",
      links=[D_ART], dev=S23,
      imgs=[("TC-143-confirm-2", "credits_refunded_dialog", None), ("TC-143-step3b", "retry_card", None), ("TC-143-detail", "detail_no_refund", None), ("TC-143-shop-balance", "balance_842", None)],
      log=("Interrupted upload, no refund", [("Generate, Wi-Fi off, Retry, balance", "14:40:50", "14:52:20")]), rel=[]),
 dict(iss="ISS-CR-26", title="My AI Artwork tabs: 「Image to Video」 is not first and 「Reel Creator」 not second", cls="UI", sev=3, owner="RD",
      cases=["TC-089"], rep=(1, 1),
      note="R-080 (PM artwork frame and Design 05: 「Image to Video」 first, 「Reel Creator」 second, then the other feature tabs). The tab row is 「Recent」 then alphabetical (AI Anime Video, AI Art …, Character Motion Swap, Image to Video, Reel Creator, Style Transfer). The Reel Creator tab and its items are right; no 「Cinematic Reel Creator」 tab.",
      short="My AI Artwork: 「Image to Video」 / 「Reel Creator」 not first and second",
      steps=ROOM + ["Tap the history icon", "Swipe the tab row right to its start"],
      res="Tabs start 「Recent」, 「AI Anime Video」, 「AI Art」 …; 「Image to Video」 and 「Reel Creator」 come late.",
      res_zh="My AI Artwork 分頁依字母排序，Image to Video 與 Reel Creator 不在最前。",
      exp="「Image to Video」 first and 「Reel Creator」 second.",
      exp_zh="Image to Video 第一、Reel Creator 第二。",
      links=[P_ART, D_ART], dev=S23,
      imgs=[("TC-089-tabs-start", "tabs_start", None), ("TC-089-tabs-left", "tabs_entry", None)], log=None, rel=[]),
 dict(iss="ISS-CR-27", title="Cinematic Styles reel is 3:4, not 9:16", cls="Functional", sev=2, owner="RD",
      cases=["TC-127", "TC-122"], rep=(2, 2),
      note="R-023 / R-083 (PM room board: output fixed at 9:16 for every feature). Two Micro Cinema reels: 1244 × 1660 and 1176 × 1760 (ffprobe), ≈ 3:4; the Save & Share preview box is 3:4. Creative (1080 × 1920) and Selfie Shake (720 × 1280) are 9:16.",
      short="Micro Cinema reel is 1244 × 1660 (3:4), not 9:16",
      steps=MC + ["Tap Generate", "Wait for the reel to finish", "Tap the Micro Cinema card", "Tap Save"],
      res="The saved file is 1244 × 1660 (3:4).",
      res_zh="Micro Cinema 輸出為 3:4，非 9:16。",
      exp="The reel is 9:16 in pixels.",
      exp_zh="輸出應為 9:16。",
      links=[P_ROOM], dev=S23,
      imgs=[("TC-127-open", "preview_3_4", None), ("TC-127-save", "saved", None)], log=None, rel=[]),
 dict(iss="ISS-CR-28", title="After 「Create More」 a Micro Cinema result download timed out: ⚠ Retry, no notification", cls="Functional", sev=3, owner="RD",
      cases=["TC-122"], rep=(1, 1),
      note="R-113 (KP-083: after Create More a new generation runs normally). From the room opened by 「Create More」, Micro Cinema (48 charged, 698 → 650): server Done at 15:41:28, then `downloadVideo Exception: java.net.SocketTimeoutException: timeout` → `DOWNLOAD_FAILED`, status DownloadFail; the card became ⚠ 「Retry」, no notification, Wi-Fi up. One Retry downloaded it in 5 s at no charge. Seen once; whether Create More or a network stall causes it is not known (the first Micro Cinema from a normal room downloaded fine).",
      short="「Create More」 Micro Cinema: result download times out, ⚠ Retry, no notification",
      steps=ROOM + ["Tap the history icon", "Tap a finished reel", "Tap Create More", "Tap the Micro Cinema card in the first section", "Tap Use Template", "Tap 1 photo", "Tap Next", "Tap Generate", "Wait 15 minutes"],
      res="The card turns ⚠ 「Retry」 with no notification; the log shows the result download timing out.",
      res_zh="Create More 後生成完成但下載逾時，卡片變為 Retry 且沒有通知。",
      exp="The job finishes normally: the reel downloads, the card shows it and the notification arrives.",
      exp_zh="應正常完成並通知。",
      links=[P_ART], dev=S23,
      imgs=[("TC-122-artwork2", "retry_card", None), ("TC-122-done", "after_retry", None)],
      log=("Create More job download failure", [("Generate 15:27:21", "15:27:20", "15:27:30"), ("Download failed, Retry", "15:41:00", "15:43:10")]), rel=[]),
 dict(iss="ISS-CR-29", title="Activity re-creation drops the confirm page back to the room", cls="Functional", sev=3, owner="RD",
      cases=["TC-116"], rep=(2, 2),
      note="R-112 (KP-097: after Activity re-creation the confirm page keeps its photos, order and count; PM confirm frame). With Developer options 「Don’t keep activities」 ON: back from Home on the confirm page re-creates AICineStoryActivity on the room (photos, order and count lost); opening the picker destroys it too, so 「Next」 lands on the room and the confirm page cannot be reached at all. No crash. A system theme switch on a Preview also re-created the page on the room (TC-146).",
      short="「Don’t keep activities」: confirm page lost, 「Next」 lands on the room",
      steps=["Turn on Developer options, Don’t keep activities"] + SCF7 + ["Press Home", "Open PhotoDirector from Recents"],
      res="The Reel Creator room shows instead of the confirm page; picks and order are lost.",
      res_zh="Activity 重建後回到房間，確認頁的照片與順序遺失。",
      exp="The confirm page comes back with the same photos, order and count.",
      exp_zh="應回到原確認頁並保留照片、順序與張數。",
      links=[P_CONF], dev=S23,
      imgs=[("TC-116-before", "confirm_before", None), ("TC-116-after", "room_after", None), ("TC-116-next-room", "next_lands_room", None)],
      log=("Activity re-created", [("Don't keep activities ON", "15:10:00", "15:18:30")]), rel=[]),
]

BLOCKED_UP = {"TC-077": 16, "TC-078": 16, "TC-140": 16, "TC-109": 16, "TC-079": 16, "TC-080": 16, "TC-081": 16, "TC-082": 16}

OBS_NOT = [
 ("O-1", "Pixel at R1-a setup: Production + subscriber on; Test Server Free showed 0 credits (new UUID).", "Setup state."),
 ("O-2", "Device switch to the S23 from TC-008.", "Setup."),
 ("O-3", "`pm clear` keeps the Test Server credit UUID and balance (contradicts KP-133).", "Test setup; knowledge corrected (KP-136)."),
 ("O-4", "Creative Previews lack description / tips; AI Transition plays no demo.", "In ISS-CR-06 / -07."),
 ("O-5", "First 「Continue」 on the Edit Room jump dialog did nothing; second worked.", "Seen once (1/2), not reproduced."),
 ("O-6", "Picker content check marks rejects with one 「!」 and no message; two ordinary photos flagged CELEBRITY.", "No spec wording (Q-11); celebrity flag not verifiable."),
 ("O-7", "Drags taken as taps; picker keeps scroll position.", "Test-tool handling."),
 ("O-8", "Imported photos lose their tick; no 「+N」; no red tray text.", "ISS-CR-11 / -12 / -13."),
 ("O-9", "First 「Next」 took ≈ 2.5 min; later 1–46 s. Flat prices; Import prompt only after a Next in the same launch.", "Spinner seen once; prices in ISS-CR-18 / -19."),
 ("O-10", "Credit Shop showed 52 after the 1000 top-up until reopened.", "Credit Shop, not this feature; listed in report.md."),
 ("O-11", "R1-f jobs, upload while picking, stale pages, lost refund.", "ISS-CR-23 / -24 / -25."),
 ("O-12", "R1-g jobs, stale cards, re-creation, large photos rejected.", "ISS-CR-24 / -27 / -28 / -29; 6000 px rejection is the spec's 4096 px limit."),
 ("O-13", "Phone used outside the run 16:26–19:11 (subscriber on, AI Background, three crashes 17:28–17:37).", "Not from a casebook row: not drafted (report.md)."),
]
NOT_RAISED_ROWS = {}

KEEP = re.compile(r"totalRemain=|updatePackItems column|longTask retry|downloadVideo Exception|doDownloadResult|Unable to resolve host|"
                  r"Msg=Tap to see|actionUrl:phd|getCreditHistory|VRI\[AICineStoryActivity\]@\w+: (dispatchDetachedFromWindow|setView)", re.I)
DROP = re.compile(r"memberToken|access_?token|authorization|bearer|signature=|purchaseToken|creditSystemUUID|uuid|System\.err", re.I)


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
            ts = f"{parts[0]} {parts[1]}"
            if "totalRemain=" in line and "getMemberCreditRemain" in line:
                m = re.search(r"totalRemain=(\d+)", line)
                if not m or m.group(1) == last:
                    continue
                last = m.group(1)
                line = f"{ts} CreditSystem: totalRemain={last}"
            elif "getCreditHistory" in line:
                m = re.search(r"RecordItem\(creditUsage=(-?\d+), featureId=(\w+)", line)
                if not m:
                    continue
                line = f"{ts} CreditHistory: newest record creditUsage={m.group(1)}, featureId={m.group(2)}"
            elif "Msg=Tap to see" in line and "FcmFirebaseMessagingService" not in line:
                continue
            elif "Msg=Tap to see" in line:
                m = re.search(r"Msg=([^,]+), Nid=\d+, Link=(\S+?), Title=([^,}]+)", line)
                line = f"{ts} FcmFirebaseMessagingService: notification Title={m.group(3)} Msg={m.group(1)} Link={m.group(2)}" if m else line
            else:
                line = re.sub(r"^(\S+ \S+) +\d+ +\d+ [VDIWE] ", r"\1 ", line.rstrip())
                line = re.sub(r"(VRI\[AICineStoryActivity\]@\w+: setView).*", r"\1 (new window)", line)
            line = re.sub(r"(https?://[^\s'\"?]+)\?\S*", r"\1?…", line)
            if line not in got:
                got.append(line[:300])
    return sorted(got, key=lambda l: l[:23])


def excerpt(n, iss, title, secs):
    L = [f"# {iss} {title}", f"# PhotoDirector Android {V} ({B}), Samsung SM-S9110 / Android 16, logcat of the app captured by the casebook run",
         "# Lines about the job, its status, credits (balance shown only when it changes) and notifications; tokens and IDs dropped.", ""]
    for label, t0, t1 in secs:
        got = log_lines(t0, t1)
        if not got:
            sys.exit(f"empty log window {label} {t0}-{t1}")
        L.append(f"## {label} ({DAY} {t0}–{t1})")
        L.extend(got)
        L.append("")
    txt = "\n".join(L)
    if re.search(r"eyJ[A-Za-z0-9_-]{10,}|Bearer |ya29\.|memberToken|purchaseToken", txt):
        sys.exit(f"token-like text in {iss} log")
    os.makedirs(f"{OUT}/logs", exist_ok=True)
    path = f"{OUT}/logs/{V}_cr{n:02d}_log.txt"
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
    obs = re.findall(r"\*\*(O-\d+)\b|^## (O-\d+)", open(f"{RUN}/observations.md", encoding="utf-8").read(), re.M)
    obs = sorted({a or b for a, b in obs}, key=lambda x: int(x[2:]))
    MAP = {}
    for n, e in enumerate(E, 1):
        for c in e["cases"]:
            MAP.setdefault(c, []).append(f"{n}. {e['iss']}")
    for k, _, _ in OBS_NOT:
        MAP.setdefault(k, ["not raised"])
    missing = [k for k in fails + obs if k not in MAP]
    extra = [k for k in MAP if k not in fails and k not in obs]
    if missing or extra:
        sys.exit(f"reconciliation incomplete: missing {missing}, extra {extra}")
    for e in E:
        for c in e["cases"]:
            if c not in fails:
                sys.exit(f"{e['iss']} cites {c}, which is not a Fail")

    img_root = f"{OUT}/{NAME}_images"
    if os.path.isdir(img_root):
        shutil.rmtree(img_root)
    os.makedirs(img_root)
    L = []
    w = L.append
    w(f"# Reel Creator / Creative Reel (Android) — eBug drafts, round R1 (table v4), PhotoDirector {V} build {B}")
    w("")
    w(f"**Source:** spec-casebook run `library/phd/creative-reel/android/runs/2026-11-17-r1/` — phase R1 of draft `drafts/20261117-150251` (table v4, {len(rows)} cases), 2026-11-18 08:48 → 15:45, TC-001 – TC-007 on Google Pixel 8a / Android 16, the rest on Samsung Galaxy S23 (SM-S9110) / Android 16, Appium / UiAutomator2, Test Server, Free. Tally: " + ", ".join(f"{v} {k}" for k, v in sorted(tally.items())) + ". TC-072 / TC-073 (R1-h) are Not run yet.")
    w("")
    w("**Status:** nothing filed, uploaded or commented. TR261113-0038 (build 20.19.0.v202611132003, R4) names the build tested (versionCode 90201901). ECL product 「PhotoDirector Mobile for Android」. Creator WILLY_WU, [AIAgent], API — from the batch-editing batch on the same TR (no filed batch for this feature yet): confirm.")
    w("")
    w("Rules: reviewer rules 2026-10-21 — one action per Repro step, a Spec Link on every entry (URL on its own line), at least one image per entry, the logcat excerpt on every failure / charge entry, no video. PM decisions are filed to PM (UX → `[AIAgent][UX]`, text `[AIAgent][UI]`, behaviour Functional); text and layout `[AIAgent][UI]`, RD when the Design / PM states it; the rest `[AIAgent]` Functional, RD. Spec basis per entry against PM page 7238:8623 (section spec) and Design page 933:4528 (section Design 976:11727); domain rules (KP-…) named as such. Creative rows ran on stand-in templates (no 「Top 5 of My Year」 on Test Server, ISS-CR-06).")
    w("")
    w(f"**What is drafted:** {len(E)} new entries (ISS-CR-01…{len(E):02d}), of which {sum(1 for e in E if e['owner'] == 'PM')} ask PM for a decision. Dedupe per OS: see dedupe.txt.")
    w("")
    w("Legend — Class: Functional / UI / UX · Severity: S1 critical and blocking only, S2 important, S3 moderate, S4 minor · Owner: RD / PM.")
    w("")
    for n, e in enumerate(E, 1):
        folder = f"{n:02d}_{e['iss']}"
        os.makedirs(f"{img_root}/{folder}")
        names = []
        for png, slug, box in e["imgs"]:
            src = f"{RUN}/screenshots/{png}.png"
            if not os.path.exists(src):
                sys.exit(f"missing screenshot {src}")
            name = f"{V}_cr{n:02d}_{slug}.jpg"
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
        w(f"## {n}. {e['iss']} — {e['title']}  ·  Class: {e['cls']}  ·  Severity: S{e['sev']}  ·  Owner: {e['owner']}")
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
        w(""); w("Note:"); w(e["dev"])
        for l in e["links"]:
            w(l)
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
    w(f"| Blocked ({len(blocked)}) | " + ", ".join(f"{v} {k}" for k, v in sorted(bd.items())) + " | 8 deeplink rows (no URLs, Q-15); 8 rows behind ISS-CR-16 (no Text Language bar): " + ", ".join(BLOCKED_UP) + ". |")
    w("")
    w("# Reconciliation against the run")
    w("")
    nq = sum(1 for f in fails if disp[f] == "question")
    w(f"{len(fails)} Fail ({len(fails) - nq} defect, {nq} question), {len(blocked)} Blocked, {tally.get('Not run', 0)} Not run (TC-072, TC-073), {len(obs)} observations (O-1 … O-{len(obs)}).")
    w("")
    w("| Item | Result | Disposition | Became |")
    w("|---|---|---|---|")
    for k in fails:
        w(f"| {k} | Fail | {disp[k]} | {'; '.join(MAP[k])} |")
    for k in obs:
        w(f"| {k} | observation | — | {'; '.join(MAP[k])} |")
    w("")
    w("Filing order by severity: " + ", ".join(f"**{i}**" for s in (1, 2, 3, 4) for i, e in enumerate(E, 1) if e["sev"] == s) + ". Nothing is filed until the review page's decisions come back.")
    w("")
    open(f"{OUT}/{NAME}.md", "w", encoding="utf-8").write("\n".join(L))
    json.dump({e["iss"]: {"cases": e["cases"], "why": e["title"]} for e in E}, open(f"{OUT}/entries.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"wrote {len(E)} entries → {OUT}/{NAME}.md")


if __name__ == "__main__":
    main()
