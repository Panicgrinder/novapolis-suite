---
stand: 2026-04-02 06:27
update: Handelslog fuehrt jetzt den belegten Rahmen `handel_gelegentlich` mit Händlerbund und die Freigabekette Kaspar/Yara.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260402_062604.md
category: canon
slug: handelslog_eisenkonklave_v1
version: "0.1"
---

Handelslog – Eisenkonklave
==========================

Kontext
-------

- Quelle: `database-raw/99-exports/RAW-canvas-2025-10-16T16-55-00-000Z.txt` (Cluster `eisenkonklave_operativ`).
- Zweck: konservative Nachverfolgung belegter Handelsfenster und Angebotslagen der Eisenkonklave.
- Verknüpft mit [Relationslog-Eisenkonklave](./Relationslog-Eisenkonklave.md), [Missionslog-Eisenkonklave](../05-projects/Missionslog-Eisenkonklave.md), [Eiserne-Enklave-inventar](../04-inventory/Eiserne-Enklave-inventar.md).

Aktive Deals
------------

| Gegenpartei | Status | Rahmen | Verantwortliche | Beleg |
| --- | --- | --- | --- | --- |
| Haendlerbund | belegt, mengenoffen | `handel_gelegentlich`; einzelne Handelsfenster nur nach Sicherheitsfreigabe | Kaspar Dorn, Yara Kest | `RAW-canvas-2025-10-16T16-55-00-000Z.txt`, [Relationslog-Eisenkonklave](./Relationslog-Eisenkonklave.md), [Missionslog-Eisenkonklave](../05-projects/Missionslog-Eisenkonklave.md) |

Offene Angebote / Bedarf
------------------------

- Eigenlage: Werkstoff-/Instandsetzungsgueter, Rohstoffe sowie Schutzgüter sind als interne Bestandsklassen der Eisenkonklave belegt; ob daraus konkrete Handelsware wird, bleibt pro Fenster `tbd`.
- Bedarf: belastbare Dealprotokolle, Gegengüter, Zeitpunkte und Routen bleiben `tbd`.
- Guardrail: ohne Sicherheitsfreigabe und ohne missions- oder dealbezogenen Beleg keine Mengensetzung im Handelslog.
