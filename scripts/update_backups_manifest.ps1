<#
.SYNOPSIS
Generates Backups/manifest.v1.json and manifest.v1.sha256sum.txt with SHA-256 checksums.

.DESCRIPTION
Enumerates backup artifacts in the Backups directory, computes deterministic metadata,
and emits a JSON manifest next to a sha256sum-compatible checksum list.
Run with PowerShell 7 (pwsh) -NoProfile to avoid user profile side-effects.
#>
[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [string]$BackupsPath,

    [Parameter()]
    [string]$ManifestFile = "manifest.v1.json",

    [Parameter()]
    [string]$ChecksumFile = "manifest.v1.sha256sum.txt",

    [switch]$IncludeSubdirectories
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Resolve-BackupsPath {
    param([string]$InputPath)

    if ([string]::IsNullOrWhiteSpace($InputPath)) {
        $repoRoot = Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')
        return Join-Path $repoRoot "Backups"
    }

    return $InputPath
}

$backupsPathResolved = Resolve-BackupsPath -InputPath $BackupsPath
$backupsFullPath = [System.IO.Path]::GetFullPath($backupsPathResolved)

if (-not (Test-Path -LiteralPath $backupsFullPath -PathType Container)) {
    throw "Backups path '$backupsFullPath' does not exist."
}

$searchParams = @{ Path = $backupsFullPath; File = $true }
if ($IncludeSubdirectories.IsPresent) {
    $searchParams.Recurse = $true
}

$excludedNames = @(
    'manifest.v1.json',
    'manifest.v1.sha256sum.txt',
    'rotation.log',
    'README.md',
    'AUDIT.md'
)

$allFiles = Get-ChildItem @searchParams | Where-Object { $excludedNames -notcontains $_.Name }

if (-not $allFiles) {
    Write-Warning "No backup artifacts found in '$backupsFullPath'. Manifest will contain zero entries."
}

$normalizedBase = $backupsFullPath
if (-not $normalizedBase.EndsWith([System.IO.Path]::DirectorySeparatorChar)) {
    $normalizedBase += [System.IO.Path]::DirectorySeparatorChar
}

$entries = @()
foreach ($file in $allFiles) {
    $hash = Get-FileHash -Algorithm SHA256 -LiteralPath $file.FullName
    $relative = $file.FullName.Substring($normalizedBase.Length)
    if ([string]::IsNullOrWhiteSpace($relative)) {
        $relative = $file.Name
    }

    $entries += [pscustomobject]@{
        filename    = $relative.Replace([System.IO.Path]::DirectorySeparatorChar, '/')
        size_bytes  = $file.Length
        sha256      = $hash.Hash.ToLowerInvariant()
        created_at  = $file.CreationTimeUtc.ToString('o')
        modified_at = $file.LastWriteTimeUtc.ToString('o')
    }
}

if (-not $entries) {
    $entries = @()
}

$sortedEntries = $entries | Sort-Object filename

$manifest = [pscustomobject]@{
    manifest_version = '1'
    generated_at     = [DateTime]::UtcNow.ToString('o')
    generator        = 'scripts/update_backups_manifest.ps1'
    base_path        = $backupsFullPath
    entry_count      = $sortedEntries.Count
    entries          = $sortedEntries
}

$manifestPath = Join-Path $backupsFullPath $ManifestFile
$manifest | ConvertTo-Json -Depth 6 | Out-File -FilePath $manifestPath -Encoding utf8

$checksumPath = Join-Path $backupsFullPath $ChecksumFile
$checksumLines = $sortedEntries | ForEach-Object { "{0}  {1}" -f $_.sha256, $_.filename }
$checksumLines | Out-File -FilePath $checksumPath -Encoding ascii

Write-Host "Manifest written to $manifestPath"
Write-Host "Checksums written to $checksumPath"
Write-Host ("Entries: {0}" -f $sortedEntries.Count)
