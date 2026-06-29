---
stand: 2026-06-29 16:07
update: Der Active-Surface-Index bleibt jetzt ausdruecklich die Dev-Hub-Klassifikation; der workspaceweite Freshness-Scope lebt getrennt unter docs/meta/doc-freshness-scope.md.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260629_155310.md; snapshot-lock PASS (2026-06-29 16:07)
---

Active Surface Index (Dev Docs)
===============================

Ziel
----

- Scanbare Klassifikation der aktiven Dev-Dokumentoberflaeche.
- Einheitliche Felder: `surface`, `owner`, `last_check`.

Legende
-------

- `ACTIVE`: Operativer Arbeitsbestand, regelmaessig mutiert.
- `REFERENCE`: SSOT/Referenz, seltene Aenderungen.
- `HISTORICAL`: Historische Evidenz, keine aktive Regelbasis.

Index (novapolis-dev/docs)
--------------------------

| Path | surface | owner | last_check |
| --- | --- | --- | --- |
| `novapolis-dev/docs/donelog.md` | ACTIVE | dev-governance | 2026-04-17 |
| `novapolis-dev/docs/todo.index.md` | ACTIVE | dev-governance | 2026-04-17 |
| `novapolis-dev/docs/todo.dev.md` | ACTIVE | dev-governance | 2026-04-17 |
| `novapolis-dev/docs/todo.rp.md` | ACTIVE | rp-governance | 2026-04-17 |
| `novapolis-dev/docs/todo.agent-board.md` | ACTIVE | agent-governance | 2026-04-17 |
| `novapolis-dev/docs/todo.sim.md` | ACTIVE | sim-governance | 2026-04-17 |
| `novapolis-dev/docs/index.md` | REFERENCE | dev-governance | 2026-04-18 |
| `novapolis-dev/docs/naming-policy.md` | REFERENCE | dev-governance | 2026-04-18 |
| `novapolis-dev/docs/tests.md` | REFERENCE | qa-governance | 2026-04-18 |
| `novapolis-dev/docs/dataset-provenance.md` | REFERENCE | data-governance | 2026-04-18 |
| `novapolis-dev/docs/copilot-vscode-usage.md` | REFERENCE | tooling-governance | 2026-04-18 |
| `novapolis-dev/docs/readme_decisions.md` | REFERENCE | dev-governance | 2026-04-18 |
| `novapolis-dev/docs/readme.hub.md` | REFERENCE | dev-governance | 2026-04-18 |
| `novapolis-dev/docs/architecture-summary-local-ai.md` | REFERENCE | architecture | 2026-04-18 |
| `novapolis-dev/docs/specs/**` | REFERENCE | domain-maintainers | 2026-04-18 |
| `novapolis-dev/docs/process/**` | REFERENCE | process-governance | 2026-04-17 |
| `novapolis-dev/docs/meta/**` | REFERENCE | dev-governance | 2026-04-18 |
| `novapolis-dev/archive/docs/**` | HISTORICAL | archive-maintainers | 2026-04-15 |

Pflege
------

- Bei Neuaufnahme/Aenderung operativer Dev-Dokumente den Index im selben Lauf aktualisieren.
- `last_check` wird bei inhaltlicher Pruefung oder Klassifikationsaenderung aktualisiert.
- Die Sammelwerte fuer `process/**` und `meta/**` bleiben bewusst Gruppensignale; punktuelle Einzellaeufe muessen nicht jeden Referenzpfad auf denselben Tag ziehen.
- Der workspaceweite Freshness-Check liest seinen Scope nicht mehr aus dieser Tabelle, sondern aus `novapolis-dev/docs/meta/doc-freshness-scope.md`.
- Die Wildcard-Zeilen (`specs/**`, `process/**`, `meta/**`) bleiben hier reine Dev-Klassifikation und nicht laenger ein versteckter Workspace-Freshness-Scope.



