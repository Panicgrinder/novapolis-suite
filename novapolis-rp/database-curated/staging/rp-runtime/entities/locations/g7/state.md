---
stand: 2026-04-29 03:56
update: In entity-centric Runtime-Dossier migriert; Inhalt bleibt Arbeitsstand ohne Kanon-Promotion.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260429_035444.md
---
Runtime State - G7
==================

Status
------

- slug: g7
- scope: location
- state: Beobachtungsstand
- review_state: working

Current State
-------------

- summary: G7 bleibt im aktuellen Hauptpfad der externe Eigenkern des Haendlerbunds, fuehrt aber fuer Novapolis keinen neuen Runtime-Stand, weil `Mara Quell` weiterhin in `C6` bleibt und nichts nach draussen gespiegelt hat. Die Zentrale bleibt damit fuer den frischen Nordlinie-Zug auf ihrem vorherigen Wissensstand.
- drivers:
  - G7 bleibt Leitstelle, Handels- und Sicherheitsfreigabekern des Haendlerbunds.
  - ohne Rueckmeldung aus C6 laeuft keine belastbare neue Novapolis-Information in G7 auf
  - die H-47-Niederlassung in C6 bleibt aus G7-Sicht auf dem zuletzt bekannten Rahmenstand
- blockers:
  - Mara ist nicht vor Ort in G7
  - keine neue Meldung aus C6
  - damit keine belastbare neue Groessenordnung fuer Reaktion, Freigabe oder Konvoi
- impacted_entities:
  - G7
  - Haendlerbund
  - H-47

Evidence
--------

- SSOT: `database-rp/01-factions/haendlerbund/03-locations/G7.md`
- SSOT: `database-rp/01-factions/haendlerbund/02-characters/Mara-Quell.md`

Promotion Notes
---------------

- G7 fuehrt hier bewusst keinen neuen Novapolis-Laufstand.
- Erst aktualisieren, wenn aus `C6` wirklich eine Meldung oder ein belastbarer externer Schritt nach aussen geht.
