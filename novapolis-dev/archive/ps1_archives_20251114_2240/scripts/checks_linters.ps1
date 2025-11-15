---
archived: "true"
Timestamp: 2025-11-15 04:07
---

param()

$ErrorActionPreference = 'Stop'
$root = Split-Path -Path $PSScriptRoot -Parent
Set-Location $root

$python = Join-Path $root ".venv\Scripts\python.exe"
if (-not (Test-Path -LiteralPath $python)) { $python = 'python' }

& $python -m ruff check .
$ruffExit = $LASTEXITCODE
& $python -m black --check .
$blackExit = $LASTEXITCODE

if ($ruffExit -ne 0 -or $blackExit -ne 0) { exit 1 }
exit 0
param()

$ErrorActionPreference = 'Stop'
$root = Split-Path -Path $PSScriptRoot -Parent
Set-Location $root

$python = Join-Path $root ".venv\Scripts\python.exe"
if (-not (Test-Path -LiteralPath $python)) { $python = 'python' }

& $python -m ruff check .
$ruffExit = $LASTEXITCODE
& $python -m black --check .
$blackExit = $LASTEXITCODE

if ($ruffExit -ne 0 -or $blackExit -ne 0) { exit 1 }
exit 0
