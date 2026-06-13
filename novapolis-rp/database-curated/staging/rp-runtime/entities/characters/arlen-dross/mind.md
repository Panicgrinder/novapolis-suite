---
stand: 2026-06-13 09:17
update: In entity-centric Runtime-Dossier migriert; Inhalt bleibt Arbeitsstand ohne Kanon-Promotion.
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=PASS; frontmatter=PASS; path-portability=FAIL; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=FAIL; logs-policy=PASS; ruff=FAIL; black=FAIL; pytest=FAIL; pyright=SKIP; mypy=PASS; report=.tmp\results\reports\checks_report_20260613_091615.md
---
Arlen Dross Runtime Mind
========================

Status
------

- slug: arlen-dross
- owner_id: char:arlen-dross
- state: Arbeitsstand
- review_state: working
- baseline_cluster: ../../../../../../database-rp/01-factions/novapolis/07-mind-clusters/arlen-dross-mind-cluster.md
- session_id: d5-c6-nordlinie-sanierung-01
- last_turn: Turn 11 / C6-Runtime-Nachzug

Runtime Carry-Forward
---------------------

- baseline_reading: ausgleichender Vermittler mit Freiheitsdrang, schriftlicher Absicherung und hoher Sensibilitaet fuer Kontrollverlust.
- current_mental_state: moderierend bereit, aber nicht individuell aktiviert; Arlen bleibt als C6-/H-47-Schnittstelle abrufbar.
- confirmed_signals:
  - Arlen ist als H-47-/C6-Vor-Ort-Entitaet belegt.
  - Er traegt Vermittlung und Aussenkontakte, ohne Koras interne Stationsleitung zu duplizieren.
  - Kein aktueller Hauptpfad-Zug belegt eine neue Verhandlung, Zusage oder Konfliktverschiebung.
- open_questions:
  - Ob eine kommende Uebergabe, Quittung oder Handelsansprache Arlen individuell aktiviert, bleibt offen.

Delta Candidates
----------------

```yaml
delta_candidates:
  - observer_id: char:arlen-dross
    target_id: char:marven-kael
    target_type: character
    delta_class: carry_forward_confirmed
    hard_score_change: none
    relation_status: kooperativ
    event_refs: ["C6 runtime consolidation 2026-04-29"]
    reason_codes: [RC-support]
    applied_rules: [R-MCL-SSOT]
    runtime_note: Arlens Vermittlungsrolle bleibt an Marvens Konvoifuehrung gekoppelt; keine neue Mind-Delta ohne eigene Handlung.
```

Promotion Notes
---------------

- Erst promoten, wenn Arlen individuell verhandelt, eine Quittung oder Transferentscheidung traegt oder eine relationale Lage sichtbar veraendert.
