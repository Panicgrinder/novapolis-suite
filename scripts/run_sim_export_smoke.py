from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

DEFAULT_EXPORT_EXE = "novapolis-sim/exports/windows/NovapolisSim.exe"


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the local Windows export smoke for novapolis-sim"
    )
    parser.add_argument("--repo-root", default=Path(__file__).resolve().parents[1])
    parser.add_argument("--export-exe", default=DEFAULT_EXPORT_EXE)
    parser.add_argument("--launch", action="store_true")
    parser.add_argument("--startup-timeout", type=float, default=3.0)
    return parser.parse_args(argv)


def _collect_companions(export_exe: Path) -> list[str]:
    stem = export_exe.stem
    directory = export_exe.parent
    companions = sorted(
        item.name
        for item in directory.iterdir()
        if item.is_file() and item.name != export_exe.name and item.stem == stem
    )
    return companions


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    repo_root = Path(args.repo_root).resolve()
    export_exe = (repo_root / args.export_exe).resolve()

    if not export_exe.exists():
        print(
            json.dumps(
                {
                    "ok": False,
                    "error": "export executable missing",
                    "expected": str(export_exe),
                },
                ensure_ascii=False,
            )
        )
        return 2

    payload: dict[str, object] = {
        "ok": True,
        "export_exe": str(export_exe),
        "companions": _collect_companions(export_exe),
    }

    if not args.launch:
        print(json.dumps(payload, ensure_ascii=False))
        return 0

    process = subprocess.Popen([str(export_exe)], cwd=export_exe.parent)
    try:
        exit_code = process.wait(timeout=float(args.startup_timeout))
    except subprocess.TimeoutExpired:
        process.terminate()
        try:
            process.wait(timeout=2.0)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=2.0)
        payload["launch"] = "started"
        print(json.dumps(payload, ensure_ascii=False))
        return 0

    if exit_code != 0:
        payload["ok"] = False
        payload["launch"] = "failed"
        payload["exit_code"] = exit_code
        print(json.dumps(payload, ensure_ascii=False))
        return int(exit_code) or 1

    payload["launch"] = "exited_cleanly"
    payload["exit_code"] = exit_code
    print(json.dumps(payload, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
