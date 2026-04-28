---
stand: 2026-04-29 00:59
update: Marktflaechen fuehren jetzt den aktuellen Kanon fuer breite Handels- und Bedarfsklassen von C6.
checks: snapshot-lock PASS (2026-04-29 00:59)
slug: novapolis-markets
category: Economy
schemaVersion: 1
language: de
tags: [rp, economy, novapolis]
status: active
owners: [admin-novapolis]
relatedSlugs: [reference-campaign-state, marktpreise-inventar, handelslog_novapolis_v1, relationslog_novapolis_v1]
---

Märkte & Handelsplätze (Novapolis)
=================================

Überblick
---------
Novapolis trennt **interne Versorgung** (D5) strikt von **Außenhandel** (C6). Der Außenhandel läuft ausschließlich über kontrollierte Übergaben/Protokolle und wird im Handels-/Relationslog gespiegelt.

Handelsplatz D5 (intern)
------------------------
- Zweck: Versorgung, Werkstatt- und Missionsbedarf; keine offenen Außenkontakte.
- Zugang: Kernteam + autorisierte Trupps; Ausgabe über Quartiermeisterin (Nika Perez).
- Typische Güter (Beispiele): Werkzeuge/Teile, Schutzkleidung, Verbrauchsmaterial, Energiezellen.

Handelsplatz C6 (Außenhandel)
-----------------------------
- Zweck: kontrollierter Außenhandel / Übergabepunkt.
- Leitung/Koordination: Kora Malenkov (C6) in Abstimmung mit Ronja (Diplomatie/Freigaben) und Pahl (Sicherheitslage).
- Zugang: Nur über Freigabe + dokumentiertes Lieferfenster; Koordinatenschutz hat Vorrang.
- Typische Gueter (Beispiele): Tauschware, Rohmaterialien, Ersatzteile, Grundbedarfsgueter, Munition/Waehrungseinheiten (KUGELN), Informationsgueter, Medizinische Gueter.

Regeln (Kurz)
-------------
- Währung/Einheiten: siehe Reference (KUGELN neu/gebraucht).
- Jede Übergabe wird protokolliert (mindestens: Partei, Güter, Band/Schätzung, Risiko, Freigaben).
- Keine direkten Außenkontakte über D5; C6 ist der einzige Außenhandels-Knoten.

Verweise
--------
- Handelslog: ./Handelslog-Novapolis.md
- Relationslog: ./Relationslog-Novapolis.md
- Baseline-Preise: ../../../04-inventory/Marktpreise-inventar.md
- Referenz (Währung/Regeln): ../../../00-admin/Reference-Campaign-State.md
