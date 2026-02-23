#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any


def _is_venv_active() -> bool:
    return bool(getattr(sys, "base_prefix", sys.prefix) != sys.prefix)


def collect_prereqs(repo_root: Path, strict_venv: bool) -> dict[str, Any]:
    py = sys.version_info
    python_ok = (py.major, py.minor) >= (3, 11)
    venv_active = _is_venv_active()

    required_files = [
        repo_root / "novapolis_agent" / "run_server.py",
        repo_root / "novapolis_agent" / "app" / "main.py",
    ]
    files_ok = all(path.exists() for path in required_files)

    ollama_path = shutil.which("ollama")

    checks = {
        "python": {
            "ok": python_ok,
            "version": f"{py.major}.{py.minor}.{py.micro}",
            "required": ">=3.11",
        },
        "venv": {
            "ok": venv_active or (not strict_venv),
            "active": venv_active,
            "strict": strict_venv,
        },
        "required_files": {
            "ok": files_ok,
            "items": [str(path) for path in required_files],
        },
        "ollama_cli": {
            "ok": ollama_path is not None,
            "path": ollama_path,
            "note": "Optional for local runtime; required when using Ollama provider.",
        },
    }

    hard_failures = [
        not checks["python"]["ok"],
        not checks["venv"]["ok"],
        not checks["required_files"]["ok"],
    ]

    return {
        "ok": not any(hard_failures),
        "repo_root": str(repo_root),
        "checks": checks,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Check runtime prerequisites for novapolis_agent.")
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root path (default: current directory)",
    )
    parser.add_argument(
        "--strict-venv",
        action="store_true",
        help="Fail when no active virtual environment is detected",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON only",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    result = collect_prereqs(repo_root=repo_root, strict_venv=bool(args.strict_venv))

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("Runtime prerequisites")
        print(f"  repo_root: {result['repo_root']}")
        print(f"  ok:        {result['ok']}")
        for name, payload in result["checks"].items():
            print(f"  - {name}: {payload['ok']}")

    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
