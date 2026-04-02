---
stand: 2026-04-02 06:27
update: Verdeckte Beschaffungsfenster des Schattenbunds sind jetzt als belegter Missionsanker verankert.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260402_062604.md
title: Missionslog (Schattenbund)
category: project
slug: missionslog-schattenbund
version: "0.1"
last_updated: 2026-04-01T00:39:39+02:00
status: active
owners: [schattenbund]
authority_chain:
  - "fraktion:schattenbund"
  - "fraktions-leitung:nyra-vehl"
  - "stellv-fraktions-leitung:tbd"
  - "leitung-sicherheit:sera-nol"
  - "leitung-logistik:jarek-voan"
  - "stationsleitung:tbd"
tags: [rp, missionen, schattenbund]
dependencies: [schattenbund]
---

<!-- markdownlint-disable MD025 -->

Missionslog (Schattenbund)
==========================

Zentrale Übersicht der fraktionsspezifischen Missionen für den Schattenbund.

Hinweis
-------

- Der erste konservative Aussen- und Beschaffungsanker des Schattenbunds ist jetzt verankert.
- Globaler Einstieg bleibt [00-admin/Missionslog](../../../00-admin/Missionslog.md).

### Verdeckte Beschaffungsfenster ueber Zwischenhaendler absichern

- Ziel: knappe Gueter verdeckt beschaffen und verteilen, ohne die Abschirmung des Schattenbunds aufzugeben.
- Start: T0 / laufende Fraktionslage
- Ende: offen
- Status: aktiv
- Belege/Quittungen: `../../../database-raw/99-exports/RAW-canvas-2025-10-16T16-55-00-000Z.txt`, [Relationslog-Schattenbund](../06-handel-diplomatie/Relationslog-Schattenbund.md), [Handelslog-Schattenbund](../06-handel-diplomatie/Handelslog-Schattenbund.md)
- Verantwortliche: Jarek Voan (verdeckte Warenstroeme), Sera Nol (Abschirmung kritischer Uebergaben), Nyra Vehl (Eskalation und Prioritaeten)
- Inventar-Link: [Schattenbund-inventar](../04-inventory/Schattenbund-inventar.md)
- Orte/Projekte: [F9](../03-locations/F9.md), [Handelslog-Schattenbund](../06-handel-diplomatie/Handelslog-Schattenbund.md), [Relationslog-Schattenbund](../06-handel-diplomatie/Relationslog-Schattenbund.md)
  Hinweise:
  - Der RAW-Cluster `schattenbund_feld` belegt fuer den Schattenbund `Novapolis(unbekannt)`, `Eisenkonklave(feindselig)` und `Arkologie(verdeckt)` als Aussenlage.
  - Jarek Voan steuert verdeckte Warenstroeme ueber redundante Zwischenhaendler, Ausweichrouten und gestaffelte Uebergaben.
  - Sera Nol sichert kritische Uebergaben und Gegenaufklaerung ab; Nyra Vehl entscheidet Eskalations- und Prioritaetslinien.
  - Konkrete Routen, Mengen, benannte Gegenparteien und einzelne Lieferfenster bleiben bewusst `tbd`.

