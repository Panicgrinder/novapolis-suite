#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
import os
from pathlib import Path


LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def normalize_link_target(raw_link: str) -> str | None:
    link = raw_link.strip()
    if not link or link.startswith("#"):
        return None
    if link.lower().startswith(("http://", "https://", "mailto:")):
        return None
    if link.startswith("<") and link.endswith(">"):
        link = link[1:-1].strip()
    link = link.split("#", 1)[0].split("?", 1)[0].strip()
    if not link:
        return None
    return link.replace("\\", "/")


def parse_links(md_text: str) -> set[str]:
    found: set[str] = set()
    for raw in LINK_RE.findall(md_text):
        normalized = normalize_link_target(raw)
        if normalized is not None:
            found.add(normalized)
    return found


def collect_required_links(root: Path, current_state_file: Path) -> tuple[list[str], list[str]]:
    factions_root = root / "novapolis-rp" / "database-rp" / "01-factions"
    current_state_dir = current_state_file.parent

    required: list[str] = []
    errors: list[str] = []

    faction_dirs = sorted([p for p in factions_root.iterdir() if p.is_dir()], key=lambda p: p.name)
    for faction_dir in faction_dirs:
        inventory_readme = faction_dir / "04-inventory" / "README.md"
        missionslogs = sorted((faction_dir / "05-projects").glob("Missionslog-*.md"))

        if not inventory_readme.exists():
            errors.append(f"{faction_dir.name}: fehlendes 04-inventory/README.md")
            continue
        if not missionslogs:
            errors.append(f"{faction_dir.name}: fehlendes Missionslog-*.md unter 05-projects")
            continue

        missionslog = missionslogs[0]
        inventory_rel = os.path.relpath(inventory_readme, current_state_dir).replace("\\", "/")
        missionslog_rel = os.path.relpath(missionslog, current_state_dir).replace("\\", "/")
        required.append(inventory_rel)
        required.append(missionslog_rel)

    return required, errors


def main() -> int:
    root = repo_root()
    current_state = root / "novapolis-rp" / "database-rp" / "00-admin" / "Current-State.md"
    if not current_state.exists():
        print("[current-state-gate] FAIL: Current-State.md fehlt.")
        return 1

    text = current_state.read_text(encoding="utf-8", errors="replace")
    links = parse_links(text)
    required_links, collection_errors = collect_required_links(root, current_state)

    if collection_errors:
        print("[current-state-gate] FAIL: Strukturfehler im Fraktionsbestand:")
        for error in collection_errors:
            print(f" - {error}")
        return 1

    missing_links = [link for link in required_links if link not in links]
    broken_links: list[str] = []
    for link in links:
        link_path = (current_state.parent / link).resolve()
        if link.startswith("../01-factions/") and not link_path.exists():
            broken_links.append(link)

    if missing_links or broken_links:
        print("[current-state-gate] FAIL: Current-State Gate nicht erfüllt.")
        if missing_links:
            print("Fehlende Pflicht-Links:")
            for missing in missing_links:
                print(f" - {missing}")
        if broken_links:
            print("Defekte Fraktions-Links:")
            for broken in sorted(broken_links):
                print(f" - {broken}")
        return 1

    print("[current-state-gate] PASS: Fraktions-Missionslogs und Fraktions-Inventare sind in Current-State referenziert.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
