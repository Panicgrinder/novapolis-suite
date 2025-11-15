$ErrorActionPreference = 'Stop'
$root = (git rev-parse --show-toplevel) 2>$null
if (-not $root) { $root = (Get-Location).Path }
$ts = (Get-Date).ToString('yyyy-MM-dd HH:mm')
$lockPath = Join-Path $root ".snapshot.now"
Set-Content -Path $lockPath -Value $ts -NoNewline -Encoding UTF8
Write-Host ("[snapshot-lock] wrote {0} to {1}" -f $ts, $lockPath) -ForegroundColor Green
