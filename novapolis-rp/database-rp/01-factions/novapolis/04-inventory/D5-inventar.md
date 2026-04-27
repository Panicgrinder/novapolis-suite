---
stand: 2026-04-27 02:30
update: D5-Inventar fuehrt jetzt zusaetzlich die konservative Betriebskorridor-Lesart T0 fuer D5 als Kernbasis und C6 als Aussenposten.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_022916.md
title: Inventar - D5
last_updated: 2026-04-27T02:24:00+02:00
category: inventory
slug: d5-inventar
owner: novapolis
scope: location
location: d5
version: "0.1"
tags: []
---

<!-- markdownlint-disable MD025 -->

D5 - Inventar
=============

Policy
------
- Inventare bleiben getrennt; Transfers nur via Mission/Logistik.
- Buchungen mit Quelle/Ziel in [Logistik](../../../00-admin/Logistik.md) dokumentieren.

Betriebskorridor T0
-------------------

- Das konservative Betriebsmodell fuehrt `D5` als Kernbasis und `C6` als teilaktiven Aussenposten desselben Novapolis-Blocks; siehe [novapolis-betriebsmodell-t0](../00-doctrine/novapolis-betriebsmodell-t0.md) und [novapolis-nahraum-t0](../00-doctrine/novapolis-nahraum-t0.md).
- Inventarseitig folgt daraus: D5 traegt den belastbaren Fraktionssockel fuer Basisbetrieb, Werkstatt und Ausgaenge in den Korridor, aber nicht automatisch den gesamten Aussenpostenverbrauch von C6.

Bestände (verbucht)
-------------------
- Keine separat belastbar verbuchten D5-Bestaende aus der C6-Expedition.
- Lokaler D5-Werkzeug-/Wartungskontext ist belegt, aber ohne saubere Bestandszeile oder belastbare Mengenangabe noch nicht als eigener Item-Posten kanonisiert.
- Energiefluss D5 (Tag 12 -> 13) ist als Bilanz belegt: `+10 Produktion`, `-8 Grundlast`, `-12 Export nach C6`; absolute Speicherstaende bleiben `tbd`.

Startsnapshot D5 (2025-10-16, teilquantifizierter Stationsanker)
-----------------------------------------------------------------
- Union-Kisten mit Ersatzteilen `3`
- Alte Filterkartuschen (leer)
- Ersatzrohre und Ventilkomponenten - belegt, Menge `tbd`
- Reparaturstation - defekt, planmaessig zu reaktivieren
- Schaltplaene und technische Dokumentation - Fragment `60 %` lesbar

Aktueller Arbeitsbestand D5 (konservativ generiert, 2026-04-26)
----------------------------------------------------------------

Hinweise

- D5 wird als von innen geoeffneter, lange verriegelter Kernstandort gelesen; daraus folgt relativ intakter Altbestand bei geringer Handelsdurchmischung.
- Der Bestand ist ausgewogen, aber absichtlich nicht grosszuegig: genug fuer Betrieb, Reparaturvorbereitung und kleine Reserven, nicht genug fuer freie Materialentspannung.
- `Schweißausrüstung` und `Adapter DN60` bleiben trotz des Bestands weiter offener Mangel.

Stations- und Werkstattgut

