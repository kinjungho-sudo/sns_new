# Editorial Tech Visual

Use this reference for brandless, dark, image-rich Korean carousels and whenever the user asks for the quality or visual language of the bundled samples.

## Visual direction

- Build at `420 x 525px`; export at `1080 x 1350px`.
- Use a near-black canvas (`#080B0D`) with a subtle 32-40px grid (`rgba(255,255,255,.035)`).
- Use a Korean-first sans stack: `Pretendard`, `Noto Sans KR`, `Apple SD Gothic Neo`, `Malgun Gothic`, sans-serif.
- Use `JetBrains Mono` or another mono font only for counters, code, dates, and keyboard keys.
- Set text in white and cool gray. Use green (`#2FC35B`) as the main accent and amber (`#FFBD2E`) only for warnings, anomalies, or a second emphasis.
- Use 24-32px outer padding in the 420px design. Place the slide counter at top right as `01 / 06`.
- Favor top-left headlines, asymmetric composition, generous negative space, rounded panels, thin borders, and soft inner highlights.
- Do not render a profile photo, name, handle, logo, wordmark, watermark, branded footer, or follow CTA unless the user explicitly asks for branding.

## Meaningful visuals

Every non-cover slide must include one visual that explains or proves the point. A decorative gradient or generic icon does not count.

Choose the visual from the content:

| Content | Preferred visual |
|---|---|
| Data, anomaly, result | Table crop, line/bar chart, highlighted cell, KPI panel |
| Process, tutorial | Numbered flow, keyboard keys, annotated UI, before/after states |
| AI interaction | Chat window, prompt/result panel, cursor or upload state |
| Comparison, judgment | Split panel, risk matrix, balance scale, decision gate |
| Abstract idea | Purpose-built editorial illustration or image-generation asset |
| Real person/place/product | User-provided or sourced raster image with a dark overlay |

- Allocate roughly 35-60% of each content slide to the visual system.
- Use at least four distinct layout families across a 6-8 slide carousel.
- Prefer one strong visual over many small decorations.
- For AI-generated raster art, generate without text and add all Korean typography in HTML.
- When the topic is procedural or data-led, prefer accurate CSS/SVG visuals over decorative stock photography.
- When the topic benefits from atmosphere or human context, include at least two raster images across the carousel.

## Recommended slide rhythm

1. Hook: provocative question or contrast plus one hero visual.
2. Principle: concise thesis plus a decision model or UI metaphor.
3. Example: concrete scenario in a screenshot, mockup, table, or illustration.
4. Contrast: two states, risk levels, or before/after.
5. Action: three-step instruction with large numbered rows or keycaps.
6. Summary: memorable rule plus compact checklist or icon.

Use 6-8 slides when the content supports it. Do not force a generic white CTA slide. The final slide should complete the argument and may include a neutral `저장해 두세요` prompt without an identity block.

## Bundled visual samples

Inspect `assets/editorial-tech-samples/sample-01.png` through `sample-06.png` with the image-viewing tool before producing this style. Treat them as composition references only; do not copy their text or proprietary content.

The samples demonstrate:

- `sample-01`: spreadsheet/table as the hero proof.
- `sample-02`: file-upload UI as an explanatory illustration.
- `sample-03`: human-vs-AI comparison with a highlighted chart anomaly.
- `sample-04`: assistant response panel with hierarchy and annotation.
- `sample-05`: three-step procedure using keycap components.
- `sample-06`: summary statement with warning card and restrained iconography.

## Quality gates

- Confirm no unwanted brand or account text appears anywhere, including filenames shown inside mockups.
- Confirm every slide has a distinct job and no repeated centered-text-only layout.
- Confirm every content slide contains a meaningful visual and the visual is legible at phone size.
- Confirm Korean line breaks are intentional and headlines do not exceed three lines.
- Confirm body copy remains readable in 3-5 seconds.
- Confirm charts, tables, and UI examples support the actual claim and do not fabricate factual evidence.
- Confirm all external images are embedded or copied locally before export.
- Render and inspect every exported PNG at `1080 x 1350px` before delivery.
