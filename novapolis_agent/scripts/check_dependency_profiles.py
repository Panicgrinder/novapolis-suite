from __future__ import annotations

import argparse
import ast
from pathlib import Path

OPTIONAL_TOOL_MODULES: dict[str, str] = {
    "openai": "openai",
    "rich": "rich",
    "pypdf": "pypdf",
}

DEFAULT_TARGETS: tuple[str, ...] = (
    "novapolis_agent/scripts/openai_ft_status.py",
    "novapolis_agent/scripts/openai_finetune.py",
    "novapolis_agent/scripts/run_eval.py",
    "novapolis_agent/scripts/eval_ui.py",
    "scripts/extract_rp_pdfs.py",
)


def parse_requirement_names(path: Path) -> set[str]:
    names: set[str] = set()
    if not path.exists():
        return names
    for raw in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        line = line.split(";", 1)[0].strip()
        for sep in ("<=", ">=", "==", "~=", "!=", "<", ">", "["):
            if sep in line:
                line = line.split(sep, 1)[0].strip()
        if line:
            names.add(line.lower())
    return names


def imported_top_modules(path: Path) -> set[str]:
    modules: set[str] = set()
    source = path.read_text(encoding="utf-8", errors="ignore")
    tree = ast.parse(source, filename=str(path))
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                modules.add(alias.name.split(".", 1)[0])
        elif isinstance(node, ast.ImportFrom) and node.module:
            modules.add(node.module.split(".", 1)[0])
    return modules


def evaluate_optional_profile(
    repo_root: Path,
    requirement_rel: str,
    target_rels: tuple[str, ...],
    module_to_package: dict[str, str],
) -> dict[str, object]:
    declared = parse_requirement_names(repo_root / requirement_rel)

    usage_by_package: dict[str, list[str]] = {}
    for rel in target_rels:
        file_path = repo_root / rel
        if not file_path.exists():
            continue
        imported = imported_top_modules(file_path)
        for module, package in module_to_package.items():
            if module in imported:
                usage_by_package.setdefault(package, []).append(rel)

    used_packages = set(usage_by_package.keys())
    missing = sorted(used_packages - declared)
    declared_optional = set(module_to_package.values())
    extra = sorted(declared - declared_optional)

    return {
        "declared": sorted(declared),
        "used": sorted(used_packages),
        "missing": missing,
        "extra": extra,
        "usage_by_package": usage_by_package,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate optional dependency profile for Agent helper scripts"
    )
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parents[2]),
        help="Repository root path",
    )
    parser.add_argument(
        "--requirements-file",
        default="novapolis_agent/requirements/optional-tools.txt",
        help="Relative path to optional requirements file",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return exitcode 1 when warnings are present",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    result = evaluate_optional_profile(
        repo_root,
        args.requirements_file,
        DEFAULT_TARGETS,
        OPTIONAL_TOOL_MODULES,
    )

    print("[dependency-profiles] optional-tools check")
    print(f"  repo_root: {repo_root}")
    print(f"  requirements: {args.requirements_file}")
    print(f"  declared: {', '.join(result['declared']) or '-'}")
    print(f"  used: {', '.join(result['used']) or '-'}")

    warnings = 0
    missing = result["missing"]
    if missing:
        warnings += 1
        print(f"  WARN missing packages in optional-tools: {', '.join(missing)}")

    extra = result["extra"]
    if extra:
        warnings += 1
        print(f"  WARN unknown extra packages in optional-tools: {', '.join(extra)}")

    usage_by_package = result["usage_by_package"]
    for pkg in sorted(usage_by_package):
        paths = ", ".join(sorted(usage_by_package[pkg]))
        print(f"  usage {pkg}: {paths}")

    if warnings == 0:
        print("  OK profile is consistent")
        return 0

    return 1 if args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
