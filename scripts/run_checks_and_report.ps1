#requires -Version 7.0



<#



.SYNOPSIS



    Automatisierter Sammellauf fuer Lint-, Typ- und Test-Ergebnisse.







.DESCRIPTION



    Fuehrt auswaehlbare Pruefschritte aus (Ruff, Black, Markdownlint, Frontmatter-Validator,



    Pyright, Mypy, Pytest) und schreibt eine Markdown-Quittung unter .tmp-results/reports.



    Die Ausgabe enthaelt zusaetzlich eine Postflight-Schablone mit bereits ermittelten



    Fakten (Hash, Timestamp, Regel-Matrix etc.), damit KIs die Werte direkt uebernehmen



    koennen.







.EXAMPLE



    pwsh -File scripts/run_checks_and_report.ps1







.EXAMPLE



    pwsh -File scripts/run_checks_and_report.ps1 -SkipDocsLint -SkipFrontmatter







.NOTES



    Alle Pfade werden relativ zum Repo-Root aufgeloest. Encoding: UTF-8.



#>



param(



    [switch]$SkipCodeLint,



    [switch]$SkipDocsLint,



    [switch]$SkipTypes,



    [switch]$SkipCoverage,



    [switch]$SkipFrontmatter,



    [int]$MaxTestFiles = 40



)







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



    Push-Location $WorkingDirectory



    try {



        Write-Host "[run_checks] $Label ..." -ForegroundColor Cyan



        $allOutput = & $Command *>&1



        return @{ exit = $LASTEXITCODE; output = $allOutput }



    }



    finally {



        Pop-Location



    }



}







$scriptPath = $PSCommandPath



if (-not $scriptPath) { $scriptPath = $MyInvocation.MyCommand.Path }



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



$scriptSha = (Get-FileHash -Algorithm SHA256 -LiteralPath $MyInvocation.MyCommand.Path).Hash



$gitSha = (git -C $repoRoot rev-parse --short HEAD 2>$null)



if (-not $gitSha) { $gitSha = 'n/a' }



$pyproject = Join-Path $repoRoot 'pyproject.toml'



$projectVersion = 'n/a'



if (Test-Path -LiteralPath $pyproject) {



    $match = Select-String -Path $pyproject -Pattern '^[ \t]*version\s*=\s*"([^"]+)"' | Select-Object -First 1



    if ($match) { $projectVersion = $match.Matches[0].Groups[1].Value }



}







$pwdPath = (Get-Location).ProviderPath



$commandLine = $MyInvocation.Line



if (-not $commandLine) {



    $commandLine = "pwsh -File $scriptPath"



}







$result = [ordered]@{



    timestamp      = $timestamp



    git_sha        = $gitSha



    ps_version     = $psVersion



    pyproject_ver  = $projectVersion



    script_sha256  = $scriptSha



    lint_code      = @{ ran = $false; pass = $null; exit = $null }



    lint_docs      = @{ ran = $false; pass = $null; exit = $null }



    frontmatter    = @{ ran = $false; pass = $null; exit = $null }



    types          = @{ ran = $false; pass = $null; exit = $null }



    tests          = @{ ran = $false; pass = $null; exit = $null; collected_files = 0; coverage = 'n/a' }



}







if (-not $SkipCodeLint) {



    $ruffCmd = { & $script:pythonBinary -m ruff check . }



    $blackCmd = { & $script:pythonBinary -m black --check . }



    $ruff = Invoke-And-Capture -WorkingDirectory $repoRoot -Command $ruffCmd -Label 'ruff check'



    $black = Invoke-And-Capture -WorkingDirectory $repoRoot -Command $blackCmd -Label 'black --check'



    $ruffExit = $ruff.exit



    $blackExit = $black.exit



    $codeOk = ($ruffExit -eq 0 -and $blackExit -eq 0)



    $result.lint_code.ran = $true



    $result.lint_code.pass = $codeOk



    $result.lint_code.exit = if ($codeOk) { 0 } else { 1 }



}







