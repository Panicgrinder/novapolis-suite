---
stand: 2026-02-23 06:22
update: Nutzerkommentare eingearbeitet (C6-SQM/C6-HELPERS/Priorisierung Transferlogik) und Patchreihenfolge präzisiert.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-02-23 06:22); .\.venv\Scripts\python.exe scripts\check_frontmatter.py "novapolis-dev/docs/process/rp-canvas-rescue/delta-audit-2026-02-23.md" "novapolis-dev/docs/donelog.md" PASS (EXITCODE=0, 2026-02-23 06:22)
---

Delta-Audit RAW/Curated ↔ SSOT (Novapolis)
==========================================

Scope
-----

- Quellenbasis: RAW-Exporte (`database-raw/99-exports`), Curated-Staging (`database-curated/staging/reports`), SSOT (`database-rp/01-factions/novapolis/**`, Admin-SSOTs).
- Ziel: Prüfen, ob wichtige, bereits als „entschieden“ markierte Fakten tatsächlich in kanonischen SSOT-Dateien angekommen sind.

Methodik
--------

- Schritt 1: High-Signal-Marker aus RAW/Curated gescannt (u. a. C6-Fläche, C6-Helfer, D5-Energie, Inventartrennung).
- Schritt 2: Marker gegen SSOT-Vorkommen gegengeprüft (inkl. Szenenanker vs. kanonische Fachdateien).
- Schritt 3: Delta-Kandidaten in Klassen eingeteilt: `abgedeckt`, `teilweise`, `fehlt`, `bewusst-offen`.

Abgedeckt (kein unmittelbarer Patchbedarf)
------------------------------------------

- D5-Reaktor-Status/Teilversorgung C6 (inkl. 98→100 als RAW-Hinweis) ist in der Novapolis-Logistik verankert.
- Inventartrennung D5/C6 und „Transfer nur via Mission/Logistik“ ist mehrfach kanonisch hinterlegt.
- Karawanen-Führungs-Split (Kora/Marven/Arlen) ist in C6/Personenindex/Handelsdokumenten bereits aufgegriffen.
- Draisine-Policy (kein Personentransport Erstlauf; konservative Last) ist in Projekt-/Reference-Ebene abgebildet.

Bestätigte Deltas (priorisiert)
-------------------------------

1) P1 - C6-SQM fehlt in SSOT-Fachdateien

- Curated-Taglage: `C6-SQM` als entschieden markiert.
- RAW-/Curated-Anker: C6 mehrfach mit „440 m² nutzbar“ inkl. A/B/C-Aufteilung genannt.
- SSOT-Check: In kanonischen C6-Fachdateien kein belastbarer m²-Wert auffindbar; nur allgemeiner Zustands-/Nutzungsstatus.
- Risiko: Flächenabhängige Logistik-/Ausbauentscheidungen laufen ohne harte Bezugsgröße.
- Umsetzungsvermerk (Projektabstimmung): m²-Wert wird projektkonform neu festgelegt; A/B/C-Aufteilung bleibt erhalten, sofern sie operativ sinnvoll und konsistent bleibt.

2) P1 - C6-HELPERS nur indirekt, nicht kanonisch ausgerollt

- Curated-Taglage: `C6-HELPERS` als entschieden markiert.
- RAW-/Curated-Anker: 6 Karawanenmitglieder in C6; drei feste Bewohner (`Mikk`, `Lira`, `Darek`) explizit benannt.
- SSOT-Check: Keine kanonischen Charakterdateien für `Mikk`, `Lira`, `Darek`; keine belastbare Namensverankerung in C6-Rosterdateien.
- Risiko: Personen-/Verantwortungsdrift in Szenen und Missionslogik (insb. bei Inventar- und Wachdiensten).
- Arbeitsdefinition (für Folgepatch): `C6-HELPERS` bezeichnet die C6-Unterstützer für Tunnelinstandsetzung/Transport/Absicherung im Umfeld Nordlinie.

3) P2 - Inventar-Transfermengen weiterhin bewusst offen

- Curated/RAW melden wiederholt Lücke „wer hat was/wieviel wohin bewegt“.
- SSOT-Check: Diese Lücke ist als offen dokumentiert (kein Widerspruch), aber weiterhin ohne belastbare Mengenbuchung.
- Bewertung: Kein Inkonsistenzfehler, jedoch weiterhin operatives Risiko für künftige Tages-/Wochenabrechnungen.
- Priorisierungsvermerk: Vor Feingranularisierung der Transfermengen zunächst Nicht-Spieler-Fraktionen mit Basisvorräten und interner Logistik konsistent stabilisieren.

4) P2 - Währung „Kugeln“: Definition vorhanden, Bestände weiterhin tbd

- Curated-Unsicherheit bestätigt explizit noch offenen Quantifizierungsbedarf.
- SSOT-Check: Regelwerk (neu/gebraucht, Faustregel) ist vorhanden; Bestandszahlen bleiben offen.
- Bewertung: Erwartungskonform offen, aber weiterhin als aktiver Nachzugspunkt zu behandeln.

Nicht als Delta gewertet (False-Positive-Schutz)
------------------------------------------------

- Rohangaben wie „+10 Energiezellen/Tag“/„2 statt 4“ werden aktuell nicht als harte Kanonwerte erzwungen, da sie in SSOT bewusst als RAW-Hinweis bzw. nicht-kanonisierte Kennzahl geführt werden.
- Szenenanker allein zählen nicht als vollwertige Fachdaten-Absicherung, sind aber als Evidenzbrücke korrekt verwendet.

Empfohlene Patch-Reihenfolge
----------------------------

1. `C6-SQM` kanonisch nachziehen (mit Evidenzanker und ggf. „verifiziert/unter Vorbehalt“ Label) in C6-Fachdatei.
2. `C6-HELPERS` kanonisch schließen (mind. Roster-Eintrag + Rollenanker für `Mikk`, `Lira`, `Darek`; optional eigene Charakter-SSOTs).
3. Nicht-Spieler-Fraktionen zuerst mit belastbaren Basisvorräten und interner Logistik konsolidieren.
4. Inventar-Transferlog-Template um Pflichtfelder „Menge/Quelle/Ziel/Belegzeile“ verschärfen.
5. „Kugeln“-Bestände erst nach belastbarer Beleglage quantifizieren (kein RAW-only Hardcoding).

Audit-Entscheidung
------------------

- Erste Rescue-Pässe waren strukturell erfolgreich, aber semantisch nicht vollständig: Es bleiben mindestens zwei hochrelevante Kanon-Lücken (`C6-SQM`, `C6-HELPERS`).
- Damit ist die Nutzerannahme („wichtige Daten könnten initial übersehen worden sein“) fachlich bestätigt.
