"""Stamp PASS receipts into RP Markdown files that still have checks: PENDING.

Safety goals:
- Only touches files under novapolis-rp/database-rp.
- Only updates files whose *frontmatter* contains exactly checks: PENDING (optionally quoted).
- Only rewrites stand/update/checks keys inside the first frontmatter block.

This script intentionally avoids parsing full YAML; it operates line-based to minimize dependencies.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

_FRONTMATTER_RE = re.compile(r"\A---\r?\n(?P<body>.*?)(?:\r?\n)---\r?\n", re.DOTALL)
_CHECKS_PENDING_RE = re.compile(r"^checks:\s*(?:\"PENDING\"|'PENDING'|PENDING)\s*$")


@dataclass(frozen=True)
class StampResult:
    path: Path
    changed: bool
    reason: str


def _stamp_frontmatter(text: str, *, stand: str, receipt: str) -> tuple[str, bool, str]:
    m = _FRONTMATTER_RE.search(text)
    if not m:
        return text, False, "no_frontmatter"

    body = m.group("body")
    lines = body.splitlines()

    checks_index: int | None = None
    for i, line in enumerate(lines):
        if _CHECKS_PENDING_RE.match(line.strip()):
            checks_index = i
            break

    if checks_index is None:
        return text, False, "checks_not_pending"

    out_lines: list[str] = []
    saw_stand = False
    update_value: str | None = None

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("stand:"):
            out_lines.append(f"stand: {stand}")
            saw_stand = True
            continue

        if stripped.startswith("update:"):
            # Preserve original update, but append a short receipt note once.
            raw_value = line.split(":", 1)[1].strip()
            update_value = raw_value
            continue

        if stripped.startswith("checks:"):
            # Replaced later (only if PENDING matched).
            out_lines.append(line)
            continue

        out_lines.append(line)

    if update_value is None:
        update_value = "Checks receipted."

    # Normalize update value: avoid double-appending.
    if (
        re.search(r"\bChecks\b.*\bPASS\b", update_value, flags=re.IGNORECASE) is None
        and re.search(r"\breceipt(ed)?\b", update_value, flags=re.IGNORECASE) is None
    ):
        if update_value.endswith('"') and update_value.startswith('"'):
            # Remove surrounding quotes for controlled re-quoting.
            unquoted = update_value[1:-1]
            update_value = f'"{unquoted}; Checks PASS."'
        elif update_value.endswith("'") and update_value.startswith("'"):
            unquoted = update_value[1:-1]
            update_value = f"'{unquoted}; Checks PASS.'"
        else:
            update_value = f"{update_value}; Checks PASS."

    # Insert/replace update line at original position.
    # If we saw an update line, it was skipped above; we need to re-add it where it appeared.
    # Simplest: rebuild again, replacing stand/checks and re-emitting update inline.
    rebuilt: list[str] = []
    update_emitted = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("stand:"):
            rebuilt.append(f"stand: {stand}")
            continue
        if stripped.startswith("update:"):
            rebuilt.append(f"update: {update_value}")
            update_emitted = True
            continue
        if _CHECKS_PENDING_RE.match(stripped):
            rebuilt.append(f"checks: {receipt}")
            continue
        rebuilt.append(line)

    if not saw_stand:
        rebuilt.insert(0, f"stand: {stand}")
    if not update_emitted:
        # Place update after stand if it didn't exist.
        insert_at = 1 if rebuilt and rebuilt[0].startswith("stand:") else 0
        rebuilt.insert(insert_at, f"update: {update_value}")

    new_body = "\n".join(rebuilt)
    new_text = text[: m.start("body")] + new_body + text[m.end("body") :]
    return new_text, True, "stamped"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Stamp PASS receipts into RP Markdown files with checks: PENDING"
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="Repository root (default: cwd)",
    )
    parser.add_argument(
        "--stand",
        required=True,
        help="Value for frontmatter stand (YYYY-MM-DD HH:mm)",
    )
    parser.add_argument(
        "--receipt",
        required=True,
        help="Value for frontmatter checks (receipt string)",
    )
    parser.add_argument("--dry-run", action="store_true", help="Do not write files; just report")
    args = parser.parse_args()

    rp_root = (args.repo_root / "novapolis-rp" / "database-rp").resolve()
    if not rp_root.exists():
        raise SystemExit(f"RP root not found: {rp_root}")

    results: list[StampResult] = []
    for path in sorted(rp_root.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        new_text, changed, reason = _stamp_frontmatter(text, stand=args.stand, receipt=args.receipt)
        if changed and not args.dry_run:
            path.write_text(new_text, encoding="utf-8", newline="\n")
        results.append(StampResult(path=path, changed=changed, reason=reason))

    changed = [r for r in results if r.changed]
    print(f"Scanned: {len(results)} markdown file(s)")
    print(f"Changed: {len(changed)} file(s)")

    # Optional: list changed files for auditability.
    for r in changed:
        rel = r.path.relative_to(args.repo_root)
        print(f"- {rel.as_posix()}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
