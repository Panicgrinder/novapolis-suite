---
stand: 2026-04-27 02:30
update: C6-Inventar fuehrt jetzt zusaetzlich die konservative Betriebskorridor-Lesart T0 fuer den Aussenposten C6 innerhalb des D5-C6-Kernraums.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_022916.md
title: Inventar - C6
last_updated: 2026-04-27T02:24:00+02:00
category: inventory
slug: c6-inventar
owner: novapolis
scope: location
location: c6
version: "0.1"
tags: []
---

<!-- markdownlint-disable MD025 -->

C6 - Inventar
=============

Policy
------
- Inventare bleiben getrennt; Transfers nur via Mission/Logistik.
- Buchungen mit Quelle/Ziel in [Logistik](../../../00-admin/Logistik.md) dokumentieren.

Betriebskorridor T0
-------------------

- Das konservative Betriebsmodell fuehrt `C6` als teilaktiven Aussenposten innerhalb desselben Novapolis-Blocks, nicht als zweiten voll stabilen Kern; siehe [novapolis-betriebsmodell-t0](../00-doctrine/novapolis-betriebsmodell-t0.md) und [novapolis-nahraum-t0](../00-doctrine/novapolis-nahraum-t0.md).
- Inventarseitig folgt daraus: C6 bleibt der Verbrauchs-, Staging- und Druckschwerpunkt des Fraktionsraums, waehrend D5 die stabilere Quell- und Rueckhalteseite des Korridors bildet.

Bestände (lokal belegt, ohne Stückzahlen)
-----------------------------------------
- Filter - im C6-Expeditions-/Stationskontext wiederholt belegt; Typ und Menge tbd
- Energiezellen - im C6-Expeditions-/Stationskontext wiederholt belegt; Menge tbd
- Werkzeuge - im C6-Expeditions-/Stationskontext wiederholt belegt; Typen/Menge tbd
- Energiefluss C6 (Tag 12 -> 13) ist als Bilanz belegt: `+10 Zufuhr aus D5` bei `+12 Verbrauch`; absolute Speicherstaende bleiben `tbd`.

Startsnapshot C6 (2025-10-16, belegte Stückzahlen)
--------------------------------------------------
- Luftfilter `3`
- Ersatzrohre `12`
- Kabelspulen `6`
- Schmieroel `5`
- Strommodule `2`
- Wasserkanister `4`
- Werkzeugsets `2`
- Sensorpaket `1`
- Rationen `9`
- Wasserflaschen `10`
- Schutzanzuege `2`
- Ersatzmasken `3`
- Ergänzende Werkzeugliste aus `inventar_c6_v2`: Wartungsschluessel `2`, Druckmesser `1`, Schweissgeraet `1`; der tragbare Datenkern bleibt als Objekt vor Ort, aber funktional/offen.

Evakuierungsmitnahme E3 (konservativer Sammelbestand, 2026-04-26)
-----------------------------------------------------------------

Hinweise

- Die 20 Evakuierten aus E3 bringen keinen vollwertigen Stationshaushalt mit, sondern tragbare Restgueter aus Flucht, Quarantaene und Erstversorgung.
- Der Sammelbestand ist absichtlich knapp modelliert: genug, um C6 etwas zu entlasten, aber nicht genug fuer einen entspannten Vollbetrieb.

