#!/usr/bin/env python3
"""Build the Image to Video Reuse (Android) eBug draft batch for round R1 (table v3, draft 20261106-115758) on
20.19.0 (90201901) v202611181947, TR261118-0070, Google Pixel 8a.

Writes ../20261119_eBug_drafts_I2V-Reuse-R1_20.19.0.md, the sibling _images/ folder (one NN_ISS-ID folder per entry:
JPEGs named 20.19.0_irNN_<slug>.jpg, red boxes where they help, plus the logcat excerpt where the finding has a log
cause), logs/ and entries.json. Nothing is filed. Every Fail row of results.csv and every observation O-n is mapped
(entry / not raised); the script stops when one is missing. Adapted from the Creative Reel R1 generator.
Run: python library/phd/i2v-reuse/android/ebugs/2026-11-19-r1/generators/ebugs.py
"""
import csv, json, os, re, shutil, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(OUT, "..", ".."))           # library/phd/i2v-reuse/android
RUN = f"{ROOT}/runs/2026-11-19-r1"
NAME = "20261119_eBug_drafts_I2V-Reuse-R1_20.19.0"
V, B = "20.19.0", "90201901"
DAY = "2026-11-19"
PROD = "PHD-A"
FEAT = "Image_to_Video"
PIX = "Device: Google Pixel 8a / Android 16, Test Server, Free account (build 20.19.0.v202611181947)"
PM_URL = "https://www.figma.com/design/lSk4JUgbXG3DjauMLS9Et7/Image-to-Video"
DS_URL = "https://www.figma.com/design/VU8bgYiFHTWhYddg7ciqtL/Image-to-video---Character-motion-swap"


def pm(board, what, node):
    return f"Spec Link: Image to Video Reuse PM Figma (page 26'11/E support to reuse model settings in My artwork), {board} board ({what}) -\n{PM_URL}?node-id={node}"


def ds(frame, what, node):
    return f"Spec Link: Image to Video Reuse Design Figma (page 261105_support to reuse model settings), {frame} frame ({what}) -\n{DS_URL}?node-id={node}"


P_UI_REUSE = pm("Spec - UI", "From Save & Share Reuse, D1-04 / D1-04b toast 「Settings applied」", "6366-5664")
P_UI_INTRO = pm("Spec - UI", "From Save & Share Reuse, D1-04b explanation sheet first", "6366-5664")
P_UI_BACK = pm("Spec - UI", "From Save & Share Reuse, D1-05 ‹ Back returns to Save & Share", "6366-5664")
P_UI_ART = pm("Spec - UI", "My AI Artwork, D1-03 Create more mockup", "6366-5664")
P_FLOW = pm("Spec - Flow", "Reuse flow and Create more mockup", "6366-4241")
P_TRACK = pm("【Tracking Event】", "D4-05 ImageToVideo_Reuse_Click, parameter model", "6394-586")
D_SS = ds("Save & Share light", "Prompts & Settings card, chips 「10s」 「Pro」 「Sound on」, section order", "4702-20032")
D_SSD = ds("Save & Share dark", "Save & Share page in dark mode", "4720-469")

ART = ["Launch the APP", "Tap AI Photos", "Tap My Artwork", "Tap the All categories button", "Tap Image to Video",
       "Tap a finished Custom video made with Kling 2.6 (10s, Pro, Sound on)"]
REUSE = ART + ["Tap Reuse"]
CARD = (30, 1262, 1050, 1705)
CHIP = (195, 1462, 335, 1562)

