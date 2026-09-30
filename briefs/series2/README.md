# series2 · AI 업무 자동화 — Brief Inbox

이 폴더는 **Claude(클라우드 세션)가 기획서를 넣는 인박스**이고,
**Buzz 쪽 Codex가 이 폴더를 읽어 캐러셀·배포자료를 생산·게시**하는 지점입니다.

## 흐름

1. Claude가 다음에 만들 에피소드를 정하고, 이 폴더에 `EPNN_주제.md` 브리프 파일을 커밋한다.
2. Codex(Buzz)는 이 폴더의 새 브리프를 확인해 카드(7장), 배포자료(양식+프롬프트), 캡션을 생산한다.
3. 결과물은 `carousels/shared/YYYY/MM/series2_EPNN_주제/`에 저장한다. 하위에 반드시:
   - `카드/` (PNG 7장, 1080x1350)
   - `배포자료/` (실제 원본 양식 파일 그대로 + `프롬프트.md` 완성형 단일 프롬프트)
   - `캡션.txt`
4. Codex가 게시까지 처리하면 브리프 파일 상단에 `status: published`로 표시하고 게시일을 남긴다.
5. Claude는 `배포자료/`가 새로 생기면 이를 가져와 Notion 배포 페이지([[comindworks-notion-practice-page]] 스킬)에 자동 반영한다.

## 브리프 규칙 (Claude가 작성)

- 실제 검증된 원본 자료(사용자가 준 실습 자료) 기준으로만 작성 — 텍스트로 새로 지어내지 않는다.
- 디자인 톤은 `codex-skills/instagram-carousel*`가 아니라, series2 전용 크림/러스트(A2Z 폰트) 톤을 따른다 — `anthropic-skills:sns-automation-carousel` 참고.
- 카드에는 프롬프트/양식 본문을 넣지 않는다 (배포자료로만 전달, 댓글→DM 퍼널 유지).

## 파일명 규칙

`EPNN_주제.md` (예: `EP03_견적서.md`)
