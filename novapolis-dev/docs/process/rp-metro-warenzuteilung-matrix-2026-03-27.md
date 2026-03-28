---
stand: 2026-03-28 06:53
update: Zuteilungsmatrix erneut geprueft, jetzt fraktionsscharf fuer alle aktiven Fraktionen und mit Novapolis als ausdruecklich nicht etablierter Sonderlage.
checks: markdownlint PASS; frontmatter PASS; todo-index PASS; logs-policy PASS (2026-03-27 16:22)
---

RP-Matrix: Operative Warenzuteilung Metro (2026-03-27)
======================================================

Ziel
----

- Die finale Handverteilung soll nur noch auf einer verdichteten Arbeitsbasis laufen.
- Die Matrix trennt deshalb strikt zwischen `hart gesetzt`, `konservativ geschaetzt` und `manuell zu entscheiden`.

Guardrails
----------

- Keine Mengenretcons ohne belegte Item-Kette `Entnahme -> Transport -> Ankunft -> Quittung`.
- `tbd` bleibt sichtbar, wenn ein Wert nur ueber Richtung, Prozess oder Stationskontext gestuetzt ist.
- Novapolis wird gesondert behandelt: lokale Kernfraktion ja, aber keine etablierte Metro-Hauptfraktion mit normalisiertem Handels- oder Lagernetz.
- Fuer etablierte oder extern verankerte Fraktionen gelten primar T0-Bandbreiten, Rollenbilder und die jeweils vorhandenen Inventarrahmen, keine stillen Mengenannahmen.

Arbeitsregel fuer die finale Zuteilung
-------------------------------------

1. Zuerst alle `hart gesetzt`-Posten als unverrueckbaren Sockel uebernehmen.
2. `Konservativ geschaetzt` nur dort verwenden, wo die Verteilung ohne Zusatzannahmen als Rahmenwert formuliert werden kann.
3. Alles unter `manuell zu entscheiden` bleibt Handarbeit und muss im Ergebnis weiter als Entscheidung kenntlich bleiben.

Operative Zuteilungsmatrix
--------------------------

