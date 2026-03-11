from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _load_sources(config_path: Path) -> tuple[list[Path], list[Path]]:
    raw = json.loads(config_path.read_text(encoding="utf-8"))
    items = raw.get("sources", [])
    if not isinstance(items, list):
        raise ValueError("Invalid sources config: 'sources' must be a list")

    repo_root = _repo_root()
    include: list[Path] = []
    missing_required: list[Path] = []

    for item in items:
        if not isinstance(item, dict):
            continue
        rel = item.get("path")
        required = bool(item.get("required", False))
        if not isinstance(rel, str) or not rel.strip():
            continue

        p = (repo_root / rel).resolve()
        if p.exists():
            include.append(p)
        elif required:
            missing_required.append(p)

    return include, missing_required


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build project-context index from canonical source manifest"
    )
    parser.add_argument(
        "--sources-file",
        default="novapolis_agent/eval/config/context.bridge.sources.json",
        help="Path to JSON manifest (repo-relative by default)",
    )
    parser.add_argument(
        "--out",
        default="novapolis_agent/eval/results/rag/context_bridge.index.json",
        help="Output index path (repo-relative by default)",
    )
    parser.add_argument(
        "--allow-missing-required",
        action="store_true",
        help="Continue even if required sources are missing",
    )
    args = parser.parse_args(argv)

    repo_root = _repo_root()
    sources_file = (repo_root / args.sources_file).resolve()
    out_path = (repo_root / args.out).resolve()

    if not sources_file.exists():
        print(f"ERROR: sources file not found: {sources_file}")
        return 2

    include_paths, missing_required = _load_sources(sources_file)

    if missing_required and not args.allow_missing_required:
        print("ERROR: missing required sources:")
        for p in missing_required:
            print(f"  - {p}")
        return 3

    if not include_paths:
        print("ERROR: no existing sources to index")
        return 4

    sys.path.insert(0, str(repo_root / "novapolis_agent"))
    try:
        from utils.rag import build_index, save_index
    except Exception as exc:
        print(f"ERROR: failed to import rag utils: {exc}")
        return 5

    idx = build_index([str(p) for p in include_paths])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    save_index(idx, str(out_path))

    summary: dict[str, Any] = {
        "sources_file": str(sources_file.relative_to(repo_root)),
        "indexed_sources": len(include_paths),
        "missing_required": [str(p.relative_to(repo_root)) for p in missing_required],
        "n_docs": idx.n_docs,
        "vocab": len(idx.df),
        "out": str(out_path.relative_to(repo_root)),
    }
    print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
