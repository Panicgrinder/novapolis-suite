---
stand: 2026-02-22 16:51
update: Installhinweis präzisiert; Root-pyproject ist tools-only und Shared-Pakete werden explizit als Editable installiert.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/README.md' 'packages/README.md' 'todo.root.md' 'DONELOG.md' 'WORKSPACE_STATUS.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-22 15:47); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'novapolis-rp/README.md' 'packages/README.md' 'todo.root.md' 'DONELOG.md' 'WORKSPACE_STATUS.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-22 15:47)
---

Shared packages
===============

Put reusable Python code here. The root `pyproject.toml` is tools-only, so shared packages under this directory are installed explicitly as editable packages (for example `pip install -e packages/novapolis_common`). Subfolders should expose proper packages (with `__init__.py`) so that callers from `novapolis_agent` or `novapolis-rp` can import them once the duplicates have been migrated.

