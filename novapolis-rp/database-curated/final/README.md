---
stand: 2026-02-01 14:14
update: Hinweis auf FinalGate-Records (staging) ergänzt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-02-01 14:14); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\database-curated PASS (2026-02-01 14:14); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-01 14:14)
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
- Promotion-Entscheidungen/Checklisten liegen pro Export als `database-curated/staging/<export>.finalgate.md`.
- Wenn `final/` nicht genutzt werden soll, muss stattdessen die Dokumentation im Dev-Hub angepasst werden.