| Item | Menge | Herkunft | Zustand / Qualitaet | Notiz |
| --- | --- | --- | --- | --- |
| Union-Ersatzteilkiste | `3` | `legacy` | `2` teilversiegelt, `1` angebrochen | D5 fuehrt weiter echten Altbestand statt improvisierter Streuware |
| Ersatzrohr | `10` | `legacy` | normal/alt gemischt | fuer Wartung und Leitungsflicken, nicht fuer grossen Ausbau |
| Ventilkomponente | `12` | `legacy` | normal/alt gemischt | Armaturenreserve fuer lokale Instandhaltung |
| Kabelspule | `3` | `legacy` | `2` normal, `1` alt | knapper Elektro-/Datenpuffer |
| Schaltplaene & technische Doku | `1 Set` | `legacy` | ca. `60 %` lesbar | stark nuetzlich, aber nicht vollstaendig |
| Werkzeugkit | `2 Sets` | `legacy,current` | `1` mobil, `1` Werkbank | Kernbestand fuer Ronja/Jonas |
| Werkzeugsatz (Mechanik) | `1 Set` | `legacy,current` | stark genutzt | Werkstattkern, keine Duplikatreserve |
| Multimeter | `1` | `legacy` | normal | Elektronikdiagnose knapp, aber vorhanden |
| Wartungsschluessel | `2` | `legacy` | normal | typische Stationsarbeit |
| Druckmesser | `1` | `legacy` | alt, funktionsfaehig | Messreserve ohne Redundanz |
| Hydrofilter-Behälter (Reserve) | `1` | `legacy` | ungeprueft | Reservekomponente, noch nicht eingebunden |
| Sicherungssatz | `3 Sets` | `legacy` | normal | aktueller verfuegbarer Rest nach Draisine-Werkstattbindung |
| Dichtungsmanschette | `5` | `legacy` | alt/normal gemischt | aktueller verfuegbarer Rest nach Draisine-Werkstattbindung |
| Schmieroel | `3` | `legacy` | `1` angebrochen, `2` normal | aktueller verfuegbarer Rest nach Draisine-Werkstattbindung |
| Lagerfett (Technik) | `2` | `legacy` | normal | aktueller verfuegbarer Rest nach Draisine-Werkstattbindung |

Nordlinie-Stuetzbaukasten

| Item | Menge | Herkunft | Zustand / Qualitaet | Notiz |
| --- | --- | --- | --- | --- |
| Metallprofil (lang) | `4` | `legacy,scavenged` | `2` alt, `2` normal | fuer groessere Spannweiten; keine breite Reserve |
| Metallprofil (mittel) | `8` | `legacy,scavenged` | Rest aus `4` alt, `3` normal, `1` neuwertig | aktueller D5-Rest nach kleinem Turn-7-Abgang |
| Metallprofil (kurz) | `12` | `legacy,scavenged` | Rest aus `5` alt, `5` normal, `2` neuwertig | aktueller D5-Rest nach kleinem Turn-7-Abgang |
| Stuetzklemme | `8` | `legacy` | alt/normal gemischt | aktueller D5-Rest nach kleinem Turn-7-Abgang |
| Lasche / Knotenblech | `8` | `legacy` | normal | aktueller D5-Rest nach kleinem Turn-7-Abgang |
| Ausgleichsplatte | `6` | `legacy,scavenged` | alt/normal gemischt | aktueller D5-Rest nach kleinem Turn-7-Abgang |
| Schraubensatz (mittel) | `10 Sets` | `legacy` | normal | aktueller D5-Rest nach kleinem Turn-7-Abgang |
| Bolzen-Mutter-Satz (stark) | `7 Sets` | `legacy` | `4` normal, `3` neuwertig | aktueller D5-Rest nach kleinem Turn-7-Abgang |
| Klebmasse (schwach) | `3 Kartuschen` | `legacy` | `1` normal, `2` fraglich alt | aktueller D5-Rest nach kleinem Turn-7-Abgang |

Projektbuchungen D5 (konservativ, 2026-04-27)
----------------------------------------------

Nordlinie 01 - kleiner Turn-7-Abgang

| Klasse | D5 vor Abgang | Turn-7-Abgang | im Tunnel eingesetzt | Tunnelrest vor Ort | D5-Rest |
| --- | --- | --- | --- | --- | --- |
| Metallprofil (lang) | `4` | `0` | `0` | `0` | `4` |
| Metallprofil (mittel) | `10` | `2` | `2` | `0` | `8` |
| Metallprofil (kurz) | `16` | `4` | `3` | `1` | `12` |
| Stuetzklemme | `12` | `4` | `4` | `0` | `8` |
| Lasche / Knotenblech | `10` | `2` | `2` | `0` | `8` |
| Ausgleichsplatte | `8` | `2` | `1` | `1` | `6` |
| Schraubensatz (mittel) | `14 Sets` | `4 Sets` | `3 Sets` | `1 Set` | `10 Sets` |
| Bolzen-Mutter-Satz (stark) | `8 Sets` | `1 Set` | `1 Set` | `0` | `7 Sets` |
| Klebmasse (schwach) | `4 Kartuschen` | `1 Kartusche` | `1 Kartusche` | `0` | `3 Kartuschen` |

