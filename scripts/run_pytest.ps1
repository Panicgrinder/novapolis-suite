param(
    [string]$Python = ""
)
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
if (-not $Python -or -not (Test-Path -LiteralPath $Python)) {
    $Python = Join-Path $root ".venv\Scripts\python.exe"
}
if (-not (Test-Path -LiteralPath $Python)) {
    Write-Error "Python interpreter not found: $Python"
    exit 1
}
# CWD is set by the task to novapolis_agent; just run pytest quietly
& $Python -m pytest -q
exit $LASTEXITCODE
