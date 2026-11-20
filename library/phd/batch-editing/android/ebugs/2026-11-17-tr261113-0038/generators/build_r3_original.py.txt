#!/usr/bin/env python3
"""Build the Batch Editing Android eBug draft batch for run 2026-11-13-r3 (phase R3, table v7, full run) on
20.19.0.v202611111946 (90201900, SR PHA261029-01, TR261111-0042).

Writes ../20261113_eBug_drafts_Batch-Edit-R3_20.19.0.md and the sibling _images/ folder (one NN_ISS-ID folder per
entry, red-boxed JPEGs named 20.19.0_<slug>.jpg). Nothing is filed. Every Fail row of results.csv is mapped to an
entry or to dedupe.txt, and every observation O-n is mapped; the script stops when one is missing.

    python -I library/phd/batch-editing/android/ebugs/2026-11-13-r3/generators/build.py
"""
import csv, os, re, shutil, sys

from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(OUT))                      # library/phd/batch-editing/android
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(ROOT))))
RUN = f"{ROOT}/runs/2026-11-13-r3"
SHOTS = f"{RUN}/screenshots"
NAME = "20261113_eBug_drafts_Batch-Edit-R3_20.19.0"
V, B = "20.19.0", "v202611111946 (90201900)"
PRE = f"PHD-A {V} - [AIAgent]"
DEVICE = "Device: Samsung Galaxy S23 (SM-S9110) / Android 16"
PM_URL = "https://www.figma.com/design/iWlQTjlmfykHfmlNvg9J4p/Batch-Editing?node-id="
DS_URL = "https://www.figma.com/design/qZXJfrM5gb5g4tFoCIS1YU/Batch-Edit?node-id="
S3_PDF = "Section 3 · 美圖 Apply to all 實測.pdf"


def pm(board, what, node):
    return f"Spec Link: Batch Editing PM Figma, {board} board ({what}) -\n{PM_URL}{node}"


def ds(frame, what, node):
    return f"Spec Link: Batch Edit Design Figma, {frame} frame ({what}) -\n{DS_URL}{node}"


def pdf(board, what):
    return f"Spec Link: Batch Edit PM spec ({S3_PDF}), {board} board ({what}) - no Figma URL for this PDF"


def steps(*s):
    return "\n".join(f"{i}. {x}" for i, x in enumerate(s, 1))


START = ("Launch the APP", "Tap Edit on the Launcher", "Tap Batch", "Select 12 photos", "Tap Next")
START4 = ("Launch the APP", "Tap Edit on the Launcher", "Tap Batch",
          "Select 4 photos (the last one 2730 x 1535, 16:9)", "Tap Next")
ALL = (840, 100, 1060, 225)          # 「All」 capsule, top right
LABEL = (330, 100, 760, 215)         # 「W x H」 size label, top middle
DIALOG = (70, 960, 1010, 1335)       # 「Discard changes?」 dialog

# Fail rows that repeat an open or resolved Android ticket: dedupe.txt only (dedupe per OS, overlay rule 7).
DEDUPE = {
    "TC-012": "PHA262026P0061 (Assigned)",
    "TC-060": "PHA262026P0060 (RDResolved)",
    "TC-110": "PHA262026P0057 (RDResolved)",
    "TC-144": "PHA262026P0058 (RDResolved)",
    "TC-145": "PHA262026P0059 (RDResolved)",
}

