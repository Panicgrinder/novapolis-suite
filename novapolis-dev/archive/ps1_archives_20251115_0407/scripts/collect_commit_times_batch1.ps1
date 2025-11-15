---
archived: "true"
Timestamp: 2025-11-15 04:07
---
$ErrorActionPreference='Stop'
$files = @(
  'novapolis-dev/archive/todo.root.archive.md',
  'novapolis-dev/archive/todo.rp.archive.md',
  'novapolis-dev/archive/todo.sim.archive.md',
  'novapolis-dev/docs/naming-policy.md',
  'novapolis-dev/docs/tests.md',
  'novapolis-dev/docs/todo.dev.md',
  'novapolis-dev/migrations/docs-migration-2025-10-29.md',
  'novapolis-rp/coding/devcontainer/README.md',
  'novapolis_agent/analysis_chat_routers.md',
  'novapolis_agent/eval/config/context.local.md',
  'novapolis_agent/eval/DEPRECATIONS.md',
  'novapolis_agent/eval/README.md',
  'novapolis_agent/scripts/README.md'
)
foreach ($f in $files) {
  if (-not (Test-Path -LiteralPath $f)) { Write-Output "$f|MISSING"; continue }
  $ci = git --no-pager log -1 --format=%ci -- $f 2>$null
  if (-not $ci) { $stand = Get-Date -Format 'yyyy-MM-dd HH:mm'; Write-Output "$f|NOLOG|$stand"; continue }
  $dt = [DateTimeOffset]::Parse($ci)
  $stand = $dt.ToLocalTime().ToString('yyyy-MM-dd HH:mm')
  Write-Output "$f|OK|$stand"
}
