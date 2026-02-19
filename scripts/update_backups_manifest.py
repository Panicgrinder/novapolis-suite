"""scripts.update_backups_manifest

Ersatz für `scripts/update_backups_manifest.ps1` als Python-Skript.

Erzeugt in `Backups/`:
- `manifest.v1.json`
- `manifest.v1.sha256sum.txt`

Usage:
    python -m scripts.update_backups_manifest
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import asdict, dataclass
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
class ManifestEntry:
    filename: str
    size_bytes: int
    sha256: str
    created_at: str
    modified_at: str


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _default_backups_path() -> Path:
    return _repo_root() / "Backups"


def _iso_utc(ts: float) -> str:
    return datetime.fromtimestamp(ts, tz=UTC).isoformat().replace("+00:00", "Z")


def _file_sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _iter_files(backups_path: Path, *, include_subdirectories: bool) -> list[Path]:
    if include_subdirectories:
        candidates = [p for p in backups_path.rglob("*") if p.is_file()]
    else:
        candidates = [p for p in backups_path.iterdir() if p.is_file()]

    return [p for p in candidates if p.name not in EXCLUDED_NAMES]


def build_manifest(
    backups_path: Path,
    *,
    include_subdirectories: bool,
    generator: str,
) -> tuple[dict, list[ManifestEntry]]:
    backups_full_path = backups_path.resolve()
    if not backups_full_path.exists() or not backups_full_path.is_dir():
        raise FileNotFoundError(f"Backups path '{backups_full_path}' does not exist.")

    base = str(backups_full_path)
    normalized_base = base
    if not normalized_base.endswith(("/", "\\")):
        normalized_base += "\\"

    entries: list[ManifestEntry] = []
    for f in _iter_files(backups_full_path, include_subdirectories=include_subdirectories):
        st = f.stat()
        rel = str(f)[len(normalized_base) :]
        if not rel:
            rel = f.name
        rel = rel.replace("\\", "/")

        entries.append(
            ManifestEntry(
                filename=rel,
                size_bytes=st.st_size,
                sha256=_file_sha256(f),
                created_at=_iso_utc(st.st_ctime),
                modified_at=_iso_utc(st.st_mtime),
            )
        )

    entries_sorted = sorted(entries, key=lambda e: e.filename)
    manifest = {
        "manifest_version": "1",
        "generated_at": datetime.now(tz=UTC).isoformat().replace("+00:00", "Z"),
        "generator": generator,
        "base_path": str(backups_full_path),
        "entry_count": len(entries_sorted),
        "entries": [asdict(e) for e in entries_sorted],
    }
    return manifest, entries_sorted


def write_outputs(
    backups_path: Path,
    *,
    manifest_file: str,
    checksum_file: str,
    manifest: dict,
    entries_sorted: list[ManifestEntry],
) -> None:
    manifest_path = backups_path / manifest_file
    checksum_path = backups_path / checksum_file

    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    checksum_lines = [f"{e.sha256}  {e.filename}" for e in entries_sorted]
    checksum_path.write_text("\n".join(checksum_lines) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Generate Backups/manifest.v1.json and manifest.v1.sha256sum.txt"
    )
    ap.add_argument(
        "backups_path",
        nargs="?",
        default=None,
        help="Optional Backups path (default: repo-root/Backups)",
    )
    ap.add_argument("--manifest-file", default="manifest.v1.json")
    ap.add_argument("--checksum-file", default="manifest.v1.sha256sum.txt")
    ap.add_argument("--include-subdirectories", action="store_true")
    args = ap.parse_args(argv)

    backups_path = Path(args.backups_path) if args.backups_path else _default_backups_path()
    manifest, entries_sorted = build_manifest(
        backups_path,
        include_subdirectories=bool(args.include_subdirectories),
        generator="scripts/update_backups_manifest.py",
    )
    write_outputs(
        backups_path.resolve(),
        manifest_file=str(args.manifest_file),
        checksum_file=str(args.checksum_file),
        manifest=manifest,
        entries_sorted=entries_sorted,
    )

    print(f"Manifest written to {backups_path / args.manifest_file}")
    print(f"Checksums written to {backups_path / args.checksum_file}")
    print(f"Entries: {len(entries_sorted)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
