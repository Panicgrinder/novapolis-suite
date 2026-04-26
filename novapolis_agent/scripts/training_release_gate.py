#!/usr/bin/env python
from __future__ import annotations

import argparse
import glob
import importlib
import json
import os
import sys
from dataclasses import dataclass
from typing import Any

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
REPO_ROOT = os.path.dirname(PROJECT_ROOT)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

dataset_validator = importlib.import_module("scripts.validate_eval_datasets")

DEFAULT_RESULTS_DIR = os.path.join(PROJECT_ROOT, "eval", "results")
DEFAULT_PROVENANCE_DOC = os.path.join(REPO_ROOT, "novapolis-dev", "docs", "dataset-provenance.md")
DEFAULT_SUITE_CONFIG = os.path.join(PROJECT_ROOT, "eval", "config", "suites.json")
DEFAULT_REQUIRED_SUITES = [
    "neutral",
    "rpg",
    "quality_de",
    "support_de_ab",
    "rp_content",
    "gm_session",
]
STATUS_RANK = {"rot": 0, "gelb": 1, "gruen": 2}


@dataclass
class GateResult:
    ok: bool
    code: int
    checks: list[str]
    errors: list[str]
    details: dict[str, Any]

    def to_payload(self) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "ok": self.ok,
            "checks": self.checks,
            "errors": self.errors,
        }
        payload.update(self.details)
        return payload


def _normalize_relative(path: str) -> str | None:
    abs_path = os.path.abspath(path)
    try:
        rel_path = os.path.relpath(abs_path, REPO_ROOT)
    except ValueError:
        return None
    if rel_path.startswith(".."):
        return None
    return rel_path.replace("\\", "/")


def _is_repo_path(path: str) -> bool:
    return _normalize_relative(path) is not None


def _parse_provenance_table(doc_path: str | None = None) -> dict[str, str]:
    table: dict[str, str] = {}
    resolved_doc_path = doc_path or DEFAULT_PROVENANCE_DOC
    if not os.path.exists(resolved_doc_path):
        return table

    for line in open(resolved_doc_path, encoding="utf-8").read().splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        parts = [part.strip() for part in stripped.strip("|").split("|")]
        if len(parts) < 5:
            continue
        path_cell = parts[1].strip("`")
        status = parts[3].lower()
        if not path_cell or path_cell == "Pfad" or status not in STATUS_RANK:
            continue
        table[path_cell.replace("\\", "/")] = status
    return table


