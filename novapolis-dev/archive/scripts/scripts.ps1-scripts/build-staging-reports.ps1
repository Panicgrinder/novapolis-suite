param(
  [string]$Manifest = "novapolis-rp/database-curated/staging/manifest.json"
)

# Expect Python venv already activated; otherwise, rely on system python
$repoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))))
$script = Join-Path $repoRoot "novapolis-rp/coding/tools/curation/build_staging_reports.py"

Write-Host "Building staging reports from" $Manifest
python $script
if ($LASTEXITCODE -ne 0) {
  throw "Report build failed with exit code $LASTEXITCODE"
}
Write-Host "Done."
