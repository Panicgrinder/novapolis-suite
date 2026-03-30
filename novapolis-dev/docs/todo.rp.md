---
title: "TODO (Novapolis-RP)"
date: 2025-11-12 08:59
tags: [doc]
stand: 2026-03-30 07:16
update: Das operative Arbeitsledger fuer die finale Metro-Warenzuteilung ist angelegt; der RP-Fokus liegt jetzt wieder auf Transferkette und Delta-/Bilanzformat.
checks: snapshot-lock PASS; markdownlint PASS; frontmatter PASS; todo-index PASS; naming-policy PASS; path-portability PASS; logs-policy PASS; doc-freshness PASS (2026-03-30 07:16)
---
<!-- markdownlint-disable MD012 MD022 MD041 -->
TODO (Novapolis-RP)
-------------------

<!-- Migration: Quelle aus dem frueheren coding-Hub, uebernommen am 2025-10-29 -->
<!-- Relocated aus dem ehemaligen Novapolis-RP Development-Hub nach `novapolis-dev/docs/todo.rp.md` am 2025-10-29 -->

Prioritaetstags (aktiv)
-----------------------

- `Jetzt`: RP-Folgearbeit sitzt auf Transferkette, Delta-/Bilanzformat und belastbarer Fraktionsaggregation fuer den Inventar-Backfill.
- `Als naechstes`: Mengen-Backfill fuer Inventare konkret fortsetzen; das Arbeitsledger steht, die Handentscheidungen muessen jetzt in die Zielinventare ueberfuehrt werden.
- `Spaeter`: TTS-Block (OGG-Kandidaten + Live-Dialog-Cache) ausrollen.

Aktiver Vorbereitungspunkt (2026-03-20)
---------------------------------------

