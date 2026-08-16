$ErrorActionPreference = 'Stop'
$projectDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$htmlPath = Join-Path $projectDir 'episode06_own_work_overtime_carousel_v2.html'
$exportDir = Join-Path $projectDir 'exports'
$chrome = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
New-Item -ItemType Directory -Force -Path $exportDir | Out-Null
if (-not (Test-Path -LiteralPath $chrome)) { throw "Chrome not found: $chrome" }
for ($i = 1; $i -le 8; $i++) {
  $n = $i.ToString('00')
  $out = Join-Path $exportDir "episode06-v2-card-$n.png"
  $temp = Join-Path $exportDir "_temp-card-$n.png"
  $uri = ([System.Uri]$htmlPath).AbsoluteUri + "?slide=$i&export=1"
  & $chrome --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2.5714285714 --window-size=456,525 --virtual-time-budget=3000 --screenshot=$temp $uri | Out-Null
  & ffmpeg -loglevel error -y -i $temp -vf 'crop=1080:1350:93:0' -frames:v 1 -update 1 $out
  Remove-Item -LiteralPath $temp -Force
  if (-not (Test-Path -LiteralPath $out)) { throw "Export failed: $out" }
}
