#!/usr/bin/env python3
"""Batch Editing Android: rebuild the approved R3 eBugs for the new build, plus the new Crop & Rotate crash.

Re-verification run 2026-11-17-verify-tr261113-0038 on PhotoDirector 20.19.0.v202611132003 (90201901, SR PHA261029-01,
TR261113-0038). Adapted from ../../2026-11-13-r3/generators/build.py (the R3 batch on v202611111946, TR261111-0042;
the original is kept beside this file as build_r3_original.py.txt). Only findings CONFIRMED on the new build are built;
Short Descriptions, Sev and Belong are the ones the user approved for R3 (decisions.md), ISS-BEA-20 is the new crash
the user set to Severity 1 (2026-11-17).

Writes ../20261117_eBug_drafts_Batch-Edit-TR261113-0038_20.19.0.md, ../upload/*.jpg (red-boxed), the crash log excerpt
and ../upload/bodies.json. Nothing is filed.

    PYTHONIOENCODING=utf-8 python -I library/phd/batch-editing/android/ebugs/2026-11-17-tr261113-0038/generators/build.py
"""
import json, os, shutil, sys

from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(OUT))                      # library/phd/batch-editing/android
RUN = f"{ROOT}/runs/2026-11-17-verify-tr261113-0038"
SHOTS = f"{RUN}/screenshots"
UPLOAD = f"{OUT}/upload"
NAME = "20261117_eBug_drafts_Batch-Edit-TR261113-0038_20.19.0"
FEATURE = "Batch-Edit-T38"
V, B = "20.19.0", "v202611132003 (90201901)"
TR = "TR261113-0038"
PRE = f"PHD-A {V} - [AIAgent]"
DEVICE = "Device: Samsung Galaxy S23 (SM-S9110) / Android 16"
BUILD_LINE = f"Build: {V}.v202611132003 (SR PHA261029-01)"
PM_URL = "https://www.figma.com/design/iWlQTjlmfykHfmlNvg9J4p/Batch-Editing?node-id="
S3_PDF = "Section 3 · 美圖 Apply to all 實測.pdf"
R3 = "R3 (v202611111946, TR261111-0042, run 2026-11-13-r3)"


def pm(board, what, node):
    return f"Spec Link: Batch Editing PM Figma, {board} board ({what}) -\n{PM_URL}{node}"


def pdf(board, what):
    return f"Spec Link: Batch Edit PM spec ({S3_PDF}), {board} board ({what}) - no Figma URL for this PDF"


def steps(*s):
    return "\n".join(f"{i}. {x}" for i, x in enumerate(s, 1))


START = ("Launch the APP", "Tap Edit on the Launcher", "Tap Batch", "Select 12 photos", "Tap Next")
ALL = (840, 100, 1060, 225)          # 「All」 capsule, top right
LABEL = (330, 100, 760, 215)         # 「W x H」 size label, top middle
TOAST = (80, 1780, 1000, 1965)       # toast above the ratio row

