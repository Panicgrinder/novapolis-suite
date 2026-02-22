---
stand: 2026-02-22 00:24
update: PR-Beschreibung um RP-Hard-Gate-Nachtrag ergänzt (Ursache + Frontmatter-Fix für neue 24x1h-Project-Templates).
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '.github/instructions/rp-docs.instructions.md' 'PR_DESCRIPTION.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-22 00:22); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py '.github/instructions/rp-docs.instructions.md' 'PR_DESCRIPTION.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-22 00:22)
---

PR: docs(rp) Batch C (Novapolis) – Naming, Links, Hook-Migration
================================================================

Kurz (Deutsch)
-------------

- RP: Personenindex Novapolis umbenannt (`person_index_np` -> `person-index-np`, MD + JSON-Sidecar) und Referenzen in Novapolis/Händlerbund nachgezogen.
- RP: Relative Links in den betroffenen Handel/Diplomatie-READMEs und Charakterdateien konsolidiert.
- Dev-Hub: Links im neuen Abschnitt in `novapolis-dev/docs/donelog.md` repariert (korrekt relativ oder repo-root-relativ).
- Hygiene: Volatiles Testartefakt `outputs/test-artifacts/junit.xml` aus Versionierung entfernt und via `.gitignore` ausgeschlossen.

Scope-Hinweis (Review-Kommentar)
-------------------------------

Diese PR enthält zusätzlich eine Hook-/Wrapper-Migration:

- Pre-commit Hook: Entry-Point in `githooks/pre-commit` auf Python umgestellt (`scripts/pre_commit.py`).

Grund: Repo-Governance entfernt schrittweise PowerShell-Wrapper/Scriptblocks und bevorzugt Python-Wrapper.

Details
-------

### RP-Änderungen

- Rename: `novapolis-rp/database-rp/01-factions/novapolis/02-characters/person_index_np.md` -> `person-index-np.md`.
- Sidecar: `novapolis-rp/database-rp/01-factions/novapolis/02-characters/person-index-np.json` ergänzt/angepasst.
- Referenzen in betroffenen Dokumenten auf den neuen Pfad aktualisiert.

### Tooling/Hooks

- `githooks/pre-commit`: vereinheitlicht auf einen Python-Entry-Point.
- `scripts/pre_commit.py`: Snapshot-Gate + Checks auf staged Markdown (markdownlint/frontmatter/DONELOG-Guard).

Checks
------

- Lokal: `npm --prefix novapolis-rp/coding/tools/validators run validate` PASS.
- Repo-Checks: `scripts/run_checks_and_report.py` (Lint/Typen/Tests/Coverage) PASS.

Nachtrag (2026-02-22)
---------------------

- Beim ersten Commitlauf blockierte `validate:rp` aus dem RP-Hard-Gate wegen Frontmatter-Vertragsverletzungen in neu angelegten `24x1h-Log-Template.md`-Dateien (`category: project`).
- Konkrete Ursachen: `status: draft` ist nicht im erlaubten Enum und `last_updated` fehlte.
- Umgesetzter Fix: alle sieben Fraktions-Templates auf `status: planned` harmonisiert und `last_updated: "2026-02-22"` ergänzt; danach Commit+Push erfolgreich.
