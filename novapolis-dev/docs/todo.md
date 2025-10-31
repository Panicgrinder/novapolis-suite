<!-- markdownlint-disable MD022 MD041 -->
last-updated: 2025-10-31T00:00:00+01:00
---
---

TODO (Novapolis-RP)
===================

<!-- Migration: Quelle aus dem frueheren coding-Hub, uebernommen am 2025-10-29 -->
<!-- Relocated aus dem ehemaligen Novapolis-RP Development-Hub nach `novapolis-dev/docs/todo.md` am 2025-10-29 -->

Aktive Aufgaben
---------------

- [ ] Relocation Follow-ups
  - [x] Zentrale `.github/copilot-instructions.md` im Monorepo verankert; Duplikate in agent/RP entfernt (2025-10-31)
  - [x] Datenverzeichnisse `database-curated`, `database-raw`, `database-rp` zurück nach `novapolis-rp/` verschoben (2025-10-31)
  - [ ] novapolis-sim/README verweist explizit auf zentrale Copilot-Anweisungen
  - [ ] Externe Skripte/Notizen erneut auf Altpfade prüfen
  - [ ] Set removal date for legacy stubs after downstream confirmation
  - [ ] Post-merge sweep for stragglers
  - [ ] Optional: DevContainer- und CI-Hinweise auf neue Pfade umstellen

- [ ] Sim-API auf WebSockets erweitern (Push-Updates statt Polling)
- [ ] Region-Renderlogik im Godot-Client vorbereiten (Placeholder-Geometrien)
- [ ] Darstellungs-Icons für Akteure entwerfen/ablegen
- [ ] CI-Hooks für Sim/Visualisierung (pytest + Godot Linter) ergänzen

- [ ] Exporte einsortieren
  - [ ] `99-exports/chat-export-complete.txt` hinzufügen
  - [ ] PDF `Chronist von Novapolis - Ronjas Novapolis RP.pdf` ablegen
  - [ ] Kanonische Quelle festlegen: `RAW-chat-export-2025-10-23T03-57-37-172Z.txt` als Quelle A
  - [ ] PDF als Quelle B zur Querprüfung nutzen
  - [ ] Duplikate aus `chat-export.txt` und `chat-export (1).txt` prüfen/entfernen
  - [ ] Normalisierung: `99-exports/chat-export-complete.txt` konsolidiert erzeugen

- [ ] Parsing & Normalisierung
  - [ ] Chat in strukturiertes Format (JSONL) konvertieren (optional – vorerst ausgesetzt)
  - [ ] Extrahate erzeugen: Szenenanker, Kanon-Fakten, Charakter-Fakten, Projekt-/Aufgabenstatus
  - [x] TXT-Normalisierung + Chunking (500 Zeilen) mit Index/Views (staging)

