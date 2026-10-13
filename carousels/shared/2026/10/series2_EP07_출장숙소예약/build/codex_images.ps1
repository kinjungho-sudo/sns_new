# EP07 Codex 실사 이미지 생성 (실시간 확인용 — 터미널 탭에서 실행)
$ErrorActionPreference = "Continue"
Set-Location "D:\Project\sns_new\carousels\shared\2026\10\series2_EP07_출장숙소예약\raw"
$style = "Editorial realism photograph, warm natural window light, soft shadows, muted palette that harmonizes with cream (#ECE6D8) and rust (#C0592F), shallow depth of field, no glossy stock look. Absolutely no readable text, letters, numbers, logos, brand names or barcodes anywhere (screens show only abstract blurred shapes)."
$jobs = @(
  @{ id = "EP07-S01-cover"; file = "cover.png"; prompt = "Slide 1 cover asset. Top-down view of an office desk prepared for a business trip: an open laptop (screen shows abstract blurred blocks only), a small carry-on suitcase edge, a printed itinerary sheet with blank lines, a pen, a coffee cup, a train ticket shape without text. Leave the upper 40% calm and empty for headline copy. Portrait 4:5 (1024x1280 or larger)." },
  @{ id = "EP07-S02-before"; file = "before.png"; prompt = "Slide 2 BEFORE asset. A Korean office worker (generic person, face partly turned away) at a desk late afternoon, frowning at a laptop crowded with many overlapping browser windows (abstract blurred tiles, no readable text), a sticky note pad and a calendar page with blank boxes, a suitcase by the chair. Feeling of tedious comparison. Leave the top 30% calmer for copy. Portrait 4:5." }
)
foreach ($j in $jobs) {
  Write-Host ""
  Write-Host "==================== Codex 이미지 생성: $($j.id) ====================" -ForegroundColor Yellow
  $p = "Generate an image with your built-in image generation tool. asset_id: $($j.id). $($j.prompt) $style Save the PNG into the current directory as $($j.file) (overwrite if exists) and print the path and pixel size."
  codex exec --skip-git-repo-check --sandbox workspace-write -- $p
}
Write-Host ""
Write-Host "==================== 완료 ====================" -ForegroundColor Green
Get-ChildItem | Select-Object Name, Length
