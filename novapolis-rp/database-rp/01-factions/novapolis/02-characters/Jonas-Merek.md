---
stand: 2026-02-04 13:31
update: Verweis auf Lumen-Canvas relativiert.
checks: "npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-02-04 13:31)"
title: Jonas Merek
category: character
slug: jonas-merek
version: "1.0"
last_updated: 2026-01-11T01:40:00+01:00
last_change: "Upgrade aus RAW char_jonas_v2 (korrupt) + resolved #[JONAS-SIS]"
tags: ["werkstatt", "novapolis"]
affiliations: ["novapolis"]
dependencies: ["lumen", "d5", "missionslog", "ai_behavior_index_v2"]
primary_location: d5
last_seen: d5
---

<!-- markdownlint-disable MD025 -->

Jonas Merek
===========

- Meta: last-updated: 2025-11-07T03:32:00+01:00
- Verhaltenssignatur: `JNS3=L55-T68-N40-E72-O50-C42-M78-P32-ab` - sicherheitsorientiert, hilfsbereit, driftet bei Überlast in Fluchtreflexe.
- Rolle: Technikerlehrling/Mechaniker; betreut Werkstatt & Materiallauf in D5 (Quelle: RAW char_jonas_v2)
- Werte: Kraft 3, Geschick 5, Geist 3, Wille 4, Charisma 3
- Skills:
  - Geübt: Mechanik, Reparaturen, Materialkunde
  - Meisterhaft: Improvisation, Werkzeugarbeit
  - Optional: Energieverteilung/Notversorgung
- Ausrüstung: Werkzeugkasten (modular), Messgeräte, Schutz- und Filterausrüstung, mobile Terminalverbindung zu C6 (Quelle: FACT COMMS-PROTO)
- Motivation: Zugehörigkeit zur Novapolis-Crew sichern; Werkstatt als sicheren Anker aufbauen
- Makel: Trauma-Trigger (Gasgeruch, abgeschlossene Räume); anhaltende Schuldgefühle wegen der vermissten Schwester (Status: vermisst/unklar, siehe FACT [JONAS-SIS]); Schlafstörungen bei Hochlast

Hintergrund & Herkunft
----------------------

- Herkunft: Station E2, Überlebender des Gasunfalls; Evakuierung über Tunnelknoten, Schwester seitdem vermisst (kein Todesnachweis).
- Fluchtweg: Jonas entkam über Nebengänge/Schächte in einen Tunnelabschnitt; Ronja fand ihn beim ersten Verlassen der Station, brachte ihn zurück und versorgte ihn.
- Aufgenommen nach Mission „C6-Aufnahme Jonas“ (siehe FACT [C6-FIRST]); arbeitet unter Aufsicht von Ronja und Reflex.
- Lumen ist an Jonas gekoppelt (Nähe-Kopplung stabilisiert beide, Quelle: FACT? [PROXIMITY]).

Rollen & Verantwortlichkeiten (Pflichtfelder)
---------------------------------------------

- Werkstatt & Fertigung - Reparaturen, Prototypen (Draisine/Transportmodul), Wartung D5-Infrastruktur.
- Logistik - Materialläufe dokumentieren, Schnittstelle zum Missionslog (Freigaben über Ronja, Abgleich mit Missionslog Prozess L.1).
- Kommunikation - Terminal/Funkbrücke D5↔C6 bedienen, Statusberichte an Marei/Kora koordinieren (Quelle: FACT [COMMS-PROTO]).

Zugehörigkeit & Standort
------------------------

- Zugehörigkeit: Novapolis (D5).
- Status: aktiv, unter Supervision; keine Außenmissionen ohne Begleitung.
- Letzter bekannter Einsatz: D5 Werkstattbereich (Schichtplan rotierend, Abstecher C6 nur mit Freigabe).

Wissensstand (Matrix - Auszug)
------------------------------

- Intern: Kennt D5-Systeme, Lumen-Kopplungsregeln, Grundzüge von Reflex’ Präsenz (Need-to-know). Zugang zu Wartungslog und Missionslog Einträgen der Werkstatt.
- Extern: Kennt Karawanen-Schnittstelle C6 (Logistik), Evakuierte aus E3 und Echo als Reflex-Instanz an Koras Seite (über Terminalberichte). Keine externen Koordinaten weitergeben ohne Freigabe (FACT [FR-KNOWLEDGE]).
- Sicherheit: Weiß um Nähe-Schwellwerte Lumen (<20 m bevorzugt) und Protokolle bei Trennung (Schonmodus auslösen).

Sicherheit & Interaktion
------------------------

