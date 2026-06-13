---
stand: 2026-06-13 09:17
update: In entity-centric Runtime-Dossier migriert; Inhalt bleibt Arbeitsstand ohne Kanon-Promotion.
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=PASS; frontmatter=PASS; path-portability=FAIL; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=FAIL; logs-policy=PASS; ruff=FAIL; black=FAIL; pytest=FAIL; pyright=SKIP; mypy=PASS; report=.tmp\results\reports\checks_report_20260613_091615.md
---
Marven Kael Runtime Mind
========================

Status
------

- slug: marven-kael
- owner_id: char:marven-kael
- state: Arbeitsstand
- review_state: working
- baseline_cluster: ../../../../../../database-rp/01-factions/novapolis/07-mind-clusters/marven-kael-mind-cluster.md
- session_id: d5-c6-nordlinie-sanierung-01
- last_turn: Turn 11 / C6-Runtime-Nachzug

Runtime Carry-Forward
---------------------

- baseline_reading: vorsichtiger Stratege mit hoher Crew-Loyalitaet, Risikofokus und Rueckzugsorientierung.
- current_mental_state: kontrolliert abwartend; Marven ist in C6 als Vor-Ort-Koordinator relevant, aber ohne neue externe Meldung nicht als freier G7-Reaktionsmotor zu lesen.
- confirmed_signals:
  - Marven bleibt als H-47-/C6-Vor-Ort-Entitaet belegt.
  - Seine Crew- und Aussenkoordination bleibt von Koras interner Stationsleitung getrennt.
  - Kein aktueller Hauptpfad-Zug belegt eine neue Handelszusage, G7-Meldung oder Konvoiaktion.
- open_questions:
  - Ob der naechste Material- oder Handelsimpuls Marven in eine aktive Uebergabeentscheidung zieht, bleibt offen.

Delta Candidates
----------------

```yaml
delta_candidates:
  - observer_id: char:marven-kael
    target_id: char:kora-malenkov
    target_type: character
    delta_class: carry_forward_confirmed
    hard_score_change: none
    relation_status: kooperativ
    event_refs: ["C6 runtime consolidation 2026-04-29"]
    reason_codes: [RC-intel_share]
    applied_rules: [R-MCL-SSOT]
    runtime_note: Marvens C6-Anschluss bleibt ueber Kora als operative Schnittstelle lesbar; keine neue Mind-Delta ohne eigene Handlung.
```

Promotion Notes
---------------

- Erst promoten, wenn Marven individuell entscheidet, eine Meldung nach G7 ausloest oder eine echte Uebergabe- beziehungsweise Handelsfolge traegt.
