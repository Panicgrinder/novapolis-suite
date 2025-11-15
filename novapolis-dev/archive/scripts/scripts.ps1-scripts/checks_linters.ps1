param()

$ErrorActionPreference = 'Stop'
$root = Split-Path -Path $PSScriptRoot -Parent
Set-Location $root

$python = Join-Path $root ".venv\Scripts\python.exe"
if (-not (Test-Path -LiteralPath $python)) { $python = 'python' }

# Run linters and black-check
& $python -m ruff check .
$ruffExit = $LASTEXITCODE
& $python -m black --check .
$blackExit = $LASTEXITCODE

if ($ruffExit -ne 0 -or $blackExit -ne 0) { exit 1 }
exit 0
