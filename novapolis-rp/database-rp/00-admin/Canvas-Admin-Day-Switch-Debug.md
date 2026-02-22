---
stand: 2026-02-22 04:16
update: Veralteten Timeline-Link auf kanonisches Canvas-T0-Timeline-Ziel korrigiert.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-02-22 02:26); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/index-rules.md' 'novapolis-rp/database-rp/00-admin/Current-State.md' 'novapolis-rp/database-rp/00-admin/Logistik.md' 'novapolis-rp/database-rp/00-admin/Metrograph.md' 'novapolis-rp/database-rp/00-admin/Ortsgraph.md' 'novapolis-rp/database-rp/00-admin/Canvas-Admin-Day-Switch-Debug.md' 'novapolis-rp/database-rp/00-admin/Kernkonversationen.md' 'novapolis-rp/database-rp/00-admin/Metrokarte-T0.md' 'novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md' 'novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-22 02:27)
slug: canvas-admin-day-switch-debug
canvas: Admin Day-Switch & Debug
last-updated: 2025-11-07T03:32:00+01:00
category: Admin
version: 0.1
---

Admin: Day-Switch & Debug
=========================

Ziel: Sicheren Tageswechsel durchführen (Persistenz) und bei Bedarf Debug-Ausgaben aktivieren, ohne Spielstand/Canvas zu beschädigen.

Mechanik
--------

- Persistenz: Systemmeldungen mit ATSD-String + Canvas-Zahl protokollieren (Beginn/Ende)
- Tageswechsel: Status einfrieren → Inventarabschluss → Verlinkungen → Archiv (Prozess L.1)
- Debug-Mode: zuschaltbar für erweiterte Ausgaben (nur Admin)

ATSD-String (Definition)
------------------------

- A = Aktiv (welcher Datenstand aktiv ist; laufende Persistenz / Snapshot)
- T = Total (Gesamtkontext/Turn; z. B. T+0, T+1; inkl. Uhrzeitfenster)
- S = System (Subsystem/Segment-Zähler, z. B. S0, S1)
- D = Defekt (Defekt-/Degradationslevel, z. B. small/mid/large)

Beispiel: ATSD "A3-T+1-20:15-S1-D:mid"

Prozedur (Checkliste)
---------------------

1. Vorbereitungen
   - Canvas-Zahl prüfen/notieren
   - ATSD-String generieren/übernehmen
   - Offene Missionen sichten
2. Abschluss T
   - Inventarabschluss je Knoten (D5/C6, Fraktionen)
   - Missions-Verlinkungen setzen (Missionslog, Orte/Projekte)
3. Umschalten auf T+1
   - Systemmeldung protokollieren (ATSD + Canvas-Zahl)
   - Debug-Mode optional aktivieren, dann direkt wieder deaktivieren

### Systemmeldung (Beispiel)

```text
[SYSTEM] Day-Switch: start | ATSD=A{n}-T+{k}-{hh}:{mm}-S{s}-D:{small|mid|large} | Canvas={count}
[SYSTEM] Day-Switch: end   | ATSD=A{n}-T+{k}-{hh}:{mm}-S{s}-D:{small|mid|large} | Canvas={count}
```

Logs & Evidenz
--------------

- Minimal: Zeit, ATSD, Canvas-Zahl, Who+What
- Optional: Differenzlisten (Inventare, Energie-Konten), Missionsstatus

Fehlerfälle & Recovery
----------------------

- Abbruch vor Archivierung → erneut bei Schritt „2. Abschluss T“ einsetzen
- Debug-Mode blieb an → sofort deaktivieren, Systemmeldung mit Hinweis setzen
- Inkonsistente Verlinkung → Missionslog/Orte/Projekte mit Backlink-Check durchgehen

Testfälle
---------

- Leerer Tageswechsel (keine Missionen) → keine Differenzen außer Zähler
- Aktiver Missionsabschluss → erzeugt Links + Archiv-Eintrag
- Debug-Mode an/aus → keine Persistenzfehler

Links
-----

- Timeline (T+0) → ./Canvas-T0-Timeline.md
- Missionslog → ./Missionslog.md
- Logistik (Admin) → ./Logistik.md
- C6 (Ort) → ../03-locations/C6.md
- C6 - Logistik-Policy → ../01-factions/novapolis/03-locations/C6-Logistik-Policy.md



