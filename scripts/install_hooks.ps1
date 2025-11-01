$ErrorActionPreference = 'Stop'

function Get-RepoRoot {
  param([string]$start)
  if (-not $start) { $start = (Get-Location).Path }
  return $start
}

$root = Get-RepoRoot -start (Resolve-Path ".").Path
$src = Join-Path $root 'githooks'
$dst = Join-Path $root '.git/hooks'

if (-not (Test-Path $dst)) { throw ".git/hooks nicht gefunden. Bitte innerhalb eines Git-Repos ausführen." }

Get-ChildItem -Path $src -File | ForEach-Object {
  Copy-Item -Path $_.FullName -Destination (Join-Path $dst $_.Name) -Force
}

Write-Host "Lokale Git-Hooks installiert (Quelle: githooks → Ziel: .git/hooks)." -ForegroundColor Green
Write-Host "Hinweis: Git for Windows führt Shell-Hooks aus; dieser Hook ruft PowerShell auf." -ForegroundColor DarkGray
