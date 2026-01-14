r"""Generate RP character SSOTs (Markdown + JSON sidecars).

This generator is intentionally deterministic and conservative:
- Only writes new files (refuses to overwrite by default).
- Validates that slugs are unique across novapolis-rp/database-rp.
- Uses minimal, SSOT-compatible frontmatter fields.

Usage (PowerShell):
    & .\.venv\Scripts\python.exe scripts\generate_rp_character_batch.py --stand "YYYY-MM-DD HH:mm" \
        --last-updated "YYYY-MM-DDTHH:mm:00+01:00" --write

"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path

_SLUG_RE = re.compile(r"^slug:\s*(?P<slug>[^\s#]+)\s*$", re.MULTILINE)


@dataclass(frozen=True)
class CharacterSpec:
    name: str
    slug: str
    faction_slug: str  # folder under 01-factions
    filename: str
    affiliations: list[str]
    primary_location: str
    last_seen: str
    tags: list[str]
    dependencies: list[str]
    role: str
    personality: str
    hook: str


def _collect_existing_slugs(rp_root: Path) -> set[str]:
    slugs: set[str] = set()
    for path in rp_root.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        m = _SLUG_RE.search(text)
        if m:
            slugs.add(m.group("slug").strip())
    return slugs


def _write_file(path: Path, content: str, *, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise SystemExit(f"Refusing to overwrite existing file: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def _md_for(spec: CharacterSpec, *, stand: str, last_updated: str) -> str:
    tags = ", ".join(f'"{t}"' for t in spec.tags)
    affiliations = ", ".join(f'"{a}"' for a in spec.affiliations)
    dependencies = ", ".join(f'"{d}"' for d in spec.dependencies)

    return (
        "---\n"
        f"stand: {stand}\n"
        f'update: "Neu: Charakter-SSOT angelegt ({spec.slug})."\n'
        "checks: PENDING\n\n"
        f"title: {spec.name}\n"
        "category: character\n"
        f"slug: {spec.slug}\n"
        'version: "0.1"\n'
        f"last_updated: {last_updated}\n"
        f"tags: [{tags}]\n"
        f"affiliations: [{affiliations}]\n"
        f"dependencies: [{dependencies}]\n"
        f"primary_location: {spec.primary_location}\n"
        f"last_seen: {spec.last_seen}\n"
        "---\n\n"
        "<!-- markdownlint-disable MD025 -->\n\n"
        f"{spec.name}\n"
        "=====\n\n"
        f"- Rolle: {spec.role}\n"
        f"- Persönlichkeit: {spec.personality}\n"
        f"- Hook: {spec.hook}\n"
        "\n"
        "Rollen & Verantwortlichkeiten (Pflichtfelder)\n"
        "---------------------------------------------\n"
        f"- {spec.role}\n\n"
        "Zugehörigkeit & Standort\n"
        "------------------------\n"
        f"- Zugehörigkeit: {', '.join(spec.affiliations)}\n"
        "- Status: aktiv\n"
        f"- Letzter bekannter Einsatzort: {spec.last_seen.upper()}\n"
    )


def _json_for(spec: CharacterSpec, *, last_updated: str, source: str) -> str:
    payload = {
        "title": spec.name,
        "category": "character",
        "slug": spec.slug,
        "version": "0.1",
        "last_updated": last_updated,
        "tags": spec.tags,
        "affiliations": spec.affiliations,
        "primary_location": spec.primary_location,
        "last_seen": spec.last_seen,
        "dependencies": spec.dependencies,
        "source": source,
    }
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def _build_specs() -> list[CharacterSpec]:
    # 20 Evakuierte aus E3 (inkl. Marei) existieren kanonisch,
    # aber Marei ist bereits als SSOT vorhanden.
    # Hier erzeugen wir die 19 weiteren Personen als eigene Charakter-SSOTs.
    evakuierte: list[CharacterSpec] = [
        CharacterSpec(
            name="Iva Kern",
            slug="iva-kern",
            faction_slug="novapolis",
            filename="Iva-Kern",
            affiliations=["novapolis", "e3", "c6"],
            primary_location="c6",
            last_seen="c6",
            tags=["evakuierte", "e3", "c6"],
            dependencies=["c6-bewohner", "marei", "c6", "e3", "logistik"],
            role="Sanität (Basis)",
            personality="direkt, pragmatisch, warmherzig",
            hook="Erkennt Stress früh und fordert klare Zuständigkeiten.",
        ),
        CharacterSpec(
            name="Bastian Ruehl",
            slug="bastian-ruehl",
            faction_slug="novapolis",
            filename="Bastian-Ruehl",
            affiliations=["novapolis", "e3", "c6"],
            primary_location="c6",
            last_seen="c6",
            tags=["evakuierte", "e3", "c6"],
            dependencies=["c6-bewohner", "marei", "c6", "e3"],
            role="Instandhaltung (Leitungen)",
            personality="vorsichtig, detailfixiert, loyal",
            hook="Hat Angst vor erneutem Blackout; prüft alles doppelt.",
        ),
        CharacterSpec(
            name="Selma Varga",
            slug="selma-varga",
            faction_slug="novapolis",
            filename="Selma-Varga",
            affiliations=["novapolis", "e3", "c6"],
            primary_location="c6",
            last_seen="c6",
            tags=["evakuierte", "e3", "c6"],
            dependencies=["c6-bewohner", "c6", "logistik"],
            role="Verpflegung/Planung",
            personality="humorarm, effizient, konsequent",
            hook="Will Vorräte zählen dürfen, nicht 'gefühlt' verteilen.",
        ),
        CharacterSpec(
            name="Nino Jaspers",
            slug="nino-jaspers",
            faction_slug="novapolis",
            filename="Nino-Jaspers",
            affiliations=["novapolis", "e3", "c6"],
            primary_location="c6",
            last_seen="c6",
            tags=["evakuierte", "e3", "c6"],
            dependencies=["c6-bewohner", "c6"],
            role="Runner/Botengänge",
            personality="neugierig, schnell, leichtsinnig",
            hook="Kennt Abkürzungen; muss gebremst werden.",
        ),
        CharacterSpec(
            name="Anouk Seidel",
            slug="anouk-seidel",
            faction_slug="novapolis",
            filename="Anouk-Seidel",
            affiliations=["novapolis", "e3", "c6"],
            primary_location="c6",
            last_seen="c6",
            tags=["evakuierte", "e3", "c6"],
            dependencies=["c6-bewohner", "c6", "e3"],
            role="Wasser/Filter",
            personality="geduldig, methodisch, skeptisch",
            hook="Fragt nach Messwerten, bevor sie zusagt.",
        ),
        CharacterSpec(
            name="Farid Qamar",
            slug="farid-qamar",
            faction_slug="novapolis",
            filename="Farid-Qamar",
            affiliations=["novapolis", "e3", "c6"],
            primary_location="c6",
            last_seen="c6",
            tags=["evakuierte", "e3", "c6"],
            dependencies=["c6-bewohner", "c6", "logistik"],
            role="Strom/Ladefenster",
            personality="gelassen, lösungsorientiert, stur",
            hook="Verteidigt 'seine' Ladezeiten gegen Eingriffe.",
        ),
        CharacterSpec(
            name="Rika Malm",
            slug="rika-malm",
            faction_slug="novapolis",
            filename="Rika-Malm",
            affiliations=["novapolis", "e3", "c6"],
            primary_location="c6",
            last_seen="c6",
            tags=["evakuierte", "e3", "c6"],
            dependencies=["c6-bewohner", "c6"],
            role="Küche/Improvisation",
            personality="kreativ, empfindsam, energiegeladen",
            hook="Macht aus Resten Gerichte; Trigger bei Gerüchen.",
        ),
        CharacterSpec(
            name="Hagen Dittmar",
            slug="hagen-dittmar",
            faction_slug="novapolis",
            filename="Hagen-Dittmar",
            affiliations=["novapolis", "e3", "c6"],
            primary_location="c6",
            last_seen="c6",
            tags=["evakuierte", "e3", "c6"],
            dependencies=["c6-bewohner", "c6"],
            role="Lager/Transport",
            personality="wortkarg, kräftig, zuverlässig",
            hook="Arbeitet am liebsten nachts; meidet Menschenmengen.",
        ),
        CharacterSpec(
            name="Leena Roos",
            slug="leena-roos",
            faction_slug="novapolis",
            filename="Leena-Roos",
            affiliations=["novapolis", "e3", "c6"],
            primary_location="c6",
            last_seen="c6",
            tags=["evakuierte", "e3", "c6"],
            dependencies=["c6-bewohner", "c6"],
            role="Ruhezone/Betreuung",
            personality="sanft, beharrlich, aufmerksam",
            hook="Deeskaliert Konflikte und fordert Rückzugsorte.",
        ),
        CharacterSpec(
            name="Milan Tarek",
            slug="milan-tarek",
            faction_slug="novapolis",
            filename="Milan-Tarek",
            affiliations=["novapolis", "e3", "c6"],
            primary_location="c6",
            last_seen="c6",
            tags=["evakuierte", "e3", "c6"],
            dependencies=["c6-bewohner", "marei", "c6"],
            role="Funk/Notizen",
            personality="nervös, klug, misstrauisch",
            hook="Dokumentiert alles; braucht Freigabe-Rituale.",
        ),
        CharacterSpec(
            name="Jule Benning",
            slug="jule-benning",
            faction_slug="novapolis",
            filename="Jule-Benning",
            affiliations=["novapolis", "e3", "c6"],
            primary_location="c6",
            last_seen="c6",
            tags=["evakuierte", "e3", "c6"],
            dependencies=["c6-bewohner", "c6"],
            role="Reparatur (klein)",
            personality="pfiffig, stolz, ungeduldig",
            hook="Will ernst genommen werden; hasst 'Schonung'.",
        ),
        CharacterSpec(
            name="Orhan Velik",
            slug="orhan-velik",
            faction_slug="novapolis",
            filename="Orhan-Velik",
            affiliations=["novapolis", "e3", "c6"],
            primary_location="c6",
            last_seen="c6",
            tags=["evakuierte", "e3", "c6"],
            dependencies=["c6-bewohner", "c6"],
            role="Sicherheit (Wache)",
            personality="wachsam, höflich, kompromisslos",
            hook="Reagiert schlecht auf unklare Regeln.",
        ),
        CharacterSpec(
            name="Pia Lentz",
            slug="pia-lentz",
            faction_slug="novapolis",
            filename="Pia-Lentz",
            affiliations=["novapolis", "e3", "c6"],
            primary_location="c6",
            last_seen="c6",
            tags=["evakuierte", "e3", "c6"],
            dependencies=["c6-bewohner", "c6"],
            role="Hygiene/Quarantäne",
            personality="streng, fürsorglich, prinzipientreu",
            hook="Setzt Standards durch; wird bei Schlamperei kalt.",
        ),
        CharacterSpec(
            name="Sora Min",
            slug="sora-min",
            faction_slug="novapolis",
            filename="Sora-Min",
            affiliations=["novapolis", "e3", "c6"],
            primary_location="c6",
            last_seen="c6",
            tags=["evakuierte", "e3", "c6"],
            dependencies=["c6-bewohner", "logistik", "c6"],
            role="Daten/Inventar",
            personality="still, analytisch, loyal",
            hook="Baut Listen; möchte Zugriff auf die Logistik-Policy.",
        ),
        CharacterSpec(
            name="Viktor Lahn",
            slug="viktor-lahn",
            faction_slug="novapolis",
            filename="Viktor-Lahn",
            affiliations=["novapolis", "e3", "c6"],
            primary_location="c6",
            last_seen="c6",
            tags=["evakuierte", "e3", "c6"],
            dependencies=["c6-bewohner", "marei", "c6"],
            role="Schichtkoordination (unter Marei)",
            personality="dominant, zuverlässig, reizbar",
            hook="Will klare Ansagen; Konfliktpotenzial in Stresslagen.",
        ),
        CharacterSpec(
            name="Elif Nader",
            slug="elif-nader",
            faction_slug="novapolis",
            filename="Elif-Nader",
            affiliations=["novapolis", "e3", "c6"],
            primary_location="c6",
            last_seen="c6",
            tags=["evakuierte", "e3", "c6"],
            dependencies=["c6-bewohner", "c6"],
            role="Reparatur (Feinmechanik)",
            personality="ruhig, konzentriert, stolz",
            hook="Arbeitet an Ventilen/Fittings; mag keine Hektik.",
        ),
        CharacterSpec(
            name="Timo Bracht",
            slug="timo-bracht",
            faction_slug="novapolis",
            filename="Timo-Bracht",
            affiliations=["novapolis", "e3", "c6"],
            primary_location="c6",
            last_seen="c6",
            tags=["evakuierte", "e3", "c6"],
            dependencies=["c6-bewohner", "c6"],
            role="Entsorgung/Filterwechsel",
            personality="zäh, freundlich, abergläubisch",
            hook="Glaubt an 'Tunnelzeichen' und kann Unruhe auslösen.",
        ),
        CharacterSpec(
            name="Amira Halden",
            slug="amira-halden",
            faction_slug="novapolis",
            filename="Amira-Halden",
            affiliations=["novapolis", "e3", "c6"],
            primary_location="c6",
            last_seen="c6",
            tags=["evakuierte", "e3", "c6"],
            dependencies=["c6-bewohner", "marei", "c6"],
            role="Betreuung/Versorgung",
            personality="empathisch, erschöpft, mutig",
            hook="Setzt sich für Schwache ein, braucht aber feste Pausen.",
        ),
        CharacterSpec(
            name="Kian Rohde",
            slug="kian-rohde",
            faction_slug="novapolis",
            filename="Kian-Rohde",
            affiliations=["novapolis", "e3", "c6"],
            primary_location="c6",
            last_seen="c6",
            tags=["evakuierte", "e3", "c6"],
            dependencies=["c6-bewohner", "c6"],
            role="Materialkunde",
            personality="offen, lernbegierig, respektvoll",
            hook="Will von Kora/Ronja lernen, 'wie es läuft'.",
        ),
    ]

    # 6. Karawanenmitglied (Händlerbund, H-47) - neu, damit Karawane=6 auch als SSOT belegbar ist.
    caravan = CharacterSpec(
        name="Darian Voss",
        slug="darian-voss",
        faction_slug="haendlerbund",
        filename="Darian-Voss",
        affiliations=["haendlerbund"],
        primary_location="g7",
        last_seen="g7",
        tags=["karawane", "haendlerbund"],
        dependencies=["caravan_moves", "g7", "missionslog", "logistik"],
        role="Konvoi-Sicherheit / Scouts (H-47)",
        personality="wachsam, trocken, loyal",
        hook="Sichert Übergaben, erkennt Muster in Überfällen und drängt auf klare Rückzugspläne.",
    )

    return [*evakuierte, caravan]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stand", required=True, help="Frontmatter stand (YYYY-MM-DD HH:mm)")
    parser.add_argument(
        "--last-updated",
        required=True,
        help="Frontmatter last_updated (ISO, e.g. 2026-01-14T14:04:00+01:00)",
    )
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    repo_root: Path = args.repo_root.resolve()
    rp_root = (repo_root / "novapolis-rp" / "database-rp").resolve()

    if not rp_root.exists():
        raise SystemExit(f"RP root not found: {rp_root}")

    specs = _build_specs()

    existing_slugs = _collect_existing_slugs(rp_root)
    new_slugs = [s.slug for s in specs]

    duplicates = [s for s in new_slugs if s in existing_slugs]
    if duplicates:
        raise SystemExit(f"Slug collision(s) detected: {sorted(set(duplicates))}")

    md_paths: list[Path] = []
    json_paths: list[Path] = []

    for spec in specs:
        base_dir = rp_root / "01-factions" / spec.faction_slug / "02-characters"
        md_path = base_dir / f"{spec.filename}.md"
        json_path = base_dir / f"{spec.filename}.json"

        rel_source = (
            Path("database-rp")
            / "01-factions"
            / spec.faction_slug
            / "02-characters"
            / f"{spec.filename}.md"
        ).as_posix()

        md_content = _md_for(spec, stand=args.stand, last_updated=args.last_updated)
        json_content = _json_for(spec, last_updated=args.last_updated, source=rel_source)

        md_paths.append(md_path)
        json_paths.append(json_path)

        if args.write:
            _write_file(md_path, md_content, overwrite=args.overwrite)
            _write_file(json_path, json_content, overwrite=args.overwrite)

    if not args.write:
        print("DRY-RUN (no files written)")

    print(f"Specs: {len(specs)}")
    print(f"Would write: {len(md_paths)} markdown + {len(json_paths)} json")
    for p in md_paths:
        print(f"- {p.relative_to(repo_root).as_posix()}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
