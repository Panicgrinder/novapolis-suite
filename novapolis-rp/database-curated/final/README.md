---
stand: 2026-01-11 03:44
update: checks aktualisiert (Basis-Stabilisierung)
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-01-11 03:44); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\database-curated\README.md novapolis-rp\database-curated\final\README.md PASS (2026-01-11 03:44)
---

Final (Platzhalter)
==================

Dieser Ordner ist aktuell ein Platzhalter, weil der Workflow in den Dev-Hub-Dokumenten `database-curated/final/` referenziert.

Konvention (vorläufig)
----------------------

- `staging/` bleibt der Arbeitsbereich (unvollständig/Review).
- `final/` ist für freigegebene, „finale“ kuratierte Artefakte gedacht.

Hinweis
-------

- SSOT für RP-Inhalte bleibt `novapolis-rp/database-rp/`.
- Wenn `final/` nicht genutzt werden soll, muss stattdessen die Dokumentation im Dev-Hub angepasst werden.
