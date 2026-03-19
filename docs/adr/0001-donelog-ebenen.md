---
stand: 2026-03-19 11:09
update: Akzeptierte Architekturentscheidung fuer die normalisierten DONELOG-Ebenen dokumentiert.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260318_052318.md
---

ADR 0001: DONELOG-Ebenen normalisieren
======================================

- Status: accepted
- Datum: 2026-03-18

Kontext
-------

- Das Repository fuehrt operative Status- und Verlaufsinformationen parallel auf Root-, Dev- und Report-Ebene.
- Ohne klare Ebenentrennung drohen doppelte Eintraege, unklare Zustaendigkeiten und schwer lesbare aktive Oberflaechen.
- Die aktuelle Governance unterscheidet bereits zwischen Root-Summary, Dev-Current-Window und technischen Laufartefakten, diese Unterscheidung war aber bisher nur in Referenzdokumenten beschrieben.

Entscheidung
------------

- Die DONELOG-Struktur wird verbindlich in drei Ebenen normalisiert:
  - Ebene A: `novapolis-dev/docs/donelog.md` als menschenlesbares Current-Window fuer operative Entscheidungen und laufende Fortschritte.
  - Ebene B: `.tmp/results/reports/**` als maschinenlesbare Detail- und Laufbelege.
  - Ebene C: `DONELOG.md` als kurze Root-Summary fuer Governance-, Release- und Workspace-weite Entscheidungen.
- Jede Mutation im aktiven Scope wird im passenden Modul-DONELOG dokumentiert; Root-relevante Aenderungen erhalten zusaetzlich einen knappen Summary-Eintrag in `DONELOG.md`.
- Aktive Oberflaechen bleiben bewusst kurz. Historische Detailketten werden nicht in den aktiven Logs gehalten, sondern in die vorgesehenen Archivpfade ausgelagert.

Konsequenzen
------------

- Leser finden operative Detailhistorie und Root-Summary schneller, ohne zwischen gemischten Logformaten springen zu muessen.
- Neue Aenderungslaufe muessen bewusst entscheiden, welche Ebene den Eintrag traegt; redundante Volltexte in mehreren Logs sind unerwuenscht.
- Reports unter `.tmp/results/reports/**` bleiben die technische Wahrheitsquelle fuer Check- und Testdetails; die beiden menschenlesbaren DONELOG-Ebenen verweisen nur knapp auf diese Artefakte.

Verweise
--------

- `README.md` (Abschnitt `DONELOG-Ebenen (normalisiert)`)
- `novapolis-dev/docs/donelog.md`
- `DONELOG.md`
- `.github/copilot-instructions.md` (`R-DONELOG`)