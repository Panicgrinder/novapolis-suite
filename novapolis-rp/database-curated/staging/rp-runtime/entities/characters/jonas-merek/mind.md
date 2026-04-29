---
stand: 2026-04-29 03:56
update: In entity-centric Runtime-Dossier migriert; Inhalt bleibt Arbeitsstand ohne Kanon-Promotion.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260429_035444.md
---
Jonas Merek Runtime Mind
========================

Status
------

- slug: jonas-merek
- owner_id: char:jonas-merek
- state: Arbeitsstand
- review_state: working
- baseline_cluster: ../../../../../../database-rp/01-factions/novapolis/07-mind-clusters/jonas-merek-mind-cluster.md
- session_id: d5-c6-nordlinie-sanierung-01
- last_turn: Turn 8

Runtime Carry-Forward
---------------------

- baseline_reading: technisch verlaesslicher, stressanfaelliger Werkstattanker mit hoher Improvisationsbereitschaft und laufender Lumen-Kopplung.
- current_mental_state: unter Werkstattdruck stabil funktionsorientiert; die Runtime belegt knappe, belastbare Rueckmeldungen statt hektischer Fehlversprechen, und Jonas bleibt dabei im belegten Lumen-Begleitfenster.
- confirmed_signals:
  - Jonas bleibt mit Pahl an der Draisine und Werkstattarbeit gebunden, statt freie Loesungen zu versprechen.
  - Die Rueckmeldungen aus D5 bestaetigen Bedarf, nennen harte Stopper offen und ziehen nur einen kleinen realen Behelfssatz nach.
  - Aus Sicht des laufenden Tunnels wirkt Jonas als verlaesslicher Teil der Material- und Antwortkette, nicht als diffuse Hintergrundfigur.
  - Jonas wird im aktuellen Runtime-Stand nicht allein gefuehrt; Lumen bleibt als gekoppelte Begleitinstanz Teil desselben D5-Arbeitsfensters.
- open_questions:
  - Ob die belastbar knappe Verlaesslichkeit bereits einen spuerbaren Vertrauensanstieg in Jonas' Achsen gegen Ronja oder Pahl erzeugt, ist noch nicht hart genug belegt.

Delta Candidates
----------------

```yaml
delta_candidates:
  - observer_id: char:jonas-merek
    target_id: char:ronja-kerschner
    target_type: character
    delta_class: tentative_shift
    hard_score_change: open
    relation_status: kooperativ
    event_refs: ["scene-log Turn 6", "scene-log Turn 7"]
    reason_codes: [RC-intel_share, RC-resource_share]
    applied_rules: [R-MCL-SSOT]
    runtime_note: Ronjas Bedarf wird von Jonas belastbar aufgenommen und in einen echten kleinen Behelfssatz uebersetzt; ein harter Rescore bleibt fuer Folgezuege offen.
  - observer_id: char:jonas-merek
    target_id: char:pahl-brenner
    target_type: character
    delta_class: carry_forward_confirmed
    hard_score_change: none
    relation_status: angespannt
    event_refs: ["scene-log Turn 4", "scene-log Turn 6"]
    reason_codes: [RC-intel_share]
    applied_rules: [R-MCL-SSOT]
    runtime_note: Jonas arbeitet weiter in derselben kontrollierten Werkstattkopplung mit Pahl; keine belegte Eskalation, aber auch keine klare Entspannung.
  - observer_id: char:jonas-merek
    target_id: char:reflex
    target_type: character
    delta_class: carry_forward_confirmed
    hard_score_change: none
    relation_status: kooperativ
    event_refs: ["scene-log Turn 7"]
    reason_codes: [RC-support]
    applied_rules: [R-MCL-SSOT]
    runtime_note: Die kleine Teilbereitstellung funktioniert in derselben D5-Tunnel-Kette, in der Reflex als koerpernahe Assistenz mitgedacht bleibt; keine neue Reibung erkennbar.
  - observer_id: char:jonas-merek
    target_id: char:lumen
    target_type: character
    delta_class: carry_forward_confirmed
    hard_score_change: none
    relation_status: kooperativ
    event_refs: ["scene-log Turn 1", "scene-log Turn 6", "scene-log Turn 7"]
    reason_codes: [RC-support]
    applied_rules: [R-MCL-SSOT]
    runtime_note: Jonas bleibt im aktiven Hauptpfad im belegten Lumen-Naehefenster; die Begleitlogik war bislang im Runtime-Slice untererfasst, wird hier aber explizit nachgezogen.
```

Promotion Notes
---------------

- Erst promoten, wenn die naechsten Folgezuege zeigen, ob Jonas' verlaesslicher Antwortstil dauerhaft als Vertrauensgewinn oder nur als bestaetigte Werkstattfunktion gelesen wird.
