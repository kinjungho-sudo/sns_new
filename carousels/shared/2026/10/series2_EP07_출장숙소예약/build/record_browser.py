# -*- coding: utf-8 -*-
"""EP07 실제 웹 화면 녹화 — AI가 브라우저를 직접 조작하는 장면.

Playwright로 실제 예약 사이트(부킹닷컴 모바일 화면)를 열어
검색어 입력 → 결과 스크롤 → 조식 필터 → 숙소 열기 → 객실 수 선택 → '지금 예약' 직전 정지
를 진행하며 녹화한다. 화면에 AI 커서·클릭 파동·정지 배너를 그리고, 숙소명은 블러 처리.
결제·개인정보 입력은 하지 않는다.

    python record_browser.py      -> ../short/rec/*.webm (+ 마지막 1장 png)
"""
import asyncio, pathlib, shutil
from playwright.async_api import async_playwright

OUT = pathlib.Path("../short/rec"); OUT.mkdir(parents=True, exist_ok=True)
VW, VH = 1280, 800
SEARCH = ("https://www.booking.com/searchresults.ko.html?ss=%ED%95%B4%EC%9A%B4%EB%8C%80"
          "&checkin=2026-10-14&checkout=2026-10-16&group_adults=1&no_rooms=1&group_children=0&selected_currency=KRW"
          "&nflt=ht_id%3D204%3Bmealplan%3D1%3Breview_score%3D80")

OVERLAY = r"""
(() => {
  const css = `
    #ai-cursor{position:fixed;left:0;top:0;width:34px;height:34px;z-index:2147483647;pointer-events:none;
      transform:translate(-4px,-2px);transition:left .05s linear, top .05s linear;}
    #ai-cursor svg{filter:drop-shadow(0 3px 6px rgba(0,0,0,.35));}
    #ai-tag{display:none;}
    #ai-glow{position:fixed;inset:0;z-index:2147483645;pointer-events:none;box-shadow:inset 0 0 0 3px #D97757, inset 0 0 28px 6px rgba(217,119,87,.45);}
    .ai-ripple{position:fixed;width:16px;height:16px;margin:-8px 0 0 -8px;border-radius:50%;
      border:3px solid #D97757;z-index:2147483646;pointer-events:none;animation:aiR .6s ease-out forwards;}
    @keyframes aiR{to{width:70px;height:70px;margin:-35px 0 0 -35px;opacity:0;}}
    /* hide real property names */
    [data-testid="title"], [data-testid="property-card-title"], h2.pp-header__title, #hp_hotel_name,
    .hprt-roomtype-link, [data-testid="property-header"] h2 {filter:blur(7px)!important;}
  `;
  const add = () => {
    if (document.getElementById('ai-cursor')) return;
    const st = document.createElement('style'); st.textContent = css; document.documentElement.appendChild(st);
    const c = document.createElement('div'); c.id = 'ai-cursor';
    c.innerHTML = '<svg width="34" height="34" viewBox="0 0 24 24"><path d="M4 2l14 9-6.5 1.5L15 20l-2.6 1.2-3.4-7.4L4 18z" fill="#D97757" stroke="#fff" stroke-width="1.6"/></svg>';
    const t = document.createElement('div'); t.id = 'ai-tag'; t.textContent = 'AI';
    document.documentElement.appendChild(c); document.documentElement.appendChild(t);
    const g = document.createElement('div'); g.id = 'ai-glow'; document.documentElement.appendChild(g);
    const mv = (x, y) => { c.style.left = x + 'px'; c.style.top = y + 'px'; t.style.left = (x + 26) + 'px'; t.style.top = (y + 26) + 'px'; };
    mv(window.innerWidth * 0.6, window.innerHeight * 0.4);
    addEventListener('mousemove', e => mv(e.clientX, e.clientY), true);
    addEventListener('mousedown', e => { const r = document.createElement('div'); r.className = 'ai-ripple';
      r.style.left = e.clientX + 'px'; r.style.top = e.clientY + 'px'; document.documentElement.appendChild(r);
      setTimeout(() => r.remove(), 700); }, true);
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', add); else add();
  if (location.pathname.includes('/hotel/')) {
    const hide = () => {
      const name = (document.title.split(',')[0] || '').trim();
      if (!name || name.length < 2 || !document.body) return;
      const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
      while (w.nextNode()) { const t = w.currentNode; if (t.nodeValue.includes(name) && t.parentElement) t.parentElement.style.filter = 'blur(7px)'; }
    };
    const st2 = document.createElement('style'); st2.textContent = 'h1,h2{filter:blur(7px)!important}';
    (document.head || document.documentElement).appendChild(st2);
    setInterval(hide, 80);
  }
})();
"""

BLUR_NAME = r"""() => {
  const name = (document.title.split(',')[0] || '').trim();
  if (!name || name.length < 2) return 0;
  let n = 0;
  const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const hits = [];
  while (w.nextNode()) { if (w.currentNode.nodeValue.includes(name)) hits.push(w.currentNode.parentElement); }
  hits.forEach(el => { el.style.filter = 'blur(7px)'; n++; });
  return n;
}"""

BANNER = r"""(text) => {
  const b = document.createElement('div');
  b.style.cssText = 'position:fixed;left:50%;transform:translateX(-50%);bottom:40px;z-index:2147483647;background:#D97757;color:#fff;' +
    'font:800 26px sans-serif;padding:18px 34px;border-radius:16px;box-shadow:0 10px 30px rgba(0,0,0,.35);text-align:center;';
  b.textContent = text; document.documentElement.appendChild(b);
}"""


