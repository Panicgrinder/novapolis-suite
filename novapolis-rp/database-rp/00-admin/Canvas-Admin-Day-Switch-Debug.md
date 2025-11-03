---
canvas: Admin Day-Switch & Debug
last-updated: 2025-10-27T18:13:52+01:00
category: Admin
version: 0.1
---

# Admin: Day‑Switch & Debug

Ziel: Sicheren Tageswechsel durchführen (Persistenz) und bei Bedarf Debug‑Ausgaben aktivieren, ohne Spielstand/Canvas zu beschädigen.

## Mechanik

- Persistenz: Systemmeldungen mit ATSD‑String + Canvas‑Zahl protokollieren (Beginn/Ende)
- Tageswechsel: Status einfrieren → Inventarabschluss → Verlinkungen → Archiv (Prozess L.1)
- Debug‑Mode: zuschaltbar für erweiterte Ausgaben (nur Admin)

## ATSD‑String (Definition)

- A = Aktionen (Anzahl abgeschlossene Missions-/Arbeitsblöcke)
- T = Timeline‑Marker (z. B. T+0, T+1; inkl. Uhrzeitfenster)
- S = Szenen (Anzahl neuer/abgeschlossener Szenen‑Kacheln)
- D = Delta (Änderungsgröße: kleine/mittlere/große Änderung oder Hash)

Beispiel: ATSD "A3-T+1-20:15-S1-D:mid"

## Prozedur (Checkliste)

1. Vorbereitungen
   - Canvas‑Zahl prüfen/notieren
   - ATSD‑String generieren/übernehmen
   - Offene Missionen sichten
2. Abschluss T
   - Inventarabschluss je Knoten (D5/C6, Fraktionen)
   - Missions‑Verlinkungen setzen (Missionslog, Orte/Projekte)
3. Umschalten auf T+1
   - Systemmeldung protokollieren (ATSD + Canvas‑Zahl)
   - Debug‑Mode optional aktivieren, dann direkt wieder deaktivieren

### Systemmeldung (Beispiel)

```text
[SYSTEM] Day-Switch: start | ATSD=A{n}-T+{k}-{hh}:{mm}-S{s}-D:{small|mid|large} | Canvas={count}
[SYSTEM] Day-Switch: end   | ATSD=A{n}-T+{k}-{hh}:{mm}-S{s}-D:{small|mid|large} | Canvas={count}
```

## Logs & Evidenz

- Minimal: Zeit, ATSD, Canvas‑Zahl, Who+What
- Optional: Differenzlisten (Inventare, Energie‑Konten), Missionsstatus

## Fehlerfälle & Recovery

- Abbruch vor Archivierung → erneut bei Schritt „2. Abschluss T“ einsetzen
- Debug‑Mode blieb an → sofort deaktivieren, Systemmeldung mit Hinweis setzen
- Inkonsistente Verlinkung → Missionslog/Orte/Projekte mit Backlink‑Check durchgehen

## Testfälle

- Leerer Tageswechsel (keine Missionen) → keine Differenzen außer Zähler
- Aktiver Missionsabschluss → erzeugt Links + Archiv‑Eintrag
- Debug‑Mode an/aus → keine Persistenzfehler

## Links

- Timeline (T+0) → ./Canvas-T+0-Timeline.md
- Missionslog → ./Missionslog.md
- Logistik (Admin) → ./Logistik.md
- C6 (Ort) → ../03-locations/C6.md
- C6 – Logistik‑Policy → ./C6-Logistik-Policy.md

