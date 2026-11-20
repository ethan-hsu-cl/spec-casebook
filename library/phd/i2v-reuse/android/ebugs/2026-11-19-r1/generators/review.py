#!/usr/bin/env python3
"""Build the self-contained eBug review page for Image to Video Reuse R1 (Android) from upload/bodies.json.

Layout per ebug-tr-filer/references/review-page.md: page head facts (TRCode / account shown as 「needed」: no TR named,
no filed batch yet), batch decisions, one card per entry (why, Short Description, collapsed body, evidence strip with
lightbox, collapsed log, My read), then PM questions, not filed, gaps, and Copy decisions. Thumbnails are embedded as
data: URIs (Pillow), so the page needs no folder. Nothing is filed. Run after ebugs.py, drafts_to_bodies.py and the
format check.
"""
import base64, html, io, json, os, re, sys
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ebugs as G

OUT = G.OUT
PAGE = f"{OUT}/20261119_eBug_review_I2V-Reuse-R1_20.19.0.html"
bodies = json.load(open(f"{OUT}/upload/bodies.json", encoding="utf-8"))
items = list(bodies.values()) if isinstance(bodies, dict) else bodies
byiss = {e["iss"]: e for e in G.E}
esc = html.escape
ZH = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "zh.json"), encoding="utf-8"))


def thumb(path, size=760, q=72):
    im = Image.open(path).convert("RGB")
    im.thumbnail((size, size))
    b = io.BytesIO()
    im.save(b, "JPEG", quality=q)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()


SEVC = {1: "var(--s1)", 2: "var(--s2)", 3: "var(--s3)", 4: "var(--s4)", 5: "var(--s4)"}
cards = []
for it in items:
    e = byiss[it["iss"]]
    z = ZH.get(it["iss"], {})
    zbox = (f'<div class="zh"><div class="zl">中文說明（僅供審核，不會送出）</div><div class="zt">{esc(z["t"])}</div>'
            f'<div>{esc(z["w"])}</div><div class="zs">{esc(z["s"])}</div></div>') if z else ""
    n = it["entry"]
    imgs, logs = [], []
    for f in it["files"]:
        p = os.path.join(it["images_dir"], f)
        if f.endswith(".txt"):
            logs.append((f, open(p, encoding="utf-8").read()))
        else:
            imgs.append((f, thumb(p)))
    strip = "".join(
        f'<figure class="th" data-n="{n}" data-i="{i}"><img src="{src}" alt="{esc(f)}" loading="lazy"><figcaption>{i + 1}/{len(imgs)} · {esc(f.split("_", 2)[-1].rsplit(".", 1)[0].replace("_", " "))}</figcaption></figure>'
        for i, (f, src) in enumerate(imgs))
    logh = "".join(f'<details class="log"><summary>Log · {esc(f)}</summary><pre>{esc(t)}</pre></details>' for f, t in logs)
    chips = f'<span class="chip">Reproduced {e["rep"][0]}/{e["rep"][1]}</span><span class="chip">{esc(", ".join(e["cases"]))}</span>'
    if not imgs:
        chips += '<span class="chip warn">Evidence gap</span>'
    belong = it["belong"]
    opts = "".join(f'<option{" selected" if b == belong else ""}>{b}</option>' for b in ["RD", "PC-Doc", "PM", "PC-Art", "Setup Kit", "Marketing", "RD-ECL"])
    topts = "".join(f'<option{" selected" if t == it["type"] else ""}>{t}</option>' for t in ["Functional", "UI", "UX"])
    sev = "".join(f'<label><input type="radio" name="sev{n}" value="{s}"{" checked" if s == it["sev"] else ""}>{s}</label>' for s in range(1, 6))
    cards.append(f'''
<article class="card" id="F-{n}" data-n="{n}" style="--sev:{SEVC[it['sev']]}">
  <header><span class="fid">F-{n}</span><h3>{esc(e['title'])}</h3><div class="chips">{chips}</div></header>
  <p class="why">{esc(e['res'])} Expected: {esc(e['exp'])}</p>
  {zbox}
  <div class="sd" data-sd="{n}">{esc(it['short'])}</div>
  <details class="body"><summary>Description (as filed)</summary><pre>{esc(it['desc'])}</pre></details>
  <div class="strip">{strip}</div>
  {logh}
  <aside class="read"><b>My read.</b><span class="zhh">我的判斷（英文，細節見上方中文說明）</span> {esc(e['note'])}</aside>
  <div class="bar">
    <label class="file"><input type="checkbox" data-k="file" checked> file</label>
    <span class="sev" data-k="sev">Sev {sev}</span>
    <label>Belong <select data-k="belong">{opts}</select></label>
    <label>Type <select data-k="type">{topts}</select></label>
    <label class="ctx">Add context — what am I missing? <textarea data-k="note" rows="1" placeholder="Rewrite, split, merge, hold reason…"></textarea></label>
  </div>
</article>''')