Draisine-Transportmodul - aktuelle Werkstattbindung

| Posten | D5 vor Bindung | im Prototyp gebunden | verfuegbarer Rest |
| --- | --- | --- | --- |
| Schmieroel | `4` | `1` | `3` |
| Lagerfett (Technik) | `3` | `1` | `2` |
| Sicherungssatz | `4 Sets` | `1 Set` | `3 Sets` |
| Dichtungsmanschette | `6` | `1` | `5` |

Hinweise

- Die aktuellen D5-Tabellen fuehren bereits den verfuegbaren Rest nach diesen beiden Projektbuchungen.
- Der Draisine-Posten ist als Werkstattbindung, nicht als abgeschlossener Feldverbrauch zu lesen.

Versorgungs- und Basisgut

| Item | Menge | Herkunft | Zustand / Qualitaet | Notiz |
| --- | --- | --- | --- | --- |
| Rationen | `24` | `legacy,current` | gemischt, trocken | reicht fuer Kernteam, aber nicht fuer lockeren Mehrverbrauch |
| Wasserkanister | `6` | `legacy,current` | `2` angebrochen | stabiler D5-Puffer, nicht fuer Grossversorgung |
| Medkit (Standard) | `2 Sets` | `legacy,current` | normal | `1` Basis, `1` Reserve |
| Verbandmaterial (Set) | `4 Sets` | `legacy,current` | normal | fuer Werkstatt- und Tunnelverletzungen brauchbar |
| Desinfektionsmittel | `3` | `legacy,current` | normal | kleine Hygienereserve |

Verbrauchsrahmen D5 (konservativ, 2026-04-27)
---------------------------------------------

Hinweise

- Die Werte beschreiben operativen Druck auf den direkt gefuehrten Reservebestand, nicht die vollstaendige unsichtbare Stationsoekonomie.
- D5 bleibt beim Verbrauch deutlich stabiler als C6, steht aber unter Werkstatt- und Projektlast durch Nordlinie und Draisine.

| Verbrauchslinse | Takt / Rhythmus | Konservativer Verbrauch | Druckbild |
| --- | --- | --- | --- |
| Basisbetrieb D5 | pro Tag | `3-4` Rationenaequivalente, `1` Wasserkanister, geringe Hygiene-/Mednutzung | fuer `2-3` Humanoide arbeitsfaehig, aber ohne lockeren Puffer |
| Nordlinie 01 (D5-seitige Sicherungsarbeit) | je aktivem Sicherungsblock | `1-2` Metallprofile (`mittel/kurz`), `2-3` Stuetzklemmen, `1-2` Schraubensaetze, optional `0-1` Bolzen-Mutter-Satz und `0-1` Klebmasse | kleiner Stuetzbaukasten sinkt nicht taeglich, aber in jedem echten Sicherungszug spuerbar |
| Draisine-Transportmodul | je Werkstattblock | `0-1` Schmieroel, `0-1` Lagerfett, `0-1` Sicherungssatz; episodisch `0-1` Dichtungsmanschette oder Kabelanschnitt | Werkstattprojekt zieht wenig Volumen, aber konstant an knappen Technikposten |

Arbeitslesart

- Wenn Nordlinie und Draisine parallel Druck machen, bleibt D5 weiter funktionsfaehig, verliert aber zuerst Bequemlichkeit und dann Redundanz.
- `Schweißausrüstung` und `DN60` bleiben keine Verbrauchsposten, sondern harte Luecken im Projektpfad.

Potenziale
----------
- Werkzeug-/Wartungsmaterial aus D5-Kontext moeglich, aber derzeit nur als Umfeld- und Fundkontext belegt.
- Tunnelbaumaterial ist fuer Tag 12 -> 13 als gemeinsamer Verbrauch belegt, aber noch nicht standortscharf D5 oder C6 zugeordnet.
- Der Nordlinie-Bedarf `Stuetzelemente` ist ab jetzt als komponentenbasierter Stuetzbaukasten aus Profilen, Formteilen und Verbindungsmitteln zu lesen; siehe [Nordlinie-01-Stuetzbaukasten](../05-projects/Nordlinie-01-Stuetzbaukasten.md).

