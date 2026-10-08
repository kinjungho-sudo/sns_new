# -*- coding: utf-8 -*-
# EP04 card_01(표지) 재빌드 — 기존 레이아웃 유지하되 매출_통합 표 패널이
# 우측 프레임에 잘리던 블리드를 제거(안전여백 ≥24px). 프레임/톤/문구 동일.
import asyncio, pathlib
from playwright.async_api import async_playwright

OUT = pathlib.Path(__file__).parent
FONT = (OUT / "font.css").read_text(encoding="utf-8")

CSS = f"""
{FONT}
*{{margin:0;padding:0;box-sizing:border-box;}}
.card{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:'A2Z';
 background:#ECE6D8;background-image:radial-gradient(#DED6C6 1.4px, transparent 1.4px);
 background-size:26px 26px;color:#2A241F;}}
.pad{{position:absolute;inset:0;padding:76px 74px;display:flex;flex-direction:column;}}
.top{{display:flex;justify-content:space-between;align-items:center;}}
.tag{{background:#C0592F;color:#fff;font-weight:800;font-size:23px;padding:11px 22px;border-radius:100px;letter-spacing:.3px;}}
.ep{{color:#8A7F72;font-weight:700;font-size:23px;}}
.bot{{position:absolute;left:74px;right:74px;bottom:56px;display:flex;justify-content:space-between;align-items:center;
 border-top:1.5px solid #D5CBBB;padding-top:22px;}}
.brand{{font-weight:800;font-size:22px;color:#5A5048;}}
.brand b{{color:#C0592F;}}
.kick{{font-weight:700;font-size:30px;color:#C0592F;margin-bottom:14px;}}
.h1{{font-weight:900;font-size:92px;line-height:1.06;letter-spacing:-2px;}}
.h1 .u{{background:linear-gradient(transparent 60%, #E4B9A3 60%);}}
.sub{{font-weight:500;font-size:30px;color:#5A5048;line-height:1.5;}}
.rust{{color:#C0592F;}}
.swipe{{position:absolute;right:74px;bottom:120px;font-weight:800;font-size:24px;color:#C0592F;}}

/* summary panel */
.panel{{position:absolute;right:74px;bottom:290px;width:432px;background:#FBF8F1;border:1px solid #E6DCCB;
 border-radius:18px;box-shadow:0 24px 60px -18px rgba(80,60,40,.35);overflow:hidden;padding:20px 22px;}}
.ptitle{{font-weight:700;font-size:21px;color:#6A5F52;margin-bottom:14px;display:flex;align-items:center;gap:9px;}}
.ptitle::before{{content:'';width:11px;height:11px;border-radius:50%;background:#C0592F;display:inline-block;}}
table{{width:100%;border-collapse:collapse;}}
th,td{{padding:11px 14px;font-size:24px;}}
th{{font-weight:700;color:#6A5F52;background:#F1E8D9;font-size:22px;}}
td{{font-weight:600;color:#3A342E;border-bottom:1px solid #EFE7D8;text-align:center;}}
td.amt{{text-align:right;}}
tr.total td{{background:#FBF1E9;font-weight:900;color:#C0592F;border-bottom:none;}}
th:first-child{{border-top-left-radius:10px;}} th:last-child{{border-top-right-radius:10px;}}

/* input chips */
.chips{{position:absolute;left:74px;bottom:168px;display:flex;align-items:center;gap:14px;}}
.chip{{background:#fff;border:1px solid #E6DCCB;font-weight:800;font-size:26px;color:#4A433B;padding:14px 24px;border-radius:14px;
 box-shadow:0 10px 22px -16px rgba(80,60,40,.4);}}
.chip.rust{{background:#C0592F;color:#fff;border-color:#C0592F;}}
.arrow{{font-weight:900;font-size:30px;color:#C0592F;}}
"""

CARD = f"""<div class="card"><div class="pad">
  <div class="top"><span class="tag">AI 업무 자동화</span><span class="ep">EP.04 · 매출 통합</span></div>
  <div style="margin-top:120px;">
    <div class="kick">직장인 AI 업무 자동화 · 4편</div>
    <div class="h1">분기 엑셀 4개,<br>AI가 <span class="u">1개로</span></div>
    <div class="sub" style="margin-top:26px;">따로 흩어진 매출 파일을 던지면<br>하나로 합치고 요약까지 만들어 줍니다.</div>
  </div>
  <div class="panel">
    <div class="ptitle">매출_통합.xlsx</div>
    <table>
      <tr><th>분기</th><th>건수</th><th>매출</th></tr>
      <tr><td>Q1</td><td>50</td><td class="amt">6.0억</td></tr>
      <tr><td>Q2</td><td>50</td><td class="amt">7.0억</td></tr>
      <tr><td>Q3</td><td>50</td><td class="amt">8.0억</td></tr>
      <tr><td>Q4</td><td>50</td><td class="amt">9.0억</td></tr>
      <tr class="total"><td>합계</td><td>200</td><td class="amt">30.0억</td></tr>
    </table>
  </div>
  <div class="chips">
    <span class="chip">엑셀 4개</span>
    <span class="chip">통합 기준</span>
    <span class="arrow">→</span>
    <span class="chip rust">통합 시트</span>
  </div>
</div>
<div class="swipe">밀어서 보기 →</div>
<div class="bot"><span class="brand">Co<b>Mind</b>works</span><span></span></div>
</div>"""


async def main():
    html = "<!doctype html><html><head><meta charset='utf-8'><style>" + CSS + "</style></head><body>" + CARD + "</body></html>"
    p = OUT / "card_01.html"; p.write_text(html, encoding="utf-8")
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=2)
        await pg.goto(p.resolve().as_uri())
        await pg.wait_for_timeout(600)
        el = await pg.query_selector(".card")
        await el.screenshot(path=str(OUT / "card_01_new.png"))
        await b.close()
    print("done -> card_01_new.png")

asyncio.run(main())
