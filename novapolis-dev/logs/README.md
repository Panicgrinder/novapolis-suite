---
stand: 2026-03-05 01:00
update: Logs-Policy geschaerft: `*.tmp.md` im aktiven Logpfad verboten; Rohlogs in Quarantaene archivieren.
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=PASS; frontmatter=PASS; path-portability=FAIL; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260305_005843.md
---

<!-- markdownlint-disable MD022 MD041 -->

Betriebsmodus-Logs
==================

Dieses Verzeichnis hält Rohlogs und verdichtete Zusammenfassungen aus Sitzungen im Sicherheitsprotokoll. Rohlogs bleiben lokal, nur ausgewählte Auszüge oder Nachweise können ins Repository aufgenommen werden.

Benennung
---------

- Rohlog (lokal, nicht commiten): `betriebsmodi-YYYYMMDD-HHMM.tmp.md`
- Verdichtete Zusammenfassung (commitbar): `betriebsmodi-YYYYMMDD-HHMM.md`

Policy (verbindlich)
--------------------

- Im aktiven Pfad `novapolis-dev/logs/` sind keine `*.tmp.md` Dateien erlaubt.
- Rohlogs werden nach Sichtung in `novapolis-dev/archive/quarantine/logs/` verschoben.
- Nur kuratierte, commitbare Zusammenfassungen (`*.md` ohne `.tmp`) bleiben unter `novapolis-dev/logs/`.
- Technischer Gate-Check: `scripts/check_logs_policy.py`.

Inhalt
------

1. YAML-Frontmatter mit `stand`, `aufgabe`, `modus`, `checks`, optional `drift`.
2. Abschnitt "Expected State" gemäß Vorlage.
3. Pakete à 3-5 Operationen mit Zeitstempel, Aktionen, IST/SOLL-Abgleich, Driftbewertung, Folgeschritte.
4. Abschlussblock "Auswertung" mit Befund, getesteten Checks, offenen Risiken.

Rotation (lokal)
-----------------

- Maximal fünf Rohlogs parallel aufbewahren.
- Ältere Rohlogs archivieren oder löschen, nachdem die Zusammenfassung erstellt wurde.
- Nur finale Zusammenfassungen ins Repo aufnehmen.

Vorlage
-------

Siehe `log-template.md` in diesem Ordner. Kopiere die Datei und passe Inhalte an.


