---
stand: 2026-03-10 13:14
update: Inventar und Guard-Regeln fuer archivierte Legacy-Shims eingefuehrt; `novapolis_agent.app.utils.examples` auf kanonischen Top-Level-Shim entkoppelt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis_agent/docs/legacy-shim-inventory.md' 'novapolis_agent/docs/runbook.md' 'novapolis-dev/docs/todo.agent-board.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'novapolis_agent/docs/DONELOG.txt' PASS (2026-03-10 12:59); .\.venv\Scripts\python.exe scripts/check_frontmatter.py 'novapolis_agent/docs/legacy-shim-inventory.md' 'novapolis_agent/docs/runbook.md' 'novapolis-dev/docs/todo.agent-board.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'novapolis_agent/docs/DONELOG.txt' PASS (EXITCODE=0, 2026-03-10 12:59)
---

Legacy Shim Inventory (Agent)
=============================

Ziel
----

- Transparente Uebersicht ueber archivierte Legacy-Shims.
- Klare Guard-Regel, damit neue produktive Importe auf archivierte Pfade frueh auffallen.

Aktive archivierte Shim-Pfade
-----------------------------

- `app.api.api` -> archiviert unter `novapolis_agent/archive/app/api/api.py`
- `app.prompt` -> archiviert unter `novapolis_agent/archive/app/prompt`
- `app.utils.examples` -> archiviert unter `novapolis_agent/archive/app/utils/examples`

Kompatibilitaetslayer (`novapolis_agent.app.*`)
------------------------------------------------

- Der Spiegelpfad `novapolis_agent.app.utils.examples` ist auf den kanonischen
  Top-Level-Shim `app.utils.examples` entkoppelt (keine eigene Archivlogik mehr).

Verbleibende erlaubte Importstellen
-----------------------------------

- Tests, die explizit das erwartete `ModuleNotFoundError` absichern:
  - `novapolis_agent/tests/test_module_exports.py`

Guard-Check
-----------

- Skript: `novapolis_agent/scripts/check_legacy_shim_imports.py`
- Standardmodus: zeigt Treffer, Exitcode bleibt 0.
- Strict-Modus: bei nicht-erlaubten Treffern Exitcode 1.

Aufrufbeispiel:

```powershell
..\.venv\Scripts\python.exe scripts\check_legacy_shim_imports.py --strict
```
