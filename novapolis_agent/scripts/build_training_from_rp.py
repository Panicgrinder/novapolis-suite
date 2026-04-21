#!/usr/bin/env python
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

DEFAULT_INCLUDE_GLOB = "**/*.md"


@dataclass(frozen=True)
class RPTrainingItem:
    item_id: str
    slug: str
    source_file: str
    source_kind: str
    title: str
    prompt: str
    profile: str
    promotion_level: str
    license_scope: str
    source_package: str
    lead: str

    def to_record(self) -> dict[str, object]:
        profile_tag = f"profile-rp-{self.profile}"
        role_tag = "lore" if self.profile == "lore" else "operations"
        return {
            "id": self.item_id,
            "slug": self.slug,
            "category": "rp_training_seed",
            "profile": self.profile,
            "tags": [
                "training",
                "rp",
                "ssot",
                role_tag,
                profile_tag,
                f"source-{self.source_kind}",
            ],
            "messages": [{"role": "user", "content": self.prompt}],
            "source_file": self.source_file,
            "source_kind": self.source_kind,
            "promotion_level": self.promotion_level,
            "license_scope": self.license_scope,
            "source_package": self.source_package,
            "meta": {
                "source_title": self.title,
                "source_lead": self.lead,
            },
        }


def _slugify(value: str) -> str:
    text = value.lower().strip()
    text = text.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
    text = text.replace("ß", "ss")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def _parse_title(md_text: str, fallback: str) -> str:
    for line in md_text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("---"):
            continue
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip()
    return fallback


def _parse_lead(md_text: str) -> str:
    skip_prefixes = ("---", "stand:", "update:", "checks:", "status:", "last_updated:")
    for line in md_text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith(skip_prefixes):
            continue
        return stripped
    return ""


def _derive_source_kind(relative_path: str) -> str:
    rel = relative_path.replace("\\", "/")
    if rel.startswith("00-admin/"):
        return "admin"
    if "/02-characters/" in rel:
        return "character"
    if "/03-locations/" in rel:
        return "location"
    if "/04-inventory/" in rel:
        return "inventory"
    if rel.startswith("01-factions/"):
        return "faction"
    return "rp"


def _focus_hint(source_kind: str, profile: str) -> str:
    lore_hints = {
        "admin": "mit Fokus auf belegte Rahmenlage, Regeln und sichtbare Folgen",
        "character": "mit Fokus auf Beziehungen, Motive und belegte Spannungen",
        "location": "mit Fokus auf Ort, Nutzung und Inworld-Spannung",
        "inventory": "mit Fokus auf Knappheit, Versorgung und alltagsnahe Folgen",
        "faction": "mit Fokus auf Akteure, Interessen und Reibung",
        "rp": "mit Fokus auf belegte Inworld-Fakten",
    }
    ops_hints = {
        "admin": "mit Fokus auf Status, Prozessrahmen und belastbare Handlungsgrenzen",
        "character": "mit Fokus auf Rollen, Zustaendigkeiten und operative Abhaengigkeiten",
        "location": "mit Fokus auf Funktion, Zugang und operative Relevanz",
        "inventory": "mit Fokus auf Bestand, Mangel, Transfer und Folgeaufwand",
        "faction": "mit Fokus auf Zustaendigkeiten, Austausch und Konfliktpunkte",
        "rp": "mit Fokus auf belastbare, operative Fakten",
    }
    hints = lore_hints if profile == "lore" else ops_hints
    return hints.get(source_kind, hints["rp"])


