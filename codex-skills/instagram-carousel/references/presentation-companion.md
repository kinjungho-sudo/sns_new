# Presentation Companion

Create a presentation companion whenever `create_presentation_html` is true or the user asks for presentation, PPT, large-screen, recording, or YouTube reuse.

## Output

- Save `presentation-16x9.html` beside the carousel HTML.
- Author each presentation slide at a fixed `1600 x 900px`.
- Provide `export_presentation.ps1` and export clean `1920 x 1080px` PNGs when practical.
- Reuse the carousel's copy, visual language, and local assets, but recompose for 16:9. Do not stretch or center-crop the square/portrait card as the main layout.

## Interaction

Support:

- Left/right arrow navigation
- Touch and mouse swipe
- `F` for fullscreen
- `Space` for autoplay pause/resume
- `?slide=N` deep linking
- `?autoplay=1&seconds=5.5` recording mode
- `?export=1&slide=N` clean export mode without controls

Use the configured `presentation_autoplay_seconds`; default to 5.5 seconds. Eight slides at this pace produce an approximately 44-second screen-recording sequence.

## Motion

When `presentation_motion` is true, create distinct scene choreography instead of repeating one entrance effect.

- Use 2-4 purposeful motions per slide.
- Vary patterns according to content: line/word reveal, Korean character typing, left-then-right comparison, modular assembly, image push-in, timeline draw, sequential checklist completion, and CTA card reveal.
- Keep each slide's main choreography within roughly 3.2-3.6 seconds so the message can rest before the next slide.
- Apply `presentation_motion_speed` as a multiplier to animation delays and durations; default to `1.28` for a measured presentation pace.
- Replay the active slide with `R`.
- Respect `prefers-reduced-motion`.
- Hide controls immediately when `?autoplay=1` is active.
- Disable motion in `?export=1` mode and show the fully resolved frame.
- Cancel prior animations before replaying or navigating so re-entry is stable.

## Design

- Increase type and information density for viewing from a distance.
- Preserve at least four layout families from the carousel.
- Keep all essential copy within the 16:9 title-safe area.
- Use generated or supplied images as full-bleed or split-layout documentary visuals, not decorative thumbnails.
- Keep branding and blocked-term behavior identical to the carousel.

## Validation

- Inspect a contact sheet of all presentation slides.
- Verify every exported presentation PNG is exactly `1920 x 1080px`.
- Confirm controls are hidden in export mode.
- Confirm autoplay, fullscreen, keyboard navigation, and slide deep links work.
- Capture representative mid-animation frames to confirm sequencing and legibility.
- Keep timeline endpoints and final-column labels inside a generous right-side safe area; do not center the final node on the canvas edge.
