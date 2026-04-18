#!/usr/bin/env python

from __future__ import annotations

import argparse
import importlib
import json
import os
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

GM_RESULTS_GLOB = "results_*_gm_session*.jsonl"
GM_CHECKS = "must_include,keywords_any,keywords_at_least,not_include,regex,rpg_style"
GM_PREFLIGHT_TIMEOUT_SEC = 5.0
REFERENCE_SPECS = (
    "novapolis_agent/eval/config/text_rpg_reference_session.v1.json",
    "novapolis_agent/eval/config/text_rpg_reference_session_handover_slot31_40.v1.json",
)


@dataclass(frozen=True)
class GateStep:
    name: str
    command: tuple[str, ...]
    cwd: Path
    log_path: Path
    metadata: dict[str, str] = field(default_factory=dict)


@dataclass
class StepResult:
    name: str
    status: str
    exit_code: int
    duration_ms: int
    command: list[str]
    cwd: str
    log_path: str
    metadata: dict[str, str] = field(default_factory=dict)


def _step_result(
    *,
    name: str,
    status: str,
    exit_code: int,
    duration_ms: int,
    repo_root: Path,
    cwd: Path,
    log_path: Path,
    command: list[str] | None = None,
    metadata: dict[str, str] | None = None,
) -> StepResult:
    return StepResult(
        name=name,
        status=status,
        exit_code=exit_code,
        duration_ms=duration_ms,
        command=command or [],
        cwd=_relative(cwd, repo_root),
        log_path=_relative(log_path, repo_root),
        metadata=dict(metadata or {}),
    )


