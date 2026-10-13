$ErrorActionPreference = "Continue"
$OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$ep = Split-Path -Parent $PSScriptRoot
Set-Location $ep
$round = if ($args.Count -gt 0) { $args[0] } else { "1" }
$log = Join-Path $ep "실행검증\codex_review_$round.log"
Write-Host "==================== Codex 검수 $round 차 ====================" -ForegroundColor Yellow
if ($round -eq "1") {
  $prompt = Get-Content (Join-Path $PSScriptRoot "review_prompt.txt") -Raw -Encoding UTF8
  $cards = (Get-ChildItem (Join-Path $ep "카드") -Filter "card_*.png" | ForEach-Object { $_.FullName })
  $prompt | codex exec --skip-git-repo-check -s read-only -i $cards - 2>&1 | Tee-Object -FilePath $log
} else {
  $prompt = Get-Content (Join-Path $PSScriptRoot "review_reply.txt") -Raw -Encoding UTF8
  $prompt | codex exec --skip-git-repo-check -s read-only resume --last - 2>&1 | Tee-Object -FilePath $log
}
Write-Host "==================== 검수 $round 차 종료 ====================" -ForegroundColor Green
