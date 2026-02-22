---
stand: 2026-02-22 04:13
update: T0-Startbelegung je Groessenklasse ergänzt; D5 gemäß RP-Hinweis auf maximal station_m korrigiert.
checks: npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-22 04:13); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/00-admin/Metrokarte-T0.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-22 04:13); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/Metrokarte-T0.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-22 04:13)
slug: metrokarte-t0
category: Admin
canvas: metrokarte-t0
status: active
owners: [admin-novapolis]
tags: [rp, admin, metro, t0, operations]
relatedSlugs: [metrograph-index, ortsgraph-index, stationskontroll-matrix]
---

Metrokarte (T0)
===============

Zweck
-----

Operative Sicht auf das aktuell relevante Stationsnetz für T0.
Dieses Dokument ergänzt den strukturellen [Metrograph](./Metrograph.md) um einen kompakten Lageblick,
ohne neue Kanonfakten zu erfinden.

Kernumfang T0 (gesetzt)
-----------------------

- Zielgröße Kernnetz: **54 Stationen**.
- Begründung: ausreichend Dichte für mehrere Fraktionen plus neutrale Puffer, ohne Berlin-Skalierung (175) zu kopieren.
- Umsetzungsprinzip: zuerst Struktur und Verbindungslogik festziehen, dann stationsweise Detailpflege.

Verteilung T0 (54)
------------------

| Segment | Anzahl | Zweck |
| --- | --- | --- |
| Fraktionsnahe Stationen | 24 | Primäre Operationsräume und Fraktionsanker |
| Neutrale Puffer-/Transitstationen | 18 | Trenn- und Austauschzonen zwischen Fraktionsräumen |
| Rand-/Peripherie-Stationen | 12 | Erweiterungs- und Unsicherheitsraum (tbd) |

Regel "Neutrale Zwischenstation"
---------------------------------

- Zwischen zwei fraktionsgeprägten Kernräumen liegt im Regelfall mindestens **eine** neutrale Station.
- Direkte Fraktions-zu-Fraktions-Kopplung ist nur als expliziter Sonderfall zulässig (Konfliktlage/Frontkorridor).
- Neutrale Stationen dienen als Puffer für Handels-, Diplomatie- und Ereignisübergänge.

Bereichsfluss (Godot-kompatibles Modell)
----------------------------------------

- Standardpfad: `Station -> Zugang -> Tunnel -> Tunnel-Abzweig (Ereignis-Möglichkeit) -> Tunnel -> Zugang -> nächste Station`.
- Bei mehreren Zugängen je Station gilt derselbe Pfad je Zugangsarm.
- Modellziel: Navigation zwischen verbundenen Bereichen ohne Sonderlogik, anschlussfähig für spätere Godot-Implementierung.

ID-Schema (verbindlich)
-----------------------

- `ST-<CODE>` für Stationen (z. B. `ST-D5`, `ST-C6`).
- `AC-<CODE>-<NN>` für Zugänge je Station (z. B. `AC-D5-01`).
- `TN-<VON>-<NACH>-<NN>` für Tunnelsegmente (z. B. `TN-D5-C6-01`).
- `JB-<VON>-<NACH>-<NN>` für Tunnel-Abzweige/Junctions (z. B. `JB-D5-C6-01`).
- Alle IDs sind global eindeutig; keine Wiederverwendung über Epochen/Versionen.

Stationsgroessen (verbindliche Labels)
--------------------------------------

- `station_xs` = sehr klein = 500-999 m2
- `station_s` = klein = 1000-2999 m2
- `station_m` = mittel = 3000-5499 m2
- `station_l` = groß = 5500-7999 m2
- `station_xl` = sehr groß = 8000-10000 m2

T0-Startbelegung m2 (Default je Klasse)

- `station_xs` -> `750`
- `station_s` -> `2000`
- `station_m` -> `4250`
- `station_l` -> `6750`
- `station_xl` -> `9000`

Regel: Wenn bei einer Station `size_m2=pending` steht, gilt im T0-Betrieb der jeweilige Klassen-Default als Startwert.

Textkarte T0 (KI-optimiert, Backbone 54 v0.3)
----------------------------------------------

Formatregeln

- Genau ein Objekt pro Zeile im Schema `TYP|key=value|key=value...`.
- Referenzen laufen ausschließlich über IDs (`station=ST-D5`, `from=AC-D5-01`).
- Reihenfolge im Pfad bleibt explizit (keine impliziten Kanten).
- Zusätzliche Objekttypen sind erlaubt (`HAZARD`) und referenzieren vorhandene IDs.

