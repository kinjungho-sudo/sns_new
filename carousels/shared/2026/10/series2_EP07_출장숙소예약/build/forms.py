# -*- coding: utf-8 -*-
"""출장 숙소 후보 비교표 렌더 — 빈 표(templ_empty) / 채운 표(templ_filled).
실제 숙소명·업체명은 쓰지 않는다(A/B/C 호텔). 값은 실행검증(2026-10-13) 결과를 반올림한 예시."""
import asyncio, pathlib
from playwright.async_api import async_playwright

FONT = pathlib.Path("font.css").read_text(encoding="utf-8")

CSS = f"""
{FONT}
*{{margin:0;padding:0;box-sizing:border-box;}}
.paper{{width:940px;background:#FBF8F1;font-family:'A2Z';color:#2A241F;padding:44px 48px 46px;}}
.head{{display:flex;align-items:center;gap:16px;border-bottom:2px solid #E6DDCD;padding-bottom:20px;}}
.doc{{flex:1;font-weight:900;font-size:34px;letter-spacing:1px;}}
.doc u{{text-decoration:none;background:linear-gradient(transparent 60%, #E4B9A3 60%);padding:0 6px;}}
.pill{{flex:none;background:#C0592F;color:#fff;font-weight:800;font-size:17px;padding:9px 16px;border-radius:100px;}}
.cond{{display:flex;flex-wrap:wrap;gap:8px;margin:20px 0 18px;}}
.cond span{{background:#F0DCCF;color:#9A5A3C;font-weight:700;font-size:17px;padding:7px 14px;border-radius:100px;}}
table{{width:100%;border-collapse:separate;border-spacing:0;font-size:19px;background:#fff;
  border:1.5px solid #E0D6C5;border-radius:12px;overflow:hidden;}}
th{{background:#F4EEE2;font-weight:800;color:#6A5F52;text-align:left;padding:14px 14px;font-size:17px;}}
td{{padding:15px 14px;border-top:1px solid #EFE7DA;font-weight:600;color:#3A342E;height:58px;}}
tr.best td{{background:#FBF1E9;}}
tr.best td:first-child{{border-left:5px solid #C0592F;}}
.badge{{display:inline-block;background:#C0592F;color:#fff;font-weight:800;font-size:14px;padding:3px 9px;border-radius:100px;margin-left:6px;vertical-align:middle;}}
.yes{{color:#2F8F6B;font-weight:800;}}
.no{{color:#A99D8E;}}
.bl{{display:inline-block;border-bottom:1.5px solid #E0D6C5;width:90%;height:20px;}}
.stop{{margin-top:22px;display:flex;gap:16px;align-items:center;background:#FBF3EC;border:1.6px solid #EAD3C4;
  border-radius:14px;padding:18px 22px;}}
.stop .ic{{flex:none;width:52px;height:52px;border-radius:14px;background:#C0592F;color:#fff;font-weight:900;font-size:26px;
  display:flex;align-items:center;justify-content:center;}}
.stop .t{{font-weight:800;font-size:21px;color:#C0592F;}}
.stop .d{{font-weight:600;font-size:18px;color:#5A5048;margin-top:3px;}}
.note{{margin-top:12px;font-size:15px;color:#9A8F82;font-weight:500;}}
"""

ROWS = [
    ("A 호텔", "13.4만원", "8.6 / 10", True, "해운대 · 역 도보", True),
    ("B 호텔", "16.6만원", "8.4 / 10", False, "해운대 해변 인근", False),
    ("C 호텔", "19.3만원", "8.6 / 10", False, "해운대 중심가", False),
]


def build(filled: bool):
    head = ("<tr><th style='width:22%'>숙소</th><th style='width:18%'>2박 요금</th><th style='width:17%'>평점</th>"
            "<th style='width:13%'>조식</th><th>위치</th></tr>")
    if filled:
        body = ""
        for name, price, score, bf, loc, best in ROWS:
            badge = '<span class="badge">추천</span>' if best else ""
            bfs = '<span class="yes">포함</span>' if bf else '<span class="no">미포함</span>'
            body += f"<tr class='{'best' if best else ''}'><td><b>{name}</b>{badge}</td><td>{price}</td><td>{score}</td><td>{bfs}</td><td>{loc}</td></tr>"
        stop = ('<div class="stop"><div class="ic">II</div><div><div class="t">객실 선택 화면에서 멈췄습니다</div>'
                '<div class="d">A 호텔 · 스탠다드 더블 · 2박 조식 포함 — 예약자 정보와 결제는 직접 확인해 주세요</div></div></div>'
                '<div class="note">2026-10-13 검증 당시 표시 요금 · 10점 척도 평점은 5점 기준 4.0 = 8.0으로 환산</div>')
    else:
        body = "".join("<tr>" + "".join("<td><span class='bl'></span></td>" for _ in range(5)) + "</tr>" for _ in range(3))
        stop = ('<div class="stop"><div class="ic">II</div><div><div class="t">결제 직전에서 멈추기</div>'
                '<div class="d"><span class="bl" style="width:520px;"></span></div></div></div>')
    return f"""<div class="paper">
  <div class="head"><div class="doc">출장 숙소 <u>후보 비교</u></div><div class="pill">AI 검색 · 결제는 사람</div></div>
  <div class="cond"><span>부산 해운대</span><span>10/14~16 · 2박 · 1인</span><span>1박 12만원 이하</span><span>평점 4.0+</span><span>조식 선호</span></div>
  <table>{head}{body}</table>
  {stop}
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