async def glide(page, x, y, steps=18):
    await page.mouse.move(x, y, steps=steps)
    await page.wait_for_timeout(250)


async def click_el(page, loc, pause=600):
    box = await loc.bounding_box()
    if not box:
        return False
    x, y = box["x"] + box["width"] / 2, box["y"] + box["height"] / 2
    await glide(page, x, y)
    await page.mouse.down(); await page.mouse.up()
    await page.wait_for_timeout(pause)
    return True


async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch(headless=False, args=["--lang=ko-KR"])
        ctx = await b.new_context(
            viewport={"width": VW, "height": VH}, device_scale_factor=1, locale="ko-KR",
            record_video_dir=str(OUT), record_video_size={"width": VW, "height": VH})
        await ctx.add_init_script(OVERLAY)
        page = await ctx.new_page()

        # 1) home → type destination like a person
        await page.goto("https://www.booking.com/index.ko.html", wait_until="domcontentloaded")
        await page.wait_for_timeout(1800)
        for _ in range(10):
            try:
                closed = await page.evaluate("""() => {
              const b = [...document.querySelectorAll('[role=dialog] button, [aria-modal=true] button')].find(x => {
                const l = (x.getAttribute('aria-label') || '') + ' ' + (x.textContent || '');
                return /닫기|close|dismiss|나중에|×/i.test(l) && x.offsetParent !== null;
              });
              if (b) { b.click(); return true; } return false; }""")
            except Exception:
                closed = False
            if closed:
                break
            await page.wait_for_timeout(300)
        await page.wait_for_timeout(800)
        for sel in ["button:has-text('동의')", "#onetrust-reject-all-handler", "button[aria-label*='닫기']"]:
            try:
                el = page.locator(sel).first
                if await el.is_visible(timeout=800):
                    await click_el(page, el, 400)
            except Exception:
                pass
        dest = page.locator("input[name='ss'], input[placeholder*='여행지']").first
        try:
            await click_el(page, dest, 500)
            await page.keyboard.type("해운대", delay=220)
            await page.wait_for_timeout(1200)
        except Exception as e:
            print("dest input skipped:", e)

        # 2) results (direct URL with dates/guests — same as pressing search)
        await page.goto(SEARCH, wait_until="domcontentloaded")
        await page.wait_for_timeout(1500)
        # dismiss the "open in app" bottom sheet if it shows up
        for _ in range(6):
            try:
                closed = await page.evaluate("""() => {
              const b = [...document.querySelectorAll('[role=dialog] button, [aria-modal=true] button')].find(x => {
                const l = (x.getAttribute('aria-label') || '') + ' ' + (x.textContent || '');
                return /닫기|close|dismiss|나중에|×/i.test(l) && x.offsetParent !== null;
              });
              if (b) { b.click(); return true; } return false; }""")
            except Exception:
                closed = False
            await page.keyboard.press("Escape")
            if closed:
                break
            await page.wait_for_timeout(400)
        await page.wait_for_timeout(1500)
        await glide(page, VW * 0.55, VH * 0.6)
        await page.evaluate(BANNER, "조건: 조식 포함 · 평점 8+ · 1박 12만원 이하")
        await page.wait_for_timeout(1200)
        await page.evaluate("() => document.querySelectorAll('div').forEach(d => { if (d.textContent.startsWith('조건: ')) d.remove(); })")
        for _ in range(4):
            await page.mouse.wheel(0, 380); await page.wait_for_timeout(700)
        await page.mouse.wheel(0, -1520); await page.wait_for_timeout(900)

        # 3) breakfast filter if visible
        try:
            f = page.get_by_text("조식 포함", exact=False).first
            if await f.is_visible(timeout=1500):
                await click_el(page, f, 2500)
        except Exception as e:
            print("filter skipped:", e)

        # 4) open first property card
        card = page.locator("[data-testid='property-card'] a, a[data-testid='title-link']").first
        href = None
        try:
            href = await card.get_attribute("href")
            await click_el(page, card, 300)
        except Exception as e:
            print("card click failed:", e)
        if href:
            if href.startswith("/"):
                href = "https://www.booking.com" + href
            await page.goto(href, wait_until="commit")
            for _ in range(40):
                try:
                    await page.evaluate(BLUR_NAME)
                except Exception:
                    pass
                await page.wait_for_timeout(100)
            print("hotel page t-mark")
        await page.wait_for_timeout(3000)
        print("blurred", await page.evaluate(BLUR_NAME))
        await page.wait_for_timeout(500)
        await page.mouse.wheel(0, 350); await page.wait_for_timeout(800)

        # 5) availability block: hover the check/reserve button, then STOP
        try:
            btn = page.locator("button:has-text('객실 확인'), button:has-text('예약'), a:has-text('객실 선택')").first
            await btn.scroll_into_view_if_needed(timeout=4000); await page.wait_for_timeout(900)
            box = await btn.bounding_box()
            if box:
                await glide(page, box["x"] + box["width"] / 2, box["y"] + box["height"] / 2, steps=24)
                await page.wait_for_timeout(600)
        except Exception as e:
            print("reserve hover skipped:", e)
        await page.evaluate(BANNER, "❚❚ 결제 직전에서 멈췄습니다 · 결제는 사람이 직접")
        await page.wait_for_timeout(3000)
        await page.screenshot(path=str(OUT / "last.png"))
        await ctx.close(); await b.close()
    vids = sorted(OUT.glob("*.webm"), key=lambda p: p.stat().st_mtime)
    if vids:
        shutil.copy(vids[-1], OUT / "booking_take.webm")
        print("video:", (OUT / "booking_take.webm").resolve())

asyncio.run(main())