E = [
 dict(key="01", iss="ISS-BEA-12", cls="Functional", sev=3, owner="RD", rep="2/2", cases=["TC-162", "TC-164"],
      title="「All」 stays enabled on a photo with no change of its own while another photo has an unapplied change",
      short=f"{PRE} Batch_Editing: 「All」 stays enabled on a photo with no change of its own after switching photos",
      steps=steps(*START, "Tap Adjustments", "Drag the Exposure slider to 0.43", "Tap photo 2's thumbnail",
                  "Check 「All」 at the top right"),
      result="On photo 2 (Exposure 0, no change of its own) 「All」 stays enabled; it follows photo 1's unapplied change.",
      result_zh="切到沒有任何修改的第 2 張時，All 仍為可按，跟著第 1 張未套用的修改走。",
      expect="On switching photos 「All」 is set by that photo's own unapplied changes: disabled on photo 2.",
      expect_zh="切換照片時 All 依該張自己的未套用修改決定：第 2 張沒有修改，All 應為停用。",
      notes=["Related: the same in the Crop & Rotate room (Square on photo 1, then photo 2)"],
      links=[pm("pm-ui-3", "Batch Edit Room · Crop & Rotate / Adjustment, 【NEW】 Apply to all normal / disabled states, DR-04: 切換照片依該張", "16-13767")],
      images=[("tc164-3-p2.png", "adjust_photo2_no_change_all_enabled", ALL),
              ("TC-162-p2.png", "crop_photo2_no_change_all_enabled", ALL)],
      qa=f"Reproduced on v202611132003 (TR261113-0038), 2026-11-17, Premium, Test Server. TC-164: on entering 「All」 is greyed (expected); Exposure 「0.43」 by one thumb drag on photo 1 → 「All」 normal (expected); photo 2 and photo 3 (Exposure 「0」, no change of their own) → 「All」 stays normal, `els` batchApplyToAllBtn with no `disabled` flag (fails R-234); photo 1 again → normal (expected). TC-162: Square on photo 1 (「640 x 640」, no 「All」 tap) → photo 2 (「960 x 640」, Original) and photo 3 (「960 x 1280」, Original) keep 「All」 normal. Square instead of R3's 3:2 because photo 1 of this set is natively 3:2. Same as {R3}: TC-162 / TC-164 Fail there with 3:2 and Exposure 「0.6」 (R3 images 20.19.0_bea12_*.jpg)."),
 dict(key="02", iss="ISS-BEA-14", cls="UX", sev=3, owner="PM", rep="2/2", cases=["TC-062", "TC-076"],
      title="PM decision: one Undo after an edit + 「All」 reverts the 11 other photos but keeps the current photo's own edit",
      short=f"{PRE}[UX] Batch_Editing: One Undo after an edit and 「All」 keeps the current photo's own edit",
      steps=steps(*START, "Tap Crop & Rotate", "Tap Square", "Tap All", "Tap Undo", "Check the current photo",
                  "Tap another photo's thumbnail"),
      result="One Undo reverts the 11 other photos only; the current photo keeps Square (「960 x 960」) until a 2nd Undo.",
      result_zh="一次 Undo 只還原其他 11 張，目前這張保留 Square，需再按一次。",
      expect="PM to decide whether one Undo also reverts the current photo's own edit (all 12 together) or not.",
      expect_zh="請 PM 決定一次 Undo 是否連目前這張的修改一起還原（12 張同時）。",
      notes=["Related: the same in the Adjustment room (Exposure, then All, then Undo)"],
      links=[pm("pm-ui-3", "Batch Edit Room · Crop & Rotate / Adjustment · applied, DR-05b", "16-13767")],
      images=[("TC-062-undo1-p3.png", "crop_undo1_current_keeps_square", LABEL),
              ("TC-062-undo1-p1.png", "crop_undo1_other_photo_original", LABEL),
              ("tc076-undo1-p1.png", "adjust_undo_photo1_keeps_exposure", (20, 1450, 1060, 1775))],
      qa=f"Reproduced on v202611132003 (TR261113-0038), 2026-11-17. Crop TC-062: the room was on photo 3 (「960 x 1280」); Square (「960 x 960」) + 「All」, one Undo: photo 1 back to 「960 x 640」 Original and photo 4 「1280 x 851」 Original, photo 3 still 「960 x 960」 Square, Undo still enabled, 「All」 normal again. Adjustment TC-076: Exposure 「0.43」 + 「All」 (toast 「Applied to 11 photos」), one Undo (toast 「Undo: Apply to all」): photos 2–4 back to Exposure 「0」, photo 1 keeps 「0.43」, 「All」 normal again. Same as {R3} (TC-062 with 3:2, TC-076 with 「0.6」; R3 images 20.19.0_bea14_*.jpg). R-087 / R-105 say only that Apply to all is one step; R-099 makes a single edit that photo's own step: open question to PM, Type UX."),
 dict(key="03", iss="ISS-BEA-15", cls="UX", sev=3, owner="PM", rep="1/1", cases=["TC-049", "TC-057", "TC-058"],
      title="PM decision: Crop & Rotate sizes a large photo from a 2560 px copy and accepts 147 px, not Section 3's original-size range",
      short=f"{PRE}[UX] Batch_Editing: Crop sizes use a 2560 px copy and a 147 px minimum, not Section 3's range",
      steps=steps("Launch the APP", "Tap Edit on the Launcher", "Tap Batch",
                  "Select an 800 x 800 photo and a 1576 x 1970 photo (the 800 x 800 one first)", "Tap Next",
                  "Tap Crop & Rotate", "Tap the pencil next to the size", "Tap the link icon", "Enter 237 in Width",
                  "Enter 237 in Height", "Tap OK", "Check the size label"),
      result="237 x 237 is accepted (「237 x 237」); the range toast reads 50 to 800 for this photo, not 238 px upwards.",
      result_zh="237x237 可接受；此照片的範圍提示為 50 到 800，而非 238 px 起。",
      expect="PM to decide the range: Section 3 gives 238 px up to the photo's own size, computed from the original.",
      expect_zh="請 PM 決定範圍：Section 3 結論為 238 px 到照片原尺寸（依原圖計算）。",
      notes=["Related: on the TR261111-0042 build a 2730 x 1535 photo read 「2560 x 1439」 (3:4 box 「1075 x 1435」) and the toast read 「Width should be between 147 and 2560. Please try again.」; on this build that photo cannot be opened in Crop & Rotate (ISS-BEA-20, crash)"],
      links=[pdf("meitu-conclusion (✅ 結論: PhD crop · Apply to all rules) and meitu-cases C12",
                 "238 px up to the photo's own width / height; box sizes from each original"),
             pm("pm-ui-3", "Batch Edit Room · Crop & Rotate · default, size label and pencil", "16-14279")],
      images=[("tc058-after.png", "crop_custom_237x237_accepted", LABEL),
              ("tc057-toast.png", "crop_custom_toast_50_800", TOAST)],
      qa=f"Partly re-verified on v202611132003 (TR261113-0038), 2026-11-17. The minimum part still fails Section 3: on stand-in ③ (800 × 800) the Custom resolution dialog accepts 237 × 237 (label 「237 x 237」, no toast; TC-058) and 3000 × 3000 is refused with 「Width should be between 50 and 800. Please try again.」 (TC-057) — the minimum is 50 here (147 on the 2730 px photo in R3), never 238. The 2560 px copy (TC-049, stand-in ④ 2730 × 1535 read as 「2560 x 1439」, 3:4 box 「1075 x 1435」) could not be re-checked: Crop & Rotate crashes when it shows ④ or ① on this build (ISS-BEA-20). R3 evidence for that part: {R3}, images 20.19.0_bea15_*.jpg. Related: PHA262026P0060 (Square on a 2730 x 1535 photo saves 1434 x 1435). Short Description kept as approved; the reviewer may want to drop 「2560 px copy」 or wait for ISS-BEA-20's fix."),
 dict(key="04", iss="ISS-BEA-16", cls="UI", sev=3, owner="PM", rep="1/1", cases=["TC-057"],
      title="PM decision: the Custom resolution out-of-range toast names only the width, and PhD's copy is undecided (Q-6)",
      short=f"{PRE}[UI] Batch_Editing: Custom resolution out-of-range toast names only the width",
      steps=steps("Launch the APP", "Tap Edit on the Launcher", "Tap Batch",
                  "Select an 800 x 800 photo and a 1576 x 1970 photo (the 800 x 800 one first)", "Tap Next",
                  "Tap Crop & Rotate", "Tap the pencil next to the size", "Tap the link icon", "Enter 3000 in Width",
                  "Enter 3000 in Height", "Tap OK", "Check the toast"),
      result="Toast 「Width should be between 50 and 800. Please try again.」; the height (also out of range) is not named.",
      result_zh="提示只寫 Width 的範圍，高度同樣超出卻沒提到。",
      expect="PM to decide the toast copy for width and height (Meitu: 「Width and height exceed the range」, range under the field).",
      expect_zh="請 PM 決定寬高超出範圍時的提示文案（Q-6）。",
      notes=["Related: ISS-BEA-15 (the range itself)"],
      links=[pdf("meitu-cases C12", "Meitu toast 「Width and height exceed the range」; PhD copy open, Q-6")],
      images=[("tc057-toast.png", "crop_custom_toast_width_only", TOAST)],
      qa=f"Reproduced on v202611132003 (TR261113-0038), 2026-11-17, on stand-in ③ (800 × 800) because ④ (2730 × 1535) crashes Crop & Rotate on this build (ISS-BEA-20). Link off, 3000 × 3000, OK: refused, dialog stays, toast 「Width should be between 50 and 800. Please try again.」 (page source Toast node). In {R3} on ④ it read 「Width should be between 147 and 2560. Please try again.」 (image 20.19.0_bea16_crop_custom_toast_width_only.jpg). Q-6 still open; text the spec has not decided → PM, Class UI."),
 dict(key="07", iss="ISS-BEA-19", cls="UX", sev=3, owner="PM", rep="2/2", cases=["TC-135"],
      title="PM decision: as a Free user the Batch Save page has no native ad card, while the single Save & Share page has one",
      short=f"{PRE}[UX] Batch_Editing: Free user Batch Save page has no native ad card, unlike single save",
      steps=steps("Launch the APP as a Free user", "Tap Edit on the Launcher", "Tap Batch", "Select 5 photos", "Tap Next",
                  "Tap Save at the top right", "Close the ad or IAP page", "Check the Batch Save page"),
      result="The Batch Save page shows the 5 photos and 「Edit Next Batch」 only; no native ad card (the single save page has one).",
      result_zh="批次儲存頁只有照片與 Edit Next Batch，沒有原生廣告卡；單張儲存頁的 Share to 下方有。",
      expect="PM to decide whether the Batch Save page carries the save page's native ad (R-158: ads appear as usual).",
      expect_zh="請 PM 決定批次儲存頁是否要放單張儲存頁的原生廣告（R-158：廣告照常出現）。",
      notes=["Related: the Premium IAP flyer and the Rate Us dialog do appear after batch saves"],
      links=[pm("pm-ui-8", "Batch Save Page · saved, R-158: IAP flyers and ads appear as usual; no ad slot drawn", "16-15383")],
      images=[("tc135-b1-savepage.png", "batch_save_page_no_ad", (20, 1150, 1060, 2050)),
              ("tc135-single-2.png", "single_save_page_native_ad", (60, 1830, 1030, 2230))],
      qa=f"Reproduced on v202611132003 (TR261113-0038), 2026-11-17, Free tier (debug 「Set to subscriber」 off; Mine 「Upgrade to Premium!」). 1st batch save of 5 → 「PhotoDirector Premium」 IAP flyer (✕) → 「Saved 5 photos」 / 「Edit Next Batch」, no ad_container even after 10 s; 2nd batch save → 「Rate Us」 (Not Now) → 「Saved 5 photos」, no ad_container (DCIM/PhotoDirector 940 → 945 → 950). Positive control, single save (Edit › Single, Save): interstitial ad (Close) → 「Save & Share」 with a native AdMob card under 「Share to」 (ad_container / savePageAdMobNativeContentAdView, 「Ad Choices Icon」). Same as {R3} (images 20.19.0_bea19_*.jpg). Then back to Premium (「Hello VIP!」)."),
 dict(key="08", iss="ISS-BEA-20", cls="Functional", sev=1, owner="RD", rep="4/4", cases=["TC-049", "TC-057", "TC-058"],
      title="The app crashes when the Batch Crop & Rotate room shows a large photo (1706 x 2559 or 2730 x 1535)",
      short=f"{PRE} Batch_Editing: App crashes when Crop & Rotate shows a 2730 x 1535 or 1706 x 2559 photo",
      steps=steps("Launch the APP", "Tap Edit on the Launcher", "Tap Batch",
                  "Select a 2730 x 1535 photo and an 800 x 800 photo (the 2730 x 1535 one first)", "Tap Next",
                  "Tap Crop & Rotate"),
      result="PhotoDirector closes at once and the system shows 「Clear cache for PhotoDirector?」.",
      result_zh="點 Crop & Rotate 後 App 立即閃退（IllegalArgumentException）。",
      expect="The Crop & Rotate room opens on the photo and shows its size label; no crash.",
      expect_zh="Crop & Rotate 正常開啟並顯示照片與尺寸，不閃退。",
      notes=["Related: also when the room opens on a 1706 x 2559 photo, and when the room is open on the 800 x 800 photo and the 2730 x 1535 photo's thumbnail is tapped",
             "Related: the same photos opened without a crash on the TR261111-0042 build (v202611111946)"],
      links=[pm("pm-ui-3", "Batch Edit Room · Crop & Rotate · default, size label and pencil", "16-14279")],
      images=[("crash2-dialog.png", "crop_room_crash_clear_cache_dialog", (30, 1612, 1050, 2182)),
              ("s30-room4.png", "batch_room_before_crop_tap", (110, 2000, 340, 2215))],
      log=(f"{RUN}/logs/crash-excerpt-bca.txt", "crop_room_crash_log"),
      qa="New on v202611132003 (TR261113-0038), 2026-11-17, Premium, Test Server; 4 of 4 tries, logcat -b crash: (1) 10:06:20 — 4 Section 3 stand-ins ① 1706×2559, ② 1576×1970, ③ 800×800, ④ 2730×1535 in that order (Casebook album), Next, tap Crop & Rotate (room opens on ①) → crash, 「Cannot coerce value to an empty range: maximum 104.21999999999991 is less than minimum 104.21999999999997.」; (2) 10:07:05 — the same again after relaunch → same exception, 「Clear cache for PhotoDirector?」; (3) 10:08:07 — ④ then ③, tap Crop & Rotate (room opens on ④) → crash, 「maximum 310.83187499999997 is less than minimum 310.831875」; (4) 10:08:52 — ③ then ④, Crop & Rotate opens fine on ③ (「800 x 800」), tap ④'s thumbnail → same crash (310.83…). Stack: BatchCropRoomFragment.showPhoto → BatchCropRoomFragment.b0/n0 → crop.a.g → CropRotateImageView.o/C/g → kotlin coerceIn (floating-point min > max). Photos that opened fine: ③ 800×800 and the phone's 960×640 / 960×1280 / 1280×851 gallery photos. In R3 (v202611111946) the same four stand-ins opened in Crop & Rotate (TC-049/057/058 recorded sizes), so a regression on this build. Severity 1 set by the user (「這個crash要發S1」, 2026-11-17); log excerpt scanned, no tokens."),
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
    shutil.rmtree(UPLOAD, ignore_errors=True)
    os.makedirs(UPLOAD)
    md = [f"# Batch Editing (Android) — eBug drafts for {TR}, PhotoDirector {V} build {B}\n",
          f"**Source:** re-verification run `library/phd/batch-editing/android/runs/2026-11-17-verify-tr261113-0038/` "
          f"(verify.md) of the five R3 findings the user approved (`../2026-11-13-r3/decisions.md`), plus the new Crop & "
          f"Rotate crash. Samsung Galaxy S23 (SM-S9110, Android 16), Test Server, Premium by the debug switch (Free for TC-135).\n",
          "**Status:** nothing filed, uploaded or commented. Filing: Creator WILLY_WU, [AIAgent], API, TRCode "
          f"{TR}.\n\n---\n"]
    bodies = {}
    for e in E:
        tag = e["iss"].split("-")[-1].lower()
        cites, files = [], []
        for src, slug, box in e["images"]:
            fn = f"{V}_bea{tag}_{slug}.jpg"
            boxed(src, f"{UPLOAD}/{fn}", box)
            cites.append(fn)
            files.append(fn)
        if e.get("log"):
            src, slug = e["log"]
            fn = f"{V}_bea{tag}_{slug}.txt"
            shutil.copyfile(src, f"{UPLOAD}/{fn}")
            cites.append(fn)
            files.append(fn)
        note = [DEVICE] + e["notes"] + e["links"] + ["<Claude Reviewed>"]
        desc = (f"Repro Steps:\n{e['steps']}\n\nResult:\n{e['result']}\n摘要：{e['result_zh']}\n"
                + " ".join("{" + c + "}" for c in cites)
                + f"\n\nExpect Result:\n{e['expect']}\n摘要：{e['expect_zh']}\n\nNote:\n" + "\n".join(note))
        if len(e["short"]) > 140:
            sys.exit(f"{e['iss']} short description {len(e['short'])} chars")
        out, times = e["rep"].split("/")
        bodies[f"{FEATURE}-{e['key']}"] = dict(
            entry=int(e["key"]), iss=e["iss"], title=e["title"], feature=FEATURE, type=e["cls"], sev=e["sev"],
            belong=e["owner"], out=int(out), times=int(times), short=e["short"], desc=desc, files=files,
            images_dir=UPLOAD, qa_note=e["qa"], ux=e["cls"] == "UX", basis="")
        md.append(f"## {e['key']}. {e['iss']} — {e['title']}  ·  Class: {e['cls']}  ·  Severity: S{e['sev']}  ·  Owner: {e['owner']}\n")
        md.append(f"**Report step:** {', '.join(e['cases'])}  ·  **Reproduce:** {e['rep']}  ·  **Verified on:** {V}.{B}\n")
        md.append(f"> **QA note — not pasted into eBug.** {e['qa']}\n")
        md.append(f"**Short Description:**\n\n```\n{e['short']}\n```\n")
        md.append(f"**Description:**\n\n```\n{desc}\n```\n")
        md.append(f"**Files:** {', '.join('`upload/' + f + '`' for f in files)}\n\n---\n")
    open(f"{OUT}/{NAME}.md", "w", encoding="utf-8").write("\n".join(md))
    json.dump(bodies, open(f"{UPLOAD}/bodies.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"wrote {NAME}.md and upload/bodies.json with {len(bodies)} entries")


if __name__ == "__main__":
    main()
