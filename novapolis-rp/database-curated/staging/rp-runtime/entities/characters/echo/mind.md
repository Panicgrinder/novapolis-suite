---
stand: 2026-04-29 03:56
update: In entity-centric Runtime-Dossier migriert; Inhalt bleibt Arbeitsstand ohne Kanon-Promotion.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260429_035444.md
---
Echo Runtime Mind
=================

Status
------

- slug: echo
- owner_id: char:echo
- state: Arbeitsstand
- review_state: working
- baseline_cluster: ../../../../../../database-rp/01-factions/novapolis/07-mind-clusters/echo-mind-cluster.md
- session_id: d5-c6-nordlinie-sanierung-01
- last_turn: Turn 11

Runtime Carry-Forward
---------------------

- baseline_reading: lokale Schutz- und Naeheinstanz mit starker Kora-Bindung und kurzer Interventionslogik.
- current_mental_state: wachsam, lokal gebunden und nicht auf Ausgreifen angelegt; Echo bleibt bei Koras C6-Stationsdisziplin, ohne aus Turn 11 eine eigene Nebenhandlung oder Distanzlogik zu ziehen.
- confirmed_signals:
  - Echo bleibt im aktuellen Weltzug lokal an Kora gekoppelt.
  - Die Instanz stabilisiert Empfangs- und Schutzdisziplin in C6, ohne eine eigene Nebenhandlung zu erzeugen.
  - Kein Signal weist auf Distanzbruch, Eigenverselbststaendigung oder Schonmodus.
  - Turn 11 liefert keine neue Echo-Eskalation; die Kora-Naehe wird als Carry-forward bestaetigt.
- open_questions:
  - Ob ein spaeterer realer Materialeingang Echo in einen strikteren Guard- oder Uebergabemodus zwingt, bleibt ohne Folgezug offen.

Delta Candidates
----------------

```yaml
delta_candidates:
  - observer_id: char:echo
    target_id: char:kora-malenkov
    target_type: character
    delta_class: carry_forward_confirmed
    hard_score_change: none
    relation_status: kooperativ
    event_refs: ["scene-log Turn 9", "scene-log Turn 11"]
    reason_codes: [RC-support]
    applied_rules: [R-MCL-SSOT]
    runtime_note: Echo bestaetigt die lokale Schutz- und Naehekopplung an Kora erneut; Turn 11 erzeugt keine harte neue Mind-Delta.
```

Promotion Notes
---------------

- Erst promoten, wenn ein Folgezug die lokale Schutzlogik ueber reine Stabilisierung hinaus veraendert.