# Each entry: iss, title, cls (Functional / UI / UX), sev, owner, cases, rep, note (QA note, not pasted), short, steps,
# res, res_zh, exp, exp_zh, links, dev, imgs [(png, slug, box or None)], log (title, [(label, t0, t1)]) or None, rel
E = [
 dict(iss="ISS-IR-01", title="No 「Settings applied」 toast after Reuse", cls="Functional", sev=3, owner="RD",
      cases=["TC-010", "TC-013", "TC-015"], rep=(4, 4),
      note="R-025 / R-026 (PM Spec - UI, From Save & Share Reuse D1-04 / D1-04b: entering the reused Custom page shows the toast 「Settings applied」). Reuse fills the room correctly (model, Start/End, prompt, empty photo; TC-010 / TC-013 / TC-012 Pass), but no toast: screenshots at ~0.6 s and ~2.6 s, a 9 s recording at 2 fps (TC-010), an 8 s recording (TC-015) and waitfor 「Settings applied」 7 s (TC-010, TC-013) found none. Seen on video A (Kling 2.6) and video C (Kling 3.0, Start/End). Blocks TC-016 (toast over a panel) and TC-046. The PM drew the toast only; no Design frame for it (PM-only).",
      short="No 「Settings applied」 toast when Reuse opens the Custom page",
      steps=REUSE + ["Watch the Custom page for 8 seconds"],
      res="The Custom page opens with the video's settings and prompt, but the toast 「Settings applied」 never shows.",
      res_zh="Reuse 進入 Custom 頁設定已帶入，但沒有出現「Settings applied」toast。",
      exp="On entering the Custom page the toast 「Settings applied」 shows (PM D1-04).",
      exp_zh="進入 Custom 頁時應顯示 toast「Settings applied」。",
      links=[P_UI_REUSE], dev=PIX,
      imgs=[("tc010-room", "reuse_room_no_toast", None), ("tc010-grid", "recording_frames_no_toast", None), ("tc013-room", "start_end_room_no_toast", None)],
      log=("Reuse tap and the room opening (no toast line)", [("TC-010 Reuse on video A", "14:05:30", "14:06:30")]), rel=[]),
 dict(iss="ISS-IR-02", title="Reuse skips the Image to Video explanation sheet", cls="Functional", sev=4, owner="RD",
      cases=["TC-015"], rep=(2, 2),
      note="R-026 (PM Spec - UI D1-04b: when Image to Video would show its Android explanation sheet, it shows first as today, then the toast). 「Don't show again」 was never tapped: entering Image to Video from AI Videos (14:14) and from a fresh My AI Artwork 「Create More」 (TC-028) still shows the 「Image To Video」 intro (Try now / Don't show again) and the 「Steps」 page, but 「Reuse」 opens the Custom page directly, every time (R1-a, R1-b, R1-c). TC-046 (Back on that sheet) is Blocked behind it.",
      short="Reuse opens Custom without the Image to Video explanation sheet shown elsewhere",
      steps=["Launch the APP", "Tap AI Videos", "Tap Image to Video", "Check the explanation sheet shows", "Tap the device Back button", "Tap AI Photos", "Tap My Artwork", "Tap the All categories button", "Tap Image to Video", "Tap a finished Custom video made with Kling 2.6", "Tap Reuse"],
      res="From AI Videos the 「Image To Video」 explanation sheet shows; from 「Reuse」 the Custom page opens directly with no sheet.",
      res_zh="從 AI Videos 進入會出現說明頁，但從 Reuse 進入直接到 Custom 頁，沒有說明頁。",
      exp="When Image to Video would show its explanation sheet, Reuse shows it first as today, then the Custom page (PM D1-04b).",
      exp_zh="說明頁應照常先出現，關閉後才進入 Custom 頁。",
      links=[P_UI_INTRO], dev=PIX,
      imgs=[("tc015-ai-videos-entry", "ai_videos_entry_sheet", None), ("tc015-room", "reuse_no_sheet", None)], log=None, rel=[]),
 dict(iss="ISS-IR-03", title="‹ and system Back in the reused room skip the Save & Share page", cls="Functional", sev=3, owner="RD",
      cases=["TC-020", "TC-043"], rep=(3, 3),
      note="R-033 (PM Spec - UI From Save & Share Reuse D1-05: ‹ Back in the reused room returns to the Save & Share page) and R-058 / R-064 (system Back acts as ‹). Both ‹ (top_back_btn) and system Back land on My AI Artwork › Image to Video (the list), never on the video's Save & Share page. First seen as O-3 (R1-a), then TC-020 / TC-043 (R1-b).",
      short="‹ / Back in the room opened by Reuse go to My AI Artwork, not Save & Share",
      steps=REUSE + ["Tap ‹ at the top left", "Tap the same video", "Tap Reuse", "Tap the device Back button"],
      res="Both ‹ and system Back return to the My AI Artwork Image to Video list; the video's Save & Share page is skipped.",
      res_zh="Reuse 房間按 ‹ 或返回鍵都回到 My AI Artwork 列表，未回到 Save & Share 頁。",
      exp="‹ (and system Back) in the reused room return to the video's Save & Share page (PM D1-05).",
      exp_zh="應回到該影片的 Save & Share 頁。",
      links=[P_UI_BACK], dev=PIX,
      imgs=[("tc020-back", "back_arrow_to_artwork", None), ("tc043-back", "system_back_to_artwork", None)], log=None, rel=[]),
 dict(iss="ISS-IR-04", title="Quality chip is lower case: 「pro」 / 「std」", cls="UI", sev=4, owner="RD",
      cases=["TC-006", "TC-024"], rep=(4, 4),
      note="R-012 (Design Save & Share light: chips 「10s」 「Pro」 「Sound on」; the Custom room's own Video Quality options read 「Pro」 / 「Standard」). Video A and the video generated from its Reuse (TC-024) show 「pro」, videos B and C show 「std」 (TC-013 saw 「std」 on C). Q-13 asked for the chip wording of each quality; the Design sample 「Pro」 states it for Pro, so this is RD (text differs from the stated spec). For Standard the Design has no sample: 「std」 vs 「Standard」 / 「Std」 is noted in the Expect.",
      short="Save & Share: quality chip reads lower-case 「pro」 / 「std」 (Design 「Pro」)",
      steps=ART + ["Read the chips on the Prompts & Settings card"],
      res="The quality chip reads 「pro」 (Kling 2.6 Pro video); on Standard videos it reads 「std」.",
      res_zh="畫質 chip 顯示小寫 pro／std。",
      exp="The chip reads 「Pro」 as the Design draws it (Standard capitalised the same way, e.g. 「Standard」 as in the room).",
      exp_zh="應顯示「Pro」（Standard 亦應首字大寫）。",
      links=[D_SS], dev=PIX,
      imgs=[("tc002-saveshare", "chip_pro_lowercase", CHIP), ("tc013-saveshare", "chip_std_lowercase", CHIP)], log=None, rel=["Q-13"]),
 dict(iss="ISS-IR-05", title="Save & Share order: 「Prompts & Settings」 right under 「Save」, no 「More Video Editing Tools」", cls="UI", sev=3, owner="RD",
      cases=["TC-049"], rep=(2, 2),
      note="R-067 (Design Save & Share light / dark: 「Save」, 「More Video Editing Tools」, 「Add Text」 「Add Sticker」 「Add Music」, 「Prompts & Settings」, 「Share to」). The app places the 「Prompts & Settings」 card directly under 「Save」, above the editing buttons, and has no 「More Video Editing Tools」 heading; 「Make It Reel-Ready」 sits between the editing buttons and 「Share to」 (not drawn; other feature).",
      short="Save & Share: 「Prompts & Settings」 sits under 「Save」; no 「More Video Editing Tools」",
      steps=ART + ["Scroll the page from top to bottom"],
      res="「Prompts & Settings」 sits right under 「Save」, above the editing buttons; no 「More Video Editing Tools」 heading.",
      res_zh="設定卡片在 Save 正下方，且缺少 More Video Editing Tools 標題。",
      exp="Order (Design): Save, More Video Editing Tools, Add Text / Sticker / Music, Prompts & Settings, Share to.",
      exp_zh="順序應為 Save、More Video Editing Tools、編輯按鈕、Prompts & Settings。",
      links=[D_SS, D_SSD], dev=PIX,
      imgs=[("tc002-saveshare", "order_card_under_save", CARD), ("tc049-bottom", "order_bottom", None)], log=None, rel=[]),
 dict(iss="ISS-IR-06", title="PM: Create more placeholder and counter differ from the Reuse spec mockup", cls="UI", sev=4, owner="PM",
      cases=["TC-028"], rep=(2, 2),
      note="R-041 (PM Spec - UI My AI Artwork D1-03 / Spec - Flow mockup: placeholder 「Describe the subject, action, and overall scene, e.g. A woman walking in a park on a sunny afternoon.」, counter 「0/2,500」; the reuse mockup also writes 「58/2,500」). The app's Create more room reads 「Describe the subject and how they move in the scene, e.g. A dancer spins and jumps under stage lights.」 and 「0/2500」. Create more is meant to be unchanged by this feature, so the mockup may simply copy an older string; filed to PM to confirm which text is current (text rule: PM when the spec's own text must change).",
      short="Create more: placeholder and 「0/2500」 differ from the PM mockup — PM to confirm",
      steps=["Launch the APP", "Tap AI Photos", "Tap My Artwork", "Tap the All categories button", "Tap Image to Video", "Tap Create More", "Tap Try now", "Tap Continue", "Read the prompt box"],
      res="Placeholder reads 「Describe the subject and how they move in the scene, e.g. A dancer spins…」; counter 「0/2500」.",
      res_zh="Create more 的提示文字與計數格式和 PM 稿不同。",
      exp="PM to confirm the text: the mockup shows 「Describe the subject, action, and overall scene, e.g. …」 and 「0/2,500」.",
      exp_zh="請 PM 確認正確提示文字與計數格式（稿上為 0/2,500）。",
      links=[P_UI_ART, P_FLOW], dev=PIX,
      imgs=[("tc028-room", "create_more_placeholder", [(75, 1455, 920, 1735), (860, 1738, 1005, 1820)])], log=None, rel=[]),
 dict(iss="ISS-IR-07", title="Reuse sends Artwork_Reuse_Click without model, not ImageToVideo_Reuse_Click", cls="Functional", sev=3, owner="RD",
      cases=["TC-037"], rep=(3, 3),
      note="R-051 (PM 【Tracking Event】 D4-05: new event ImageToVideo_Reuse_Click with parameter model). Observed in the app's logcat Mixpanel lines (Q-8: a log pull): each 「Reuse」 tap logs 「logEvent name=Artwork_Reuse_Click」 (the form used for events without parameters; events with parameters print JSON) and 「[setCurFrom] from = artwork_reuse」. Three taps, 14:29:36, 14:32:52, 14:36:21. Generate after Reuse sends ImageToVideo_Result_Generate with from = artwork_reuse (TC-038 / TC-039 Pass) and Create more from = Artwork (TC-040 Pass).",
      short="Tracking: Reuse logs Artwork_Reuse_Click without model, not ImageToVideo_Reuse_Click",
      steps=ART + ["Tap Reuse", "Pull the app's logcat", "Find the Mixpanel event logged at the Reuse tap"],
      res="The Reuse tap logs 「logEvent name=Artwork_Reuse_Click」 with no parameters.",
      res_zh="點 Reuse 送出的事件為 Artwork_Reuse_Click，且沒有 model 參數。",
      exp="ImageToVideo_Reuse_Click is sent with parameter model = the video's model value (PM D4-05).",
      exp_zh="應送出 ImageToVideo_Reuse_Click 並帶 model 參數。",
      links=[P_TRACK], dev=PIX,
      imgs=[("tc023-room", "reuse_room", None)],
      log=("Mixpanel lines at Reuse and Generate", [("TC-023 Reuse and Generate", "14:29:30", "14:30:16"), ("TC-039 Reuse from Recent", "14:36:15", "14:36:47")]), rel=[]),
 dict(iss="ISS-IR-08", title="Switching the system theme on Save & Share drops the page to the Launcher", cls="Functional", sev=3, owner="RD",
      cases=["O-1"], rep=(1, 1),
      note="Observation O-1 (TC-050 setup, R1-a). With video A's Save & Share page open, the phone's system theme was switched dark → light: the app recreated and showed the Launcher's AI Videos tab; the Save & Share page was lost. The app follows the system theme (it turned light). Expected: an activity recreated by a configuration change keeps the page the user was on. Seen once (theme change is a system setting; restored after).",
      short="Save & Share: changing the system theme sends the app back to the Launcher",
      steps=ART + ["Open Android Settings from the quick settings panel", "Turn Dark theme off", "Return to PhotoDirector"],
      res="PhotoDirector shows the Launcher's AI Videos tab in light mode; the Save & Share page is gone.",
      res_zh="在 Save & Share 頁切換系統深淺色後，App 回到 Launcher，原頁面消失。",
      exp="The Save & Share page stays open and redraws in the new theme.",
      exp_zh="應停留在 Save & Share 頁並以新主題重繪。",
      links=[D_SSD], dev=PIX,
      imgs=[("tc050-dark", "saveshare_dark_before", None), ("tc050-light-check", "launcher_after_theme", None)], log=None, rel=[]),
 dict(iss="ISS-IR-09", title="Reuse transition draws the room rotated for a moment", cls="UI", sev=4, owner="RD",
      cases=["O-2"], rep=(3, 3),
      note="Observation O-2 (TC-010, again TC-015). The 9 s screen recording of 「Reuse」 shows the Custom room drawn rotated 90° (landscape layout) for one or two frames before it settles portrait (frames 3–4 of the grid). Phone in portrait, auto-rotate unchanged.",
      short="Reuse: Custom room flashes rotated (landscape) before settling portrait",
      steps=REUSE + ["Watch the transition into the Custom page"],
      res="For one or two frames the Custom room is drawn rotated (landscape) before it shows portrait.",
      res_zh="Reuse 轉場時房間短暫以橫向（旋轉）畫面出現。",
      exp="The Custom room opens in portrait without a rotated frame.",
      exp_zh="應直接以直向開啟，不閃現旋轉畫面。",
      links=[P_UI_REUSE], dev=PIX,
      imgs=[("tc010-grid", "rotated_frames", None), ("tc015-grid", "rotated_frames_again", None)], log=None, rel=[]),
 dict(iss="ISS-IR-10", title="PM: first tap in a reused prompt selects the whole prompt", cls="UX", sev=4, owner="PM",
      cases=["O-5"], rep=(2, 2),
      note="Observation O-5 (TC-045, TC-032). The first tap into the prompt box of a room opened by Reuse highlights the whole reused prompt; a Backspace or a typed letter then replaces all of it. The spec says nothing about the selection; R-022 brings the prompt back for editing. Filed to PM to decide (UX decision rule 2026-11-11).",
      short="Reused room: first tap selects the whole prompt (one key erases it) — PM to decide",
      steps=REUSE + ["Tap inside the prompt box"],
      res="The whole reused prompt is highlighted; the next key press replaces it.",
      res_zh="第一次點擊提示詞欄位會全選整段文字，再按一鍵即全部被取代。",
      exp="PM to decide: the tap places the cursor (keeping the prompt) or selects all on purpose.",
      exp_zh="請 PM 決定第一次點擊應放置游標或刻意全選。",
      links=[P_UI_REUSE], dev=PIX,
      imgs=[("tc045-after", "prompt_all_selected", None), ("tc032-focus", "prompt_all_selected_2", None)], log=None, rel=[],
      basis="None — neither the PM spec nor the Design states how the first tap treats the reused prompt; PM to decide"),
]

