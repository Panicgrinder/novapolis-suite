---
stand: 2026-03-30 05:08
update: Phase-2-Konsistenzlauf zieht das Log-README auf den aktuellen PASS-Kontext und die aktive Logs-Policy ohne Alt-Receipt nach.
checks: snapshot-lock PASS; markdownlint PASS; frontmatter PASS; todo-index PASS; naming-policy PASS; path-portability PASS; logs-policy PASS; doc-freshness PASS; scan-links PASS; validate-rp PASS (2026-03-30 05:08)
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


