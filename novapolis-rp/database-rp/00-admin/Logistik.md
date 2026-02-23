---
stand: 2026-02-23 03:59
update: Frische-Review durchgeführt; globales Logistik-Regelwerk und Verweise weiterhin gültig (kein Kanon-Delta).
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/00-admin/Logistik.md' PASS (2026-02-23 04:00); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/Logistik.md' PASS (2026-02-23 04:00); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-23 04:00)
canvas: Logistik
last_updated: 2025-11-07T04:09:00+01:00
category: admin
slug: logistik
version: 0.9
---

Logistik (Globales Regelwerk)
=============================

Hinweis (Scope)
---------------

Dieses Dokument ist eine Admin-/Reference-Sicht (inkl. Tabellen/Constraints).
Fraktions-/Stationsspezifische Operativstände werden **nicht** hier gepflegt,
sondern in den jeweiligen Fraktions-Doctrines unter `01-factions/*/00-doctrine/`.

System-/Meta-Notizen gehören nach [Ops / Systemnotes](../00-ops/README.md).

Fokus: Energie-Konten, Generatoren, Leitungen, Ladefenster, Prioritäten, Transportketten, Beleg-Fluss, Materialien/Bestände.

Energie-Konten (generisch)
--------------------------

- Primärstation: Produktion/Verbrauch (kWh, Speicher-%)
- Außenposten: Verbrauch/Teilversorgung (abhängig von lokaler Erzeugung + Transfer)

Tagesabschluss (Buchungen, minimal)
----------------------------------

- Konten (spielbar, Muster)
  - `ENERGY_PRIMARY_CELLS` (Speicher-%)
  - `ENERGY_OUTPOST_CELLS` (Speicher-%)
  - `ENERGY_PIPELINE_PRIMARY_OUTPOST` (Leitung aktiv/limitiert/aus)
- Konten (Hintergrund/Meta, Muster)
  - `ENERGY_PRIMARY_BASELOAD_KWH` (Lebenserhalt + Grundlast)
  - `ENERGY_OUTPOST_BASELOAD_KWH` (Grundlast + Monitoring)

- Tagesabschluss-Regel (einfach):
  - 1) Grundlast buchen (Primärstation/Außenposten)
  - 2) Projekt-/Mission-Lasten buchen
  - 3) Transfer buchen (Primärstation → Außenposten), wenn Leitung aktiv und Speicher vorhanden
  - 4) Ergebnis als Kurzzeile protokollieren (Bilanz + 1 Satz Ursache)

Beispielbuchung
--------------

- Tag X: Primär −8 (Grundlast), Außenposten −12 (Grundlast + Monitoring), Transfer +10 ⇒ Netto Primär −18, Außenposten −2

Generatoren
-----------
- Energiequellen je Station werden im fraktionsspezifischen Operativkontext gepflegt.
- Im Admin-Dokument werden nur Modellregeln/Constraints geführt.

Leitungen/Schaltzustände
------------------------
- Leitungsstatus je Streckenabschnitt fraktionsspezifisch pflegen.
- Einschränkungen definieren (Infrastruktur limitiert reale Versorgung).

Constraints (global)
--------------------

- Keine Instandsetzung/Leistungsangaben ohne belegte Schritte behaupten.
- Inventar-/Transferänderungen nur nach belegten Einträgen nachziehen.
- Retcons vermeiden; Korrekturen explizit dokumentieren.

Inventar-Transfers (Policy)
---------------------------

- Inventare stationenspezifisch getrennt führen.
- Transfers nur über Mission/Logistik mit Quelle/Ziel buchen.
- Physisch getrennte Standorte grundsätzlich als getrennte Inventar-/Produktionsräume behandeln.

Ladefenster / Prioritäten
-------------------------
- Ladefenster pro Tag (Start/Ende)
- Prioritätenmatrix: Lebenserhalt > Sicherheit > Produktion > Komfort

Transportketten
---------------
- Quelle → Transport → Ziel; Kapazitäten/Wege; Engpässe

Beleg-/Quittungsfluss
---------------------
- Standardfluss: Entnahme (Quelle/Canvas) → Transport → Ankunft (Ziel/Canvas) → Belege/Quittungen → Verantwortliche

Materialien / Bestände
----------------------
- Bestandsliste mit Einheiten (kg/t, m, m², m³, kWh, Zellen-%)
- Trigger für Skalierung (SUPPLY) - Low/Med/High Stufen
- Waehrung "Kugeln" als Inventar-Item (neu/gebraucht)

Wochenzyklus (globales Muster)
------------------------------

- Zyklus: täglicher Kurzabschluss + wöchentliche Konsolidierung.
- Wöchentliche Pflichtpunkte: Delta-Liste (Bestände/Transfers), offene Bedarfe, Risiken/Blocker, Freigabe-/Prioritätsupdate.
- Ergebnisformat: kompakter Wochenreport mit Verweisen auf Tagesabschlüsse und betroffene Inventar-/Missionslogeinträge.

Lagerstände (globales Muster)
-----------------------------

- Lagerstände werden pro Standort geführt (Primärstation/Außenposten), nicht als gemischter Gesamtwert.
- Mindestfelder je Eintrag: Item, Status (`verbucht/offen`), Quelle (Mission/Beleg), letzte Änderung.
- Ohne belastbare Quelle bleiben Mengen/Kennzahlen `tbd`.

Versionierung & Referenzschema
------------------------------

- Kanonische Referenzierung über Slugs/Pfade (z. B. `logistik`, `novapolis-logistics`) statt Legacy-Versionstokens (`*_v1`, `*_v2`).
- Legacy-Bezeichner aus RAW dürfen als Hinweis bestehen, aber nicht als primäre SSOT-ID.

Scoping-Regel (Admin vs. Fraktion)
----------------------------------

- `00-admin/Logistik.md`: globales Regelwerk (Modelle, Buchungslogik, Constraints, Flows).
- `01-factions/*/00-doctrine/*-logistics.md`: fraktions-/stationsspezifische Operativlagen.
- Beispiel Novapolis: `../01-factions/novapolis/00-doctrine/novapolis-logistics.md`.

Verlinkungen
------------
- [Missionslog](./Missionslog.md)
- [Admin: Day-Switch & Debug](./Canvas-Admin-Day-Switch-Debug.md)
- [Admin: Timeline (T+0)](./Canvas-T0-Timeline.md)
- [Admin: Warenueberblick (T0)](./Warenueberblick-T0.md)
- [Admin: Stationskontroll-Matrix](./Stationskontroll-Matrix.md)
- [Process-Workflow](./Process-Workflow.md)
- [Index-Rules](./index-rules.md)
- [Beispiel Fraktions-Doctrine: Novapolis-Logistics](../01-factions/novapolis/00-doctrine/novapolis-logistics.md)


