#!/usr/bin/env python
from __future__ import annotations

import argparse
import fnmatch
import glob
import importlib
import json
import os
from typing import Any

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
DEFAULT_SUITE_CONFIG = os.path.join(PROJECT_ROOT, "eval", "config", "suites.json")
DEFAULT_DATASET_PATTERNS = [
    os.path.join(PROJECT_ROOT, "eval", "datasets", "**", "*.json*"),
    os.path.join(PROJECT_ROOT, "eval", "datasets", "**", "*.yml"),
    os.path.join(PROJECT_ROOT, "eval", "datasets", "**", "*.yaml"),
]


def _load_coercer():
    import sys

    if PROJECT_ROOT not in sys.path:
        sys.path.insert(0, PROJECT_ROOT)
    mod = importlib.import_module("utils.eval_utils")
    return mod.coerce_eval_records


def _validate_record(record: dict[str, Any], file_path: str, index: int) -> list[str]:
    errors: list[str] = []
    tags = record.get("tags")

    if tags is not None:
        if not isinstance(tags, list) or not all(isinstance(t, str) for t in tags):
            errors.append(f"{file_path}#{index}: tags must be list[str]")

    if "messages" not in record and "prompt" not in record and "conversation" not in record:
        errors.append(f"{file_path}#{index}: missing messages/prompt/conversation")

    return errors


def _load_suite_patterns(suite_config_path: str, selected_suites: list[str] | None) -> list[str]:
    try:
        raw = json.loads(open(suite_config_path, encoding="utf-8").read())
    except Exception:
        return []

    suites_obj = raw.get("suites") if isinstance(raw, dict) else None
    if not isinstance(suites_obj, dict):
        return []

    if not selected_suites:
        return []

    suite_names = selected_suites
    patterns: list[str] = []
    for name in suite_names:
        suite = suites_obj.get(name)
        if not isinstance(suite, dict):
            continue
        packages = suite.get("packages")
        if isinstance(packages, list):
            for package in packages:
                if isinstance(package, str) and package.strip():
                    patterns.append(package.strip())
    return patterns


def _duplicate_allowed(file_a: str, file_b: str, allow_patterns: list[str]) -> bool:
    base_a = os.path.basename(file_a)
    base_b = os.path.basename(file_b)
    for pattern in allow_patterns:
        if fnmatch.fnmatch(file_a, pattern) or fnmatch.fnmatch(file_b, pattern):
            return True
        if fnmatch.fnmatch(base_a, pattern) or fnmatch.fnmatch(base_b, pattern):
            return True
    return False


def _matches_any(path: str, patterns: list[str]) -> bool:
    base = os.path.basename(path)
    for pattern in patterns:
        if fnmatch.fnmatch(path, pattern) or fnmatch.fnmatch(base, pattern):
            return True
    return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate eval datasets (id/slug/tags + basic shape)"
    )
    parser.add_argument(
        "--pattern",
        action="append",
        default=[],
        help="Glob pattern for dataset files (repeatable)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail on duplicate ids/slugs and missing id+slug",
    )
    parser.add_argument(
        "--suite-config",
        default=DEFAULT_SUITE_CONFIG,
        help="Path to suite config JSON",
    )
    parser.add_argument(
        "--suite",
        action="append",
        default=[],
        help="Suite name from suite-config (repeatable)",
    )
    parser.add_argument(
        "--allow-duplicate-pattern",
        action="append",
        default=["*combined*"],
        help="Glob pattern for files where duplicate ids/slugs are allowed",
    )
    parser.add_argument(
        "--allow-missing-id-pattern",
        action="append",
        default=[],
        help="Glob pattern for files where missing id/slug is tolerated",
    )
    args = parser.parse_args(argv)
    coerce_eval_records = _load_coercer()

    suite_patterns = _load_suite_patterns(args.suite_config, args.suite or None)

    patterns = list(args.pattern or [])
    patterns.extend(suite_patterns)
    if not patterns:
        patterns = list(DEFAULT_DATASET_PATTERNS)

    files: list[str] = []
    for pat in patterns:
        files.extend(glob.glob(pat, recursive=True))
    files = sorted(set(files))

    if not files:
        print("No dataset files found.")
        return 1

    errors: list[str] = []
    warnings: list[str] = []
    seen_ids: dict[str, str] = {}
    seen_slugs: dict[str, str] = {}
    record_count = 0

    for file_path in files:
        try:
            text = open(file_path, encoding="utf-8").read()
        except Exception as exc:
            errors.append(f"{file_path}: read failed: {exc}")
            continue

        records = coerce_eval_records(text, file_path)
        if not records:
            errors.append(f"{file_path}: no records parsed")
            continue

        for idx, record in enumerate(records, start=1):
            record_count += 1
            errors.extend(_validate_record(record, file_path, idx))

            rec_id_raw = str(record.get("id") or "").strip()
            rec_slug_raw = str(record.get("slug") or "").strip()
            rec_id = rec_id_raw.lower()
            rec_slug = rec_slug_raw.lower()

            if rec_id:
                if rec_id in seen_ids and seen_ids[rec_id] != file_path:
                    msg = f"duplicate id '{rec_id_raw}' in {file_path} and {seen_ids[rec_id]}"
                    if args.strict and not _duplicate_allowed(
                        file_path, seen_ids[rec_id], args.allow_duplicate_pattern
                    ):
                        errors.append(msg)
                    else:
                        warnings.append(msg)
                else:
                    seen_ids[rec_id] = file_path

            if rec_slug:
                if rec_slug in seen_slugs and seen_slugs[rec_slug] != file_path:
                    msg = (
                        f"duplicate slug '{rec_slug_raw}' in {file_path} and {seen_slugs[rec_slug]}"
                    )
                    if args.strict and not _duplicate_allowed(
                        file_path, seen_slugs[rec_slug], args.allow_duplicate_pattern
                    ):
                        errors.append(msg)
                    else:
                        warnings.append(msg)
                else:
                    seen_slugs[rec_slug] = file_path

            if not rec_id and not rec_slug:
                msg = f"{file_path}#{idx}: missing id and slug"
                if args.strict and not _matches_any(file_path, args.allow_missing_id_pattern):
                    errors.append(msg)
                else:
                    warnings.append(msg)

    # In non-strict mode fehlt-id/slug Hinweise aus _validate_record nicht als Fehler zählen.
    if not args.strict:
        errors = [e for e in errors if "missing id and slug" not in e]

    if errors:
        print("Eval dataset validation FAILED:")
        for err in errors:
            print(f"- {err}")
        return 1

    if warnings:
        print("Eval dataset validation WARNINGS:")
        for warn in warnings:
            print(f"- {warn}")

    print("Eval dataset validation OK:")
    print(
        f"files={len(files)}, records={record_count}, "
        + f"ids={len(seen_ids)}, slugs={len(seen_slugs)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