| Item | Menge | Herkunft | Zustand / Qualitaet | Notiz |
| --- | --- | --- | --- | --- |
| Rationen | `16` | `evac_e3` | gemischt, teils verbrauchsnah | persoenlich getragen oder als Restpakete mitgefuehrt |
| Wasserflasche | `18` | `evac_e3` | gemischt | tragbare Reserve, kein Stationspuffer |
| Wasserkanister | `2` | `evac_e3` | benutzt | groessere Mitnahme nur in kleinem Umfang |
| Notdecke | `12` | `evac_e3` | gebraucht, funktionsfaehig | Schlaf- und Quarantaenehilfe |
| Wechselkleidung (Set) | `8 Sets` | `evac_e3` | gemischt | nicht fuer alle, aber fuer die haerteren Faelle |
| Hygienepaket (Basis) | `10 Sets` | `evac_e3` | gemischt | kleiner Hygienepuffer nach Quarantaene |
| Verbandmaterial (Set) | `2 Sets` | `evac_e3` | normal | portable Wundversorgung |
| Ersatzmaske | `2` | `evac_e3` | gebraucht, brauchbar | zusaetzliche Schutzreserve |
| Werkzeugkit | `1 Set` | `evac_e3` | improvisiert, stark genutzt | tragbares Werkzeug aus Flucht-/Arbeitskontext |
| Kochgeschirr (Set) | `3 Sets` | `evac_e3` | gemischt | Gruppenversorgung statt individueller Vollausstattung |

Aktueller Arbeitsbestand C6 (konservativ generiert, 2026-04-26)
----------------------------------------------------------------

Hinweise

- C6 bleibt teilaktiver Aussenposten mit 27 humanoiden Personen vor Ort; dadurch sind Versorgung, Hygiene und Medizin deutlich straffer als in D5.
- Der aktuelle Bestand fuehrt Alt-/Stationsgut und Evakuierungsmitnahme zusammen, bleibt aber bewusst knapp und priorisierungsbeduerftig.

| Item | Menge | Herkunft | Zustand / Qualitaet | Notiz |
| --- | --- | --- | --- | --- |
| Luftfilter (Gasmasken) | `3` | `legacy` | normal | harte Schutzreserve, nicht grosszuegig |
| Ersatzrohr | `10` | `legacy,current` | normal/alt gemischt | leichter Rueckgang durch laufende Arbeit |
| Kabelspule | `5` | `legacy,current` | normal | C6 fuehrt noch Montagepuffer |
| Schmieroel | `4` | `legacy,current` | teils angebrochen | Werkstattgut unter Druck |
| Strommodul | `2` | `legacy` | normal | keine breite Redundanz |
| Wasserkanister | `6` | `legacy,evac_e3` | `2` benutzt | operative Reserve, aber fuer 27 Personen knapp |
| Wasserflasche | `28` | `legacy,evac_e3` | gemischt | tragbarer Bestand fuer Schicht- und Evaklagen |
| Rationen | `25` | `legacy,evac_e3` | gemischt | fuer 27 Personen klar angespannt |
| Werkzeugkit | `3 Sets` | `legacy,evac_e3` | `1` improvisiert, `2` normal | arbeitsfaehig, aber nicht komfortabel |
| Wartungsschluessel | `2` | `legacy` | normal | stationsnahes Werkzeug |
| Druckmesser | `1` | `legacy` | normal | Messreserve ohne Backup |
| Schweissgeraet | `1` | `legacy` | werkbankgebunden, feldschwach | erklaert, warum operative Schweißausruestung weiter kritisch bleibt |
| Sensorpaket | `1 Set` | `legacy` | normal | Monitoringkern bleibt klein |
| Schutzanzug | `2` | `legacy` | normal | zu wenig fuer breite Einsatzfreigabe |
| Ersatzmaske | `5` | `legacy,evac_e3` | gebraucht/normal gemischt | kleine Atemschutzreserve |
| Medkit (Standard) | `1 Set` | `legacy,current` | normal | Ersthilfe vorhanden, aber keine Komfortreserve |
| Verbandmaterial (Set) | `3 Sets` | `legacy,evac_e3` | normal | verteilbar, aber endlich |
| Hygienepaket (Basis) | `10 Sets` | `evac_e3,current` | gemischt | druckempfindlicher Evakposten |
| Notdecke | `12` | `evac_e3,current` | gebraucht | Schlaf- und Quarantaenepuffer |
| Wechselkleidung (Set) | `8 Sets` | `evac_e3,current` | gemischt | nicht fuer alle integriert Vor-Ort |
| Kochgeschirr (Set) | `3 Sets` | `evac_e3,current` | gemischt | Gruppenbetrieb, keine Vollausstattung |

Verbrauchsrahmen C6 (konservativ, 2026-04-27)
---------------------------------------------

