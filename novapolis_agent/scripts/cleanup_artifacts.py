from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

DEFAULT_TARGETS: tuple[str, ...] = (
    "novapolis_agent/eval/results",
    "novapolis_agent/outputs",
    "outputs",
)

RUN_GROUP_TARGETS = {"novapolis_agent/eval/results"}
RUN_TOKEN_RE = re.compile(r"(\d{8}_\d{4})")


@dataclass(frozen=True)
class ArtifactDecision:
    path: Path
    target: str
    action: str
    reason: str


@dataclass(frozen=True)
class ArtifactGroup:
    key: str
    target: str
    paths: tuple[Path, ...]
    newest_mtime: float


def _iter_files(target_dir: Path) -> list[Path]:
    if not target_dir.exists():
        return []
    return [p for p in target_dir.rglob("*") if p.is_file()]


def _matches_keep_name(path: Path | str, keep_names: tuple[str, ...]) -> str | None:
    low = str(path).replace("\\", "/").lower()
    for name in keep_names:
        n = name.strip().lower()
        if n and n in low:
            return n
    return None


def _extract_run_token(path: Path | str) -> str | None:
    matches = RUN_TOKEN_RE.findall(str(path).replace("\\", "/"))
    if not matches:
        return None
    return matches[-1]


def _group_key_for_target(target: str, target_dir: Path, file_path: Path) -> str:
    rel = file_path.relative_to(target_dir).as_posix()

    if target in RUN_GROUP_TARGETS:
        run_token = _extract_run_token(rel)
        if run_token is not None:
            return f"run:{run_token}"

    top_level = rel.split("/", 1)[0]
    return f"entry:{top_level}"


def _build_artifact_groups(target: str, target_dir: Path) -> list[ArtifactGroup]:
    grouped_paths: dict[str, list[Path]] = {}

    for file_path in _iter_files(target_dir):
        group_key = _group_key_for_target(target, target_dir, file_path)
        grouped_paths.setdefault(group_key, []).append(file_path)

    groups: list[ArtifactGroup] = []
    for group_key, paths in grouped_paths.items():
        groups.append(
            ArtifactGroup(
                key=group_key,
                target=target,
                paths=tuple(sorted(paths, key=lambda path: path.as_posix())),
                newest_mtime=max(path.stat().st_mtime for path in paths),
            )
        )

    return sorted(
        groups,
        key=lambda group: (-group.newest_mtime, group.key),
    )


def plan_artifact_cleanup(
    repo_root: Path,
    targets: tuple[str, ...] = DEFAULT_TARGETS,
    keep_latest: int = 15,
    keep_names: tuple[str, ...] = ("baseline", "marathon", "quality_de"),
) -> list[ArtifactDecision]:
    decisions: list[ArtifactDecision] = []

    for rel in targets:
        target_dir = repo_root / rel
        groups = _build_artifact_groups(rel, target_dir)
        kept_latest_groups = 0

        for group in groups:
            keep_token = None
            for group_path in group.paths:
                rel_path = group_path.relative_to(repo_root).as_posix()
                keep_token = _matches_keep_name(rel_path, keep_names)
                if keep_token is not None:
                    break

            if keep_token is not None:
                action = "keep"
                reason = f"name:{keep_token}"
            elif kept_latest_groups < keep_latest:
                action = "keep"
                reason = f"latest-groups:{keep_latest}"
                kept_latest_groups += 1
            else:
                action = "remove"
                reason = f"beyond-latest-groups:{keep_latest}"

            for file_path in group.paths:
                decisions.append(
                    ArtifactDecision(
                        path=file_path,
                        target=rel,
                        action=action,
                        reason=reason,
                    )
                )

    return decisions


def apply_cleanup(
    decisions: list[ArtifactDecision],
    dry_run: bool = True,
    remove_empty_dirs: bool = False,
) -> tuple[int, int]:
    removed = 0
    kept = 0

    for d in decisions:
        if d.action == "keep":
            kept += 1
            continue

        if dry_run:
            continue

        if d.path.exists():
            d.path.unlink()
            removed += 1

    if (not dry_run) and remove_empty_dirs:
        roots = sorted({d.path.parent for d in decisions}, key=lambda p: len(p.parts), reverse=True)
        for root in roots:
            for p in sorted(root.rglob("*"), key=lambda x: len(x.parts), reverse=True):
                if p.is_dir():
                    with_context = any(c.path.parent == p for c in decisions)
                    if with_context:
                        try:
                            p.rmdir()
                        except OSError:
                            pass

    return removed, kept


def build_report(
    repo_root: Path,
    decisions: list[ArtifactDecision],
    dry_run: bool,
    removed_count: int,
) -> dict[str, object]:
    keep = [d for d in decisions if d.action == "keep"]
    remove = [d for d in decisions if d.action == "remove"]

    return {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "repo_root": str(repo_root),
        "dry_run": dry_run,
        "summary": {
            "targets": sorted({d.target for d in decisions}),
            "keep_count": len(keep),
            "remove_count": len(remove),
            "removed_count": removed_count,
        },
        "kept": [
            {
                "path": d.path.relative_to(repo_root).as_posix(),
                "target": d.target,
                "reason": d.reason,
            }
            for d in keep
        ],
        "would_remove": [
            {
                "path": d.path.relative_to(repo_root).as_posix(),
                "target": d.target,
                "reason": d.reason,
            }
            for d in remove
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Cleanup eval/training artifacts with retention rules"
    )
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parents[2]),
        help="Repository root path",
    )
    parser.add_argument(
        "--target",
        action="append",
        default=None,
        help="Relative target directory (can be specified multiple times)",
    )
    parser.add_argument("--keep-latest", type=int, default=15)
    parser.add_argument(
        "--keep-name",
        action="append",
        default=["baseline", "marathon", "quality_de"],
        help="Keep files containing this token in filename (can repeat)",
    )
    parser.add_argument("--dry-run", action="store_true", help="Plan only, do not delete files")
    parser.add_argument("--remove-empty-dirs", action="store_true")
    parser.add_argument(
        "--report",
        default=".tmp/results/reports/artifact_lifecycle_report.json",
        help="Path to machine-readable JSON report (relative to repo root)",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    targets = tuple(args.target) if args.target else DEFAULT_TARGETS
    keep_names = tuple(args.keep_name or [])

    decisions = plan_artifact_cleanup(
        repo_root=repo_root,
        targets=targets,
        keep_latest=max(0, int(args.keep_latest)),
        keep_names=keep_names,
    )
    removed_count, kept_count = apply_cleanup(
        decisions=decisions,
        dry_run=bool(args.dry_run),
        remove_empty_dirs=bool(args.remove_empty_dirs),
    )

    report = build_report(
        repo_root=repo_root,
        decisions=decisions,
        dry_run=bool(args.dry_run),
        removed_count=removed_count,
    )
    report_path = (repo_root / args.report).resolve()
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print("[artifact-cleanup] report:", report_path)
    print("  dry_run:", bool(args.dry_run))
    print("  keep_count:", kept_count)
    print("  remove_count:", len([d for d in decisions if d.action == "remove"]))
    print("  removed_count:", removed_count)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
