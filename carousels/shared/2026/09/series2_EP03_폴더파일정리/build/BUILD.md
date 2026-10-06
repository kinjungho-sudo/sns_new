# EP03 표지(card_01) 재빌드 소스

card_01 표지의 "정리 완료" 패널이 프레임 오른쪽 끝에 잘리던 노-블리드 FAIL을
고친 재현 소스. 패널을 `width:398px · right:56px`로 당겨 안전여백(≥24px)을 확보하고,
2x 렌더 후 1080×1350으로 다운스케일해 나머지 6장과 해상도를 맞춘다.

## 파일
- `card_01_rebuild.py` — 표지 1장 렌더(frame/CSS는 sns-carousel-build 레퍼런스와 동일 토큰).
- `regen.py` — 렌더된 card_01을 카드 폴더에 반영하고 `카드_PNG.zip`(card_01~07)·`컨택트시트.png`(4×2, 1500×936) 재생성.
- `font.css` — A2Z 9웨이트 @font-face(해시 파일명 매핑). **폰트 바이너리(.ttf)는 상용 폰트라 커밋하지 않는다.**

## 재현 절차
```bash
# 1) 폰트 스테이징 (커밋 안 함): A2Z 9종을 build/fonts/ 로 복사
#    출처: D:/project/sns_claude/_system/fonts (font.css가 참조하는 해시 파일명)
mkdir -p fonts && cp /d/project/sns_claude/_system/fonts/*_____*.ttf fonts/

# 2) 표지 렌더 → out/card_01.png (1080×1350)
python card_01_rebuild.py

# 3) 카드 폴더 반영 + zip/컨택트시트 재생성
python regen.py "../카드" out/card_01.png

# 4) 노-블리드 게이트 (EXIT 0 = 통과)
python "$HOME/.claude/skills/sns-carousel-build/scripts/check_bleed.py" ../카드
```

## 검증 결과 (2026-10-06, 커밋 fe6aa11 기준)
- 노-블리드 게이트: card_01~07 모두 `ok`, `PASS`, EXIT 0
- 카드 7장 전부 1080×1350, `카드_PNG.zip` 7엔트리, 컨택트시트 1500×936
