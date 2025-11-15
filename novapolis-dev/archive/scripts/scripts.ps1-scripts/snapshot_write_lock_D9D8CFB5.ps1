$ErrorActionPreference = 'Stop'
# Writes a lock file with the current system timestamp (local) used by snapshot_gate.ps1
$root = (git rev-parse --show-toplevel) 2>$null
if (-not $root) { $root = (Get-Location).Path }
$shell = if (Get-Command pwsh -ErrorAction SilentlyContinue) { 'pwsh' } else { 'powershell' }
$ts = & $shell -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd HH:mm'"
$ts = $ts.Trim()
$lockPath = Join-Path $root ".snapshot.now"
Set-Content -Path $lockPath -Value $ts -NoNewline -Encoding UTF8
Write-Host ("[snapshot-lock] wrote {0} to {1}" -f $ts, $lockPath) -ForegroundColor Green
