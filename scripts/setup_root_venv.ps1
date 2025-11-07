# Requires: PowerShell 7+
# Purpose: Create/ensure root .venv and install dependencies (idempotent)
# Usage: pwsh -NoProfile -File scripts/setup_root_venv.ps1

[CmdletBinding()]
param(
    [switch] $Recreate
)

$ErrorActionPreference = 'Stop'

function Write-Info([string]$msg) { Write-Host "[setup_venv] $msg" -ForegroundColor Cyan }
function Write-Warn([string]$msg) { Write-Host "[setup_venv] WARN: $msg" -ForegroundColor Yellow }
function Write-Err([string]$msg) { Write-Host "[setup_venv] ERROR: $msg" -ForegroundColor Red }

$root = Split-Path -Parent $PSScriptRoot
Set-Location $root
$venvPath = Join-Path $root '.venv'
$venvPython = Join-Path $venvPath 'Scripts\python.exe'

Write-Info "Root: $root"
Write-Info "Venv: $venvPath"

if ($Recreate -and (Test-Path -LiteralPath $venvPath)) {
    Write-Warn "Recreate requested: removing existing .venv"
    Remove-Item -Recurse -Force -LiteralPath $venvPath
}

if (-not (Test-Path -LiteralPath $venvPath)) {
    Write-Info "Creating virtual environment (.venv)"
    $created = $false
    try {
        & py -3 -m venv $venvPath
        if ($LASTEXITCODE -eq 0) { $created = $true }
    } catch {}
    if (-not $created) {
        Write-Warn "Fallback to 'python -m venv'"
        & python -m venv $venvPath
    }
}

if (-not (Test-Path -LiteralPath $venvPython)) {
    Write-Err "python.exe not found in .venv (expected: $venvPython)"
    exit 1
}

# Ensure pip up-to-date
Write-Info "Upgrading pip"
& $venvPython -m pip install --upgrade pip

# Install requirements (base + dev if present)
$reqBase = Join-Path $root 'requirements.txt'
$reqDev  = Join-Path $root 'requirements-dev.txt'

if (Test-Path -LiteralPath $reqBase) {
    Write-Info "Installing requirements.txt"
    & $venvPython -m pip install -r $reqBase
} else {
    Write-Warn "requirements.txt not found (skipping)"
}

if (Test-Path -LiteralPath $reqDev) {
    Write-Info "Installing requirements-dev.txt"
    & $venvPython -m pip install -r $reqDev
} else {
    Write-Info "requirements-dev.txt not present (optional)"
}

# Print versions summary
$pyver = & $venvPython --version
$pipver = & $venvPython -m pip --version
Write-Host "[setup_venv] Python: $pyver" -ForegroundColor Green
Write-Host "[setup_venv] Pip: $pipver" -ForegroundColor Green

Write-Info "Done. You can now use the interpreter at: $venvPython"