Hinweise

- Die Werte beschreiben den Druck auf direkt gefuehrte Reserve- und Einsatzgueter; sie ersetzen keine vollstaendige Lebensmittel- oder Wasseroekonomie.
- C6 steht unter Dauerlast aus `27` Humanoiden, Evakuierungsfolge und laufender Nordlinie-Unterstuetzung.

| Verbrauchslinse | Takt / Rhythmus | Konservativer Verbrauch | Druckbild |
| --- | --- | --- | --- |
| Basisbetrieb C6 | pro Tag | `8-12` Rationen aus Reserve-/Schnellverpflegung, `1-2` Wasserkanister plus `6-10` Wasserflaschen als mobile Reserve | der gelistete Bestand puffert nur kurz; C6 bleibt auf Priorisierung und Zuteilung angewiesen |
| Hygiene / Erstversorgung | pro Tag unter Normaldruck | `0-1` Hygienepaket, `0-1` Verbandmaterial-Set; bei Spannungs- oder Krankheitslage sofort mehr | Evak-/Schichtbetrieb zieht die kleinen Versorgungsposten schneller leer als D5 |
| Nordlinie-Unterstuetzung C6 | je aktivem Tunneltag | `0-1` Schmieroel, `0-1` Verbandmaterial-Set, optional `0-1` Ersatzmaske; episodisch `1-2` Ersatzrohre oder Kabelanschnitt fuer Baustellennaehe | C6 verbraucht weniger Baukernmaterial als D5, aber mehr Schutz-, Verschleiss- und Einsatzgut |

C6-Staging und Baustellenvorlauf (belegt, mengenoffen)
------------------------------------------------------

Hinweise

- Der belegte D5-Lauf endet zuerst in C6 und nicht direkt im Tunnel.
- Belastbar ist der Prozess `Eintreffen -> Bestandsaufnahme -> Empfangsbestaetigung -> spaeterer Baustellenabgang`; nicht belastbar sind konkrete Itemmengen je Stufe.

| Stufe | Ort | Gueterklassen | Mengenstand | Aussage |
| --- | --- | --- | --- | --- |
| C6-Empfang | C6-Schleuse / C6-Lagerhalle | `Bauteile`, `Werkzeuge`, `Versorgungsgueter` aus D5 | `tbd` | der Materiallauf kommt zuerst in C6 an; der Tunnel ist dabei nur Durchgang, nicht Zielort |
| Bestandsaufnahme / Staging | C6-Lagerkontext | `Bauteile`, `Werkzeuge`, `Versorgungsgueter` | `tbd` | Ware bleibt nach Ankunft zunaechst auf C6-Seite, bis Empfang und Sichtung erfolgt sind |
| Baustellenabgang | C6 -> C6-/Nordlinie-Baustellenumfeld | `Bauteile`, `Werkzeuge`, `Versorgungsgueter` | `tbd` | Weitergabe an die Baustellen erfolgt erst nach Personaleinteilung; Itemsplit und Zielcharge bleiben offen |

Arbeitslesart

- C6 ist mit dem aktuellen Bestand arbeitsfaehig, aber nicht komfortabel; jede Stoerung, Nachbelegung oder laengere Sperre kippt zuerst die Reservegueter.
- `DN60` und operative Schweißausruestung bleiben auch hier keine normale Verbrauchsfrage, sondern Projektblocker.

Potenziale
----------
- Hydrofilter-Behälter (Reserve) - Potenzial vorhanden, Einbindung offen
- Mechanik-Werkzeug (priorisiert, ohne Stückzahlen)
- Tunnelbaumaterial ist fuer Tag 12 -> 13 als gemeinsamer Verbrauch belegt, aber noch nicht standortscharf D5 oder C6 zugeordnet.

Fehlend / Offen
---------------
- Adapter/Fittings DN60 (kritisch)
- Schweißausrüstung (kritisch)
- Lagerplätze/Containerstruktur für C6-Inventar
- Item- und chargenscharfer Split des belegten C6-Stagings zwischen Schleuse, Lagerhalle und Baustellenabgang
- Bequeme Nahrungs-, Hygiene- und Maskenreserve fuer 27 Personen; C6 bleibt mit Evakbestand arbeitsfaehig, aber angespannt

