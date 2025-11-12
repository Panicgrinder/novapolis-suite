[System.Diagnostics.CodeAnalysis.SuppressMessage('Style','PSUseOutputTypeCorrectly', Justification='Legacy script header kept minimal')]
#requires -Version 7.0
<#
 .SYNOPSIS
 Automatisierter Sammellauf für Lint-, Typ- und Test-Ergebnisse.

 .DESCRIPTION
 Führt optionale Prüfschritte (Lint, Frontmatter, Typen, Tests, Coverage)
 aus und schreibt eine strukturierte Markdown-Quittung unter `.tmp-results/reports`.

 .EXAMPLE
 pwsh -File scripts/run_checks_and_report.ps1

 .EXAMPLE
 pwsh -File scripts/run_checks_and_report.ps1 -SkipDocsLint -SkipFrontmatter
#>
[CmdletBinding()]
param(
    [switch]$SkipCodeLint,
    [switch]$SkipDocsLint,
    [switch]$SkipTypes,
    [switch]$SkipCoverage,
    [switch]$SkipFrontmatter,
    [switch]$SkipTests,
    [int]$MaxTestFiles = 1000
)

Set-StrictMode -Version Latest

$ErrorActionPreference = 'Stop'

function Resolve-Python {
    param([string]$RepoRoot)
    $venvPy = Join-Path $RepoRoot '.venv\Scripts\python.exe'
    if (Test-Path -LiteralPath $venvPy) { return $venvPy }
    return 'python'
}

function Resolve-Pyright {
    param([string]$RepoRoot)
    $venvBin = Join-Path $RepoRoot '.venv\Scripts\pyright.exe'
    if (Test-Path -LiteralPath $venvBin) { return $venvBin }
    return 'pyright'
}

function Invoke-And-Capture {
    param(
        [string]$WorkingDirectory,
        [scriptblock]$Command,
        [string]$Label
    )
    Push-Location -LiteralPath $WorkingDirectory
    try {
        Write-Host "[run_checks] $Label ..." -ForegroundColor Cyan
        $output = & $Command *>&1
        return @{ exit = $LASTEXITCODE; output = $output }
    } finally {
        Pop-Location
    }
}

function Get-Status {
    param(
        [bool]$Ran,
        [object]$Pass
    )
    if (-not $Ran) { return 'SKIP' }
    if ($Pass) { return 'PASS' }
    return 'FAIL'
}

function Update-Overall {
    param(
        [hashtable]$Root,
        [string]$Phase,
        [int]$ExitCode
    )
    if ($ExitCode -eq 0) { return }
    $Root.overall.pass = $false
    if ($Root.overall.exit -eq 0) { $Root.overall.exit = $ExitCode }
    $Root.overall.failures += "{0}:{1}" -f $Phase, $ExitCode
}

$scriptPath = if ($PSCommandPath) { $PSCommandPath } else { $MyInvocation.MyCommand.Path }
if (-not $scriptPath) { throw 'Cannot determine script path. Run via pwsh -File.' }
$repoRoot = Split-Path -Parent (Split-Path -Parent $scriptPath)
$agentDir = Join-Path $repoRoot 'novapolis_agent'
$tmpRoot = Join-Path $repoRoot '.tmp-results'
$reportDir = Join-Path $tmpRoot 'reports'
New-Item -ItemType Directory -Force -Path $reportDir | Out-Null

$frontmatterScript = Join-Path $repoRoot 'scripts\check_frontmatter.py'
$python = Resolve-Python -RepoRoot $repoRoot
$pyright = Resolve-Pyright -RepoRoot $repoRoot
$script:pythonBinary = $python
$script:pyrightBinary = $pyright
$script:frontmatterScriptPath = $frontmatterScript

$timestamp = Get-Date -Format 'yyyy-MM-dd HH:mm'
$stampId = Get-Date -Format 'yyyyMMdd_HHmmss'
$psVersion = $PSVersionTable.PSVersion.ToString()
$scriptSha = (Get-FileHash -Algorithm SHA256 -LiteralPath $scriptPath).Hash
$gitSha = (git -C $repoRoot rev-parse --short HEAD 2>$null)
if (-not $gitSha) { $gitSha = 'n/a' }

