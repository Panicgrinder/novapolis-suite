---
stand: 2026-06-13 09:17
update: In entity-centric Runtime-Dossier migriert; Inhalt bleibt Arbeitsstand ohne Kanon-Promotion.
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=PASS; frontmatter=PASS; path-portability=FAIL; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=FAIL; logs-policy=PASS; ruff=FAIL; black=FAIL; pytest=FAIL; pyright=SKIP; mypy=PASS; report=.tmp\results\reports\checks_report_20260613_091615.md
---
Marei Falk Runtime Mind
=======================

Status
------

- slug: marei
- owner_id: char:marei-falk
- state: Arbeitsstand
- review_state: working
- baseline_cluster: ../../../../../../database-rp/01-factions/novapolis/07-mind-clusters/marei-falk-mind-cluster.md
- session_id: d5-c6-nordlinie-sanierung-01
- last_turn: Turn 11 / C6-Runtime-Nachzug

Runtime Carry-Forward
---------------------

- baseline_reading: strukturierende, versorgungsorientierte Stellvertretung mit hoher Stabilitaet in geregelten Schicht- und Versorgungsablaeufen.
- current_mental_state: funktional stabil und auf Entlastung der C6-Leitung ausgerichtet; im Turn-11-Hauptpfad noch nicht individuell ausgespielt.
- confirmed_signals:
  - Marei bleibt als E3-01 und C6-Stellvertretung Teil der Vor-Ort-Oberflaeche.
  - Ihre Aufgabe liegt in Tageskoordination, Inventar-/Versorgungsabgleich und E3-Nachsorge.
  - Kein aktuelles Signal erzwingt einen harten Rescore gegen Kora, Ronja oder Echo.
- open_questions:
  - Ob Marei im naechsten C6-Folgezug eigene Prioritaeten gegen Kora, H-47 oder den Evak-Druck setzt, bleibt offen.

Delta Candidates
----------------

```yaml
delta_candidates:
  - observer_id: char:marei-falk
    target_id: char:kora-malenkov
    target_type: character
    delta_class: carry_forward_confirmed
    hard_score_change: none
    relation_status: kooperativ
    event_refs: ["C6 runtime consolidation 2026-04-29"]
    reason_codes: [RC-support]
    applied_rules: [R-MCL-SSOT]
    runtime_note: Mareis C6-Entlastungsrolle bleibt fuer Koras Stationsfuehrung bestaetigt; keine neue Mind-Delta aus Turn 11.
```

Promotion Notes
---------------

- Erst promoten, wenn Marei individuell handelt oder ein Folgezug eine echte C6-Schicht-, Evak- oder Vertrauensverschiebung belegt.
