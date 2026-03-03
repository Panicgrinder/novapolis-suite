---
stand: 2026-03-03 14:32
update: Repo-weite Naming-SSOT fuer aktive Doku/Governance normiert und maschinelles Gate (`check_naming_policy.py`) verbindlich verankert.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/naming-policy.md' 'DONELOG.md' 'WORKSPACE_STATUS.md' 'novapolis-dev/docs/donelog.md' PASS (2026-03-03 02:47); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'novapolis-dev/docs/naming-policy.md' 'DONELOG.md' 'WORKSPACE_STATUS.md' 'novapolis-dev/docs/donelog.md' PASS (EXITCODE=0, 2026-03-03 02:47); .\.venv\Scripts\python.exe scripts\check_naming_policy.py --repo-root . PASS (EXITCODE=0, 2026-03-03 02:47)
---

Naming Policy (SSOT fuer aktive Doku/Governance)
================================================

Zweck
-----

- Diese Datei ist die einzige Naming-SSOT fuer aktive Doku-/Governance-Pfade.
- Ziel ist ein reproduzierbarer, maschinenpruefbarer Namensstandard ohne stille Auto-Korrekturen.

Begriffslexikon
---------------

- `SSOT`: aktive, verbindliche Quelle fuer Inhalt und Regeln.
- `RAW`: ungefilterte Exporte/Quellmaterial unter `novapolis-rp/database-raw/**`.
- `Archive`: historische, nicht aktive Regelquelle unter `novapolis-dev/archive/**`.
- `Staging`: kuratierte Zwischenartefakte unter `novapolis-rp/database-curated/staging/**`.

Scope des Naming-Gates
----------------------

- Aktiver Scope (Whitelist): `.github/**`, `novapolis-dev/docs/**`, `README.md`, `WORKSPACE_INDEX.md`, `WORKSPACE_STATUS.md`, `DONELOG.md`, `todo.root.md`.
- Ausnahmen (Blacklist): `.git/**`, `.venv/**`, `Backups/**`, `outputs/**`, `.tmp/**`, `.tmp-results/**`, `novapolis-dev/archive/**`, `novapolis-rp/database-raw/**`, `novapolis-rp/database-curated/staging/**`, `novapolis_agent/eval/results/**`.
- Archive/RAW/Audit-Artefakte werden fuer dieses Gate nur als Ausnahmebereich behandelt, nicht als aktive Regelbasis.

Namensregeln (Dateien/Ordner)
-----------------------------

- Erlaubte Zeichen fuer Dateinamen: `A-Z a-z 0-9 . _ -`.
- Keine Leerzeichen oder Sonderzeichen in Dateinamen.
- Scoped Instruction-Dateien unter `.github/instructions/` enden auf `.instructions.md`.

Rule-/Reason-Namespace
----------------------

- Governance-Rule-IDs: `R-<BEREICH>-<THEMA>` in Großbuchstaben.
- Engine-Rule-IDs: `E-<BEREICH>-<THEMA>` in Großbuchstaben.
- Reason-Codes: `RC-<token>` mit kleinem Token (`[a-z0-9_]+`).
- Freitext in maschinenrelevanten Rule-/Reason-ID-Feldern ist unzulaessig.

Slug/ID/Tags
------------

- `slug` (wenn vorhanden): `^[a-z0-9]+(?:[-_][a-z0-9]+)*$`.
- `id` bleibt domaenspezifisch, muss aber als Feldwert nicht leer sein.
- `tags` werden als String-Liste erwartet; nicht-listige Formen gelten mindestens als Warnung.

Registry-Orte
-------------

- Kernregel-IDs (`R-*`): `.github/copilot-instructions.md` und scoped `.github/instructions/*.instructions.md`.
- Domaenenregister (`R-MCL-*`, `E-MCL-*`, `RC-*`): jeweilige scoped Instruction-Datei (z. B. `.github/instructions/mind-cluster.instructions.md`).

Hard Fail vs Warnung
--------------------

- Hard Fail (`exit != 0`): Scope-/Dateinamenverletzung, falsches Instruction-Suffix, ungueltige Rule-ID-Namespaceform, ungueltiger Reason-Code, ungueltiger `slug`.
- Warnung (`exit == 0` moeglich): nicht-kritische Formabweichungen, z. B. uneinheitliche `tags`-Darstellung.

Migrationsprinzip
-----------------

- Keine stillen Auto-Fixes.
- Jede Korrektur erfolgt als explizite Dateiaenderung mit nachvollziehbarer Logkette.
- Gate-Verstoesse werden als Befund (`Datei:Zeile:Regel:Wert`) ausgegeben.

Maschinelles Gate
-----------------

- Befehl: `& .\.venv\Scripts\python.exe scripts\check_naming_policy.py --repo-root .`
- Ausgabeformat: `Datei:Zeile:Regel:Wert`
- Exitcode: `0` ohne Hard-Fail, `1` bei mindestens einem Hard-Fail.

Hinweis zu bestehenden Spezialchecks
------------------------------------

- `novapolis-rp/coding/tools/validators/src/check-names.js` bleibt RP-spezifischer Spezialcheck fuer `database-rp/**`.
- Das neue Gate ersetzt diesen Check nicht, sondern deckt den aktiven Doku-/Governance-Scope repo-weit ab.