OBS_NOT = [
 ("O-3", "‹ in the Reuse room goes to My AI Artwork.", "In ISS-IR-03 (TC-020 / TC-043)."),
 ("O-4", "‹ in a Create More room reached via the room's history button → Reuse → ‹ → Create More went to the Launcher.", "Existing Image to Video navigation through the history button, outside this feature's spec; not compared with a pre-feature build."),
]

KEEP = re.compile(r"Mixpanel|totalRemain=|addNewPack|credit_action_id|Toast|ImageToVideoActivity\]?: \[on(Create|Destroy)|updatePackItems column value", re.I)
DROP = re.compile(r"memberToken|access_?token|authorization|bearer|signature=|purchaseToken|credit_member_token|credit_unique_id|creditSystemUUID|uuid|System\.err", re.I)


def log_lines(t0, t1):
    got, last = [], None
    base = f"{RUN}/logs"
    for f in sorted(os.listdir(base)):
        p = f"{base}/{f}/logcat-live.txt"
        if not os.path.exists(p):
            continue
        for line in open(p, encoding="utf-8", errors="replace"):
            parts = line.split(" ", 2)
            if len(parts) < 3 or parts[0] != DAY or not (t0 <= parts[1][:8] <= t1):
                continue
            if not KEEP.search(line):
                continue
            ts = f"{parts[0]} {parts[1]}"
            if "totalRemain=" in line:
                m = re.search(r"totalRemain=(\d+)", line)
                if not m or m.group(1) == last:
                    continue
                last = m.group(1)
                line = f"{ts} CreditSystem: totalRemain={last}"
            elif "addNewPack" in line:
                a = re.search(r'"credit_action_id":"([^"]+)"', line)
                c = re.search(r'"credit_total_credit":(\d+)', line)
                line = f"{ts} AIEditorPreferenceUtil: addNewPack credit_action_id={a.group(1) if a else '?'} credit_total_credit={c.group(1) if c else '?'}"
            else:
                if DROP.search(line):
                    continue
                line = re.sub(r"^(\S+ \S+) +\d+ +\d+ [VDIWE] ", r"\1 ", line.rstrip())
            line = re.sub(r"(https?://[^\s'\"?]+)\?\S*", r"\1?…", line)
            if line not in got:
                got.append(line[:400])
    return sorted(got, key=lambda l: l[:23])


