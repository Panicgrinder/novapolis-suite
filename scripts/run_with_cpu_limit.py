#!/usr/bin/env python3
"""Run a command with a conservative CPU affinity and lower priority."""

from __future__ import annotations

import argparse
import ctypes
import os
import subprocess
import sys
from collections.abc import Sequence
from ctypes import wintypes

DEFAULT_PRIORITY = "below_normal"
THREAD_LIMIT_ENV_VARS = (
    "OMP_NUM_THREADS",
    "OPENBLAS_NUM_THREADS",
    "MKL_NUM_THREADS",
    "NUMEXPR_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
    "RAYON_NUM_THREADS",
)
PRIORITY_CLASSES = {
    "idle": 0x00000040,
    "below_normal": 0x00004000,
    "normal": 0x00000020,
}
PROCESS_SET_INFORMATION = 0x0200
PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_QUERY_LIMITED_INFORMATION = 0x1000


def detect_logical_cpus() -> int:
    return max(1, os.cpu_count() or 1)


def default_cpu_limit(logical_cpus: int) -> int:
    if logical_cpus <= 2:
        return 1
    return min(4, max(2, logical_cpus // 2))


def resolve_cpu_limit(explicit_limit: int | None, logical_cpus: int) -> int:
    if explicit_limit is not None:
        return max(1, min(explicit_limit, logical_cpus))
    env_limit = os.environ.get("NVP_CPU_LIMIT", "").strip()
    if env_limit:
        try:
            return max(1, min(int(env_limit), logical_cpus))
        except ValueError:
            pass
    return default_cpu_limit(logical_cpus)


def build_affinity_mask(cpu_limit: int) -> int:
    return (1 << cpu_limit) - 1


def build_limited_env(base_env: dict[str, str], cpu_limit: int) -> dict[str, str]:
    env = dict(base_env)
    cpu_limit_text = str(cpu_limit)
    for key in THREAD_LIMIT_ENV_VARS:
        env.setdefault(key, cpu_limit_text)
    env.setdefault("TOKENIZERS_PARALLELISM", "false")
    env["NVP_CPU_LIMIT"] = cpu_limit_text
    env["NVP_CPU_LIMIT_ACTIVE"] = cpu_limit_text
    return env


def _windows_kernel32() -> ctypes.WinDLL | None:
    if os.name != "nt":
        return None
    return ctypes.WinDLL("kernel32", use_last_error=True)


def set_current_process_limits(mask: int, priority: str) -> bool:
    kernel32 = _windows_kernel32()
    if kernel32 is None:
        return False
    process = kernel32.GetCurrentProcess()
    ok_affinity = bool(kernel32.SetProcessAffinityMask(process, ctypes.c_size_t(mask)))
    priority_class = PRIORITY_CLASSES.get(priority, PRIORITY_CLASSES[DEFAULT_PRIORITY])
    ok_priority = bool(kernel32.SetPriorityClass(process, wintypes.DWORD(priority_class)))
    return ok_affinity and ok_priority


def apply_limits_to_pid(pid: int, mask: int, priority: str) -> bool:
    kernel32 = _windows_kernel32()
    if kernel32 is None:
        return False
    desired_access = (
        PROCESS_SET_INFORMATION | PROCESS_QUERY_INFORMATION | PROCESS_QUERY_LIMITED_INFORMATION
    )
    handle = kernel32.OpenProcess(wintypes.DWORD(desired_access), False, wintypes.DWORD(pid))
    if not handle:
        return False
    try:
        ok_affinity = bool(kernel32.SetProcessAffinityMask(handle, ctypes.c_size_t(mask)))
        priority_class = PRIORITY_CLASSES.get(priority, PRIORITY_CLASSES[DEFAULT_PRIORITY])
        ok_priority = bool(kernel32.SetPriorityClass(handle, wintypes.DWORD(priority_class)))
    finally:
        kernel32.CloseHandle(handle)
    return ok_affinity and ok_priority


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a command with a conservative CPU limit for local tests/checks.",
    )
    parser.add_argument(
        "--max-cpus",
        type=int,
        default=None,
        help="Maximale Zahl logischer CPUs. Standard: auto bzw. NVP_CPU_LIMIT.",
    )
    parser.add_argument(
        "--priority",
        choices=sorted(PRIORITY_CLASSES),
        default=os.environ.get("NVP_CPU_PRIORITY", DEFAULT_PRIORITY),
        help="Windows-Prioritaetsklasse fuer den Kindprozess.",
    )
    parser.add_argument(
        "command",
        nargs=argparse.REMAINDER,
        help="Befehl nach --, der mit CPU-Limit ausgefuehrt wird.",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)
    if args.command and args.command[0] == "--":
        args.command = args.command[1:]
    return args


def run_limited_command(command: Sequence[str], cpu_limit: int, priority: str) -> int:
    if not command:
        raise ValueError("command must not be empty")
    mask = build_affinity_mask(cpu_limit)
    set_current_process_limits(mask, priority)
    env = build_limited_env(os.environ, cpu_limit)
    child = subprocess.Popen(list(command), env=env)
    apply_limits_to_pid(child.pid, mask, priority)
    return child.wait()


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    if not args.command:
        print("No command provided. Use -- <command> [args...]", file=sys.stderr)
        return 2
    logical_cpus = detect_logical_cpus()
    cpu_limit = resolve_cpu_limit(args.max_cpus, logical_cpus)
    print(
        f"[cpu-limit] logical={logical_cpus} active={cpu_limit} priority={args.priority}",
        flush=True,
    )
    return run_limited_command(args.command, cpu_limit, args.priority)


if __name__ == "__main__":
    raise SystemExit(main())
