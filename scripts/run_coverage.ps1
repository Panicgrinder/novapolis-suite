param(
    [string]$Python = ""
)
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$coverConfig = Join-Path $root "novapolis_agent\.coveragerc"
if (-not $Python -or -not (Test-Path -LiteralPath $Python)) {
    $Python = Join-Path $root ".venv\Scripts\python.exe"
}
if (-not (Test-Path -LiteralPath $Python)) {
    Write-Error "Python interpreter not found: $Python"
    exit 1
}
# CWD is set by the task to novapolis_agent; provide explicit coveragerc path from root
& $Python -m pytest -q --cov --cov-report=term-missing --cov-branch --cov-config "$coverConfig" --cov-fail-under=80
exit $LASTEXITCODE
