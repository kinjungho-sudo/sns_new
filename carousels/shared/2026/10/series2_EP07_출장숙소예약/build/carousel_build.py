# -*- coding: utf-8 -*-
"""EP.07 출장 숙소 예약 — 7장 캐러셀 빌드 (크림/러스트·A2Z·Before→After, Parro/핸들/실명 제외)."""
import asyncio, pathlib, base64
from playwright.async_api import async_playwright
from PIL import Image

FONT = pathlib.Path("font.css").read_text(encoding="utf-8")

def b64(p):
    if not pathlib.Path(p).exists():
        return ""
    return "data:image/png;base64," + base64.b64encode(pathlib.Path(p).read_bytes()).decode()

TE = b64("templ_empty.png")
TF = b64("templ_filled.png")
COVER = b64("../raw/cover.png")
BEFORE = b64("../raw/before.png")

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
.pg{{font-weight:700;font-size:21px;color:#B7AC9C;}}
.kick{{font-weight:700;font-size:30px;color:#C0592F;margin-bottom:14px;}}
.h1{{font-weight:900;font-size:92px;line-height:1.05;letter-spacing:-2px;}}
.h1 .u{{background:linear-gradient(transparent 62%, #E4B9A3 62%);}}
.h2{{font-weight:900;font-size:64px;line-height:1.12;letter-spacing:-1.5px;}}
.sub{{font-weight:500;font-size:30px;color:#5A5048;line-height:1.5;}}
.rust{{color:#C0592F;}}
.swipe{{position:absolute;right:74px;bottom:120px;font-weight:800;font-size:24px;color:#C0592F;display:flex;gap:8px;align-items:center;}}
.chip{{background:#fff;font-weight:700;font-size:23px;color:#4A413A;padding:12px 20px;border-radius:100px;
  box-shadow:0 8px 20px -10px rgba(80,60,40,.4);}}
.chip.r{{background:#C0592F;color:#fff;}}
.arrow{{font-weight:900;font-size:28px;color:#C0592F;}}
/* 받은 메일 목업 (card2) */
.mail{{background:#fff;border:1px solid #EAE1D2;border-radius:18px;
  box-shadow:0 30px 70px -22px rgba(80,60,40,.45);overflow:hidden;}}
.mail .mh{{background:#F4EEE2;padding:20px 26px;border-bottom:1px solid #E6DDCD;display:flex;align-items:center;gap:12px;}}
.mail .mh .ic{{width:40px;height:40px;border-radius:50%;background:#C0592F;color:#fff;font-weight:900;font-size:22px;
  display:flex;align-items:center;justify-content:center;}}
.mail .mh .ti{{font-weight:800;font-size:25px;color:#3A342E;}}
.mail .mh .fr{{font-weight:600;font-size:19px;color:#9A8F82;}}
.mail .mb{{padding:24px 28px;}}
.mail .q{{display:flex;gap:14px;align-items:center;margin-bottom:16px;font-weight:600;font-size:26px;color:#3A342E;}}
.mail .q:last-child{{margin-bottom:0;}}
.mail .q .b{{flex:none;width:40px;height:40px;border-radius:12px;background:#F0DCCF;color:#C0592F;
  font-weight:900;font-size:24px;display:flex;align-items:center;justify-content:center;}}
.note{{background:#FBF3EC;border:1.5px solid #EAD3C4;border-radius:18px;padding:22px 28px;}}
.note .nt{{font-weight:800;font-size:25px;color:#C0592F;margin-bottom:6px;}}
.note .nd{{font-weight:500;font-size:25px;color:#5A5048;line-height:1.45;}}
.ref{{display:inline-block;background:#F0DCCF;color:#9A5A3C;font-weight:700;font-size:22px;
  padding:9px 18px;border-radius:100px;margin-top:18px;}}
"""

def frame(inner, pg, tag="AI 업무 자동화", ep="EP.07 · 출장 숙소 예약", swipe=False, show_pg=True):
    sw = '<div class="swipe">밀어서 보기 →</div>' if swipe else ''
    pgs = f'<span class="pg">{pg} / 7</span>' if show_pg else '<span></span>'
    return f"""<div class="card"><div class="pad">
    <div class="top"><span class="tag">{tag}</span><span class="ep">{ep}</span></div>
    {inner}
    </div>
    {sw}
    <div class="bot"><span class="brand">Co<b>Mind</b>Works</span>{pgs}</div>
    </div>"""


# Card 1: Cover — photo top, headline, chips
c1 = f"""
<img src="{COVER}" style="position:absolute;right:60px;top:560px;width:380px;height:470px;object-fit:cover;border-radius:16px;
  box-shadow:0 30px 70px -20px rgba(80,60,40,.45);transform:rotate(3deg);border:8px solid #fff;">
<div style="margin-top:110px;">
  <div class="kick">직장인 AI 업무 자동화 · 7편</div>
  <div class="h1" style="font-size:96px;">출장 숙소,<br><span class="u">결제 직전</span>까지</div>
  <div class="sub" style="margin-top:26px;max-width:500px;">조건만 적으면 AI가 직접 검색하고<br>비교해서, 결제 앞에서 멈춥니다.</div>
</div>
<div style="position:absolute;left:74px;bottom:180px;display:flex;gap:12px;align-items:center;">
  <span class="chip">출장 조건</span><span class="arrow">→</span><span class="chip">후보 3곳 비교</span>
  <span class="arrow">→</span><span class="chip r">결제 직전 정지</span>
</div>
"""
CARD1 = frame(c1, 1, swipe=True, show_pg=False)

# Card 2: Before — Codex photo
c2 = f"""
<div style="margin-top:50px;">
  <div class="kick">BEFORE</div>
  <div class="h2">숙소 하나 잡는데<br>탭이 열 개</div>
</div>
<img src="{BEFORE}" style="margin-top:36px;width:100%;height:600px;object-fit:cover;border-radius:16px;
  box-shadow:0 30px 70px -22px rgba(80,60,40,.45);border:8px solid #fff;">
<div class="sub" style="margin-top:26px;margin-bottom:150px;">날짜 넣고, 예산 보고, 평점 보고, 조식까지.<br><span class="rust">사이트마다 하나씩 대조</span>하는 반복입니다.</div>
"""
CARD2 = frame(c2, 2)

# Card 3: 핵심 — empty table
c3 = f"""
<div style="margin-top:56px;">
  <div class="kick">핵심은 이겁니다</div>
  <div class="h2">찾을 조건과 함께<br><span class="rust">멈출 지점</span>을 정하기</div>
  <div class="sub" style="margin-top:20px;max-width:880px;">지역·날짜·예산·평점·조식을 적고,<br>"예약자 정보·결제 직전에 멈춰"까지 같이 적어 줍니다.</div>
</div>
<div style="flex:1;display:flex;align-items:flex-end;justify-content:center;margin-bottom:150px;">
  <img src="{TE}" style="width:700px;border-radius:12px;box-shadow:0 26px 64px -18px rgba(80,60,40,.4);border:1px solid #EAE1D2;">
</div>
"""
CARD3 = frame(c3, 3)

# Card 4: After — filled table
c4 = f"""
<div style="margin-top:56px;">
  <div class="kick">AFTER</div>
  <div class="h2">비교표를 받고,<br>결제 앞에서 멈춥니다</div>
</div>
<div style="flex:1;display:flex;align-items:center;justify-content:center;">
  <img src="{TF}" style="width:780px;border-radius:12px;box-shadow:0 30px 70px -20px rgba(80,60,40,.45);border:1px solid #EAE1D2;">
</div>
<div class="sub" style="margin-bottom:150px;">고르면 객실 선택까지 진행하고, <span class="rust">결제는 내가 직접</span>.</div>
"""
CARD4 = frame(c4, 4)

# Card 5: 3 steps
def step(n, t, d):
    return f"""<div style="display:flex;gap:22px;align-items:flex-start;margin-bottom:28px;">
    <div style="flex:none;width:64px;height:64px;border-radius:18px;background:#C0592F;color:#fff;
      font-weight:900;font-size:32px;display:flex;align-items:center;justify-content:center;">{n}</div>
    <div><div style="font-weight:800;font-size:34px;color:#2A241F;">{t}</div>
    <div style="font-weight:500;font-size:26px;color:#6A5F52;margin-top:4px;">{d}</div></div></div>"""
c5 = f"""
<div style="margin-top:56px;">
  <div class="kick">따라 하기 · 딱 3단계</div>
  <div class="h2">이게 전부입니다</div>
</div>
<div style="margin-top:48px;max-width:760px;">
  {step(1, "브라우저 AI 켜기", "Claude in Chrome 또는 에이전트 모드")}
  {step(2, "조건 + 멈출 지점 붙여넣기", "지역·날짜·예산·평점·조식, 결제 직전 정지")}
  {step(3, "비교표 보고 고르기", "객실 선택까지 진행 → 결제는 직접")}
</div>
<div class="ref">[참고] 실제 사이트 검색은 브라우저를 조작하는 AI 기능(유료 플랜)에서 돼요</div>
"""
CARD5 = frame(c5, 5)

# Card 6: summary + 자주 막히는 곳
def bullet(t):
    return f"""<div style="display:flex;gap:16px;align-items:flex-start;margin-bottom:22px;">
    <div style="flex:none;width:38px;height:38px;border-radius:50%;background:#F0DCCF;color:#C0592F;
      font-weight:900;font-size:22px;display:flex;align-items:center;justify-content:center;margin-top:3px;">✓</div>
    <div style="font-weight:600;font-size:31px;color:#3A342E;line-height:1.4;">{t}</div></div>"""
c6 = f"""
<div style="margin-top:56px;">
  <div class="kick">3줄 요약</div>
  <div class="h2">기억할 건 이것만</div>
</div>
<div style="margin-top:46px;max-width:820px;">
  {bullet('검색·비교는 <b>AI가 직접</b> 한다')}
  {bullet('프롬프트에 <b>멈출 지점</b>을 꼭 적는다')}
  {bullet('<b>결제와 개인정보 입력</b>은 사람이 한다')}
</div>
<div style="margin-top:14px;background:#FBF3EC;border:1.5px solid #EAD3C4;border-radius:18px;padding:26px 30px;max-width:820px;">
  <div style="font-weight:800;font-size:25px;color:#C0592F;margin-bottom:6px;">⚠ 자주 막히는 곳</div>
  <div style="font-weight:500;font-size:25px;color:#5A5048;line-height:1.45;">
  사이트마다 <b>평점 척도</b>(5점·10점)가 다르고, <b>세금 별도 요금</b>과 <b>광고 숙소</b>가 섞여요. 프롬프트에 기준을 적어 두세요.</div>
</div>
"""
CARD6 = frame(c6, 6)

# Card 7: CTA
c7 = f"""
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;margin-top:-20px;">
  <div class="kick">무료로 드려요</div>
  <div class="h1" style="font-size:78px;">댓글에 <span class="u">자료</span></div>
  <div class="sub" style="margin-top:26px;">출장 숙소 <span class="rust">프롬프트</span> +<br>연습용 출장 <span class="rust">시나리오 파일</span>을 보내드립니다.</div>
  <div style="margin-top:40px;display:flex;gap:14px;">
    <div style="background:#C0592F;color:#fff;font-weight:800;font-size:30px;padding:20px 34px;border-radius:16px;">댓글 → 자료 받기</div>
    <div style="background:#fff;color:#C0592F;font-weight:800;font-size:30px;padding:20px 30px;border-radius:16px;border:2px solid #E4B9A3;">팔로우 → 다음 편 받기</div>
  </div>
</div>
<img src="{TF}" style="position:absolute;right:50px;bottom:120px;width:380px;border-radius:12px;
  box-shadow:0 26px 64px -18px rgba(80,60,40,.4);transform:rotate(5deg);border:1px solid #EAE1D2;">
"""
CARD7 = frame(c7, 7, show_pg=False)

CARDS = [CARD1, CARD2, CARD3, CARD4, CARD5, CARD6, CARD7]

async def main():
    html = "<!doctype html><html><head><meta charset='utf-8'><style>" + CSS + "</style></head><body>" + "".join(CARDS) + "</body></html>"
    p = pathlib.Path("cards.html"); p.write_text(html, encoding="utf-8")
    outdir = pathlib.Path("../카드"); outdir.mkdir(exist_ok=True)
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=2)
        await pg.goto(p.resolve().as_uri())
        await pg.wait_for_timeout(700)
        els = await pg.query_selector_all(".card")
        for i, el in enumerate(els, 1):
            await el.screenshot(path=str(outdir / f"card_{i:02d}.png"))
        await b.close()
    # 최종 규격 1080x1350으로 다운샘플(2160x2700 → LANCZOS, 크리스프 유지)
    for i in range(1, len(CARDS) + 1):
        fp = outdir / f"card_{i:02d}.png"
        im = Image.open(fp)
        if im.size != (1080, 1350):
            im = im.resize((1080, 1350), Image.LANCZOS)
            im.save(fp)
    print("done", len(CARDS), "cards (1080x1350) ->", outdir.resolve())

asyncio.run(main())
