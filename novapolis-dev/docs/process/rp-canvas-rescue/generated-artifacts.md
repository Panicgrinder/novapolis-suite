---
stand: 2026-02-22 17:31
update: Frontmatter-Checks auf portable Pfadangaben ohne hostgebundene Absolutpfade umgestellt.
checks: ./.venv/Scripts/python.exe scripts/check_portable_paths.py --repo-root . PASS (2026-02-22 17:10)
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
