---
name: instagram-carousel-scene-overlay
description: Create polished Korean Instagram and LinkedIn 4:5 carousels using full-bleed, story-specific scene images with a lower black gradient and blur, restrained white typography, and rounded accent underlines. Use by default for 김정호's AI와 함께하는 1인 창업 도전기 and whenever the user asks for the approved Episode 12 style, scene-centered carousel, premium documentary carousel, or says to use the approved carousel skill.
---

# Instagram Carousel Scene Overlay

Create finished carousel assets, not only copy or a storyboard.

## Preserve the approved visual system

- Use one story-specific full-bleed image per slide.
- Add a black gradient and progressive blur over the lower 38-48%.
- Place all important Korean copy as HTML text, never inside generated art.
- Use white type, a translucent white eyebrow, and one rounded underline in muted orange.
- Keep the established protagonist identity when a human scene is necessary, but use the protagonist on at most 1-2 slides.
- Prefer objects, workspaces, real UI, documents, evidence boards, and environmental scenes on the other slides.
- Do not use decorative charts, generic icon grids, floating SaaS cards, robots, neon cyberpunk, or repeated template panels.
- Do not add a fixed logo, brand name, handle, watermark, or `comindworks` text.

## Build the story

1. Read the supplied manuscript and prior relevant episode assets.
2. Preserve one message per slide and use the requested card count.
3. Assign each slide a visual scene that communicates the claim before the copy is read.
4. Reuse a prior approved image only when its semantic match and quality are strong; otherwise generate a new scene.
5. Keep body copy to about two short sentences and make Korean line breaks intentional.

## Generate or select images

- Read and follow `imagegen` before creating or editing raster images.
- Use premium Korean editorial-webtoon direction: hand-inked charcoal outlines, restrained cel shading, tactile paper grain, documentary framing, warm natural or desk lighting.
- Use deep navy, warm paper, muted blue-gray, and restrained orange.
- Do not generate readable Korean text, logos, watermarks, or generic AI imagery.
- Copy selected images into the project `assets/` folder with `slide-01.*` style names. Preserve the original generated or supplied source.

## Implement

- Output under `D:/SNS/outputs/instagram-carousel/YYYY-MM-DD-project-slug/` unless the user specifies another location.
- Create `index.html` with inline CSS and local images under `assets/`.
- Author slides at fixed `420 x 525px` and export at `1080 x 1350px`.
- Keep essential text at least 37 design pixels from the sides and 34 pixels from the bottom.
- Default typography: Pretendard, Noto Sans KR, Apple SD Gothic Neo, system-ui.
- Default title: 25-29 design pixels, weight 800-900, line-height about 1.28.
- Default body: 9.8-10.5 design pixels, weight about 480, line-height about 1.6.
- Use one rounded orange underline per slide; do not recolor multiple headline fragments.
- Add only a small page counter. No fixed series watermark.

## Export and validate

Create:

- `index.html`
- `assets/slide-01.png` through the final background image
- `exports/slide-01.png` through the final card at `1080 x 1350`
- `contact-sheet.png`
- `README.md`
- `image-prompts.md`
- a ZIP containing only the final exported PNGs

Inspect the contact sheet and representative full-resolution cards. Fix clipping, weak contrast, poor Korean line breaks, mismatched imagery, or excess darkness. Verify the slide count, every PNG dimension, ZIP entry count, local asset paths, and absence of blocked brand terms before delivery.

## Deliver

Show the completed contact sheet first. Link the PNG ZIP, editable HTML, PNG folder, contact sheet, and project folder. Report the verified card count, dimensions, ZIP count, and blocked-term result.
