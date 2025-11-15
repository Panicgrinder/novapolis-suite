---
archived: "true"
Timestamp: 2025-11-15 04:07
---
<#
Runs pytest with coverage using the workspace's root venv if available.
Splits logic across steps to avoid complex -Command quoting issues in VS Code tasks.
Also writes machine-readable artifacts (JUnit XML, coverage XML) and a short summary.

Note: Parameterisierung ist vorerst deaktiviert, um einen ParamSet-Fehler in einigen PS-Umgebungen zu umgehen.
Später können optionale Flags (Quiet/Pattern/Markers/FailUnder/SkipCollectCheck) wieder aktiviert werden.
#>

# Static defaults (can be re-introduced as parameters later)
$Quiet = $false
$Pattern = $null
$Markers = $null
$FailUnder = 80
$SkipCollectCheck = $false

$ErrorActionPreference = 'Stop'

# Derive workspace root from this script's location (scripts/ -> root)
$scriptDir = $PSScriptRoot
if (-not $scriptDir) {
    # Fallback for environments that don't set PSScriptRoot
    $scriptDir = Split-Path -Path $MyInvocation.MyCommand.Path -Parent
}
$root = Split-Path -Path $scriptDir -Parent

# Determine Python interpreter (prefer root .venv)
$python = Join-Path -Path $root -ChildPath '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $python)) {
    $python = 'python'
}

# Coverage config and working directory
$agentDir = Join-Path -Path $root -ChildPath 'novapolis_agent'
$cover = Join-Path -Path $agentDir -ChildPath '.coveragerc'

# Artifacts directory
$artDir = Join-Path -Path $root -ChildPath 'outputs\test-artifacts'
if (-not (Test-Path -LiteralPath $artDir)) {
    New-Item -ItemType Directory -Path $artDir | Out-Null
}
$junitXml = Join-Path -Path $artDir -ChildPath 'junit.xml'
$covXml = Join-Path -Path $artDir -ChildPath 'coverage.xml'
$summaryPath = Join-Path -Path $artDir -ChildPath 'summary.txt'

Push-Location -LiteralPath $agentDir
try {
    # Optional safety: guard against accidentally huge test runs
    if (-not $SkipCollectCheck) {
        $maxTestFiles = 400
        $collectArgs = @('--collect-only')
        if ($Pattern) { $collectArgs += @('-k', $Pattern) }
        if ($Markers) { $collectArgs += @('-m', $Markers) }
        $collectOutput = & $python -m pytest @collectArgs 2>&1
        $collectedFiles = $collectOutput | Where-Object { $_ -match '::' } | ForEach-Object { ($_ -split '::')[0] }
        $uniqueFiles = $collectedFiles | Sort-Object -Unique
        $fileCount = ($uniqueFiles | Measure-Object).Count
        if ($fileCount -gt $maxTestFiles) {
            Write-Host "STOP: Zu viele Testdateien gesammelt ($fileCount > $maxTestFiles). Bitte Scope prüfen."
            exit 2
        }
    }

    # Build pytest args
    $args = @()
    if ($Quiet) { $args += '-q' }
    if ($Pattern) { $args += @('-k', $Pattern) }
    if ($Markers) { $args += @('-m', $Markers) }

    # Coverage + reports (term + xml), threshold parametric
    $args += @('--cov', '--cov-report=term-missing', '--cov-branch', "--cov-config=$cover")
    $args += @("--cov-report=xml:$covXml", "--junitxml=$junitXml", "--cov-fail-under=$FailUnder")

    # Run pytest
    & $python -m pytest @args
    $exit = $LASTEXITCODE

    # Write summary
    $ts = (Get-Date).ToString('yyyy-MM-dd HH:mm')
    $lines = @(
        "timestamp: $ts",
        "exitcode: $exit",
        "junit: $junitXml",
        "coverage_xml: $covXml"
    )
    $lines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

    if ($exit -eq 0) {
        Write-Host 'Pytest PASS'
    } else {
        Write-Host "Pytest FAIL ($exit)"
    }
    exit $exit
}
finally {
    Pop-Location
}