- [ ] Curation-Review (chat-export (1).txt)
  - [x] Chunk part-022 annotieren ([FACT?]/[OPEN], global 10501–10819)
  - [x] Chunk part-021 annotieren ([FACT?]/[OPEN], global 10001–10500)
  - [x] Chunk part-020 annotieren ([FACT?]/[OPEN], global 9501–10000)
  - [x] Chunk part-019 annotieren ([FACT?]/[OPEN], global 9001–9500)
  - [x] Chunk part-018 annotieren ([FACT?]/[OPEN], global 8501–9000)
  - [x] Chunk part-017 annotieren ([FACT?]/[OPEN], global 8001–8500)
  - [x] Chunk part-016 annotieren ([FACT?]/[OPEN], global 7501–8000)
  - [x] Chunk part-015 annotieren ([FACT?]/[OPEN], global 7001–7500)
  - [x] Chunk part-014 annotieren ([FACT?]/[OPEN], global 6501–7000)
  - [x] Chunk part-013 annotieren ([FACT?]/[OPEN], global 6001–6500)
  - [x] Chunk part-012 annotieren ([FACT?]/[OPEN], global 5501–6000)
  - [x] Chunk part-011 annotieren ([FACT?]/[OPEN], global 5001–5500)
  - [x] Chunk part-010 annotieren ([FACT?]/[OPEN], global 4501–5000)
  - [x] Chunk part-009 annotieren ([FACT?]/[OPEN], global 4001–4500)
  - [x] Chunk part-008 annotieren ([FACT?]/[OPEN], global 3501–4000)
  - [x] Chunk part-007 annotieren ([FACT?]/[OPEN], global 3001–3500)
  - [x] Chunk part-006 annotieren ([FACT?]/[OPEN], global 2501–3000)
  - [x] Chunk part-005 annotieren ([FACT?]/[OPEN], global 2001–2500)
  - [x] Chunk part-004 annotieren ([FACT?]/[OPEN], global 1501–2000)
  - [x] Chunk part-003 annotieren ([FACT?]/[OPEN], global 1001–1500)
  - [x] Chunk part-002 annotieren ([FACT?]/[OPEN], global 501–1000)
  - [x] Chunk part-001 annotieren ([FACT?]/[OPEN], global 1–500)
  - [x] Weiter rückwärts bis part-001 (stichprobenweise tiefer, Fokus auf strittige Stellen)

  - [ ] Tagging‑Pipeline (YAML‑getrieben)
    - [x] 019–016: Dry‑Run → Write (Heuristiken: N7→c6‑nord, NOTE/EVENT, MISSION C6‑Nord, Sektor‑Codes)
    - [ ] 015–010: Dry‑Run → Write
    - [ ] 009–001: Dry‑Run → Write
    - [ ] Alias‑Kollisionen prüfen/entscheiden ("C6" → c6 vs c6‑nord; Präferenz festlegen und ggf. Alias entfernen)
    - [ ] Unresolved klären: `Echo`, `Reflex-Wissensstand-Trainingsstand` (MD anlegen/Slug anpassen)
    - [ ] Co‑Occurrence‑Vorschläge prüfen (falls vorhanden) und Alias‑Liste gezielt ergänzen

- [ ] Regeln & Verwaltung (Canvas)
  - [ ] Unumstößlich-Canvas finalisieren (Fraktionen, D5/C6-Kernfakten, N7-Entfernung)
  - [x] Day-Switch-Canvas erstellen (Checkliste: alles laden, Validierungen, Teil-Fraktionszug)
  - [ ] A/T/S/D-Metriken definieren (Bedeutung, Anzeigeformat, Zählweise)
  - [ ] Systemmeldung erweitern: Anzahl geladener Canvas + ATSD-String; Persistenz sicherstellen
  - [ ] Canvas-Kategorien A/B/C: Regeln/Workflows und Risiken dokumentieren
  - [ ] Logbuch-Policy festschreiben (stationenweit verfügbar, außer „secret“)
  - [ ] person_index_np – Struktur/Felder (Name, Rolle, Zugehörigkeit, Status, Notizen)
  - [ ] Canvas „Logistik“ – Scope, robuste Verlinkungen (Generator/Energie-Konten), Lazy-Load-Strategie
  - [ ] Canvas „Mission Tunnel“ – Felder/Metriken (Abschnitte, %Fortschritt, Blocker)
  - [ ] Export „alle Canvas“ – Sortierung nach letztem Update (Quelle für Timestamps klären)

- [ ] Memory-Bundle gegen Export prüfen und ggf. verdichten
  - [ ] Welt-/Kanon-Kernpunkte aktualisieren
  - [ ] Charakter-Kompakteinträge (Ronja, Reflex, Jonas) aktualisieren
  - [ ] Orte (D5, C6, Tunnel) und Projekt „Nordlinie 01“ einpflegen
  - [ ] Offene Loops/Blocking-Issues ergänzen

- [ ] Charakter-Canvas prüfen/ergänzen
  - [ ] Gegen Extrahate aus dem Export abgleichen
  - [ ] Ronja – Werte, Skills, Inventar, Ziele
  - [ ] Reflex – Natur/Regeln, Instanzen/Überwachung
  - [ ] Jonas – Herkunft, Rolle, Werkstatt

