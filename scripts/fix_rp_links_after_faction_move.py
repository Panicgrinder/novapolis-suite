#!/usr/bin/env python3
"""fix_rp_links_after_faction_move.py

Targeted post-migration fix:
- Files moved to `database-rp/01-factions/<faction>/<category>/...` are one level deeper than before.
- Links that previously used `../00-admin/...` now need `../../00-admin/...`.

This script rewrites only Markdown link targets (inside `](...)`) for those paths.

Usage:
  & .\\.venv\\Scripts\\python.exe scripts\\fix_rp_links_after_faction_move.py

Exit codes:
- 0 success
"""

from __future__ import annotations

import re
from pathlib import Path

ENC = "utf-8"

CATEGORY_DIRS = ("02-characters", "03-locations", "04-inventory", "05-projects")

# Only rewrite inside markdown link targets.
LINK_RE = re.compile(r"(\]\()([^)]*)(\))")


def resolve_repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def main() -> int:
    repo_root = resolve_repo_root()
    rp_root = repo_root / "novapolis-rp" / "database-rp"

    changed = 0
    scanned = 0

    for cat in CATEGORY_DIRS:
        for md in rp_root.glob(f"01-factions/*/{cat}/**/*.md"):
            scanned += 1
            text = md.read_text(encoding=ENC, errors="replace")

            def repl(m: re.Match[str]) -> str:
                prefix, target, suffix = m.group(1), m.group(2), m.group(3)
                # Only adjust the specific relative admin reference.
                if target.startswith("../00-admin/"):
                    target = "../../../00-admin/" + target[len("../00-admin/") :]
                elif target.startswith("../../00-admin/"):
                    target = "../../../00-admin/" + target[len("../../00-admin/") :]
                return prefix + target + suffix

            new_text = LINK_RE.sub(repl, text)
            if new_text != text:
                md.write_text(new_text, encoding=ENC)
                changed += 1

    print(f"Scanned: {scanned}")
    print(f"Changed: {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
