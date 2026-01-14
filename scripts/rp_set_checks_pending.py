r"""Set checks: PENDING in RP Markdown frontmatter.

Why:
- RP receipts are stamped only when checks is exactly PENDING (see rp_receipt_pending_checks.py).
- Editing RP files should invalidate prior receipts without relying on brittle exact-line patches.

Safety goals:
- Only touches files under novapolis-rp/database-rp.
- Only rewrites stand/update/checks keys inside the first frontmatter block.
- Does not attempt to parse full YAML; line-based, minimal dependencies.

Usage:
    & .\.venv\Scripts\python.exe scripts\rp_set_checks_pending.py --stand "YYYY-MM-DD HH:mm" \
        --paths <one or more repo-relative paths>

Notes:
- If a file has no checks key, it will be inserted after update
    (or after stand if update is missing).
- If a file has checks already set to PENDING (any quoting), it is left as-is.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

_FRONTMATTER_RE = re.compile(r"\A---\r?\n(?P<body>.*?)(?:\r?\n)---\r?\n", re.DOTALL)
_CHECKS_PENDING_RE = re.compile(r"^checks:\s*(?:\"PENDING\"|'PENDING'|PENDING)\s*$")


@dataclass(frozen=True)
class PendingResult:
    path: Path
    changed: bool
    reason: str


def _set_pending(text: str, *, stand: str) -> tuple[str, bool, str]:
    m = _FRONTMATTER_RE.search(text)
    if not m:
        return text, False, "no_frontmatter"

    body = m.group("body")
    lines = body.splitlines()

    # If any checks line is already PENDING, we still allow stand update but keep checks.
    checks_index: int | None = None
    for i, line in enumerate(lines):
        if line.strip().startswith("checks:"):
            checks_index = i
            break

    already_pending = False
    for line in lines:
        if _CHECKS_PENDING_RE.match(line.strip()):
            already_pending = True
            break

    out: list[str] = []
    saw_stand = False
    saw_update = False

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("stand:"):
            out.append(f"stand: {stand}")
            saw_stand = True
            continue

        if stripped.startswith("update:"):
            out.append(line)
            saw_update = True
            continue

        if stripped.startswith("checks:"):
            if already_pending:
                out.append(line)
                continue
            out.append("checks: PENDING")
            continue

        out.append(line)

    if not saw_stand:
        out.insert(0, f"stand: {stand}")

    if checks_index is None:
        # Insert checks after update if possible, else after stand.
        insert_at = 0
        if out and out[0].startswith("stand:"):
            insert_at = 1
        if saw_update:
            for i, line in enumerate(out):
                if line.strip().startswith("update:"):
                    insert_at = i + 1
                    break
        out.insert(insert_at, "checks: PENDING")

    new_body = "\n".join(out)
    new_text = text[: m.start("body")] + new_body + text[m.end("body") :]

    changed = new_text != text
    return new_text, changed, "pending_set" if changed else "noop"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Set checks: PENDING for selected RP markdown files"
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
        "--paths",
        nargs="+",
        required=True,
        help="One or more repo-relative paths to .md files",
    )
    parser.add_argument("--dry-run", action="store_true", help="Do not write files; just report")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    rp_root = (repo_root / "novapolis-rp" / "database-rp").resolve()
    if not rp_root.exists():
        raise SystemExit(f"RP root not found: {rp_root}")

    results: list[PendingResult] = []

    for rel in args.paths:
        rel_path = Path(rel)
        abs_path = (repo_root / rel_path).resolve()

        if abs_path.suffix.lower() != ".md":
            raise SystemExit(f"Not a markdown file: {rel}")
        if rp_root not in abs_path.parents:
            raise SystemExit(f"Refusing to touch non-RP path: {rel}")
        if not abs_path.exists():
            raise SystemExit(f"File not found: {rel}")

        text = abs_path.read_text(encoding="utf-8")
        new_text, changed, reason = _set_pending(text, stand=args.stand)
        if changed and not args.dry_run:
            abs_path.write_text(new_text, encoding="utf-8", newline="\n")
        results.append(PendingResult(path=abs_path, changed=changed, reason=reason))

    changed = [r for r in results if r.changed]
    print(f"Scanned: {len(results)} file(s)")
    print(f"Changed: {len(changed)} file(s)")
    for r in changed:
        print(f"- {r.path.relative_to(repo_root).as_posix()}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