Fehlend / Offen
---------------
- Schweißausrüstung (D5-Priorität, aber nicht als lokaler Bestand belegt)
- Adapter / Fitting (DN60) (D5-Priorität, aber nicht als lokaler Bestand belegt)
- Qualitaetsstufenscharfer Vorzustand des kleinen Turn-7-Abgangs bleibt konservative Review-Buchung statt voll belegt chargenscharfer Lagerhistorie
- Folgeabgaenge und Ruecklaeufe nach dem kleinen Turn-7-Satz bleiben offen, bis weitere Runtime-Zuege belastbar gebucht sind
- Frische Handels- oder Komfortgueter ausserhalb des Kernbedarfs; D5 fuehrt eher verriegelten Altbestand als bequemen Marktbestand
- Saubere Trennung lokalem D5-Bestand vs. C6-Expeditionsgut im Wochenzyklus weiter nachziehen

Bewegungen (Log)
----------------
- 2026-02-10 17:09 [FACT?] Werkzeugtasche (Fundstueck) in D5 beobachtet; Ownership/Inhalt offen. Quelle: scene-2025-10-27-g.
- 2026-03-20 06:28 [REVIEW] Fruehere C6-Posten (`Filter`, `Energiezellen`, `Hydrofilter-Behälter`) aus D5 entfernt; RAW/Staging und `scene-2025-10-27-x` bestaetigen die Standorttrennung ohne impliziten Transfer.
- 2026-03-20 06:45 [FACT?] Tagesabschluss Tag 12 -> 13: D5 `+10 Produktion - 8 Eigenverbrauch - 12 Export` => `-10` Tagesbilanz; nur Flusslogik belegt, keine absolute Zellmenge. Quelle: `database-curated/staging/chat-export.normalized.txt`, [Logistik](../../../00-admin/Logistik.md).
- 2026-03-20 06:52 [FACT?] Tagesabschluss Tag 12 -> 13: Tunnelarbeiten verbrauchen fraktionsweit `1,3 t Baustoffe`, `120 m Schienenprofil`, `18 m² Betonplatten`; `2` Werkzeuge sind beschaedigt, geschaetzt reparabel. Der Verbrauchsort ist konservativ als C6-/Nordlinie-Baustellenumfeld lesbar; D5 bleibt Quell- und Transferseite ohne harte Materialabbuchung je Posten. Quelle: `database-curated/staging/chat-export.normalized.txt`, [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md).
- 2026-03-20 07:22 [FACT?] Startsnapshot 2025-10-16: D5 fuehrt im Basis-Canvas ein Stationsinventar mit `Union-Kisten (3)`, leeren Filterkartuschen, Ersatzrohren/Ventilkomponenten, defekter Reparaturstation und zu `60 %` lesbaren Schaltplaenen. Quelle: `database-curated/staging/RAW-canvas-2025-10-16T12-00-00-000Z.normalized.txt`.
- 2026-03-20 11:49 [REVIEW] Ein Materiallauf `D5 -> C6` fuer Reparatur- und Versorgungsgueter ist als Vorgang belegt. Belastbar sind Richtung und Zweck sowie generische Frachtarten wie `Bauteile`, `Werkzeuge` und `Versorgungsgueter`; nicht belastbar sind Entnahmemengen, konkrete D5-Abbuchungen und die spaetere Zielbuchung in C6. Quelle: `database-raw/99-exports/RAW-canvas-2025-10-16T13-05-00-000Z.txt`, `database-raw/99-exports/chat-export.txt`, [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md).
- 2026-03-31 08:46 [FACT?] Der Chat-RAW fuehrt den D5-Abgang jetzt explizit auf Prozessebene: `Ronja wird das notwendige einpacken` und das Material `zusammen mit Reflex Unterstuetzung zur Station bringen`; der RAW-Logistikcanvas stuetzt dazu `manuellerTransport` und `Tragegestell(ReflexAssist)`. Konkrete Item-Mengen und eine saubere D5-Abbuchung bleiben weiter `tbd`. Quelle: `database-raw/99-exports/RAW-chat-export-2025-10-27T09-16-00-188Z.txt`, `database-raw/99-exports/RAW-canvas-2025-10-16T13-05-00-000Z.txt`.
- 2026-04-26 22:07 [FACT?] Der Nordlinie-Bedarf `Stuetzelemente` wird im aktiven Projektkontext ab jetzt als komponentenbasierter Stuetzbaukasten gelesen statt als fertiger Lagerposten; belastbare Mengen je Klasse bleiben weiter offen. Quelle: [Nordlinie-01-Stuetzbaukasten](../05-projects/Nordlinie-01-Stuetzbaukasten.md), [Nordlinie-01](../05-projects/Nordlinie-01.md).
- 2026-04-26 22:31 [REVIEW] Der aktuelle D5-Arbeitsbestand wird jetzt konservativ aus verriegeltem Altbestand, laufender Basennutzung und geringer Handelsdurchmischung modelliert. Das Ergebnis ist absichtlich arbeitsfaehig, aber nicht komfortabel; `Schweißausrüstung` und `DN60` bleiben offen. Quelle: [D5](../03-locations/D5.md), [Warenueberblick-T0](../../../00-admin/Warenueberblick-T0.md), [Nordlinie-01-Stuetzbaukasten](../05-projects/Nordlinie-01-Stuetzbaukasten.md).
- 2026-04-27 00:06 [REVIEW] D5 fuehrt jetzt einen konservativen Verbrauchsrahmen fuer Basisbetrieb und beide offenen Projekte. Der Hauptdruck sitzt auf Rationen-/Wasserreserve moderat, auf Werkstatt- und Stuetzbaukastenposten aber kumulativ ueber Nordlinie plus Draisine. Quelle: [Nordlinie-01](../05-projects/Nordlinie-01.md), [Draisine-Transportmodul](../05-projects/Draisine-Transportmodul.md), [D5](../03-locations/D5.md).
- 2026-04-27 00:44 [REVIEW] Der kleine Nordlinie-Turn-7-Satz wird jetzt klassenweise aus D5 abgebucht und vom D5-Rest getrennt gefuehrt; zugleich ist fuer die Draisine ein kleiner Werkstattsatz als gebundener Prototypbestand aus D5 herausgezogen. Quelle: [Nordlinie-01](../05-projects/Nordlinie-01.md), [Draisine-Transportmodul](../05-projects/Draisine-Transportmodul.md), [Nordlinie-01-Stuetzbaukasten](../05-projects/Nordlinie-01-Stuetzbaukasten.md).