- [x] [Jetzt] Heutiges Pilotpaket fuer Mengen-Backfill und Skill-Mapping vorbereitet.
  - Ziel: den offenen RP-Folgepunkt ohne Scope-Drift in einen konkreten Arbeitsslot fuer heute ueberfuehren.
  - Evidenz: `novapolis-dev/docs/process/rp-inventory-backfill-pilot-2026-03-20.md`.
  - Pilot-Scope: `D5-inventar`, `C6-inventar`, `Novapolis-inventar`.
  - Korrektur 2026-03-20 06:21: RAW und Staging fuer Inventar-/Item-Belege sind jetzt explizit mit durchsucht und im Pilotblatt verankert.
  - Abgleichstart 2026-03-20 06:28: D5/C6/Novapolis werden jetzt gegen RAW, Staging, Szenen und Missionslog gegengeprueft; erster harter Driftpunkt ist `D5-inventar` mit dort gefuehrten C6-Bestaenden trotz Trennungsregel.
  - Ergebnis 2026-03-20 06:36: erster konservativer Abgleich ist abgeschlossen; D5 fuehrt keine C6-Posten mehr lokal, C6 ist als lokaler Belegkontext ohne freie Mengen geschaerft, Novapolis bleibt aggregiert-konservativ.
  - Ergebnis 2026-03-20 06:45: belegter Energie-Tagesabschluss fuer Tag 12 -> 13 ist in D5/C6/Novapolis nachgezogen; nur Bilanz- und Transferlogik, keine neuen absoluten Zellmengen.
  - Ergebnis 2026-03-20 06:52: belegter Materialverbrauch fuer Tag 12 -> 13 ist als Delta eingetragen (`1,3 t Baustoffe`, `120 m Schienenprofil`, `18 m² Betonplatten`, `2` beschaedigte Werkzeuge); Rest- und Standortmengen bleiben offen.
  - Ergebnis 2026-03-20 07:14: `inventar_c6_v2` und `logistik_c6_v2` liefern einen harten C6-Startsnapshot mit Stueckzahlen (`Luftfilter(3)`, `Ersatzrohre(12)`, `Kabelspulen(6)`, `Schmieroel(5)`, `Strommodule(2)`, `Wasserkanister(4)`, `Werkzeugsets(2)`, `Sensorpaket(1)`, `Rationen(9)`, `Wasserflaschen(10)`, `Schutzanzuege(2)`, `Ersatzmasken(3)`).
  - Ergebnis 2026-03-20 07:22: `RAW-canvas-2025-10-16T12-00-00-000Z` liefert fuer D5 einen fruehen Stationsanker mit `Union-Kisten (3)`, Ersatzrohren/Ventilkomponenten, defekter Reparaturstation und `60 %` lesbaren Schaltplaenen; fuer Fraktionssummen fehlt weiter die spaetere Transfer- und Verbrauchskette.
  - Ergebnis 2026-03-20 11:33: Die fehlende Transferkette ist jetzt konkret eingegrenzt. Belegt sind allgemeine Frachtarten (`D5 -> C6: Bauteile/Werkzeuge/Versorgungsgueter`, `C6 -> D5: Materialrueckfuehrung`) und die Tagesbilanz Tag 12 -> 13, aber nicht die Item-Kette `Entnahme -> Transport -> Ankunft -> Quittung`.
  - Folge fuer den offenen Punkt: Solange keine standortscharfen Abbuchungen und keine belegten Zielbuchungen vorliegen, bleibt `Novapolis-inventar` bewusst ohne harte Fraktionssumme.
  - Ergebnis 2026-03-20 11:40: Die Guetermission `D5 -> C6` ist jetzt als eigener Missionsanker im aktiven SSOT verankert. Sie taugt fuer Richtungs- und Kontextbeleg, aber weiterhin nicht fuer Mengenpromotion, weil Item-Entnahme und Quittung fehlen.
  - Ergebnis 2026-03-20 11:49: D5- und C6-Teilinventar fuehren den Materiallauf jetzt ebenfalls als lokale Review-Anker. Damit ist der Gap standortscharf dokumentiert, ohne neue Mengen oder stillschweigende Buchungen zu erfinden.
  - Ergebnis 2026-03-27 08:33: Die C6-Zielseite ist jetzt auch auf Systemebene enger gerahmt. `logistik_novapolis_v2` fuehrt `D5 -> C6 (Bauteile, Werkzeuge, Versorgungsgueter)` als aktive Fracht, `logistik_c6_v2` benennt fuer C6 `Primaerlager (Bereich 3)` und `Sekundaerlager (Kontrollraum)`. Das taugt als semiformeller Zielanker fuer einen missionierten Versorgungslauf, aber nicht als konkrete Zielbuchung oder Charge.
  - Folge fuer den offenen Punkt 2026-03-27 08:33: Konservativ definierbar ist derzeit hoechstens `missionierter Versorgungslauf D5 -> C6 mit bestaetigtem Empfang, Bestandsaufnahme und nachgelagerter Baustellenverteilung`. Nicht definierbar bleiben Item-Mengen, exakte Lagerzuordnung des konkreten Laufs und Inventarlog-Quittung.
  - Ergebnis 2026-03-27 09:46: Vor manueller Verteilung ist der RAW-Rettungsstand jetzt klar abgegrenzt. Hart rettbar sind ein quantifizierter C6-Startsnapshot, ein teilquantifizierter D5-Startanker, der generische Transferpfad `D5 -> C6`, der semiformelle C6-Empfangs-/Zielanker sowie einzelne Tagesdeltas fuer Energie und Materialverbrauch.
  - Folge fuer den offenen Punkt 2026-03-27 09:46: Weich rettbar sind Rollen-, Freigabe- und Prozesslogik fuer D5/C6/Novapolis. Manuell gesetzt werden muessen weiterhin aktuelle Fraktionssummen, standortscharfe Restbestaende, mehrtaegige Verbrauchsreihen sowie konkrete Transfermengen pro Lauf.

