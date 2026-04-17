---
stand: 2026-04-17 04:39
update: Die aktiven Boards, DONELOGs und Prozessquellen fuehren jetzt belastbare April-Pruefstaende statt des alten Maerz-Drifts.
checks: snapshot-lock PASS (2026-04-17 02:44); markdownlint=PASS; frontmatter=PASS
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
| `novapolis-dev/docs/index.md` | REFERENCE | dev-governance | 2026-03-04 |
| `novapolis-dev/docs/naming-policy.md` | REFERENCE | dev-governance | 2026-03-04 |
| `novapolis-dev/docs/tests.md` | REFERENCE | qa-governance | 2026-03-04 |
| `novapolis-dev/docs/dataset-provenance.md` | REFERENCE | data-governance | 2026-03-04 |
| `novapolis-dev/docs/copilot-vscode-usage.md` | REFERENCE | tooling-governance | 2026-03-04 |
| `novapolis-dev/docs/readme_decisions.md` | REFERENCE | dev-governance | 2026-03-04 |
| `novapolis-dev/docs/readme.hub.md` | REFERENCE | dev-governance | 2026-03-04 |
| `novapolis-dev/docs/architecture-summary-local-ai.md` | REFERENCE | architecture | 2026-03-04 |
| `novapolis-dev/docs/specs/**` | REFERENCE | domain-maintainers | 2026-03-04 |
| `novapolis-dev/docs/process/**` | REFERENCE | process-governance | 2026-04-17 |
| `novapolis-dev/docs/meta/**` | REFERENCE | dev-governance | 2026-03-04 |
| `novapolis-dev/archive/docs/**` | HISTORICAL | archive-maintainers | 2026-04-15 |

Pflege
------

- Bei Neuaufnahme/Aenderung operativer Dev-Dokumente den Index im selben Lauf aktualisieren.
- `last_check` wird bei inhaltlicher Pruefung oder Klassifikationsaenderung aktualisiert.
- Die Sammelwerte fuer `process/**` und `meta/**` bleiben bewusst Gruppensignale; punktuelle Einzellaeufe muessen nicht jeden Referenzpfad auf denselben Tag ziehen.



