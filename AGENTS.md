# SNS Codex Operating Guide

This repository is the shared Windows/Mac mini operating base for CoMindWorks SNS carousel production.

## Default Workflow

- Use `instagram-carousel-scene-overlay` by default for Korean `AI와 함께하는 1인 창업 도전기` carousel work unless the user explicitly asks for another style.
- Keep prior versions. Create a new versioned output directory instead of overwriting an earlier package.
- Put shared/current work under `carousels/shared/`.
- Preserve the CoMindWorks defaults unless the user changes them: `CoMindWorks`, `comindworks`, no subtitle, no profile photo, teal accent, dark style.
- Public SNS deliverables should avoid unnecessary real names, company names, or place references. Use anonymized wording such as `마케팅 회사 임 대표` when needed.

## Visual Standard

- Use story-specific full-bleed editorial scenes, not repeated text panels.
- Add a lower black gradient/progressive blur for legibility.
- Use restrained Korean typography, white text, one muted-orange rounded underline, and a small page counter.
- Prefer objects, workspaces, real UI, documents, evidence scenes, diagrams, timelines, and emotional moments.
- Avoid decorative charts, generic icon grids, robots, neon cyberpunk, and repetitive template panels.

## Required Deliverables

- Editable HTML source.
- Local assets used by the HTML.
- Final `1080x1350` PNG exports.
- Contact sheet.
- PNG-only ZIP containing the final card PNGs.
- `caption.md` and relevant copy/design notes when applicable.

## Verification Before Handoff

- Confirm PNG count and `1080x1350` dimensions.
- Confirm ZIP entry count matches final PNG count.
- Confirm the contact sheet exists.
- Scan visible copy for unwanted real names, forbidden brand/profile strings, and stale repeated material.
- If Korean text is read or validated in Windows PowerShell, set `PYTHONUTF8=1` to avoid `cp949` corruption.

## series2 · AI 업무 자동화 (별도 트랙 — 위 Default Workflow와 다름)

`series2 'AI 업무 자동화'`는 시리즈1(1인창업 도전기)과 완전히 다른 톤/퍼널을 쓰는 별도 트랙이다. 위 "Default Workflow"와 "Visual Standard"는 시리즈1 전용이며, series2에는 적용하지 않는다.

- **입력(브리프) 채널**: Claude(클라우드 세션)가 `briefs/series2/EPNN_주제.md`에 기획서를 커밋해서 넣는다. `briefs/series2/_TEMPLATE.md` 형식을 따른다. Codex는 이 폴더의 새 브리프를 작업 대상으로 삼는다.
- **톤/스타일**: 크림(#ECE6D8) 배경 + 러스트(#C0592F) 포인트, A2Z 폰트. 직장인 대상 Before→After 7장 구조. 자세한 디자인 토큰·7장 구조는 `codex-skills/sns-automation-carousel/`(없으면 Claude 쪽 `anthropic-skills:sns-automation-carousel` 스킬 내용을 요청해서 동기화) 참고.
- **카드에 프롬프트/양식 노출 금지**: series2는 "결과물만 카드에 보여주고, 양식·프롬프트는 댓글→DM 자동화로만 배포"하는 리드 퍼널이다. 절대 카드 안에 프롬프트 전문이나 빈 양식 전체를 넣지 않는다.
- **산출 위치**: `carousels/shared/YYYY/MM/series2_EPNN_주제/` 아래에
  - `카드/` (PNG 7장, 1080x1350) + 컨택트시트
  - `배포자료/` — **사용자가 제공한 실제 원본 파일을 그대로** 넣는다(양식.docx 등을 텍스트로 재구성하지 않음) + `프롬프트.md`(한 번에 완성되는 단일 프롬프트, 원본에 없는 내용 임의 생성 금지 · 모르면 "확인 필요" 규칙 포함)
  - `캡션.txt`
- **완료 표시**: 브리프 파일(`briefs/series2/EPNN_주제.md`) 상단 frontmatter의 `status`를 `draft → ready → in_production → published`로 갱신한다. 게시까지 Codex가 처리했다면 `published`로 두고 게시일/링크를 파일 하단에 남긴다.
- **Claude 쪽 연동**: `배포자료/`가 새로 생기면 Claude가 이를 읽어 Notion 배포 페이지에 자동 반영한다(Claude 쪽 `comindworks-notion-practice-page` 스킬). 그러니 `배포자료/` 폴더명과 파일명은 위 규칙을 반드시 지킬 것 — 형식이 바뀌면 자동 반영이 깨진다.

## Skills

Repo copies of the reusable Codex skills live in `codex-skills/`.

To install them into the local Codex home, run:

```bash
bash scripts/install-codex-skills.sh
```

On Windows PowerShell:

```powershell
.\scripts\install-codex-skills.ps1
```