Delta zum Missionslog
---------------------

- Delta 1 (belegt): D5-Werkzeug-/Wartungskontext als Missionsanker vorhanden; Inventar-Ownership der Werkzeugtasche bleibt offen bis belastbare Zuordnung vorliegt.
  - Quelle: [Missionslog-Novapolis - D5: Wartungsauftrag & Wartungsgang](../05-projects/Missionslog-Novapolis.md#d5-wartungsauftrag--wartungsgang), [scene-2025-10-27-g](../../../06-scenes/scene-2025-10-27-g.md)
- Delta 2 (belegt/offen): Trennung D5↔C6 bleibt verbindlich; fuer den Materiallauf sind D5-Abmeldung, Verpacken in D5 und Transportfuehrung durch Ronja mit Reflex-Assist jetzt explizit belegt. Offen bleiben weiter Itemliste, Charge und die eigentliche Mengenabbuchung aus D5.
  - Quelle: [Missionslog-Novapolis - D5 -> C6: Materiallauf / Guetertransport](../05-projects/Missionslog-Novapolis.md#d5---c6-materiallauf--guetertransport), `database-raw/99-exports/RAW-chat-export-2025-10-27T09-16-00-188Z.txt`, `database-raw/99-exports/RAW-canvas-2025-10-16T13-05-00-000Z.txt`
- Delta 3 (belegt): Staging/RAW bestaetigen, dass die C6-Expeditionsgueter nicht stillschweigend im D5-Inventar landen duerfen.
  - Quelle: `database-raw/99-exports/chat-export-complete.txt` (Inventar & Ressourcen), `database-curated/staging/chat-export-complete.finalgate.md`, `database-curated/staging/chat-export (1).review.md`
- Delta 4 (belegt): Der D5-Reaktor-/Energiepfad bleibt lokal verankert; fuer Tag 12 -> 13 ist eine exportgetriebene Tagesbilanz `-10` belegt, ohne dass daraus ein absoluter Restbestand ableitbar waere.
  - Quelle: `database-curated/staging/chat-export.normalized.txt` (Tagesabrechnung Tag 12 -> 13), [Logistik](../../../00-admin/Logistik.md)
- Delta 5 (belegt/offen): Materialverbrauch und Werkzeugschaden des Tunnel-Tagesabschlusses sind jetzt konservativ als C6-/Nordlinie-Baustellenverbrauch lesbar; fuer D5 bleibt lediglich die Quell-/Transferseite belegt, waehrend die eigentliche D5-Abbuchung je Item weiter `tbd` ist.
  - Quelle: `database-curated/staging/chat-export.normalized.txt` (Materialverbrauch / Werkzeuginspektion Tag 12 -> 13), [Missionslog-Novapolis - D5 -> C6: Materiallauf / Guetertransport](../05-projects/Missionslog-Novapolis.md#d5---c6-materiallauf--guetertransport)
- Delta 6 (belegt): Fuer D5 existiert ein frueher Stationsanker mit teilquantifiziertem Basisinventar; er taugt fuer lokale Startwerte, aber nicht fuer aktuelle Restbestaende ohne spaetere Verbrauchs- und Transferkette.
  - Quelle: `database-curated/staging/RAW-canvas-2025-10-16T12-00-00-000Z.normalized.txt`, [D5](../03-locations/D5.md)
- Delta 7 (belegt/review): Der aktive Nordlinie-Bedarf `Stuetzelemente` ist jetzt als Stuetzbaukasten mit Profil-, Formteil- und Verbindungsklassen geklaert; der kleine Turn-7-Abgang wird konservativ klassenweise gebucht. Offen bleiben die chargenscharfe Vorhistorie und weitere Folgeabgaenge.
  - Quelle: [Nordlinie-01-Stuetzbaukasten](../05-projects/Nordlinie-01-Stuetzbaukasten.md), [Nordlinie-01](../05-projects/Nordlinie-01.md)
- Delta 8 (review): D5 fuehrt jetzt einen konservativ generierten aktuellen Stationsbestand. Der Stand ist bewusst als arbeitsfaehiger Basispuffer modelliert: relativ intakter Altbestand durch Verriegelung, aber kein breiter Handelsueberhang.
  - Quelle: [D5](../03-locations/D5.md), [Warenueberblick-T0](../../../00-admin/Warenueberblick-T0.md)
- Delta 9 (review): D5 fuehrt jetzt auch einen operativen Verbrauchsrahmen fuer Basisbetrieb, Nordlinie und Draisine; damit ist erstmals nicht nur Bestand, sondern laufender Projektdruck pro Station lesbar.
  - Quelle: [Nordlinie-01](../05-projects/Nordlinie-01.md), [Draisine-Transportmodul](../05-projects/Draisine-Transportmodul.md)
- Delta 10 (review): D5 fuehrt jetzt echte Reststaende nach dem kleinen Nordlinie-Turn-7-Abgang sowie nach der aktuellen Draisine-Werkstattbindung; damit stehen fuer beide offenen Projekte erstmals konkrete D5-Abgaenge und verfuegbare Restposten im selben Inventar.
  - Quelle: [Nordlinie-01](../05-projects/Nordlinie-01.md), [Draisine-Transportmodul](../05-projects/Draisine-Transportmodul.md)

Aktionen
--------
- [ ] Lagerplätze definieren und QR/Tagging überlegen
- [ ] Verbrauchslog anlegen