```text
STATION|id=ST-A1|code=A1|faction=arkologie-a1|status=active|tier=faction|size_class=station_l|size_m2=pending
STATION|id=ST-A2|code=A2|faction=neutral|status=active|tier=neutral|size_class=station_s|size_m2=pending
STATION|id=ST-A3|code=A3|faction=arkologie-a1|status=partial|tier=faction|size_class=station_m|size_m2=pending
STATION|id=ST-A4|code=A4|faction=neutral|status=partial|tier=periphery|size_class=station_s|size_m2=pending
STATION|id=ST-A5|code=A5|faction=arkologie-a1|status=active|tier=faction|size_class=station_m|size_m2=pending
STATION|id=ST-A6|code=A6|faction=neutral|status=restricted|tier=periphery|size_class=station_xs|size_m2=pending
STATION|id=ST-B1|code=B1|faction=neutral|status=active|tier=neutral|size_class=station_s|size_m2=pending
STATION|id=ST-B2|code=B2|faction=schienenbund|status=active|tier=faction|size_class=station_l|size_m2=pending
STATION|id=ST-B3|code=B3|faction=schienenbund|status=active|tier=faction|size_class=station_m|size_m2=pending
STATION|id=ST-B4|code=B4|faction=neutral|status=active|tier=neutral|size_class=station_m|size_m2=pending
STATION|id=ST-B5|code=B5|faction=neutral|status=partial|tier=neutral|size_class=station_s|size_m2=pending
STATION|id=ST-B6|code=B6|faction=neutral|status=restricted|tier=periphery|size_class=station_xs|size_m2=pending
STATION|id=ST-C1|code=C1|faction=neutral|status=active|tier=neutral|size_class=station_s|size_m2=pending
STATION|id=ST-C2|code=C2|faction=neutral|status=active|tier=neutral|size_class=station_s|size_m2=pending
STATION|id=ST-C3|code=C3|faction=neutral|status=partial|tier=neutral|size_class=station_m|size_m2=pending
STATION|id=ST-C4|code=C4|faction=neutral|status=active|tier=neutral|size_class=station_m|size_m2=pending
STATION|id=ST-C5|code=C5|faction=neutral|status=active|tier=neutral|size_class=station_m|size_m2=pending
STATION|id=ST-C6|code=C6|faction=novapolis|status=partial|tier=faction|size_class=station_m|size_m2=pending
STATION|id=ST-C7|code=C7|faction=neutral|status=partial|tier=neutral|size_class=station_s|size_m2=pending
STATION|id=ST-D1|code=D1|faction=neutral|status=active|tier=neutral|size_class=station_s|size_m2=pending
STATION|id=ST-D2|code=D2|faction=neutral|status=partial|tier=neutral|size_class=station_s|size_m2=pending
STATION|id=ST-D3|code=D3|faction=neutral|status=active|tier=neutral|size_class=station_m|size_m2=pending
STATION|id=ST-D4|code=D4|faction=neutral|status=active|tier=neutral|size_class=station_m|size_m2=pending
STATION|id=ST-D5|code=D5|faction=novapolis|status=active|tier=faction|size_class=station_m|size_m2=4250
STATION|id=ST-D6|code=D6|faction=neutral|status=partial|tier=neutral|size_class=station_s|size_m2=pending
STATION|id=ST-D7|code=D7|faction=neutral|status=active|tier=neutral|size_class=station_m|size_m2=pending
STATION|id=ST-E1|code=E1|faction=neutral|status=partial|tier=neutral|size_class=station_s|size_m2=pending
STATION|id=ST-E2|code=E2|faction=neutral|status=active|tier=neutral|size_class=station_m|size_m2=pending
STATION|id=ST-E3|code=E3|faction=novapolis|status=evacuated|tier=faction|size_class=station_l|size_m2=pending
STATION|id=ST-E4|code=E4|faction=neutral|status=restricted|tier=periphery|size_class=station_xs|size_m2=pending
STATION|id=ST-E5|code=E5|faction=neutral|status=active|tier=neutral|size_class=station_s|size_m2=pending
STATION|id=ST-E6|code=E6|faction=neutral|status=partial|tier=neutral|size_class=station_m|size_m2=pending
STATION|id=ST-E7|code=E7|faction=neutral|status=active|tier=neutral|size_class=station_m|size_m2=pending
STATION|id=ST-F1|code=F1|faction=neutral|status=active|tier=neutral|size_class=station_s|size_m2=pending
STATION|id=ST-F2|code=F2|faction=neutral|status=active|tier=neutral|size_class=station_m|size_m2=pending
STATION|id=ST-F3|code=F3|faction=neutral|status=partial|tier=neutral|size_class=station_m|size_m2=pending
STATION|id=ST-F4|code=F4|faction=neutral|status=restricted|tier=periphery|size_class=station_xs|size_m2=pending
STATION|id=ST-F5|code=F5|faction=haendlerbund|status=active|tier=faction|size_class=station_m|size_m2=pending
STATION|id=ST-F6|code=F6|faction=neutral|status=partial|tier=neutral|size_class=station_m|size_m2=pending
STATION|id=ST-F7|code=F7|faction=schattenbund|status=active|tier=faction|size_class=station_m|size_m2=pending
STATION|id=ST-F8|code=F8|faction=neutral|status=partial|tier=neutral|size_class=station_s|size_m2=pending
STATION|id=ST-F9|code=F9|faction=schattenbund|status=active|tier=faction|size_class=station_l|size_m2=pending
STATION|id=ST-G1|code=G1|faction=eisenkonklave|status=active|tier=faction|size_class=station_m|size_m2=pending
STATION|id=ST-G2|code=G2|faction=neutral|status=partial|tier=neutral|size_class=station_s|size_m2=pending
STATION|id=ST-G3|code=G3|faction=neutral|status=active|tier=neutral|size_class=station_s|size_m2=pending
STATION|id=ST-G4|code=G4|faction=neutral|status=restricted|tier=periphery|size_class=station_xs|size_m2=pending
STATION|id=ST-G5|code=G5|faction=haendlerbund|status=partial|tier=faction|size_class=station_m|size_m2=pending
STATION|id=ST-G6|code=G6|faction=fluesterkollektiv|status=active|tier=faction|size_class=station_m|size_m2=pending
STATION|id=ST-G7|code=G7|faction=haendlerbund|status=active|tier=faction|size_class=station_xl|size_m2=pending
STATION|id=ST-H1|code=H1|faction=fluesterkollektiv|status=partial|tier=faction|size_class=station_m|size_m2=pending
STATION|id=ST-H2|code=H2|faction=eisenkonklave|status=active|tier=faction|size_class=station_m|size_m2=pending
STATION|id=ST-H3|code=H3|faction=eisenkonklave|status=partial|tier=faction|size_class=station_m|size_m2=pending
STATION|id=ST-H12|code=H12|faction=eisenkonklave|status=active|tier=faction|size_class=station_xl|size_m2=pending
STATION|id=ST-K4|code=K4|faction=fluesterkollektiv|status=active|tier=faction|size_class=station_l|size_m2=pending

ACCESS|id=AC-A1-01|station=ST-A1|kind=main|status=active
ACCESS|id=AC-A2-01|station=ST-A2|kind=main|status=active
ACCESS|id=AC-A3-01|station=ST-A3|kind=main|status=partial
ACCESS|id=AC-A4-01|station=ST-A4|kind=main|status=partial
ACCESS|id=AC-A5-01|station=ST-A5|kind=main|status=active
ACCESS|id=AC-A6-01|station=ST-A6|kind=main|status=restricted
ACCESS|id=AC-B1-01|station=ST-B1|kind=main|status=active
ACCESS|id=AC-B2-01|station=ST-B2|kind=main|status=active
ACCESS|id=AC-B3-01|station=ST-B3|kind=main|status=active
ACCESS|id=AC-B4-01|station=ST-B4|kind=main|status=active
ACCESS|id=AC-B5-01|station=ST-B5|kind=main|status=partial
ACCESS|id=AC-B6-01|station=ST-B6|kind=main|status=restricted
ACCESS|id=AC-C1-01|station=ST-C1|kind=main|status=active
ACCESS|id=AC-C2-01|station=ST-C2|kind=main|status=active
ACCESS|id=AC-C3-01|station=ST-C3|kind=main|status=partial
ACCESS|id=AC-C4-01|station=ST-C4|kind=main|status=active
ACCESS|id=AC-C5-01|station=ST-C5|kind=main|status=active
ACCESS|id=AC-C6-01|station=ST-C6|kind=main|status=active
ACCESS|id=AC-C7-01|station=ST-C7|kind=main|status=partial
ACCESS|id=AC-D1-01|station=ST-D1|kind=main|status=active
ACCESS|id=AC-D2-01|station=ST-D2|kind=main|status=partial
ACCESS|id=AC-D3-01|station=ST-D3|kind=main|status=active
ACCESS|id=AC-D4-01|station=ST-D4|kind=main|status=active
ACCESS|id=AC-D5-01|station=ST-D5|kind=main|status=active
ACCESS|id=AC-D6-01|station=ST-D6|kind=main|status=partial
ACCESS|id=AC-D7-01|station=ST-D7|kind=main|status=active
ACCESS|id=AC-E1-01|station=ST-E1|kind=main|status=partial
ACCESS|id=AC-E2-01|station=ST-E2|kind=main|status=active
ACCESS|id=AC-E3-01|station=ST-E3|kind=main|status=restricted
ACCESS|id=AC-E4-01|station=ST-E4|kind=main|status=restricted
ACCESS|id=AC-E5-01|station=ST-E5|kind=main|status=active
ACCESS|id=AC-E6-01|station=ST-E6|kind=main|status=partial
ACCESS|id=AC-E7-01|station=ST-E7|kind=main|status=active
ACCESS|id=AC-F1-01|station=ST-F1|kind=main|status=active
ACCESS|id=AC-F2-01|station=ST-F2|kind=main|status=active
ACCESS|id=AC-F3-01|station=ST-F3|kind=main|status=partial
ACCESS|id=AC-F4-01|station=ST-F4|kind=main|status=restricted
ACCESS|id=AC-F5-01|station=ST-F5|kind=main|status=active
ACCESS|id=AC-F6-01|station=ST-F6|kind=main|status=partial
ACCESS|id=AC-F7-01|station=ST-F7|kind=main|status=active
ACCESS|id=AC-F8-01|station=ST-F8|kind=main|status=partial
ACCESS|id=AC-F9-01|station=ST-F9|kind=main|status=active
ACCESS|id=AC-G1-01|station=ST-G1|kind=main|status=active
ACCESS|id=AC-G2-01|station=ST-G2|kind=main|status=partial
ACCESS|id=AC-G3-01|station=ST-G3|kind=main|status=active
ACCESS|id=AC-G4-01|station=ST-G4|kind=main|status=restricted
ACCESS|id=AC-G5-01|station=ST-G5|kind=main|status=partial
ACCESS|id=AC-G6-01|station=ST-G6|kind=main|status=active
ACCESS|id=AC-G7-01|station=ST-G7|kind=main|status=active
ACCESS|id=AC-H1-01|station=ST-H1|kind=main|status=partial
ACCESS|id=AC-H2-01|station=ST-H2|kind=main|status=active
ACCESS|id=AC-H3-01|station=ST-H3|kind=main|status=partial
ACCESS|id=AC-H12-01|station=ST-H12|kind=main|status=active
ACCESS|id=AC-K4-01|station=ST-K4|kind=main|status=active

JUNCTION|id=JB-D5-C6-01|segment=D5-C6|event_slot=enabled|status=active
TUNNEL|id=TN-D5-C6-01|from=AC-D5-01|to=JB-D5-C6-01|status=active
TUNNEL|id=TN-D5-C6-02|from=JB-D5-C6-01|to=AC-C6-01|status=active

JUNCTION|id=JB-C6-E3-01|segment=C6-E3|event_slot=enabled|status=partial
TUNNEL|id=TN-C6-E3-01|from=AC-C6-01|to=JB-C6-E3-01|status=partial
TUNNEL|id=TN-C6-E3-02|from=JB-C6-E3-01|to=AC-E3-01|status=restricted
HAZARD|id=HZ-C6-E3-01|on=TN-C6-E3-02|type=radiation_pocket|severity=high|state=active

JUNCTION|id=JB-C6-C5-01|segment=C6-C5|event_slot=enabled|status=active
TUNNEL|id=TN-C6-C5-01|from=AC-C6-01|to=JB-C6-C5-01|status=active
TUNNEL|id=TN-C6-C5-02|from=JB-C6-C5-01|to=AC-C5-01|status=active
JUNCTION|id=JB-C5-B5-01|segment=C5-B5|event_slot=enabled|status=active
TUNNEL|id=TN-C5-B5-01|from=AC-C5-01|to=JB-C5-B5-01|status=active
TUNNEL|id=TN-C5-B5-02|from=JB-C5-B5-01|to=AC-B5-01|status=partial
JUNCTION|id=JB-B5-A5-01|segment=B5-A5|event_slot=enabled|status=partial
TUNNEL|id=TN-B5-A5-01|from=AC-B5-01|to=JB-B5-A5-01|status=partial
TUNNEL|id=TN-B5-A5-02|from=JB-B5-A5-01|to=AC-A5-01|status=partial
JUNCTION|id=JB-A5-A1-01|segment=A5-A1|event_slot=enabled|status=active
TUNNEL|id=TN-A5-A1-01|from=AC-A5-01|to=JB-A5-A1-01|status=active
TUNNEL|id=TN-A5-A1-02|from=JB-A5-A1-01|to=AC-A1-01|status=active

JUNCTION|id=JB-D5-D4-01|segment=D5-D4|event_slot=enabled|status=active
TUNNEL|id=TN-D5-D4-01|from=AC-D5-01|to=JB-D5-D4-01|status=active
TUNNEL|id=TN-D5-D4-02|from=JB-D5-D4-01|to=AC-D4-01|status=active
JUNCTION|id=JB-D4-C4-01|segment=D4-C4|event_slot=enabled|status=active
TUNNEL|id=TN-D4-C4-01|from=AC-D4-01|to=JB-D4-C4-01|status=active
TUNNEL|id=TN-D4-C4-02|from=JB-D4-C4-01|to=AC-C4-01|status=active
JUNCTION|id=JB-C4-B4-01|segment=C4-B4|event_slot=enabled|status=active
TUNNEL|id=TN-C4-B4-01|from=AC-C4-01|to=JB-C4-B4-01|status=active
TUNNEL|id=TN-C4-B4-02|from=JB-C4-B4-01|to=AC-B4-01|status=active
JUNCTION|id=JB-B4-B3-01|segment=B4-B3|event_slot=enabled|status=active
TUNNEL|id=TN-B4-B3-01|from=AC-B4-01|to=JB-B4-B3-01|status=active
TUNNEL|id=TN-B4-B3-02|from=JB-B4-B3-01|to=AC-B3-01|status=active
JUNCTION|id=JB-B3-B2-01|segment=B3-B2|event_slot=enabled|status=active
TUNNEL|id=TN-B3-B2-01|from=AC-B3-01|to=JB-B3-B2-01|status=active
TUNNEL|id=TN-B3-B2-02|from=JB-B3-B2-01|to=AC-B2-01|status=active

JUNCTION|id=JB-C6-C7-01|segment=C6-C7|event_slot=enabled|status=partial
TUNNEL|id=TN-C6-C7-01|from=AC-C6-01|to=JB-C6-C7-01|status=partial
TUNNEL|id=TN-C6-C7-02|from=JB-C6-C7-01|to=AC-C7-01|status=partial
JUNCTION|id=JB-C7-D7-01|segment=C7-D7|event_slot=enabled|status=active
TUNNEL|id=TN-C7-D7-01|from=AC-C7-01|to=JB-C7-D7-01|status=active
TUNNEL|id=TN-C7-D7-02|from=JB-C7-D7-01|to=AC-D7-01|status=active
JUNCTION|id=JB-D7-E7-01|segment=D7-E7|event_slot=enabled|status=active
TUNNEL|id=TN-D7-E7-01|from=AC-D7-01|to=JB-D7-E7-01|status=active
TUNNEL|id=TN-D7-E7-02|from=JB-D7-E7-01|to=AC-E7-01|status=active
JUNCTION|id=JB-E7-F8-01|segment=E7-F8|event_slot=enabled|status=damaged
TUNNEL|id=TN-E7-F8-01|from=AC-E7-01|to=JB-E7-F8-01|status=damaged
TUNNEL|id=TN-E7-F8-02|from=JB-E7-F8-01|to=AC-F8-01|status=damaged
HAZARD|id=HZ-E7-F8-01|on=TN-E7-F8-01|type=toxic_flooding|severity=medium|state=active
JUNCTION|id=JB-F8-F9-01|segment=F8-F9|event_slot=enabled|status=active
TUNNEL|id=TN-F8-F9-01|from=AC-F8-01|to=JB-F8-F9-01|status=active
TUNNEL|id=TN-F8-F9-02|from=JB-F8-F9-01|to=AC-F9-01|status=active

JUNCTION|id=JB-E3-E2-01|segment=E3-E2|event_slot=enabled|status=restricted
TUNNEL|id=TN-E3-E2-01|from=AC-E3-01|to=JB-E3-E2-01|status=restricted
TUNNEL|id=TN-E3-E2-02|from=JB-E3-E2-01|to=AC-E2-01|status=damaged
HAZARD|id=HZ-E3-E2-01|on=TN-E3-E2-02|type=structural_instability|severity=high|state=active
JUNCTION|id=JB-E2-F2-01|segment=E2-F2|event_slot=enabled|status=active
TUNNEL|id=TN-E2-F2-01|from=AC-E2-01|to=JB-E2-F2-01|status=active
TUNNEL|id=TN-E2-F2-02|from=JB-E2-F2-01|to=AC-F2-01|status=active
JUNCTION|id=JB-F2-G2-01|segment=F2-G2|event_slot=enabled|status=partial
TUNNEL|id=TN-F2-G2-01|from=AC-F2-01|to=JB-F2-G2-01|status=partial
TUNNEL|id=TN-F2-G2-02|from=JB-F2-G2-01|to=AC-G2-01|status=partial
JUNCTION|id=JB-G2-G7-01|segment=G2-G7|event_slot=enabled|status=active
TUNNEL|id=TN-G2-G7-01|from=AC-G2-01|to=JB-G2-G7-01|status=active
TUNNEL|id=TN-G2-G7-02|from=JB-G2-G7-01|to=AC-G7-01|status=active

JUNCTION|id=JB-G7-H3-01|segment=G7-H3|event_slot=enabled|status=active
TUNNEL|id=TN-G7-H3-01|from=AC-G7-01|to=JB-G7-H3-01|status=active
TUNNEL|id=TN-G7-H3-02|from=JB-G7-H3-01|to=AC-H3-01|status=active
JUNCTION|id=JB-H3-H12-01|segment=H3-H12|event_slot=enabled|status=damaged
TUNNEL|id=TN-H3-H12-01|from=AC-H3-01|to=JB-H3-H12-01|status=damaged
TUNNEL|id=TN-H3-H12-02|from=JB-H3-H12-01|to=AC-H12-01|status=damaged
HAZARD|id=HZ-H3-H12-01|on=TN-H3-H12-01|type=magnetic_interference|severity=medium|state=active

JUNCTION|id=JB-F9-G6-01|segment=F9-G6|event_slot=enabled|status=active
TUNNEL|id=TN-F9-G6-01|from=AC-F9-01|to=JB-F9-G6-01|status=active
TUNNEL|id=TN-F9-G6-02|from=JB-F9-G6-01|to=AC-G6-01|status=active
JUNCTION|id=JB-G6-H2-01|segment=G6-H2|event_slot=enabled|status=partial
TUNNEL|id=TN-G6-H2-01|from=AC-G6-01|to=JB-G6-H2-01|status=partial
TUNNEL|id=TN-G6-H2-02|from=JB-G6-H2-01|to=AC-H2-01|status=partial
JUNCTION|id=JB-H2-K4-01|segment=H2-K4|event_slot=enabled|status=restricted
TUNNEL|id=TN-H2-K4-01|from=AC-H2-01|to=JB-H2-K4-01|status=restricted
TUNNEL|id=TN-H2-K4-02|from=JB-H2-K4-01|to=AC-K4-01|status=restricted
HAZARD|id=HZ-H2-K4-01|on=TN-H2-K4-02|type=signal_distortion|severity=high|state=active

JUNCTION|id=JB-A1-A2-01|segment=A1-A2|event_slot=enabled|status=active
TUNNEL|id=TN-A1-A2-01|from=AC-A1-01|to=JB-A1-A2-01|status=active
TUNNEL|id=TN-A1-A2-02|from=JB-A1-A2-01|to=AC-A2-01|status=active
JUNCTION|id=JB-A2-B1-01|segment=A2-B1|event_slot=enabled|status=active
TUNNEL|id=TN-A2-B1-01|from=AC-A2-01|to=JB-A2-B1-01|status=active
TUNNEL|id=TN-A2-B1-02|from=JB-A2-B1-01|to=AC-B1-01|status=active
JUNCTION|id=JB-B1-B2-01|segment=B1-B2|event_slot=enabled|status=partial
TUNNEL|id=TN-B1-B2-01|from=AC-B1-01|to=JB-B1-B2-01|status=partial
TUNNEL|id=TN-B1-B2-02|from=JB-B1-B2-01|to=AC-B2-01|status=partial

JUNCTION|id=JB-B2-C3-01|segment=B2-C3|event_slot=enabled|status=active
TUNNEL|id=TN-B2-C3-01|from=AC-B2-01|to=JB-B2-C3-01|status=active
TUNNEL|id=TN-B2-C3-02|from=JB-B2-C3-01|to=AC-C3-01|status=active
JUNCTION|id=JB-C3-D3-01|segment=C3-D3|event_slot=enabled|status=partial
TUNNEL|id=TN-C3-D3-01|from=AC-C3-01|to=JB-C3-D3-01|status=partial
TUNNEL|id=TN-C3-D3-02|from=JB-C3-D3-01|to=AC-D3-01|status=partial
HAZARD|id=HZ-C3-D3-01|on=TN-C3-D3-01|type=micro_collapse|severity=low|state=active
JUNCTION|id=JB-D3-D5-01|segment=D3-D5|event_slot=enabled|status=active
TUNNEL|id=TN-D3-D5-01|from=AC-D3-01|to=JB-D3-D5-01|status=active
TUNNEL|id=TN-D3-D5-02|from=JB-D3-D5-01|to=AC-D5-01|status=active

JUNCTION|id=JB-G7-G5-01|segment=G7-G5|event_slot=enabled|status=active
TUNNEL|id=TN-G7-G5-01|from=AC-G7-01|to=JB-G7-G5-01|status=active
TUNNEL|id=TN-G7-G5-02|from=JB-G7-G5-01|to=AC-G5-01|status=active
JUNCTION|id=JB-G5-F5-01|segment=G5-F5|event_slot=enabled|status=partial
TUNNEL|id=TN-G5-F5-01|from=AC-G5-01|to=JB-G5-F5-01|status=partial
TUNNEL|id=TN-G5-F5-02|from=JB-G5-F5-01|to=AC-F5-01|status=partial
HAZARD|id=HZ-G5-F5-01|on=TN-G5-F5-02|type=steam_vent|severity=medium|state=active
JUNCTION|id=JB-F5-F9-01|segment=F5-F9|event_slot=enabled|status=active
TUNNEL|id=TN-F5-F9-01|from=AC-F5-01|to=JB-F5-F9-01|status=active
TUNNEL|id=TN-F5-F9-02|from=JB-F5-F9-01|to=AC-F9-01|status=active

JUNCTION|id=JB-H12-H1-01|segment=H12-H1|event_slot=enabled|status=partial
TUNNEL|id=TN-H12-H1-01|from=AC-H12-01|to=JB-H12-H1-01|status=partial
TUNNEL|id=TN-H12-H1-02|from=JB-H12-H1-01|to=AC-H1-01|status=partial
JUNCTION|id=JB-H1-G1-01|segment=H1-G1|event_slot=enabled|status=active
TUNNEL|id=TN-H1-G1-01|from=AC-H1-01|to=JB-H1-G1-01|status=active
TUNNEL|id=TN-H1-G1-02|from=JB-H1-G1-01|to=AC-G1-01|status=active
JUNCTION|id=JB-G1-G7-01|segment=G1-G7|event_slot=enabled|status=damaged
TUNNEL|id=TN-G1-G7-01|from=AC-G1-01|to=JB-G1-G7-01|status=damaged
TUNNEL|id=TN-G1-G7-02|from=JB-G1-G7-01|to=AC-G7-01|status=damaged
HAZARD|id=HZ-G1-G7-01|on=TN-G1-G7-01|type=power_arc|severity=medium|state=active

JUNCTION|id=JB-K4-F7-01|segment=K4-F7|event_slot=enabled|status=restricted
TUNNEL|id=TN-K4-F7-01|from=AC-K4-01|to=JB-K4-F7-01|status=restricted
TUNNEL|id=TN-K4-F7-02|from=JB-K4-F7-01|to=AC-F7-01|status=restricted
JUNCTION|id=JB-F7-F9-01|segment=F7-F9|event_slot=enabled|status=active
TUNNEL|id=TN-F7-F9-01|from=AC-F7-01|to=JB-F7-F9-01|status=active
TUNNEL|id=TN-F7-F9-02|from=JB-F7-F9-01|to=AC-F9-01|status=active
HAZARD|id=HZ-K4-F7-01|on=TN-K4-F7-01|type=echo_resonance|severity=high|state=active

JUNCTION|id=JB-C2-C1-01|segment=C2-C1|event_slot=enabled|status=active
TUNNEL|id=TN-C2-C1-01|from=AC-C2-01|to=JB-C2-C1-01|status=active
TUNNEL|id=TN-C2-C1-02|from=JB-C2-C1-01|to=AC-C1-01|status=active
JUNCTION|id=JB-C1-D1-01|segment=C1-D1|event_slot=enabled|status=active
TUNNEL|id=TN-C1-D1-01|from=AC-C1-01|to=JB-C1-D1-01|status=active
TUNNEL|id=TN-C1-D1-02|from=JB-C1-D1-01|to=AC-D1-01|status=active
JUNCTION|id=JB-D1-D2-01|segment=D1-D2|event_slot=enabled|status=partial
TUNNEL|id=TN-D1-D2-01|from=AC-D1-01|to=JB-D1-D2-01|status=partial
TUNNEL|id=TN-D1-D2-02|from=JB-D1-D2-01|to=AC-D2-01|status=partial
JUNCTION|id=JB-D2-E1-01|segment=D2-E1|event_slot=enabled|status=active
TUNNEL|id=TN-D2-E1-01|from=AC-D2-01|to=JB-D2-E1-01|status=active
TUNNEL|id=TN-D2-E1-02|from=JB-D2-E1-01|to=AC-E1-01|status=active
JUNCTION|id=JB-E1-E2-01|segment=E1-E2|event_slot=enabled|status=active
TUNNEL|id=TN-E1-E2-01|from=AC-E1-01|to=JB-E1-E2-01|status=active
TUNNEL|id=TN-E1-E2-02|from=JB-E1-E2-01|to=AC-E2-01|status=active

JUNCTION|id=JB-A3-A4-01|segment=A3-A4|event_slot=enabled|status=partial
TUNNEL|id=TN-A3-A4-01|from=AC-A3-01|to=JB-A3-A4-01|status=partial
TUNNEL|id=TN-A3-A4-02|from=JB-A3-A4-01|to=AC-A4-01|status=partial
JUNCTION|id=JB-A4-A6-01|segment=A4-A6|event_slot=enabled|status=restricted
TUNNEL|id=TN-A4-A6-01|from=AC-A4-01|to=JB-A4-A6-01|status=restricted
TUNNEL|id=TN-A4-A6-02|from=JB-A4-A6-01|to=AC-A6-01|status=restricted
HAZARD|id=HZ-A4-A6-01|on=TN-A4-A6-01|type=debris_field|severity=medium|state=active

JUNCTION|id=JB-E4-E5-01|segment=E4-E5|event_slot=enabled|status=restricted
TUNNEL|id=TN-E4-E5-01|from=AC-E4-01|to=JB-E4-E5-01|status=restricted
TUNNEL|id=TN-E4-E5-02|from=JB-E4-E5-01|to=AC-E5-01|status=restricted
JUNCTION|id=JB-E5-E6-01|segment=E5-E6|event_slot=enabled|status=partial
TUNNEL|id=TN-E5-E6-01|from=AC-E5-01|to=JB-E5-E6-01|status=partial
TUNNEL|id=TN-E5-E6-02|from=JB-E5-E6-01|to=AC-E6-01|status=partial
JUNCTION|id=JB-E6-F6-01|segment=E6-F6|event_slot=enabled|status=active
TUNNEL|id=TN-E6-F6-01|from=AC-E6-01|to=JB-E6-F6-01|status=active
TUNNEL|id=TN-E6-F6-02|from=JB-E6-F6-01|to=AC-F6-01|status=active
JUNCTION|id=JB-F6-G6-01|segment=F6-G6|event_slot=enabled|status=active
TUNNEL|id=TN-F6-G6-01|from=AC-F6-01|to=JB-F6-G6-01|status=active
TUNNEL|id=TN-F6-G6-02|from=JB-F6-G6-01|to=AC-G6-01|status=active

JUNCTION|id=JB-F1-F3-01|segment=F1-F3|event_slot=enabled|status=partial
TUNNEL|id=TN-F1-F3-01|from=AC-F1-01|to=JB-F1-F3-01|status=partial
TUNNEL|id=TN-F1-F3-02|from=JB-F1-F3-01|to=AC-F3-01|status=partial
JUNCTION|id=JB-F3-F4-01|segment=F3-F4|event_slot=enabled|status=restricted
TUNNEL|id=TN-F3-F4-01|from=AC-F3-01|to=JB-F3-F4-01|status=restricted
TUNNEL|id=TN-F3-F4-02|from=JB-F3-F4-01|to=AC-F4-01|status=restricted
HAZARD|id=HZ-F3-F4-01|on=TN-F3-F4-02|type=contamination|severity=medium|state=active

JUNCTION|id=JB-G3-G4-01|segment=G3-G4|event_slot=enabled|status=collapsed
TUNNEL|id=TN-G3-G4-01|from=AC-G3-01|to=JB-G3-G4-01|status=collapsed
TUNNEL|id=TN-G3-G4-02|from=JB-G3-G4-01|to=AC-G4-01|status=dead_end
HAZARD|id=HZ-G3-G4-01|on=TN-G3-G4-01|type=hard_collapse|severity=high|state=active

JUNCTION|id=JB-D6-DEAD-01|segment=D6-DEAD|event_slot=enabled|status=collapsed
TUNNEL|id=TN-D6-DEAD-01|from=AC-D6-01|to=JB-D6-DEAD-01|status=dead_end
HAZARD|id=HZ-D6-DEAD-01|on=TN-D6-DEAD-01|type=collapse|severity=high|state=active
JUNCTION|id=JB-B6-DEAD-01|segment=B6-DEAD|event_slot=enabled|status=flooded
TUNNEL|id=TN-B6-DEAD-01|from=AC-B6-01|to=JB-B6-DEAD-01|status=dead_end
HAZARD|id=HZ-B6-DEAD-01|on=TN-B6-DEAD-01|type=deep_flooding|severity=high|state=active
JUNCTION|id=JB-G4-DEAD-01|segment=G4-DEAD|event_slot=enabled|status=sealed
TUNNEL|id=TN-G4-DEAD-01|from=AC-G4-01|to=JB-G4-DEAD-01|status=dead_end
HAZARD|id=HZ-G4-DEAD-01|on=TN-G4-DEAD-01|type=spore_zone|severity=medium|state=active
```

