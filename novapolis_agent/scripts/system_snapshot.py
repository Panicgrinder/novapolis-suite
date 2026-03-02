#!/usr/bin/env python
"""Best-effort System-Snapshot fuer Hub/Agent-Studio (Windows-first)."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from typing import Any


def _run_powershell_json(ps_code: str) -> dict[str, Any]:
    command = [
        "powershell",
        "-NoLogo",
        "-NoProfile",
        "-Command",
        ps_code,
    ]
    try:
        proc = subprocess.run(command, capture_output=True, text=True, timeout=6.0, check=False)
    except subprocess.TimeoutExpired:
        return {}
    if proc.returncode != 0:
        return {}
    output = proc.stdout.strip()
    if not output:
        return {}
    try:
        parsed = json.loads(output)
    except Exception:
        return {}
    if isinstance(parsed, dict):
        return parsed
    return {}


def _collect_windows_cpu_ram() -> tuple[float | None, float | None]:
    ps = (
        "$cpu=(Get-CimInstance Win32_Processor | "
        "Measure-Object -Property LoadPercentage -Average).Average;"
        "$os=Get-CimInstance Win32_OperatingSystem;"
        "$total=[double]$os.TotalVisibleMemorySize;"
        "$free=[double]$os.FreePhysicalMemory;"
        "$ram=0;"
        "if($total -gt 0){$ram=(($total-$free)/$total)*100};"
        "@{cpu=[math]::Round($cpu,1);ram=[math]::Round($ram,1)}|ConvertTo-Json -Compress"
    )
    payload = _run_powershell_json(ps)
    cpu_raw = payload.get("cpu")
    ram_raw = payload.get("ram")
    cpu = float(cpu_raw) if isinstance(cpu_raw, (int, float)) else None
    ram = float(ram_raw) if isinstance(ram_raw, (int, float)) else None
    return cpu, ram


def _collect_windows_cpu_temp() -> float | None:
    ps = (
        "$t=Get-CimInstance -Namespace root/wmi -ClassName MSAcpi_ThermalZoneTemperature "
        "-ErrorAction SilentlyContinue | Select-Object -First 1 CurrentTemperature;"
        "if($t -and $t.CurrentTemperature){"
        "$c=[math]::Round(($t.CurrentTemperature/10)-273.15,1);"
        "@{temp=$c}|ConvertTo-Json -Compress"
        "}"
    )
    payload = _run_powershell_json(ps)
    temp_raw = payload.get("temp")
    if isinstance(temp_raw, (int, float)):
        value = float(temp_raw)
        if -20.0 <= value <= 130.0:
            return value
    return None


def _collect_nvidia_gpu() -> tuple[float | None, float | None, float | None, float | None]:
    if shutil.which("nvidia-smi") is None:
        return None, None, None, None
    command = [
        "nvidia-smi",
        "--query-gpu=utilization.memory,memory.used,memory.total,temperature.gpu",
        "--format=csv,noheader,nounits",
    ]
    proc = subprocess.run(command, capture_output=True, text=True, timeout=2.0, check=False)
    if proc.returncode != 0:
        return None, None, None, None
    line = proc.stdout.strip().splitlines()[0] if proc.stdout.strip() else ""
    if not line:
        return None, None, None, None
    parts = [p.strip() for p in line.split(",")]
    if len(parts) < 4:
        return None, None, None, None
    vram_pct = None
    vram_used_mb = None
    vram_total_mb = None
    temp = None
    try:
        vram_pct = float(parts[0])
    except Exception:
        vram_pct = None
    try:
        vram_used_mb = float(parts[1])
    except Exception:
        vram_used_mb = None
    try:
        vram_total_mb = float(parts[2])
    except Exception:
        vram_total_mb = None
    try:
        temp = float(parts[3])
    except Exception:
        temp = None
    return vram_pct, vram_used_mb, vram_total_mb, temp


def main() -> int:
    cpu_pct = None
    ram_pct = None
    cpu_temp_c = None

    if sys.platform.startswith("win"):
        cpu_pct, ram_pct = _collect_windows_cpu_ram()
        cpu_temp_c = _collect_windows_cpu_temp()

    gpu_vram_percent, gpu_vram_used_mb, gpu_vram_total_mb, gpu_temp_c = _collect_nvidia_gpu()

    payload: dict[str, Any] = {
        "ok": True,
        "cpu_percent": cpu_pct,
        "ram_percent": ram_pct,
        "gpu_vram_percent": gpu_vram_percent,
        "gpu_vram_used_mb": gpu_vram_used_mb,
        "gpu_vram_total_mb": gpu_vram_total_mb,
        "cpu_temp_c": cpu_temp_c,
        "gpu_temp_c": gpu_temp_c,
    }
    print(json.dumps(payload, ensure_ascii=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