E = [
 dict(iss="ISS-BEA-12", cls="Functional", sev=3, owner="RD", rep="2/2", cases=["TC-162", "TC-164"],
      title="「All」 stays enabled on a photo with no change of its own while another photo has an unapplied change",
      short=f"{PRE} Batch_Editing: 「All」 stays enabled on a photo with no change of its own after switching photos",
      steps=steps(*START, "Tap Adjustments", "Drag the Exposure slider to 0.6", "Tap photo 2's thumbnail",
                  "Check 「All」 at the top right"),
      result="On photo 2 (Exposure 0, no change of its own) 「All」 stays enabled; it follows photo 1's unapplied change.",
      result_zh="切到沒有任何修改的第 2 張時，All 仍為可按，跟著第 1 張未套用的修改走。",
      expect="On switching photos 「All」 is set by that photo's own unapplied changes: disabled on photo 2.",
      expect_zh="切換照片時 All 依該張自己的未套用修改決定：第 2 張沒有修改，All 應為停用。",
      notes=["Related: the same in the Crop & Rotate room (3:2 on photo 1, then photo 2)"],
      links=[pm("pm-ui-3", "Batch Edit Room · Crop & Rotate / Adjustment, 【NEW】 Apply to all normal / disabled states, DR-04: 切換照片依該張", "16-13767")],
      images=[("tc164-3-p2.png", "adjust_photo2_no_change_all_enabled", ALL),
              ("TC-162-p2.png", "crop_photo2_no_change_all_enabled", ALL)],
      qa="Carried from R2's unfiled ISS-BEA-12, narrowed to the part that still fails on the TR261111-0042 build. Fixed on this build (Pass in R3): 「All」 greyed on entering (TC-153, TC-164 step 1), after the apply with no toast on a disabled tap (TC-042, TC-075), after Redo (TC-063, TC-165) and after a size-only change (TC-163). Still failing: on a photo with no change of its own, while another photo has an unapplied change, 「All」 stays normal — white icon and text, `els` batchApplyToAllBtn with no `disabled` flag (TC-164 step 3 Adjustment, photo 1 Exposure 「0.6」 by thumb drag; TC-162 Crop & Rotate, photo 1 3:2 「910 x 605」, photo 2 「1067 x 1600」). Back on photo 1 it is normal, as expected. R-234 (PM Figma DR-04 【NEW】 「切換照片依該張」). Spec basis checked: the 【NEW】 list on pm-ui-3 is the decided rule (Q-16 answered, REQ-011); no newer frame draws otherwise. Not in PHA262026P0057–P0061."),
 dict(iss="ISS-BEA-14", cls="UX", sev=3, owner="PM", rep="2/2", cases=["TC-062", "TC-076"],
      title="PM decision: one Undo after an edit + 「All」 reverts the 11 other photos but keeps the current photo's own edit",
      short=f"{PRE}[UX] Batch_Editing: One Undo after an edit and 「All」 keeps the current photo's own edit",
      steps=steps(*START, "Tap Crop & Rotate", "Tap 3:2", "Tap All", "Tap Undo", "Check photo 1 and photo 2"),
      result="One Undo reverts the 11 other photos only; photo 1 keeps 3:2 (「910 x 605」) until a 2nd Undo.",
      result_zh="一次 Undo 只還原其他 11 張，目前這張保留 3:2，需再按一次。",
      expect="PM to decide whether one Undo also reverts the current photo's own edit (all 12 together) or not.",
      expect_zh="請 PM 決定一次 Undo 是否連目前這張的修改一起還原（12 張同時）。",
      notes=["Related: the same in the Adjustment room (Exposure, then All, then Undo)"],
      links=[pm("pm-ui-3", "Batch Edit Room · Crop & Rotate / Adjustment · applied, DR-05b", "16-13767")],
      images=[("TC-062-undo1.png", "crop_undo1_photo1_keeps_3x2", LABEL),
              ("tc076-1-undo1.png", "adjust_undo_photo1_keeps_exposure", (20, 1540, 345, 1710))],
      qa="Carried from R2's unfiled ISS-BEA-14 (R1 held it as a PM question); same on the TR261111-0042 build on the S23. Crop TC-062: 3:2 + 「All」 (「Applied to 11 photos」), one Undo: photo 2 「1067 x 1600」 and photo 4 「1600 x 1066」 back, photo 1 still 「910 x 605」, Undo still enabled. Adjustment TC-076: Exposure 「0.6」 + 「All」, one Undo (「Undo: Apply to all」): photos 2–6 back to their entry values, photo 1 keeps 「0.6」. R-087 / R-105 say only that Apply to all is one step; R-099 makes a single edit that photo's own step, so the app may be intended: an open question, filed to PM (user, 2026-11-11), Type UX (how Undo feels). R2's empty first Undo from a no-change 「All」 is gone on this build. The TC-076 image shows photo 1 (selected, still bright) beside photo 2 (back to its original)."),
 dict(iss="ISS-BEA-15", cls="UX", sev=3, owner="PM", rep="3/3", cases=["TC-049", "TC-057", "TC-058"],
      title="PM decision: Crop & Rotate sizes a large photo from a 2560 px copy and accepts 147 px, not Section 3's original-size range",
      short=f"{PRE}[UX] Batch_Editing: Crop sizes use a 2560 px copy and a 147 px minimum, not Section 3's range",
      steps=steps(*START4, "Tap Crop & Rotate", "Tap photo 4's thumbnail", "Check the size label",
                  "Tap the pencil next to the size", "Tap the link icon", "Enter 237 in Width", "Enter 237 in Height",
                  "Tap OK", "Check the size label"),
      result="Photo 4 (2730 x 1535) reads 「2560 x 1439」, its 3:4 box 「1075 x 1435」; 237 x 237 is accepted (minimum 147).",
      result_zh="2730x1535 的照片顯示為 2560x1439，3:4 框 1075x1435；237x237 可接受。",
      expect="PM to decide the range: Section 3 gives 238 px up to the photo's own size (3:4 box 1151 x 1535).",
      expect_zh="請 PM 決定範圍：Section 3 結論為 238 px 到照片原尺寸（3:4 框 1151 x 1535）。",
      notes=["Related: the out-of-range toast reads 「Width should be between 147 and 2560. Please try again.」 (3000 x 3000 refused)",
             "Related: PHA262026P0060 (Square on this photo saves 1434 x 1435)"],
      links=[pdf("meitu-conclusion (✅ 結論: PhD crop · Apply to all rules) and meitu-cases C12",
                 "238 px up to the photo's own width / height; box sizes from each original"),
             pm("pm-ui-3", "Batch Edit Room · Crop & Rotate · default, size label and pencil", "16-14279")],
      images=[("tc049-p4.png", "crop_photo4_3x4_1075x1435", LABEL),
              ("tc058-after.png", "crop_custom_237x237_accepted", LABEL),
              ("tc057-toast.png", "crop_custom_toast_147_2560", (80, 1000, 1010, 1175))],
      qa="Held as a PM question in R1 (O-5, O-7) and never filed; same on the TR261111-0042 build. Stand-in ④ (2730 × 1535, 16:9) is held in the Crop room as 「2560 x 1439」 (a 2560 px long-side cap): its 3:4 box reads 「1075 x 1435」 (TC-049; the position rule holds), the Custom resolution dialog refuses 3000 × 3000 with 「Width should be between 147 and 2560. Please try again.」 (TC-057) and accepts 237 × 237 (TC-058, minimum 147). Section 3's 「✅ 結論」 (R-066, R-060) computes from the original: 238 px up to the photo's own width / height, 3:4 box 1151 × 1535. Whether PhD keeps the 2560 cap and the 147 minimum is a product decision: filed to PM (open questions to PM, user 2026-11-11), Type UX. The toast copy itself is Q-6, ISS-BEA-16. The saved Square 1434 × 1435 is PHA262026P0060 (TC-060, deduped)."),
 dict(iss="ISS-BEA-16", cls="UI", sev=3, owner="PM", rep="1/1", cases=["TC-057"],
      title="PM decision: the Custom resolution out-of-range toast names only the width, and PhD's copy is undecided (Q-6)",
      short=f"{PRE}[UI] Batch_Editing: Custom resolution out-of-range toast names only the width",
      steps=steps(*START4, "Tap Crop & Rotate", "Tap photo 4's thumbnail", "Tap the pencil next to the size",
                  "Tap the link icon", "Enter 3000 in Width", "Enter 3000 in Height", "Tap OK", "Check the toast"),
      result="Toast 「Width should be between 147 and 2560. Please try again.」; the height (also out of range) is not named.",
      result_zh="提示只寫 Width 的範圍，高度同樣超出卻沒提到。",
      expect="PM to decide the toast copy for width and height (Meitu: 「Width and height exceed the range」, range under the field).",
      expect_zh="請 PM 決定寬高超出範圍時的提示文案（Q-6）。",
      notes=["Related: ISS-BEA-15 (the range itself)"],
      links=[pdf("meitu-cases C12", "Meitu toast 「Width and height exceed the range」; PhD copy open, Q-6")],
      images=[("tc057-toast.png", "crop_custom_toast_width_only", (80, 1000, 1010, 1175))],
      qa="Q-6 (PhD toast copy for an out-of-range pixel value) is still open in table v7; Section 3 quotes only Meitu's 「Width and height exceed the range」. The app names only the width although both values (3000 × 3000, link off) are out of range. Text the spec has not decided → PM, Class UI (text rule, user 2026-11-11). Not answered by any ruling or ticket (PHA262026P0061 is the 21st-photo toast)."),
 dict(iss="ISS-BEA-17", cls="UX", sev=3, owner="PM", rep="2/2", cases=["TC-100", "TC-142"],
      title="PM decision: ✕ or Back after a finished batch AI Enhance asks 「Discard changes?」 instead of returning with the results kept",
      short=f"{PRE}[UX] Batch_Editing: ✕ after batch AI Enhance asks 「Discard changes?」, not keep the results",
      steps=steps(*START, "Tap AI Enhance", "Tap Enhance", "Tap Enhance in the dialog", "Wait until all 12 photos finish",
                  "Tap ✕", "Check the result"),
      result="「Discard changes?」 「All your existing changes will be lost.」 Keep / Discard opens; system Back does the same.",
      result_zh="✕ 或系統返回鍵開出「Discard changes?」對話框，而不是保留結果回到 Batch Edit Room。",
      expect="PM to decide: PM says ✕ returns to Batch Edit Room with the results kept; the Design draws this dialog (Q-19).",
      expect_zh="請 PM 決定：PM 寫 ✕ 保留結果返回，Design 畫了 Discard 對話框（Q-19）。",
      notes=["Related: a second system Back leaves the dialog open, as PHA262026P0059 (Discard dialog from Home)"],
      links=[pm("pm-ui-5", "Batch Edit Room · AI Enhance · result_success, R-130: ✕ returns with the results kept", "16-15034"),
             ds("Discard dialog", "Discard Dialog drawn over the AI Enhance page", "110-4532")],
      images=[("tc100-x.png", "enhance_done_x_discard_dialog", DIALOG),
              ("tc142-back2.png", "enhance_done_back_discard_dialog", DIALOG)],
      qa="Held as a PM question in R1 and never filed; same on the TR261111-0042 build. After the 12-photo batch finished, ✕ (TC-100) and system Back (TC-142) open 「Discard changes?」 「All your existing changes will be lost.」 「Keep」 / 「Discard」; 「Keep」 stays on AI Enhance with the results, only ✓ returns with them. R-130 (PM flow-ai-enhance) says ✕ returns to Batch Edit Room keeping the results; the Design draws the Discard Dialog over the AI Enhance page (Q-19, open). Design-first (user, 2026-11-13) would favour the dialog, but the Design frames carry no date (Q-12), so the order cannot be settled from the files: filed to PM, Type UX. The second Back not closing the dialog is the open-ticket behaviour of PHA262026P0059 (not drafted again)."),
 dict(iss="ISS-BEA-18", cls="UI", sev=3, owner="PM", rep="1/1", cases=["TC-128"],
      title="PM decision: Batch Save page title reads 「Saved 12 photos」 (PM) while the Design draws 「Save 12 photos」 (Q-20)",
      short=f"{PRE}[UI] Batch_Editing: Batch Save title 「Saved 12 photos」 differs from Design 「Save 12 photos」",
      steps=steps(*START, "Tap Save at the top right", "Check the page title"),
      result="The Batch Save page title reads 「Saved 12 photos」.",
      result_zh="批次儲存頁標題為「Saved 12 photos」。",
      expect="PM to decide the title: Design save2 draws 「Save 12 photos」, the PM board writes 「Saved 12 photos」 (Q-20).",
      expect_zh="請 PM 決定標題：Design 為 Save，PM 為 Saved（Q-20）。",
      notes=[],
      links=[ds("save2", "Batch Save page title 「Save 12 photos」", "57-6001"),
             pm("pm-ui-8", "Batch Save Page · saved, 「Saved 12 photos」, D1-07", "16-15383")],
      images=[("tc128-page.png", "save_page_title_saved_12", (20, 240, 420, 340))],
      qa="Held as a PM question in R1 (O-16) and never filed; same on this build. The two sheets disagree and the Design frames carry no date (Q-12), so the Design-first order (user, 2026-11-13) cannot be applied from the files; text whose spec source disagrees goes to PM, never Doc (user, 2026-11-11). Class UI."),
 dict(iss="ISS-BEA-19", cls="UX", sev=3, owner="PM", rep="2/2", cases=["TC-135"],
      title="PM decision: as a Free user the Batch Save page has no native ad card, while the single Save & Share page has one",
      short=f"{PRE}[UX] Batch_Editing: Free user Batch Save page has no native ad card, unlike single save",
      steps=steps("Launch the APP as a Free user", "Tap Edit on the Launcher", "Tap Batch", "Select 5 photos", "Tap Next",
                  "Tap Save at the top right", "Close the ad or IAP page", "Check the Batch Save page"),
      result="The Batch Save page shows the 5 photos and 「Edit Next Batch」 only; no native ad card (the single save page has one).",
      result_zh="批次儲存頁只有照片與 Edit Next Batch，沒有原生廣告卡；單張儲存頁的 Share to 下方有。",
      expect="PM to decide whether the Batch Save page carries the save page's native ad (R-158: ads appear as usual).",
      expect_zh="請 PM 決定批次儲存頁是否要放單張儲存頁的原生廣告（R-158：廣告照常出現）。",
      notes=["Related: interstitial ads and the Premium IAP flyer do appear after batch saves"],
      links=[pm("pm-ui-8", "Batch Save Page · saved, R-158: IAP flyers and ads appear as usual; no ad slot drawn", "16-15383")],
      images=[("tc135-b-savepage.png", "batch_save_page_no_ad", (20, 1150, 1060, 2050)),
              ("tc135-single-2.png", "single_save_page_native_ad", (60, 2030, 1030, 2230))],
      qa="Held as a PM question in R1 (O-19) and never filed; same on this build. Free tier (debug 「Set to subscriber」 off): 1st batch save of 5 → interstitial (Dance AI) → 「Saved 5 photos」; 2nd → Premium IAP flyer → 「Saved 5 photos」; neither Batch Save page has an ad_container. Single save (Edit › Single): Rate Us, then 「Save & Share」 with a native AdMob card under 「Share to」 (savePageAdMobNativeContentAdView). R-158 says ads appear as usual; neither PM nor the Design draws an ad slot on the Batch Save page: filed to PM, Type UX (monetisation placement)."),
]

