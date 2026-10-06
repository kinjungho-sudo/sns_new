# -*- coding: utf-8 -*-
"""EP03: replace card_01, rebuild 카드_PNG.zip (card_01..07) and 컨택트시트.png (4x2, 1500x936)."""
import sys, pathlib, zipfile
from PIL import Image

carddir = pathlib.Path(sys.argv[1])            # .../series2_EP03_폴더파일정리/카드
new_c1  = pathlib.Path(sys.argv[2])            # rebuilt card_01.png (1080x1350)
epdir   = carddir.parent

# 1) replace card_01
Image.open(new_c1).convert("RGB").save(carddir / "card_01.png")

# 2) verify all 7 are 1080x1350
cards = [carddir / f"card_{i:02d}.png" for i in range(1, 8)]
for c in cards:
    w, h = Image.open(c).size
    assert (w, h) == (1080, 1350), f"{c.name} is {w}x{h}"

# 3) rebuild card ZIP (only card_*.png)
zp = epdir / "카드_PNG.zip"
with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
    for c in cards:
        z.write(c, arcname=c.name)

# 4) rebuild contact sheet 4 cols x 2 rows -> 1500x936
cols, rows = 4, 2
cw, ch = 375, 468
sheet = Image.new("RGB", (1500, 936), (236, 230, 216))
for idx, c in enumerate(cards):
    r, col = divmod(idx, cols)
    thumb = Image.open(c).convert("RGB").resize((cw, ch), Image.LANCZOS)
    sheet.paste(thumb, (col * cw, r * ch))
sheet.save(carddir / "컨택트시트.png")

print("OK", epdir.name, "zip entries:",
      len(zipfile.ZipFile(zp).namelist()), "contact:", Image.open(carddir / "컨택트시트.png").size)