- [x] [Jetzt] Ebenenmodell, Pflichtartefakte und Delta-Formate fuer den metro-weiten Warenbestand aus dem vorhandenen RP-Modul abgeleitet.
  - Ziel: den offenen Backfill von einer losen Inventarsammlung auf eine feste Promotionskette `Charakter -> Team/POI -> Station -> Fraktion -> Metro` umstellen.
  - Evidenzbasis: `00-admin/Logistik.md`, `00-admin/Waren-Index.md`, `00-admin/Warenueberblick-T0.md`, `00-admin/Metrokarte-T0.md`, `00-admin/Stationskontroll-Matrix.md`, `00-admin/Fraktionen-Taxonomie.md`, die vorhandenen Fraktionsinventare unter `01-factions/*/04-inventory/`, die Novapolis-Orte/POIs unter `01-factions/novapolis/03-locations/`, `Missionslog-Novapolis.md`, `person-index-np.md`, `novapolis-markets.md`, `novapolis-pricebands.md` sowie die szenischen `inventoryRefs` unter `06-scenes/`.
  - Verbindliches Ebenenmodell:
    - Charakter: personengebundene Ausruestung, mitgetragene Verbrauchsgueter und explizite Ausgabe-/Rueckgabevorgaenge; keine stillen privaten Lagerbestaende ohne Rollen- oder Szenenanker.
    - Team/POI: operative Zwischenebene fuer Werkstatt, Lagerhalle, Schleuse, Konvoi oder feste Arbeitsgruppe; fuehrt Ausgabe, Annahme, Quarantaene, Puffer und lokale Arbeitsverbraeuche.
    - Station: kanonisches Standortinventar aggregiert die POI-/Teamlage je Station und fuehrt standortscharfe Delta- und Restlogik.
    - Fraktion: aggregiert nur bestaetigte Stationsstaende, fraktionsweite Bilanzen und belegte Handels-/Transferstroeme.
    - Metro: fuehrt nur vergleichende T0-/Wochenlage je Fraktion, Station und Warengruppe; keine implizite Welt-Gesamtsumme ohne belastbare Fraktionspfade.
  - Pflichtartefakte je Ebene:
    - Charakter: Charakter-Canvas plus Missions-/Szenenbezug; eigene Inventarseite nur bei wiederkehrendem Besitz, Ausgabehoheit oder dauerhafter Rollenlast.
    - Team/POI: Orts-/POI-Canvas plus zugehoeriges Inventar- oder Logistikziel fuer Ausgabe, Eingang, Quarantaene und Lagerlauf.
    - Station: Lokations-Canvas plus Stationsinventar und Missions-/Logistikverweise.
    - Fraktion: Fraktionsinventar plus Missionslog; bei Aussenfluss zusaetzlich Handelslog oder Relationslog.
    - Metro: Admin-Artefakte `Metrokarte-T0`, `Stationskontroll-Matrix`, `Warenueberblick-T0` und `Fraktionen-Taxonomie` als Vergleichs- und Guardrail-Ebene.
  - Delta-Formate (Minimalset, aus vorhandenem RP-Bestand abgeleitet):
    - `Transfer`: Datum, Status, Item/Warengruppe, Menge/Einheit oder `tbd`, `von`, `nach`, Anlass, Beleg, Verantwortliche/Quittung.
    - `Verbrauch`: Datum, Status, Item/Warengruppe, Menge/Einheit oder `tbd`, Entnahmeort, Zweck/Projekt, Beleg.
    - `Handel`: Datum, Status, Item/Warengruppe, Menge/Einheit oder `tbd`, Gegenpartei, Abrechnung/Band, Uebergabepunkt, Beleg.
    - `Bilanz`: Zeitraum, Ebene, Delta je Warengruppe oder Energiekonto, bekannte Vor-/Nachher-Staende oder `tbd`, Belegkette.
  - Promotionsregel: `Scene/RAW -> Missionslog oder Logistik -> Teilinventar/POI -> Stationsinventar -> Fraktionsinventar -> Metro-Ueberblick`; ohne sauberen Uebergabeschritt wird nicht nach oben promoted.

- [x] [Jetzt] Operative Zuteilungsmatrix fuer die finale Metro-Warenverteilung aus aktiver SSOT und RAW-Rettungsstand abgeleitet.
  - Ziel: vor der finalen Handverteilung alle belastbaren RP-Daten in eine Arbeitsmatrix `hart gesetzt | konservativ geschaetzt | manuell zu entscheiden` ueberfuehren.
  - Evidenz: `novapolis-dev/docs/process/rp-metro-warenzuteilung-matrix-2026-03-27.md`.
  - Ergebnis 2026-03-27 16:12: Die Matrix fuehrt Metro-Rahmen, Novapolis-T0-Lage, D5-/C6-Startanker, Tagesdeltas und den Versorgungslauf `D5 -> C6` in genau dieser Dreiteilung zusammen.
  - Folge fuer die finale Handverteilung 2026-03-27 16:12: Direkt gesetzt werden koennen die belegten D5-/C6-Anker und Tagesdeltas; offen fuer Handentscheid bleiben aktuelle Fraktionssummen, konkrete Transfermengen, Restbestaende je Station und exakte Mengen der uebrigen Hauptfraktionen.
  - Recheck 2026-03-27 16:19: Die Matrix ist jetzt fraktionsscharf fuer Arkologie-A1, Schienenbund, Haendlerbund, Eiserne Enklave/Eisenkonklave, Schattenbund und Fluesterkollektiv nachgezogen. Novapolis bleibt darin ausdruecklich gesondert, weil die aktive SSOT nur eine lokale Kernfraktion in frueher Aufbauphase belegt, nicht aber eine etablierte Metro-Hauptfraktion mit normalisiertem Handelsnetz.

