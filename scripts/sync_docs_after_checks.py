#!/usr/bin/env python3
"""Synchronize changed Root/Dev docs after a validated checks report."""

from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime
from pathlib import Path

try:
    from scripts import check_frontmatter as frontmatter_mod
    from scripts import check_todo_index_sync as todo_sync_mod
    from scripts import run_checks_and_report as checks_runner
except ModuleNotFoundError:  # pragma: no cover
    import check_frontmatter as frontmatter_mod  # type: ignore[no-redef]
    import check_todo_index_sync as todo_sync_mod  # type: ignore[no-redef]
    import run_checks_and_report as checks_runner  # type: ignore[no-redef]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".", help="Repository root path")
    parser.add_argument(
        "--report",
        default="latest",
        help="Markdown/JSON report path from run_checks_and_report.py or 'latest'",
    )
    parser.add_argument(
        "--files",
        nargs="*",
        default=None,
        help="Explicit markdown files to sync; defaults to changed markdown files",
    )
    parser.add_argument(
        "--skip-snapshot-lock",
        action="store_true",
        help="Do not refresh .snapshot.now before syncing frontmatter",
    )
    parser.add_argument(
        "--sync-todo-index",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Run check_todo_index_sync.py --write-index-meta when active TODO boards are involved",
    )
    parser.add_argument(
        "--validate-frontmatter",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Validate touched markdown files with check_frontmatter.py after sync",
    )
    parser.add_argument(
        "--allow-non-pass",
        action="store_true",
        help="Allow syncing even if the selected report headline is not overall=PASS",
    )
    return parser.parse_args(argv)


def find_latest_report(report_dir: Path) -> Path:
    candidates = sorted(report_dir.glob("checks_report_*.md"))
    if not candidates:
        raise FileNotFoundError("no checks_report_*.md files found")
    return candidates[-1]


def extract_headline_from_markdown(report_path: Path) -> str:
    text = report_path.read_text(encoding="utf-8")
    fm_lines, _body_lines, _original_lines = checks_runner.split_frontmatter(text)
    for line in fm_lines[1:-1]:
        stripped = line.strip()
        if stripped.lower().startswith("checks:"):
            return stripped.split(":", 1)[1].strip()
    raise ValueError(f"missing checks frontmatter in {report_path}")


def rebuild_headline_from_summary(summary_path: Path) -> str:
    payload = json.loads(summary_path.read_text(encoding="utf-8"))
    status_map = {
        str(item["tool"]): str(item["status"])
        for item in payload.get("checks", [])
        if isinstance(item, dict) and item.get("tool")
    }
    parts = [f"overall={payload['overall']['status']}"]
    for tool in [
        "markdownlint",
        "frontmatter",
        "path-portability",
        "namingpolicy",
        "todo-index-sync",
        "doc-freshness",
        "logs-policy",
        "sim-assets",
        "ruff",
        "black",
        "pytest",
        "pyright",
        "mypy",
    ]:
        status = status_map.get(tool)
        if status:
            parts.append(f"{tool}={status}")
    return "; ".join(parts)


def resolve_report(repo_root: Path, report_arg: str) -> tuple[Path, str, str]:
    if report_arg == "latest":
        report_path = find_latest_report(repo_root / ".tmp" / "results" / "reports")
    else:
        candidate = Path(report_arg)
        report_path = candidate if candidate.is_absolute() else (repo_root / candidate)
    report_path = report_path.resolve()

    if report_path.suffix.lower() == ".json":
        markdown_path = report_path.with_suffix(".md")
        headline = (
            extract_headline_from_markdown(markdown_path)
            if markdown_path.exists()
            else rebuild_headline_from_summary(report_path)
        )
        report_ref = markdown_path if markdown_path.exists() else report_path
        return report_ref, headline, report_ref.relative_to(repo_root).as_posix()

    if report_path.suffix.lower() != ".md":
        raise ValueError(f"unsupported report format: {report_path}")

    headline = extract_headline_from_markdown(report_path)
    return report_path, headline, report_path.relative_to(repo_root).as_posix()


def read_snapshot_value(repo_root: Path) -> str:
    snapshot_path = repo_root / ".snapshot.now"
    if snapshot_path.exists():
        return snapshot_path.read_text(encoding="utf-8").strip()
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def run_python_subprocess(
    python_exec: Path, script_path: Path, *args: str, cwd: Path
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [str(python_exec), str(script_path), *args],
        cwd=str(cwd),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )


