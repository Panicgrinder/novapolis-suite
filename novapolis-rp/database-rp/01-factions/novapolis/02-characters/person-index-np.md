---
stand: 2026-02-23 06:46
update: C6-Helper-Namen Mikk/Lira/Darek mit Rollenankern im Personenindex ergänzt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-02-23 06:46); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md' 'novapolis-rp/database-rp/01-factions/novapolis/02-characters/C6-Bewohner.md' 'novapolis-rp/database-rp/01-factions/novapolis/02-characters/person-index-np.md' 'novapolis-dev/docs/donelog.md' PASS (EXITCODE=0, 2026-02-23 06:46); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-23 06:46)
slug: person-index-np
canvas: person_index_np
last_updated: 2026-02-23T06:46:18+01:00
category: admin
version: 0.9
---

Personenindex Novapolis (person-index-np)
=========================================

Hinweis: Felder gemäß Beschluss - Name, Rolle(n), Zugehörigkeit, Status, Notizen, Verlinkungen. Wöchentliche Pflege (siehe INDEX-CYCLE).

|Name|Rolle(n)|Zugehörigkeit|Status|Notizen|Verlinkungen|
|----|-------:|-----------:|-----:|--------|------------:|
|Jonas Merek|Technik, Logistik|Novapolis (D5)|aktiv|Werkstatt/Funk D5↔C6; Lumen-Kopplung; Schwester vermisst (FACT [JONAS-SIS])|[Jonas](./Jonas-Merek.md), [D5](../03-locations/D5.md)|
|Nika Perez|Quartiermeisterin (D5), Inventar & Ausgabe|Novapolis (D5)|aktiv|Ausrüstung/Materialausgabe, Priorisierung & Ausgabeprotokolle; Schnittstelle zu Pahl (Sicherheit) und Ronja (Freigaben)|[Nika Perez](./Nika-Perez.md), [D5](../03-locations/D5.md)|
|Kora Malenkov|Stellvertretung (Novapolis), Leitung C6, Handel|Novapolis (C6)|aktiv|Interne Leitung C6, Außenhandel über C6, Echo-Protokolle, Abgleich mit Marven/Arlen (FACT [CARAVAN-LEADERSHIP])|[Kora](./Kora-Malenkov.md), [C6](../03-locations/C6.md), [Logistik](../../../00-admin/Logistik.md)|
|Marven Kael|Konvoiführung, Handelskoordination|Novapolis (C6)|aktiv|Führt Konvoi, Sicherheits-/Verhandlungsprotokolle, wahrt Koordinatenschutz (FACT [FR-KNOWLEDGE])|[Marven](./Marven-Kael.md), [caravan-moves](../../haendlerbund/05-projects/caravan-moves.md), [C6](../03-locations/C6.md)|
|Ronja Kerschner|Leitung (Novapolis, D5), Diplomatie, Technik|Novapolis (D5/C6)|aktiv|Fraktionsleitung + Standortleitung D5; Außenkontakte/Diplomatie in Abstimmung mit C6-Handel|[Ronja](./Ronja-Kerschner.md), [Reflex](./Reflex.md)|
|Pahl Brenner|Sicherheit (Officer), Technik, Wartungsleitung|Novapolis (D5)|aktiv (Reha)|Sicherheit/Freigaben (intern), Hausregeln; Überlebender C6-Reaktorunfall; Jonas überwacht Atemlog|[Pahl Brenner](./Pahl-Brenner.md), [D5](../03-locations/D5.md), [C6](../03-locations/C6.md)|
|Lyra Hest|Stellv. Leitung Zivil/Logistik|Novapolis (D5/C6)|aktiv|Stellvertretung gemäß Beschluss A.2 (Zivil/Logistik)|[Lyra Hest](./Lyra-Hest.md), [D5](../03-locations/D5.md), [C6](../03-locations/C6.md)|
|Senn Daru|Händler/Vermittler|Novapolis (C6)|aktiv|Kontakt/Protokolle (u. a. Richtung G7) nach Anschluss der Karawane H-47|[Senn Daru](./Senn-Daru.md), [C6](../03-locations/C6.md)|
|Arlen Dross|Händler/Vermittler|Novapolis (C6)|aktiv|Moderiert Karawane↔Außenkontakte, reflektiert Freiheits-/Verantwortungsbalance (FACT [CARAVAN-LEADERSHIP])|[Arlen](./Arlen-Dross.md), [caravan-moves](../../haendlerbund/05-projects/caravan-moves.md), [C6](../03-locations/C6.md)|
|Mikk Renn|C6-Helper (Absicherung/Wache)|Novapolis (C6)|aktiv|Fester C6-Bewohner aus H-47; sichert Randposten und Zugänge A/B/C|[C6-Bewohner](./C6-Bewohner.md), [C6](../03-locations/C6.md)|
|Lira Vas|C6-Helper (Transport/Lagerlauf)|Novapolis (C6)|aktiv|Feste C6-Bewohnerin aus H-47; koordiniert Umlagerung und interne Laufwege|[C6-Bewohner](./C6-Bewohner.md), [C6](../03-locations/C6.md)|
|Darek Holv|C6-Helper (Tunnelinstandsetzung)|Novapolis (C6)|aktiv|Fester C6-Bewohner aus H-47; unterstützt schwere Reparaturarbeiten im Nordlinien-Umfeld|[C6-Bewohner](./C6-Bewohner.md), [C6](../03-locations/C6.md)|
|Tess Avari|Vermittlerin (Deals, Lieferfenster)|Novapolis (C6)|aktiv|Moderiert Übergaben, besteht auf Log-Disziplin (Protokoll/Funk)|[Tess Avari](./Tess-Avari.md), [C6](../03-locations/C6.md)|
|Darian Voss|Konvoi-Sicherheit / Scouts|Novapolis (C6)|aktiv|Sichert Übergaben, erkennt Muster in Überfällen|[Darian Voss](./Darian-Voss.md), [caravan-moves](../../haendlerbund/05-projects/caravan-moves.md), [C6](../03-locations/C6.md)|
|Varek Solun|Kommandant Militär/Zivil|Eisenkonklave (H12/Sektor_H3)|aktiv|Führt Konklave, sucht Union-Hauptarchiv; Novapolis nur als Gerücht|[Varek Solun](../../eisenkonklave/02-characters/Varek-Solun.md)|
|Liora Navesh|Leiterin Forschungsrat / Chefärztin Biotechnologie|Arkologie A1|aktiv|Fokussiert auf SÜDFRAGMENT-Signale; keine bestätigten Novapolis-Kenntnisse|[Liora Navesh](../../arkologie-a1/02-characters/Liora-Navesh.md)|
|Marei Falk|Stellvertretung C6, ehem. Stationsleitung E3|Novapolis (C6)|aktiv|Koordiniert Evakuierte, Inventar- und Logistikabgleich D5↔C6|[Marei Falk](./Marei-Falk.md), [C6](../03-locations/C6.md), [E3](../03-locations/E3.md)|

Legende Zugehörigkeit: Station/Fraktion. Bitte Links auf Charakter-/Lokations-Canvas ergänzen.



