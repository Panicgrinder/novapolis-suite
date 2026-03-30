---
stand: 2026-03-30 07:16
update: Die fraktionsscharfe Metro-Zuteilungsmatrix ist in ein operatives Arbeitsledger mit Zielpfaden und Updatekette ueberfuehrt.
checks: snapshot-lock PASS; markdownlint PASS; frontmatter PASS; todo-index PASS; naming-policy PASS; path-portability PASS; logs-policy PASS; doc-freshness PASS (2026-03-30 07:16)
---

RP-Arbeitsledger: Finale Metro-Warenzuteilung (2026-03-30)
==========================================================

Ziel
----

- Dieses Arbeitsledger ueberfuehrt die vorhandene Matrix `hart gesetzt | konservativ geschaetzt | manuell zu entscheiden` in direkte Arbeitszeilen fuer die naechste RP-Handverteilung.
- Es ist bewusst kein neues SSOT fuer Mengen, sondern die operative Zwischenebene zwischen Matrix und den Zielinventaren.

Verbindliche Lesart
-------------------

- `fix`: darf ohne neue Annahmen in den Zielpfad uebernommen werden.
- `rahmenwert`: darf nur als konservativer Rahmen oder Prozessanker uebernommen werden, nicht als exakte Menge.
- `handentscheidung`: bleibt sichtbar `tbd`, bis eine echte Entscheidung oder neue Belegkette vorliegt.
- Neue sichtbare Setzungen duerfen nur aus der Spalte `handentscheidung` stammen; `fix` und `rahmenwert` uebernehmen nur bereits belegte oder bewusst weiche Aussagen.

Operative Reihenfolge
---------------------

1. `fix`-Zeilen in Stations- und Fraktionsinventare uebernehmen.
2. `rahmenwert`-Zeilen nur als Kontext- oder Prozessrahmen in den Zielpfaden verankern.
3. `handentscheidung`-Zeilen offen halten, bis Transferkette, Delta-/Bilanzformat oder eine manuelle Verteilung den Punkt schliessen.
4. Danach erst die Fortschreibung in `Novapolis-inventar.md` und die spaetere Rueckspiegelung in die Metro-Ebene anpassen.

Fix-Sockel
----------

