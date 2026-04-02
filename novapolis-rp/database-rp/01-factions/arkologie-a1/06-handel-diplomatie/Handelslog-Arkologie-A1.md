---
stand: 2026-04-02 06:27
update: Handelslog fuehrt jetzt den belegten beschraenkten Haendlergilden-Kanal der Arkologie A1 mit Sicherheits- und Biosicherheitsauflagen.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260402_062604.md
category: canon
slug: handelslog_arkologie_a1_v1
version: "0.1"
---

Handelslog – Arkologie A1
=========================

Kontext
-------

- Quelle: `database-raw/99-exports/RAW-canvas-2025-10-16T16-55-00-000Z.txt` (Cluster `arkologie_a1`) sowie [Liora-Navesh](../02-characters/Liora-Navesh.md).
- Zweck: konservative Nachverfolgung belegter Tauschfenster und Handelsauflagen der Arkologie A1.
- Verknüpft mit [Relationslog-Arkologie-A1](./Relationslog-Arkologie-A1.md), [Missionslog-Arkologie-A1](../05-projects/Missionslog-Arkologie-A1.md), [Arkologie-inventar](../04-inventory/Arkologie-inventar.md).

Zweck
-----
- Deals/Trades, laufende Abmachungen, offene Forderungen.

Aktive Deals
------------

| Gegenpartei | Status | Rahmen | Verantwortliche | Beleg |
| --- | --- | --- | --- | --- |
| Haendlerbund | belegt, mengenoffen | `beschraenkt`; nur gepruefte Lieferketten und freigegebene Transitfenster | Nera Vossen, Borin Khade | `RAW-canvas-2025-10-16T16-55-00-000Z.txt`, [Liora-Navesh](../02-characters/Liora-Navesh.md), [Nera-Vossen](../02-characters/Nera-Vossen.md), [Relationslog-Arkologie-A1](./Relationslog-Arkologie-A1.md) |

Offene Angebote / Bedarf
------------------------

- Bedarf: kritische Beschaffungspfade fuer Energie-, MedTech- und Filterengpaesse bleiben priorisiert; konkrete Lieferfenster, Gegengueter und Abrechnungen bleiben `tbd`.
- Angebotsseite: selektive Austauschgueter der Arkologie A1 bleiben als Rahmen belegt, aber ohne belastbare Mengen- oder Chargenliste.
- Novapolis bleibt fuer Arkologie A1 weiter `unbekannt`; daraus wird bewusst kein direkter Handelskanal abgeleitet.

Red Lines
---------

- Kein Transit ohne Sicherheitsfreigabe durch die Arkologie-Sicherheitskette.
- Keine Mengensetzung ohne deal- oder missionsbezogenen Beleg.
- Keine unvalidierten Aussenkontakte oder Datenpfade jenseits gepruefter Lieferketten.
