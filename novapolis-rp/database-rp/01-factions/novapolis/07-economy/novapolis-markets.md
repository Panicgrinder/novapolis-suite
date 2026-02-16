---
stand: 2026-02-16 12:01
update: Märkte/Handelsplätze (D5/C6) als Economy-Subdoc ergänzt.
checks: not run (not requested)
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
- Typische Güter (Beispiele): Tauschware, Ersatzteile, Munition/Währungseinheiten (KUGELN), Informationen, medizinische Versorgung.

Regeln (Kurz)
-------------
- Währung/Einheiten: siehe Reference (KUGELN neu/gebraucht).
- Jede Übergabe wird protokolliert (mindestens: Partei, Güter, Band/Schätzung, Risiko, Freigaben).
- Keine direkten Außenkontakte über D5; C6 ist der einzige Außenhandels-Knoten.

Verweise
--------
- Handelslog: ../06-handel-diplomatie/Handelslog-Novapolis.md
- Relationslog: ../06-handel-diplomatie/Relationslog-Novapolis.md
- Baseline-Preise: ../../04-inventory/Marktpreise-inventar.md
- Referenz (Währung/Regeln): ../../00-admin/Reference-Campaign-State.md
