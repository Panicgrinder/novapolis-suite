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
    ,
    [switch]$AutoFix
)

$ErrorActionPreference = 'Stop'

$scriptPath = $PSCommandPath
if (-not $scriptPath) { $scriptPath = $MyInvocation.MyCommand.Path }
if (-not $scriptPath) { throw 'Cannot determine script path. Run via pwsh -File.' }
$repoRoot = Split-Path -Parent (Split-Path -Parent $scriptPath)
$tmpRoot = Join-Path $repoRoot '.tmp-results'
$linksDir = Join-Path $tmpRoot 'reports\scan_links_reports'
New-Item -ItemType Directory -Force -Path $linksDir | Out-Null

# Central backup directory for link-scan AutoFix backups
$backupRoot = Join-Path $repoRoot '.tmp-datasets\lscan_links_backups'
New-Item -ItemType Directory -Force -Path $backupRoot | Out-Null

Write-Information 'Verfügbare Scopes:' -Tags 'LinkScan'
$indexedScopes = @()
for ($i = 0; $i -lt $Scopes.Count; $i++) {
    $candidate = $Scopes[$i]
    $abs = Join-Path $repoRoot $candidate
    if (Test-Path -LiteralPath $abs) {
        $indexedScopes += [pscustomobject]@{ Index = $i; Name = $candidate; Path = $abs }
        Write-Information ("[{0}] {1}" -f $i, $candidate) -Tags 'LinkScan'
    }
}
if (-not $indexedScopes) { throw 'Keine gültigen Scopes gefunden.' }

$selectedIndex = $ScopeIndex
if ($selectedIndex -lt 0) {
    # Non-interactive mode: default to the first available indexed scope
    $firstScope = $indexedScopes | Select-Object -First 1
    if ($null -eq $firstScope) { throw 'Keine gültigen Scopes gefunden.' }
    $selectedIndex = $firstScope.Index
}

$scope = $indexedScopes | Where-Object { $_.Index -eq $selectedIndex }
if (-not $scope) { throw 'Auswahl nicht gefunden.' }
$scopePath = $scope.Path

Write-Information ("[link-scan] Starte Scan in {0}" -f $scope.Name) -Tags 'LinkScan'
$files = Get-ChildItem -LiteralPath $scopePath -Recurse -File -ErrorAction SilentlyContinue
$files = @($files)
$markdownLinks = New-Object System.Collections.Generic.List[object]
$broken = New-Object System.Collections.Generic.List[object]

$fixes = New-Object System.Collections.Generic.List[object]

$absHttp = '^(https?:)?//'
$timestamp = Get-Date -Format 'yyyy-MM-dd HH:mm'
$stampId = Get-Date -Format 'yyyyMMdd_HHmmss'