- [x] [Jetzt] Finale Metro-Warenzuteilung aus der Matrix in ein operatives Arbeitsledger ueberfuehren.
  - Ziel: Die Dreiteilung `hart gesetzt | konservativ geschaetzt | manuell zu entscheiden` soll in ein belastbares Zuteilungsblatt fuer Stationen und Fraktionen ueberfuehrt werden.
  - Akzeptanzkriterien:
    1) jeder verteilte Posten ist als `fix`, `rahmenwert` oder `handentscheidung` markiert,
    2) Station, Fraktion und Zielpfad pro Posten sind sichtbar,
    3) offene Handentscheidungen bleiben explizit als `tbd` statt implizit gesetzt,
    4) das Ergebnis verweist sauber auf Matrix, Inventarebene und den spaeteren Updatepfad fuer D5/C6/Fraktionsinventare.
  - Evidenz: `novapolis-dev/docs/process/rp-metro-warenzuteilung-matrix-2026-03-27.md` fuehrt die benoetigte Dreiteilung bereits vollstaendig; im Board selbst fehlt aber noch der direkte Uebergang in ein operatives Verteilungsledger fuer die finale Handarbeit.
  - Abschluss 2026-03-30: `novapolis-dev/docs/process/rp-metro-warenzuteilung-arbeitsledger-2026-03-30.md` fuehrt die Matrix jetzt als operatives Ledger mit getrennten Tabellen fuer `fix`, `rahmenwert` und `handentscheidung`, sichtbaren Zielpfaden sowie einem expliziten Updatepfad fuer `D5-inventar.md`, `C6-inventar.md`, `Novapolis-inventar.md` und die externen Fraktionsinventare.

Canvas-Rettung - Sprint 1 (Stand 2025-11-01)
--------------------------------------------
Archiv-Hinweis (manuell, bis Validator bereit)
----------------------------------------------

- Sobald ein Abschnitt (H2/H3) vollständig abgehakt ist ([x] überall) und - für RP - kanonisiert, bitte den gesamten Block manuell nach `novapolis-dev/archive/todo.<modul>.archive.md` verschieben (neuester oben).
- Direkt unter der Abschnitts-Überschrift im Archiv eine Zeile ergänzen: `archived_at: YYYY-MM-DD HH:MM`.
- Automatisierung folgt erst nach Struktur-Review/Validator (Dry-Run only). Keine halb fertigen Blöcke verschieben.

Plan Charakter-Review (laufend)
-------------------------------

Reihenfolge
-----------

- Ronja Kerschner → Abgleich `resolved.md`, RAW `char_ronja_v2` + Flag, Rollenmatrix, Ziele, Systemverknüpfungen, Drift-Notizen. *(erledigt 2025-11-01T17:10+01:00)*
- Jonas Merek → RAW `RAW-canvas-2025-10-16T14-12-00-000Z.*`, Schwesterstatus gemäß `[FACT][JONAS-SIS]`, Werkstatt-/Tunnelinfos konsolidieren. *(erledigt 2025-11-02T13:55+01:00)*
- Lumen → Jonas-Quellen + `[FACT][PROXIMITY]`, Fähigkeiten/Kopplung und Trainings-Canvas aktualisieren. *(validiert erledigt 2026-02-21)*
- Kora Malenkov → RAW `RAW-canvas-2025-10-16T14-56-00-000Z.txt`, paranoide Vorsicht, C6-Linienstatus (FACT `C6-LINES`), Echo-Interaktion. *(erledigt 2025-11-02T14:20+01:00)*
- Senn Daru → Relationslog `RAW-canvas-2025-10-16T08-07-00-000Z.*`, Handels-/Diplomatie-Notizen, Wissensgrenzen. *(validiert erledigt 2026-02-21)*
- Marven Kael → RAW `RAW-canvas-2025-10-16T14-56-10-000Z.*`, Konvoi-/Handelsleitung (`[FACT][CARAVAN-LEADERSHIP]`), Beziehungen Händlergilde/Novapolis. *(erledigt 2025-11-02T14:45+01:00)*
- Arlen Dross → RAW `RAW-canvas-2025-10-16T14-56-20-000Z.*`, Vermittlerrolle, Reflex-Einschätzung. *(erledigt 2025-11-02T15:05+01:00)*
- Pahl → RAW `RAW-canvas-2025-10-16T14-41-00-000Z.*`, Gesundheitsstatus, Risiken, Energie-/Generatorwissen. *(erledigt 2025-11-02T15:25+01:00)*
- Reflex (Primärinstanz) → RAW `char_reflex_v2`, FACTs `[REFLEX-*]` (Frequenzband, Detach, Speech), Wissens-/Trainings-Canvas synchronisieren. *(erledigt 2025-11-02T16:05+01:00)*

