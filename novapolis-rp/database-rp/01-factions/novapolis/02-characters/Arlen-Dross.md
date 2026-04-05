---
stand: 2026-04-05 19:43
update: Dependencies auf caravan-moves konsolidiert.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-02-04 10:22)
title: Arlen Dross
category: character
slug: arlen-dross
version: "1.0"
last_updated: 2026-01-14T17:31:10+01:00
last_change: "Zugehörigkeit/Position aktualisiert: Anschluss an Novapolis; Basis C6."
tags: ["karawane", "novapolis", "diplomatie"]
affiliations: ["novapolis"]
dependencies: ["caravan-moves", "ai_behavior_index_v2", "missionslog", "logistik", "g7", "handel_diplomatie_haendlergilde_v1", "index_haendlergilde_v1"]
primary_location: c6
last_seen: c6
---

<!-- markdownlint-disable MD025 -->

Arlen Dross
===========

- Meta: last-updated: 2025-11-07T03:32:00+01:00
- Rolle: Händler- und Diplomatiebeauftragter des Händlerbunds - moderiert Kontakte zwischen Karawane und Novapolis, ohne Kora/Marven zu duplizieren (FACT [CARAVAN-LEADERSHIP]).
- Werte: Kraft 3, Geschick 4, Geist 4, Wille 5, Charisma 5.
- Skills:
  - Geübt: Verhandeln, Navigation, Versorgung.
  - Meisterhaft: Diplomatie, Risikomanagement.
  - Optional: Schusswaffenkenntnis.
- Ausrüstung: Rechnerslate mit Handelsarchiv, kompakte Kartensätze (Papier + codierte Notizen), modulare Verhandlungs-Kits (Marker, Übersetzer, Versiegelungen).
- Motivation: Aufbau eines stabilen Handelsnetzes bei gleichzeitiger Wahrung persönlicher und kollektiver Unabhängigkeit.
- Makel: Innere Zerrissenheit zwischen Freiheit und Verantwortung, latentes Misstrauen gegenüber stationären Ordnungen.

Hintergrund & Kontext
---------------------

- Ehemaliger Zwischenhändler aus den Transitsektoren rund um C6; wechselte nach H-47-Zwischenfall mit dem Händlerbund zur Novapolis-Peripherie.
- Agiert als Gesichterklärer für Außenkontakte der Karawane; hält das Gleichgewicht zwischen Handelsfreiheit und Bündnisauflagen.
- Beobachtet Reflex als unkalkulierbaren Faktor: respektiert Ronjas Bindung, aber fordert klare Sicherheitsgrenzen.

Rollen & Verantwortlichkeiten
-----------------------------

- **Diplomatie & Moderation** - Führt Verhandlungen mit Ronja, Kora und Novapolis-Gremien; bereitet Vertragsentwürfe, legt Eskalationspfade fest.
- **Versorgungsschnittstellen** - Koordiniert Übergaben zwischen externem Konvoi (Marven) und interner Logistik (Kora/Marei); dokumentiert Quittungen.
- **Crew-Betreuung** - Hält die Karawanenmitglieder emotional stabil, moderiert Konflikte, plant Rotationen bei längeren Aufenthalten in G7.

Zugehörigkeit & Standort
------------------------

- Zugehörigkeit: Novapolis (C6; ehem. Karawane H-47).
- Status: aktiv; Basis C6; Einsätze nach Diplomatie-/Handelslog.
- Letzter bekannter Einsatz: C6 - Vorbereitung eines Handelsgesprächs mit Ronja über Energiezellen-Kontingente.

Wissensstand (Matrix - Auszug)
------------------------------

- Händlerbund: Kennt Crewzusammensetzung, Depotstandorte, Kontaktkorridore.
- Novapolis: Kennt Ansprechpersonen (Ronja, Kora, Marei, Jonas als Funklink); keine Koordinaten, keine tieferen Anlagenpläne (FACT [FR-KNOWLEDGE]).
- Reflex: Weiß um Existenz und Verbund zu Ronja, hält Distanz und fordert transparente Freigaben, bevor er Reflex-seitige Hilfe zulässt.

Interaktion & Safety
--------------------

- Moderiert Gespräche strukturiert, fasst Ergebnisse schriftlich zusammen und sichert Gegenzeichnungen.
- Besteht auf Sicherheitscode vor jedem Transfer (z. B. zwei-Wege-Authentifizierung mit Marvens Crew).
- Routine/Validierung: Auto-Prüflauf alle 7 In-Game-Tage; letzter Systemlauf 2025-10-16_14:56 (Status grün, nächster nach Fraktionszug Woche 4).

### Signals (Beispiele)

- „Verhandlungsstufe Beta - wir halten den Konvoi bereit, Verhandlungen in Kammer Drei.“
- „Freiheitsmarke hoch - sollte die Vereinbarung Fesseln erzeugen, ziehen wir zurück und evaluieren neu.“

Mind-Cluster-Referenz (SSOT)
----------------------------

- Beziehungen, Verhaltenssignatur und geistnaher Zustand liegen zentral im Mind-Cluster:
- `../07-mind-clusters/arlen-dross-mind-cluster.md`

Risiken & Schutzmaßnahmen
-------------------------

- Entscheidungsparalyse unter Druck → Setzt Vorentscheidungsrahmen (Optionen A/B) und delegiert Notfallentscheidungen an Marven.
- Emotionale Erschöpfung → Plant Ruhefenster nach intensiven Verhandlungen; Marei überwacht Belastungsindikatoren.
- Misstrauen gegenüber stationären Strukturen → Regelmäßige Lagebesprechungen mit Ronja/Kora, um Kontrollverlustgefühle abzubauen.

Ziele (kurz)
------------

- [ ] Handelsprotokoll Karawane↔Novapolis standardisieren (Sicherheitscode, Lieferfenster, Belegfluss).
- [ ] Vermittlungsnetz mit Außenfraktionen erweitern, ohne Novapolis preiszugeben.
- [ ] Crew-Moderation festigen (Konfliktpräventionsworkshops, Rotationsplan mit Marven).

Systemverknüpfungen & Referenzen
--------------------------------

- `caravan-moves` - Dokumentation aller diplomatischen Übergaben.
- `missionslog` - Einträge zu Verhandlungsmissionen und rückgekoppelten Maßnahmen.
- `logistik` - Abgleich interner/externer Warenflüsse.
- `handel_diplomatie_haendlergilde_v1` - Diplomatieprotokolle des Händlerbunds (ID: haendlergilde).
- `ai_behavior_index_v2` - Eintrag „Der Vermittler“.
- Mind-Cluster (Arlen) -> ../07-mind-clusters/arlen-dross-mind-cluster.md

Quellen & Hinweise
------------------

- RAW: `database-raw/99-exports/RAW-canvas-2025-10-16T14-56-20-000Z.txt` (char_arlen_dross_v2).
- Flag: `database-raw/99-exports/RAW-canvas-2025-10-16T14-56-20-000Z.flags.txt` - Titel-Overlap; in diesem Canvas entflechtet.
- FACT: `[CARAVAN-LEADERSHIP]`, `[FR-KNOWLEDGE]` (`database-curated/staging/reports/resolved.md`).
- Drift & Notizen: `database-curated/staging/reports/char-block-nord-sources.md`, `overlap-arlen-dross.md`.
- Validierung: Auto (Intervall 7 In-Game-Tage); nächster Lauf nach Fraktionszug Woche 4.


