param(
    [Parameter(Mandatory = $true)]
    [string]$CardsDirectory,
    [Parameter(Mandatory = $true)]
    [string]$InstagramCaption,
    [Parameter(Mandatory = $true)]
    [string]$LinkedInCaption,
    [Parameter(Mandatory = $true)]
    [string]$NaverCaption,
    [Parameter(Mandatory = $true)]
    [string]$TistoryCaption
)

$ErrorActionPreference = 'Stop'
$publicResourceUrl = 'https://uncovered-crate-996.notion.site/AI-3eb147a5e90f80bcbc73c5a9107e5060'
$resourceKeyword = ([string][char]0xC790) + ([string][char]0xB8CC)
$commentWord = ([string][char]0xB313) + ([string][char]0xAE00)
$failures = [System.Collections.Generic.List[string]]::new()

function Read-RequiredTextFile {
    param([string]$Path, [string]$Label)
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        $failures.Add("$Label file is missing: $Path")
        return ''
    }
    return Get-Content -LiteralPath $Path -Encoding utf8 -Raw
}

$resolvedCardsDirectory = Resolve-Path -LiteralPath $CardsDirectory -ErrorAction SilentlyContinue
if (-not $resolvedCardsDirectory) {
    $failures.Add("Cards directory is missing: $CardsDirectory")
    $cards = @()
} else {
    $cards = @(Get-ChildItem -LiteralPath $resolvedCardsDirectory.Path -Filter '*.png' -File | Sort-Object Name)
}

if ($cards.Count -ne 7) {
    $failures.Add("Expected 7 PNG cards, found $($cards.Count).")
}

Add-Type -AssemblyName System.Drawing
foreach ($card in $cards) {
    $image = $null
    try {
        $image = [System.Drawing.Image]::FromFile($card.FullName)
        if ($image.Width -ne 1080 -or $image.Height -ne 1350) {
            $failures.Add("$($card.Name) is $($image.Width)x$($image.Height), expected 1080x1350.")
        }
    } catch {
        $failures.Add("Could not open PNG: $($card.FullName)")
    } finally {
        if ($image) { $image.Dispose() }
    }
}

$instagramText = Read-RequiredTextFile -Path $InstagramCaption -Label 'Instagram caption'
if ($instagramText -notmatch [regex]::Escape($resourceKeyword)) {
    $failures.Add('Instagram caption must include the configured resource keyword.')
}

$directLinkCaptions = @(
    @{ Label = 'LinkedIn caption'; Path = $LinkedInCaption },
    @{ Label = 'Naver caption'; Path = $NaverCaption },
    @{ Label = 'Tistory caption'; Path = $TistoryCaption }
)

foreach ($caption in $directLinkCaptions) {
    $captionText = Read-RequiredTextFile -Path $caption.Path -Label $caption.Label
    if ($captionText -notlike "*$publicResourceUrl*") {
        $failures.Add("$($caption.Label) must include the public Notion resource URL.")
    }
    $unsupportedPromisePattern = [regex]::Escape($commentWord) + '.{0,20}DM'
    if ($captionText -match $unsupportedPromisePattern) {
        $failures.Add("$($caption.Label) promises comment-triggered private delivery, which is unsupported.")
    }
}

$result = [ordered]@{
    ok = ($failures.Count -eq 0)
    cards = $cards.Count
    required_channels = @('Instagram', 'LinkedIn', 'Naver Blog', 'Tistory')
    public_resource_url = $publicResourceUrl
    failures = @($failures)
}

$result | ConvertTo-Json -Depth 4
if ($failures.Count -gt 0) { exit 1 }
