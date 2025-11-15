---
archived: "true"
Timestamp: 2025-11-15 04:07
---
[CmdletBinding(SupportsShouldProcess = $true)]
Param(
  [string[]] $Names,
  [switch] $VerboseLog
)

# Determine repository root relative to this script
$repo = Resolve-Path (Join-Path $PSScriptRoot '..')

# Build list of workspace files to remove. If -Names is provided, use the
# explicit whitelist; otherwise remove all *.code-workspace files in the repo
# root. This keeps the behaviour explicit but still guards against typos.
$targets = @()
if ($Names -and $Names.Count -gt 0) {
  foreach ($n in $Names) {
    $targets += (Join-Path $repo $n)
  }
} else {
  $targets = Get-ChildItem -LiteralPath $repo -Filter '*.code-workspace' -File |
    ForEach-Object { $_.FullName }
}

if (-not $targets -or $targets.Count -eq 0) {
  Write-Host "No .code-workspace files found at: $repo"
  exit 0
}

$failed = 0

foreach ($t in $targets) {
  if (Test-Path -LiteralPath $t) {
    try {
      $shouldRemove = $PSCmdlet.ShouldProcess($t, 'Remove')
      if ($shouldRemove) {
        Remove-Item -LiteralPath $t -Force -ErrorAction Stop
        if ($VerboseLog) {
          if ($WhatIfPreference) {
            Write-Host "Would delete (WhatIf): $t"
          } else {
            Write-Host "Deleted: $t"
          }
        }
      } elseif ($VerboseLog -and -not $WhatIfPreference) {
        Write-Host "Skipped (confirmation declined): $t"
      }
    }
    catch {
      Write-Host "Failed to delete: $t"
      Write-Host $_
      $failed++
    }
  } elseif ($VerboseLog) {
    Write-Host "Not found: $t"
  }
}

if ($failed -gt 0) {
  exit 1
}

exit 0
