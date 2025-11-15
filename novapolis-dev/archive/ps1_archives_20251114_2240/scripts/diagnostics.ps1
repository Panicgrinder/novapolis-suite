[CmdletBinding()]
param()

---
archived: "true"
Timestamp: 2025-11-15 05:59
---

$root = Split-Path -Parent $PSScriptRoot
$cleanupScript = Join-Path $PSScriptRoot "cleanup_workspace_files.ps1"

$rootCount = (Get-ChildItem -Path $root -Filter "*.code-workspace").Count
$recurseCount = (Get-ChildItem -Path $root -Filter "*.code-workspace" -Recurse).Count
$cleanupHash = Get-FileHash -LiteralPath $cleanupScript -Algorithm SHA256

[PSCustomObject]@{
    RootWorkspaceCount    = $rootCount
    RecursiveWorkspaceCount = $recurseCount
    CleanupScriptSha256   = $cleanupHash.Hash
}
