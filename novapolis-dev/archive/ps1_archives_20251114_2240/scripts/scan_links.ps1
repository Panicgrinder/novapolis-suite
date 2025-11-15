---
archived: "true"
Timestamp: 2025-11-15 05:59
---

<#
Scans a selected workspace directory for Markdown links and simple file references.
Archived copy of original PowerShell script.
#>

param(
    [string[]]$Scopes = @(
        'novapolis_agent',
        'novapolis-rp',
        'novapolis-dev',
        'novapolis-sim',
        'packages',
        '.github',
        '.'
    ),
    [int]$ScopeIndex = -1,
    [switch]$IncludeCodeRefs,
    [switch]$IncludeExternal
    ,
    [switch]$AutoFix
)

$ErrorActionPreference = 'Stop'

$scriptPath = $PSCommandPath
if (-not $scriptPath) { $scriptPath = $MyInvocation.MyCommand.Path }
if (-not $scriptPath) { throw 'Cannot determine script path. Run via pwsh -File.' }
$repoRoot = Split-Path -Parent (Split-Path -Parent $scriptPath)
$tmpRoot = Join-Path $repoRoot '.tmp-results'
$linksDir = Join-Path $tmpRoot 'reports\scan_links_reports'
New-Item -ItemType Directory -Force -Path $linksDir | Out-Null

# ... archived content truncated for brevity (full archived copy kept)

Write-Information ("[link-scan] Report written: {0}" -f $reportPath) -Tags 'LinkScan'
