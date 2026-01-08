"""RP Kanon Sync (MD frontmatter -> JSON mirror).

Ziel:
- JSON-Dateien in database-rp spiegeln die Metadaten aus dem Markdown-Frontmatter.
- Minimal-invasive Fixes:
  - JSON: version als String, last_updated als String (ISO), source konsistent.
  - MD: Entfernt bekannte Doppel-Metablock/Doppel-Frontmatter-Patterns direkt nach dem Frontmatter.
  - MD: last-updated -> last_updated (nur im Frontmatter, falls vorhanden).

Default ist WhatIf (keine Writes). Mit --write werden Änderungen geschrieben.

Hinweis: Parser ist bewusst konservativ und deckt die im Repo verwendeten Frontmatter-Patterns ab.
"""

from __future__ import annotations

import argparse
import json
import re
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any


RP_DIRS = [
    "02-characters",
    "03-locations",
    "04-inventory",
    "05-projects",
    "06-scenes",
]


@dataclass
class Change:
    path: Path
    kind: str  # "md" | "json"
    summary: str


_FRONTMATTER_START = "---"
_FRONTMATTER_END = "---"


def _unquote(value: str) -> str:
    v = value.strip()
    if len(v) >= 2 and ((v[0] == v[-1] == '"') or (v[0] == v[-1] == "'")):
        return v[1:-1]
    return v


def _parse_list_brackets(raw: str) -> list[str] | None:
    v = raw.strip()
    if not (v.startswith("[") and v.endswith("]")):
        return None
    inner = v[1:-1].strip()
    if inner == "":
        return []

    # Split on commas not inside quotes (simple conservative splitter).
    parts: list[str] = []
    buf: list[str] = []
    quote: str | None = None
    for ch in inner:
        if quote is None and ch in ("'", '"'):
            quote = ch
            buf.append(ch)
            continue
        if quote is not None and ch == quote:
            quote = None
            buf.append(ch)
            continue
        if quote is None and ch == ",":
            parts.append("".join(buf).strip())
            buf = []
            continue
        buf.append(ch)
    if buf:
        parts.append("".join(buf).strip())

    out: list[str] = []
    for p in parts:
        if p == "":
            continue
        out.append(_unquote(p.strip()))
    return out


def parse_frontmatter(text: str) -> tuple[dict[str, Any], int, int]:
    """Return (frontmatter_map, start_index, end_index).

    start_index/end_index are character offsets into text where the YAML block including delimiters
    lives:
    text[start_index:end_index].
    Returns ({}, -1, -1) if no frontmatter.
    """

    if not text.startswith(_FRONTMATTER_START + "\n"):
        return {}, -1, -1

    end_marker = "\n" + _FRONTMATTER_END + "\n"
    end_pos = text.find(end_marker, len(_FRONTMATTER_START) + 1)
    if end_pos == -1:
        return {}, -1, -1

    # YAML lines without delimiters.
    yaml_block = text[len(_FRONTMATTER_START) + 1 : end_pos]
    fm: dict[str, Any] = {}
    for line in yaml_block.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^(?P<k>[^:]+):\s*(?P<v>.*)$", line)
        if not m:
            continue
        key = m.group("k").strip()
        raw_val = m.group("v").strip()
        if raw_val == "":
            fm[key] = ""
            continue

        list_val = _parse_list_brackets(raw_val)
        if list_val is not None:
            fm[key] = list_val
        else:
            fm[key] = _unquote(raw_val)

    start_index = 0
    end_index = end_pos + len(end_marker)
    return fm, start_index, end_index


def _detect_duplicate_meta_block(body_after_frontmatter: str) -> tuple[int, int] | None:
    """Detect and return (start,end) offsets inside body_after_frontmatter for a duplicate block.

    Pattern handled:
    - Immediately after frontmatter, a second block of key/value lines ending with '---' exists.
    - OR a second '--- ... ---' frontmatter directly follows.

    Returns None if not found.
    """

    # Skip leading blank lines
    m = re.match(r"^\s*", body_after_frontmatter)
    if not m:
        return None
    scan_start = m.end()
    tail = body_after_frontmatter[scan_start:]

    # Case A: second frontmatter starts immediately
    if tail.startswith(_FRONTMATTER_START + "\n"):
        end_marker = "\n" + _FRONTMATTER_END + "\n"
        end_pos = tail.find(end_marker, len(_FRONTMATTER_START) + 1)
        if end_pos != -1:
            return scan_start, scan_start + end_pos + len(end_marker)

    # Case B: key/value metablock ending with ---
    # We limit search window to avoid touching deeper content.
    window = tail[:4000]
    # Heuristic: metablock starts with one of these keys.
    if not re.match(
        r"^(title|category|slug|version|last_updated|last-updated|tags|affiliations|dependencies|primary_location|last_seen):\s*",
        window,
    ):
        return None

    # Find a terminating line that is exactly '---'
    lines = window.splitlines(keepends=True)
    acc = 0
    end_at: int | None = None
    for ln in lines[:120]:
        acc += len(ln)
        if ln.strip() == _FRONTMATTER_END:
            end_at = acc
            break
    if end_at is None:
        return None

    return scan_start, scan_start + end_at