foreach ($file in $files) {
    $content = Get-Content -LiteralPath $file.FullName -Raw -ErrorAction SilentlyContinue
    if (-not $content) { continue }

    if ($file.Extension -ieq '.md') {
        $mdMatches = [regex]::Matches($content, '\[[^\]]*\]\(([^)]+)\)')
        foreach ($m in $mdMatches) {
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
        $codeRefMatches = [regex]::Matches($content, $pattern)
        foreach ($ref in $codeRefMatches) {
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

# Auto-fix logic: only run if requested and there are broken links
if ($AutoFix -and $broken.Count -gt 0) {
    Write-Information '[link-scan] AutoFix enabled — prüfe Duplikate und bereite Änderungen vor.' -Tags 'LinkScan'
    # Group broken by target to avoid repeated work
    $grouped = $broken | Group-Object -Property resolved -NoElement
    foreach ($g in $grouped) {
        $resolved = $g.Name
        # determine the base file name to search for duplicates
        $fileName = [IO.Path]::GetFileName($resolved)
        if ([string]::IsNullOrWhiteSpace($fileName)) { continue }

        # search the repo for files with that name
        $matches = Get-ChildItem -LiteralPath $repoRoot -Recurse -File -ErrorAction SilentlyContinue | Where-Object { $_.Name -ieq $fileName }
        $matchCount = ($matches | Measure-Object).Count

        if ($matchCount -gt 1) {
            # Multiple versions found — do not auto-resolve, record suggestion
            $fixes.Add([pscustomobject]@{ target = $resolved; fix = 'mehrere Versionen. (Prüfen)'; matches = $matchCount }) | Out-Null
            Write-Information ("[link-scan] Mehrere Versionen für {0} gefunden: {1} Treffer" -f $fileName, $matchCount) -Tags 'LinkScan'
            continue
        }

        if ($matchCount -eq 1) {
            $found = $matches | Select-Object -First 1
            # compute a relative path from the markdown file's directory to the found file
            # We'll compute per-broken-entry replacements below (need the original markdown file)
            $fixes.Add([pscustomobject]@{ target = $resolved; fix = $found.FullName; matches = $matchCount }) | Out-Null
            Write-Information ("[link-scan] Ein Treffer für {0} gefunden: {1}" -f $fileName, $found.FullName) -Tags 'LinkScan'
        } else {
            # no matches found in repo — leave as-is but note
            $fixes.Add([pscustomobject]@{ target = $resolved; fix = 'nicht gefunden im Repo'; matches = 0 }) | Out-Null
            Write-Information ("[link-scan] Keine Repo-Treffer für {0}" -f $fileName) -Tags 'LinkScan'
        }
    }

    # Apply replacements per file: iterate broken items and update their source files
    foreach ($b in $broken) {
        $srcFile = $b.file
        $target = $b.resolved
        # find corresponding fix info (match by resolved path)
        $info = $fixes | Where-Object { $_.target -eq $target } | Select-Object -First 1
        if (-not $info) { continue }

        # read content and prepare replacement string
        $content = Get-Content -LiteralPath $srcFile -Raw -ErrorAction SilentlyContinue
        if (-not $content) { continue }

        if ($info.matches -gt 1) {
            $replacement = 'mehrere Versionen. (Prüfen)'
        } elseif ($info.matches -eq 1) {
            # compute relative path from src file directory to found file
            $foundFull = $info.fix
            try {
                $rel = [IO.Path]::GetRelativePath((Split-Path -Parent $srcFile), $foundFull)
            } catch {
                # fallback: use forward-slash relative from repo root
                $rel = Join-Path '..' $fileName
            }
            # normalize for markdown links (use forward slashes)
            $replacement = $rel -replace '\\','/'
        } else {
            $replacement = $info.fix
        }

        # make a backup before changing (store in central backup directory)
        $stamp = Get-Date -Format 'yyyyMMdd_HHmmss'
        $baseName = [IO.Path]::GetFileName($srcFile)
        $backup = Join-Path $backupRoot ("{0}_{1}.bak.linkscan" -f $stamp, $baseName)
        Copy-Item -LiteralPath $srcFile -Destination $backup -Force

        # Replace exact occurrences of the original target inside parentheses in markdown and other simple refs
        $escapedTarget = [regex]::Escape($b.target)
        $pattern = "(?<=\()$escapedTarget(?=\))"
        $newContent = [regex]::Replace($content, $pattern, [System.Text.RegularExpressions.MatchEvaluator]{ param($m) $replacement })

        if ($newContent -ne $content) {
            Set-Content -LiteralPath $srcFile -Value $newContent -Encoding utf8BOM
            Write-Information ("[link-scan] Datei aktualisiert: {0} (ersetze {1} -> {2})" -f $srcFile, $b.target, $replacement) -Tags 'LinkScan'
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

Set-Content -LiteralPath $reportPath -Value ($summary -join [Environment]::NewLine) -Encoding utf8BOM
Write-Information ("[link-scan] Report geschrieben: {0}" -f $reportPath) -Tags 'LinkScan'

