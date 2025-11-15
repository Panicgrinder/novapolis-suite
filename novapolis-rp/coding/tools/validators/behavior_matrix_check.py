#!/usr/bin/env python3
"""Validate behavior signatures in the AI-Behavior-Mapping anchor register."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

ANCHOR_LINE_RE = re.compile(r"^\|\s*([A-Z0-9]+)\s*\|")
SEGMENT_RE = re.compile(r"^[A-Z][0-9]{2}$")
MODIFIER_RE = re.compile(r"^[a-z]+$")
SIGNATURE_CAPTURE_RE = re.compile(
    r"([A-Z0-9]+)\s*=\s*([A-Z][0-9]{2}(?:-[A-Z][0-9]{2})*(?:-[a-z]+)?)"
)
ALLOWED_CLUSTERS = {"O", "E", "M", "N", "C", "S", "L", "T", "P"}
DRIFT_THRESHOLD = 5


@dataclass
class AnchorRecord:
    anchor: str
    entity: str
    kind: str
    signature: str
    source: str
    raw_signature: str


def find_repo_root() -> Path:
    return Path(__file__).resolve().parents[4]


def extract_anchor_table(md_text: str) -> list[AnchorRecord]:
    lines = md_text.splitlines()
    entries: list[AnchorRecord] = []
    in_table = False
    for line in lines:
        if not in_table:
            if line.strip().startswith("| Anchor") and "Signatur" in line:
                in_table = True
            continue
        if line.strip().startswith("| ---"):
            continue
        if not line.strip().startswith("|"):
            break
        cells = [part.strip() for part in line.strip().split("|")[1:-1]]
        if len(cells) < 5:
            continue
        anchor, entity, kind, raw_signature, source = cells[:5]
        signature = raw_signature.split()[0] if raw_signature else ""
        entries.append(AnchorRecord(anchor, entity, kind, signature, source, raw_signature))
    return entries


def validate_signature(record: AnchorRecord) -> list[str]:
    errors: list[str] = []
    signature = record.signature
    anchor = record.anchor
    if not anchor:
        errors.append("Empty anchor code detected")
        return errors
    if not ANCHOR_LINE_RE.match(f"| {anchor} |"):
        errors.append(f"Anchor '{anchor}' verwendet unerwartetes Format")
    if signature.lower() in {"n/a", "unbestimmt", "tbd", "pending"}:
        errors.append(
            f"Anchor '{anchor}' hat keine kuratierte Signatur (gefunden: '{record.raw_signature}')"
        )
        return errors
    parts = signature.split("-")
    if not parts:
        errors.append(f"Anchor '{anchor}' besitzt eine leere Signatur")
        return errors
    modifiers: str | None = None
    if parts and parts[-1].islower():
        modifiers = parts.pop()
        if not MODIFIER_RE.match(modifiers):
            errors.append(f"Anchor '{anchor}' nutzt unbekannte Modifikatoren '{modifiers}'")
    seen_clusters = set()
    for _idx, part in enumerate(parts):
        if not SEGMENT_RE.match(part):
            errors.append(f"Anchor '{anchor}' enthält ungültigen Segmentcode '{part}'")
            continue
        cluster = part[0]
        value = int(part[1:])
        if cluster not in ALLOWED_CLUSTERS:
            errors.append(f"Anchor '{anchor}' nutzt unbekannten Cluster '{cluster}'")
        if not 1 <= value <= 99:
            errors.append(f"Anchor '{anchor}' besitzt Intensität außerhalb 01-99 ('{part}')")
        if cluster in seen_clusters:
            errors.append(f"Anchor '{anchor}' wiederholt Cluster '{cluster}'")
        seen_clusters.add(cluster)
    if not seen_clusters:
        errors.append(f"Anchor '{anchor}' enthält keine validen Cluster-Segmente")
    return errors


def parse_signature_map(signature: str) -> dict[str, int]:
    parts = signature.split("-")
    if parts and parts[-1].islower():
        parts = parts[:-1]
    cluster_map: dict[str, int] = {}
    for part in parts:
        if not SEGMENT_RE.match(part):
            continue
        cluster_map[part[0]] = int(part[1:])
    return cluster_map


def locate_source_path(repo_root: Path, source_cell: str) -> Path | None:
    match = re.search(r"(database-[^\s)]+\.md)", source_cell)
    if not match:
        return None
    rel = Path(match.group(1))
    candidate = repo_root / rel
    if not candidate.exists():
        candidate = repo_root / "novapolis-rp" / rel
    return candidate if candidate.exists() else None


def extract_from_json(node) -> dict[str, str]:
    matches: dict[str, str] = {}
    if isinstance(node, dict):
        anchor = node.get("anchor")
        signature = node.get("signature")
        if (
            isinstance(anchor, str)
            and isinstance(signature, str)
            and SIGNATURE_CAPTURE_RE.match(f"{anchor}={signature}")
        ):
            matches[anchor] = signature
        for value in node.values():
            matches.update(extract_from_json(value))
    elif isinstance(node, list):
        for item in node:
            matches.update(extract_from_json(item))
    return matches


def load_psymatrix_signatures(repo_root: Path) -> tuple[dict[str, str], list[str]]:
    exports_dir = repo_root / "novapolis-rp" / "database-raw" / "99-exports"
    if not exports_dir.exists():
        return {}, []
    candidates = sorted(exports_dir.glob("*ai_psymatrix_index_v1*"))
    hints: list[str] = []
    if not candidates:
        return {}, []
    signatures: dict[str, str] = {}
    for path in candidates:
        text = path.read_text(encoding="utf-8")
        parsed = False
        try:
            data = json.loads(text)
            matches = extract_from_json(data)
            if matches:
                signatures.update(matches)
                parsed = True
        except json.JSONDecodeError:
            pass
        if not parsed:
            matches = {m.group(1): m.group(2) for m in SIGNATURE_CAPTURE_RE.finditer(text)}
            if matches:
                signatures.update(matches)
                parsed = True
        if not parsed:
            hints.append(
                f"Psymatrix-Datei konnte nicht interpretiert werden: {path.relative_to(repo_root)}"
            )
    return signatures, hints


def compare_with_psymatrix(
    anchors: list[AnchorRecord], psymatrix: dict[str, str]
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not psymatrix:
        return errors, warnings

    anchor_lookup = {record.anchor: record for record in anchors}

    for anchor_code, _ps_signature in psymatrix.items():
        if anchor_code not in anchor_lookup:
            warnings.append(f"Psymatrix enthält unbekannten Anchor '{anchor_code}'")

    for record in anchors:
        anchor_code = record.anchor
        anchor_map = parse_signature_map(record.signature)
        ps_signature = psymatrix.get(anchor_code)
        if ps_signature is None:
            errors.append(f"Psymatrix fehlt Eintrag für Anchor '{anchor_code}'")
            continue
        ps_map = parse_signature_map(ps_signature)
        for cluster in sorted(set(anchor_map) | set(ps_map)):
            ref_value = anchor_map.get(cluster)
            ps_value = ps_map.get(cluster)
            if ref_value is None:
                errors.append(
                    f"Anchor '{anchor_code}': Cluster '{cluster}' fehlt im Register "
                    f"(Psymatrix {ps_value:02d})"
                )
                continue
            if ps_value is None:
                errors.append(f"Anchor '{anchor_code}': Cluster '{cluster}' fehlt in der Psymatrix")
                continue
            delta = abs(ref_value - ps_value)
            if delta > DRIFT_THRESHOLD:
                errors.append(
                    f"Anchor '{anchor_code}': Cluster '{cluster}' differiert um {delta} Punkte "
                    f"(Register {ref_value:02d} vs. Psymatrix {ps_value:02d})"
                )
    return errors, warnings


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Prüft das Anchor-Register der AI-Behavior-Mapping-Datei."
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Reserviert für zukünftige JSON-Ausgabe (derzeit ohne Funktion).",
    )
    parser.parse_args(list(argv) if argv is not None else None)

    repo_root = find_repo_root()
    mapping_file = (
        repo_root / "novapolis-rp" / "database-rp" / "00-admin" / "AI-Behavior-Mapping.md"
    )
    if not mapping_file.exists():
        print(f"behavior_matrix_check: Datei nicht gefunden: {mapping_file}", file=sys.stderr)
        return 1

    md_text = mapping_file.read_text(encoding="utf-8")
    anchors = extract_anchor_table(md_text)
    if not anchors:
        print("behavior_matrix_check: Keine Anchor-Daten gefunden.", file=sys.stderr)
        return 1

    errors: list[str] = []
    warnings: list[str] = []

    seen_codes = set()
    for record in anchors:
        if record.anchor in seen_codes:
            errors.append(f"Anchor-Code doppelt vergeben: '{record.anchor}'")
        seen_codes.add(record.anchor)
        errors.extend(validate_signature(record))
        source_path = locate_source_path(repo_root, record.source)
        if source_path and not source_path.exists():
            warnings.append(f"Quelle fehlt: {record.anchor} → {source_path.relative_to(repo_root)}")

    psymatrix_signatures, psymatrix_hints = load_psymatrix_signatures(repo_root)
    warnings.extend(psymatrix_hints)
    if psymatrix_signatures:
        cmp_errors, cmp_warnings = compare_with_psymatrix(anchors, psymatrix_signatures)
        errors.extend(cmp_errors)
        warnings.extend(cmp_warnings)
    else:
        print(
            "Hinweis: ai_psymatrix_index_v1 nicht gefunden oder ohne erkennbare "
            "Signaturen - Abgleich übersprungen."
        )

    if errors:
        print("behavior_matrix_check: FEHLER")
        for msg in errors:
            print(f" - {msg}")
        if warnings:
            print("Hinweise:")
            for hint in warnings:
                print(f" - {hint}")
        return 1

    print(f"behavior_matrix_check: OK ({len(anchors)} Anchors geprüft)")
    for hint in warnings:
        print(f"Warnung: {hint}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
