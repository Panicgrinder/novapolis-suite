---
stand: 2026-04-29 03:56
update: In entity-centric Runtime-Dossier migriert; Inhalt bleibt Arbeitsstand ohne Kanon-Promotion.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260429_035444.md
---
Runtime State - Haendlerbund
============================

Status
------

- slug: haendlerbund
- scope: faction
- state: Beobachtungsstand
- review_state: working

Current State
-------------

- summary: Der Haendlerbund ist im aktuellen Hauptpfad als aktive, aber nicht allwissende Fraktionsachse praesent. `G7` bleibt externer Eigenkern, Handels- und Freigaberaum; `H-47` bleibt als eingebettete Niederlassung in `C6` der naechste Partnerpfad zu Novapolis. Fuer den frischen Nordlinie-Zug fuehrt der Haendlerbund damit keine freie Gesamtreaktion, sondern einen geteilten Stand: `G7` bleibt ohne neue Meldung aus `C6` auf altem Wissensstand, waehrend `Mara Quell` vor Ort in `C6` bleibt.
- drivers:
  - `G7` bleibt Zentrale, Handels- und Sicherheitsfreigabekern des Haendlerbunds.
  - `H-47` bleibt die belegte, in `C6` eingebettete Niederlassung mit Partnerpfad zu Novapolis.
  - Belegte Austauschklassen im aktiven Rahmen bleiben `Energie`, `technische Reparaturen` und `Kommunikationszugang` gegen `Nahrungsmittel`, `Filter` und `Grundbedarfsgueter`.
  - Ohne Rueckmeldung aus `C6` kippt der Haendlerbund nicht in freie neue Nordlinie-Reaktion.
- blockers:
  - keine neue Meldung aus `C6` nach `G7`
  - keine belastbaren Konvoi-, Manifest- oder Mengenketten fuer einen neuen Aussenlauf
  - keine neue belastbare Groessenordnung fuer Freigabe, Reaktion oder Materialbewegung aus dem Eigenkern
- impacted_entities:
  - Haendlerbund
  - G7
  - H-47
  - Mara Quell
  - C6

Active Runtime Axes
-------------------

- Ortsachsen:
  - `G7` als externer Eigenkern ohne frischen Novapolis-Ruecklauf
  - `C6` als eingebettetes Partner- und Niederlassungsfenster ueber `H-47`
- Fraktionslogik:
  - G7 bleibt auf altem Wissensstand, bis aus `C6` eine belastbare Meldung oder Bewegung nach aussen geht
  - Mara fuehrt die Vor-Ort-Kante in `C6`, nicht die Fernreaktion in `G7`

Evidence
--------

- SSOT: `database-rp/01-factions/haendlerbund/04-inventory/Haendlerbund-inventar.md`
- SSOT: `database-rp/01-factions/haendlerbund/03-locations/G7.md`
- SSOT: `database-rp/01-factions/haendlerbund/05-projects/caravan-moves.md`
- Runtime: `../../locations/g7/state.md`
- Runtime: `../../locations/c6/state.md`
- Runtime: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 9, Turn 10, Turn 11

Promotion Notes
---------------

- Dieser Fraktionsstatus aggregiert den aktiven Haendlerbund-Slice nur ueber `G7`, `H-47` und die belegte C6-Einbettung.
- Erst erweitern, wenn neue Meldungen, Konvoiwege oder Mengenketten im Runtime-Zug selbst belastbar werden.
