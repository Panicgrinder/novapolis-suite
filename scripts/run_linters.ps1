$ErrorActionPreference = 'Continue'
Set-StrictMode -Version Latest
# Normalize console rendering to avoid spaced characters in some terminals
try { $global:PSStyle.OutputRendering = 'PlainText' } catch {}
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch {}

Write-Host "Running linters..." -ForegroundColor Cyan

$root = Split-Path -Parent $MyInvocation.MyCommand.Path | Split-Path -Parent
$python = Join-Path $root ".venv/Scripts/python.exe"
if (-not (Test-Path $python)) {
  Write-Host "Python venv not found at $python" -ForegroundColor Yellow
  $python = "python"
}

Push-Location $root
try {
  $mdExit = 0
  $ruffExit = 0
  $blackExit = 0

  Write-Host "[1/3] markdownlint-cli2..." -ForegroundColor Cyan
  try {
    npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc "**/*.md"
    $mdExit = $LASTEXITCODE
  } catch {
    Write-Host "markdownlint-cli2 failed to run: $_" -ForegroundColor Red
    $mdExit = 1
  }
  Write-Host ("MD_EXIT:{0}" -f $mdExit)

  Write-Host "[2/3] ruff check..." -ForegroundColor Cyan
  try {
    & $python -m ruff check .
    $ruffExit = $LASTEXITCODE
  } catch {
    Write-Host "ruff failed to run: $_" -ForegroundColor Red
    $ruffExit = 1
  }
  Write-Host ("RUFF_EXIT:{0}" -f $ruffExit)

  Write-Host "[3/3] black --check..." -ForegroundColor Cyan
  try {
    & $python -m black --check .
    $blackExit = $LASTEXITCODE
  } catch {
    Write-Host "black failed to run: $_" -ForegroundColor Red
    $blackExit = 1
  }
  Write-Host ("BLACK_EXIT:{0}" -f $blackExit)

  $total = 0
  if ($mdExit -ne 0 -or $ruffExit -ne 0 -or $blackExit -ne 0) { $total = 1 }
  Write-Host ("TOTAL_EXIT:{0}" -f $total)
  exit $total
}
finally {
  Pop-Location
}