def excerpt(n, iss, title, secs):
    L = [f"# {iss} {title}", f"# PhotoDirector Android {V} ({B}) v202611181947, Google Pixel 8a / Android 16, logcat of the app captured by the casebook run",
         "# Mixpanel, credit and job lines only (balance shown only when it changes); tokens and IDs dropped.", ""]
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
    path = f"{OUT}/logs/{V}_ir{n:02d}_log.txt"
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
    obs = sorted(set(re.findall(r"^- (O-\d+)\b", open(f"{RUN}/observations.md", encoding="utf-8").read(), re.M)), key=lambda x: int(x[2:]))
    MAP = {}
    for n, e in enumerate(E, 1):
        for c in e["cases"]:
            MAP.setdefault(c, []).append(f"{n}. {e['iss']}")
    for k, _, b in OBS_NOT:
        MAP.setdefault(k, []).append("not raised" if not b.startswith("In ISS") else b.rstrip("."))
    missing = [k for k in fails + obs if k not in MAP]
    extra = [k for k in MAP if k not in fails and k not in obs]
    if missing or extra:
        sys.exit(f"reconciliation incomplete: missing {missing}, extra {extra}")
    for e in E:
        for c in e["cases"]:
            if c not in fails and c not in obs:
                sys.exit(f"{e['iss']} cites {c}, which is not a Fail or observation")

    img_root = f"{OUT}/{NAME}_images"
    if os.path.isdir(img_root):
        shutil.rmtree(img_root)
    os.makedirs(img_root)
    L = []
    w = L.append
    w(f"# Image to Video Reuse (Android) — eBug drafts, round R1 (table v3), PhotoDirector {V} build {B}")
    w("")
    w(f"**Source:** spec-casebook run `library/phd/i2v-reuse/android/runs/2026-11-19-r1/` — phase R1 of draft `drafts/20261106-115758` (table v3, {len(rows)} cases), 2026-11-19 11:05 → 14:50, Google Pixel 8a / Android 16, Appium / UiAutomator2, Test Server, Free (Premium only for the R1-setup model probes). Tally: " + ", ".join(f"{v} {k}" for k, v in sorted(tally.items())) + ".")
    w("")
    w("**Status:** nothing filed, uploaded or commented. TR261118-0070 names build 20.19.0.v202611181947 (versionCode 90201901), the build tested. ECL product 「PhotoDirector Mobile for Android」. No filed batch for this feature yet: Creator, source tag and method to confirm on the review page.")
    w("")
    w("Rules: reviewer rules 2026-10-21 — one action per Repro step, a Spec Link on every entry (URL on its own line), at least one image per entry, the logcat excerpt on failure / tracking entries, no video. UX decisions to PM as `[AIAgent][UX]`; text and layout `[AIAgent][UI]` (RD when the Design / PM states the text, PM when the spec's text must be confirmed); behaviour `[AIAgent]` Functional, RD. Spec basis per entry against the PM page 6336:3478 (section Spec) and the Design page 4701:15518 (four frames).")
    w("")
    w(f"**What is drafted:** {len(E)} new entries (ISS-IR-01…{len(E):02d}), of which {sum(1 for e in E if e['owner'] == 'PM')} ask PM for a decision. Dedupe per OS: see dedupe.txt.")
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
                src = f"{RUN}/recordings/{png}.png"
            if not os.path.exists(src):
                sys.exit(f"missing screenshot {png}")
            name = f"{V}_ir{n:02d}_{slug}.jpg"
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
        if e.get("basis"):
            w(f"Basis: {e['basis']}")
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
    w(f"| Blocked ({len(blocked)}) | " + ", ".join(f"{v} {k}" for k, v in sorted(bd.items())) + " | " + ", ".join(r["ID"] for r in blocked) + ". |")
    w("")
    w("# Reconciliation against the run")
    w("")
    w(f"{len(fails)} Fail, {len(blocked)} Blocked, {tally.get('Not run', 0)} Not run, {len(obs)} observations (O-1 … O-{len(obs)}).")
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