Arbeitsschritte pro Charakter
-----------------------------

- Quellen sammeln: `database-curated/staging/reports/resolved.md`, `.../uncertainties.md`, zugehörige RAW-/Flag-Dateien, overlap-Reports.
- Canvas aktualisieren (Werte, Skills, Motivation, Wissensmatrix, Beziehungen, Ziele, Risiken) und Systemverknüpfungen prüfen.
- Zugehörige Wissens-/Trainings-Canvases mitziehen (Instanzen).
- Behavior-Signatur gegen Anchor-Register prüfen; Drift-Flags dokumentieren.
- JSON-Sidecar, `char-block-nord-sources.md`, `person-index-np.md`, DONELOGs (`novapolis-dev/docs/donelog.md`, Root `DONELOG.md`) und TODO-Status aktualisieren.
- Nach einem Bündel Updates Validator laufen lassen (`npm --prefix novapolis-rp/coding/tools/validators run validate:rp` + optional `npm --prefix ... run validate:crossrefs`).

Archivstatus (2026-02-22)
-------------------------

- Vollständig erledigte Blöcke `Aktiv jetzt (sicher)`, `Priorität B - Logistik & Inventar` und `Priorität C - Systeme, Indizes, Ereignisse` wurden nach `novapolis-dev/archive/todo.rp.archive.md` verschoben.

Arbeitsregeln & Referenzen
--------------------------

- Workflow siehe `novapolis-dev/docs/process/rp-canvas-rescue/canvas-rescue-plan.md`.
- Quellen + Drift-Notizen in `novapolis-dev/docs/process/rp-canvas-rescue/char-block-nord-sources.md` berücksichtigen.
- FACT-Beschlüsse aus `novapolis-dev/docs/process/rp-canvas-rescue/resolved.md` vor Promotion prüfen.
- Jede Migration mit JSON-Sidecar und DONELOG-Eintrag dokumentieren (`novapolis-dev/docs/donelog.md`).
- Flags (`vorsichtig_behandeln`, `korrupt`) sichtbar übernehmen, bis Review abgeschlossen ist.

Linkübersicht
-------------

- Plan: `novapolis-dev/docs/process/rp-canvas-rescue/canvas-rescue-plan.md`
- Quellen: `novapolis-dev/docs/process/rp-canvas-rescue/char-block-nord-sources.md`
- RAW: `database-raw/99-exports/`
- Kanon/Policies: `novapolis-dev/docs/process/rp-canvas-rescue/resolved.md`, `.github/copilot-instructions.md`

<details>
<summary>Archiviertes Backlog (ausgelagert)</summary>

- Volltext ausgelagert nach `novapolis-dev/archive/todo.rp.historical-backlog.md`.
- Inhalt bleibt historisch/nicht aktiv; Reaktivierung nur per explizitem Soll-Ist-Abgleich gegen aktuelle SSOT-Dateien.

</details>
Neue Aufgaben - Zeitmodell, Annotation & Logs (2025-11-01 22:24)
----------------------------------------------------------------

Prioritaet 0 - Gesamtbild T0 (vor Detailmengen)
-----------------------------------------------

Ziel
----

- Zuerst ein belastbares Gesamtbild aufbauen (Karte, Kontrolle, Warenlage), danach Detailmengen pro Station schrittweise nachziehen.
- Keine neuen unbelegten Canon-Behauptungen; unbekannte Punkte bleiben explizit `tbd`/`unklar`.

Umsetzungsreihenfolge (MVP)
---------------------------

- [x] P0.1 Metro-Topologie als Arbeitskarte T0 anlegen (Stationen, Verbindungen, Status pro Knoten/Kante).
- [x] P0.2 Stationskontrolle je Fraktion erfassen (gesichert/umkaempft/verlassen/unklar + Confidence).
- [x] P0.3 Warenueberblick T0 je Fraktion/Station als Bandbreitenmodell erfassen (`none|low|medium|high` statt Scheingenauigkeit).
- [x] P0.4 Herkunftslabel pro Warenposten verpflichtend setzen (`legacy|evac_e3|scavenged|produced|unknown`).
- [x] P0.5 D5/C6 sauber als fruehe Aufbauphase markieren (kein etablierter Handel; Bestand nur aus Altbestand/Funden/E3-Mitnahme).
  - Evidenz: `novapolis-rp/database-rp/00-admin/Metrokarte-T0.md`, `novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md`, `novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md`.

