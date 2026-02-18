---
stand: 2026-02-17 20:50
update: Generierte Artefakte im Staging-Reports-Scope explizit gekennzeichnet.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc DONELOG.md WORKSPACE_STATUS.md todo.root.md novapolis-rp/database-curated/staging/reports/generated-artifacts.md PASS (2026-02-17 20:50); F:/VS-Code-Workspace/Main/.venv/Scripts/python.exe scripts/check_frontmatter.py DONELOG.md WORKSPACE_STATUS.md todo.root.md novapolis-rp/database-curated/staging/reports/generated-artifacts.md PASS (2026-02-17 20:50)
---

Generated Artifacts (Staging Reports)
=====================================

Zweck
-----

Diese Datei markiert report-nahe Dateien unter diesem Ordner als generierte Arbeitsartefakte.

Generierte Muster
-----------------

- delta-*.md
- overlap-*.md
- segment-hash-*.txt
- text-stats*.md
- tagging-*.log

Hinweis
-------

- Diese Artefakte sind fuer Analyse/Review gedacht.
- Loeschung oder Verschiebung nur nach expliziter Freigabe.
- SSOT fuer kuratierte Langzeitdoku bleibt novapolis-dev/docs/process/rp-canvas-rescue/.
