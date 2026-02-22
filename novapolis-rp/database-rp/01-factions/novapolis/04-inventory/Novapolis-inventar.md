---
stand: 2026-02-21 21:58
update: Delta-zum-Missionslog ergänzt und Systemlinks auf aktuelle Pfade ausgerichtet.
checks: "npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/todo.rp.md' 'novapolis-dev/docs/donelog.md' 'novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/Relationslog-Novapolis.md' 'novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md' 'novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md' 'novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md' PASS (2026-02-21 21:55); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-dev/docs/todo.rp.md' 'novapolis-dev/docs/donelog.md' 'novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/Relationslog-Novapolis.md' 'novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md' 'novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md' 'novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md' PASS (EXITCODE=0, 2026-02-21 21:55)"
canvas: Inventar Novapolis
last_updated: 2025-11-07T04:32:00+01:00
category: inventory
slug: novapolis-inventar
owner: novapolis
scope: faction
version: "0.1"
---
Inventar - Novapolis (Fraktion)
================================

Hinweis: Fraktionsinventare strikt getrennt (Policy Y.1). Abrechnung im Wochenzyklus.

- Transfers zwischen D5 und C6 nur via Mission/Logistik.
- Waehrung "Kugeln" wird als Inventar-Item gefuehrt (neu/gebraucht).

Bestände (Auszug)
-----------------
- Kugeln (neu): tbd (hochwertig; 1 neu ≈ 10 gebraucht)
- Kugeln (gebraucht): tbd (Alltag/Hauptmunition; Qualität streut)
- Energiezellen (%): tbd
- Werkzeuge/Material: tbd

Bewegungen (Log)
----------------
- tbd

Delta zum Missionslog
---------------------

- Lagebild: C6-relevante Materialbedarfe/Bestände werden über das fraktionsspezifische Missionslog nachgeführt; Fraktionsinventar führt den aggregierten Stand.
- Delta 1 (offen): Übernahme belastbarer Mengen aus C6-/D5-Teilinventaren in den Fraktionsaggregatstand.
  - Quelle: [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md), [C6-inventar](./C6-inventar.md), [D5-inventar](./D5-inventar.md)
- Delta 2 (offen): Verbuchung missionierter Transferzeilen (Quelle→Ziel) sobald Quittungen/Belege final sind.
  - Quelle: [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md)

Links
-----
- Logistik-Policy C6 → ../03-locations/C6-Logistik-Policy.md
- Logistik (Admin) → ../../../00-admin/Logistik.md
- Missionslog → ../05-projects/Missionslog-Novapolis.md
- Währung "Kugeln" (Reference) → ../../../00-admin/Reference-Campaign-State.md


