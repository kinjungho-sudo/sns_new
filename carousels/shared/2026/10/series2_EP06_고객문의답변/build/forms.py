# -*- coding: utf-8 -*-
"""고객 문의 답변 초안 양식 렌더 — 빈 양식(templ_empty) / 채운 양식(templ_filled).
실명·실제 회사명은 넣지 않는다(가공 예시). 기준으로 확정 못 하는 항목은 '내부 확인사항'으로 분리."""
import asyncio, pathlib
from playwright.async_api import async_playwright

FONT = pathlib.Path("font.css").read_text(encoding="utf-8")

CSS = f"""
{FONT}
*{{margin:0;padding:0;box-sizing:border-box;}}
.paper{{width:940px;background:#FBF8F1;font-family:'A2Z';color:#2A241F;
  padding:48px 52px 50px;position:relative;}}
.head{{display:flex;align-items:center;gap:16px;border-bottom:2px solid #E6DDCD;padding-bottom:22px;}}
.doc{{flex:1;font-weight:900;font-size:36px;letter-spacing:2px;}}
.doc u{{text-decoration:none;background:linear-gradient(transparent 60%, #E4B9A3 60%);padding:0 6px;}}
.pill{{flex:none;background:#C0592F;color:#fff;font-weight:800;font-size:18px;padding:9px 18px;border-radius:100px;}}
.lab{{display:inline-flex;align-items:center;gap:8px;font-weight:800;font-size:22px;margin:26px 0 12px;}}
.lab .dot{{width:12px;height:12px;border-radius:50%;background:#C0592F;}}
.lab.send .dot{{background:#2F8F6B;}}
.field{{display:flex;gap:14px;font-size:20px;margin-bottom:10px;}}
.field .k{{flex:none;width:92px;font-weight:700;color:#8A7F72;}}
.field .v{{flex:1;font-weight:600;border-bottom:1.5px solid #E0D6C5;padding-bottom:7px;min-height:30px;}}
.body{{border:1.5px solid #E0D6C5;border-radius:12px;background:#fff;padding:22px 24px;font-size:19px;
  line-height:1.62;font-weight:500;color:#3A342E;min-height:214px;}}
.body .row{{display:flex;gap:10px;margin-bottom:9px;}}
.body .row b{{color:#C0592F;font-weight:800;flex:none;}}
.sign{{margin-top:14px;font-weight:700;color:#6A5F52;text-align:right;}}
.inbox{{margin-top:24px;background:#FBF3EC;border:1.6px solid #EAD3C4;border-radius:14px;padding:20px 24px;}}
.inbox .t{{font-weight:800;font-size:20px;color:#C0592F;margin-bottom:12px;display:flex;align-items:center;gap:8px;}}
.inbox .it{{display:flex;gap:12px;font-size:18px;font-weight:600;color:#5A5048;line-height:1.4;margin-bottom:10px;}}
.inbox .it:last-child{{margin-bottom:0;}}
.inbox .it .m{{flex:none;color:#C0592F;font-weight:900;}}
.blank{{color:transparent;}}
.bl{{display:inline-block;border-bottom:1.5px solid #E0D6C5;min-width:240px;height:22px;vertical-align:middle;}}
"""

def build(filled: bool):
    if filled:
        subject = "사내 AI 기초교육 문의 안내드립니다"
        rows = [
            ("안내", "안녕하세요, 담당자님. 교육운영팀입니다."),
            ("교육비", "18명 기준 1회 90만원 (부가세 별도)"),
            ("출장비", "서울 지역 출장비 없음"),
            ("준비물", "교육장·인터넷·빔프로젝터 / 실습자 노트북·계정"),
            ("교육자료", "교육 후 PDF로 제공"),
        ]
        sign = "교육운영팀 드림"
        internal = [
            "희망 일정(○월 ○일)은 강사 일정 확인 후 확정 — 가능하다고 약속하지 않음",
        ]
    else:
        subject = None
        rows = []
        sign = None
        internal = None

    if filled:
        body_rows = "".join(
            f'<div class="row"><b>{k}</b><span>{v}</span></div>' for k, v in rows
        )
        body = f'{body_rows}<div class="sign">{sign}</div>'
        subj_v = subject
        inbox_items = "".join(
            f'<div class="it"><span class="m">!</span><span>{t}</span></div>'
            for t in internal
        )
        inbox = f'<div class="inbox"><div class="t">🔒 내부 확인사항 · 고객에게 보내지 않음</div>{inbox_items}</div>'
    else:
        body = ('<div class="row"><span class="bl" style="min-width:680px;"></span></div>'
                '<div class="row"><span class="bl" style="min-width:620px;"></span></div>'
                '<div class="row"><span class="bl" style="min-width:650px;"></span></div>'
                '<div class="row"><span class="bl" style="min-width:560px;"></span></div>'
                '<div class="sign"><span class="bl" style="min-width:220px;"></span></div>')
        subj_v = '<span class="bl" style="min-width:420px;"></span>'
        inbox = ('<div class="inbox"><div class="t">🔒 내부 확인사항 · 고객에게 보내지 않음</div>'
                 '<div class="it"><span class="m">!</span><span class="bl" style="min-width:560px;"></span></div></div>')

    return f"""<div class="paper">
  <div class="head"><div class="doc">고객 문의 <u>답변 초안</u></div><div class="pill">AI 작성 · 사람 검토 후 발송</div></div>
  <div class="lab send"><span class="dot"></span>고객 발송용</div>
  <div class="field"><div class="k">제목</div><div class="v">{subj_v}</div></div>
  <div class="body">{body}</div>
  {inbox}
</div>"""

async def render(name, filled):
    html = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{build(filled)}</body></html>"
    p = pathlib.Path(f"_form_{name}.html"); p.write_text(html, encoding="utf-8")
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        pg = await b.new_page(device_scale_factor=2)
        await pg.goto(p.resolve().as_uri()); await pg.wait_for_timeout(400)
        el = await pg.query_selector(".paper")
        await el.screenshot(path=f"{name}.png")
        await b.close()
    print("rendered", name)

async def main():
    await render("templ_empty", False)
    await render("templ_filled", True)

asyncio.run(main())
