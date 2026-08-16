---
name: instagram-carousel
description: "Design and export high-quality Instagram and LinkedIn carousel posts as self-contained HTML and platform-ready PNGs, with an optional or preference-driven 16:9 large-screen presentation HTML companion for PPT-style presenting, screen recording, and short YouTube reuse. Turns supplied scripts or narration drafts into coordinated carousel, animated presentation, image export, and caption bundles. Supports brandless, image-rich editorial layouts, tables, charts, UI mockups, screenshots, diagrams, and generated illustrations. Use for social carousels, carousel cards, slide decks, presentation HTML, visual explainers, script-to-carousel production, or carousel image export."
---

# Instagram Carousel Designer

Create self-contained Instagram carousel HTML with fixed `420 x 525px` slides and export pixel-perfect `1080 x 1350px` PNGs. Handle both copy and design.

Default to a brandless, image-rich editorial system. Add names, handles, profile photos, logos, wordmarks, watermarks, or brand CTAs only when the user explicitly asks for branding or the preferences config sets `show_brand: true`.

## References

Read only the references needed for the selected style:

| File | Read when |
|---|---|
| `references/editorial-tech.md` | Always for brandless, Korean, image-rich, dark editorial, AI/data/tutorial, or sample-quality requests |
| `references/design-system.md` | Always for dimensions and shared architecture |
| `references/export-guide.md` | Always before rendering or exporting |
| `references/presentation-companion.md` | When `create_presentation_html` is true or the user asks for PPT, presentation, large-screen, recording, or YouTube reuse |
| `references/styles.md` | Only for a legacy style |
| `references/components.md` | Only for a legacy style; identity components require `show_brand: true` |

For Editorial Tech Visual, inspect `assets/editorial-tech-samples/sample-01.png` through `sample-06.png` with the image-viewing tool before designing. Treat them as composition references only; do not copy their text or proprietary content.

## Dimensions

Use fixed dimensions. Do not make slide geometry responsive.

```text
Design: 420 x 525px
Export: 1080 x 1350px
Scale: 2.5714x
Ratio: 4:5
```

## Styles

| Style | Best for | Character |
|---|---|---|
| **Editorial Tech Visual** | AI, data, frameworks, tutorials, decision guides, Korean educational content | Brandless dark grid, strong Korean type, evidence-led visuals |
| **Bold Impact** | Numbered insights, shifts, mistakes, tips | Dark, massive type, accent color, film grain |
| **Tweet Post** | Hot takes, opinions, quotes | Minimal and conversational |
| **Clean Editorial** | Light educational layouts | White grid, structured hierarchy |
| **Product Showcase** | Tools, products, comparisons | Soft gradient, app cards, pagination dots |

Select a style in this order:

1. Follow an explicit style request.
2. Use Editorial Tech Visual for Korean educational content, AI, data, tutorials, frameworks, decision guides, or any request for images, higher quality, or the bundled sample direction.
3. Otherwise use `default_style` from the preferences config.
4. If no default exists, use Editorial Tech Visual. Ask at most one question only when the answer materially changes the result.

## Workflow

Follow these phases in order.

### 0. Load preferences

Read `carousels/brand-config.json` from the working directory when it exists. Honor `show_brand`, `visual_mode`, `default_style`, and `blocked_brand_terms` before legacy identity fields.

If the file does not exist, create this brandless default. Ask for identity details only if the user explicitly requests branded output.

```json
{
  "name": "",
  "handle": "",
  "subtitle": "",
  "profile_photo": "",
  "accent_color": "#2FC35B",
  "secondary_accent": "#FFBD2E",
  "initials": "",
  "default_style": "editorial-tech",
  "show_brand": false,
  "visual_mode": "image-rich",
  "create_presentation_html": false,
  "presentation_ratio": "16:9",
  "presentation_design_size": "1600x900",
  "presentation_export_size": "1920x1080",
  "presentation_autoplay_seconds": 5.5,
  "presentation_motion": false,
  "presentation_motion_style": "varied-editorial",
  "presentation_motion_speed": 1.28,
  "script_input_bundle": false,
  "script_input_outputs": [
    "carousel-html",
    "carousel-png",
    "caption"
  ],
  "script_input_default_slides": 8,
  "blocked_brand_terms": [],
  "setup_complete": true
}
```

When `show_brand` is false, leave identity fields empty and do not invent an author identity. When it is true, collect only the missing fields required by the requested design.

Create `carousels/[year]/[month]/` when needed.

### 1. Research and visual plan

