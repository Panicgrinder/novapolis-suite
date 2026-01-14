---
stand: 2026-01-14 17:50
update: "Karawane H-47: Zugehörigkeit/Standort auf Novapolis (C6) korrigiert; Tess Avari und Darian Voss ergänzt.; Checks PASS."
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc **/*.md PASS (2026-01-14 17:50); & .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py novapolis-rp\\database-rp PASS (2026-01-14 17:50); & .\\.venv\\Scripts\\python.exe scripts\\checks_rp_consistency.py --strict PASS (2026-01-14 17:50); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:rp PASS (2026-01-14 17:50); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:crossrefs PASS (2026-01-14 17:50)
slug: person-index-np
canvas: person_index_np
last-updated: 2026-01-14T17:31:10+01:00
category: A
version: 0.9
---

Personenindex Novapolis (person_index_np)
=========================================

Hinweis: Felder gemäß Beschluss - Name, Rolle(n), Zugehörigkeit, Status, Notizen, Verlinkungen. Wöchentliche Pflege (siehe INDEX-CYCLE).

|Name|Rolle(n)|Zugehörigkeit|Status|Notizen|Verlinkungen|
|----|-------:|-----------:|-----:|--------|------------:|
|Jonas Merek|Technik, Logistik|Novapolis (D5)|aktiv|Werkstatt/Funk D5↔C6; Lumen-Kopplung; Schwester vermisst (FACT [JONAS-SIS])|[Jonas](../01-factions/novapolis/02-characters/Jonas-Merek.md), [D5](../01-factions/novapolis/03-locations/D5.md)|
|Kora Malenkov|Logistikkoordination C6|Novapolis (C6)|aktiv|Interne Leitung, Echo-Protokolle, Abgleich mit Marven/Arlen (FACT [CARAVAN-LEADERSHIP])|[Kora](../01-factions/haendlerbund/02-characters/Kora-Malenkov.md), [C6](../01-factions/novapolis/03-locations/C6.md), [Logistik](../00-admin/Logistik.md)|
|Marven Kael|Konvoiführung, Handelskoordination|Novapolis (C6)|aktiv|Führt Konvoi, Sicherheits-/Verhandlungsprotokolle, wahrt Koordinatenschutz (FACT [FR-KNOWLEDGE])|[Marven](../01-factions/haendlerbund/02-characters/Marven-Kael.md), [caravan_moves](../01-factions/haendlerbund/05-projects/caravan_moves.md), [C6](../01-factions/novapolis/03-locations/C6.md)|
|Ronja Kerschner|Leitung, Technik|Novapolis (D5/C6)|aktiv|Bezugsperson Reflex; Routine 7 Tage, Stressmonitor aktiv|[Ronja](../01-factions/novapolis/02-characters/Ronja-Kerschner.md), [Reflex](../01-factions/novapolis/02-characters/Reflex.md)|
|Pahl|Technik, Wartungsleitung|Novapolis (D5)|aktiv (Reha)|Einziger Überlebender C6-Reaktorunfall; Ronja/Reflex Rettung, Jonas überwacht Atemlog & Hausregeln|[Pahl](../01-factions/novapolis/02-characters/Pahl.md), [D5](../01-factions/novapolis/03-locations/D5.md), [C6](../01-factions/novapolis/03-locations/C6.md)|
|Lyra Hest|Stellv. Leitung Zivil/Logistik|Novapolis (D5/C6)|aktiv|Stellvertretung gemäß Beschluss A.2 (Zivil/Logistik)|[Lyra Hest](../01-factions/novapolis/02-characters/Lyra-Hest.md), [D5](../01-factions/novapolis/03-locations/D5.md), [C6](../01-factions/novapolis/03-locations/C6.md)|
|Senn Daru|Händler/Vermittler|Novapolis (C6)|aktiv|Kontakt/Protokolle (u. a. Richtung G7) nach Anschluss der Karawane H-47|[Senn Daru](../01-factions/haendlerbund/02-characters/Senn-Daru.md), [C6](../01-factions/novapolis/03-locations/C6.md)|
|Arlen Dross|Händler/Vermittler|Novapolis (C6)|aktiv|Moderiert Karawane↔Außenkontakte, reflektiert Freiheits-/Verantwortungsbalance (FACT [CARAVAN-LEADERSHIP])|[Arlen](../01-factions/haendlerbund/02-characters/Arlen-Dross.md), [caravan_moves](../01-factions/haendlerbund/05-projects/caravan_moves.md), [C6](../01-factions/novapolis/03-locations/C6.md)|
|Tess Avari|Vermittlerin (Deals, Lieferfenster)|Novapolis (C6)|aktiv|Moderiert Übergaben, besteht auf Log-Disziplin (Protokoll/Funk)|[Tess Avari](../01-factions/haendlerbund/02-characters/Tess-Avari.md), [C6](../01-factions/novapolis/03-locations/C6.md)|
|Darian Voss|Konvoi-Sicherheit / Scouts|Novapolis (C6)|aktiv|Sichert Übergaben, erkennt Muster in Überfällen|[Darian Voss](../01-factions/haendlerbund/02-characters/Darian-Voss.md), [caravan_moves](../01-factions/haendlerbund/05-projects/caravan_moves.md), [C6](../01-factions/novapolis/03-locations/C6.md)|
|Varek Solun|Kommandant Militär/Zivil|Eisenkonklave (H12/Sektor_H3)|aktiv|Führt Konklave, sucht Union-Hauptarchiv; Novapolis nur als Gerücht|[Varek Solun](../01-factions/eisenkonklave/02-characters/Varek-Solun.md)|
|Liora Navesh|Leiterin Forschungsrat / Chefärztin Biotechnologie|Arkologie A1|aktiv|Fokussiert auf SÜDFRAGMENT-Signale; keine bestätigten Novapolis-Kenntnisse|[Liora Navesh](../01-factions/novapolis/02-characters/Liora-Navesh.md)|
|Marei|Stellvertretung C6, ehem. Stationsleitung E3|Novapolis (C6)|aktiv|Koordiniert Evakuierte, Inventar- und Logistikabgleich D5↔C6|[Marei](../01-factions/novapolis/02-characters/Marei.md), [C6](../01-factions/novapolis/03-locations/C6.md), [E3](../01-factions/novapolis/03-locations/E3.md)|

Legende Zugehörigkeit: Station/Fraktion. Bitte Links auf Charakter-/Lokations-Canvas ergänzen.



