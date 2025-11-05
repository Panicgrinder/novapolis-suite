param(
    [string]$Python = ""
)
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$script = Join-Path $root "novapolis_agent\scripts\append_done.py"
if (-not $Python -or -not (Test-Path -LiteralPath $Python)) {
    $Python = Join-Path $root ".venv\Scripts\python.exe"
}
if (-not (Test-Path -LiteralPath $Python)) {
    Write-Error "Python interpreter not found: $Python"
    exit 1
}
& $Python "$script"
exit $LASTEXITCODE
