---
name: script-to-social-bundle
description: "Turn a supplied script, narration draft, content brief, outline, or episode manuscript into a complete Korean or English Instagram and LinkedIn content bundle: an image-rich carousel HTML with platform PNGs, a 16:9 animated presentation HTML for presenting or screen recording, 1920x1080 presentation stills, contact sheets, caption, asset notes, and downloadable PNG ZIP. Use when the user says 대본으로 만들어줘, 이 내용으로 캐러셀과 영상 자료를 만들어줘, 발표용 HTML도 같이 만들어줘, 영어 버전도 만들어줘, or asks to create or revise the same coordinated social-content package."
---

# Script to Social Bundle

Create the finished content bundle, not only copy or a storyboard.

## Load the production rules

1. Read `D:/SNS/carousels/brand-config.json` when it exists. Treat it as the user's default.
2. Read and follow the `instagram-carousel` skill before creating carousel artifacts.
3. Treat this skill's explicit square-carousel contract as the geometry override when the downstream skill assumes another carousel ratio.
4. Read and follow `hyperframes` only when the user asks for an actual rendered video or motion-graphic file. Animated presentation HTML alone does not require HyperFrames.
5. Use the image-generation skill when an original raster image materially improves the visual narrative.

## Default bundle

Unless the user overrides it, create one project folder under:

`D:/SNS/carousels/YYYY/MM/carousel-XX-topic/`

Produce:

- `carousel-XX-topic.html`: self-contained carousel preview and exporter
- `exports/slide-01.png` through the final slide: `1080 x 1080px`
- `contact-sheet.png`: carousel review sheet
- `presentation-16x9.html`: animated large-screen companion
- `presentation-exports/presentation-01.png` through the final slide: `1920 x 1080px`
- `presentation-contact-sheet.png`: presentation review sheet
- `caption.md`: publish-ready LinkedIn and Instagram caption
- `image-prompts.md`: generated-image and local-asset notes
- `sources.md` when attribution or external factual support appears
- a ZIP containing only the final carousel PNGs

Default to eight slides. Use 6-10 only when the script clearly needs a different count. Keep the carousel and presentation in the same project folder.

## Convert the script into visual beats

Preserve the script's point of view and factual meaning. Do not inflate it into a success story or invent evidence.

1. Extract the central tension, turning point, useful details, and closing invitation.
2. Map the argument into visual beats. A typical eight-slide rhythm is:
   - hook
   - misconception or context
   - initiating question
   - concrete evidence or tools
   - decision or contrast
   - timeline or process
   - present-tense log
   - reflective CTA
3. Keep one message per slide.
4. Write short headlines and no more than 2-3 short body lines unless the slide is a deliberate list or timeline.
5. Use a neutral save, comment, or reflection CTA. Avoid sales copy unless requested.
6. Keep any spoken script available as the semantic source; shorten for slides rather than changing its meaning.
7. Assign every card a visual job. If the image could be swapped with a generic person-at-laptop scene without changing the meaning, make it more specific.

## Design the square carousel

Use a high-quality editorial system with at least four layout families across eight slides.

- Default visual direction: corporate documentary, strong information hierarchy, dark editorial hero moments, restrained color, Korean sans-serif typography.
- Default palette: follow the user's brief; otherwise use deep navy, graphite, warm white, muted gray, and one signal accent.
- Default identity: brandless. Do not add a fixed brand name, handle, logo, watermark, or branded footer.
- Never include `comindworks`, `CoMindWorks`, or `@comindworks`.
- Use meaningful imagery, UI scenes, diagrams, timelines, comparison panels, or documentary textures. Avoid repeated text-only cards.
- Avoid cute startup-ad styling, generic robot icons, excessive gradients, invented statistics, and decorative visuals that do not support the message.
- Keep all Korean text as HTML text. Generate raster art without embedded wording.

Build touch swipe, mouse drag, keyboard navigation, and per-slide PNG export into the HTML.

## Build an English sibling

When the user requests English, create a separate `-en` sibling project and produce the complete bundle again. Reuse approved imagery, but translate all visible text, terminal prompts, diagram labels, and CTA copy. Rewrite line breaks for natural English, inspect long headlines individually, and validate both image dimensions and ZIP contents.

## Build the animated 16:9 companion

Recompose each slide for `1600 x 900` design space and `1920 x 1080` export. Do not center a square carousel image on a widescreen canvas.

Use different motion logic according to the slide:

- masked headline reveal and slow image push-in
- left-side premise followed by right-side explanation
- Korean character or word build for a question
- module or chip assembly
- comparison emphasis and directional paths
- timeline line growth and milestone reveals
- sequential checklist completion
- closing question and CTA reveal

Apply these defaults:

- autoplay interval: `5.5` seconds
- motion speed multiplier: `1.28`
- supported query parameters: `slide`, `autoplay`, and `seconds`
- keyboard navigation and click/touch controls
- restart motion cleanly whenever a slide becomes active
- respect `prefers-reduced-motion`

Keep motion readable and varied. Do not reuse the same entrance on every slide. Reserve at least 80 design pixels on the left and right for the safe area, and verify that wide timelines, chips, and captions never clip at the right edge.

## Write the caption

Write one concise publish-ready caption that:

- opens with the script's main tension
- states the practical or personal takeaway
- invites one specific response
- uses only relevant hashtags
- avoids brand signatures when `show_brand` is false

## Validate before delivery

Do not stop at generated source files.

1. Export every carousel and presentation image.
2. Build both contact sheets and inspect all slides visually.
3. Check representative early, middle, and late animation frames.
4. Verify Korean line breaks, hierarchy, contrast, safe margins, and right-edge clipping.
5. Search filenames, HTML, captions, mockups, and visible text case-insensitively for every `blocked_brand_terms` entry.
6. Confirm the final artifact counts and dimensions.
7. Open or smoke-test the local presentation URL when browser control is available.
8. Confirm the downloadable ZIP contains exactly the final carousel PNG count.

## Deliver

Lead with the completed result. Link the downloadable PNG ZIP, project folder, carousel HTML, animated presentation HTML, contact sheets, and caption. Include a recording URL example such as:

`presentation-16x9.html?slide=1&autoplay=1&seconds=5.5`

Mention only material deviations from the defaults.