Scope-Guardrails
----------------

- [x] D5/C6: Keine Handelsnormalisierung simulieren, solange Handelsbeziehungen im RP noch nicht etabliert sind.
- [x] Etablierte Fraktionen: Grundvorräte zulassen, aber Stationenlage explizit als unvollstaendig kennzeichnen.
- [x] Mengenpraezision erst nach P0.1-P0.4 erhoehen; bis dahin nur Bandbreiten + Quellenanker.

Konkrete Deliverables
---------------------

- [x] Admin: Metrokarte-T0 (Knoten/Kanten + Statusmodell) unter `00-admin`.
- [x] Admin: Fraktionskontroll-Matrix Stationen (Fraktion x Station x Status x Confidence).
- [x] Admin: Warenueberblick-T0 (globales Raster + Herkunftssystem).
- [x] Fraktionen: Minimal-Abgleich je Basis/known stations mit Verweis auf Admin-SSOT. *(erledigt 2026-02-23)*
  - Evidenz: `novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md` (Abschnitt „Minimal-Abgleich Basis-/Known-Stationen (T0)“) mit Referenzen auf `Metrokarte-T0`, `Stationskontroll-Matrix`, `Warenueberblick-T0`.

Definition of Done (P0)
-----------------------

- [x] Jede bekannte Station ist in Karte + Kontrollmatrix mindestens einmal referenziert. *(erledigt 2026-02-23)*
  - Evidenz: `novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md` enthält jetzt alle in `novapolis-rp/database-rp/00-admin/Metrokarte-T0.md` geführten Stationscodes (Abdeckung 54/54).
- [x] [Jetzt] Jede Fraktion hat einen T0-Warenueberblick mit Herkunftslabeln.
  - Evidenz: `novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md` (Abschnitt `Fraktionsueberblick T0 (Herkunftslabel)`).
- [x] [Jetzt] D5/C6 sind konsistent als fruehe Aufbauphase modelliert; keine impliziten Handelsannahmen.
  - Evidenz: `novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md` (Abschnitt `D5/C6-Modell (fruehe Aufbauphase)`).
- [ ] [Als naechstes] Danach erst Mengen-Backfill in Inventaren (D5/C6/Fraktionen) starten.
  - Startreihenfolge fuer den heutigen Pilot: `C6-inventar` -> `D5-inventar` -> `Novapolis-inventar`.
  - Arbeitsgrundlage: `novapolis-dev/docs/process/rp-inventory-backfill-pilot-2026-03-20.md`.
  - Verbindliche Gesamt-Reihenfolge fuer den naechsten Ausbau: `Metro-Rahmen` -> `Fraktionsbasis/known stations` -> `Stationsinventare` -> `Team/POI` -> `Charakter-/Rollenanker` -> `Fraktionsaggregation`.
  - Vor jeder Mengenpromotion muessen mindestens die betroffene Missions-/Logistikspur und die Ziel-Inventarebene existieren; fuer Aussenfluss zusaetzlich Handels- oder Relationslog.
  - Die vier Minimal-Deltas `Transfer`, `Verbrauch`, `Handel`, `Bilanz` sind ab jetzt der Pflichtwortschatz fuer neue Bestandsfortschreibung; ohne Quelle, Ziel oder Beleg bleibt der Eintrag `tbd`/`offen`.