Bewegungen (Log)
----------------
- 2026-01-16 [FACT?] Prioritätenliste für C6-Inventar benannt (Filter, Energiezellen, Adapter/Fittings DN60, Schweißausrüstung, Mechanik-Werkzeug; ohne Stückzahlen). Quelle: scene-2026-01-16-a.
- 2026-02-10 17:09 [FACT?] Artefakt 7A im C6-Kontext markiert; Details erst nach Inventarisierung. Quelle: scene-2025-10-27-d.
- 2026-02-10 17:09 [FACT?] Datenkern (tragbar) am Fundort C6 belassen; nicht aufgenommen. Quelle: scene-2025-10-27-x.
- 2026-03-20 06:28 [REVIEW] RAW/Staging bestaetigen C6 als lokalen Fundort fuer Filter, Energiezellen und Werkzeuge; keine belastbaren Stückzahlen, aber klare lokale Zuordnung.
- 2026-03-20 06:45 [FACT?] Tagesabschluss Tag 12 -> 13: C6 `+12 Verbrauch` bei `+10 Zufuhr aus D5` => `-2` Tagesbilanz; nur Flusslogik belegt, keine absolute Zellmenge. Quelle: `database-curated/staging/chat-export.normalized.txt`, [Logistik](../../../00-admin/Logistik.md).
- 2026-03-20 06:52 [FACT?] Tagesabschluss Tag 12 -> 13: Tunnelarbeiten verbrauchen fraktionsweit `1,3 t Baustoffe`, `120 m Schienenprofil`, `18 m² Betonplatten`; `2` Werkzeuge sind beschaedigt, geschaetzt reparabel. Der Verbrauchsort ist konservativ als C6-/Nordlinie-Baustellenumfeld lesbar; konkrete C6-Lager- oder Itemabbuchungen bleiben weiter `tbd`. Quelle: `database-curated/staging/chat-export.normalized.txt`, [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md).
- 2026-03-20 07:14 [FACT?] Startsnapshot 2025-10-16: `inventar_c6_v2` und `logistik_c6_v2` belegen für C6 konkrete Lager-/Frachtwerte (`Luftfilter(3)`, `Ersatzrohre(12)`, `Kabelspulen(6)`, `Schmieroel(5)`, `Strommodule(2)`, `Wasserkanister(4)`, `Werkzeugsets(2)`, `Sensorpaket(1)`, `Rationen(9)`, `Wasserflaschen(10)`, `Schutzanzuege(2)`, `Ersatzmasken(3)`), plus Werkzeugliste `Wartungsschluessel(2)`, `Druckmesser(1)`, `Schweissgeraet(1)`. Quelle: `database-curated/staging/RAW-canvas-2025-10-16T12-30-00-000Z.normalized.txt`, `database-curated/staging/RAW-canvas-2025-10-16T12-55-00-000Z.normalized.txt`.
- 2026-03-20 11:49 [REVIEW] Ein missionierter Zugang aus D5 nach C6 ist als Reparatur- und Versorgungslauf belegt. Belastbar sind Transportrichtung und Kontext; nicht belastbar sind Ankunftsmengen je Item, saubere Zielbuchungen in der C6-Lagerstruktur und Quittungen an Schleuse oder Lagerhalle. Quelle: `database-raw/99-exports/RAW-canvas-2025-10-16T13-05-00-000Z.txt`, `database-raw/99-exports/chat-export.txt`, [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md), [C6-Schleuse](../03-locations/C6-Schleuse.md), [C6-Lagerhalle](../03-locations/C6-Lagerhalle.md).
- 2026-03-31 08:46 [FACT?] Der Chat-RAW fuehrt die C6-Seite des Laufs jetzt explizit als `Eintreffen in C6`, `Bestandsaufnahme` und `Empfang der Ware muss bestaetigt werden`; anschliessend geht die Ware zusammen mit D5-Material an die Baustellen. Welche Charge in Primaer- oder Sekundaerlager landete, bleibt weiter `tbd`. Quelle: `database-raw/99-exports/chat-export.txt`, [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md), [C6-Lagerhalle](../03-locations/C6-Lagerhalle.md).
- 2026-04-26 22:31 [REVIEW] Der aktuelle C6-Arbeitsbestand wird jetzt konservativ aus Stationssnapshot, Evakuierungsmitnahme E3 und laufender Verbrauchslage modelliert. Ergebnis: arbeitsfaehig, aber fuer 27 Personen klar angespannt; `DN60` und operative Schweißausruestung bleiben kritisch. Quelle: [C6](../03-locations/C6.md), [Warenueberblick-T0](../../../00-admin/Warenueberblick-T0.md), [Verbindungstunnel-C6-E3](../03-locations/Verbindungstunnel-C6-E3.md).
- 2026-04-27 00:06 [REVIEW] C6 fuehrt jetzt einen konservativen Verbrauchsrahmen fuer Stationsbetrieb und Nordlinie-Unterstuetzung. Der groesste Druck sitzt auf schneller Verpflegung, tragbarem Wasser, Hygiene und kleinen Einsatzposten statt auf vollem Werkstattkern. Quelle: [C6](../03-locations/C6.md), [Nordlinie-01](../05-projects/Nordlinie-01.md), [Verbindungstunnel-C6-E3](../03-locations/Verbindungstunnel-C6-E3.md).
- 2026-04-27 00:51 [REVIEW] C6 fuehrt den belegten Materiallauf jetzt explizit als Empfang, Bestandsaufnahme und belegt-mengenoffenes Staging vor dem spaeteren Baustellenabgang. Der Rohbeleg trennt damit C6 als Zwischenlager von einem direkten Tunnelabwurf, ohne freie Itemmengen zu behaupten. Quelle: `database-raw/99-exports/chat-export.txt`, `database-curated/staging/chat-export-complete.normalized.txt`, [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md), [C6-Schleuse](../03-locations/C6-Schleuse.md), [C6-Lagerhalle](../03-locations/C6-Lagerhalle.md).

