---
stand: 2026-02-16 12:01
update: Preisbänder (Heuristik) als Economy-Subdoc ergänzt.
checks: not run (not requested)
slug: novapolis-pricebands
category: Economy
schemaVersion: 1
language: de
tags: [rp, economy, novapolis]
status: active
owners: [admin-novapolis]
relatedSlugs: [reference-campaign-state, marktpreise-inventar]
---

Preisbänder (Novapolis, Heuristik)
=================================

Zweck
-----
Diese Datei hält **fraktionsspezifische Preisbänder** als Heuristik fest (ohne harte Zahlen). Konkrete Preise werden bei Bedarf im Handelslog dokumentiert.

Preisband-Skala
---------------
- **Band S (sehr günstig)**: häufig verfügbar / leicht ersetzbar / geringe Risikokosten.
- **Band N (niedrig)**: verfügbar, aber mit Varianz; kleine Engpässe möglich.
- **Band M (mittel)**: planbar, aber abhängig von Lieferfenstern/Beständen.
- **Band H (hoch)**: knapp, risikobehaftet, sicherheitskritisch oder technisch anspruchsvoll.
- **Band X (extrem)**: selten, missionskritisch, nur mit Sonderfreigabe.

Währung (Reference): Kugeln (neu vs gebraucht)
----------------------------------------------

- Kugeln sind die Standard-Währungseinheit im Feld.
- Zwei Wertstufen:
  - Kugeln (neu) = hochwertige Währung.
  - Kugeln (gebraucht) = Alltags-Währung.
- Faustregel: **1 Kugel (neu) ≈ 10 Kugeln (gebraucht)**.
- Die Quote kann lageabhängig schwanken (typisch 1:8 bis 1:12), Standard bleibt 1:10.
- Gebrauchte Kugeln bleiben die häufigste Hauptmunition im Alltag; Qualität streut.

Artikelgruppen (Startliste)
--------------------------

|Gruppe|Band (typisch)|Hinweise|
|---|---:|---|
|KUGELN (gebraucht)|N–M|Haupttauschmittel; Qualität streut; Zustand zählt|
|KUGELN (neu)|H–X|Reserve/Schlüsselgut; nur kontrolliert|
|Energiezellen / Energiematerial|M–H|Abhängig von Technik/Netzlage|
|Werkzeuge/Standardteile|N–M|D5 kann vieles intern halten/repairen|
|Medizin / Desinfektion / Antibiotika|H–X|Engpassanfällig; Vertrauens-/Protokollpflicht|
|Filter / Masken / Atemschutz|M–H|Sicherheitsrelevant, Nachfrage schwankt|
|Elektronik / Sensorik|H|Reparaturfähig, aber Teile knapp|
|Informationen / Lagebilder|M–X|Wert hängt von Aktualität/Risiko ab|

Abgleich & Pflege
-----------------
- Baseline/Global: siehe Marktpreise-Inventar.
- Fraktionslog: Abweichungen/Deals stets im Handelslog verankern.

Verweise
--------
- Baseline-Preise: ../../04-inventory/Marktpreise-inventar.md
- Handelslog: ../06-handel-diplomatie/Handelslog-Novapolis.md
- Referenz (Währung): ../../00-admin/Reference-Campaign-State.md
