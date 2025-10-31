param(
    [string]$ScriptFile,
    [string[]]$ScriptArgs,
    [string]$Command,
    [int]$TimeoutSec = 7200,
    [string]$MutexName = "Global\\NovapolisRP.Tasks.Lock"
)

# Ensure .NET types are available
Add-Type -AssemblyName System.Threading | Out-Null

$mutex = $null
function Get-SafeMutexName([string]$Name) {
    if ([string]::IsNullOrWhiteSpace($Name)) { return "Global\\NovapolisRP_Tasks_Lock" }
    # Allow only safe chars for object manager path; keep single backslashes (namespace separator)
    $san = ($Name -replace "[^A-Za-z0-9_\-.\\]", "_")
    # Avoid trailing/back-to-back backslashes
    $san = $san.TrimEnd('\')
    if ([string]::IsNullOrWhiteSpace($san)) { $san = "Global\\NovapolisRP_Tasks_Lock" }
    return $san
}

function New-NamedMutex([string]$Name) {
    try {
        return New-Object System.Threading.Mutex($false, $Name)
    }
    catch {
        # Fallbacks: try sanitized global, then local
        $fallback1 = "Global\\NovapolisRP_Tasks_Lock"
        try {
            return New-Object System.Threading.Mutex($false, $fallback1)
        } catch {
            $fallback2 = "NovapolisRP_Tasks_Lock"
            return New-Object System.Threading.Mutex($false, $fallback2)
        }
    }
}
try {
    $safeName = Get-SafeMutexName $MutexName
    $mutex = New-NamedMutex $safeName
    $acquired = $mutex.WaitOne([TimeSpan]::FromSeconds($TimeoutSec))
    if (-not $acquired) {
        Write-Error "Task-Lock konnte nicht erworben werden (Timeout). Ein anderer Task läuft bereits."
        exit 1
    }

    if ($ScriptFile) {
        & $ScriptFile @ScriptArgs
        $exit = $LASTEXITCODE
    }
    elseif ($Command) {
        powershell -NoProfile -ExecutionPolicy Bypass -Command $Command
        $exit = $LASTEXITCODE
    }
    else {
        Write-Error "with_lock.ps1: Kein -ScriptFile oder -Command angegeben."
        $exit = 1
    }
}
finally {
    if ($mutex) {
        try { $mutex.ReleaseMutex() | Out-Null } catch { }
    }
}
exit $exit
