#!/usr/bin/env python

from __future__ import annotations

import argparse
import asyncio
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import httpx

DEFAULT_SPEC = "novapolis_agent/eval/config/text_rpg_reference_session.v1.json"
DEFAULT_HANDOVER_SPEC = (
    "novapolis_agent/eval/config/text_rpg_reference_session_handover_slot31_40.v1.json"
)
DEFAULT_SESSION_STORE = ".tmp/results/reference_sessions"

SCRIPT_DIR = Path(__file__).resolve().parent
MODULE_ROOT = SCRIPT_DIR.parent
REPO_ROOT = MODULE_ROOT.parent
for candidate in (MODULE_ROOT, REPO_ROOT):
    candidate_text = str(candidate)
    if candidate_text not in sys.path:
        sys.path.insert(0, candidate_text)


def _read_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{path.as_posix()} must contain a JSON object")
    return payload


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    entries: list[dict[str, Any]] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        parsed = json.loads(line)
        if isinstance(parsed, dict):
            entries.append(parsed)
    return entries


def _default_report_paths(repo_root: Path, timestamp: str) -> tuple[Path, Path]:
    reports_dir = repo_root / ".tmp" / "results" / "reports"
    return (
        reports_dir / f"text_rpg_reference_session_{timestamp}.json",
        reports_dir / f"text_rpg_reference_session_{timestamp}.md",
    )


def load_reference_spec(path: Path) -> dict[str, Any]:
    spec = _read_json(path)
    if not isinstance(spec.get("session_id"), str) or not spec["session_id"].strip():
        raise ValueError("reference session spec requires non-empty session_id")
    steps = spec.get("steps")
    if not isinstance(steps, list) or not steps:
        raise ValueError("reference session spec requires non-empty steps list")
    for index, step in enumerate(steps, start=1):
        if not isinstance(step, dict):
            raise ValueError(f"reference session step {index} must be an object")
    expected = spec.get("expected")
    if expected is not None and not isinstance(expected, dict):
        raise ValueError("reference session spec field 'expected' must be an object")
    return spec


def _collect_actual(
    session_payload: dict[str, Any],
    replay_payload: dict[str, Any],
    session_dir: Path,
) -> dict[str, Any]:
    savegame_path = session_dir / "savegame.json"
    world_log_path = session_dir / "world_log.jsonl"
    pc_log_path = session_dir / "pc_log.jsonl"
    replay_path = session_dir / "replay_manifest.json"

    world_entries = _read_jsonl(world_log_path)
    pc_entries = _read_jsonl(pc_log_path)

    return {
        "contract_version": session_payload.get("contract_version"),
        "session_status": session_payload.get("session_status"),
        "scene_id": session_payload.get("scene_id"),
        "slot_id": session_payload.get("slot_id"),
        "slot_index": session_payload.get("slot_index"),
        "turn_id": session_payload.get("turn_id"),
        "resume_checkpoint_id": session_payload.get("resume_checkpoint_id"),
        "turn_context": session_payload.get("turn_context"),
        "carry_over_count": len(session_payload.get("carry_over") or []),
        "checkpoints": list(session_payload.get("checkpoints") or []),
        "world_log_count": len(session_payload.get("world_log") or []),
        "pc_log_count": len(session_payload.get("pc_log") or []),
        "state_patch_count": len(session_payload.get("state_patches") or []),
        "world_event_count": replay_payload.get("world_event_count"),
        "pc_event_count": replay_payload.get("pc_event_count"),
        "artifacts": {
            "savegame": {
                "path": savegame_path.as_posix(),
                "exists": savegame_path.exists(),
            },
            "world_log": {
                "path": world_log_path.as_posix(),
                "exists": world_log_path.exists(),
                "entries": len(world_entries),
            },
            "pc_log": {
                "path": pc_log_path.as_posix(),
                "exists": pc_log_path.exists(),
                "entries": len(pc_entries),
            },
            "replay_manifest": {
                "path": replay_path.as_posix(),
                "exists": replay_path.exists(),
            },
        },
    }