- [ ] Orte
  - [ ] Gegen Extrahate aus dem Export abgleichen
  - [ ] D5 – Fix-Beschreibung (vom Tunnel aus), Maße je Raum, Lastenaufzug 2t unter Bahnsteig
  - [ ] C6 – Fix-Beschreibung, Beleuchtung (historisch), nutzbare m² je Raum, Liniennetz (D5, F1, verschütteter Trakt, Karawanenlinie) + Wandtunnel; Konflikte zu 4‑Linien-Angaben auflösen
  - [ ] Tunnel D5–C6 – Gesamtlänge fixieren (ggf. aus Reisezeit), Schaden, Materialliste
  - [ ] C6‑Nord (N7) – Sealed Room: Status/Mission-Canvas, Abgrenzung Metro-Kontext dokumentieren

- [ ] Projekte
  - [ ] Gegen Extrahate aus dem Export abgleichen
  - [ ] Nordlinie 01 – Abschnitte, Material, Blocker
  - [ ] Draisine – Spezifikation (Breite≈U-Bahn, Länge ~6 m, ~10 Pers., Antrieb), Baufortschritt dokumentieren
  - [ ] Tunnel-Fortschritt – Methode festlegen (Differenz vs. %/Tag/Person), 40%-Stand verifizieren
  - [ ] Mission C6‑Nord – Ereignisse/Status pflegen; Trigger/Guards verlinken (AI-Behavior-Mapping)

- [ ] Inventar
  - [ ] Gegen Extrahate aus dem Export abgleichen
  - [ ] Fehlteile: Schweißgerät, Adapter DN60, Hydrofilter-Behälter-Plan

- [ ] Energie & Logistik
  - [ ] Energieformel/Saldo finalisieren (D5/C6), Generator-Verlinkung im Logistik-Canvas sicherstellen
  - [ ] Lazy-Load vs. dauerhaft aktive Canvas: Policy definieren (damit Verlinkungen zuverlässig ziehen)
  - [ ] Algen-/Pilz-Kapazitäten und Vorratsreichweiten modellieren; Skalierung mit Bevölkerungszahl
  - [ ] D5↔C6 Datenaustausch-Prozess (Jonas) definieren und verlinken (Logistik/Inventar)

- [ ] Szenen-Backfill & Timeline
  - [ ] `06-scenes/` füllen: letzte 3–5 Szenen rückwärts aus Export
  - [ ] Szenen-Kacheln: Datum, Kernentscheidungen, offene Fäden
  - [ ] Optional: Timeline-Index anlegen

- [ ] Nächste Spielsitzung vorbereiten
  - [ ] Szenen-Kachel 1: Status-Ping D5/C6/Nordlinie
  - [ ] Szenen-Kachel 2: Pahl/Jonas Versorgung
  - [ ] Szenen-Kachel 3: Exo-Prototyp erste Iteration

- [ ] Qualitätssicherung
  - [ ] Konsistenzcheck: Memory-Bundle vs. Einzeldateien
  - [ ] Benennungskonventionen vereinheitlichen
  - [x] Markdown-Lint/CI prüfen
  - [x] Daten-Validierungen in CI verankern (Schema + Cross-Refs)
  - [x] Szenen-Front-Matter etabliert (README + erste Szene aktualisiert)
  - [ ] Szenen-Backfill mit Front-Matter (letzte 3–5 Szenen)
  - [x] Benennung vereinheitlichen (database-rp)
  - [x] Policy dokumentieren (`novapolis-dev/docs/naming-policy.md`)
    - [x] Name-Linter hinzufügen (Dry-Run in CI)
    - [x] Dry-Run lokal ausführen (Task: "lint:names (auto)") – 0 Verstöße
    - [x] Renames: aktuell nicht erforderlich

Abgeschlossene Basisaufgaben
----------------------------

- [x] Workspace auf F:\Novapolis-RP anlegen (Ordnerstruktur)
- [x] Admin-Setup: README, Memory-Bundle, System-Prompt, Donelog

Hintergrund & Notizen
---------------------

- Vorschläge nur auf Anfrage; Kontinuität strikt wahren.
- Nach jedem Post interne 200-Token-Zusammenfassung (vom SL) einfordern.
