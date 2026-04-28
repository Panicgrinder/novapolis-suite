---
stand: 2026-04-28 05:46
update: Runtime-Mind-Dateien fuehren jetzt geistnahe und relationale Delta-Lesarten getrennt vom kanonischen Mind-Cluster-SSOT und sind gegen den RP-Doku-Slice validiert.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260428_052348.md; snapshot-lock PASS (2026-04-28 05:46)
---

Runtime Mind
============

Zweck
-----

Hier werden Mind-/Sphaeren-Arbeitsstaende gesammelt, die waehrend RP entstehen oder bestaetigt werden.

- geistnaher Zustand unter Runtime-Druck
- gerichtete relationale Delta-Lesarten gegen bestehende Mind-Cluster
- bestaetigte Carry-Forwards ohne freien Zahlenersatz
- offene Review-Fragen vor Promotion in die eigentliche Mind-Cluster-SSOT

Dateikontrakt
-------------

- Eine Datei pro Beobachter-/Entitaetstraeger: `mind/<slug>.md`
- Die Runtime-Datei ersetzt nie den Mind-Cluster unter `database-rp/**/07-mind-clusters/`, sondern fuehrt nur Arbeitsstand und Delta-Lesart.
- Wenn kein harter Rescore belastbar ist, wird `carry-forward bestaetigt` oder `Score-Shift offen` notiert statt Scheinpraezision zu erfinden.
- Relationale Eintraege bleiben gerichtet (`observer -> target`).
- Promotion in die eigentliche Mind-Cluster-SSOT erfolgt erst nach Review.

Pflichtinhalte
--------------

- Referenz auf die baseline-Mind-Cluster-Datei
- Session- und Turn-Anker fuer die Runtime-Evidenz
- aktueller geistnaher Zustand als Arbeitslesart
- Delta-Kandidaten pro betroffener Zielentitaet
- offene Fragen oder bewusst noch nicht gezogene Scores

Nicht hierher
-------------

- reine Welt-, Orts- oder Projektfolgen ohne geistnahe/relationale Wirkung
- allgemeine Taxonomien, Regeln oder Preisbaender
- fertige Kanon-Promotion ohne Review