1. Scan past carousel titles and filenames to avoid repeating topics and layouts.
2. Determine the style.
3. Inventory user-provided images, screenshots, tables, data, and reference designs.
4. Plan one meaningful visual for every content slide before building HTML.
5. Assign a distinct job to each slide: hook, principle, example, contrast, action, or summary.

### 2. Write copy

Write direct, concrete, concise copy. Prefer claims the user can verify. Avoid filler, vague corporate language, and unsupported specifics.

- When the user supplies a script or narration draft and `script_input_bundle` is true, preserve the argument while mapping it into `script_input_default_slides` visual beats. Keep one message per slide and generate every artifact listed in `script_input_outputs`.
- When `script_input_outputs` includes `animated-presentation-html`, enable the presentation companion and use varied, seek-safe motion suited to each slide rather than repeating one entrance effect.
- Use 5-10 slides; prefer 6-8.
- Keep each slide readable in 3-5 seconds.
- Use a strong question, tension, contrast, or promise on slide 1.
- Keep Korean headline line breaks intentional and generally within three lines.
- Do not force a generic white CTA slide. End by completing the argument; a neutral save/share prompt is acceptable.

### 3. Build HTML

Read the required references and generate one self-contained HTML file.

Critical rules:

1. Set every slide to exactly `width: 420px; height: 525px`.
2. Use `accent_color` as the main accent and `secondary_accent` sparingly for warnings or anomalies.
3. If `show_brand` is false, omit all name, handle, profile, logo, wordmark, watermark, branded footer, and follow CTA elements. Do not leak legacy identity text from templates.
4. If `show_brand` is true, use only identity elements explicitly supplied by the user.
5. Embed or locally bundle every image so export is deterministic.
6. Use user assets first. Use accurate CSS/SVG for data, process, and interface visuals.
7. If a raster illustration materially improves the idea, load and follow the available image-generation skill. Generate art without text, then overlay all Korean type in HTML.
8. Include a preview frame plus touch swipe, mouse drag, and keyboard arrow navigation.
9. Include PNG-per-slide export and optional PDF export.
10. Save as `carousels/[year]/[month]/carousel-XX-topic.html`.
11. Replace legacy sample colors `#6EE421`, `#85F040`, and `#5BC01C` in both cases with the configured main accent.
12. Search generated HTML, captions, filenames, and visible mockup text case-insensitively for every value in `blocked_brand_terms`. Delivery fails until every match is removed.
13. When `create_presentation_html` is true, read `references/presentation-companion.md` and create the 16:9 large-screen companion after the carousel HTML. Recompose the content for presentation; do not merely place the carousel image in the center.

### 4. Preview and inspect

Render the full carousel. Inspect each slide as an image, not only as HTML. Fix overflow, awkward Korean line breaks, weak hierarchy, repetitive layouts, and decorative visuals that do not support the point.

### 5. Export

Follow `references/export-guide.md` and export one platform-sized PNG per slide. Use the browser fallback only when Playwright is unavailable. Export PDF only when requested or already included by the template. When presentation output is enabled, also validate the 16:9 HTML and export `1920 x 1080px` presentation PNGs when practical.

### 6. Deliver

Save the carousel HTML, PNGs, and suggested caption. When enabled, also save and link the presentation HTML, presentation PNGs, and recording-mode query example. For a script-input bundle, confirm that every configured output was created and keep the carousel and presentation in the same project folder.

## Quality checklist

Verify all items before delivery:

- [ ] Preferences were read and `show_brand` was honored.
- [ ] No `blocked_brand_terms` value appears in HTML, captions, mockups, filenames, or exports.
- [ ] Every slide is exactly `420 x 525px`; every PNG is `1080 x 1350px`.
- [ ] Korean typography uses an appropriate Korean font stack.
- [ ] Every slide is readable in 3-5 seconds.
- [ ] The hook is visually and verbally strong.
- [ ] Every content slide contains a meaningful visual, not merely decorative effects.
- [ ] At least four layout families appear across a 6-8 slide carousel.
- [ ] Editorial Tech output uses a top-right slide counter and avoids repeated centered-text-only layouts.
- [ ] Brandless output contains no profile header, handle, logo, wordmark, watermark, branded footer, or follow CTA.
- [ ] Charts, tables, and UI mockups support the actual claim and do not present invented data as evidence.
- [ ] All images are embedded or locally bundled.
- [ ] Touch, mouse, and keyboard navigation works.
- [ ] PNG export was rendered and visually inspected slide by slide.
- [ ] Caption and hashtags were suggested.
- [ ] When `create_presentation_html` is true, a recomposed `1600 x 900px` presentation HTML exists and its `1920 x 1080px` export was visually inspected.