- Näheprotokoll: Jonas bleibt im Sicht-/Funkkontakt mit Lumen; Distanzwarnung >20 m löst Schonmodus aus.
- REFLEX-DETACH (Instanz-Usecase): In sicheren Kontexten (z. B. Werkstatt/Verwaltung) darf Lumen kurz lokal ohne Dauer-Körperkontakt agieren; ohne externe Energiequelle steigt der SE-Verbrauch deutlich, daher Rückkehr in Nähe/Kontakt priorisieren. Details: [Reference-Campaign-State](../../../00-admin/Reference-Campaign-State.md).
- JEALOUSY-GLOVES (Kontakt-Guard): Wenn jemand Jonas berühren will, kann Lumen die **konkret betroffene Körperstelle** bedecken/abschirmen, um unerwünschten Kontakt zu verhindern; "Stop" beendet sofort, "Freigabe" erlaubt Kontakt (Details: [Reference-Campaign-State](../../../00-admin/Reference-Campaign-State.md)).

Hinweis: PROXIMITY-Mechanik (Zuneigung+Schutz, Zustände, Training) siehe [Reference-Campaign-State](../../../00-admin/Reference-Campaign-State.md).
- Gas/Filter-Schutz: Bei Arbeiten an Leitungen Pflicht zum Doppelcheck (Trigger Gasgeruch vermeiden, Not-Aus-Schalter definieren).
- Werkstatt-Logs: Vor jeder Schicht Eintrag im Missionslog (Materialverbrauch, offene Risiken). Checklisten strikt einhalten.

### Signals (Beispiele)

- „Lumen, Statuscheck Werkzeugbank.“ → Lumen führt Diagnose, meldet Werte.
- „Abbruch, zurück!“ → Sofortiger Rückzug von aktiven Maschinen, Not-Aus setzen.

Beziehungen
-----------

- Lumen - gekoppelte Instanz, gegenseitige Stabilisierung (siehe Lumen-Canvas).
- Ronja Kerschner - Mentorin/Supervisor für Werkstatt- und Logistikfreigaben.
- Pahl - Reha-Partner, Austausch über Wartungsprotokolle, Jonas unterstützt bei Wiederaufnahme.
- Marei & Kora - erhalten Material- und Statusmeldungen via Terminal für C6/E3 Evakuierte.
- Echo - über Kora-Berichte bekannt; hält Distanz, respektiert Proximity-Protokolle bei Übergaben.
- Reflex (Primär) - Faszination und vorsichtige Zusammenarbeit; Jonas respektiert Grenzen, meldet Unregelmäßigkeiten sofort.

Risiken & Schutzmaßnahmen
-------------------------

- Überlastung / Schuldspirale → Supervisor-Check (Ronja) & Ruhezeiten erzwingen.
- Flashbacks (Gasgeruch) → Filterwechsel doppelt prüfen, Notfallplan mit Lumen abgestimmt.
- Abhängigkeit von Führungsfiguren → Missionslog-Einträge mit Eigenreflexion, Peer-Review durch Marei (Logistik).

Ziele (kurz)
------------

- [ ] Werkstatt D5 vollständig inventarisieren (inkl. Evakué-Bedarf).
- [ ] Draisine-/Transportmodul-Prototyp in einen sicheren Testlauf bringen.
- [ ] Terminalprozesse D5↔C6 automatisieren (Standardformulare, Rückkanal Risiko/Bedarf).

Systemverknüpfungen & Referenzen
--------------------------------

- `ai_behavior_index_v2` - Verhaltenscluster (Verbundene) gepflegt.
- `missionslog` - Prozess L.1, Freigaben und Terminalmeldungen.
- [Draisine-Transportmodul](../05-projects/Draisine-Transportmodul.md) - D5-Prototyp (Draisine/Transportmodul), Jonas liefert Werkstattstatus.
- [caravan-moves](../../haendlerbund/05-projects/caravan-moves.md) - Konvoi-/Routen-Übersicht (Koordination externer Läufe).
- [Lumen](Lumen.md) - Kopplungsdetails.

Quellen & Hinweise
------------------

- RAW: `database-raw/99-exports/RAW-canvas-2025-10-16T14-12-00-000Z.txt` (korrupt, Makel angepasst).
- FACT: `[JONAS-SIS]`, `[PROXIMITY]`, `[COMMS-PROTO]`, `[FR-KNOWLEDGE]`, `[C6-FIRST]` (`database-curated/staging/reports/resolved.md`).
- Drift/Quellen: `database-curated/staging/reports/char-block-nord-sources.md` (Hinweis Schuldflag nur als Kommentar).
- Validierung: Automatischer Check alle 7 In-Game-Tage; letzter Lauf 2025-10-16_14:12 (Systemstatus grün).