Delta zum Missionslog
---------------------

- Delta 1 (belegt): C6-Fund-/Sicherungsanker (Artefakt 7A, Datenkern am Fundort belassen) sind im Missionslog referenziert und im Inventar als offen markiert.
  - Quelle: [Missionslog-Novapolis - C6: Sicherung/Markierung (C6-N3) & Artefakt „7A“](../05-projects/Missionslog-Novapolis.md#c6-sicherungmarkierung-c6-n3--artefakt-7a), [scene-2025-10-27-d](../../../06-scenes/scene-2025-10-27-d.md), [scene-2025-10-27-x](../../../06-scenes/scene-2025-10-27-x.md)
- Delta 2 (belegt/offen): C6-Monitoring/Funk-Abschnitte sind als aktive Missionen geführt; daraus resultierende Material-/Transferdetails bleiben bis Belegzeile offen.
  - Quelle: [Missionslog-Novapolis - C6: Funk/Scan & Stationssuche](../05-projects/Missionslog-Novapolis.md#c6-funkscan--stationssuche), [Missionslog-Novapolis - Monitoring: C6-Überwachung](../05-projects/Missionslog-Novapolis.md#monitoring-c6-überwachung-auswertung)
- Delta 3 (belegt): RAW/Staging fuehren Filter, Energiezellen und Werkzeuge konsistent als C6-Expeditions- bzw. Stationskontext; fehlende Schweißausrüstung und Adapter DN60 bleiben Bedarf, nicht Bestand.
  - Quelle: `database-raw/99-exports/chat-export-complete.txt` (Inventar & Ressourcen), `database-curated/staging/chat-export (1).review.md`, [scene-2026-01-16-a](../../../06-scenes/scene-2026-01-16-a.md), [scene-2026-01-14-b](../../../06-scenes/scene-2026-01-14-b.md)
- Delta 4 (belegt): Der Energiepfad D5 -> C6 ist fuer Tag 12 -> 13 mit `+10` Transfer und `-2` Tagesbilanz auf C6-Seite belegt; belastbare Vor-/Nachher-Speicherstaende fehlen weiter.
  - Quelle: `database-curated/staging/chat-export.normalized.txt` (Tagesabrechnung Tag 12 -> 13), [Logistik](../../../00-admin/Logistik.md)
- Delta 5 (belegt/offen): Materialverbrauch und Werkzeugschaden des Tunnel-Tagesabschlusses sind jetzt konservativ als C6-/Nordlinie-Baustellenverbrauch lesbar; offen bleiben die konkrete C6-Lagerbuchung, der genaue Lagerplatz und jede Item-Menge.
  - Quelle: `database-curated/staging/chat-export.normalized.txt` (Materialverbrauch / Werkzeuginspektion Tag 12 -> 13), [Missionslog-Novapolis - D5 -> C6: Materiallauf / Guetertransport](../05-projects/Missionslog-Novapolis.md#d5---c6-materiallauf--guetertransport)
- Delta 6 (belegt): Fuer C6 existiert ein frueher, quantifizierter Bestandssnapshot; er taugt als Startanker fuer lokale Restmengen, aber nicht als aktueller Fraktionsgesamtstand ohne D5-Gegenbeleg und spaetere Verbrauchs-/Transferkette.
  - Quelle: `database-curated/staging/RAW-canvas-2025-10-16T12-30-00-000Z.normalized.txt`, `database-curated/staging/RAW-canvas-2025-10-16T12-55-00-000Z.normalized.txt`, `database-curated/staging/RAW-canvas-2025-10-16T13-05-00-000Z.normalized.txt`
- Delta 7 (belegt/offen): Der Reparatur- und Versorgungslauf aus D5 nach C6 ist jetzt bis `Ankunft -> Bestandsaufnahme -> Empfangsbestaetigung` explizit belegt. Offen bleiben weiterhin konkrete Zielbuchung, Lagerzuordnung zwischen Primaer-/Sekundaerlager und jede Item-Menge.
  - Quelle: [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md), `database-raw/99-exports/chat-export.txt`, `database-raw/99-exports/RAW-canvas-2025-10-16T12-55-00-000Z.txt`, [C6-Schleuse](../03-locations/C6-Schleuse.md), [C6-Lagerhalle](../03-locations/C6-Lagerhalle.md)
- Delta 8 (review): C6 fuehrt jetzt einen konservativ generierten aktuellen Stationsbestand plus definierte Evakuierungsmitnahme aus E3. Der Stand soll C6 nicht leicht machen: Versorgung, Medizin und Schutz sind vorhanden, aber unter 27-Personen-Druck klar knapp.
  - Quelle: [C6](../03-locations/C6.md), [Verbindungstunnel-C6-E3](../03-locations/Verbindungstunnel-C6-E3.md), [Warenueberblick-T0](../../../00-admin/Warenueberblick-T0.md)
- Delta 9 (review): C6 fuehrt jetzt einen operativen Verbrauchsrahmen fuer Stationsbetrieb und Nordlinie-Unterstuetzung; damit ist der Druck auf Reserveverpflegung, Wasser und Hygieneposten erstmals stationsscharf lesbar.
  - Quelle: [C6](../03-locations/C6.md), [Nordlinie-01](../05-projects/Nordlinie-01.md)
- Delta 10 (belegt/review): C6 fuehrt jetzt den belegten Zwischenpfad `Empfang -> Bestandsaufnahme -> Staging -> Baustellenabgang` explizit, ohne ihn mit freier Item- oder Mengenpraezision zu ueberziehen.
  - Quelle: [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md), [C6-Schleuse](../03-locations/C6-Schleuse.md), [C6-Lagerhalle](../03-locations/C6-Lagerhalle.md)

Aktionen
--------
- [ ] Lagerplätze/Container definieren
- [ ] Verbrauchslog anlegen