| Status | Station / Zielraum | Fraktion | Ledger-Satz | Zielpfad | Updatepfad | Kernquellen |
| --- | --- | --- | --- | --- | --- | --- |
| fix | D5 | Novapolis | D5 fuehrt einen belegten Stationsanker mit `Union-Kisten (3)`, leeren Filterkartuschen, Ersatzrohr-/Ventilkontext, defekter Reparaturstation und der Energiebilanz Tag 12 -> 13 `+10 - 8 - 12 = -10`. | `novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md` | `D5-inventar.md` -> `Novapolis-inventar.md` -> `00-admin/Warenueberblick-T0.md` | Matrix, `D5-inventar.md`, `RAW-canvas-2025-10-16T12-00-00-000Z.normalized.txt` |
| fix | C6 | Novapolis | C6 fuehrt einen quantifizierten Startsnapshot mit `Luftfilter 3`, `Ersatzrohre 12`, `Kabelspulen 6`, `Schmieroel 5`, `Strommodule 2`, `Wasserkanister 4`, `Werkzeugsets 2`, `Sensorpaket 1`, `Rationen 9`, `Wasserflaschen 10`, `Schutzanzuege 2`, `Ersatzmasken 3` plus lokaler Werkzeugliste; Energiedelta Tag 12 -> 13 bleibt `+10 Zufuhr` bei `+12 Verbrauch`. | `novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md` | `C6-inventar.md` -> `Novapolis-inventar.md` -> `00-admin/Warenueberblick-T0.md` | Matrix, `C6-inventar.md`, `RAW-canvas-2025-10-16T12-30-00-000Z.normalized.txt`, `RAW-canvas-2025-10-16T12-55-00-000Z.normalized.txt` |
| fix | D5 -> C6 | Novapolis | Der Versorgungslauf `D5 -> C6` ist als Missions- und Frachtanker belegt; uebernommen wird nur der Prozessrahmen `Abmeldung -> Ankunft -> Bestandsaufnahme -> bestaetigter Empfang`, nicht aber eine Mengenbuchung. | `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Missionslog-Novapolis.md` | `Missionslog-Novapolis.md` -> spaeter `D5-inventar.md` und `C6-inventar.md` | Matrix, `Missionslog-Novapolis.md`, `rp-inventory-backfill-pilot-2026-03-20.md` |
| fix | D5/C6 fraktionsweit | Novapolis | Tag 12 -> 13 fuehrt das harte Verbrauchsdelta `1,3 t Baustoffe`, `120 m Schienenprofil`, `18 m2 Betonplatten`, `2` beschaedigte Werkzeuge`; der Standortsplit bleibt ausdruecklich offen. | `novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md` | `Novapolis-inventar.md` -> spaeter standortscharfer Split in `D5-inventar.md` / `C6-inventar.md` | Matrix, `Novapolis-inventar.md`, `chat-export.normalized.txt` |

Rahmenwerte
-----------

| Status | Station / Zielraum | Fraktion | Ledger-Satz | Zielpfad | Updatepfad | Kernquellen |
| --- | --- | --- | --- | --- | --- | --- |
| rahmenwert | D5 Materiallager / Werkstatt | Novapolis | Der Quellraum fuer schwere Reparatur- und Versorgungsgueter ist konservativ als `D5-Materiallager unter dem Bahnsteig und/oder Werkstattbestand` lesbar; konkrete Entnahmen bleiben offen. | `novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md` | Kontext erst in `D5-inventar.md`, spaeter nur bei belegter Entnahme nach `Novapolis-inventar.md` promoten | Matrix, `rp-inventory-backfill-pilot-2026-03-20.md`, `D5-inventar.md` |
| rahmenwert | C6 Primaer- / Sekundaerlager | Novapolis | Die Zielseite des Laufs endet plausibel in bestaetigtem Empfang mit nachgelagerter Baustellenverteilung; konkrete Lagerzuordnung zwischen Primaer- und Sekundaerlager bleibt offen. | `novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md` | Prozessrahmen in `C6-inventar.md`, Zielbuchung erst nach neuer Belegzeile | Matrix, `rp-inventory-backfill-pilot-2026-03-20.md`, `C6-inventar.md` |
| rahmenwert | D5 + C6 | Novapolis | Das Fraktionsaggregat bleibt Bilanz- und Risikoebene; es fuehrt keine harte Restmenge, solange Transfer- und Verbrauchskette nicht komplett belegt sind. | `novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md` | `D5-inventar.md` + `C6-inventar.md` -> `Novapolis-inventar.md` | Matrix, `Novapolis-inventar.md` |
| rahmenwert | externe Stationen tbd | Arkologie-A1 | Arkologie-A1 bleibt als etablierter Block mit stabiler Grundversorgung und selektiven Austauschguetern gerahmt; exakte Mengen bleiben offen. | `novapolis-rp/database-rp/01-factions/arkologie-a1/04-inventory/Arkologie-inventar.md` | `Arkologie-inventar.md` -> `00-admin/Warenueberblick-T0.md` | Matrix, `Warenueberblick-T0.md`, `Arkologie-inventar.md` |
| rahmenwert | externe Stationen tbd | Schienenbund | Schienenbund bleibt als logistischer Reparatur- und Baukontext gerahmt; Mengen und stationsscharfe Reserven bleiben offen. | `novapolis-rp/database-rp/01-factions/schienenbund/04-inventory/Schienenbund-inventar.md` | `Schienenbund-inventar.md` -> `00-admin/Warenueberblick-T0.md` | Matrix, `Warenueberblick-T0.md`, `Schienenbund-inventar.md` |
| rahmenwert | externe Stationen tbd | Haendlerbund | Haendlerbund bleibt als Umlauf- und Versorgungsraum gerahmt; harte Lagerzahlen werden nicht gesetzt. | `novapolis-rp/database-rp/01-factions/haendlerbund/04-inventory/Haendlerbund-inventar.md` | `Haendlerbund-inventar.md` -> `00-admin/Warenueberblick-T0.md` | Matrix, `Warenueberblick-T0.md`, `Haendlerbund-inventar.md` |
| rahmenwert | externe Stationen tbd | Eisenkonklave | Eisenkonklave bleibt als Werkstoff- und Schutzgueterrahmen lesbar; konkrete Rohstoff- oder Waffenmengen bleiben offen. | `novapolis-rp/database-rp/01-factions/eisenkonklave/04-inventory/Eiserne-Enklave-inventar.md` | `Eiserne-Enklave-inventar.md` -> `00-admin/Warenueberblick-T0.md` | Matrix, `Warenueberblick-T0.md`, `Eiserne-Enklave-inventar.md` |
| rahmenwert | externe Stationen tbd | Schattenbund | Schattenbund bleibt als opportunistischer Schmuggel- und Tarnraum gerahmt; konkrete Ware und Lagerstaende bleiben offen. | `novapolis-rp/database-rp/01-factions/schattenbund/04-inventory/Schattenbund-inventar.md` | `Schattenbund-inventar.md` -> `00-admin/Warenueberblick-T0.md` | Matrix, `Warenueberblick-T0.md`, `Schattenbund-inventar.md` |
| rahmenwert | externe Stationen tbd | Fluesterkollektiv | Fluesterkollektiv bleibt als Informations- und Spezialgueterraum gerahmt; konkrete Verbrauchsmengen und Technikposten bleiben offen. | `novapolis-rp/database-rp/01-factions/fluesterkollektiv/04-inventory/Fluesterkollektiv-inventar.md` | `Fluesterkollektiv-inventar.md` -> `00-admin/Warenueberblick-T0.md` | Matrix, `Warenueberblick-T0.md`, `Fluesterkollektiv-inventar.md` |

Handentscheidungen
------------------

| Status | Station / Zielraum | Fraktion | Offener Entscheid | Zielpfad | Naechster belegter Schritt | Kernquellen |
| --- | --- | --- | --- | --- | --- | --- |
| handentscheidung | D5 | Novapolis | Aktuelle D5-Restmengen pro Item bleiben `tbd`, bis eine echte Entnahme- oder Verbrauchszeile vorliegt. | `novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md` | Transferkette `Entnahme -> Transport -> Ankunft -> Quittung` belegen | Matrix, `D5-inventar.md`, `rp-inventory-backfill-pilot-2026-03-20.md` |
| handentscheidung | C6 | Novapolis | Restmengen, Charge und konkrete Lagerzuordnung in C6 bleiben `tbd`, bis eine Zielbuchung in Schleuse oder Lagerhalle vorliegt. | `novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md` | Zielbuchung / Inventarlog-Eintrag fuer C6 belegen | Matrix, `C6-inventar.md`, `rp-inventory-backfill-pilot-2026-03-20.md` |
| handentscheidung | D5 -> C6 | Novapolis | Konkrete Transfermengen, Quellabgang, Quittung und verantwortliche Person bleiben `tbd`. | `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Missionslog-Novapolis.md` | Missionslog plus D5-/C6-Inventare mit derselben Transferzeile schliessen | Matrix, `Missionslog-Novapolis.md`, `todo.rp.md` |
| handentscheidung | D5/C6 fraktionsweit | Novapolis | Der standortscharfe Split des Verbrauchsdeltas Tag 12 -> 13 bleibt `tbd`, bis D5 und C6 getrennte Belegzeilen fuehren. | `novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md` | `Novapolis-inventar.md` auf Delta-/Bilanzformat umstellen | Matrix, `Novapolis-inventar.md`, `todo.rp.md` |
| handentscheidung | externe Stationen tbd | alle externen Fraktionen | Exakte Mengen, stationsscharfe Lageranteile und mehrtaegige Verbrauchsreihen bleiben durchgehend `tbd`. | `novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md` | Fraktionsinventare nur bei neuer Belegkette quantifizieren | Matrix, `Warenueberblick-T0.md` |
| handentscheidung | Metro gesamt | Metro | Neutrale Stationslager und eine weltweite Gesamtmenge bleiben `tbd`; das Arbeitsledger setzt hier bewusst keinen stillen Summenwert. | `novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md` | Erst nach belastbaren Fraktionspfaden wieder auf Metro-Ebene verdichten | Matrix, `Metrokarte-T0.md`, `Stationskontroll-Matrix.md`, `Warenueberblick-T0.md` |

Updatekette fuer den naechsten Lauf
----------------------------------

1. `D5-inventar.md`: nur belegte `fix`- und `rahmenwert`-Rahmen ohne neue Mengen fortschreiben.
2. `C6-inventar.md`: nur belegte `fix`- und `rahmenwert`-Rahmen ohne freie Lagerzuordnung fortschreiben.
3. `Missionslog-Novapolis.md`: die offene Transferkette nur dann schliessen, wenn Quellabgang, Zielbuchung und Quittung dieselbe Beleglage tragen.
4. `Novapolis-inventar.md`: auf Delta-/Bilanzformat umstellen und die `fix`-Verbrauchsdeltas strukturiert statt nur narrativ fuehren.
5. Externe Fraktionsinventare: nur `rahmenwert`-Rahmen bestaetigen; keine neue Mengensetzung ohne fraktionsscharfe Evidenz.

Nicht-Ziele
-----------

- Keine Retcon von Restmengen fuer D5, C6 oder externe Fraktionen.
- Keine Normalisierung von Novapolis zu einer etablierten Metro-Handelsfraktion.
- Keine stillen Summen fuer Metro-Gesamtlager, neutrale Stationen oder den Ruecklauf `C6 -> D5`.
