#!/usr/bin/env python
"""Liefert kompakte Agent-Modul-Statusdaten je Aktion als JSON."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Agent module action summaries")
    parser.add_argument(
        "--action",
        required=True,
        choices=["datasets", "synonyms", "finetune", "profiles"],
    )
    return parser.parse_args()


def _fmt_ts(path: Path | None) -> str:
    if path is None:
        return "n/a"
    return datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d %H:%M")


def _latest(paths: list[Path]) -> Path | None:
    if not paths:
        return None
    return max(paths, key=lambda p: p.stat().st_mtime)


def _datasets(project_root: Path) -> dict[str, Any]:
    datasets_dir = project_root / "eval" / "datasets"
    files = list(datasets_dir.rglob("*.jsonl")) if datasets_dir.exists() else []
    latest = _latest(files)
    lines = [
        f"Items: {len(files)} Dateien",
        f"Latest: {latest.name if latest else 'n/a'}",
        f"Updated: {_fmt_ts(latest)}",
    ]
    return {"title": "Datasets", "lines": lines}


def _synonyms(project_root: Path) -> dict[str, Any]:
    candidates = [p for p in project_root.rglob("*synonym*.json*") if p.is_file()]
    latest = _latest(candidates)
    lines = [
        f"Dateien: {len(candidates)}",
        f"Latest: {latest.name if latest else 'n/a'}",
        f"Updated: {_fmt_ts(latest)}",
    ]
    return {"title": "Synonyms", "lines": lines}


def _finetune(project_root: Path) -> dict[str, Any]:
    outputs_dir = project_root.parent / "outputs"
    lora_dirs = (
        [p for p in outputs_dir.glob("lora-*") if p.is_dir()] if outputs_dir.exists() else []
    )
    results_dir = project_root / "eval" / "results"
    result_files = (
        [p for p in results_dir.glob("finetune*.jsonl") if p.is_file()]
        if results_dir.exists()
        else []
    )
    latest_lora = _latest(lora_dirs)
    latest_result = _latest(result_files)
    lines = [
        f"LoRA-Runs: {len(lora_dirs)}",
        f"Latest LoRA: {latest_lora.name if latest_lora else 'n/a'}",
        f"Finetune-Reports: {len(result_files)}",
        f"Latest Report: {latest_result.name if latest_result else 'n/a'}",
    ]
    return {"title": "Finetune", "lines": lines}


def _profiles(project_root: Path) -> dict[str, Any]:
    config_dir = project_root / "eval" / "config"
    profile_files: list[Path] = []
    if config_dir.exists():
        profile_files.extend([p for p in config_dir.glob("*profile*.json*") if p.is_file()])
        suites = config_dir / "suites.json"
        if suites.exists():
            profile_files.append(suites)
    latest = _latest(profile_files)
    lines = [
        f"Config-Dateien: {len(profile_files)}",
        f"Latest: {latest.name if latest else 'n/a'}",
        f"Updated: {_fmt_ts(latest)}",
    ]
    return {"title": "Profiles", "lines": lines}


def main() -> int:
    args = _parse_args()
    project_root = Path(__file__).resolve().parents[1]

    mapping = {
        "datasets": _datasets,
        "synonyms": _synonyms,
        "finetune": _finetune,
        "profiles": _profiles,
    }
    payload = mapping[args.action](project_root)
    out = {
        "ok": True,
        "action": args.action,
        "title": payload["title"],
        "lines": payload["lines"],
    }
    print(json.dumps(out, ensure_ascii=False, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
