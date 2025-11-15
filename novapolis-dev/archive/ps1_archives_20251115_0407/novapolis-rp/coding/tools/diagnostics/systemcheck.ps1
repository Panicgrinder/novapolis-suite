---
archived: "true"
Timestamp: 2025-11-15 04:07
---
#requires -Version 5.1
<#+
  System-Check (Windows) – Virtualisierung/WSL/Docker
  - Prüft: BIOS‑Virtualisierung (so gut wie möglich), optionale Windows‑Features, WSL‑Status/Version, Docker‑CLI
  - Ausgabe: PASS/WARN/FAIL mit kurzen Hinweisen
  - Exitcode: 0 (nur Diagnose)
#>
[CmdletBinding()]
param()

function Write-Result {
  param(
    [string]$Name,
    [ValidateSet('PASS','WARN','FAIL')]
    [string]$Status,
    [string]$Details = ''
  )
  $color = switch ($Status) {
    'PASS' { 'Green' }
    'WARN' { 'Yellow' }
    'FAIL' { 'Red' }
  }
  $label = "[{0}] {1}" -f $Status, $Name
  if ($Details) {
    Write-Host $label -ForegroundColor $color
    Write-Host "  → $Details"
  } else {
    Write-Host $label -ForegroundColor $color
  }
}

# 1) Virtualisierung in Firmware
$virtEnabled = $null
try {
  $line = systeminfo 2>$null | Select-String -Pattern "Virtualization Enabled In Firmware|Virtualisierung in der Firmware aktiviert" -ErrorAction SilentlyContinue
  if ($line) {
    $virtEnabled = ($line.ToString() -match '(Yes|Ja)')
  }
} catch {}

if ($null -ne $virtEnabled) {
  if ($virtEnabled) { Write-Result 'Virtualisierung (BIOS/UEFI)' 'PASS' 'Firmware‑Virtualisierung ist aktiviert.' }
  else { Write-Result 'Virtualisierung (BIOS/UEFI)' 'FAIL' 'Im BIOS/UEFI aktivieren (Intel VT‑x/VT‑d bzw. AMD‑V/SVM). Danach Windows neu starten.' }
} else {
  Write-Result 'Virtualisierung (BIOS/UEFI)' 'WARN' 'Konnte nicht sicher ermittelt werden. Prüfe Task‑Manager → Leistung → CPU: "Virtualisierung".'
}

# 2) Windows‑Features: VirtualMachinePlatform, WSL
$features = @{
  'VirtualMachinePlatform' = $null
  'Microsoft-Windows-Subsystem-Linux' = $null
}
foreach ($f in $features.Keys) {
  try {
    $state = (Get-WindowsOptionalFeature -Online -FeatureName $f -ErrorAction Stop).State
    $features[$f] = $state
  } catch { $features[$f] = 'NotPresent' }
}

foreach ($kvp in $features.GetEnumerator()) {
  $name = $kvp.Key
  $state = [string]$kvp.Value
  if ($state -eq 'Enabled') {
    Write-Result "Feature: $name" 'PASS' 'Aktiviert.'
  } elseif ($state -in @('Disabled','NotPresent')) {
    $hint = if ($name -eq 'VirtualMachinePlatform') { 'Aktiviere mit: dism /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart' } 
            elseif ($name -eq 'Microsoft-Windows-Subsystem-Linux') { 'Aktiviere mit: dism /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart' } 
            else { 'Aktiviere per DISM/Windows-Features.' }
    Write-Result "Feature: $name" 'FAIL' $hint
  } else {
    Write-Result "Feature: $name" 'WARN' "Status: $state"
  }
}

# 3) WSL Status/Version
$wslAvailable = $false
$defaultV = $null
try {
  $wslStatus = & wsl --status 2>&1
  if ($LASTEXITCODE -eq 0 -or $wslStatus) {
    $wslAvailable = $true
    $m = [regex]::Match(($wslStatus | Out-String), 'Default Version:\s*(\d)')
    if ($m.Success) { $defaultV = [int]$m.Groups[1].Value }
  }
} catch {}

if ($wslAvailable) {
  if ($defaultV -eq 2) { Write-Result 'WSL Default Version' 'PASS' 'Default Version: 2' }
  elseif ($defaultV -eq 1) { Write-Result 'WSL Default Version' 'WARN' 'Default ist 1. Empfohlen: wsl --set-default-version 2' }
  else { Write-Result 'WSL Default Version' 'WARN' 'Konnte Default nicht ermitteln. Prüfe: wsl --status' }
} else {
  Write-Result 'WSL' 'FAIL' 'WSL nicht verfügbar. Installiere/aktualisiere: wsl --install --no-distribution; danach Neustart.'
}

# 4) Docker CLI
$dockerCmd = Get-Command docker -ErrorAction SilentlyContinue
if ($dockerCmd) {
  Write-Result 'Docker CLI' 'PASS' "Gefunden: $($dockerCmd.Source)"
} else {
  Write-Result 'Docker CLI' 'WARN' 'Nicht gefunden. Für Dev‑Container ohne WSL kann Docker Desktop (Hyper‑V Backend) genutzt werden.'
}

Write-Host ''
Write-Host 'Empfohlene Schritte bei FAIL:' -ForegroundColor Cyan
Write-Host '  1) Firmware‑Virtualisierung aktivieren (BIOS/UEFI) und neu starten.'
Write-Host '  2) Features aktivieren (als Admin):' 
Write-Host '     dism /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart'
Write-Host '     dism /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart'
Write-Host '     shutdown /r /t 0'
Write-Host '  3) WSL aktualisieren & Default setzen:'
Write-Host '     wsl --update; wsl --set-default-version 2'
