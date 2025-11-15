---
archived: "true"
Timestamp: 2025-11-15 04:07
---
<#
.SYNOPSIS
Implements tiered retention (daily/weekly/monthly/yearly) for backup artifacts.

.DESCRIPTION
Analyzes backup files in the Backups directory, determines which artifacts should be kept
according to configured retention windows, and optionally deletes the surplus files.
Run with PowerShell 7 (pwsh) -NoProfile to avoid user profile side-effects.
#>
[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [string]$BackupsPath,

    [int]$DailyRetentionDays = 14,
    [int]$WeeklyRetentionWeeks = 8,
    [int]$MonthlyRetentionMonths = 6,
    [int]$YearlyRetentionYears = 2,
    [int]$MinimumKeep = 5,

    [switch]$Apply,
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

$files = Get-ChildItem @searchParams | Where-Object { $excludedNames -notcontains $_.Name } | Sort-Object LastWriteTimeUtc -Descending

if (-not $files) {
    Write-Host "No backup artifacts found in '$backupsFullPath'."
    return
}

$now = [DateTime]::UtcNow
$calendar = [System.Globalization.CultureInfo]::InvariantCulture.Calendar
$keepSet = New-Object 'System.Collections.Generic.HashSet[string]' ([System.StringComparer]::OrdinalIgnoreCase)

function Add-KeepFile {
    param([System.IO.FileInfo]$File)
    $null = $keepSet.Add($File.FullName)
}

$takeCount = [Math]::Min($MinimumKeep, $files.Count)
for ($i = 0; $i -lt $takeCount; $i++) {
    Add-KeepFile -File $files[$i]
}

$dailyBuckets = @{}
$weeklyBuckets = @{}
$monthlyBuckets = @{}
$yearlyBuckets = @{}

$dailyCutoff = $DailyRetentionDays
$weeklyCutoff = $DailyRetentionDays + (7 * $WeeklyRetentionWeeks)
$monthlyCutoff = $weeklyCutoff + (30 * $MonthlyRetentionMonths)
$yearlyCutoff = $monthlyCutoff + (365 * $YearlyRetentionYears)

foreach ($file in $files) {
    if ($keepSet.Contains($file.FullName)) {
        continue
    }

    $ageDays = ($now - $file.LastWriteTimeUtc).TotalDays

    if ($ageDays -lt $dailyCutoff) {
        $key = $file.LastWriteTimeUtc.ToString('yyyy-MM-dd')
        if (-not $dailyBuckets.ContainsKey($key)) {
            $dailyBuckets[$key] = $true
            Add-KeepFile -File $file
        }
        continue
    }

    if ($ageDays -lt $weeklyCutoff) {
        $week = $calendar.GetWeekOfYear(
            $file.LastWriteTimeUtc,
            [System.Globalization.CalendarWeekRule]::FirstFourDayWeek,
            [DayOfWeek]::Monday
        )
        $key = '{0:0000}-W{1:00}' -f $file.LastWriteTimeUtc.Year, $week
        if (-not $weeklyBuckets.ContainsKey($key)) {
            $weeklyBuckets[$key] = $true
            Add-KeepFile -File $file
        }
        continue
    }

    if ($ageDays -lt $monthlyCutoff) {
        $key = $file.LastWriteTimeUtc.ToString('yyyy-MM')
        if (-not $monthlyBuckets.ContainsKey($key)) {
            $monthlyBuckets[$key] = $true
            Add-KeepFile -File $file
        }
        continue
    }

    if ($ageDays -lt $yearlyCutoff) {
        $key = $file.LastWriteTimeUtc.ToString('yyyy')
        if (-not $yearlyBuckets.ContainsKey($key)) {
            $yearlyBuckets[$key] = $true
            Add-KeepFile -File $file
        }
        continue
    }
}

$normalizedBase = $backupsFullPath
if (-not $normalizedBase.EndsWith([System.IO.Path]::DirectorySeparatorChar)) {
    $normalizedBase += [System.IO.Path]::DirectorySeparatorChar
}

$plan = foreach ($file in $files | Sort-Object LastWriteTimeUtc) {
    $relative = $file.FullName.Substring($normalizedBase.Length)
    if ([string]::IsNullOrWhiteSpace($relative)) {
        $relative = $file.Name
    }

    $action = if ($keepSet.Contains($file.FullName)) { 'Keep' } else { 'Delete' }
    $ageDaysRaw = ($now - $file.LastWriteTimeUtc).TotalDays

    [pscustomobject]@{
        Action       = $action
        File         = $relative.Replace([System.IO.Path]::DirectorySeparatorChar, '/')
        SizeBytes    = $file.Length
        ModifiedUtc  = $file.LastWriteTimeUtc.ToString('o')
        AgeDays      = [string]::Format([System.Globalization.CultureInfo]::InvariantCulture, '{0:0.0}', [Math]::Round($ageDaysRaw, 1))
    }
}

$deletePlan = @($plan | Where-Object { $_.Action -eq 'Delete' })
$keepPlan = @($plan | Where-Object { $_.Action -eq 'Keep' })

Write-Host "Retention plan:" -ForegroundColor Cyan
$plan | Format-Table -AutoSize
Write-Host
Write-Host ("Keep: {0} | Delete: {1}" -f $keepPlan.Count, $deletePlan.Count)

if (-not $Apply.IsPresent) {
    Write-Host "Dry-run complete. Re-run with -Apply to delete flagged files." -ForegroundColor Yellow
    return
}

if (-not $deletePlan) {
    Write-Host "Nothing to delete. Retention satisfied." -ForegroundColor Green
    return
}

$logPath = Join-Path $backupsFullPath 'rotation.log'
$logLines = @(
    ("[{0}] Deleted {1} file(s)" -f [DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ssZ'), $deletePlan.Count)
)

foreach ($entry in $deletePlan) {
    $target = Join-Path $backupsFullPath $entry.File.Replace('/', [System.IO.Path]::DirectorySeparatorChar)
    Remove-Item -LiteralPath $target -Force
    $logLines += ("- {0} (modified {1})" -f $entry.File, $entry.ModifiedUtc)
}

$logLines | Out-File -FilePath $logPath -Encoding ascii -Append

Write-Host "Deleted files:" -ForegroundColor Red
$deletePlan | Format-Table -AutoSize
