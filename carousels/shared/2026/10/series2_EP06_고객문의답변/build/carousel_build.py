# -*- coding: utf-8 -*-
"""EP.06 고객 문의 답변 초안 — 7장 캐러셀 빌드 (크림/러스트·A2Z·Before→After, Parro/핸들/실명 제외)."""
import asyncio, pathlib, base64
from playwright.async_api import async_playwright

FONT = pathlib.Path("font.css").read_text(encoding="utf-8")

def b64(p):
    return "data:image/png;base64," + base64.b64encode(pathlib.Path(p).read_bytes()).decode()

TE = b64("templ_empty.png")
TF = b64("templ_filled.png")

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

def frame(inner, pg, tag="AI 업무 자동화", ep="EP.06 · 고객 문의 답변", swipe=False, show_pg=True):
    sw = '<div class="swipe">밀어서 보기 →</div>' if swipe else ''
    pgs = f'<span class="pg">{pg} / 7</span>' if show_pg else '<span></span>'
    return f"""<div class="card"><div class="pad">
    <div class="top"><span class="tag">{tag}</span><span class="ep">{ep}</span></div>
    {inner}
    </div>
    {sw}
    <div class="bot"><span class="brand">Co<b>Mind</b>works</span>{pgs}</div>
    </div>"""

# Card 1: Cover
c1 = f"""
<div style="margin-top:140px;">
  <div class="kick">직장인 AI 업무 자동화 · 6편</div>
  <div class="h1">문의 메일에<br><span class="u">답장 초안</span>까지</div>
  <div class="sub" style="margin-top:26px;max-width:610px;">회사 응대 기준을 읽혀,<br>보낼 답변과 내부 확인사항을 나눠서 자동으로.</div>
</div>
<img src="{TF}" style="position:absolute;right:48px;bottom:250px;width:440px;border-radius:14px;
  box-shadow:0 30px 70px -20px rgba(80,60,40,.45);transform:rotate(4deg);border:1px solid #EAE1D2;">
<div style="position:absolute;left:74px;bottom:180px;display:flex;gap:12px;align-items:center;">
  <span class="chip">문의 메일</span><span class="chip">응대 기준</span>
  <span class="arrow">→</span><span class="chip r">답장 초안</span>
</div>
"""
CARD1 = frame(c1, 1, swipe=True, show_pg=False)

# Card 2: Before (받은 메일 목업)
c2 = f"""
<div style="margin-top:50px;">
  <div class="kick">BEFORE</div>
  <div class="h2">문의 한 통에<br>물어보는 건 다섯 가지</div>
</div>
<div class="mail" style="margin-top:40px;">
  <div class="mh"><span class="ic">@</span>
    <div><div class="ti">사내 AI 기초교육 문의드립니다</div>
    <div class="fr">고객사 인사팀 → 교육운영팀</div></div></div>
  <div class="mb">
    <div class="q"><span class="b">?</span>이 일정에 교육이 가능한가요</div>
    <div class="q"><span class="b">?</span>교육비와 준비물은 무엇인가요</div>
    <div class="q"><span class="b">?</span>할인은 받을 수 있나요</div>
    <div class="q"><span class="b">?</span>교육 자료도 받을 수 있나요</div>
  </div>
</div>
<div class="sub" style="margin-top:28px;margin-bottom:150px;">답하려면 <span class="rust">회사 기준 문서를 매번 뒤져</span><br>손으로 하나씩 맞춰 써야 합니다.</div>
"""
CARD2 = frame(c2, 2)

# Card 3: 핵심 — empty form
c3 = f"""
<div style="margin-top:56px;">
  <div class="kick">핵심은 이겁니다</div>
  <div class="h2">회사 기준 그대로 읽히고<br>못 정하는 건 빼게 하기</div>
  <div class="sub" style="margin-top:20px;max-width:560px;">확정할 수 있는 것만 답하고,<br><span class="rust">할인·일정은 약속 말고</span> 내부 확인으로.</div>
</div>
<img src="{TE}" style="position:absolute;right:56px;bottom:150px;width:500px;border-radius:12px;
  box-shadow:0 26px 64px -18px rgba(80,60,40,.4);border:1px solid #EAE1D2;">
"""
CARD3 = frame(c3, 3)

# Card 4: After — filled form
c4 = f"""
<div style="margin-top:56px;">
  <div class="kick">AFTER</div>
  <div class="h2">문의만 넣으면<br>이렇게 나뉩니다</div>
</div>
<div style="flex:1;display:flex;align-items:center;justify-content:center;">
  <img src="{TF}" style="width:640px;border-radius:12px;
    box-shadow:0 30px 70px -20px rgba(80,60,40,.45);border:1px solid #EAE1D2;">
</div>
<div class="sub" style="margin-bottom:150px;">고객 발송용 답변과 <span class="rust">내부 확인사항</span>이<br>처음부터 따로 나옵니다.</div>
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
<div style="margin-top:48px;max-width:720px;">
  {step(1, "프롬프트 붙여넣기", "문의 메일과 회사 기준을 함께 올리기")}
  {step(2, "답변 초안 받기", "발송용 답변 + 내부 확인사항으로 분리")}
  {step(3, "Skill로 저장하기", "다음 문의부터 같은 규칙으로 재사용")}
</div>
<div class="ref">[참고] 무료 ChatGPT는 하루 파일 3개 한도 · 한 번에 여러 파일 되는 Claude면 수월</div>
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
<div style="margin-top:46px;max-width:780px;">
  {bullet('답장은 <b>회사 기준을 먼저 읽히는</b> 게 시작이다')}
  {bullet('<b>못 정하는 건 약속 말고</b> 내부 확인으로 뺀다')}
  {bullet('한 번 만든 규칙은 <b>Skill로 저장</b>해 재사용한다')}
</div>
<div style="margin-top:14px;background:#FBF3EC;border:1.5px solid #EAD3C4;border-radius:18px;
  padding:26px 30px;max-width:780px;">
  <div style="font-weight:800;font-size:25px;color:#C0592F;margin-bottom:6px;">⚠ 자주 막히는 곳</div>
  <div style="font-weight:500;font-size:25px;color:#5A5048;line-height:1.45;">
  할인·일정을 AI가 덜컥 약속할 수 있어요. <b>'확정 못 하면 내부 확인으로'</b> 규칙을 꼭 넣고, 초안은 사람이 검토 후 보내세요.</div>
</div>
"""
CARD6 = frame(c6, 6)

# Card 7: CTA
c7 = f"""
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;margin-top:-20px;">
  <div class="kick">무료로 드려요</div>
  <div class="h1" style="font-size:78px;">댓글에 <span class="u">자료</span></div>
  <div class="sub" style="margin-top:26px;">답장 초안 <span class="rust">프롬프트</span> +<br>예제 문의·응대 기준 <span class="rust">파일</span>을 보내드립니다.</div>
  <div style="margin-top:40px;display:flex;gap:14px;">
    <div style="background:#C0592F;color:#fff;font-weight:800;font-size:30px;padding:20px 34px;border-radius:16px;">댓글 → 자료 받기</div>
    <div style="background:#fff;color:#C0592F;font-weight:800;font-size:30px;padding:20px 30px;border-radius:16px;border:2px solid #E4B9A3;">팔로우 → 다음 편 받기</div>
  </div>
</div>
<img src="{TF}" style="position:absolute;right:50px;bottom:120px;width:360px;border-radius:12px;
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
    print("done", len(CARDS), "cards ->", outdir.resolve())

asyncio.run(main())