- [ ] [Jetzt] Fehlende Transferkette `Entnahme -> Transport -> Ankunft -> Quittung` fuer `D5 -> C6` mit belastbaren RP-Belegzeilen schliessen.
  - Ziel: den aktuell nur generisch belegten Materiallauf so absichern, dass er fuer echte Bestandsfortschreibung taugt.
  - Akzeptanzkriterien:
    1) mindestens eine explizite Entnahmezeile im Quellkontext D5 ist belegt,
    2) mindestens eine Ankunfts- oder Zielbuchungszeile fuer C6 ist belegt,
    3) Verantwortliche oder Quittung sind im Missions-/Logistikpfad genannt,
    4) `Missionslog-Novapolis.md`, `D5-inventar.md`, `C6-inventar.md` und `Novapolis-inventar.md` fuehren dieselbe Transferkette ohne Widerspruch.
  - Evidenz: `novapolis-dev/docs/process/rp-inventory-backfill-pilot-2026-03-20.md`, `novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md`, `novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md`, `novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md`, `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Missionslog-Novapolis.md`.
  - Recheck 2026-03-27 08:14: Umfeld und RAW erneut geprueft. Hart belegt sind aktuell nur `AktiveFracht:D5->C6(Bauteile,Werkzeuge,Versorgungsgueter)` im RAW-Logistikcanvas `RAW-canvas-2025-10-16T13-05-00-000Z`, die Abmeldung `melden sich noch bei D5 ab` sowie die anschliessende `Ankunft` und `Bestandsaufnahme` in C6 im Chat-RAW. Nicht belegt bleiben explizite Entnahmezeilen, konkrete C6-Zielbuchungen in Schleuse/Lagerhalle und Quittungen/Verantwortliche; der Punkt bleibt daher bewusst offen.
  - Recheck 2026-03-27 08:25: D5-seitig ist der Quellkontext jetzt enger. `RAW-canvas-2025-10-20T12-05-00-000Z` belegt ein Materiallager unter dem Bahnsteig mit Lastenaufzug und Nutzung `Schwerlast, Rohstahl, Kabeltrommeln, Energiezellenpaletten`; `Draisine-Transportmodul.md` und Chat-RAW belegen parallel Werkstattbestand, Materiallauf-Unterstuetzung und die Freigabe/Fokussierung von Jonas, Pahl und Lumen auf das Transportmodul. Das reicht fuer eine belastbare Herkunftsannahme `D5-Materiallager und/oder Werkstattbestand`, aber weiter nicht fuer eine harte Inventarbuchung ohne explizite Entnahme- und Quittungszeile.
  - Recheck 2026-03-27 08:29: C6-seitig ist der Empfangspfad jetzt enger. Chat-RAW belegt nach der Abmeldung in D5 nicht nur `Ankunft` und `Bestandsaufnahme`, sondern auch den expliziten Satz `der Empfang der Ware muss bestaetigt werden`; anschliessend soll die Ware `zusammen mit der aus D5 an die Baustellen gebracht` werden. Das reicht fuer eine belastbare Zielannahme `Empfang in C6 mit nachgelagerter Baustellenverteilung`, aber weiter nicht fuer eine harte Inventarbuchung in `C6-Schleuse` oder `C6-Lagerhalle`, weil Einlagerungs-/Inventarlog-Zeilen fehlen.

- [ ] [Jetzt] `Novapolis-inventar.md` von der generischen Fraktionslage auf ein belegtes Delta-/Bilanzformat umstellen.
  - Ziel: Das Fraktionsinventar soll nicht nur offene Hinweise sammeln, sondern die belegten Deltas `Transfer`, `Verbrauch`, `Handel`, `Bilanz` direkt in einer auswertbaren Struktur fuehren.
  - Akzeptanzkriterien:
    1) jeder aktuelle Fraktionsposten ist einem Delta-Typ zugeordnet,
    2) unbelegte Restmengen bleiben sichtbar `tbd`, aber ohne Mischformat aus Freitext und Halb-Buchung,
    3) die Struktur referenziert sauber auf D5/C6-Teilinventare und Missionslog,
    4) RP-Validator bleibt gruen.
  - Evidenz: Das Board fuehrt seit 2026-03-20 die vier Pflicht-Deltas; `Novapolis-inventar.md` enthaelt bislang zwar belegt/offen-Anker, aber noch keine eigenstaendige Delta-Struktur.

- 24×1h-Runden (PC-zentriert) einführen
  - [x] Policy festhalten: Stunde spult leise weiter, bis ein PC-relevantes Ereignis eintritt (z. B. „Reflex weckt Ronja“). *(erledigt 2026-02-22)*
  - [x] Pro Stunde zwei Logs führen: `world_log` (Wahrheit) und `pc_log` (nur Sichtbares für den PC). *(erledigt 2026-02-22)*
  - [x] Sichtbarkeit umsetzen: scope `private|allies_only|pc|public`, plus `channel`, `source`, `confidence`, `freshness` (siehe Knowledge-Schema unten). *(erledigt 2026-02-22)*
  - [x] Referenz: `novapolis-dev/docs/specs/annotation-spec.md` vorhanden und weiterhin passend zum 24×1h-Vorgehen. *(validiert 2026-02-22)*

