---
stand: 2026-01-11 03:44
update: checks aktualisiert (Basis-Stabilisierung)
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-01-11 03:44); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-dev\README.md novapolis-dev\migrations\docs-migration-2025-10-29.md novapolis-dev\integrations\mcp-openai-eval\README.md PASS (2026-01-11 03:44)
---
Docs-Migration 2025-10-29
=========================

| Datum       | Alter Pfad                              | Neuer Pfad                                   | Bemerkung                                                   |
|-------------|-----------------------------------------|----------------------------------------------|-------------------------------------------------------------|
| 2025-10-29  | legacy coding · donelog.md              | novapolis-dev/docs/donelog.md                | Inhalte unverändert übernommen; Herkunftsvermerk ergänzt.   |
| 2025-10-29  | legacy coding · donelog.json            | novapolis-dev/docs/meta/donelog.json         | `source` aktualisiert, Feld `origin` ergänzt.               |
| 2025-10-29  | legacy coding · todo.md                 | novapolis-dev/docs/todo.md                   | Aufgaben neu gruppiert (Actionables oben).                  |
| 2025-10-29  | legacy coding · todo.json               | novapolis-dev/docs/meta/todo.json            | `source` aktualisiert, Feld `origin` ergänzt.               |
| 2025-10-29  | legacy coding · copilot-behavior.md     | novapolis-dev/docs/copilot-behavior.md       | Referenzen auf neue Pfade gesetzt, Kommentar hinzugefügt.   |
| 2025-10-29  | legacy coding · copilot-behavior.json   | novapolis-dev/docs/meta/copilot-behavior.json| `source` aktualisiert, Feld `origin` ergänzt.               |
| 2025-10-29  | legacy coding · INDEX.md                | novapolis-dev/docs/index.md                  | Inhalt an neue Struktur angepasst.                          |
| 2025-10-29  | legacy coding · INDEX.json              | novapolis-dev/docs/meta/index.json           | `source` aktualisiert, Feld `origin` ergänzt.               |
| 2025-10-29  | legacy coding · naming-policy.md        | novapolis-dev/docs/naming-policy.md          | Format auf setext-Überschriften umgestellt.                 |
| 2025-10-29  | legacy coding · naming-policy.json      | novapolis-dev/docs/meta/naming-policy.json   | `source` aktualisiert, Feld `origin` ergänzt.               |
| 2025-10-29  | -                                       | novapolis-dev/docs/tests.md                  | Neu angelegt: Testübersicht + Mini-Prequel-Testplan.        |

Hinweise
--------

- Originaldateien unter `coding/` bleiben bestehen, bis die Aufräumfreigabe erfolgt.
- Weitere Datenmigrationen (Roh- und Kurationsdaten) folgen in separaten Protokollen.


