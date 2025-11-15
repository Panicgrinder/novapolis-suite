param(
    [switch]$VerboseMode
)

$ErrorActionPreference = [System.Management.Automation.ActionPreference]::Stop

# Detect dot-sourcing (when invoked via ". script.ps1")
$script:dotSourced = ($MyInvocation.InvocationName -eq ".")

function Finish([int]$code) {
    $global:LASTEXITCODE = $code
    if ($script:dotSourced) {
        if ($VerboseMode) { Write-Host "[lint:names] dot-sourced; returning code $code" -ForegroundColor Yellow }
        return
    } else {
        exit $code
    }
}

# Resolve workspace root (three levels up from this script)
$workspaceRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\\..\\..")).Path

$hasDocker = $null -ne (Get-Command docker -ErrorAction SilentlyContinue)
$nodeExe = $null; $npmCmd = $null
$cmd = Get-Command node -ErrorAction SilentlyContinue; if ($cmd) { $nodeExe = $cmd.Source }
if (-not $nodeExe -and (Test-Path "C:\\Program Files\\nodejs\\node.exe")) { $nodeExe = "C:\\Program Files\\nodejs\\node.exe" }
if (-not $nodeExe -and (Test-Path "C:\\Program Files (x86)\\nodejs\\node.exe")) { $nodeExe = "C:\\Program Files (x86)\\nodejs\\node.exe" }
$cmd = Get-Command npm -ErrorAction SilentlyContinue; if ($cmd) { $npmCmd = $cmd.Source }
if (-not $npmCmd -and (Test-Path "C:\\Program Files\\nodejs\\npm.cmd")) { $npmCmd = "C:\\Program Files\\nodejs\\npm.cmd" }
if (-not $npmCmd -and (Test-Path "C:\\Program Files (x86)\\nodejs\\npm.cmd")) { $npmCmd = "C:\\Program Files (x86)\\nodejs\\npm.cmd" }
$hasNode = [string]::IsNullOrWhiteSpace($nodeExe) -eq $false
$hasNpm  = [string]::IsNullOrWhiteSpace($npmCmd) -eq $false

if ($VerboseMode) {
    Write-Host "Workspace: $workspaceRoot"
    Write-Host "Docker: $hasDocker, Node: $hasNode, Npm: $hasNpm"
}

if ($hasDocker) {
    Write-Host "[lint:names] Running in Docker (node:22-alpine)" -ForegroundColor Cyan
    & docker run --rm -v "${workspaceRoot}:/workdir" -w /workdir node:22-alpine sh -lc "npm ci --prefix coding/tools/validators && node coding/tools/validators/src/check-names.js"
    Finish $LASTEXITCODE
}
elseif ($hasNode -and $hasNpm) {
    Write-Host "[lint:names] Running locally (Node/npm)" -ForegroundColor Cyan
    Push-Location (Join-Path $workspaceRoot "coding\tools\validators")
    & $npmCmd ci
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[lint:names] npm ci failed (likely missing package-lock). Falling back to npm install..." -ForegroundColor Yellow
        & $npmCmd install --no-audit --no-fund
        if ($LASTEXITCODE -ne 0) { Pop-Location; Finish $LASTEXITCODE; return }
    }
    & $nodeExe src/check-names.js
    $code = $LASTEXITCODE
    Pop-Location
    if ($code -ne 0) { Finish $code } else { Finish 0 }
}
else {
    Write-Host "Voraussetzungen fehlen: Docker Desktop oder Node.js (npm). Optionen: 1) Dev Containers 2) Docker Desktop 3) Node.js LTS" -ForegroundColor Yellow
    Finish 1
}