def _build_training_prompt(title: str, lead: str, source_kind: str, profile: str) -> str:
    focus = _focus_hint(source_kind, profile)
    base = (
        f'Nutze nur belegte RP-SSOT-Fakten aus "{title}" {focus}. '
        "Erfinde keine neuen Orte, Fraktionen, Mengen oder Geheimauftraege. "
    )
    if profile == "lore":
        task = (
            "Formuliere daraus eine kurze, lore-nahe Chronistin-Vorlage fuer einen spaeteren "
            "Trainingsdatensatz."
        )
    else:
        task = (
            "Formuliere daraus eine knappe operative Lage-, Prozess- oder Bestandsvorlage fuer "
            "einen spaeteren Trainingsdatensatz."
        )
    if lead:
        return f"{base}{task} Ausgangspunkt: {lead}"
    return f"{base}{task}"


def collect_rp_training_items(
    rp_root: Path,
    *,
    profile: str,
    limit: int = 120,
    include_globs: list[str] | None = None,
    promotion_level: str = "rp_ssot_reviewed",
    license_scope: str = "internal",
    source_package: str | None = None,
) -> list[RPTrainingItem]:
    globs = include_globs or [DEFAULT_INCLUDE_GLOB]
    files: list[Path] = []
    seen: set[Path] = set()
    for include_glob in globs:
        for path in sorted(rp_root.glob(include_glob)):
            if path in seen or not path.is_file():
                continue
            seen.add(path)
            files.append(path)

    package_name = source_package or f"rp_{profile}_builder.v1"
    items: list[RPTrainingItem] = []
    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        title = _parse_title(text, path.stem.replace("-", " "))
        if not title:
            continue
        lead = _parse_lead(text)
        rel = path.relative_to(rp_root).as_posix()
        source_kind = _derive_source_kind(rel)
        prompt = _build_training_prompt(title, lead, source_kind, profile)
        basis = f"{profile}|{rel}|{title}|{source_kind}"
        short_hash = hashlib.sha1(basis.encode("utf-8")).hexdigest()[:10]
        slug = f"train-rp-{profile}-{_slugify(title)[:32]}-{short_hash}"
        items.append(
            RPTrainingItem(
                item_id=slug,
                slug=slug,
                source_file=rel,
                source_kind=source_kind,
                title=title,
                prompt=prompt,
                profile=profile,
                promotion_level=promotion_level,
                license_scope=license_scope,
                source_package=package_name,
                lead=lead,
            )
        )
        if len(items) >= max(0, int(limit)):
            break

    return items


def write_jsonl(path: Path, records: Iterable[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build RP-derived training seed dataset")
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parents[2]),
        help="Repository root path",
    )
    parser.add_argument(
        "--rp-root",
        default="novapolis-rp/database-rp",
        help="Relative RP source root",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Relative output path (defaults to profile-based training dataset path)",
    )
    parser.add_argument("--profile", choices=["lore", "ops"], default="lore")
    parser.add_argument("--limit", type=int, default=120)
    parser.add_argument(
        "--include-glob",
        action="append",
        default=[],
        help="Repeatable glob below rp-root",
    )
    parser.add_argument("--promotion-level", default="rp_ssot_reviewed")
    parser.add_argument("--license-scope", default="internal")
    parser.add_argument("--source-package", default=None)
    args = parser.parse_args(argv)

    repo_root = Path(args.repo_root).resolve()
    rp_root = (repo_root / args.rp_root).resolve()
    out_rel = args.out or f"novapolis_agent/eval/datasets/training/rp_{args.profile}_train.v1.jsonl"
    out_path = (repo_root / out_rel).resolve()

    if not rp_root.exists():
        print(f"[rp-train-builder] ERROR rp_root not found: {rp_root}")
        return 2

    items = collect_rp_training_items(
        rp_root,
        profile=args.profile,
        limit=args.limit,
        include_globs=args.include_glob or None,
        promotion_level=args.promotion_level,
        license_scope=args.license_scope,
        source_package=args.source_package,
    )
    records = [item.to_record() for item in items]
    write_jsonl(out_path, records)

    print("[rp-train-builder] done")
    print(f"  profile: {args.profile}")
    print(f"  source_root: {rp_root}")
    print(f"  output: {out_path}")
    print(f"  records: {len(records)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())