---
stand: 2026-02-17 09:12
update: PR-Beschreibung auf PR #4 (docs(rp) Batch C) aktualisiert; Scope-Hinweis zur pre-commit-Migration ergänzt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc PR_DESCRIPTION.md PASS (2026-02-17 07:17); & .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py PR_DESCRIPTION.md PASS (2026-02-17 07:17)
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