OBS = [
 ("O-1", "Help (i) hidden on the Adjustment Details tab (likely no tutorial for Details); not a row, not raised."),
 ("O-2", "No credit pill on the batch AI Enhance page (R-113 draws none; the Design's pill sits on the Discard frame, Q-19, ISS-BEA-17); not raised."),
 ("O-3", "One photo of a 7-photo retry failed with SocketTimeoutException on working Wi-Fi, as R1 O-13; the next retry finished it. Watch, not raised."),
 ("O-4", "Picker tray tile for selection #10 showed another picture once while the grid and the room were right; display-only, seen once, not raised."),
]


def boxed(src, dst, box):
    im = Image.open(f"{SHOTS}/{src}").convert("RGB")
    if box:
        d = ImageDraw.Draw(im)
        x0, y0, x1, y1 = box
        x1, y1 = min(x1, im.size[0] - 1), min(y1, im.size[1] - 1)
        for k in range(6):
            d.rectangle([x0 + k, y0 + k, x1 - k, y1 - k], outline=(255, 0, 0))
    im.save(dst, "JPEG", quality=85)


def main():
    results = list(csv.DictReader(open(f"{RUN}/results.csv", encoding="utf-8-sig")))
    fails = {r["ID"] for r in results if r["Result"] == "Fail"}
    mapped = {c for e in E for c in e["cases"]} | set(DEDUPE)
    if fails - mapped:
        sys.exit(f"unmapped Fail rows: {sorted(fails - mapped)}")
    obs = set(re.findall(r"^- (O-\d+)", open(f"{RUN}/observations.md", encoding="utf-8").read(), re.M))
    if obs - {o for o, _ in OBS}:
        sys.exit(f"unmapped observations: {sorted(obs - {o for o, _ in OBS})}")
    tally = {}
    for r in results:
        tally[r["Result"]] = tally.get(r["Result"], 0) + 1
    nq = sum(1 for e in E if e["owner"] == "PM")

    imgroot = f"{OUT}/{NAME}_images"
    shutil.rmtree(imgroot, ignore_errors=True)
    md = [f"# Batch Editing (Android) — eBug drafts, run R3 (table v7, full run), PhotoDirector {V} build {B}\n",
          f"**Source:** spec-casebook run `library/phd/batch-editing/android/runs/2026-11-13-r3/` — phase R3 of draft "
          f"`drafts/20261112-150000` (approved table v7, all 170 rows), 2026-11-13 on Samsung Galaxy S23 (SM-S9110, "
          f"Android 16) through Appium / UiAutomator2, Test Server, Premium through the debug switch (Free for R3-g). "
          f"Build 20.19.0.v202611111946, SR PHA261029-01, TR261111-0042. Tally: {tally.get('Pass', 0)} Pass, "
          f"{tally.get('Fail', 0)} Fail, {tally.get('Blocked', 0)} Blocked, {tally.get('Not run', 0)} Not run.\n",
          "**Status:** nothing filed, uploaded or commented. Filing defaults: Creator WILLY_WU, [AIAgent], API from the "
          "newest filed batch (2026-11-10-r1, `ebug-defaults.ts`); TRCode TR261111-0042 (the build these findings were "
          "verified on; the 2026-11-10-r1 batch was on TR261106-0051). All for the reviewer to confirm. Dedupe is "
          "read-only, Android pool only (dedupe per OS): see `dedupe.txt`.\n",
          "Rules: reviewer rules — one action per Repro step, a Spec Link on every entry (URL on its own line), at least "
          "one image per entry, no video; no failure-related entry, so no log. RD defects are `[AIAgent]`; open "
          "questions the run cannot settle go to PM (BugBelong PM): `[AIAgent][UX]` for user-experience decisions "
          "(rule restored 2026-11-13), `[AIAgent][UI]` for undecided text (never Doc, user 2026-11-11). Feature name "
          "`Batch_Editing:` (REQ-008). Spec basis check (REQ-055) done per entry.\n",
          f"**What is drafted:** {len(E)} entries (ISS-BEA-12, 14…19; R2's ISS-BEA-12 and 14 were never filed and are "
          f"carried forward, ISS-BEA-13 is fixed on this build) from {len(fails) - len(DEDUPE)} Fail rows: 1 RD defect "
          f"(2 rows), {nq} PM decisions. {len(DEDUPE)} Fail rows repeat existing Android tickets and are only in "
          f"`dedupe.txt`.\n",
          "Legend — Class: Functional / UI / UX · Severity: S1 critical and blocking only, S2 important, S3 moderate · "
          "Owner: RD / PM.\n\n---\n"]
    for n, e in enumerate(E, 1):
        folder = f"{imgroot}/{n:02d}_{e['iss']}"
        os.makedirs(folder)
        tag = e["iss"].split("-")[-1].lower()
        cites = []
        for src, slug, box in e["images"]:
            fn = f"{V}_bea{tag}_{slug}.jpg"
            boxed(src, f"{folder}/{fn}", box)
            cites.append(fn)
        note = [DEVICE] + e["notes"] + e["links"] + ["<Claude Reviewed>"]
        desc = (f"Repro Steps:\n{e['steps']}\n\nResult:\n{e['result']}\n摘要：{e['result_zh']}\n"
                + " ".join("{" + c + "}" for c in cites)
                + f"\n\nExpect Result:\n{e['expect']}\n摘要：{e['expect_zh']}\n\nNote:\n" + "\n".join(note))
        if len(e["short"]) > 140:
            sys.exit(f"{e['iss']} short description {len(e['short'])} chars")
        md.append(f"## {n}. {e['iss']} — {e['title']}  ·  Class: {e['cls']}  ·  Severity: S{e['sev']}  ·  Owner: {e['owner']}\n")
        md.append(f"**Report step:** {', '.join(e['cases'])}  ·  **Reproduce:** {e['rep']}  ·  **Verified on:** {V}.{B}\n")
        md.append(f"> **QA note — not pasted into eBug.** {e['qa']}\n")
        md.append(f"**Short Description:**\n\n```\n{e['short']}\n```\n")
        md.append(f"**Description:**\n\n```\n{desc}\n```\n")
        md.append(f"**Images:** `{NAME}_images/{n:02d}_{e['iss']}/`\n\n---\n")
    md.append("## Deduped — repeats of existing Android tickets (not drafted; `dedupe.txt`)\n")
    md.append("| Case | Ticket |\n|---|---|")
    for c, t in DEDUPE.items():
        md.append(f"| {c} | {t} |")
    md.append("\n## Not raised (observations, for the record)\n")
    for o, t in OBS:
        md.append(f"- {o}: {t}")
    md.append("\n## Reconciliation against the run (Fail rows)\n")
    md.append("| Case | Result | Where |\n|---|---|---|")
    where = {}
    for n, e in enumerate(E, 1):
        for c in e["cases"]:
            where[c] = (where[c] + ", " if c in where else "") + f"F-{n} {e['iss']}"
    for c, t in DEDUPE.items():
        where[c] = f"dedupe.txt ({t})"
    for r in results:
        if r["Result"] == "Fail":
            md.append(f"| {r['ID']} | {r['Result']} {r['Disposition']} | {where.get(r['ID'], '—')} |")
    md.append("\nBlocked rows (no verdict, not drafted): " + ", ".join(
        f"{r['ID']} ({r['Disposition']})" for r in results if r["Result"] == "Blocked") + ".\n")
    open(f"{OUT}/{NAME}.md", "w", encoding="utf-8").write("\n".join(md))
    print(f"wrote {NAME}.md with {len(E)} entries")


if __name__ == "__main__":
    main()
