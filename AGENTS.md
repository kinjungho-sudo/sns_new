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