| Bereich | Hart gesetzt | Konservativ geschaetzt | Manuell zu entscheiden | Kernquellen |
| --- | --- | --- | --- | --- |
| Metro-Rahmen | Novapolis kontrolliert `D5` aktiv, `C6` teilaktiv, `E3` historisch/evakuiert; der Pfad `D5 <-> C6` ist als aktiver Tunnelabschnitt gesetzt. | Die Verbindung taugt als operativer Hauptkorridor fuer Novapolis-Transfer und Baustellenversorgung. | Metro-weite Gesamtmengen, neutrale Stationslager und fraktionsuebergreifende Weltgesamtsumme. | `Metrokarte-T0.md`, `Stationskontroll-Matrix.md` |
| Novapolis (nicht etabliert) | `Novapolis` ist in der aktiven Taxonomie als lokale Kernfraktion gefuehrt; T0-seitig sind Energie, Wasser und Werkzeuge verfuegbar, D5/C6 bleiben aber ausdruecklich fruehe Aufbauphase ohne implizite Handelsnormalisierung. | Novapolis kann nur als junges lokales Versorgungsnetz mit knappen Puffern gelesen werden, nicht als normalisierte Metro-Handelsfraktion. | Jede Ableitung eines etablierten Markts, belastbare Fraktionssummen ausserhalb der D5-/C6-Belege und jede Handelsnormalisierung ueber D5/C6 hinaus. | `Fraktionen-Taxonomie.md`, `Warenueberblick-T0.md` |
| D5-Startanker | `Union-Kisten (3)`, leere Filterkartuschen, Ersatzrohre/Ventilkomponenten, defekte Reparaturstation, `60 %` lesbare Schaltplaene. Energiepfad Tag 12 -> 13 als `+10 Produktion - 8 Eigenverbrauch - 12 Export = -10` belegt. | D5 ist belastbar als Quellstation fuer Wartung, Energie und schwere Reparaturgueter gerahmt. | Aktuelle D5-Restmengen, saubere Abgaenge einzelner Posten und jede nachtraegliche Umlagerung nach C6. | `D5-inventar.md`, `RAW-canvas-2025-10-16T12-00-00-000Z.normalized.txt` |
| C6-Startanker | Belegt sind `Luftfilter 3`, `Ersatzrohre 12`, `Kabelspulen 6`, `Schmieroel 5`, `Strommodule 2`, `Wasserkanister 4`, `Werkzeugsets 2`, `Sensorpaket 1`, `Rationen 9`, `Wasserflaschen 10`, `Schutzanzuege 2`, `Ersatzmasken 3` sowie lokale Werkzeugposten. Energiepfad Tag 12 -> 13 als `+10 Zufuhr` bei `+12 Verbrauch` belegt. | C6 ist belastbar als knapper, aber bereits quantifizierter Reparatur- und Empfangsknoten lesbar. | Aktuelle Restmengen nach Verbrauch, Einlagerungsorte pro Posten und jeder spaetere Zielabgleich in Schleuse/Lagerhalle. | `C6-inventar.md`, `RAW-canvas-2025-10-16T12-30-00-000Z.normalized.txt`, `RAW-canvas-2025-10-16T12-55-00-000Z.normalized.txt` |
| Novapolis Tagesdeltas | Fraktionsweit sind fuer Tag 12 -> 13 `1,3 t Baustoffe`, `120 m Schienenprofil`, `18 m2 Betonplatten` und `2` beschaedigte Werkzeuge als Verbrauch/Schaden belegt. | Das Delta taugt als harter Verbrauchsanker fuer die Handverteilung, auch wenn die Standortaufteilung offen bleibt. | Restbestandszahlen nach dem Tagesabschluss und die standortscharfe Abbuchung D5 vs. C6. | `Novapolis-inventar.md`, `chat-export.normalized.txt` |
| Versorgungslauf `D5 -> C6` | Der Lauf ist als Missionsvorgang und als generische aktive Fracht fuer `Bauteile`, `Werkzeuge` und `Versorgungsgueter` belegt. Prozessanker fuer `Abmeldung`, `Ankunft`, `Bestandsaufnahme` und bestaetigten Empfang liegen vor. | Konservativ definierbar ist ein missionierter Versorgungslauf mit Empfang in C6 und anschliessender Baustellenverteilung. | Item-Mengen, Charge, Quellabgang, Zielbuchung, Quittung und verantwortliche Person. | `Missionslog-Novapolis.md`, `RAW-canvas-2025-10-16T13-05-00-000Z.txt`, `chat-export.txt` |
| D5-Quellorte des Laufs | Das `Materiallager unter dem Bahnsteig` und der D5-Werkstattkontext sind als physischer Herkunftsrahmen belegt. | Der Lauf kann ohne Retcon als `D5-Materiallager und/oder Werkstattbestand` gerahmt werden. | Welche konkreten Items aus welchem Quellort entnommen wurden. | `rp-inventory-backfill-pilot-2026-03-20.md`, `D5-inventar.md` |
| C6-Zielseite des Laufs | Primaer-/Sekundaerlager sind als Systemrahmen benannt; Empfang und nachgelagerte Baustellenverteilung sind im RAW explizit gestuetzt. | Der Lauf endet plausibel in bestaetigtem Empfang plus operativer Verteilung statt in freier Umlagerung. | Welche Charge in welchem Lager landete und was direkt an die Baustelle ging. | `C6-inventar.md`, `rp-inventory-backfill-pilot-2026-03-20.md` |
| Novapolis Fraktionsaggregat | `Kugeln` bleiben Fraktions-Items, aber mengenoffen; die Fraktionslage fuehrt harte Energie- und Verbrauchsdeltas, keine harten Restbestaende. | Das Aggregat taugt als Bilanz- und Risikoebene, nicht als fertiges Lagerbuch. | Aktuelle Fraktionssummen, mehrtaegige Verbrauchsreihen, belastbare Transfermengen pro Lauf. | `Novapolis-inventar.md` |
| Arkologie-A1 (etabliert/external) | T0-Warenbild: Grundversorgung stabil, Austauschgueter selektiv; Inventarrahmen fuehrt `Kugeln`, Handelsgueter und Ersatzteile, aber ohne Mengen. | Als etablierter externer Block plausibel mit stabiler Basisversorgung, aber ohne harte Stations- oder Fraktionsmengen im aktiven Inventar. | Jede konkrete Warenmenge, interne Lagerquote und jeder stationsscharfe Abzug/Zugang. | `Warenueberblick-T0.md`, `Arkologie-inventar.md`, `Fraktionen-Taxonomie.md` |
| Schienenbund (etabliert/external) | T0-Warenbild: Logistik-/Reparaturfokus; Inventarrahmen fuehrt `Kugeln`, Schienen-/Baukomponenten und Werkzeuge, aber ohne Mengen. | Als etablierter Infrastrukturfokus ist ein robuster Reparatur- und Baukontext plausibel, nicht aber ein harter Lagerstand. | Konkrete Baukomponenten-Mengen, stationsscharfe Werkstattreserven und echte Verbrauchsbilanzen. | `Warenueberblick-T0.md`, `Schienenbund-inventar.md`, `Fraktionen-Taxonomie.md` |
| Haendlerbund (etabliert/external) | T0-Warenbild: Umlaufgueter verfuegbar, stationaere Reserven variabel; Inventarrahmen fuehrt `Kugeln`, Handelswaren und Ersatzteile/Werkzeug, aber ohne Mengen. | Als etabliertes Handelsnetz kann der Haendlerbund als Versorgungs- und Umlaufraum gelesen werden, nicht als quantifiziertes Festlager. | Konkrete Umlaufmengen, stationaere Reserven und belastbare Bestandsketten je Station. | `Warenueberblick-T0.md`, `Haendlerbund-inventar.md`, `Fraktionen-Taxonomie.md` |
| Eiserne Enklave / Eisenkonklave (etabliert/external) | T0-Warenbild: Werkstoff-/Instandsetzungsgueter verfuegbar, Verbrauchsgueter variabel; Inventarrahmen fuehrt `Kugeln`, Waffen/Schutzausruestung und Rohstoffe, aber ohne Mengen. | Als etablierter Machtblock ist ein belastbarer Werkstoff- und Schutzguerterahmen plausibel, nicht aber ein quantifiziertes Gesamtlager. | Konkrete Rohstoffmengen, Waffen-/Ruestungsbestaende und stationsscharfe Lageranteile. | `Warenueberblick-T0.md`, `Eiserne-Enklave-inventar.md`, `Fraktionen-Taxonomie.md` |
| Schattenbund (etabliert im T0-Lagebild) | T0-Warenbild: Versorgung uneinheitlich; Inventarrahmen fuehrt `Kugeln`, Schmuggelware, leise/kompakte Werkzeuge und Tarnmaterial als variable Klassen. | Fuer die Verteilung nur als opportunistischer Beschaffungs- und Abschirmraum lesbar, nicht als hartes Mengendepot. | Jede konkrete Ware, jede Quotierung zwischen Schmuggel/Tarnung/Werkzeug und jeder belastbare Lagerstand. | `Warenueberblick-T0.md`, `Schattenbund-inventar.md` |
| Fluesterkollektiv (etabliert im T0-Lagebild) | T0-Warenbild: Lagerbild nur teilweise belastbar; Inventarrahmen fuehrt `Kugeln`, Informationsgueter, Tarn-/Signaltechnik und Verbrauchsmaterial als variable Klassen. | Fuer die Verteilung nur als Informations- und Spezialgueterraum lesbar, nicht als harter Sachgutbestand. | Jede konkrete Menge an Verbrauchsmaterial, Technik oder tauschbarem Spezialgut. | `Warenueberblick-T0.md`, `Fluesterkollektiv-inventar.md` |

Operative Ableitung fuer die finale Handverteilung
-------------------------------------------------

- Direkt verteilbar ohne neue Annahmen: C6-Startsnapshot, D5-Startanker, Novapolis-Tagesdeltas, Metro-Kontrollrahmen und die explizit belegten Novapolis-Prozessanker.
- Nur als konservativer Rahmen verteilbar: Novapolis selbst als nicht etablierte Fraktion, Versorgungslauf `D5 -> C6`, D5-Quellorte, C6-Zielseite sowie die T0-Warenbilder und Inventarklassen der einzelnen etablierten Fraktionen.
- Explizit als Handentscheidung offen lassen: aktuelle Fraktionssummen, konkrete Transfermengen, Restbestaende je Station, mehrtaegige Verbrauchsreihen und alle exakten Mengen aller externen Fraktionen.

Naechster Arbeitsschritt
------------------------

- Auf Basis dieser Matrix kann die finale Warenzuteilung direkt als Dreiteilung laufen: `fix uebernehmen`, `konservativ setzen`, `manuell entscheiden`.
- Sobald die echte Zuteilung geschrieben wird, sollten nur die Posten aus der dritten Spalte neue sichtbare Entscheidungen erzeugen.