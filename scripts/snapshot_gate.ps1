param(
    [int]$ToleranceMinutes = 5
)

$ErrorActionPreference = 'Stop'

function Get-RepoRoot {
    $scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
    return (Resolve-Path (Join-Path $scriptDir '..')).Path
}

function Get-CurrentTimestamp {
    # Required command per policy
    $ts = & powershell -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd HH:mm'"
    return $ts.Trim()
}

function Get-StagedMarkdownFiles {
    $files = git diff --cached --name-only --diff-filter=ACMRT | Where-Object { $_ -match '\.md$' }
    return $files
}

function Get-StagedFileContent([string]$path) {
    $content = git show ":$path" 2>$null
    return $content
}

function Find-StandTimestamp([string]$content) {
    # Look only in the first ~40 lines for YAML frontmatter 'stand:'
    $lines = $content -split "\r?\n"
    $limit = [Math]::Min($lines.Length, 40)
    for ($i = 0; $i -lt $limit; $i++) {
        $m = [regex]::Match($lines[$i], '^\s*stand:\s*(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})\s*$')
        if ($m.Success) { return $m.Groups[1].Value }
    }
    return $null
}

function Is-TimestampFresh([string]$standTs, [string]$nowTs, [int]$tolMin) {
    try {
        $fmt = 'yyyy-MM-dd HH:mm'
        $a = [datetime]::ParseExact($standTs, $fmt, $null)
        $b = [datetime]::ParseExact($nowTs, $fmt, $null)
        $delta = [Math]::Abs(($a - $b).TotalMinutes)
        return ($delta -le $tolMin)
    } catch { return $false }
}

# Allow bypass for emergency
if ($env:SNAPSHOT_GATE_BYPASS -eq '1') {
    Write-Host "[snapshot-gate] BYPASS set. Skipping checks." -ForegroundColor Yellow
    exit 0
}

$root = Get-RepoRoot
Set-Location $root

# Only run if git is available
try { git rev-parse --is-inside-work-tree *> $null } catch {
    Write-Host "[snapshot-gate] Not a git repo. Skipping." -ForegroundColor Yellow
    exit 0
}

$current = Get-CurrentTimestamp
$files = Get-StagedMarkdownFiles

if (-not $files -or $files.Count -eq 0) {
    exit 0
}

$failed = @()
foreach ($f in $files) {
    $content = Get-StagedFileContent $f
    if (-not $content) { continue }
    $standTs = Find-StandTimestamp $content
    if (-not $standTs) { continue }

    # Only enforce if the stand line is changed in this commit
    $diffLine = git diff --cached -U0 -- "$f" | Select-String -Pattern '^[+].*\bstand:\s*' -SimpleMatch | Select-Object -First 1
    if (-not $diffLine) {
        continue
    }

    if (-not (Is-TimestampFresh $standTs $current $ToleranceMinutes)) {
        $failed += [pscustomobject]@{ File=$f; Stand=$standTs; Now=$current }
    }
}

if ($failed.Count -gt 0) {
    Write-Host "[snapshot-gate] FAIL: Nicht-aktueller 'stand:' Timestamp in folgenden Dateien:" -ForegroundColor Red
    foreach ($x in $failed) {
        Write-Host (" - {0}: stand={1} | now={2}" -f $x.File, $x.Stand, $x.Now) -ForegroundColor Red
    }
    Write-Host "\nBitte vor dem Commit die Systemzeit holen und übernehmen:" -ForegroundColor Red
    Write-Host '  cd "F:/VS Code Workspace/Main"; powershell -NoProfile -Command "Get-Date -Format ''yyyy-MM-dd HH:mm''"' -ForegroundColor Red
    Write-Host "Danach YAML-Frontmatter 'stand:' aktualisieren und erneut committen." -ForegroundColor Red
    Write-Host "Bypass (nicht empfohlen): setx SNAPSHOT_GATE_BYPASS 1 (neues Terminal nötig)" -ForegroundColor DarkYellow
    exit 1
}

Write-Host "[snapshot-gate] PASS: Alle 'stand:'-Timestamps frisch (±$ToleranceMinutes min)." -ForegroundColor Green
exit 0
