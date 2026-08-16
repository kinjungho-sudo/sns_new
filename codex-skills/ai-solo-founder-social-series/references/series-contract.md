# Solo Founder with AI — Series Contract

## 1. Project and naming contract

- Root: `D:/SNS/carousels/YYYY/MM/`
- Determine the next `carousel-XX` number from existing folders.
- Korean project: `carousel-XX-ai-solo-founder-EP-topic-cartoon/`
- English sibling: append `-en`.
- Never overwrite a prior episode or language edition unless explicitly requested.
- Keep all assets, source HTML, exports, captions, notes, and ZIPs in the episode project.

## 2. Required artifacts

For `N` cards, create:

- `carousel-XX-...html`
- `exports/slide-01.png` through `slide-NN.png` at `1080 x 1080`
- `contact-sheet.png`
- `presentation-16x9.html`
- `presentation-exports/presentation-01.png` through `presentation-NN.png` at `1920 x 1080`
- `presentation-contact-sheet.png`
- `motion-previews/` with at least three mid-animation frames and a review sheet when practical
- `caption.md`
- `image-prompts.md`
- `sources.md` when factual attribution, product assets, a book cover, or a public figure appears
- `AI-solo-founder-episode-EP-LANG-PNG-YYYYMMDD.zip` containing only the final square PNGs

Default to 8-9 cards. Follow the user's requested count when supplied.

## 3. Series voice

- Use first-person reflection with calm confidence.
- Show an unfinished process, uncertainty, experiments, corrections, and decisions.
- Avoid victory-lap language, hustle slogans, AI worship, fear marketing, unsupported numbers, and absolute predictions.
- Do not make resignation sound like escape when the episode frames it as self-directed choice.
- Preserve cautious paraphrases. Never convert a paraphrase into a direct quotation.
- End with one answerable, low-pressure question.

## 4. Visual story standard

### Semantic match

Every card must pass this test: if the copy were hidden, would the image still suggest the card's claim?

Use:

- a concrete situation for personal experience;
- a visible before/after or causal transition for transformation;
- a diagram or timeline for process and comparison;
- a real supplied object image when the object itself is evidence;
- a believable terminal, browser, document, presentation, or workflow screen when the story names that output.

Reject:

- a generic person at a laptop when the claim is about cost, time, leverage, review, speed, or questions;
- repeated portraits used only as decoration;
- robot mascots, neon cyberpunk backgrounds, holographic AI brains, and SaaS landing-page gloss;
- generated text baked into illustrations;
- imagery that only repeats the headline without showing the situation.

### Protagonist continuity

- Reuse the approved Korean male founder identity from the latest relevant episode when available.
- Keep face structure, black side-parted hair, age impression, and build consistent.
- Vary pose, camera distance, clothing details, and setting according to the scene.
- Prefer 2-4 recognizable protagonist appearances in an 8-9 card episode; use object- and system-led cards elsewhere.
- Do not copy private reference photos into the reusable skill.

### Layout rhythm

- Make every cover structurally different from the previous episode.
- Use at least four layout families per deck.
- Include 2-3 light cards unless the brief requires another rhythm.
- Use one message per card and short mobile-readable copy.
- Maintain a 28-32 design-pixel safe margin on the square canvas.
- Add small card numbers only. Never add a fixed brand name, handle, logo, watermark, or mouse cursor.

## 5. English edition contract

- Create a full sibling bundle, not a text-only translation.
- Reuse the approved Korean edition's images and story order unless the user requests new visuals.
- Translate meaning and emotional cadence rather than Korean word order.
- Shorten headlines where needed and re-break lines deliberately for mobile reading.
- Translate terminal commands, diagram labels, buttons, captions, and CTA text.
- Use `Inter, Pretendard, Arial, sans-serif`.
- Reduce negative letter spacing compared with Korean and inspect Cards 1, 4, 6, 8, and the CTA card individually.
- Keep product names unchanged.
- Keep public-figure language cautious and non-quotational.

## 6. Claude Code and real-output scenes

When a card says that Claude Code or another coding agent produced a web result:

- show a terminal command or short prompt;
- show a believable real V1 web page, not abstract glowing panels;
- make the causal direction clear from command to browser;
- use HTML overlays for terminal text and labels;
- include visible web structure such as navigation, data cards, table rows, chart, form, or action button;
- label the result modestly, for example `REAL WEB · V1`;
- keep review and human judgment visible elsewhere in the story so the scene does not imply perfect autonomous completion.

## 7. Animated presentation contract

- Recompose each card for a `1600 x 900` design stage and export at `1920 x 1080`.
- Do not place a cropped square card on a widescreen background.
- Support `slide`, `autoplay`, `seconds`, and `export` query parameters.
- Default autoplay interval: `5.5` seconds.
- Default motion multiplier: `1.28`.
- Use staggered, content-specific motion: premise then evidence, command then web result, comparison sequencing, path growth, checklist completion, or CTA reveal.
- Keep the resolved frame static in export mode.
- Leave at least 80 design pixels of left and right safe area.

## 8. Validation contract

- Verify every square PNG is exactly `1080 x 1080`.
- Verify every presentation PNG is exactly `1920 x 1080`.
- Inspect both contact sheets and long-copy individual cards.
- Check at least three animation mid-frames.
- Confirm local asset references resolve.
- Confirm the ZIP entry count equals the card count.
- Run:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:/Users/김정호/.codex/skills/editorial-webtoon-social-bundle/scripts/build_contact_sheets.ps1" -ProjectRoot "<project>"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:/Users/김정호/.codex/skills/editorial-webtoon-social-bundle/scripts/validate_bundle.ps1" -ProjectRoot "<project>" -SlideCount <N>
```

Fix all failures and visible defects before delivery.
