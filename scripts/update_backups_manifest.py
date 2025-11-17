"""
Ersatz für `scripts/update_backups_manifest.ps1` als Python-Skript.
Funktion (minimal): Sammle Dateien in `Backups/` und erstelle/aktualisiere ein
Manifest `Backups/manifest.v1.json` mit basic metadata (name, size, sha256 optional).

Usage:
    python -m scripts.update_backups_manifest
"""
from __future__ import annotations
import json
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BACKUPS = ROOT / "Backups"
MANIFEST = BACKUPS / "manifest.v1.json"


def file_sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def build_manifest() -> dict:
    if not BACKUPS.exists():
        print("Backups/ directory does not exist. Creating it.")
        BACKUPS.mkdir(parents=True, exist_ok=True)
    manifest = {"generated_at": None, "files": []}
    from datetime import datetime
    manifest["generated_at"] = datetime.now().isoformat()
    for p in sorted(BACKUPS.iterdir()):
        if p.is_file() and p.name != MANIFEST.name:
            manifest["files"].append({
                "name": p.name,
                "size": p.stat().st_size,
                "sha256": file_sha256(p)
            })
    return manifest


def main() -> int:
    m = build_manifest()
    with MANIFEST.open("w", encoding="utf-8") as fh:
        json.dump(m, fh, indent=2, ensure_ascii=False)
    print(f"Wrote manifest: {MANIFEST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