if (-not $SkipDocsLint) {



    $mdCmd = { npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' }



    $md = Invoke-And-Capture -WorkingDirectory $repoRoot -Command $mdCmd -Label 'markdownlint-cl2'



    $mdExit = $md.exit



    $result.lint_docs.ran = $true



    $result.lint_docs.pass = ($mdExit -eq 0)



    $result.lint_docs.exit = $mdExit



}







if ((-not $SkipFrontmatter) -and (Test-Path -LiteralPath $frontmatterScript)) {



    $fmCmd = { & $script:pythonBinary $script:frontmatterScriptPath }



    $fm = Invoke-And-Capture -WorkingDirectory $repoRoot -Command $fmCmd -Label 'frontmatter-validator'



    $fmExit = $fm.exit



    $result.frontmatter.ran = $true



    $result.frontmatter.pass = ($fmExit -eq 0)



    $result.frontmatter.exit = $fmExit



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



}







$collectCmd = { & $script:pythonBinary -m pytest --collect-only }



$collect = Invoke-And-Capture -WorkingDirectory $agentDir -Command $collectCmd -Label 'pytest collect-only'



$collectedFiles = $collect.output | Where-Object { $_ -match '::' } | ForEach-Object { ($_ -split '::')[0] } | Sort-Object -Unique



$fileCount = @($collectedFiles).Count



$result.tests.collected_files = $fileCount



if ($fileCount -gt $MaxTestFiles) {



    Write-Warning "STOP: Zu viele Testdateien gesammelt ($fileCount > $MaxTestFiles)."



    $result.tests.ran = $false



    $result.tests.pass = $false



    $result.tests.exit = 2



} else {



    $pytestArgs = @('--cov','--cov-branch')



    if (-not $SkipCoverage) {



        $covCfg = Join-Path $agentDir '.coveragerc'



        if (Test-Path -LiteralPath $covCfg) { $pytestArgs += @('--cov-config', $covCfg) }



        $pytestArgs += '--cov-fail-under=80'



    }



    $script:pytestArgsLocal = $pytestArgs



    $testCmd = { & $script:pythonBinary -m pytest @script:pytestArgsLocal }



    $tests = Invoke-And-Capture -WorkingDirectory $agentDir -Command $testCmd -Label 'pytest'



    $script:pytestArgsLocal = $null



    $testExit = $tests.exit



    $result.tests.ran = $true



    $result.tests.pass = ($testExit -eq 0)



    $result.tests.exit = $testExit



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







$codeStatus = if ($result.lint_code.ran) { if ($result.lint_code.pass) { 'PASS' } else { 'FAIL' } } else { 'SKIP' }



$docsStatus = if ($result.lint_docs.ran) { if ($result.lint_docs.pass) { 'PASS' } else { 'FAIL' } } else { 'SKIP' }



$fmStatus = if ($result.frontmatter.ran) { if ($result.frontmatter.pass) { 'PASS' } else { 'FAIL' } } else { 'SKIP' }



$typeStatus = if ($result.types.ran) { if ($result.types.pass) { 'PASS' } else { 'FAIL' } } else { 'SKIP' }



$testStatus = if ($result.tests.pass) { 'PASS' } else { 'FAIL' }



$summaryLine = "ruff/black=$codeStatus; markdownlint=$docsStatus; frontmatter=$fmStatus; types=$typeStatus; pytest=$testStatus (files=$($result.tests.collected_files); cov=$($result.tests.coverage))"







$frontmatterExit = if ($result.frontmatter.ran) { $result.frontmatter.exit } else { 'NA' }



$docsExit = if ($result.lint_docs.ran) { $result.lint_docs.exit } else { 'NA' }







$ruleUsage = [ordered]@{



    'R-WRAP' = $true



    'R-STOP' = $false



    'R-FM' = (-not $SkipFrontmatter)



    'R-LINT' = ((-not $SkipCodeLint) -or (-not $SkipDocsLint))



    'R-SCAN' = $false



    'R-CTX' = $true



    'R-SEC' = $true



    'R-LOG' = $true



    'R-COV' = (-not $SkipCoverage)



    'R-IDX' = $false



    'R-COMM' = $true



    'R-RED' = $false



    'R-TODO' = $false



    'R-TIME' = $true



    'R-SAFE' = $true



}







$ruleString = ($ruleUsage.GetEnumerator() | ForEach-Object { "{0}({1})" -f $_.Key, ($(if ($_.Value) { 'true' } else { 'false' })) }) -join ','



$ruleDetails = 'Automatisierter Checklauf; keine Mutationen.'







$todoFile = Join-Path $repoRoot 'todo.root.md'



$openTodos = 'n/a'



if (Test-Path -LiteralPath $todoFile) {



    $todoMatches = Select-String -Path $todoFile -Pattern '^\s*-\s*\[ \]'



    if ($todoMatches) { $openTodos = $todoMatches.Count } else { $openTodos = 0 }



}







$postflight = [ordered]@{



    meta = [ordered]@{



        Modus = 'Postflight'



        Modell = '<SET BY AGENT>'



        Arbeitsverzeichnis = $pwdPath



        RepoRoot = $repoRoot



        PSScriptRoot = $PSScriptRoot



        PSVersion = $psVersion



        Aufruf = ($commandLine -replace "\r?\n", ' ')



        SHA256 = $scriptSha



        STOPGate = 'deaktiviert'



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



$body = @()



$body += '---'



$body += "stand: $timestamp"



$body += 'update: Automatisierter Lint/Typen/Test-Run'



$body += "checks: $summaryLine"



$body += '---'



$body += ''



$body += 'Pruefzusammenfassung'



$body += '===================='



$body += ''



$body += "* Zeitpunkt: $timestamp"



$body += "* Git SHA: $gitSha"



$body += "* Version (pyproject): $projectVersion"



$body += "* Skript SHA256: $scriptSha"



$body += "* PowerShell-Version: $psVersion"



$body += ''



$body += 'Ergebnisse'



$body += '----------'



$body += ''



$body += '```json'



$body += ($result | ConvertTo-Json -Depth 5)



$body += '```'







$body += ''



$body += 'Postflight-Vorlage'



$body += '------------------'



$body += ''



$body += '```'



$body += "Meta: Modus=$($postflight.meta.Modus), Modell=$($postflight.meta.Modell), Arbeitsverzeichnis=$($postflight.meta.Arbeitsverzeichnis), RepoRoot=$($postflight.meta.RepoRoot), PSScriptRoot=$($postflight.meta.PSScriptRoot), PSVersion=$($postflight.meta.PSVersion), Aufruf=$($postflight.meta.Aufruf), SHA256=$($postflight.meta.SHA256), STOP-Gate=$($postflight.meta.STOPGate), Wrapper-Policy=$($postflight.meta.WrapperPolicy), Quellen=$([string]::Join(';', $postflight.meta.Quellen)), Aktion=$($postflight.meta.Aktion)"



$body += "Pruefung: markdownlint=$($postflight.pruefung.markdownlint), ExitcodeLint=$($postflight.pruefung.ExitcodeLint), behobenLint=$($postflight.pruefung.behobenLint), Frontmatter-Validator=$($postflight.pruefung.Frontmatter), ExitcodeFM=$($postflight.pruefung.ExitcodeFM), behobenFM=$($postflight.pruefung.behobenFM), Cleanup-WhatIf-Exit=$($postflight.pruefung.CleanupWhatIfExit), behobenWhatIf=$($postflight.pruefung.behobenWhatIf), Cleanup-Real-Exit=$($postflight.pruefung.CleanupRealExit), behobenReal=$($postflight.pruefung.behobenReal), WorkspaceScanRoot=$($postflight.pruefung.WorkspaceScanRoot), WorkspaceScanRecurse=$($postflight.pruefung.WorkspaceScanRecurse)"



$body += "Regeln: IDs=$($postflight.regeln.IDs), Details=$($postflight.regeln.Details)"



$body += "Todos: offen=$($postflight.todos.offen), BeispielFix=$($postflight.todos.BeispielFix), ReRun=$($postflight.todos.ReRun), Faellig=$($postflight.todos.Faellig)"



$body += "Ende: Timestamp=$($postflight.ende.Timestamp)"



$body += '```'



Set-Content -LiteralPath $reportPath -Value ($body -join [Environment]::NewLine) -Encoding UTF8



Write-Host "[run_checks] Report geschrieben: $reportPath" -ForegroundColor Green



exit 0

