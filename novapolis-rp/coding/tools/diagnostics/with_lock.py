#!/usr/bin/env python3
"""
with_lock.py
Lightweight wrapper that acquires a named lock (via lockfile) and runs a script or command.
Designed as a Python replacement for `with_lock.ps1` so callers can prefer `python with_lock.py ...`.
"""
import argparse
import os
import sys
import tempfile
import time
import subprocess
import shlex
import hashlib


def safe_name(name: str) -> str:
    if not name:
        name = "NovapolisRP_Tasks_Lock"
    # keep only safe chars
    san = ''.join(c if c.isalnum() or c in ('_', '-', '.') else '_' for c in name)
    return san


def acquire_lock(lockpath: str, timeout: int) -> bool:
    start = time.time()
    while True:
        try:
            fd = os.open(lockpath, os.O_CREAT | os.O_EXCL | os.O_RDWR)
            os.write(fd, str(os.getpid()).encode('utf-8'))
            os.close(fd)
            return True
        except FileExistsError:
            if (time.time() - start) >= timeout:
                return False
            time.sleep(0.5)


def release_lock(lockpath: str) -> None:
    try:
        if os.path.exists(lockpath):
            os.remove(lockpath)
    except Exception:
        pass


def run_subprocess(cmd, shell=False):
    try:
        result = subprocess.run(cmd, shell=shell)
        return result.returncode
    except KeyboardInterrupt:
        return 130


def main():
    p = argparse.ArgumentParser(description="Acquire named lock and run script/command")
    p.add_argument('--script-file', '-s', help='Path to a script file to execute')
    p.add_argument('--script-args', '-a', nargs=argparse.REMAINDER, help='Arguments for the script')
    p.add_argument('--command', '-c', help='Command string to execute')
    p.add_argument('--timeout', '-t', type=int, default=7200, help='Timeout seconds to acquire lock')
    p.add_argument('--mutex-name', '-m', default='Global\\NovapolisRP.Tasks.Lock', help='Mutex name (sanitized)')
    args = p.parse_args()

    safe = safe_name(args.mutex_name)
    lockfile = os.path.join(tempfile.gettempdir(), f"{safe}.lock")

    got = acquire_lock(lockfile, args.timeout)
    if not got:
        print("Task-Lock konnte nicht erworben werden (Timeout). Ein anderer Task läuft bereits.")
        sys.exit(1)

    try:
        if args.script_file:
            path = args.script_file
            script_args = args.script_args or []
            if path.endswith('.py'):
                cmd = [sys.executable, path] + script_args
                rc = run_subprocess(cmd)
            elif path.endswith('.ps1'):
                # fallback: call pwsh -File
                cmd = ['pwsh', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', path] + script_args
                rc = run_subprocess(cmd)
            else:
                # try to execute directly
                cmd = [path] + script_args
                rc = run_subprocess(cmd)
        elif args.command:
            # If first token is existing script, prefer file execution
            tokens = shlex.split(args.command)
            if tokens:
                first = tokens[0]
                if os.path.exists(first):
                    rest = tokens[1:]
                    if first.endswith('.py'):
                        cmd = [sys.executable, first] + rest
                        rc = run_subprocess(cmd)
                    elif first.endswith('.ps1'):
                        cmd = ['pwsh', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', first] + rest
                        rc = run_subprocess(cmd)
                    else:
                        cmd = [first] + rest
                        rc = run_subprocess(cmd)
                else:
                    # fallback to running via pwsh -Command to preserve behavior
                    rc = run_subprocess(['pwsh', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-Command', args.command])
            else:
                print('with_lock: empty command')
                rc = 1
        else:
            print('with_lock: Kein --script-file oder --command angegeben.')
            rc = 1
    finally:
        release_lock(lockfile)

    sys.exit(rc)


if __name__ == '__main__':
    main()
