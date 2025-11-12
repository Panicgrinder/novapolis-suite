"""Unified repository check runner producing Markdown and JSON reports."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import platform
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional

try:
    import tomllib  # type: ignore[attr-defined]
except ModuleNotFoundError:  # pragma: no cover
    import tomli as tomllib  # type: ignore[no-redef]


@dataclass
class CheckResult:
    tool: str
    status: str
    exit_code: Optional[int]
    duration_ms: int
    findings_count: int
    details_path: Optional[Path]
    notes: Optional[str] = None


MANDATORY_CHECKS = {
    "markdownlint",
    "frontmatter",
    "ruff",
    "black",
    "pyright",
    "mypy",
    "pytest",
}
OPTIONAL_CHECKS = {"yamllint", "jsonlint", "hadolint"}
LOG_ENCODING = "utf-8"
CHECK_TIMEOUT = None


def resolve_repo_root(script_path: Path) -> Path:
    scripts_dir = script_path.parent
    return scripts_dir.parent.resolve()


def resolve_python(repo_root: Path) -> Path:
    venv_python = repo_root / ".venv" / "Scripts" / "python.exe"
    if venv_python.exists():
        return venv_python.resolve()
    return Path(sys.executable).resolve()


def load_config(repo_root: Path) -> dict[str, int]:
    config = {"coverage_fail_under": 80}
    pyproject = repo_root / "pyproject.toml"
    if pyproject.exists():
        data = tomllib.loads(pyproject.read_text(encoding="utf-8"))
        try:
            coverage_value = (
                data["tool"]["novapolis"]["checks"]["coverage_fail_under"]
            )
        except KeyError:
            coverage_value = None
        if isinstance(coverage_value, (int, float)):
            config["coverage_fail_under"] = int(coverage_value)
    return config


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_log(path: Path, output: str) -> None:
    path.write_text(output, encoding=LOG_ENCODING)


def format_guard_status(guards: dict[str, bool]) -> tuple[str, str]:
    detail = "|".join(f"{name}:{'PASS' if ok else 'FAIL'}" for name, ok in guards.items())
    aggregate = "PASS" if all(guards.values()) else "FAIL"
    return aggregate, detail


def run_command(
    command: Iterable[str],
    cwd: Path,
    log_path: Path,
    timeout: Optional[int] = CHECK_TIMEOUT,
) -> tuple[int, str, int]:
    env = os.environ.copy()
    env.setdefault("PYTHONIOENCODING", LOG_ENCODING)
    start = time.perf_counter()
    completed = subprocess.run(
        list(command),
        cwd=str(cwd),
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding=LOG_ENCODING,
        errors="replace",
        timeout=timeout,
    )
    duration_ms = int((time.perf_counter() - start) * 1000)
    output = completed.stdout or ""
    write_log(log_path, output)
    return completed.returncode, output, duration_ms


def check_tool_available(executable: str) -> Optional[Path]:
    path = shutil.which(executable)
    return Path(path) if path else None


def count_findings(output: str) -> int:
    return sum(1 for line in output.splitlines() if line.strip())


def collect_git_sha(repo_root: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=str(repo_root),
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            encoding=LOG_ENCODING,
            check=False,
        )
    except FileNotFoundError:
        return "n/a"
    value = (result.stdout or "").strip()
    return value or "n/a"


def parse_coverage_percent(xml_path: Path) -> Optional[float]:
    if not xml_path.exists():
        return None
    import xml.etree.ElementTree as ET

    try:
        tree = ET.parse(xml_path)
    except ET.ParseError:
        return None
    root = tree.getroot()
    rate = root.attrib.get("line-rate")
    try:
        return round(float(rate) * 100, 2) if rate is not None else None
    except ValueError:
        return None


def maybe_skip_optional(tool: str, reason: str, log_path: Path) -> CheckResult:
    write_log(log_path, f"SKIP: {reason}\n")
    return CheckResult(
        tool=tool,
        status="SKIP",
        exit_code=None,
        duration_ms=0,
        findings_count=0,
        details_path=log_path,
        notes=reason,
    )


def run_checks(args: argparse.Namespace) -> tuple[list[CheckResult], dict[str, str]]:
    script_path = Path(__file__).resolve()
    repo_root = resolve_repo_root(script_path)
    python_exec = resolve_python(repo_root)
    agent_dir = repo_root / "novapolis_agent"
    tmp_root = repo_root / ".tmp-results"
    report_dir = tmp_root / "reports"
    ensure_directory(report_dir)

    stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    logs_dir = report_dir / f"checks_run_{stamp}"
    ensure_directory(logs_dir)

    config = load_config(repo_root)
    coverage_fail_under = config["coverage_fail_under"]

    guards = {
        "ScriptLocation": script_path.parent == (repo_root / "scripts"),
        "WorkingDir": Path.cwd().resolve() == repo_root,
        "RepoRoot": repo_root.exists(),
    }

    results: list[CheckResult] = []

    def run_or_fail(
        tool: str,
        command: Iterable[str],
        cwd: Path,
        optional: bool = False,
        note: Optional[str] = None,
    ) -> None:
        log_path = logs_dir / f"{tool}.log"
        command_list = list(command)
        try:
            exit_code, output, duration = run_command(command_list, cwd, log_path)
        except FileNotFoundError:
            reason = f"Executable not found: {command_list[0]}"
            if optional:
                results.append(maybe_skip_optional(tool, reason, log_path))
                return
            write_log(log_path, f"FAIL: {reason}\n")
            results.append(
                CheckResult(
                    tool=tool,
                    status="FAIL",
                    exit_code=127,
                    duration_ms=0,
                    findings_count=1,
                    details_path=log_path,
                    notes=reason,
                )
            )
            return
        status = "PASS" if exit_code == 0 else "FAIL"
        findings = count_findings(output) if exit_code != 0 else 0
        results.append(
            CheckResult(
                tool=tool,
                status=status,
                exit_code=exit_code,
                duration_ms=duration,
                findings_count=findings,
                details_path=log_path,
                notes=note,
            )
        )

    npx_executable = check_tool_available("npx")
    markdownlint_config = repo_root / ".markdownlint-cli2.jsonc"
    if npx_executable and markdownlint_config.exists():
        run_or_fail(
            "markdownlint",
            [
                str(npx_executable),
                "--yes",
                "markdownlint-cli2",
                "--config",
                str(markdownlint_config),
                "**/*.md",
            ],
            repo_root,
        )
    else:
        reason = "npx or markdownlint config missing"
        log_path = logs_dir / "markdownlint.log"
        write_log(log_path, f"FAIL: {reason}\n")
        results.append(
            CheckResult(
                tool="markdownlint",
                status="FAIL",
                exit_code=127,
                duration_ms=0,
                findings_count=1,
                details_path=log_path,
                notes=reason,
            )
        )

    frontmatter_script = repo_root / "scripts" / "check_frontmatter.py"
    run_or_fail(
        "frontmatter",
        [str(python_exec), str(frontmatter_script)],
        repo_root,
    )

    run_or_fail(
        "ruff",
        [str(python_exec), "-m", "ruff", "check", """."""],
        repo_root,
    )

    run_or_fail(
        "black",
        [str(python_exec), "-m", "black", "--check", """."""],
        repo_root,
    )

    run_or_fail(
        "pyright",
        ["pyright", "-p", "pyrightconfig.json"],
        agent_dir,
    )

    run_or_fail(
        "mypy",
        [str(python_exec), "-m", "mypy", "--config-file", "mypy.ini", "app", "scripts"],
        agent_dir,
    )

    artifacts_dir = repo_root / "outputs" / "test-artifacts"
    ensure_directory(artifacts_dir)
    coverage_xml = artifacts_dir / "coverage.xml"
    junit_xml = artifacts_dir / "junit.xml"

    pytest_command = [
        str(python_exec),
        "-m",
        "pytest",
        "--cov",
        "--cov-branch",
        "--cov-report=term-missing",
        "--cov-report",
        f"xml:{coverage_xml}",
        "--junitxml",
        str(junit_xml),
        "--cov-config",
        str(agent_dir / ".coveragerc"),
        f"--cov-fail-under={coverage_fail_under}",
    ]
    run_or_fail("pytest", pytest_command, agent_dir)

    yamllint_exec = check_tool_available("yamllint")
    yamllint_config_candidates = [repo_root / ".yamllint", repo_root / ".yamllint.yaml"]
    yamllint_config = next((cfg for cfg in yamllint_config_candidates if cfg.exists()), None)
    if yamllint_exec and yamllint_config:
        run_or_fail(
            "yamllint",
            [str(yamllint_exec), "-c", str(yamllint_config), str(repo_root)],
            repo_root,
            optional=True,
        )
    else:
        reason = "yamllint skipped (tool or config missing)"
        results.append(
            maybe_skip_optional("yamllint", reason, logs_dir / "yamllint.log")
        )

    jsonlint_exec = check_tool_available("jsonlint")
    if jsonlint_exec:
        run_or_fail(
            "jsonlint",
            [str(jsonlint_exec), "-q", str(repo_root)],
            repo_root,
            optional=True,
        )
    else:
        reason = "jsonlint skipped (tool missing)"
        results.append(
            maybe_skip_optional("jsonlint", reason, logs_dir / "jsonlint.log")
        )

    hadolint_exec = check_tool_available("hadolint")
    dockerfile = repo_root / "Dockerfile"
    if hadolint_exec and dockerfile.exists():
        run_or_fail(
            "hadolint",
            [str(hadolint_exec), str(dockerfile)],
            repo_root,
            optional=True,
        )
    else:
        reason = "hadolint skipped (tool or Dockerfile missing)"
        results.append(
            maybe_skip_optional("hadolint", reason, logs_dir / "hadolint.log")
        )

    extra_context = {
        "stamp": stamp,
        "logs_dir": logs_dir,
        "python": python_exec,
        "repo_root": repo_root,
        "coverage_xml": coverage_xml,
        "guards": guards,
        "coverage_fail_under": coverage_fail_under,
        "git_sha": collect_git_sha(repo_root),
    }
    return results, extra_context


def build_summary(
    results: list[CheckResult],
    ctx: dict[str, object],
) -> tuple[dict[str, object], str]:
    repo_root: Path = ctx["repo_root"]  # type: ignore[assignment]
    coverage_xml: Path = ctx["coverage_xml"]  # type: ignore[assignment]
    coverage_percent = parse_coverage_percent(coverage_xml)

    checks_payload = []
    for res in results:
        details = str(res.details_path.relative_to(repo_root)) if res.details_path else None
        checks_payload.append(
            {
                "tool": res.tool,
                "status": res.status,
                "exitcode": res.exit_code,
                "duration_ms": res.duration_ms,
                "findings_count": res.findings_count,
                "details_path": details,
                "notes": res.notes,
            }
        )

    status_map = {res.tool: res.status for res in results}
    mandatory_ok = all(status_map.get(tool) == "PASS" for tool in MANDATORY_CHECKS)
    overall_status = "PASS" if mandatory_ok else "FAIL"
    exit_code = 0 if overall_status == "PASS" else 1

    guard_status, guard_detail = format_guard_status(ctx["guards"])

    metadata = {
        "timestamp": dt.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "python": sys.version.split()[0],
        "runner_python": str(ctx["python"]),
        "os": platform.platform(),
        "repo_root": str(repo_root),
        "git_sha": ctx["git_sha"],
        "script_sha256": hashlib_sha(Path(__file__)),
        "coverage_fail_under": ctx["coverage_fail_under"],
        "coverage_percent": coverage_percent,
        "wrapper_guards": guard_detail,
        "wrapper_guards_status": guard_status,
    }

    summary = {
        "metadata": metadata,
        "checks": checks_payload,
        "overall": {
            "status": overall_status,
            "exitcode": exit_code,
        },
    }

    headline_parts = [f"overall={overall_status}"] + [
        f"{res.tool}={res.status}" for res in results if res.tool in MANDATORY_CHECKS
    ]
    headline = "; ".join(headline_parts)
    return summary, headline


def hashlib_sha(path: Path) -> str:
    data = path.read_bytes()
    import hashlib

    return hashlib.sha256(data).hexdigest()


def write_reports(
    summary: dict[str, object],
    headline: str,
    ctx: dict[str, object],
) -> tuple[Path, Path]:
    repo_root: Path = ctx["repo_root"]  # type: ignore[assignment]
    stamp: str = ctx["stamp"]  # type: ignore[assignment]
    report_dir: Path = repo_root / ".tmp-results" / "reports"
    markdown_path = report_dir / f"checks_report_{stamp}.md"
    summary_path = report_dir / f"checks_report_{stamp}.json"

    json_text = json.dumps(summary, indent=2, ensure_ascii=False)
    summary_path.write_text(json_text, encoding=LOG_ENCODING)

    metadata = summary["metadata"]
    overall = summary["overall"]["status"]
    coverage_percent = summary["metadata"].get("coverage_percent")
    coverage_line = (
        f"Coverage: {coverage_percent:.2f}%" if isinstance(coverage_percent, float) else "Coverage: n/a"
    )

    lines = [
        "---",
        f"stand: {metadata['timestamp']}",
        "update: Konsolidierter Prüf- und Gate-Lauf",
        f"checks: {headline}",
        "---",
        "",
        "Pruefzusammenfassung",
        "====================",
        "",
        f"* Gesamt-Gate: {overall}",
        f"* Wrapper-Guards: {metadata['wrapper_guards_status']} ({metadata['wrapper_guards']})",
        f"* Python: {metadata['python']} ({metadata['runner_python']})",
        f"* OS: {metadata['os']}",
        f"* Git SHA: {metadata['git_sha']}",
        f"* Script SHA256: {metadata['script_sha256']}",
        f"* Coverage fail-under: {metadata['coverage_fail_under']}",
        f"* {coverage_line}",
        f"* JSON-Summary: {summary_path.relative_to(repo_root)}",
        "",
        "Ergebnisse",
        "----------",
        "",
        "```json",
        json_text,
        "```",
    ]
    markdown_path.write_text("\n".join(lines) + "\n", encoding=LOG_ENCODING)
    return markdown_path, summary_path


def build_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run repository checks and generate reports.")
    parser.add_argument(
        "--allow-non-zero",
        action="store_true",
        help="Return exit code 0 even if checks fail (useful for local dry runs).",
    )
    return parser


def main() -> int:
    parser = build_argparser()
    args = parser.parse_args()
    results, ctx = run_checks(args)
    summary, headline = build_summary(results, ctx)
    markdown_path, json_path = write_reports(summary, headline, ctx)
    print(f"Markdown report: {markdown_path}")
    print(f"JSON summary: {json_path}")
    exit_code = summary["overall"]["exitcode"]  # type: ignore[index]
    if args.allow_non_zero:
        return 0
    return int(exit_code)


if __name__ == "__main__":
    sys.exit(main())
