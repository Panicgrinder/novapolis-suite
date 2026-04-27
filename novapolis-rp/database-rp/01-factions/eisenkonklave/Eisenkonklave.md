---
stand: 2026-04-27 02:30
update: Eisenkonklave fuehrt jetzt ein konservatives Betriebs- und Nahraummodell T0 fuer H12 und den Schadenskorridor H3-H12.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_022916.md
slug: eisenkonklave
category: faction
status: active
version: "0.1"
---

Eisenkonklave (Fraktion)
========================

Überblick
---------
- Status: aktiv
- Rolle im Setting: stark kontrollierter Werkstoff-, Schutz- und Freigabeblock mit einem aktiven Kernknoten in H12.

Kerngebiet
----------

- [H12](./03-locations/H12.md): aktiver Kommando-, Sicherheits- und Freigabeknoten der Eisenkonklave.

Betriebskorridor T0
-------------------

- `H12` bleibt der einzige klar aktive Kernknoten der Fraktion.
- Der Schadenskorridor `H3 -> H12` bildet den unmittelbaren Belastungs- und Sicherheitsraum fuer Versorgung, Transit und Oeffnung.
- Die Eisenkonklave bleibt damit als enger Kontrollblock lesbar und nicht als breit ausgerollter Stationsverbund.

Rollenlesart T0
---------------

- Varek Solun fuehrt H12 ueber Kontrolle, Priorisierung und den Schutz eigener Module.
- Kaspar Dorn haelt nur selektive Handels- und Versorgungsfenster offen.
- Yara Kest zwingt Transit, Konvois und jede Oeffnung durch eine harte Sicherheitsfreigabe.

Betriebsmodell T0
-----------------

- Das konservative Arbeitsmodell fuer Kernknoten, Freigabekette und innere Konfliktlinien liegt in [eisenkonklave-betriebsmodell-t0](./00-doctrine/eisenkonklave-betriebsmodell-t0.md).
- Kernlesart: `H12` fuehrt; der beschaedigte Zulauf `H3 -> H12` bestimmt, wie weit Kontrolle, Handel und Versorgung real tragen.

Nahraum T0
----------

- Der unmittelbare Eisenkonklave-Nahraum ist jetzt konservativ in [eisenkonklave-nahraum-t0](./00-doctrine/eisenkonklave-nahraum-t0.md) verdichtet.
- Darin sind `H12`, der Schadenskorridor, Sicherheitsdruck und die naechsten Belastungsachsen zusammengezogen.

Diplomatie & Beziehungen
------------------------
- Novapolis: neutral_wachsam → laufende Gespräche über Zugang zu Ressourcen.
- Händlerbund: wechselhaft → einzelne Handelsfenster via [caravan-moves](../haendlerbund/05-projects/caravan-moves.md).
- Schienenbund: feindselig → Konflikt um Tunnelkontrolle.

Systemverknüpfungen
-------------------
- `relationslog_eisenkonklave_v1`
- `ai_behavior_index_v2`
- `cluster_index_v1`
- `handelslog_eisenkonklave_v1` (Pending-Dokument)

ToDo
----
- Missions-/Inventarverknüpfungen ergänzen (z. B. benoetigte Module, Sicherheitsauflagen).
- Diplomatieereignisse in `Missionslog` spiegeln.
- Rollenliste erweitern (Second-in-Command, Kontakte zum Händlerbund).