def _validate_expected(actual: dict[str, Any], expected: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    field_map = {
        "contract_version": "contract_version",
        "session_status": "session_status",
        "scene_id": "scene_id",
        "slot_id": "slot_id",
        "slot_index": "slot_index",
        "turn_id": "turn_id",
        "resume_checkpoint_id": "resume_checkpoint_id",
        "turn_context": "turn_context",
        "carry_over_count": "carry_over_count",
        "checkpoints": "checkpoints",
        "world_log_count": "world_log_count",
        "pc_log_count": "pc_log_count",
        "state_patch_count": "state_patch_count",
        "world_event_count": "world_event_count",
        "pc_event_count": "pc_event_count",
    }
    for expected_key, actual_key in field_map.items():
        if expected_key not in expected:
            continue
        if actual.get(actual_key) != expected[expected_key]:
            actual_value = actual.get(actual_key)
            expected_value = expected[expected_key]
            errors.append(
                f"expected {expected_key}={expected_value!r} " f"but got {actual_value!r}"
            )

    artifacts = actual.get("artifacts") or {}
    for artifact_name in ("savegame", "world_log", "pc_log", "replay_manifest"):
        artifact = artifacts.get(artifact_name) or {}
        if not artifact.get("exists"):
            errors.append(f"missing artifact: {artifact_name}")
    return errors


def _build_markdown(report: dict[str, Any]) -> str:
    if "cases" in report:
        lines = ["# Text-RPG Reference Sessions", ""]
        lines.append(f"- Status: {report['status']}")
        lines.append(f"- Cases: {report['passed_cases']}/{report['case_count']}")
        lines.append(f"- Session Store: {report['session_store_dir']}")
        lines.append("")
        lines.append("## Cases")
        for case in report["cases"]:
            actual = case["actual"]
            lines.append(
                "- "
                f"{case['session_id']}: {case['status']} "
                f"(spec={case['spec_path']}, slot={actual.get('slot_id')}, "
                f"turn={actual.get('turn_id')}, resume={actual.get('resume_checkpoint_id')})"
            )
            lines.append(
                "  "
                f"logs={actual.get('world_log_count')}/{actual.get('pc_log_count')}, "
                f"patches={actual.get('state_patch_count')}, "
                f"carry_over={actual.get('carry_over_count')}"
            )
        lines.append("")
        lines.append("## Errors")
        if report["errors"]:
            for entry in report["errors"]:
                lines.append(f"- {entry}")
        else:
            lines.append("- none")
        lines.append("")
        return "\n".join(lines)

    lines = ["# Text-RPG Reference Session", ""]
    lines.append(f"- Status: {report['status']}")
    lines.append(f"- Session ID: {report['session_id']}")
    lines.append(f"- Spec: {report['spec_path']}")
    lines.append(f"- Session Store: {report['session_store_dir']}")
    lines.append(f"- Steps Executed: {len(report['steps'])}")
    lines.append("")
    lines.append("## Final State")
    actual = report["actual"]
    for key in (
        "contract_version",
        "session_status",
        "scene_id",
        "slot_id",
        "slot_index",
        "turn_id",
        "resume_checkpoint_id",
        "turn_context",
        "carry_over_count",
        "world_log_count",
        "pc_log_count",
        "state_patch_count",
    ):
        lines.append(f"- {key}: {actual.get(key)!r}")
    lines.append("")
    lines.append("## Artifacts")
    for artifact_name, artifact in actual["artifacts"].items():
        suffix = ""
        if "entries" in artifact:
            suffix = f", entries={artifact['entries']}"
        lines.append(
            f"- {artifact_name}: exists={artifact['exists']}, path={artifact['path']}{suffix}"
        )
    lines.append("")
    lines.append("## Errors")
    if report["errors"]:
        for entry in report["errors"]:
            lines.append(f"- {entry}")
    else:
        lines.append("- none")
    lines.append("")
    return "\n".join(lines)


async def run_reference_session(spec_path: Path, session_store_dir: Path) -> dict[str, Any]:
    spec = load_reference_spec(spec_path)
    session_id = str(spec["session_id"])

    from novapolis_agent.app.api import sim as sim_api

    original_store_dir = sim_api._SESSION_STORE_DIR
    sanitized_session_id = sim_api._sanitize_session_id(session_id)
    session_dir = session_store_dir / sanitized_session_id

    session_store_dir.mkdir(parents=True, exist_ok=True)
    shutil.rmtree(session_dir, ignore_errors=True)

    step_reports: list[dict[str, Any]] = []
    errors: list[str] = []
    session_payload: dict[str, Any] = {}
    replay_payload: dict[str, Any] = {}

    sim_api._SESSION_STORE_DIR = session_store_dir
    sim_api.reset_state()
    try:
        transport = httpx.ASGITransport(app=sim_api.app)
        async with httpx.AsyncClient(transport=transport, base_url="http://asgi") as client:
            for index, step in enumerate(spec["steps"], start=1):
                response = await client.put(f"/session/{session_id}", json=step)
                if response.status_code != 200:
                    errors.append(
                        f"step {index} failed with status {response.status_code}: {response.text}"
                    )
                    break
                payload = response.json()
                step_reports.append(
                    {
                        "step": index,
                        "scene_id": payload.get("scene_id"),
                        "slot_id": payload.get("slot_id"),
                        "turn_id": payload.get("turn_id"),
                        "resume_checkpoint_id": payload.get("resume_checkpoint_id"),
                        "world_log_count": len(payload.get("world_log") or []),
                        "pc_log_count": len(payload.get("pc_log") or []),
                        "state_patch_count": len(payload.get("state_patches") or []),
                    }
                )

            if not errors:
                session_response = await client.get(f"/session/{session_id}")
                replay_response = await client.get(f"/session/{session_id}/replay")
                if session_response.status_code != 200:
                    detail = session_response.text
                    errors.append(
                        "session fetch failed with status "
                        f"{session_response.status_code}: {detail}"
                    )
                else:
                    session_payload = session_response.json()
                if replay_response.status_code != 200:
                    detail = replay_response.text
                    errors.append(
                        "replay fetch failed with status "
                        f"{replay_response.status_code}: {detail}"
                    )
                else:
                    replay_payload = replay_response.json()
    finally:
        sim_api._SESSION_STORE_DIR = original_store_dir
        sim_api.reset_state()

    actual = _collect_actual(session_payload, replay_payload, session_dir)
    errors.extend(_validate_expected(actual, spec.get("expected") or {}))

    return {
        "status": "PASS" if not errors else "FAIL",
        "session_id": session_id,
        "spec_path": spec_path.as_posix(),
        "session_store_dir": session_store_dir.as_posix(),
        "session_dir": session_dir.as_posix(),
        "steps": step_reports,
        "expected": spec.get("expected") or {},
        "actual": actual,
        "errors": errors,
    }


async def run_reference_sessions(spec_paths: list[Path], session_store_dir: Path) -> dict[str, Any]:
    case_reports: list[dict[str, Any]] = []
    errors: list[str] = []

    for spec_path in spec_paths:
        report = await run_reference_session(spec_path, session_store_dir)
        case_reports.append(report)
        if report["errors"]:
            errors.extend(f"{report['session_id']}: {entry}" for entry in report["errors"])

    passed_cases = sum(1 for report in case_reports if report["status"] == "PASS")
    return {
        "status": "PASS" if not errors else "FAIL",
        "session_store_dir": session_store_dir.as_posix(),
        "spec_paths": [path.as_posix() for path in spec_paths],
        "case_count": len(case_reports),
        "passed_cases": passed_cases,
        "failed_cases": len(case_reports) - passed_cases,
        "cases": case_reports,
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run deterministic Text-RPG reference sessions")
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parents[2]),
        help="Repository root",
    )
    parser.add_argument(
        "--spec",
        action="append",
        dest="specs",
        default=[],
        help=(
            "Relative path to a reference session spec JSON. "
            "Can be repeated for multiple deterministic reference cases."
        ),
    )
    parser.add_argument(
        "--session-store-dir",
        default=DEFAULT_SESSION_STORE,
        help="Relative directory used for temporary session artifacts",
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
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    spec_inputs = args.specs or [DEFAULT_SPEC]
    spec_paths = [(repo_root / spec).resolve() for spec in spec_inputs]
    session_store_dir = (repo_root / args.session_store_dir).resolve()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    default_json, default_md = _default_report_paths(repo_root, timestamp)
    report_json = (repo_root / args.report_json).resolve() if args.report_json else default_json
    report_md = (repo_root / args.report_md).resolve() if args.report_md else default_md

    if len(spec_paths) == 1:
        report = asyncio.run(run_reference_session(spec_paths[0], session_store_dir))
    else:
        report = asyncio.run(run_reference_sessions(spec_paths, session_store_dir))
    report_json.parent.mkdir(parents=True, exist_ok=True)
    report_md.parent.mkdir(parents=True, exist_ok=True)
    report_json.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    report_md.write_text(_build_markdown(report), encoding="utf-8", newline="\n")

    print(f"[reference-session] status={report['status']}")
    if "session_id" in report:
        print(f"[reference-session] session_id={report['session_id']}")
    else:
        print(f"[reference-session] case_count={report['case_count']}")
    print(f"[reference-session] report_json={report_json}")
    print(f"[reference-session] report_md={report_md}")
    if report["errors"]:
        for entry in report["errors"]:
            print(f"[reference-session] error={entry}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
