from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

DEFAULT_PROJECT_DIR = "novapolis-sim"
DEFAULT_VERIFY_SCRIPT = "res://scripts/verify_sim.gd"


def _resolve_godot_executable(raw_value: str | None) -> Path:
    candidates: list[str] = []
    if raw_value:
        candidates.append(raw_value)
    env_value = os.environ.get("GODOT_BIN", "").strip()
    if env_value:
        candidates.append(env_value)

    for name in ("godot4", "godot"):
        found = shutil.which(name)
        if found:
            candidates.append(found)

    for candidate in candidates:
        candidate_path = Path(candidate).expanduser()
        if candidate_path.exists():
            return candidate_path.resolve()

    raise FileNotFoundError(
        "Could not resolve a Godot executable. Set GODOT_BIN, pass "
        "--godot-bin, or add godot4/godot to PATH."
    )


def _build_command(godot_executable: Path, project_dir: Path, verify_script: str) -> list[str]:
    return [
        str(godot_executable),
        "--headless",
        "--path",
        str(project_dir),
        "-s",
        verify_script,
    ]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run the canonical Godot headless smoke verifier for novapolis-sim"
    )
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parents[1]),
        help="Repository root containing the novapolis-sim project",
    )
    parser.add_argument(
        "--project-dir",
        default=DEFAULT_PROJECT_DIR,
        help="Project directory relative to the repo root",
    )
    parser.add_argument(
        "--verify-script",
        default=DEFAULT_VERIFY_SCRIPT,
        help="Godot script path to execute inside the project",
    )
    parser.add_argument(
        "--godot-bin",
        default="",
        help="Optional explicit path to the Godot executable",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the resolved command without running Godot",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    project_dir = (repo_root / args.project_dir).resolve()
    if not project_dir.exists():
        print(f"[sim-verify] project directory missing: {project_dir}", file=sys.stderr)
        return 2

    try:
        godot_executable = _resolve_godot_executable(args.godot_bin.strip() or None)
    except FileNotFoundError as exc:
        print(f"[sim-verify] {exc}", file=sys.stderr)
        return 2

    command = _build_command(godot_executable, project_dir, args.verify_script)
    print(f"[sim-verify] godot={godot_executable}")
    print(f"[sim-verify] project={project_dir}")
    print(f"[sim-verify] verify_script={args.verify_script}")
    print(f"[sim-verify] command={' '.join(command)}")

    if args.dry_run:
        return 0

    completed = subprocess.run(command, cwd=repo_root, check=False)
    return int(completed.returncode)


if __name__ == "__main__":
    raise SystemExit(main())
