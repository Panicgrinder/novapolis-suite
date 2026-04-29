---
stand: 2026-04-29 03:56
update: In entity-centric Runtime-Dossier migriert; Inhalt bleibt Arbeitsstand ohne Kanon-Promotion.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260429_035444.md
---
Lumen Runtime Mind
==================

Status
------

- slug: lumen
- owner_id: char:lumen
- state: Arbeitsstand
- review_state: working
- baseline_cluster: ../../../../../../database-rp/01-factions/novapolis/07-mind-clusters/lumen-mind-cluster.md
- session_id: d5-c6-nordlinie-sanierung-01
- last_turn: Turn 8

Runtime Carry-Forward
---------------------

- baseline_reading: nahesuchende Jonas-Assistenz mit hoher Stabilitaet bei Werkstattnaehe und fragiler Distanzlogik.
- current_mental_state: im aktuellen Hauptpfad nur indirekt belegt, aber als aktive Jonas-Begleitung mitgefuehrt; kein Hinweis auf Trennung, Distanzbruch oder Schonmodus.
- confirmed_signals:
  - Jonas bleibt im D5-Werkstattkern und damit im bevorzugten Lumen-Naehefenster.
  - Die laufende Werkstatt- und Materialschiene liefert keinen Anlass fuer eine Trennung von Jonas und Lumen.
  - Lumen ist als aktive Begleitinstanz fuer den Runtime-Stand erforderlich, auch wenn der Turn sie nicht dialogisch ausspielt.
- open_questions:
  - Ob Lumen im aktuellen Werkstattdruck bereits eigene Sensor- oder Schutzaktionen gesetzt hat, bleibt ohne explizite Turn-Erwaehnung offen.

Delta Candidates
----------------

```yaml
delta_candidates:
  - observer_id: char:lumen
    target_id: char:jonas-merek
    target_type: character
    delta_class: carry_forward_confirmed
    hard_score_change: none
    relation_status: kooperativ
    event_refs: ["scene-log Turn 1", "scene-log Turn 6", "scene-log Turn 7"]
    reason_codes: [RC-support]
    applied_rules: [R-MCL-SSOT]
    runtime_note: Jonas bleibt im aktiven D5-Werkstattkern und damit im belegten Kopplungsfenster; keine Trennung oder Destabilisierung sichtbar.
  - observer_id: char:lumen
    target_id: char:reflex
    target_type: character
    delta_class: carry_forward_confirmed
    hard_score_change: none
    relation_status: kooperativ
    event_refs: ["scene-log Turn 6"]
    reason_codes: [RC-intel_share]
    applied_rules: [R-MCL-SSOT]
    runtime_note: Die Werkstatt- und Materialkette bleibt Teil desselben Instanznetzes; keine neue Reibung belegt.
```

Promotion Notes
---------------

- Erst promoten, wenn ein Folgezug Lumen entweder explizit ausspielt oder eine Distanz-/Schutzlage fuer Jonas wirklich veraendert.