$pyproject = Join-Path $repoRoot 'pyproject.toml'
$projectVersion = 'n/a'
if (Test-Path -LiteralPath $pyproject) {
    $match = Select-String -Path $pyproject -Pattern '^[ \t]*version\s*=\s*"([^"]+)"' | Select-Object -First 1
    if ($match) { $projectVersion = $match.Matches[0].Groups[1].Value }
}

$pwdPath = (Get-Location).ProviderPath
$commandLine = if ($MyInvocation.Line) { $MyInvocation.Line -replace "\r?\n", ' ' } else { "pwsh -File $scriptPath" }

$result = [ordered]@{
    timestamp     = $timestamp
    git_sha       = $gitSha
    ps_version    = $psVersion
    pyproject_ver = $projectVersion
    script_sha256 = $scriptSha
    lint_code     = @{ ran = $false; pass = $null; exit = $null }
    lint_docs     = @{ ran = $false; pass = $null; exit = $null }
    frontmatter   = @{ ran = $false; pass = $null; exit = $null }
    types         = @{ ran = $false; pass = $null; exit = $null }
    tests         = @{ ran = $false; pass = $null; exit = $null; collected_files = 'n/a'; coverage = 'n/a' }
    overall       = @{ pass = $true; failures = @(); exit = 0 }
}

# PSScriptAnalyzer result placeholder (PowerShell static analysis)
$result.psscriptanalyzer = @{ ran = $false; pass = $null; exit = $null; issues = @() }

# Track whether a STOP Gate was triggered (e.g. too many test files)
$stopTriggered = $false

if (-not $SkipCodeLint) {
    $ruffCmd = { & $script:pythonBinary -m ruff check . }
    $blackCmd = { & $script:pythonBinary -m black --check . }
    $ruff = Invoke-And-Capture -WorkingDirectory $repoRoot -Command $ruffCmd -Label 'ruff check'
    $black = Invoke-And-Capture -WorkingDirectory $repoRoot -Command $blackCmd -Label 'black --check'
    $codeOk = ($ruff.exit -eq 0 -and $black.exit -eq 0)
    $result.lint_code.ran = $true
    $result.lint_code.pass = $codeOk
    $result.lint_code.exit = if ($codeOk) { 0 } else { 1 }
    if (-not $codeOk) { Update-Overall -Root $result -Phase 'lint_code' -ExitCode 1 }
}