def _read_jsonl_rows(path: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            text = line.strip()
            if not text:
                continue
            raw = json.loads(text)
            if isinstance(raw, dict):
                rows.append(raw)
    return rows


def _expand_repo_pattern(pattern: str) -> list[str]:
    candidate = pattern
    if not os.path.isabs(candidate):
        candidate = os.path.join(REPO_ROOT, candidate)
    matches = sorted(glob.glob(candidate, recursive=True))
    if matches:
        return matches
    return [candidate] if os.path.exists(candidate) else []


def _collect_results_source_paths(results_path: str) -> list[str]:
    rows = _read_jsonl_rows(results_path)
    meta_patterns: list[str] = []
    source_paths: list[str] = []

    for row in rows:
        if row.get("_meta"):
            patterns = row.get("patterns")
            if isinstance(patterns, list):
                for pattern in patterns:
                    if isinstance(pattern, str) and pattern.strip():
                        meta_patterns.append(pattern.strip())
            continue

        source_file = row.get("source_file")
        if isinstance(source_file, str) and source_file.strip():
            source_paths.append(source_file.strip())

    resolved: list[str] = []
    if meta_patterns:
        for pattern in meta_patterns:
            resolved.extend(_expand_repo_pattern(pattern))

    if not resolved:
        for source_path in source_paths:
            if source_path.startswith(("novapolis_agent/", "novapolis-rp/")):
                expanded = _expand_repo_pattern(source_path)
                if expanded:
                    resolved.extend(expanded)

    unique: list[str] = []
    seen: set[str] = set()
    for item in resolved:
        normalized = os.path.abspath(item)
        if normalized in seen:
            continue
        seen.add(normalized)
        unique.append(normalized)
    return unique


def _check_provenance(paths: list[str], *, minimum_status: str) -> tuple[list[str], dict[str, str]]:
    provenance = _parse_provenance_table()
    found: dict[str, str] = {}
    errors: list[str] = []
    minimum_rank = STATUS_RANK[minimum_status]

    for path in paths:
        relative = _normalize_relative(path)
        if relative is None:
            continue
        status = provenance.get(relative)
        if status is None:
            errors.append(f"provenance missing for {relative}")
            continue
        found[relative] = status
        if STATUS_RANK[status] < minimum_rank:
            errors.append(
                f"provenance status {status} below required {minimum_status} for {relative}"
            )
    return errors, found


def _latest_rp_content_result(results_dir: str | None = None) -> str | None:
    resolved_results_dir = results_dir or DEFAULT_RESULTS_DIR
    files = sorted(
        glob.glob(os.path.join(resolved_results_dir, "results_*_rp_content*.jsonl")),
        reverse=True,
    )
    return files[0] if files else None


def _rp_content_is_green(path: str) -> tuple[bool, dict[str, int | str]]:
    rows = _read_jsonl_rows(path)
    success_count = 0
    failure_count = 0
    for row in rows:
        if row.get("_meta"):
            continue
        if bool(row.get("success")):
            success_count += 1
        else:
            failure_count += 1
    return (
        success_count > 0 and failure_count == 0,
        {
            "result_file": path,
            "success_count": success_count,
            "failure_count": failure_count,
        },
    )


def ensure_release_gate(
    *,
    train_file: str | None = None,
    results_file: str | None = None,
    results_dir: str | None = None,
    require_green_provenance: bool,
) -> GateResult:
    target_path = train_file or results_file
    if not target_path:
        return GateResult(False, 2, [], ["missing target path"], {})

    if not _is_repo_path(target_path):
        return GateResult(
            True,
            0,
            ["repo-scope skipped for external target"],
            [],
            {"skipped": True},
        )

    resolved_results_dir = results_dir or DEFAULT_RESULTS_DIR

    validate_args = ["--strict", "--suite-config", DEFAULT_SUITE_CONFIG]
    for suite in DEFAULT_REQUIRED_SUITES:
        validate_args.extend(["--suite", suite])
    if dataset_validator.main(validate_args) != 0:
        return GateResult(
            False,
            3,
            [],
            ["validate_eval_datasets --strict failed"],
            {"target": target_path},
        )

    rp_content_results = _latest_rp_content_result(resolved_results_dir)
    if not rp_content_results:
        return GateResult(
            False,
            4,
            ["validate_eval_datasets --strict"],
            ["missing rp_content results"],
            {"results_dir": resolved_results_dir},
        )

    rp_content_ok, rp_content_details = _rp_content_is_green(rp_content_results)
    if not rp_content_ok:
        return GateResult(
            False,
            5,
            ["validate_eval_datasets --strict"],
            ["latest rp_content result is not green"],
            {"rp_content": rp_content_details},
        )

    provenance_paths = (
        [train_file] if train_file else _collect_results_source_paths(results_file or "")
    )
    provenance_errors, provenance_found = _check_provenance(
        [path for path in provenance_paths if path],
        minimum_status="gruen" if require_green_provenance else "gelb",
    )
    if provenance_errors:
        return GateResult(
            False,
            6,
            ["validate_eval_datasets --strict", "rp_content"],
            provenance_errors,
            {
                "rp_content": rp_content_details,
                "provenance": provenance_found,
                "target": target_path,
            },
        )

    return GateResult(
        True,
        0,
        ["validate_eval_datasets --strict", "rp_content", "provenance"],
        [],
        {
            "rp_content": rp_content_details,
            "provenance": provenance_found,
            "target": target_path,
        },
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Guard export and LoRA release paths")
    parser.add_argument("--train-file", default=None)
    parser.add_argument("--results-file", default=None)
    parser.add_argument("--results-dir", default=DEFAULT_RESULTS_DIR)
    parser.add_argument("--allow-yellow-provenance", action="store_true")
    args = parser.parse_args(argv)

    result = ensure_release_gate(
        train_file=args.train_file,
        results_file=args.results_file,
        results_dir=args.results_dir,
        require_green_provenance=not args.allow_yellow_provenance,
    )
    print(json.dumps(result.to_payload(), ensure_ascii=False))
    return result.code


if __name__ == "__main__":
    raise SystemExit(main())
