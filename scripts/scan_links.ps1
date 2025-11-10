#requires -Version 7.0
<#
Scans a selected workspace directory for Markdown links and simple file references.
Writes a markdown report under .tmp-results/reports/links.
Usage:
    pwsh -File scripts/scan_links.ps1
#>
param(
    [string[]]$Scopes = @(
        'novapolis_agent',
        'novapolis-rp',
        'novapolis-dev',
        'novapolis-sim',
        'packages',
        '.github',
        '.'
    ),
    [int]$ScopeIndex = -1,
    [switch]$IncludeCodeRefs,
    [switch]$IncludeExternal
)

$ErrorActionPreference = 'Stop'

$scriptPath = $PSCommandPath
if (-not $scriptPath) { $scriptPath = $MyInvocation.MyCommand.Path }
if (-not $scriptPath) { throw 'Cannot determine script path. Run via pwsh -File.' }
$repoRoot = Split-Path -Parent (Split-Path -Parent $scriptPath)
$tmpRoot = Join-Path $repoRoot '.tmp-results'
$linksDir = Join-Path $tmpRoot 'reports\links'
New-Item -ItemType Directory -Force -Path $linksDir | Out-Null

Write-Host 'Verfügbare Scopes:' -ForegroundColor Cyan
$indexedScopes = @()
for ($i = 0; $i -lt $Scopes.Count; $i++) {
    $candidate = $Scopes[$i]
    $abs = Join-Path $repoRoot $candidate
    if (Test-Path -LiteralPath $abs) {
        $indexedScopes += [pscustomobject]@{ Index = $i; Name = $candidate; Path = $abs }
        Write-Host ("[{0}] {1}" -f $i, $candidate)
    }
}
if (-not $indexedScopes) { throw 'Keine gültigen Scopes gefunden.' }

$selectedIndex = $ScopeIndex
if ($selectedIndex -lt 0) {
    $selection = Read-Host 'Index wählen'
    if (-not ($selection -as [int])) { throw 'Ungültige Auswahl.' }
    $selectedIndex = [int]$selection
}

$scope = $indexedScopes | Where-Object { $_.Index -eq $selectedIndex }
if (-not $scope) { throw 'Auswahl nicht gefunden.' }
$scopePath = $scope.Path

Write-Host ("[link-scan] Starte Scan in {0}" -f $scope.Name) -ForegroundColor Cyan
$files = Get-ChildItem -LiteralPath $scopePath -Recurse -File -ErrorAction SilentlyContinue
$markdownLinks = New-Object System.Collections.Generic.List[object]
$broken = New-Object System.Collections.Generic.List[object]

$absHttp = '^(https?:)?//'
$timestamp = Get-Date -Format 'yyyy-MM-dd HH:mm'
$stampId = Get-Date -Format 'yyyyMMdd_HHmmss'

foreach ($file in $files) {
    $content = Get-Content -LiteralPath $file.FullName -Raw -ErrorAction SilentlyContinue
    if (-not $content) { continue }

    if ($file.Extension -ieq '.md') {
        $matches = [regex]::Matches($content, '\[[^\]]*\]\(([^)]+)\)')
        foreach ($m in $matches) {
            $target = $m.Groups[1].Value.Trim()
            if (-not $IncludeExternal -and $target -match $absHttp) { continue }
            $clean = $target -replace '#.*$','' -replace '\?.*$',''
            if ([string]::IsNullOrWhiteSpace($clean)) { continue }
            $resolved = if ([IO.Path]::IsPathRooted($clean)) { $clean } else { Join-Path $file.DirectoryName $clean }
            $exists = Test-Path -LiteralPath $resolved
            $markdownLinks.Add([pscustomobject]@{
                file     = (Resolve-Path -LiteralPath $file.FullName).Path
                target   = $target
                resolved = $resolved
                exists   = $exists
            }) | Out-Null
            if (-not $exists) {
                $broken.Add([pscustomobject]@{
                    file     = (Resolve-Path -LiteralPath $file.FullName).Path
                    target   = $target
                    resolved = $resolved
                }) | Out-Null
            }
        }
    }

    if ($IncludeCodeRefs) {
        $pattern = '(?<![A-Za-z0-9_\-])([A-Za-z0-9_\-./\\]+\.(md|txt|json|py|ps1|cfg|ini))'
        $references = [regex]::Matches($content, $pattern)
        foreach ($ref in $references) {
            $pathRef = $ref.Groups[1].Value
            if (-not $IncludeExternal -and $pathRef -match $absHttp) { continue }
            $cleanRef = $pathRef -replace '#.*$',''
            $resolvedRef = if ([IO.Path]::IsPathRooted($cleanRef)) { $cleanRef } else { Join-Path $file.DirectoryName $cleanRef }
            if (-not (Test-Path -LiteralPath $resolvedRef)) {
                $broken.Add([pscustomobject]@{
                    file     = (Resolve-Path -LiteralPath $file.FullName).Path
                    target   = $pathRef
                    resolved = $resolvedRef
                }) | Out-Null
            }
        }
    }
}

$reportPath = Join-Path $linksDir ("link_report_{0}_{1}.md" -f $scope.Name.Replace('\\','-').Replace('/','-'), $stampId)
$summary = @()
$summary += '---'
$summary += "stand: $timestamp"
$summary += "update: Link-Scan $($scope.Name)"
$summary += "checks: files=$($files.Count); broken=$($broken.Count)"
$summary += '---'
$summary += ''
$summary += 'Link-Scan Zusammenfassung'
$summary += '========================='
$summary += ''
$summary += "* Scope: $($scope.Name)"
$summary += "* Zeitpunkt: $timestamp"
$summary += "* Dateien gescannt: $($files.Count)"
$summary += "* Defekte Verweise: $($broken.Count)"
$summary += ''
$summary += 'Markdown-Links (erste 50)'
$summary += '-------------------------'
$summary += ''
$markdownLinks | Select-Object -First 50 | ForEach-Object {
    $summary += "- $($_.file) -> $($_.target) (exists=$($_.exists))"
}
$summary += ''
$summary += 'Defekte Verweise'
$summary += '----------------'
$summary += ''
if ($broken.Count -eq 0) {
    $summary += '- keine'
} else {
    $broken | Select-Object -First 100 | ForEach-Object {
        $summary += "- Datei: $($_.file)"
        $summary += "  - Ziel: $($_.target)"
        $summary += "  - Aufgelöst: $($_.resolved)"
    }
}

Set-Content -LiteralPath $reportPath -Value ($summary -join [Environment]::NewLine) -Encoding UTF8
Write-Host ("[link-scan] Report geschrieben: {0}" -f $reportPath) -ForegroundColor Green
