---
stand: 2026-04-29 03:56
update: In entity-centric Runtime-Dossier migriert; Inhalt bleibt Arbeitsstand ohne Kanon-Promotion.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260429_035444.md
---
Kora Malenkov Runtime Mind
==========================

Status
------

- slug: kora-malenkov
- owner_id: char:kora-malenkov
- state: Arbeitsstand
- review_state: working
- baseline_cluster: ../../../../../../database-rp/01-factions/novapolis/07-mind-clusters/kora-malenkov-mind-cluster.md
- session_id: d5-c6-nordlinie-sanierung-01
- last_turn: Turn 11

Runtime Carry-Forward
---------------------

- baseline_reading: kontrollierte Logistik- und Sicherheitskoordinatorin mit hoher Prozessdisziplin und Echo-Kopplung.
- current_mental_state: angespannt, aber klar strukturiert; Kora zieht die lokale C6-Lage enger zusammen, verteilt Bewohnerarbeit und liest den Bericht des C6-Tunneltrupps als Stationsaufgabe statt als freie Entlastungszusage.
- confirmed_signals:
  - Kora haelt C6 in Turn 9 bewusst auf enger Annahme-, Sichtungs- und Schutzlogik.
  - Der Weltzug bestaetigt ihre Grundlesart `Sicherheit vor Tempo` statt spontaner Entlastungsversprechen.
  - Echo bleibt dabei lokal an ihrer Seite und wird nicht in freie Distanzlogik gedrueckt.
  - Turn 11 bestaetigt dieselbe Disziplin: Kora verteilt C6-Bewohnerarbeit weiter und verarbeitet den Tunnelbericht getrennt von Ronjas D5-Perspektive.
- open_questions:
  - Ob aus der verdichteten C6-Disziplin im naechsten Folgezug ein staerkerer Vertrauens- oder Belastungseffekt gegen D5 oder H-47 entsteht, bleibt offen.

Delta Candidates
----------------

```yaml
delta_candidates:
  - observer_id: char:kora-malenkov
    target_id: char:echo
    target_type: character
    delta_class: reaffirmed
    hard_score_change: none
    relation_status: kooperativ
    event_refs: ["scene-log Turn 9"]
    reason_codes: [RC-support]
    applied_rules: [R-MCL-SSOT]
    runtime_note: Echo bleibt in der enger gezogenen C6-Lage lokal an Kora gebunden und bestaetigt die Schutzachse erneut.
  - observer_id: char:kora-malenkov
    target_id: char:mara-quell
    target_type: character
    delta_class: carry_forward_confirmed
    hard_score_change: none
    relation_status: kooperativ
    event_refs: ["scene-log Turn 9"]
    reason_codes: [RC-intel_share]
    applied_rules: [R-MCL-SSOT]
    runtime_note: Die H-47-/G7-Kante bleibt fuer Kora bestaetigungsorientiert lesbar; kein neuer Konflikt, aber auch keine freie Entspannung.
  - observer_id: char:kora-malenkov
    target_id: group:c6-bewohner
    target_type: group
    delta_class: carry_forward_confirmed
    hard_score_change: none
    relation_status: kooperativ
    event_refs: ["scene-log Turn 11"]
    reason_codes: [RC-support]
    applied_rules: [R-MCL-SSOT]
    runtime_note: Kora verteilt die C6-Bewohnerarbeit weiter als Stationsaufgabe; keine harte neue Mind-Delta, aber der Bewohner-/Schichtdruck bleibt bestaetigt.
```

Promotion Notes
---------------

- Erst promoten, wenn ein Folgezug zeigt, ob Kora aus der engen Annahme- und Berichtsauswertungslogik in eine echte Uebergabe-, Konflikt- oder Entlastungsdynamik kippt.
