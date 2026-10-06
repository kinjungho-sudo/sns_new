# -*- coding: utf-8 -*-
"""EP03 폴더정리 — card_01 표지 재빌드 (패널을 안전여백 안으로). 2x 렌더 후 1080x1350 다운스케일."""
import asyncio, pathlib, base64
from playwright.async_api import async_playwright
from PIL import Image

FONT = pathlib.Path("font.css").read_text(encoding="utf-8")

CSS = f"""
{FONT}
*{{margin:0;padding:0;box-sizing:border-box;}}
.card{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:'A2Z';
background:#ECE6D8;
background-image:radial-gradient(#DED6C6 1.4px, transparent 1.4px);
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
.h1 .u{{background:linear-gradient(transparent 62%, #E4B9A3 62%);}}
.sub{{font-weight:500;font-size:30px;color:#5A5048;line-height:1.5;}}
.swipe{{position:absolute;right:74px;bottom:120px;font-weight:800;font-size:24px;color:#C0592F;display:flex;gap:8px;align-items:center;}}
.chip{{background:#fff;font-weight:700;font-size:24px;color:#4A413A;padding:13px 22px;border-radius:100px;
  box-shadow:0 8px 20px -10px rgba(80,60,40,.4);}}
.chip.r{{background:#C0592F;color:#fff;}}
.arrow{{font-weight:900;font-size:28px;color:#C0592F;}}
.panel{{position:absolute;right:56px;top:772px;width:398px;background:#FBF8F1;border-radius:28px;
  box-shadow:0 30px 70px -22px rgba(80,60,40,.45);border:1px solid #EFE7D8;padding:28px 32px;}}
.ph{{display:flex;align-items:center;gap:9px;margin-bottom:20px;}}
.dot{{width:11px;height:11px;border-radius:50%;display:inline-block;}}
.frow{{display:flex;align-items:center;justify-content:space-between;margin:17px 0;}}
.frow .nm{{display:flex;align-items:center;gap:14px;}}
.frow .ic{{font-size:33px;line-height:1;}}
.frow .fn{{font-weight:800;font-size:34px;color:#2A241F;}}
.frow .ct{{font-weight:600;font-size:29px;color:#B7AC9C;}}
"""

def frow(ic, nm, ct):
    return (f'<div class="frow"><div class="nm"><span class="ic">{ic}</span>'
            f'<span class="fn">{nm}</span></div><span class="ct">{ct}</span></div>')

PANEL = f"""
<div class="panel">
  <div class="ph"><span class="dot" style="background:#C9BDB0;"></span>
    <span class="dot" style="background:#C0592F;"></span>
    <span style="font-weight:700;font-size:25px;color:#9A8F82;margin-left:6px;">정리 완료</span></div>
  {frow('📁','01_보고서','4')}
  {frow('📁','02_계획','3')}
  {frow('📁','03_양식','5')}
  {frow('📁','99_검토필요','2')}
</div>
"""

INNER = f"""
<div style="margin-top:150px;">
  <div class="kick">직장인 AI 업무 자동화 · 3편</div>
  <div class="h1">폴더 정리,<br>AI한테 시켰더니<br><span class="u">3분 컷</span></div>
  <div class="sub" style="margin-top:26px;max-width:560px;">뒤섞인 파일을 던지면 규칙대로 이름 바꾸고<br>폴더별로 자동 분류해 줍니다.</div>
</div>
{PANEL}
<div style="position:absolute;left:74px;bottom:180px;display:flex;gap:12px;align-items:center;">
  <span class="chip">뒤섞인 파일</span><span class="chip">파일명 규칙</span>
  <span class="arrow">→</span><span class="chip r">정리된 폴더</span>
</div>
"""

CARD = f"""<div class="card"><div class="pad">
<div class="top"><span class="tag">AI 업무 자동화</span><span class="ep">EP.03 · 폴더 정리</span></div>
{INNER}
</div>
<div class="swipe">밀어서 보기 →</div>
<div class="bot"><span class="brand">Co<b>Mind</b>works</span><span></span></div>
</div>"""

async def main():
    html = "<!doctype html><html><head><meta charset='utf-8'><style>" + CSS + "</style></head><body>" + CARD + "</body></html>"
    pathlib.Path("c1.html").write_text(html, encoding="utf-8")
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=2)
        await pg.goto(pathlib.Path("c1.html").resolve().as_uri())
        await pg.wait_for_timeout(700)
        el = await pg.query_selector(".card")
        await el.screenshot(path="out/card_01_2x.png")
        await b.close()
    im = Image.open("out/card_01_2x.png").convert("RGB")
    print("rendered", im.size)
    im.resize((1080, 1350), Image.LANCZOS).save("out/card_01.png")
    print("saved out/card_01.png 1080x1350")

asyncio.run(main())
