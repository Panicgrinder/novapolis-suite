---
stand: 2025-11-16 06:52
update: MD003: H1/H2 auf Setext umgestellt
checks: markdownlint-cli2 PASS (single file)
---

<!-- markdownlint-disable MD022 MD041 -->

Betriebsmodus-Logs
==================

Dieses Verzeichnis hält Rohlogs und verdichtete Zusammenfassungen aus Sitzungen im Sicherheitsprotokoll. Rohlogs bleiben lokal, nur ausgewählte Auszüge oder Nachweise können ins Repository aufgenommen werden.

Benennung
---------

- Rohlog (lokal, nicht commiten): `betriebsmodi-YYYYMMDD-HHMM.tmp.md`
- Verdichtete Zusammenfassung (commitbar): `betriebsmodi-YYYYMMDD-HHMM.md`

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