notr = "".join(f"<tr><td>{esc(k)}</td><td>{esc(a)}</td><td>{esc(b)}</td></tr>" for k, a, b in G.OBS_NOT)
sevcount = {}
for it in items:
    sevcount[it["sev"]] = sevcount.get(it["sev"], 0) + 1
tally = " · ".join(f"S{s} ×{c}" for s, c in sorted(sevcount.items()))

PAGE_HTML = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>I2V Reuse eBugs R1</title>
<style>
:root{{--bg:#f7f6f3;--fg:#1d1c1a;--mut:#6b675f;--card:#fff;--line:#e3e0d8;--acc:#b4531f;--s1:#b42318;--s2:#d9480f;--s3:#b08900;--s4:#5f7f3a;--warn:#b42318;--mono:ui-monospace,Consolas,monospace;--gutter:16px}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#161514;--fg:#ece9e3;--mut:#a39e94;--card:#211f1d;--line:#36332f;--acc:#f08a4b;--s1:#f0625a;--s2:#ff8a4c;--s3:#e0b84a;--s4:#9cc26a;--warn:#ff7a70}}}}
:root[data-theme="dark"]{{--bg:#161514;--fg:#ece9e3;--mut:#a39e94;--card:#211f1d;--line:#36332f;--acc:#f08a4b;--s1:#f0625a;--s2:#ff8a4c;--s3:#e0b84a;--s4:#9cc26a;--warn:#ff7a70}}
*{{box-sizing:border-box}} body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif}}
main{{max-width:1080px;margin:0 auto;padding:24px var(--gutter) 80px}}
.eyebrow{{color:var(--mut);font-size:13px;text-transform:uppercase;letter-spacing:.06em}} h1{{margin:4px 0 6px;font-size:26px}}
dl.facts{{display:flex;flex-wrap:wrap;gap:8px 22px;margin:14px 0;padding:12px 14px;background:var(--card);border:1px solid var(--line);border-radius:10px}}
dl.facts div{{min-width:0}} dt{{font-size:12px;color:var(--mut)}} dd{{margin:0;font-weight:600;overflow-wrap:anywhere}} .need{{color:var(--warn)}}
.panel{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin:16px 0}} .panel h2{{margin:0 0 8px;font-size:18px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px}} .grid label{{display:flex;flex-direction:column;font-size:13px;color:var(--mut)}}
input[type=text],select,textarea{{font:inherit;color:var(--fg);background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:5px 8px;max-width:100%}}
.card{{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--sev);border-radius:10px;padding:14px 16px;margin:18px 0;min-width:0}}
.card.held{{opacity:.45}} .card header{{display:flex;flex-wrap:wrap;align-items:baseline;gap:8px}} .fid{{font-weight:700;color:var(--sev)}} .card h3{{margin:0;font-size:17px;flex:1 1 300px}}
.chips{{display:flex;flex-wrap:wrap;gap:6px}} .chip{{font-size:12px;border:1px solid var(--line);border-radius:999px;padding:1px 8px;color:var(--mut)}} .chip.warn{{color:var(--warn);border-color:var(--warn)}}
.why{{margin:8px 0}} .sd{{font-family:var(--mono);font-size:13px;background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:8px 10px;overflow-wrap:anywhere}}
details summary{{cursor:pointer;color:var(--mut);margin:8px 0 4px}} pre{{white-space:pre-wrap;overflow-wrap:anywhere;font-family:var(--mono);font-size:12.5px;background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:10px;margin:0}}
.strip{{display:flex;gap:10px;overflow-x:auto;padding:8px 0}} .th{{margin:0;flex:0 0 auto;width:110px;cursor:zoom-in}} .th img{{width:110px;height:auto;border-radius:6px;border:1px solid var(--line);display:block}} .th figcaption{{font-size:11px;color:var(--mut);overflow-wrap:anywhere}}
.zh{{border-left:3px solid var(--s4);background:var(--bg);border-radius:0 6px 6px 0;padding:8px 12px;margin:8px 0;font-size:14px;display:grid;gap:4px}} .zh .zt{{font-weight:700}} .zh .zs{{white-space:pre-line}} .zh .zl{{font-size:12px;color:var(--mut)}} .zhh{{font-weight:400;color:var(--mut);font-size:.85em;margin-left:6px}}
.read{{border-left:3px solid var(--acc);background:color-mix(in srgb,var(--acc) 8%,transparent);padding:8px 12px;margin:10px 0;border-radius:0 6px 6px 0;font-size:14px;overflow-wrap:anywhere}}
.bar{{display:flex;flex-wrap:wrap;gap:10px 16px;align-items:center;border-top:1px solid var(--line);padding-top:10px;font-size:14px}} .sev label{{margin-left:6px}}
.ctx{{flex:1 1 260px;display:flex;flex-direction:column;color:var(--acc);font-weight:600}} .ctx textarea{{width:100%;font-weight:400;resize:vertical}}
table{{width:100%;border-collapse:collapse;font-size:14px;table-layout:fixed}} td,th{{border-top:1px solid var(--line);padding:6px;vertical-align:top;text-align:left;overflow-wrap:anywhere}}
th:first-child,td:first-child{{width:90px}} button{{font:inherit;background:var(--acc);color:#fff;border:0;border-radius:8px;padding:8px 14px;cursor:pointer}}
#lb{{position:fixed;inset:0;background:rgba(0,0,0,.85);display:none;flex-direction:column;align-items:center;justify-content:center;padding:16px;z-index:9}} #lb.on{{display:flex}} #lb img{{max-width:100%;max-height:78vh}} #lb p{{color:#eee;margin:8px 0;text-align:center}} #lb nav{{display:flex;gap:10px}}
@media (max-width:600px){{h1{{font-size:21px}} .card{{padding:12px}}}}
</style></head><body><main>
<div class="eyebrow">spec-casebook · PhotoDirector Android · Image to Video Reuse · round R1 (table v3)</div>
<h1>Image to Video Reuse — {len(items)} eBug drafts for review</h1>
<p>Decide file / hold, severity and owner per card, add context where the draft misses something, then press <b>Copy decisions</b> and paste the block back in chat. Nothing has been filed.<br><span class="zhh" style="margin:0">中文：每張卡片是將送出的 eBug 原文（英文），綠色框是中文說明，只給審核參考、不會送出。請對每張卡片決定送出或保留、嚴重度、歸屬與類型，必要時補充說明，最後按 Copy decisions 把結果貼回對話。目前沒有送出任何 eBug。</span></p>
<dl class="facts"><div><dt>Version</dt><dd>20.19.0</dd></div><div><dt>Build No</dt><dd>90201901</dd></div><div><dt>Server</dt><dd>Test Server</dd></div>
<div><dt>Device</dt><dd>Google Pixel 8a / Android 16</dd></div><div><dt>Tested account</dt><dd>Free (Premium only for setup probes); credits 1839 → 1113</dd></div>
<div><dt>TRCode</dt><dd class="need">TR261118-0070 (20.19.0.v202611181947, R5) — confirm</dd></div><div><dt>ECL product</dt><dd>PhotoDirector Mobile for Android (from the TR)</dd></div>
<div><dt>Severity</dt><dd>{tally}</dd></div><div><dt>UX</dt><dd>UX ×{sum(1 for it in items if "[UX]" in it["short"])} (PM decisions)</dd></div></dl>
<p style="color:var(--mut);font-size:14px">Calibration: S4 is rare in this pool (1 of 175); five cosmetic or minor entries are proposed S4 (F-2, F-4, F-6, F-9, F-10). No S1 or S2: Reuse works end to end (settings, price, charge, one job per burst, video follows the prompt).</p>
<section class="panel"><h2>Batch decisions<span class="zhh">建單設定</span></h2><div class="grid">
<label>Filing account (Creator, from batch-editing 2026-11-17-tr261113-0038; no filed batch for this feature — confirm)<input type="text" id="b-creator" value="WILLY_WU"></label>
<label>TRCode (named for this run — confirm)<input type="text" id="b-tr" value="TR261118-0070"></label>
<label>Source tag<input type="text" id="b-tag" value="[AIAgent]"></label>
<label>Method<select id="b-method"><option>API (new way)</option><option>Browser form (old way)</option></select></label>
<label>ECL product<input type="text" id="b-prod" value="PhotoDirector Mobile for Android"></label></div></section>
{''.join(cards)}
<section class="panel"><h2>Reproduced but deliberately not filed<span class="zhh">有重現但不開單</span></h2><p>No same-OS duplicate among the 10 drafts (read-only dedupe over the Android pool, 2026-11-19, dedupe.txt). PHA262026P0126 (Recent opens Save & Share without Prompts & Settings, TR261113-0038) is a different defect: R1 TC-009 passed on this build. F-6 and F-10 ask PM for a decision.<br><span class="zhh" style="margin:0">10 份草稿在 Android 票池裡都沒有重複（2026-11-19 唯讀查詢，見 dedupe.txt）。PHA262026P0126（從 Recent 開的 Save & Share 沒有 Prompts & Settings）是不同的問題，這版 TC-009 已 Pass。F-6、F-10 是請 PM 決定。</span></p><table><tr><th>Item</th><th>What was seen</th><th>Why not raised</th></tr>{notr}</table></section>
<section class="panel"><h2>Gaps you should know about<span class="zhh">需要注意的缺口</span></h2><ul>
<li>11 Blocked: TC-029 – TC-031 (no removed model), TC-019 (no free trial), TC-036 (no VIP low-balance account), TC-035 (Free balance 1113 above the price 80), TC-034 (no model refuses a real-person photo on this build), TC-041 / TC-042 (no pre-feature or unreadable video), TC-016 / TC-046 (behind F-1 / F-2).<br><span class="zhh" style="margin:0">11 個 Blocked：TC-029～031（沒有已下架的模型）、TC-019（沒有免費試用）、TC-036（沒有點數不足的 VIP 帳號）、TC-035（Free 帳號餘額 1113 高於價格 80）、TC-034（這版沒有模型會擋真人照片）、TC-041／042（沒有功能上線前或讀不到設定的影片）、TC-016／046（卡在 F-1／F-2）。</span></li>
<li>TC-037 – TC-040 were set Blocked (no analytics log) in the plan but ran: the app writes its Mixpanel events to logcat (「[PHD-A][Mixpanel]」). TC-038 – TC-040 pass; TC-037 is F-7.<br><span class="zhh" style="margin:0">TC-037～040 在計畫裡因「沒有分析事件 log」先標 Blocked，但 App 會把 Mixpanel 事件寫進 logcat，所以照跑：TC-038～040 Pass，TC-037 就是 F-7。</span></li>
<li>F-8 (theme switch) and F-9 (rotated frame) come from observations O-1 / O-2, not from a row; O-4 is not drafted (history-button path, outside this spec).<br><span class="zhh" style="margin:0">F-8（切換主題）和 F-9（畫面旋轉）來自觀察 O-1／O-2，不是表格裡的 case；O-4 沒寫草稿（從歷史按鈕進的路徑，不在這次 spec 範圍）。</span></li>
<li>TC-024 failed only on the lower-case chip already in F-4; the 10 s video has sound and follows the prompt.<br><span class="zhh" style="margin:0">TC-024 只因小寫 chip 而 Fail，已包含在 F-4；那支 10 秒影片有音效，內容也符合 prompt。</span></li>
<li>verify_ebug_drafts.py now runs on Windows (its folder search hung there; fixed 2026-11-19): entry 10 got its Basis line, and what it still lists (sheet names from the old exploration Figma index, no Owner split table or Row-by-row map) is the exploration draft layout, not casebook rules; check_ebug_format.py --product PHD-A --allow-agent-ux passed with 0 errors, 10 warnings (5 × S4, 5 Short Descriptions over 120).<br><span class="zhh" style="margin:0">verify_ebug_drafts.py 在 Windows 上原本會卡住，2026-11-19 已修好：補上第 10 份的 Basis 行；它剩下列出的項目（舊探索流程的 Figma 頁名、Owner split 表、Row-by-row map）是舊草稿格式，不是 casebook 的規則。check_ebug_format.py 0 錯誤、10 個警告（5 份 S4、5 份 Short Description 超過 120 字）。</span></li></ul></section>
<section class="panel"><h2>Copy decisions<span class="zhh">複製審核結果</span></h2><button id="copy">Copy decisions</button> <span id="copied" style="color:var(--mut)"></span><pre id="out" style="margin-top:10px"></pre></section>
</main>
<div id="lb"><img alt=""><p></p><nav><button id="pv">← Prev</button><button id="cl">Close</button><button id="nx">Next →</button></nav></div>
<script>
const KEY='i2vr-r1-review';let st={{}};try{{st=JSON.parse(localStorage.getItem(KEY)||'{{}}')}}catch(e){{}}
function save(){{try{{localStorage.setItem(KEY,JSON.stringify(st))}}catch(e){{}}}}
const sevc={{1:'var(--s1)',2:'var(--s2)',3:'var(--s3)',4:'var(--s4)',5:'var(--s4)'}};
document.querySelectorAll('.card').forEach(c=>{{const n=c.dataset.n,s=st[n]||(st[n]={{}});
 const f=c.querySelector('[data-k=file]'),b=c.querySelector('[data-k=belong]'),t=c.querySelector('[data-k=type]'),no=c.querySelector('[data-k=note]');
 if(s.file!==undefined)f.checked=s.file; if(s.belong)b.value=s.belong; if(s.type)t.value=s.type; if(s.note)no.value=s.note;
 if(s.sev){{const r=c.querySelector(`input[name=sev${{n}}][value="${{s.sev}}"]`);if(r)r.checked=true}}
 const paint=()=>{{c.classList.toggle('held',!f.checked);const v=c.querySelector(`input[name=sev${{n}}]:checked`).value;c.style.setProperty('--sev',sevc[v])}};paint();
 c.addEventListener('change',()=>{{s.file=f.checked;s.belong=b.value;s.type=t.value;s.note=no.value;s.sev=c.querySelector(`input[name=sev${{n}}]:checked`).value;paint();save()}});
 no.addEventListener('input',()=>{{s.note=no.value;save()}});}});
['b-creator','b-tr','b-tag','b-method','b-prod'].forEach(id=>{{const el=document.getElementById(id);if(st[id])el.value=st[id];el.addEventListener('input',()=>{{st[id]=el.value;save()}});el.addEventListener('change',()=>{{st[id]=el.value;save()}})}});
document.getElementById('copy').onclick=()=>{{const v=id=>document.getElementById(id).value;
 let o=`Account: ${{v('b-creator')||'(needed)'}}\\nTRCode: ${{v('b-tr')||'(needed)'}}\\nSource tag: ${{v('b-tag')}}\\nMethod: ${{v('b-method')}}\\nECL product: ${{v('b-prod')}}\\n\\n| # | Sev | Belong | Type | UX check | Action | Short Description | Note |\\n|---|---|---|---|---|---|---|---|\\n`;
 document.querySelectorAll('.card').forEach(c=>{{const n=c.dataset.n;o+=`| ${{n}} | ${{c.querySelector(`input[name=sev${{n}}]:checked`).value}} | ${{c.querySelector('[data-k=belong]').value}} | ${{c.querySelector('[data-k=type]').value}} | — | ${{c.querySelector('[data-k=file]').checked?'file':'hold'}} | ${{c.querySelector('.sd').textContent}} | ${{c.querySelector('[data-k=note]').value.replace(/\\|/g,'/').replace(/\\n/g,' ')}} |\\n`}});
 document.getElementById('out').textContent=o;try{{navigator.clipboard.writeText(o);document.getElementById('copied').textContent='Copied.'}}catch(e){{document.getElementById('copied').textContent='Select the block below and copy it.'}}}};
const lb=document.getElementById('lb'),li=lb.querySelector('img'),lp=lb.querySelector('p');let cur=[],ci=0;
function show(){{const f=cur[ci];li.src=f.querySelector('img').src;lp.textContent=`F-${{f.dataset.n}} · ${{ci+1}} of ${{cur.length}} — ${{f.querySelector('figcaption').textContent}}`}}
document.querySelectorAll('.th').forEach(f=>f.onclick=()=>{{cur=[...document.querySelectorAll(`.th[data-n="${{f.dataset.n}}"]`)];ci=+f.dataset.i;show();lb.classList.add('on')}});
document.getElementById('pv').onclick=()=>{{ci=(ci+cur.length-1)%cur.length;show()}};document.getElementById('nx').onclick=()=>{{ci=(ci+1)%cur.length;show()}};
document.getElementById('cl').onclick=()=>lb.classList.remove('on');
document.addEventListener('keydown',e=>{{if(!lb.classList.contains('on'))return;if(e.key==='Escape')lb.classList.remove('on');if(e.key==='ArrowLeft')document.getElementById('pv').click();if(e.key==='ArrowRight')document.getElementById('nx').click()}});
</script></body></html>'''
open(PAGE, "w", encoding="utf-8").write(PAGE_HTML)
print(f"wrote {PAGE} ({os.path.getsize(PAGE) // 1024} KB, {len(items)} cards)")
