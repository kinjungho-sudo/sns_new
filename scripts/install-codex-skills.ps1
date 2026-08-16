$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $PSScriptRoot
$codexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
$target = Join-Path $codexHome 'skills'

New-Item -ItemType Directory -Force $target | Out-Null

Get-ChildItem -Directory (Join-Path $repoRoot 'codex-skills') | ForEach-Object {
    $dest = Join-Path $target $_.Name
    if (Test-Path $dest) {
        Remove-Item -Recurse -Force $dest
    }
    Copy-Item -Recurse -Force $_.FullName $dest
    Write-Host "installed $($_.Name) -> $dest"
}
