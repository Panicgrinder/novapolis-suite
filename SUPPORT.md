---
stand: 2026-03-19 11:09
update: Support- und Meldewege fuer externe Mitwirkende und Nutzer dokumentiert.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260318_052318.md
---

Support
=======

Zweck
-----

Dieses Dokument erklaert, welcher Kanal fuer welche Art von Rueckfrage oder Meldung gedacht ist.

Wofuer welcher Kanal?
---------------------

- Allgemeine Fragen zur Nutzung, Struktur oder lokalen Ausfuehrung:
  - GitHub Issue mit klarer Fragestellung oder reproduzierbarem Kontext.
- Fehlerberichte:
  - GitHub Issue ueber das Bug-Template.
- Verbesserungsvorschlaege und Feature-Wuensche:
  - GitHub Issue ueber das Feature-Template.
- Sicherheitsrelevante Meldungen:
  - nicht oeffentlich posten; stattdessen `SECURITY.md` folgen.
- Verhaltensbezogene Meldungen:
  - `CODE_OF_CONDUCT.md` folgen.

Was eine gute Rueckfrage oder Meldung enthalten sollte
------------------------------------------------------

- betroffener Pfad oder Teilbereich
- beobachtetes Verhalten
- erwartetes Verhalten
- reproduzierbare Schritte oder konkrete Frage
- relevante Umgebung (`OS`, Python-Version, Tool/Task)
- falls vorhanden: Reportpfad oder kurzer Log-Auszug

Erwartungsmanagement
--------------------

- Das Repository wird aktiv gepflegt, aber ohne garantierte Antwortzeit ausserhalb des in `SECURITY.md` dokumentierten Security-SLAs.
- Maintainer priorisieren reproduzierbare Bugs, Sicherheitsrelevanz, Governance-Drift und rote Pflichtchecks.
- Unklare oder nicht reproduzierbare Meldungen koennen Rueckfragen benoetigen, bevor eine Bearbeitung beginnt.

Verwandte Dokumente
-------------------

- `CONTRIBUTING.md`
- `SECURITY.md`
- `CODE_OF_CONDUCT.md`
- `MAINTAINERS.md`
