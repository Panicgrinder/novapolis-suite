from __future__ import annotations

import argparse
import ast
from pathlib import Path

LEGACY_MODULES: tuple[str, ...] = (
    "app.api.api",
    "app.prompt",
    "app.utils.examples",
)

DEFAULT_SCAN_GLOBS: tuple[str, ...] = (
    "novapolis_agent/**/*.py",
    "scripts/**/*.py",
)

DEFAULT_ALLOWLIST: tuple[str, ...] = (
    "novapolis_agent/tests/test_module_exports.py",
    "novapolis_agent/novapolis_agent/app/utils/examples/__init__.py",
    "novapolis_agent/novapolis_agent/app/utils/examples/logging_example.py",
    "novapolis_agent/novapolis_agent/app/utils/examples/summary_example.py",
)


def _module_is_legacy(module: str) -> bool:
    return module in LEGACY_MODULES or any(module.startswith(f"{m}.") for m in LEGACY_MODULES)


def _collect_legacy_imports(file_path: Path, repo_root: Path) -> list[str]:
    source = file_path.read_text(encoding="utf-8", errors="ignore")
    tree = ast.parse(source, filename=str(file_path))
    rel = file_path.relative_to(repo_root).as_posix()
    findings: list[str] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if _module_is_legacy(alias.name):
                    findings.append(f"{rel}:{node.lineno}: import {alias.name}")
        elif isinstance(node, ast.ImportFrom) and node.module:
            if _module_is_legacy(node.module):
                findings.append(f"{rel}:{node.lineno}: from {node.module} import ...")

    return findings


def scan_legacy_imports(
    repo_root: Path,
    include_globs: tuple[str, ...] = DEFAULT_SCAN_GLOBS,
    allowlist: tuple[str, ...] = DEFAULT_ALLOWLIST,
) -> tuple[list[str], list[str]]:
    allow = {Path(p).as_posix() for p in allowlist}
    allowed_hits: list[str] = []
    disallowed_hits: list[str] = []

    seen_files: set[Path] = set()
    for glob in include_globs:
        for file_path in repo_root.glob(glob):
            if file_path in seen_files or not file_path.is_file():
                continue
            seen_files.add(file_path)

            hits = _collect_legacy_imports(file_path, repo_root)
            if not hits:
                continue

            rel = file_path.relative_to(repo_root).as_posix()
            if rel in allow:
                allowed_hits.extend(hits)
            else:
                disallowed_hits.extend(hits)

    return allowed_hits, disallowed_hits


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Detect imports that reference archived legacy shim modules"
    )
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parents[2]),
        help="Repository root path",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return exitcode 1 when disallowed legacy imports are found",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    allowed, disallowed = scan_legacy_imports(repo_root)

    print("[legacy-shim-check] archived import scan")
    print(f"  repo_root: {repo_root}")
    print(f"  legacy_modules: {', '.join(LEGACY_MODULES)}")
    print(f"  allowed_hits: {len(allowed)}")
    print(f"  disallowed_hits: {len(disallowed)}")

    for hit in allowed:
        print(f"  ALLOW {hit}")
    for hit in disallowed:
        print(f"  FAIL {hit}")

    if disallowed and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
