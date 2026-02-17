"""scripts.rotate_backups

Ersatz für `scripts/rotate_backups.ps1` als Python-Skript.
Implements tiered retention (daily/weekly/monthly/yearly) for backup artifacts.

Usage:
    python -m scripts.rotate_backups
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

EXCLUDED_NAMES = {
    "manifest.v1.json",
    "manifest.v1.sha256sum.txt",
    "rotation.log",
    "README.md",
    "AUDIT.md",
}


@dataclass(frozen=True)
class PlanEntry:
    action: str
    file: str
    size_bytes: int
    modified_utc: str
    age_days: str
    _path: Path


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _default_backups_path() -> Path:
    return _repo_root() / "Backups"


def _iso_utc(ts: float) -> str:
    return datetime.fromtimestamp(ts, tz=UTC).isoformat().replace("+00:00", "Z")


def _iter_files(backups_path: Path, *, include_subdirectories: bool) -> list[Path]:
    if include_subdirectories:
        candidates = [p for p in backups_path.rglob("*") if p.is_file()]
    else:
        candidates = [p for p in backups_path.iterdir() if p.is_file()]

    return [p for p in candidates if p.name not in EXCLUDED_NAMES]


def _format_table(plan: list[PlanEntry]) -> str:
    headers = ["Action", "File", "SizeBytes", "ModifiedUtc", "AgeDays"]
    rows = [[p.action, p.file, str(p.size_bytes), p.modified_utc, p.age_days] for p in plan]
    widths = [len(h) for h in headers]
    for r in rows:
        for i, cell in enumerate(r):
            widths[i] = max(widths[i], len(cell))

    def fmt_row(r: list[str]) -> str:
        return "  ".join(cell.ljust(widths[i]) for i, cell in enumerate(r))

    out = [fmt_row(headers), fmt_row(["-" * w for w in widths])]
    out.extend(fmt_row(r) for r in rows)
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Tiered retention rotation for Backups/")
    ap.add_argument(
        "backups_path",
        nargs="?",
        default=None,
        help="Optional Backups path (default: repo-root/Backups)",
    )
    ap.add_argument("--daily-retention-days", type=int, default=14)
    ap.add_argument("--weekly-retention-weeks", type=int, default=8)
    ap.add_argument("--monthly-retention-months", type=int, default=6)
    ap.add_argument("--yearly-retention-years", type=int, default=2)
    ap.add_argument("--minimum-keep", type=int, default=5)
    ap.add_argument("--apply", action="store_true", help="Delete flagged files")
    ap.add_argument("--include-subdirectories", action="store_true")
    args = ap.parse_args(argv)

    backups_path = Path(args.backups_path) if args.backups_path else _default_backups_path()
    backups_full_path = backups_path.resolve()
    if not backups_full_path.exists() or not backups_full_path.is_dir():
        raise FileNotFoundError(f"Backups path '{backups_full_path}' does not exist.")

    files = _iter_files(backups_full_path, include_subdirectories=bool(args.include_subdirectories))
    files_sorted_desc = sorted(files, key=lambda p: p.stat().st_mtime, reverse=True)
    if not files_sorted_desc:
        print(f"No backup artifacts found in '{backups_full_path}'.")
        return 0

    now = datetime.now(tz=UTC)

    keep_set: set[str] = set()

    def keep(p: Path) -> None:
        keep_set.add(str(p.resolve()).lower())

    take_count = min(int(args.minimum_keep), len(files_sorted_desc))
    for p in files_sorted_desc[:take_count]:
        keep(p)

    daily_buckets: set[str] = set()
    weekly_buckets: set[str] = set()
    monthly_buckets: set[str] = set()
    yearly_buckets: set[str] = set()

    daily_cutoff = int(args.daily_retention_days)
    weekly_cutoff = daily_cutoff + (7 * int(args.weekly_retention_weeks))
    monthly_cutoff = weekly_cutoff + (30 * int(args.monthly_retention_months))
    yearly_cutoff = monthly_cutoff + (365 * int(args.yearly_retention_years))

    for p in files_sorted_desc:
        p_key = str(p.resolve()).lower()
        if p_key in keep_set:
            continue

        mtime = datetime.fromtimestamp(p.stat().st_mtime, tz=UTC)
        age_days = (now - mtime).total_seconds() / 86400.0

        if age_days < daily_cutoff:
            key = mtime.strftime("%Y-%m-%d")
            if key not in daily_buckets:
                daily_buckets.add(key)
                keep(p)
            continue

        if age_days < weekly_cutoff:
            iso = mtime.isocalendar()
            key = f"{iso.year:04d}-W{iso.week:02d}"
            if key not in weekly_buckets:
                weekly_buckets.add(key)
                keep(p)
            continue

        if age_days < monthly_cutoff:
            key = mtime.strftime("%Y-%m")
            if key not in monthly_buckets:
                monthly_buckets.add(key)
                keep(p)
            continue

        if age_days < yearly_cutoff:
            key = mtime.strftime("%Y")
            if key not in yearly_buckets:
                yearly_buckets.add(key)
                keep(p)
            continue

    normalized_base = str(backups_full_path)
    if not normalized_base.endswith(("/", "\\")):
        normalized_base += "\\"

    plan: list[PlanEntry] = []
    for p in sorted(files, key=lambda pp: pp.stat().st_mtime):
        full = str(p.resolve())
        rel = (
            full[len(normalized_base) :]
            if full.lower().startswith(normalized_base.lower())
            else p.name
        )
        rel = rel.replace("\\", "/")

        mtime = datetime.fromtimestamp(p.stat().st_mtime, tz=UTC)
        age_days_raw = (now - mtime).total_seconds() / 86400.0
        action = "Keep" if str(p.resolve()).lower() in keep_set else "Delete"
        plan.append(
            PlanEntry(
                action=action,
                file=rel,
                size_bytes=p.stat().st_size,
                modified_utc=_iso_utc(p.stat().st_mtime),
                age_days=f"{age_days_raw:.1f}",
                _path=p,
            )
        )

    keep_plan = [e for e in plan if e.action == "Keep"]
    delete_plan = [e for e in plan if e.action == "Delete"]

    print("Retention plan:")
    print(_format_table(plan))
    print()
    print(f"Keep: {len(keep_plan)} | Delete: {len(delete_plan)}")

    if not args.apply:
        print("Dry-run complete. Re-run with --apply to delete flagged files.")
        return 0

    if not delete_plan:
        print("Nothing to delete. Retention satisfied.")
        return 0

    log_path = backups_full_path / "rotation.log"
    now_utc = datetime.now(tz=UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    log_lines = [f"[{now_utc}] Deleted {len(delete_plan)} file(s)"]

    for entry in delete_plan:
        entry._path.unlink()
        log_lines.append(f"- {entry.file} (modified {entry.modified_utc})")

    with log_path.open("a", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(log_lines) + "\n")

    print("Deleted files:")
    print(_format_table(delete_plan))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
