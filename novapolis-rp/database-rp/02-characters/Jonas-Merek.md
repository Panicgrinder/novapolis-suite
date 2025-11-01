---
title: Jonas Merek
category: character
slug: jonas-merek
version: "1.0"
last_updated: 2025-11-02T13:55:00+01:00
last_change: "Upgrade aus RAW char_jonas_v2 (korrupt) + resolved #[JONAS-SIS]"
tags: ["werkstatt", "novapolis"]
affiliations: ["novapolis"]
dependencies: ["lumen", "d5", "missionslog", "ai_behavior_index_v2"]
primary_location: d5
last_seen: d5
---

<!-- markdownlint-disable MD025 -->

# Jonas Merek

- Meta: last-updated: 2025-11-02T13:55:00+01:00
- Verhaltenssignatur: `JNS3=L55-T68-N40-E72-O50-C42-M78-P32-ab` – sicherheitsorientiert, hilfsbereit, driftet bei Überlast in Fluchtreflexe.
- Rolle: Technikerlehrling/Mechaniker; betreut Werkstatt & Materiallauf in D5 (Quelle: RAW char_jonas_v2)
- Werte: Kraft 3, Geschick 5, Geist 3, Wille 4, Charisma 3
- Skills:
  - Geübt: Mechanik, Reparaturen, Materialkunde
  - Meisterhaft: Improvisation, Werkzeugarbeit
  - Optional: Energieverteilung/Notversorgung
- Ausrüstung: Werkzeugkasten (modular), Messgeräte, Schutz- und Filterausrüstung, mobile Terminalverbindung zu C6 (Quelle: FACT COMMS-PROTO)
- Motivation: Zugehörigkeit zur Novapolis-Crew sichern; Werkstatt als sicheren Anker aufbauen
- Makel: Trauma-Trigger (Gasgeruch, abgeschlossene Räume); anhaltende Schuldgefühle wegen der vermissten Schwester (Status: vermisst/unklar, siehe FACT [JONAS-SIS]); Schlafstörungen bei Hochlast

## Hintergrund & Herkunft

- Herkunft: Station E2, Überlebender des Gasunfalls; Evakuierung über Tunnelknoten, Schwester seitdem vermisst (kein Todesnachweis).
- Aufgenommen nach Mission „C6-Aufnahme Jonas“ (siehe FACT [C6-FIRST]); arbeitet unter Aufsicht von Ronja und Reflex.
- Lumen ist an Jonas gekoppelt (Nähe-Kopplung stabilisiert beide, Quelle: FACT [PROXIMITY]).

## Rollen & Verantwortlichkeiten (Pflichtfelder)

- Werkstatt & Fertigung – Reparaturen, Prototypen (Draisine/Transportmodul), Wartung D5-Infrastruktur.
- Logistik – Materialläufe dokumentieren, Schnittstelle zum Missionslog (Freigaben über Ronja, Abgleich mit Missionslog Prozess L.1).
- Kommunikation – Terminal/Funkbrücke D5↔C6 bedienen, Statusberichte an Marei/Kora koordinieren (Quelle: FACT [COMMS-PROTO]).

## Zugehörigkeit & Standort

- Zugehörigkeit: Novapolis (D5).
- Status: aktiv, unter Supervision; keine Außenmissionen ohne Begleitung.
- Letzter bekannter Einsatz: D5 Werkstattbereich (Schichtplan rotierend, Abstecher C6 nur mit Freigabe).

## Wissensstand (Matrix – Auszug)

- Intern: Kennt D5-Systeme, Lumen-Kopplungsregeln, Grundzüge von Reflex’ Präsenz (Need-to-know). Zugang zu Wartungslog und Missionslog Einträgen der Werkstatt.
- Extern: Kennt Karawanen-Schnittstelle C6 (Logistik), Evakuierte aus E3 und Echo als Reflex-Instanz an Koras Seite (über Terminalberichte). Keine externen Koordinaten weitergeben ohne Freigabe (FACT [FR-KNOWLEDGE]).
- Sicherheit: Weiß um Nähe-Schwellwerte Lumen (<20 m bevorzugt) und Protokolle bei Trennung (Schonmodus auslösen).

## Sicherheit & Interaktion

- Näheprotokoll: Jonas bleibt im Sicht-/Funkkontakt mit Lumen; Distanzwarnung >20 m löst Schonmodus aus.
- Gas/Filter-Schutz: Bei Arbeiten an Leitungen Pflicht zum Doppelcheck (Trigger Gasgeruch vermeiden, Not-Aus-Schalter definieren).
- Werkstatt-Logs: Vor jeder Schicht Eintrag im Missionslog (Materialverbrauch, offene Risiken). Checklisten strikt einhalten.

### Signals (Beispiele)

- „Lumen, Statuscheck Werkzeugbank.“ → Lumen führt Diagnose, meldet Werte.
- „Abbruch, zurück!“ → Sofortiger Rückzug von aktiven Maschinen, Not-Aus setzen.

## Beziehungen

- Lumen – gekoppelte Instanz, gegenseitige Stabilisierung (siehe Lumen-Canvas).
- Ronja Kerschner – Mentorin/Supervisor für Werkstatt- und Logistikfreigaben.
- Pahl – Reha-Partner, Austausch über Wartungsprotokolle, Jonas unterstützt bei Wiederaufnahme.
- Marei & Kora – erhalten Material- und Statusmeldungen via Terminal für C6/E3 Evakuierte.
- Echo – über Kora-Berichte bekannt; hält Distanz, respektiert Proximity-Protokolle bei Übergaben.
- Reflex (Primär) – Faszination und vorsichtige Zusammenarbeit; Jonas respektiert Grenzen, meldet Unregelmäßigkeiten sofort.

## Risiken & Schutzmaßnahmen

- Überlastung / Schuldspirale → Supervisor-Check (Ronja) & Ruhezeiten erzwingen.
- Flashbacks (Gasgeruch) → Filterwechsel doppelt prüfen, Notfallplan mit Lumen abgestimmt.
- Abhängigkeit von Führungsfiguren → Missionslog-Einträge mit Eigenreflexion, Peer-Review durch Marei (Logistik).

## Ziele (kurz)

- [ ] Werkstatt D5 vollständig inventarisieren (inkl. Evakué-Bedarf).
- [ ] Draisine-/Transportmodul-Prototyp in einen sicheren Testlauf bringen.
- [ ] Terminalprozesse D5↔C6 automatisieren (Standardformulare, Rückkanal Risiko/Bedarf).

## Systemverknüpfungen & Referenzen

- `ai_behavior_index_v2` – Verhaltenscluster (Verbundene) gepflegt.
- `missionslog` – Prozess L.1, Freigaben und Terminalmeldungen.
- `database-rp/05-projects/caravan_moves.md` – Draisine-/Konvoi-Projekt, Jonas liefert Werkstadtstatus.
- `database-rp/02-characters/Lumen.md` – Kopplungsdetails.

## Quellen & Hinweise

- RAW: `database-raw/99-exports/RAW-canvas-2025-10-16T14-12-00-000Z.txt` (korrupt, Makel angepasst).
- FACT: `[JONAS-SIS]`, `[PROXIMITY]`, `[COMMS-PROTO]`, `[FR-KNOWLEDGE]`, `[C6-FIRST]` (`database-curated/staging/reports/resolved.md`).
- Drift/Quellen: `database-curated/staging/reports/char-block-nord-sources.md` (Hinweis Schuldflag nur als Kommentar).
- Validierung: Automatischer Check alle 7 In-Game-Tage; letzter Lauf 2025-10-16_14:12 (Systemstatus grün).
