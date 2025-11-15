---
archived: "true"
Timestamp: 2025-11-15 04:07
---
<#
Stand: 2025-11-10 11:35
Lightweight PowerShell smoke test for the Novapolis Sim stack.

What it does:
- Starts the Sim API (uvicorn) from the workspace venv
- Waits for port 8765 to become available
- Sends one POST /world/step and checks the JSON response
- Stops the uvicorn process and returns a meaningful exit code

Usage: pwsh -File .\scripts\verify_sim.ps1
#>

Set-StrictMode -Version Latest
Write-Host "[verify_sim] Workspace root: $PWD"

$root = Resolve-Path -Path (Join-Path $PSScriptRoot "..")
$pythonCandidate = Join-Path $root ".venv\Scripts\python.exe"
if (Test-Path $pythonCandidate) { $python = $pythonCandidate } else { $python = "python" }

$uvArgs = "-m uvicorn app.api.sim:app --host 127.0.0.1 --port 8765"
Write-Host "[verify_sim] Using python: $python"

# Start uvicorn from the novapolis_agent working directory so imports work as expected
$agentCwd = Resolve-Path -Path (Join-Path $root "novapolis_agent")
Write-Host "[verify_sim] Starting uvicorn in cwd: $agentCwd"

$logDir = Join-Path $root "outputs"
if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir | Out-Null }
$outLog = Join-Path $logDir "uvicorn_verify_out.log"
$errLog = Join-Path $logDir "uvicorn_verify_err.log"

# Start uvicorn redirecting stdout/stderr to files
[System.IO.File]::WriteAllText($outLog, "[verify_sim] uvicorn stdout log`n")
[System.IO.File]::WriteAllText($errLog, "[verify_sim] uvicorn stderr log`n")
$proc = Start-Process -FilePath $python -ArgumentList $uvArgs -PassThru -WindowStyle Hidden -WorkingDirectory $agentCwd -RedirectStandardOutput $outLog -RedirectStandardError $errLog
try {
    # wait for port to be open
    $maxWait = 20
    $waited = 0
    while ($waited -lt $maxWait) {
        $conn = Test-NetConnection -ComputerName 127.0.0.1 -Port 8765 -WarningAction SilentlyContinue
        if ($conn -and $conn.TcpTestSucceeded) { break }
        Start-Sleep -Seconds 1
        $waited += 1
    }
        if ($waited -ge $maxWait) {
        Write-Host "[verify_sim] ERROR: uvicorn did not open port 8765 within timeout"
        try { Stop-Process -Id $proc.Id -ErrorAction SilentlyContinue } catch { Write-Verbose $_ }
        exit 2
    }

    Write-Host "[verify_sim] Port 8765 is open, sending POST /world/step"
    try {
        $resp = Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8765/world/step" -ContentType "application/json" -Body '{"dt":0.5}' -TimeoutSec 5
        Write-Host "[verify_sim] POST succeeded. Response: tick=$($resp.tick) time=$($resp.time)"
        $exitCode = 0
    } catch {
        Write-Host "[verify_sim] ERROR: POST failed: $($_.Exception.Message)"
        $exitCode = 3
    }
    } finally {
    if ($proc -and ($null -ne $proc.Id)) {
        Write-Host "[verify_sim] Stopping uvicorn (PID $($proc.Id))"
        try { Stop-Process -Id $proc.Id -Force -ErrorAction SilentlyContinue } catch { Write-Verbose $_ }
    }
}

exit $exitCode