def _relative(path: Path, repo_root: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def _reports_dir(repo_root: Path) -> Path:
    reports_dir = repo_root / ".tmp" / "results" / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    return reports_dir


def build_base_gate_steps(repo_root: Path, python_exec: Path, timestamp: str) -> list[GateStep]:
    reports_dir = _reports_dir(repo_root)
    reference_json = f".tmp/results/reports/text_rpg_reference_session_{timestamp}.json"
    reference_md = f".tmp/results/reports/text_rpg_reference_session_{timestamp}.md"
    gm_dataset = (
        repo_root / "novapolis_agent" / "eval" / "datasets" / "rpg" / "rpg_gm_session_core.v1.jsonl"
    )
    reference_runner = (
        repo_root / "novapolis_agent" / "scripts" / "run_text_rpg_reference_session.py"
    )
    reference_command = [
        str(python_exec),
        str(reference_runner),
        "--repo-root",
        str(repo_root),
    ]
    for spec_path in REFERENCE_SPECS:
        reference_command.extend(("--spec", spec_path))
    reference_command.extend(("--report-json", reference_json, "--report-md", reference_md))

    return [
        GateStep(
            name="checks_full",
            command=(str(python_exec), str(repo_root / "scripts" / "run_checks_and_report.py")),
            cwd=repo_root,
            log_path=reports_dir / f"text_rpg_product_gate_{timestamp}_checks_full.log",
        ),
        GateStep(
            name="pytest_api_streaming",
            command=(str(python_exec), "-m", "pytest", "-q", "-m", "api or streaming"),
            cwd=repo_root / "novapolis_agent",
            log_path=reports_dir / f"text_rpg_product_gate_{timestamp}_pytest_api_streaming.log",
        ),
        GateStep(
            name="reference_session",
            command=tuple(reference_command),
            cwd=repo_root,
            log_path=reports_dir / f"text_rpg_product_gate_{timestamp}_reference_session.log",
            metadata={
                "report_json": reference_json,
                "report_md": reference_md,
                "reference_specs": ",".join(REFERENCE_SPECS),
            },
        ),
        GateStep(
            name="sim_epoch_assets",
            command=(
                str(python_exec),
                str(repo_root / "scripts" / "check_sim_epoch_assets.py"),
                "--repo-root",
                str(repo_root),
                "--allow-empty",
                "--check-slot-consistency",
            ),
            cwd=repo_root,
            log_path=reports_dir / f"text_rpg_product_gate_{timestamp}_sim_epoch_assets.log",
        ),
        GateStep(
            name="gm_session_eval",
            command=(
                str(python_exec),
                "-m",
                "scripts.agent.run_eval",
                "--asgi",
                "--profile",
                "unrestricted",
                "--limit",
                "12",
                "--quiet",
                "--tag",
                "gm_session",
                "--checks",
                GM_CHECKS,
                "--packages",
                str(gm_dataset),
            ),
            cwd=repo_root,
            log_path=reports_dir / f"text_rpg_product_gate_{timestamp}_gm_session_eval.log",
        ),
    ]


def build_gm_summary_step(
    repo_root: Path,
    python_exec: Path,
    timestamp: str,
    gm_results_file: Path,
) -> GateStep:
    reports_dir = _reports_dir(repo_root)
    report_json = f".tmp/results/reports/gm_session_kpi_summary_{timestamp}.json"
    report_md = f".tmp/results/reports/gm_session_kpi_summary_{timestamp}.md"
    return GateStep(
        name="gm_session_summary",
        command=(
            str(python_exec),
            str(repo_root / "novapolis_agent" / "scripts" / "summarize_gm_eval_kpis.py"),
            "--repo-root",
            str(repo_root),
            "--results-file",
            _relative(gm_results_file, repo_root),
            "--report-json",
            report_json,
            "--report-md",
            report_md,
        ),
        cwd=repo_root,
        log_path=reports_dir / f"text_rpg_product_gate_{timestamp}_gm_session_summary.log",
        metadata={
            "results_file": _relative(gm_results_file, repo_root),
            "report_json": report_json,
            "report_md": report_md,
        },
    )


def load_runtime_target() -> tuple[str, str]:
    repo_root = Path(__file__).resolve().parents[1]
    module_root = repo_root / "novapolis_agent"
    for candidate in (repo_root, module_root):
        candidate_text = str(candidate)
        if candidate_text not in sys.path:
            sys.path.insert(0, candidate_text)

    for module_name in ("app.core.settings", "novapolis_agent.app.core.settings"):
        module = sys.modules.get(module_name)
        if module is None:
            try:
                module = importlib.import_module(module_name)
            except Exception:
                continue
        get_settings = getattr(module, "get_settings", None)
        if callable(get_settings):
            settings = get_settings()
            host = getattr(settings, "OLLAMA_HOST", None)
            model = getattr(settings, "MODEL_NAME", None)
            if host is not None and model is not None:
                return str(host), str(model)
        settings_obj = getattr(module, "settings", None)
        if settings_obj is not None:
            host = getattr(settings_obj, "OLLAMA_HOST", None)
            model = getattr(settings_obj, "MODEL_NAME", None)
            if host is not None and model is not None:
                return str(host), str(model)
    raise RuntimeError("could not resolve settings module for runtime target")


def run_gm_runtime_preflight(repo_root: Path, timestamp: str) -> StepResult:
    reports_dir = _reports_dir(repo_root)
    log_path = reports_dir / f"text_rpg_product_gate_{timestamp}_gm_runtime_preflight.log"
    started = time.perf_counter()
    host, model = load_runtime_target()
    parsed = urllib.parse.urlparse(host)
    scheme = parsed.scheme or "http"
    hostname = parsed.hostname or "localhost"
    port = parsed.port or (443 if scheme == "https" else 80)
    tags_url = f"{host.rstrip('/')}/api/tags"
    metadata = {
        "host": host,
        "model": model,
        "tags_url": tags_url,
    }
    log_lines = [f"host={host}", f"model={model}", f"tags_url={tags_url}"]

    try:
        with socket.create_connection((hostname, port), timeout=GM_PREFLIGHT_TIMEOUT_SEC):
            log_lines.append(f"tcp_connect=PASS host={hostname} port={port}")
    except OSError as exc:
        metadata["error_kind"] = "runtime_unreachable"
        metadata["error_detail"] = str(exc)
        log_lines.append(f"tcp_connect=FAIL host={hostname} port={port} detail={exc}")
        log_path.write_text("\n".join(log_lines) + "\n", encoding="utf-8")
        return _step_result(
            name="gm_runtime_preflight",
            status="FAIL",
            exit_code=1,
            duration_ms=int((time.perf_counter() - started) * 1000),
            repo_root=repo_root,
            cwd=repo_root,
            log_path=log_path,
            metadata=metadata,
        )

    try:
        request = urllib.request.Request(tags_url, method="GET")
        with urllib.request.urlopen(request, timeout=GM_PREFLIGHT_TIMEOUT_SEC) as response:
            raw_payload = response.read().decode("utf-8", errors="replace")
            status_code = getattr(response, "status", 200)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        metadata["error_kind"] = "tags_endpoint_http_error"
        metadata["error_detail"] = f"http_{exc.code}"
        log_lines.append(f"tags_request=FAIL status={exc.code}")
        if body:
            log_lines.append(body)
        log_path.write_text("\n".join(log_lines) + "\n", encoding="utf-8")
        return _step_result(
            name="gm_runtime_preflight",
            status="FAIL",
            exit_code=1,
            duration_ms=int((time.perf_counter() - started) * 1000),
            repo_root=repo_root,
            cwd=repo_root,
            log_path=log_path,
            metadata=metadata,
        )
    except urllib.error.URLError as exc:
        metadata["error_kind"] = "runtime_unreachable"
        metadata["error_detail"] = str(exc.reason)
        log_lines.append(f"tags_request=FAIL detail={exc.reason}")
        log_path.write_text("\n".join(log_lines) + "\n", encoding="utf-8")
        return _step_result(
            name="gm_runtime_preflight",
            status="FAIL",
            exit_code=1,
            duration_ms=int((time.perf_counter() - started) * 1000),
            repo_root=repo_root,
            cwd=repo_root,
            log_path=log_path,
            metadata=metadata,
        )

    payload = json.loads(raw_payload)
    models = payload.get("models") if isinstance(payload, dict) else None
    available_models = sorted(
        {
            str(entry.get("name", "")).strip()
            for entry in models or []
            if isinstance(entry, dict) and str(entry.get("name", "")).strip()
        }
    )
    metadata["available_models"] = ",".join(available_models)
    metadata["tags_status"] = str(status_code)
    log_lines.append(f"tags_request=PASS status={status_code}")
    log_lines.append(f"available_models={','.join(available_models) or '<none>'}")
    if model not in available_models:
        metadata["error_kind"] = "model_missing"
        metadata["error_detail"] = model
        log_lines.append(f"model_check=FAIL missing={model}")
        log_path.write_text("\n".join(log_lines) + "\n", encoding="utf-8")
        return _step_result(
            name="gm_runtime_preflight",
            status="FAIL",
            exit_code=1,
            duration_ms=int((time.perf_counter() - started) * 1000),
            repo_root=repo_root,
            cwd=repo_root,
            log_path=log_path,
            metadata=metadata,
        )

    log_lines.append(f"model_check=PASS model={model}")
    log_path.write_text("\n".join(log_lines) + "\n", encoding="utf-8")
    return _step_result(
        name="gm_runtime_preflight",
        status="PASS",
        exit_code=0,
        duration_ms=int((time.perf_counter() - started) * 1000),
        repo_root=repo_root,
        cwd=repo_root,
        log_path=log_path,
        metadata=metadata,
    )


def list_gm_result_files(results_dir: Path) -> set[Path]:
    return {path.resolve() for path in results_dir.glob(GM_RESULTS_GLOB) if path.is_file()}


def _load_jsonl_records(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        parsed = json.loads(line)
        if isinstance(parsed, dict):
            records.append(parsed)
    return records


def classify_gm_eval_failures(gm_results_file: Path) -> tuple[list[str], dict[str, str]]:
    records = _load_jsonl_records(gm_results_file)
    counts: dict[str, int] = {}
    details: list[str] = []

    for record in records:
        if record.get("_meta"):
            continue
        slug = str(record.get("slug") or record.get("item_id") or "unknown")
        response_text = str(record.get("response") or "")
        error_text = str(record.get("error") or "")
        text = f"{response_text}\n{error_text}"
        error_kind: str | None = None
        if "All connection attempts failed" in text:
            error_kind = "runtime_unreachable"
        elif "500 Internal Server Error" in text and "localhost:11434/api/chat" in text:
            error_kind = "ollama_http_500"
        elif "504 Gateway Timeout" in text and "http://asgi/chat" in text:
            error_kind = "gm_timeout_504"

        if error_kind is None:
            continue

        counts[error_kind] = counts.get(error_kind, 0) + 1
        details.append(f"{error_kind}:{slug}")

    metadata = {
        "failure_summary": (
            ", ".join(f"{key}={counts[key]}" for key in sorted(counts)) if counts else "none"
        ),
        "failure_examples": "; ".join(details[:4]) if details else "none",
    }
    errors = [f"gm_session_eval classified: {key} ({counts[key]})" for key in sorted(counts)]
    return errors, metadata


def load_summary_severity(report_json: Path) -> str | None:
    if not report_json.exists():
        return None
    payload = json.loads(report_json.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        return None
    summary = payload.get("summary")
    if not isinstance(summary, dict):
        return None
    severity = summary.get("severity")
    if not isinstance(severity, str):
        return None
    return severity.strip() or None


def pick_newest_gm_result(before: set[Path], after: set[Path]) -> Path | None:
    candidates = sorted(after - before, key=lambda path: path.stat().st_mtime, reverse=True)
    if candidates:
        return candidates[0]
    if not after:
        return None
    return max(after, key=lambda path: path.stat().st_mtime)


def run_step(step: GateStep, repo_root: Path) -> StepResult:
    step.log_path.parent.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()
    env = dict(os.environ)
    env.setdefault("PYTHONIOENCODING", "utf-8")
    env.setdefault("PYTHONUTF8", "1")
    completed = subprocess.run(
        list(step.command),
        cwd=str(step.cwd),
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    duration_ms = int((time.perf_counter() - started) * 1000)
    step.log_path.write_text(completed.stdout or "", encoding="utf-8")
    return _step_result(
        name=step.name,
        status="PASS" if completed.returncode == 0 else "FAIL",
        exit_code=completed.returncode,
        duration_ms=duration_ms,
        repo_root=repo_root,
        cwd=step.cwd,
        log_path=step.log_path,
        command=list(step.command),
        metadata=step.metadata,
    )


def _build_markdown(report: dict[str, Any]) -> str:
    lines = ["# Text-RPG Product Gate v1", ""]
    lines.append(f"- Status: {report['status']}")
    lines.append(f"- Timestamp: {report['timestamp']}")
    if report.get("gm_results_file"):
        lines.append(f"- GM Results: {report['gm_results_file']}")
    if report.get("gm_runtime_target"):
        lines.append(f"- GM Runtime Target: {report['gm_runtime_target']}")
    lines.append("")
    diagnosis = report.get("gm_diagnosis")
    if isinstance(diagnosis, dict) and diagnosis:
        lines.append("## GM Diagnosis")
        if diagnosis.get("phase"):
            lines.append(f"- Phase: {diagnosis['phase']}")
        if diagnosis.get("classification"):
            lines.append(f"- Classification: {diagnosis['classification']}")
        if diagnosis.get("detail"):
            lines.append(f"- Detail: {diagnosis['detail']}")
        if diagnosis.get("examples"):
            lines.append(f"- Examples: {diagnosis['examples']}")
        if diagnosis.get("hint"):
            lines.append(f"- Next step: {diagnosis['hint']}")
        lines.append("")
    lines.append("## Steps")
    for step in report["steps"]:
        summary = (
            f"- {step['name']}: {step['status']} "
            f"(exit={step['exit_code']}, duration_ms={step['duration_ms']}, "
            f"log={step['log_path']})"
        )
        lines.append(summary)
        for key, value in sorted(step.get("metadata", {}).items()):
            lines.append(f"  {key}: {value}")
    lines.append("")
    lines.append("## Errors")
    if report["errors"]:
        for entry in report["errors"]:
            lines.append(f"- {entry}")
    else:
        lines.append("- none")
    lines.append("")
    return "\n".join(lines)


def _gm_preflight_hint(error_kind: str, metadata: dict[str, str]) -> str:
    host = metadata.get("host", "<unbekannt>")
    model = metadata.get("model", "<unbekannt>")
    if error_kind == "runtime_unreachable":
        return (
            f"Lokale Runtime zuerst separat pruefen: Task 'Checks: gm runtime preflight' "
            f"oder --gm-preflight-only gegen {host}."
        )
    if error_kind == "model_missing":
        return (
            f"Runtime antwortet, aber Modell fehlt: {model}. Modell in Ollama verfuegbar machen "
            "und erst danach das Gesamt-Gate erneut fahren."
        )
    if error_kind == "tags_endpoint_http_error":
        return (
            f"Lokale Runtime ist erreichbar, aber /api/tags antwortet fehlerhaft auf {host}. "
            "Runtime-Logs pruefen, bevor das teure gm_session-Eval erneut laeuft."
        )
    return "Vorpruefung fehlgeschlagen; zuerst den gm-Preflight isoliert laufen lassen und den Log pruefen."


def build_gm_diagnosis(step_results: list[StepResult]) -> dict[str, str]:
    diagnosis: dict[str, str] = {
        "phase": "none",
        "classification": "none",
        "hint": "Keine gm-spezifische Diagnose vorhanden.",
    }
    preflight = next((step for step in step_results if step.name == "gm_runtime_preflight"), None)
    gm_eval = next((step for step in step_results if step.name == "gm_session_eval"), None)
    summary = next((step for step in step_results if step.name == "gm_session_summary"), None)

    if preflight is None:
        return diagnosis

    if preflight.metadata.get("host"):
        diagnosis["runtime_target"] = preflight.metadata["host"]
    if preflight.metadata.get("model"):
        diagnosis["runtime_model"] = preflight.metadata["model"]

    if preflight.exit_code != 0:
        error_kind = preflight.metadata.get("error_kind", "gm_preflight_failed")
        diagnosis.update(
            {
                "phase": "preflight",
                "classification": error_kind,
                "detail": preflight.metadata.get("error_detail", ""),
                "hint": _gm_preflight_hint(error_kind, preflight.metadata),
            }
        )
        return diagnosis

    if gm_eval is None:
        diagnosis.update(
            {
                "phase": "preflight",
                "classification": "ready",
                "hint": "Vorpruefung ist gruen; jetzt kann das vollstaendige gm_session-Gate laufen.",
            }
        )
        return diagnosis

    failure_summary = gm_eval.metadata.get("failure_summary", "none")
    if failure_summary != "none":
        diagnosis.update(
            {
                "phase": "eval",
                "classification": "eval_runtime_or_execution_failures",
                "detail": failure_summary,
                "examples": gm_eval.metadata.get("failure_examples", "none"),
                "hint": (
                    "Vorpruefung war gruen; der Fail trat erst waehrend gm_session_eval auf. "
                    "Results-Datei, KPI-Summary und Eval-Log gemeinsam triagieren."
                ),
            }
        )
        return diagnosis

    if gm_eval.exit_code != 0:
        diagnosis.update(
            {
                "phase": "eval",
                "classification": "gm_session_eval_failed_without_result_classification",
                "hint": "gm_session_eval ist fehlgeschlagen, ohne klassifizierbare Resultatdatei zu liefern; Eval-Log direkt pruefen.",
            }
        )
        return diagnosis

    if summary is None:
        diagnosis.update(
            {
                "phase": "summary",
                "classification": "summary_missing",
                "hint": "gm_session_eval ist gruen, aber die KPI-Summary fehlt; Reporter-Schritt pruefen.",
            }
        )
        return diagnosis

    if summary.exit_code != 0:
        diagnosis.update(
            {
                "phase": "summary",
                "classification": "summary_step_failed",
                "hint": "gm_session_eval lieferte Resultate, aber der KPI-Reporter ist fehlgeschlagen.",
            }
        )
        return diagnosis

    severity = summary.metadata.get("severity", "")
    if severity == "blocker":
        diagnosis.update(
            {
                "phase": "summary",
                "classification": "summary_blocker",
                "detail": severity,
                "hint": (
                    "Lokale Runtime und Modell waren erreichbar; der Rest liegt jetzt in inhaltlichen gm_session-Checks, "
                    "nicht in der Runtime-Vorpruefung."
                ),
            }
        )
        return diagnosis
    if severity:
        diagnosis.update(
            {
                "phase": "summary",
                "classification": f"summary_{severity}",
                "detail": severity,
                "hint": "gm_session-Eval ist ausgewertet; Triage jetzt ueber KPI-Summary und betroffene Faelle fortsetzen.",
            }
        )
        return diagnosis

    diagnosis.update(
        {
            "phase": "summary",
            "classification": "summary_missing_severity",
            "hint": "gm_session-Eval ist durchgelaufen, aber die KPI-Summary liefert keine Severity.",
        }
    )
    return diagnosis


def run_gm_preflight_only(repo_root: Path, timestamp: str) -> dict[str, Any]:
    preflight_result = run_gm_runtime_preflight(repo_root, timestamp)
    errors: list[str] = []
    if preflight_result.exit_code != 0:
        error_kind = preflight_result.metadata.get("error_kind", "gm_preflight_failed")
        errors.append(f"gm_runtime_preflight classified: {error_kind}")

    step_results = [preflight_result]
    return {
        "status": "PASS" if not errors and preflight_result.exit_code == 0 else "FAIL",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "gm_results_file": None,
        "gm_runtime_target": preflight_result.metadata.get("host"),
        "steps": [
            {
                "name": step.name,
                "status": step.status,
                "exit_code": step.exit_code,
                "duration_ms": step.duration_ms,
                "command": step.command,
                "cwd": step.cwd,
                "log_path": step.log_path,
                "metadata": step.metadata,
            }
            for step in step_results
        ],
        "gm_diagnosis": build_gm_diagnosis(step_results),
        "errors": errors,
    }


def run_product_gate(
    repo_root: Path,
    python_exec: Path,
    timestamp: str,
    continue_on_fail: bool,
) -> dict[str, Any]:
    steps = build_base_gate_steps(repo_root, python_exec, timestamp)
    results_dir = repo_root / "novapolis_agent" / "eval" / "results"
    step_results: list[StepResult] = []
    errors: list[str] = []
    gm_results_file: Path | None = None
    runtime_target: str | None = None

    for step in steps:
        if step.name == "gm_session_eval":
            preflight_result = run_gm_runtime_preflight(repo_root, timestamp)
            step_results.append(preflight_result)
            runtime_target = preflight_result.metadata.get("host")
            if preflight_result.exit_code != 0:
                error_kind = preflight_result.metadata.get("error_kind", "gm_preflight_failed")
                if error_kind == "runtime_unreachable":
                    errors.append("gm_runtime_preflight classified: runtime_unreachable")
                elif error_kind == "model_missing":
                    errors.append("gm_runtime_preflight classified: model_missing")
                else:
                    errors.append(f"gm_runtime_preflight classified: {error_kind}")
                if not continue_on_fail:
                    break

        gm_before = list_gm_result_files(results_dir) if step.name == "gm_session_eval" else set()
        result = run_step(step, repo_root)
        step_results.append(result)

        if step.name == "gm_session_eval":
            gm_after = list_gm_result_files(results_dir)
            gm_results_file = pick_newest_gm_result(gm_before, gm_after)
            if gm_results_file is None:
                errors.append("gm_session eval did not produce a detectable results file")
            else:
                result.metadata["results_file"] = _relative(gm_results_file, repo_root)
                classified_errors, classified_metadata = classify_gm_eval_failures(gm_results_file)
                result.metadata.update(classified_metadata)
                errors.extend(classified_errors)

                summary_step = build_gm_summary_step(
                    repo_root,
                    python_exec,
                    timestamp,
                    gm_results_file,
                )
                summary_result = run_step(summary_step, repo_root)
                step_results.append(summary_result)
                if summary_result.exit_code != 0:
                    errors.append("gm_session summary step failed")
                    if not continue_on_fail:
                        break
                else:
                    summary_report_json = repo_root / summary_step.metadata["report_json"]
                    severity = load_summary_severity(summary_report_json)
                    if severity:
                        summary_result.metadata["severity"] = severity
                    if severity == "blocker":
                        errors.append("gm_session summary classified: blocker")
                        if not continue_on_fail:
                            break

        if result.exit_code != 0:
            errors.append(f"step failed: {step.name}")
            if not continue_on_fail:
                break

    status = "PASS"
    if errors or any(step.exit_code != 0 for step in step_results):
        status = "FAIL"

    return {
        "status": status,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "gm_results_file": _relative(gm_results_file, repo_root) if gm_results_file else None,
        "gm_runtime_target": runtime_target,
        "steps": [
            {
                "name": step.name,
                "status": step.status,
                "exit_code": step.exit_code,
                "duration_ms": step.duration_ms,
                "command": step.command,
                "cwd": step.cwd,
                "log_path": step.log_path,
                "metadata": step.metadata,
            }
            for step in step_results
        ],
        "gm_diagnosis": build_gm_diagnosis(step_results),
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the canonical Text-RPG Product Gate v1")
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parents[1]),
        help="Repository root",
    )
    parser.add_argument(
        "--report-json",
        default="",
        help="Relative JSON report output path",
    )
    parser.add_argument(
        "--report-md",
        default="",
        help="Relative Markdown report output path",
    )
    parser.add_argument(
        "--continue-on-fail",
        action="store_true",
        help="Continue after failing steps instead of stopping at the first failure",
    )
    parser.add_argument(
        "--gm-preflight-only",
        action="store_true",
        help="Run only the lightweight gm runtime preflight instead of the full product gate",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    python_exec = Path(sys.executable).resolve()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    reports_dir = _reports_dir(repo_root)
    report_json = (
        (repo_root / args.report_json).resolve()
        if args.report_json
        else reports_dir / f"text_rpg_product_gate_{timestamp}.json"
    )
    report_md = (
        (repo_root / args.report_md).resolve()
        if args.report_md
        else reports_dir / f"text_rpg_product_gate_{timestamp}.md"
    )

    if args.gm_preflight_only:
        report = run_gm_preflight_only(repo_root, timestamp)
    else:
        report = run_product_gate(repo_root, python_exec, timestamp, args.continue_on_fail)
    report_json.parent.mkdir(parents=True, exist_ok=True)
    report_md.parent.mkdir(parents=True, exist_ok=True)
    report_json.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    report_md.write_text(_build_markdown(report), encoding="utf-8", newline="\n")

    print(f"[text-rpg-product-gate] status={report['status']}")
    print(f"[text-rpg-product-gate] report_json={report_json}")
    print(f"[text-rpg-product-gate] report_md={report_md}")
    if report.get("gm_results_file"):
        print(f"[text-rpg-product-gate] gm_results_file={report['gm_results_file']}")
    if report["errors"]:
        for entry in report["errors"]:
            print(f"[text-rpg-product-gate] error={entry}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