- Knowledge-Annotation schrittweise ergänzen (wichtige Charaktere/Missionen zuerst)
  - [x] Charaktere: Reflex, Ronja, Jonas - Knowledge-Einträge in dedizierten Dateien (z. B. `Reflex-Wissensstand-Trainingsstand.md`) und/oder Canvas-Frontmatter `knowledge:`. *(umgesetzt 2026-02-22)*
  - [x] Missionen/Ereignisse: je Kernereignis mind. ein Knowledge-Item mit `about`, `channel`, `source`, `scope`, `confidence`, `freshness`, `visibility_to`, `attachments`. *(umgesetzt 2026-02-22)*
  - [x] Rückblendenprozess: Items per Log/Funk von `allies_only/hidden` → `pc` heben (keine Retcons, nur Sichtbarkeit). *(umgesetzt 2026-02-22)*
  - [x] Referenz: `novapolis-dev/docs/specs/annotation-spec.md` vorhanden und weiterhin passend. *(validiert 2026-02-22)*

- Actions-Schema (für möglichen „Zug-um-Zug“-Wechsel) jetzt leicht mitpflegen
  - [x] In Missions-/Orts-Canvases `actions:` notieren: `verb`, `base_duration_min`, `effort`, `interruptible`, `locks`, `may_trigger_event`, `resources`. *(umgesetzt 2026-02-22)*
  - [x] Kernaktionen definieren (5-10): Reinigen, Reparatur, Reise, Wache, Funk, Erste Hilfe, Erkundung. *(umgesetzt 2026-02-22)*
  - [x] Naming-Konvention und kurze Beispiele dokumentieren. *(durch Spec vorhanden; validiert 2026-02-22)*
  - [x] Referenz: `novapolis-dev/docs/specs/annotation-spec.md` vorhanden und weiterhin passend. *(validiert 2026-02-22)*

- Skills aus Verhaltensmatrix ableiten (ohne zweites System)
  - Vorbereitung 2026-03-20: Start-Scope fuer `reparieren`, `wache` und `funk|wahrnehmung` auf Basis von `annotation-spec.md` und `AI-Behavior-Mapping.md` festgelegt.
  - [x] [Jetzt] Mapping-Gewichte je Skill (0-3) vorgeschlagen (Matrix-Dimensionen -> Skill), Ausgangswerte pro Rolle festgelegt. *(umgesetzt 2026-03-20; Referenz: `novapolis-dev/docs/specs/annotation-spec.md`, Abschnitt `Novapolis V1 (konservative Arbeitsfassung)`)*
  - [x] [Jetzt] Formel/Beispiele im Spec verlinkt; Ableitung bleibt on-demand, keine Duplikat-Wahrheit. *(umgesetzt 2026-03-20; Beispiele fuer Ronja, Jonas und Kora im Spec ergänzt)*
  - Ausbau 2026-03-20 07:08: zweite Referenzreihe fuer `Pahl`, `Reflex`, `Lumen` und `Echo` im Spec nachgezogen; Rollenfit bleibt konservativ auf `wartung_technik` bzw. `sicherung_monitoring` begrenzt.

- [ ] [Als naechstes] Skill-Mapping-V1 an mindestens zwei aktiven Missions- oder Rollenpfaden gegen reale Szenen pruefen.
  - Ziel: Die dokumentierte V1 soll nicht nur als Spec existieren, sondern an echten RP-Faellen auf Plausibilitaet und Grenzfaelle gegengeprueft werden.
  - Akzeptanzkriterien:
    1) mindestens zwei konkrete Szenen/Missionen sind mit der V1 nachvollziehbar gegengelesen,
    2) auffaellige Ueber- oder Unterbewertungen sind als Guardrail oder Anpassung dokumentiert,
    3) keine zweite Wahrheit in Charakterdateien entsteht,
    4) Ergebnis landet im RP-Prozesslog oder Spec-Nachtrag.
  - Evidenz: `novapolis-dev/docs/specs/annotation-spec.md` enthaelt inzwischen V1-Beispiele fuer sieben Kernfiguren, aber noch keinen dokumentierten Realabgleich gegen aktive Missionsablaeufe.

- TTS (gemischt)
  - [ ] [Spaeter] Vorproduzierte OGG-Summaries je Stunde (world/pc) - Kandidaten markieren.
  - [ ] [Spaeter] Live-Dialoge via Coqui XTTS v2 mit Cache (Hash(Text+Stimme)); Fallback Windows/Azure nur bei Bedarf.






