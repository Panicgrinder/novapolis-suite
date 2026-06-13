---
stand: 2026-06-13 09:17
update: In entity-centric Runtime-Dossier migriert; Inhalt bleibt Arbeitsstand ohne Kanon-Promotion.
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=PASS; frontmatter=PASS; path-portability=FAIL; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=FAIL; logs-policy=PASS; ruff=FAIL; black=FAIL; pytest=FAIL; pyright=SKIP; mypy=PASS; report=.tmp\results\reports\checks_report_20260613_091615.md
---
Marei Falk - Runtime Working Sheet
==================================

Status
------

- slug: marei
- entity_id: char:marei-falk
- name: Marei Falk
- state: Arbeitsstand
- review_state: working
- first_seen_session: d5-c6-nordlinie-sanierung-01

Role
----

- faction: Novapolis / E3-Nachlauf in C6
- function: Stellvertretung C6, Tageskoordination, Inventar- und Evak-Nachsorge
- current_goal: C6-Schichten, Evak-Nachsorge und Versorgung so stabil halten, dass Kora fuehrungsfaehig bleibt

Signals
-------

- confirmed:
  - Marei ist als E3-01 im C6-Bewohner-Roster belegt.
  - Sie koordiniert Tageslogik, Inventar- und Versorgungsabgleich in C6.
  - Ihre Rolle entlastet Kora und bindet den E3-Nachlauf in die C6-Schichten ein.
- tentative:
  - Im aktuellen Turn-11-Hauptpfad ist Marei als Vor-Ort-Ressource mitzudenken, aber nicht individuell ausgespielt.
- contradictions:
  - keine direkte Widerspruchslage; SSOT-Slug `marei` und Mind-Cluster-Owner `marei-falk` bleiben als Legacy-Schnitt sichtbar getrennt

Promotion Notes
---------------

- SSOT: `database-rp/01-factions/novapolis/02-characters/Marei-Falk.md`
- Mind-Runtime: `mind.md`
- Roster: `../../locations/c6/roster.md`.
