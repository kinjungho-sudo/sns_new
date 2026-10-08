# -*- coding: utf-8 -*-
# EP04 card_04 재빌드 — "4개 시트 → 통합 시트" 머지 비주얼
# 기존 EP04 프레임(크림#ECE6D8+도트 / 러스트#C0592F / A2Z / 1080x1350, 핸들 없음) 유지.
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
.pg{{font-weight:700;font-size:21px;color:#B7AC9C;}}
.kick{{font-weight:700;font-size:30px;color:#C0592F;margin-bottom:12px;}}
.h2{{font-weight:900;font-size:64px;line-height:1.1;letter-spacing:-1.5px;}}
.rust{{color:#C0592F;}}
.sub{{font-weight:500;font-size:29px;color:#5A5048;line-height:1.45;}}

/* flow layout */
.flow{{flex:1;display:flex;align-items:center;gap:16px;margin-top:34px;margin-bottom:150px;}}
.col-src{{display:flex;flex-direction:column;gap:14px;width:296px;}}
.srclabel{{font-weight:700;font-size:20px;color:#9A8F82;margin-bottom:2px;}}
.mini{{background:#FBF8F1;border:1px solid #E6DCCB;border-radius:13px;padding:13px 16px;
 box-shadow:0 10px 22px -14px rgba(80,60,40,.45);}}
.mhead{{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px;}}
.mname{{font-weight:800;font-size:20px;color:#C0592F;}}
.mcnt{{font-weight:600;font-size:17px;color:#9A8F82;}}
.mrow{{display:flex;justify-content:space-between;font-weight:500;font-size:19px;color:#4A433B;}}
.mrow .amt{{font-weight:700;color:#2A241F;}}

.arrowbox{{width:92px;display:flex;align-items:center;justify-content:center;}}

.sheet{{flex:1;background:#FBF8F1;border:1px solid #E6DCCB;border-radius:16px;
 box-shadow:0 20px 44px -18px rgba(80,60,40,.4);overflow:hidden;}}
.shead{{display:flex;justify-content:space-between;align-items:center;padding:16px 20px;background:#F3EADB;border-bottom:1px solid #E6DCCB;}}
.sname{{font-weight:800;font-size:22px;color:#2A241F;}}
.sbadge{{font-weight:800;font-size:18px;color:#fff;background:#C0592F;padding:5px 13px;border-radius:100px;}}
table{{width:100%;border-collapse:collapse;}}
th,td{{text-align:left;padding:9px 20px;font-size:19px;}}
th{{font-weight:700;color:#8A7F72;font-size:17px;border-bottom:1px solid #EAE1D2;}}
td{{font-weight:500;color:#3A342E;border-bottom:1px solid #F0E8DA;}}
td.amt,th.amt{{text-align:right;font-weight:700;color:#2A241F;}}
.more td{{color:#9A8F82;font-weight:600;font-style:normal;text-align:center;}}
.ssum{{padding:16px 20px 18px;background:#FBF3EC;border-top:1px solid #EAD3C4;}}
.ssum-title{{font-weight:800;font-size:19px;color:#C0592F;margin-bottom:9px;}}
.qrow{{display:flex;gap:7px;margin-bottom:11px;}}
.qchip{{flex:1;text-align:center;background:#fff;border:1px solid #EADBCB;border-radius:9px;padding:7px 0;}}
.qchip .q{{font-weight:700;font-size:16px;color:#9A8F82;}}
.qchip .v{{font-weight:900;font-size:21px;color:#2A241F;}}
.qchip.sum{{background:#C0592F;border-color:#C0592F;}}
.qchip.sum .q,.qchip.sum .v{{color:#fff;}}
.tags{{display:flex;gap:10px;}}
.tagpill{{font-weight:700;font-size:18px;color:#5A5048;background:#fff;border:1px solid #EADBCB;border-radius:100px;padding:6px 14px;}}
.tagpill b{{color:#C0592F;}}
"""

# 실제 샘플 데이터(각 분기 파일 첫 행) — 금액은 만원 반올림
SRC = [
    ("2024_Q1.xlsx", "T0001", "광주", "609만"),
    ("2024_Q2.xlsx", "T0051", "경기", "1,431만"),
    ("2024_Q3.xlsx", "T0101", "대구", "1,532만"),
    ("2024_Q4.xlsx", "T0151", "경기", "807만"),
]
UNI = [
    ("T0001", "광주", "609만"),
    ("T0051", "경기", "1,431만"),
    ("T0101", "대구", "1,532만"),
    ("T0151", "경기", "807만"),
]

minis = "".join(
    f'<div class="mini"><div class="mhead"><span class="mname">{n}</span><span class="mcnt">50행</span></div>'
    f'<div class="mrow"><span>{tid} · {reg}</span><span class="amt">{amt}</span></div></div>'
    for (n, tid, reg, amt) in SRC
)

unirows = "".join(
    f'<tr><td>{tid}</td><td>{reg}</td><td class="amt">{amt}</td></tr>' for (tid, reg, amt) in UNI
)

ARROW = """
<svg width="92" height="430" viewBox="0 0 92 430" fill="none">
  <path d="M2,40  C46,40  40,215 78,215" stroke="#C0592F" stroke-width="3" opacity=".75"/>
  <path d="M2,150 C46,150 46,215 78,215" stroke="#C0592F" stroke-width="3" opacity=".75"/>
  <path d="M2,280 C46,280 46,215 78,215" stroke="#C0592F" stroke-width="3" opacity=".75"/>
  <path d="M2,392 C46,392 40,215 78,215" stroke="#C0592F" stroke-width="3" opacity=".75"/>
  <polygon points="74,201 92,215 74,229" fill="#C0592F"/>
</svg>
"""

inner = f"""
<div style="margin-top:38px;">
  <div class="kick">AFTER · 30초</div>
  <div class="h2">4개 시트가 <span class="rust">하나로</span></div>
</div>
<div class="flow">
  <div class="col-src">
    <div class="srclabel">분기별 파일 4개</div>
    {minis}
  </div>
  <div class="arrowbox">{ARROW}</div>
  <div class="sheet">
    <div class="shead"><span class="sname">매출_통합.xlsx</span><span class="sbadge">200행</span></div>
    <table>
      <tr><th>거래번호</th><th>지역</th><th class="amt">금액</th></tr>
      {unirows}
      <tr class="more"><td colspan="3">⋯ 네 파일의 행이 이어 붙어 총 200건</td></tr>
    </table>
    <div class="ssum">
      <div class="ssum-title">분기별 요약 (자동 생성)</div>
      <div class="qrow">
        <div class="qchip"><div class="q">Q1</div><div class="v">6억</div></div>
        <div class="qchip"><div class="q">Q2</div><div class="v">7억</div></div>
        <div class="qchip"><div class="q">Q3</div><div class="v">8억</div></div>
        <div class="qchip"><div class="q">Q4</div><div class="v">9억</div></div>
        <div class="qchip sum"><div class="q">합계</div><div class="v">30억</div></div>
      </div>
      <div class="tags"><span class="tagpill">제품별 <b>✓</b></span><span class="tagpill">지역별 <b>✓</b></span></div>
    </div>
  </div>
</div>
<div class="sub" style="position:absolute;left:74px;right:74px;bottom:130px;">
  4개 시트의 행이 하나의 통합 시트로 — <span class="rust">거래 200건·매출 30억</span> 그대로.
</div>
"""

CARD = f"""<div class="card"><div class="pad">
  <div class="top"><span class="tag">AI 업무 자동화</span><span class="ep">EP.04 · 매출 통합</span></div>
  {inner}
</div>
<div class="bot"><span class="brand">Co<b>Mind</b>works</span><span class="pg">4 / 7</span></div>
</div>"""


async def main():
    html = "<!doctype html><html><head><meta charset='utf-8'><style>" + CSS + "</style></head><body>" + CARD + "</body></html>"
    p = OUT / "card_04.html"; p.write_text(html, encoding="utf-8")
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=2)
        await pg.goto(p.resolve().as_uri())
        await pg.wait_for_timeout(600)
        el = await pg.query_selector(".card")
        await el.screenshot(path=str(OUT / "card_04_new.png"))
        await b.close()
    print("done -> card_04_new.png")

asyncio.run(main())