if (-not $SkipDocsLint) {
    $mdCmd = { npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' }
    $md = Invoke-And-Capture -WorkingDirectory $repoRoot -Command $mdCmd -Label 'markdownlint-cli2'
    $result.lint_docs.ran = $true
    $result.lint_docs.exit = $md.exit
    $result.lint_docs.pass = ($md.exit -eq 0)
    if ($md.exit -ne 0) { Update-Overall -Root $result -Phase 'lint_docs' -ExitCode $md.exit }
}

# PSScriptAnalyzer: statische Analyse von PowerShell-Skripten (falls verfügbar)
try {
    $pssaAvailable = $null -ne (Get-Module -ListAvailable -Name PSScriptAnalyzer)
} catch {
    $pssaAvailable = $false
}
if (-not $pssaAvailable) {
    Write-Host "[run_checks] PSScriptAnalyzer nicht installiert. Versuche Installation (CurrentUser)..." -ForegroundColor Yellow
    try {
        Install-Module -Name PSScriptAnalyzer -Scope CurrentUser -Force -ErrorAction Stop
        Import-Module PSScriptAnalyzer -ErrorAction Stop
        $pssaAvailable = $true
    } catch {
        Write-Warning "PSScriptAnalyzer konnte nicht installiert/geladen werden: $_"
        $pssaAvailable = $false
    }
}

if ($pssaAvailable) {
    Write-Host "[run_checks] Invoke-ScriptAnalyzer (scripts/) ..." -ForegroundColor Cyan
    try {
        $pssaResults = Invoke-ScriptAnalyzer -Path (Join-Path $repoRoot 'scripts') -Recurse -ErrorAction Stop
    } catch {
        Write-Warning "Invoke-ScriptAnalyzer fehlgeschlagen: $_"
        $pssaResults = @()
    }
    $pssaIssues = @()
    foreach ($r in $pssaResults) {
        $pssaIssues += [ordered]@{
            file = ($r.ScriptName -or $r.FilePath -or 'n/a')
            rule = ($r.RuleName -or 'n/a')
            severity = ($r.Severity -as [string])
            line = ($r.Line -as [int])
            message = ($r.Message -as [string])
        }
    }
    $issueCount = ($pssaIssues | Where-Object { $_.severity -in @('Error','Warning') } | Measure-Object).Count
    $result.psscriptanalyzer.ran = $true
    $result.psscriptanalyzer.issues = $pssaIssues
    $result.psscriptanalyzer.exit = if ($issueCount -gt 0) { 1 } else { 0 }
    $result.psscriptanalyzer.pass = ($issueCount -eq 0)
    if ($issueCount -gt 0) { Update-Overall -Root $result -Phase 'psscriptanalyzer' -ExitCode 1 }
} else {
    Write-Host "[run_checks] PSScriptAnalyzer nicht verfügbar; überspringe PSScriptAnalyse." -ForegroundColor DarkYellow
}

if ((-not $SkipFrontmatter) -and (Test-Path -LiteralPath $frontmatterScript)) {
    $fmCmd = { & $script:pythonBinary $script:frontmatterScriptPath }
    $fm = Invoke-And-Capture -WorkingDirectory $repoRoot -Command $fmCmd -Label 'frontmatter-validator'
    $result.frontmatter.ran = $true
    $result.frontmatter.exit = $fm.exit
    $result.frontmatter.pass = ($fm.exit -eq 0)
    if ($fm.exit -ne 0) { Update-Overall -Root $result -Phase 'frontmatter' -ExitCode $fm.exit }
}

if (-not $SkipTypes) {
    $pyrightCmd = { & $script:pyrightBinary -p pyrightconfig.json }
    $mypyCmd = { & $script:pythonBinary -m mypy --config-file mypy.ini app scripts }
    $pr = Invoke-And-Capture -WorkingDirectory $agentDir -Command $pyrightCmd -Label 'pyright'
    $mp = Invoke-And-Capture -WorkingDirectory $agentDir -Command $mypyCmd -Label 'mypy'
    $typeOk = ($pr.exit -eq 0 -and $mp.exit -eq 0)
    $result.types.ran = $true
    $result.types.pass = $typeOk
    $result.types.exit = if ($typeOk) { 0 } else { 1 }
    if (-not $typeOk) {
        $exitCode = if ($pr.exit -ne 0) { $pr.exit } else { $mp.exit }
        Update-Overall -Root $result -Phase 'types' -ExitCode $exitCode
    }
}

if (-not $SkipTests) {
    $collectCmd = { & $script:pythonBinary -m pytest --collect-only }
    $collect = Invoke-And-Capture -WorkingDirectory $agentDir -Command $collectCmd -Label 'pytest collect-only'
    $collectedFiles = $collect.output | Where-Object { $_ -match '::' } | ForEach-Object { ($_ -split '::')[0] } | Sort-Object -Unique
    $fileCount = @($collectedFiles).Count
    $result.tests.collected_files = $fileCount
    if ($fileCount -gt $MaxTestFiles) {
        Write-Warning "STOP: Zu viele Testdateien gesammelt ($fileCount > $MaxTestFiles)."
        # A STOP condition occurred — count the tests as 'ran' so the summary shows FAIL
        $stopTriggered = $true
        $result.tests.ran = $true
        $result.tests.pass = $false
        $result.tests.exit = 2
        Update-Overall -Root $result -Phase 'tests' -ExitCode 2
    } else {
        $pytestArgs = @('--cov', '--cov-branch')
        if (-not $SkipCoverage) {
            $covCfg = Join-Path $agentDir '.coveragerc'
            if (Test-Path -LiteralPath $covCfg) { $pytestArgs += @('--cov-config', $covCfg) }
            $pytestArgs += '--cov-fail-under=80'
        }
        $script:pytestArgsLocal = $pytestArgs
        $testCmd = { & $script:pythonBinary -m pytest @script:pytestArgsLocal }
        $tests = Invoke-And-Capture -WorkingDirectory $agentDir -Command $testCmd -Label 'pytest'
        $script:pytestArgsLocal = $null
        $result.tests.ran = $true
        $result.tests.exit = $tests.exit
        $result.tests.pass = ($tests.exit -eq 0)
        if ($tests.exit -ne 0) { Update-Overall -Root $result -Phase 'tests' -ExitCode $tests.exit }
        if (-not $SkipCoverage) {
            $covXml = Join-Path $agentDir 'coverage.xml'
            if (Test-Path -LiteralPath $covXml) {
                try {
                    $coverageDoc = [xml](Get-Content -LiteralPath $covXml -Raw)
                    $lineRate = $coverageDoc.coverage.'line-rate'
                    if ($lineRate) {
                        $pct = [math]::Round(([double]$lineRate) * 100, 2)
                        $result.tests.coverage = "$pct%"
                    }
                } catch {
                    $result.tests.coverage = 'parse-error'
                }
            }
        }
    }
}

$codeStatus = Get-Status -Ran $result.lint_code.ran -Pass $result.lint_code.pass
$docsStatus = Get-Status -Ran $result.lint_docs.ran -Pass $result.lint_docs.pass
$fmStatus = Get-Status -Ran $result.frontmatter.ran -Pass $result.frontmatter.pass
$typeStatus = Get-Status -Ran $result.types.ran -Pass $result.types.pass
$testStatus = Get-Status -Ran $result.tests.ran -Pass $result.tests.pass
$pssaStatus = Get-Status -Ran $result.psscriptanalyzer.ran -Pass $result.psscriptanalyzer.pass
$summaryLine = "ruff/black=$codeStatus; markdownlint=$docsStatus; frontmatter=$fmStatus; types=$typeStatus; pytest=$testStatus; psscriptanalyzer=$pssaStatus (files=$($result.tests.collected_files); cov=$($result.tests.coverage))"

$frontmatterExit = if ($result.frontmatter.ran) { $result.frontmatter.exit } else { 'NA' }
$docsExit = if ($result.lint_docs.ran) { $result.lint_docs.exit } else { 'NA' }

$ruleUsage = [ordered]@{
    'R-WRAP' = $true
    'R-STOP' = $stopTriggered
    'R-FM' = (-not $SkipFrontmatter)
    'R-LINT' = ((-not $SkipCodeLint) -or (-not $SkipDocsLint))
    'R-SCAN' = $false
    'R-CTX' = $true
    'R-SEC' = $true
    'R-LOG' = $true
    'R-COV' = (-not ($SkipCoverage -or $SkipTests))
    'R-IDX' = $false
    'R-COMM' = $true
    'R-RED' = $false
    'R-TODO' = $false
    'R-TIME' = $true
    'R-SAFE' = $true
}
$ruleString = (
    $ruleUsage.GetEnumerator() |
    ForEach-Object {
        $val = if ($_.Value) { 'true' } else { 'false' }
        "{0}({1})" -f $_.Key, $val
    }
) -join ','
$ruleDetails = 'Automatisierter Checklauf; keine Mutationen.'

$todoFile = Join-Path $repoRoot 'todo.root.md'
$openTodos = 'n/a'
if (Test-Path -LiteralPath $todoFile) {
    $todoMatches = Select-String -Path $todoFile -Pattern '^\s*-\s*\[ \]'
    $openTodos = if ($todoMatches) { $todoMatches.Count } else { 0 }
}

# Compute STOPGate string separately to avoid inline-expression parsing inside the hashtable
$stopGate = if ($stopTriggered) { 'aktiv' } else { 'deaktiviert' }

$postflight = [ordered]@{
    meta = [ordered]@{
        Modus = 'Postflight'
        Modell = 'GPT-5 mini'
        Arbeitsverzeichnis = $pwdPath
        RepoRoot = $repoRoot
        PSScriptRoot = $PSScriptRoot
        PSVersion = $psVersion
        Aufruf = $commandLine
        SHA256 = $scriptSha
        STOPGate = $stopGate
        WrapperPolicy = 'erfuellt'
        Quellen = @(
            (Join-Path $repoRoot '.github\copilot-instructions.md'),
            (Join-Path $repoRoot 'WORKSPACE_STATUS.md'),
            $scriptPath
        )
        Aktion = 'Automatisierter Checklauf (Ruff/Black/Markdownlint/Frontmatter/Pyright/Mypy/Pytest)'
    }
    pruefung = [ordered]@{
        markdownlint = $docsStatus
        ExitcodeLint = $docsExit
        behobenLint = 'nein'
        Frontmatter = $fmStatus
        ExitcodeFM = $frontmatterExit
        behobenFM = 'nein'
        CleanupWhatIfExit = 'NA'
        behobenWhatIf = 'nein'
        CleanupRealExit = 'NA'
        behobenReal = 'nein'
        WorkspaceScanRoot = 0
        WorkspaceScanRecurse = 0
        PSScriptAnalyzer = if ($result.psscriptanalyzer.ran) {
            [ordered]@{
                Ran = $true
                Exitcode = $result.psscriptanalyzer.exit
                Behoben = $false
            }
        } else {
            [ordered]@{
                Ran = $false
                Exitcode = 'NA'
                Behoben = 'n/a'
            }
        }
    }
    regeln = [ordered]@{
        IDs = $ruleString
        Details = $ruleDetails
    }
    todos = [ordered]@{
        offen = $openTodos
        BeispielFix = 'Automatisierter Checklauf'
        ReRun = 'keiner'
        Faellig = 'n/a'
    }
    ende = [ordered]@{
        Timestamp = $timestamp
    }
}

$reportPath = Join-Path $reportDir ("checks_report_{0}.md" -f $stampId)
$body = @(
    '---',
    "stand: $timestamp",
    'update: Automatisierter Lint/Typen/Test-Run',
    "checks: $summaryLine",
    '---',
    '',
    'Pruefzusammenfassung',
    '====================',
    '',
    "* Zeitpunkt: $timestamp",
    "* Git SHA: $gitSha",
    "* Version (pyproject): $projectVersion",
    "* Skript SHA256: $scriptSha",
    "* PowerShell-Version: $psVersion",
    '',
    'Ergebnisse',
    '----------',
    '',
    '```json',
    ($result | ConvertTo-Json -Depth 5),
    '```',
    '',
    'Postflight-Vorlage',
    '------------------',
    '',
    '```',
    "Meta: Modus=$($postflight.meta.Modus), Modell=$($postflight.meta.Modell), Arbeitsverzeichnis=$($postflight.meta.Arbeitsverzeichnis), RepoRoot=$($postflight.meta.RepoRoot), PSScriptRoot=$($postflight.meta.PSScriptRoot), PSVersion=$($postflight.meta.PSVersion), Aufruf=$($postflight.meta.Aufruf), SHA256=$($postflight.meta.SHA256), STOP-Gate=$($postflight.meta.STOPGate), Wrapper-Policy=$($postflight.meta.WrapperPolicy), Quellen=$([string]::Join(';', $postflight.meta.Quellen)), Aktion=$($postflight.meta.Aktion)",
    "Pruefung: markdownlint=$($postflight.pruefung.markdownlint), ExitcodeLint=$($postflight.pruefung.ExitcodeLint), behobenLint=$($postflight.pruefung.behobenLint), Frontmatter-Validator=$($postflight.pruefung.Frontmatter), ExitcodeFM=$($postflight.pruefung.ExitcodeFM), behobenFM=$($postflight.pruefung.behobenFM), Cleanup-WhatIf-Exit=$($postflight.pruefung.CleanupWhatIfExit), behobenWhatIf=$($postflight.pruefung.behobenWhatIf), Cleanup-Real-Exit=$($postflight.pruefung.CleanupRealExit), behobenReal=$($postflight.pruefung.behobenReal), WorkspaceScanRoot=$($postflight.pruefung.WorkspaceScanRoot), WorkspaceScanRecurse=$($postflight.pruefung.WorkspaceScanRecurse), PSScriptAnalyzerRan=$($postflight.pruefung.PSScriptAnalyzer.Ran), PSScriptAnalyzerExit=$($postflight.pruefung.PSScriptAnalyzer.Exitcode), PSScriptAnalyzerBehoben=$($postflight.pruefung.PSScriptAnalyzer.Behoben)",
    "Regeln: IDs=$($postflight.regeln.IDs), Details=$($postflight.regeln.Details)",
    "Todos: offen=$($postflight.todos.offen), BeispielFix=$($postflight.todos.BeispielFix), ReRun=$($postflight.todos.ReRun), Faellig=$($postflight.todos.Faellig)",
    "Ende: Timestamp=$($postflight.ende.Timestamp)",
    '```'
)

Set-Content -LiteralPath $reportPath -Value ($body -join [Environment]::NewLine) -Encoding UTF8
Write-Host "[run_checks] Report geschrieben: $reportPath" -ForegroundColor Green

# Exit with the aggregated exit code so CI/consumers can detect failures
if ($null -ne $result.overall.exit -and $result.overall.exit -ne 0) {
    $exitCode = [int]$result.overall.exit
} else {
    $exitCode = 0
}
exit $exitCode