def _canonical_json_from_frontmatter(
    *,
    fm: dict[str, Any],
    rel_md_path: str,
    existing: dict[str, Any],
) -> dict[str, Any]:
    desired_order = [
        "title",
        "category",
        "slug",
        "version",
        "last_updated",
        "last_change",
        "tags",
        "affiliations",
        "primary_location",
        "last_seen",
        "dependencies",
        "source",
    ]

    # Accept both keys for last_updated from MD.
    last_updated = fm.get("last_updated") or fm.get("last-updated")

    desired: dict[str, Any] = {
        "title": fm.get("title"),
        "category": fm.get("category"),
        "slug": fm.get("slug"),
        "version": fm.get("version"),
        "last_updated": last_updated,
        "last_change": fm.get("last_change"),
        "tags": fm.get("tags"),
        "affiliations": fm.get("affiliations"),
        "primary_location": fm.get("primary_location"),
        "last_seen": fm.get("last_seen"),
        "dependencies": fm.get("dependencies"),
        "source": rel_md_path,
    }

    # Normalize version to string if present.
    if desired.get("version") is not None and desired.get("version") != "":
        desired["version"] = str(desired["version"]).strip()

    # If MD lacks some optional fields, keep existing values (do not delete).
    merged: dict[str, Any] = dict(existing)
    for k, v in desired.items():
        if v is None or v == "":
            continue
        merged[k] = v

    # Ensure source always exists.
    merged["source"] = rel_md_path

    # Ensure last_updated stays a string (if it became non-string from older JSON).
    if "last_updated" in merged and merged["last_updated"] is not None:
        merged["last_updated"] = str(merged["last_updated"])

    # Ensure tags/affiliations/dependencies stay list when possible.
    for k in ("tags", "affiliations", "dependencies"):
        if k in merged and merged[k] is not None and not isinstance(merged[k], list):
            merged[k] = [str(merged[k])]

    # Build ordered dict-like mapping: desired keys first, then extras.
    out: dict[str, Any] = {}
    for k in desired_order:
        if k in merged:
            out[k] = merged[k]
    for k, v in merged.items():
        if k not in out:
            out[k] = v
    return out


def _json_equal(a: dict[str, Any], b: dict[str, Any]) -> bool:
    return json.dumps(a, sort_keys=True, ensure_ascii=False) == json.dumps(
        b, sort_keys=True, ensure_ascii=False
    )


def iter_targets(repo_root: Path) -> Iterable[tuple[Path, Path]]:
    rp_root = repo_root / "novapolis-rp" / "database-rp"
    for d in RP_DIRS:
        folder = rp_root / d
        if not folder.exists():
            continue
        for md_path in sorted(folder.glob("*.md")):
            if md_path.name.lower() == "readme.md":
                continue
            json_path = md_path.with_suffix(".json")
            if json_path.exists():
                yield md_path, json_path


def sync_one(md_path: Path, json_path: Path, *, repo_root: Path, write: bool) -> list[Change]:
    changes: list[Change] = []

    md_text = md_path.read_text(encoding="utf-8", errors="strict")
    fm, fm_start, fm_end = parse_frontmatter(md_text)
    if fm_start == -1:
        return changes

    # MD: last-updated -> last_updated in frontmatter (rename key only).
    if "last-updated" in fm and "last_updated" not in fm:
        # Do a conservative line-based replacement inside frontmatter block.
        frontmatter_text = md_text[fm_start:fm_end]
        new_frontmatter_text = re.sub(
            r"(?m)^last-updated:\s*", "last_updated: ", frontmatter_text
        )
        if new_frontmatter_text != frontmatter_text:
            if write:
                md_text = new_frontmatter_text + md_text[fm_end:]
                md_path.write_text(md_text, encoding="utf-8", newline="\n")
            changes.append(
                Change(md_path, "md", "Frontmatter-Key rename: last-updated -> last_updated")
            )
            # Re-parse after change for downstream sync.
            fm, fm_start, fm_end = parse_frontmatter(md_text)

    # MD: remove duplicate metablock right after frontmatter.
    body = md_text[fm_end:]
    dup = _detect_duplicate_meta_block(body)
    if dup is not None:
        s, e = dup
        new_body = body[:s] + body[e:]
        if new_body != body:
            if write:
                md_text = md_text[:fm_end] + new_body
                md_path.write_text(md_text, encoding="utf-8", newline="\n")
            changes.append(
                Change(
                    md_path,
                    "md",
                    "Removed duplicate meta/frontmatter block after frontmatter",
                )
            )
            # Re-parse for correctness.
            fm, fm_start, fm_end = parse_frontmatter(md_text)

    # JSON sync
    existing_json = json.loads(json_path.read_text(encoding="utf-8"))

    rel_md = md_path.relative_to(repo_root / "novapolis-rp").as_posix()
    # Canon expects paths like database-rp/...
    if not rel_md.startswith("database-rp/"):
        rel_md = "database-rp/" + md_path.relative_to(
            repo_root / "novapolis-rp" / "database-rp"
        ).as_posix()

    desired_json = _canonical_json_from_frontmatter(
        fm=fm, rel_md_path=rel_md, existing=existing_json
    )

    if not _json_equal(existing_json, desired_json):
        if write:
            json_path.write_text(
                json.dumps(desired_json, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
                newline="\n",
            )
        changes.append(
            Change(
                json_path,
                "json",
                "Synced JSON metadata to MD frontmatter (canonical order, types)",
            )
        )

    return changes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write",
        action="store_true",
        help="Apply changes (default: WhatIf / no writes).",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]

    all_changes: list[Change] = []
    for md_path, json_path in iter_targets(repo_root):
        all_changes.extend(sync_one(md_path, json_path, repo_root=repo_root, write=args.write))

    if not all_changes:
        print("RP canon sync: no changes")
        return 0

    by_kind: dict[str, int] = {"md": 0, "json": 0}
    for ch in all_changes:
        by_kind[ch.kind] = by_kind.get(ch.kind, 0) + 1

    mode = "WRITE" if args.write else "WHATIF"
    print(f"RP canon sync ({mode}): {len(all_changes)} change(s) ({by_kind})")
    for ch in all_changes:
        rel = ch.path.relative_to(repo_root)
        print(f"- {ch.kind}: {rel.as_posix()} :: {ch.summary}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