Hinweis zum Ausbaustand
-----------------------

- 54 Stationen sind verteilt und mit je einem Primärzugang angelegt.
- Detaillierte Tunnelpfade decken Fraktionsanker, Transitachsen und erste Alternativrouten ab.
- Zusätzliche Nebenarme decken nun auch den Großteil der Restsegmente ab; wenige Ausnahmen bleiben bewusst `tbd`.

Stichprobencheck Funktionalitaet/Logik
--------------------------------------

- Referenzintegrität geprüft: `MISSING_REFS=0` (alle `station/from/to/on`-Referenzen zeigen auf existente IDs).
- Pfadstichproben geprüft und gefunden: `ST-D5 -> ST-C6`, `ST-D5 -> ST-A1`, `ST-D5 -> ST-B2`, `ST-D5 -> ST-G7`, `ST-D5 -> ST-K4`.
- Logikbefund: Primär- und Alternativrouten sind durchgängig navigierbar; Gefahrenstellen beeinflussen Risiko/Status, blockieren aber nicht das gesamte Netz.

Kernnetz (belegt)
-----------------

- D5 ↔ Verbindungstunnel D5-C6 ↔ C6
- C6 ↔ Verbindungstunnel C6-E3 ↔ E3

Externe Knoten (bekannt, Anbindung offen)
-----------------------------------------

- A1
- H12
- G7
- F9
- B2
- K4

Operativer Lageblick T0 (MVP)
-----------------------------

| Segment | Status | Risiko | Hinweis |
| --- | --- | --- | --- |
| D5-C6 | aktiv | mittel | Kernpfad Novapolis, Monitoring laufend |
| C6-E3 | eingeschraenkt | mittel-hoch | E3 gilt als evakuiert; Nutzung fallweise |
| Externe Anbindung | teilaktiv | mittel-hoch | mehrere Routen angelegt, Teilabschnitte beschädigt/risikobehaftet |
| Alternativkorridore | teilaktiv | mittel | je Fraktionsanker mindestens ein Nebenarm mit neutralem Puffer |

Guardrails
----------

- Keine Mengen-, Kapazitaets- oder Fahrzeitwerte ohne belastbare Belege eintragen.
- Unklare Verbindungen als `tbd` kennzeichnen statt implizit zu normalisieren.
- Fraktionsspezifische Details bleiben in `01-factions/*`.

Verlinkungen
------------

- [Metrograph](./Metrograph.md)
- [Ortsgraph](./Ortsgraph.md)
- [Stationskontroll-Matrix](./Stationskontroll-Matrix.md)
- [Current-State](./Current-State.md)
