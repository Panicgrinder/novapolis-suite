"""Validate Novapolis Dev logs policy for `novapolis-dev/logs/`.

Policy (enforced):
- No `*.tmp.md` files in active logs path.
- Required policy files must exist: logs-policy.md, log-template.md.
"""

from __future__ import annotations

import argparse
from pathlib import Path

LOGS_DIR = Path("novapolis-dev/logs")
REQUIRED_FILES = ("logs-policy.md", "log-template.md")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check logs policy for novapolis-dev/logs")
    parser.add_argument("--repo-root", default=".", help="Repository root path")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    logs_dir = (repo_root / LOGS_DIR).resolve()

    if not logs_dir.exists() or not logs_dir.is_dir():
        print(f"FAIL: missing logs directory {LOGS_DIR.as_posix()}")
        return 1

    findings: list[str] = []

    for required in REQUIRED_FILES:
        required_path = logs_dir / required
        if not required_path.exists() or not required_path.is_file():
            findings.append(f"missing_required|{(LOGS_DIR / required).as_posix()}")

    tmp_logs = sorted(path for path in logs_dir.glob("*.tmp.md") if path.is_file())
    for path in tmp_logs:
        rel = path.relative_to(repo_root).as_posix()
        findings.append(f"tmp_log_forbidden|{rel}")

    print(f"tmp_logs={len(tmp_logs)}")
    print(f"findings={len(findings)}")

    if findings:
        for line in findings:
            print(f"FAIL|{line}")
        return 1

    print("PASS: logs policy satisfied for novapolis-dev/logs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