def refresh_snapshot_lock(repo_root: Path, python_exec: Path) -> str:
    script_path = repo_root / "scripts" / "snapshot_write_lock.py"
    completed = run_python_subprocess(python_exec, script_path, cwd=repo_root)
    if completed.returncode != 0:
        message = (completed.stderr or completed.stdout or "snapshot_write_lock failed").strip()
        raise RuntimeError(message)
    return read_snapshot_value(repo_root)


def collect_markdown_targets(repo_root: Path, file_args: list[str] | None = None) -> list[Path]:
    if file_args:
        candidates = []
        for raw in file_args:
            candidate = Path(raw)
            path = candidate if candidate.is_absolute() else (repo_root / candidate)
            if path.exists() and path.is_file() and path.suffix.lower() == ".md":
                candidates.append(path.resolve())
        return sorted(dict.fromkeys(candidates))

    changed = checks_runner.git_changed_files(repo_root)
    candidates = []
    for rel in changed:
        if not rel.lower().endswith(".md"):
            continue
        path = (repo_root / rel).resolve()
        if path.exists() and path.is_file():
            candidates.append(path)
    return sorted(dict.fromkeys(candidates))


def sync_markdown_paths(paths: list[Path], stand_value: str, checks_value: str) -> list[Path]:
    updated: list[Path] = []
    for path in paths:
        try:
            raw_text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        fm_lines, body_lines, original_lines = checks_runner.split_frontmatter(raw_text)
        if not fm_lines:
            continue

        has_stand = any(line.strip().lower().startswith("stand:") for line in fm_lines[1:-1])
        has_checks = any(line.strip().lower().startswith("checks:") for line in fm_lines[1:-1])
        if not (has_stand and has_checks):
            continue

        new_fm: list[str] = []
        for line in fm_lines:
            stripped = line.strip().lower()
            if stripped.startswith("stand:"):
                new_fm.append(f"stand: {stand_value}")
                continue
            if stripped.startswith("checks:"):
                new_fm.append(f"checks: {checks_value}")
                continue
            new_fm.append(line)

        new_lines = new_fm + body_lines
        if new_lines == original_lines:
            continue
        path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
        updated.append(path)
    return updated


def should_sync_todo_index(paths: list[Path], repo_root: Path) -> bool:
    active_todos = {(repo_root / rel).resolve() for rel in todo_sync_mod.ACTIVE_TODO_FILES}
    return any(path.resolve() in active_todos for path in paths)


def validate_frontmatter(paths: list[Path]) -> list[str]:
    issues: list[str] = []
    for path in paths:
        for issue in frontmatter_mod.validate_frontmatter(path, touch=False):
            issues.append(f"{path}: {issue}")
    return issues


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    repo_root = Path(args.repo_root).resolve()
    python_exec = checks_runner.resolve_python(repo_root)

    _report_path, headline, report_ref = resolve_report(repo_root, args.report)
    if not args.allow_non_pass and "overall=PASS" not in headline:
        print(f"FAIL: report is not green: {headline}")
        return 1

    stand_value = (
        read_snapshot_value(repo_root)
        if args.skip_snapshot_lock
        else refresh_snapshot_lock(repo_root, python_exec)
    )
    checks_value = (
        f"scripts/run_checks_and_report.py {headline}; report={report_ref}; "
        f"snapshot-lock PASS ({stand_value})"
    )

    targets = collect_markdown_targets(repo_root, args.files)
    updated_files = sync_markdown_paths(targets, stand_value, checks_value)

    validation_targets = {path.resolve() for path in targets}
    validation_targets.update(path.resolve() for path in updated_files)

    if args.sync_todo_index and should_sync_todo_index(targets, repo_root):
        todo_sync_path = repo_root / "scripts" / "check_todo_index_sync.py"
        completed = run_python_subprocess(
            python_exec,
            todo_sync_path,
            "--repo-root",
            str(repo_root),
            "--write-index-meta",
            cwd=repo_root,
        )
        stdout = (completed.stdout or "").strip()
        stderr = (completed.stderr or "").strip()
        if stdout:
            print(stdout)
        if stderr:
            print(stderr)
        if completed.returncode != 0:
            return completed.returncode

        todo_index_path = (repo_root / todo_sync_mod.TODO_INDEX_FILE).resolve()
        sync_markdown_paths([todo_index_path], stand_value, checks_value)
        validation_targets.add(todo_index_path)

    if args.validate_frontmatter:
        issues = validate_frontmatter(sorted(validation_targets))
        if issues:
            for issue in issues:
                print(issue)
            return 1

    print(f"report={report_ref}")
    print(f"stand={stand_value}")
    print(f"synced_files={len(updated_files)}")
    print("PASS: docs sync completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
