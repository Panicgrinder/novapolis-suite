Param()

# Determine repository root relative to this script
$repo = Resolve-Path (Join-Path $PSScriptRoot '..')

$targets = @(
  (Join-Path $repo 'novapolis.code-workspace'),
  (Join-Path $repo 'cvn-agend-novapolis-rp-workspace.code-workspace')
)

foreach ($t in $targets) {
  if (Test-Path -LiteralPath $t) {
    try {
      Remove-Item -LiteralPath $t -Force
      Write-Host "Deleted: $t"
    }
    catch {
      Write-Host "Failed to delete: $t"
      Write-Host $_
      exit 1
    }
  } else {
    Write-Host "Not found: $t"
  }
}
