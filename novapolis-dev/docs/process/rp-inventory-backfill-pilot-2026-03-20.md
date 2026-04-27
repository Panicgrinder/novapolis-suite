---
stand: 2026-04-27 06:11
update: Der Pilot fuehrt den C6-Zielanker jetzt ueber den Hauptort C6; Schleuse und Lagerhalle bleiben nur noch Kompatibilitaetsstubs.
checks: snapshot-lock PASS (2026-04-27 06:11); markdownlint=PASS (2026-04-27 06:06); frontmatter=PASS (2026-04-27 06:06); todo-index-sync=PASS (2026-04-27 06:06); doc-freshness=PASS (2026-04-27 06:06); validate:rp=PASS (2026-04-27 06:06)
---

RP-Pilot: Mengen-Backfill D5/C6/Novapolis (2026-03-20)
=======================================================

Ziel
----

- Den offenen RP-Folgepunkt "Mengen-Backfill in Inventaren" in einen konkret ausfuehrbaren Pilot-Scope fuer heute ueberfuehren.
- Parallel die offene Skill-Ableitung so vorbereiten, dass anschliessend nur noch die eigentliche Gewichtsentscheidung fehlt.

Pilot-Scope fuer heute
----------------------

- Zielinventare:
  - `novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md`
  - `novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md`
  - `novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md`
- Heute ausdruecklich nicht im Scope:
  - weitere Fraktionsinventare ausser als Referenzmuster,
  - implizite Handelsnormalisierung fuer D5/C6,
  - freie Mengenerfindung ohne belastbare Missions-, Szenen- oder Transferbelege.

Verbindliche Guardrails
-----------------------

- Inventare bleiben standortgetrennt; Transfers nur via Mission/Logistik mit Quelle und Ziel.
- Ohne belastbare Quelle bleiben Mengen und Kennzahlen `tbd`.
- D5/C6 bleiben T0-seitig fruehe Aufbauphase; Bestandsannahmen duerfen nur aus `legacy`, `evac_e3` und `scavenged` hergeleitet werden.
- Kugeln bleiben Inventar-Item, aber ohne freie Zahlenretcons.

Primaere Belegquellen
---------------------

- T0-Lagebild und Herkunftslogik:
  - `novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md`
- Inventar-/Transfer-Regeln:
  - `novapolis-rp/database-rp/00-admin/Logistik.md`
- Standort-SSOT:
  - `novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md`
  - `novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md`
- Missions-/Szenenanker fuer den Pilot:
  - `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Missionslog-Novapolis.md`
  - `novapolis-rp/database-rp/06-scenes/scene-2026-01-16-a.md`
  - `novapolis-rp/database-rp/06-scenes/scene-2026-01-14-b.md`
  - `novapolis-rp/database-rp/06-scenes/scene-2025-10-27-g.md`
  - `novapolis-rp/database-rp/06-scenes/scene-2025-10-27-d.md`
  - `novapolis-rp/database-rp/06-scenes/scene-2025-10-27-x.md`
- Item-Kanon fuer Namensabgleich:
  - `novapolis-rp/database-rp/00-admin/Waren-Index.md`
  - `novapolis-rp/database-rp/04-inventory/Marktpreise-inventar.md`

Rohdatenstatus fuer Inventare und Items
---------------------------------------

- Korrektur zur ersten Vorbereitung: Der fehlende Punkt "RAW noch nicht gezielt durchsucht" ist jetzt abgearbeitet.
- Es wurde explizit in `novapolis-rp/database-raw/**` und `novapolis-rp/database-curated/staging/**` nach Inventar-/Item-Signalen gesucht.
- Relevante Trefferpfade fuer den Pilot:
  - `novapolis-rp/database-raw/99-exports/chat-export.txt`
  - `novapolis-rp/database-raw/99-exports/chat-export-complete.txt`
  - `novapolis-rp/database-curated/staging/chat-export-complete.finalgate.md`
  - `novapolis-rp/database-curated/staging/chat-export (1).review.md`
  - `novapolis-rp/database-curated/staging/chat-export (1).normalized.txt`

Rohdatenbefunde (fuer den Pilot nutzbar)
----------------------------------------

- Inventartrennung D5/C6 ist in RAW und Staging explizit gefordert; keine stillschweigenden Transfers.
- `Filter`, `Energiezellen` und `Werkzeuge` tauchen als C6-Expeditions-/Bestandskontext in RAW und Staging wiederholt auf.
- `Schweissausruestung` und `Adapter DN60` erscheinen als fehlend oder anhaengig, nicht als gesicherter Bestand.
- `Hydrofilter-Behaelter` erscheint als potenzielle Wasserreserve, aber nicht als bereits frei verfuegbarer, quantifizierter Bestand.
- `Kugeln` sind in RAW/Staging als Inventar-Item und Waehrungslogik belegt; Startmengen bleiben offen.

Transferketten-Review (2026-03-20 11:33)
----------------------------------------

- Belastbar belegt sind aktuell drei Ebenen: ein frueher D5-Anker, ein quantifizierter C6-Startsnapshot und der Tagesabschluss Tag 12 -> 13 mit Energie- und Materialdelta.
- Ebenfalls belegt ist eine generische Logistikrichtung: `D5 -> C6 (Bauteile, Werkzeuge, Versorgungsgueter)` sowie `C6 -> D5 (Materialrueckfuehrung)` im RAW-Logistikcanvas `logistik_novapolis_v2`.
- Nicht belegt ist jedoch die vollstaendige Buchungskette pro Item oder Charge: Entnahme aus Quellinventar, konkreter Transportlauf, Ankunft im Zielinventar und Quittung/Verantwortliche.
- Der Tagesabschluss liefert fuer Energie nur Bilanzwerte (`D5 -10`, `C6 -2`, Fraktion `-12`) und fuer Tunnelmaterial nur ein gemeinsames Verbrauchsdelta (`1,3 t Baustoffe`, `120 m Schienenprofil`, `18 m² Betonplatten`, `2` beschaedigte Werkzeuge), aber keine standortscharfe Abbuchung.
- Mehrere RAW-/Staging-Stellen bestaetigen die Luecke explizit: Material wurde fuer C6 transportiert, doch die Menge je Item und das entlastete Quellinventar fehlen; genau diese fehlende Entnahme-/Quittungskette wurde im Chat selbst beanstandet.
- Ergebnis fuer den Pilot: Aus D5- und C6-Ankern kann noch keine belastbare harte Fraktionssumme gebildet werden; vor einer Aggregation braucht es belegte Transferzeilen oder einen kanonischen Wochenreport mit Quelle, Ziel, Mengen und Verantwortlichen.

Nachpruefung D5 -> C6 (2026-03-27 08:14; Autoritaetspfad nachgezogen 2026-04-27 06:06)
---------------------------------------------------------------------------------------------

- Das Umfeld wurde erneut gegen die aktiven SSOT-Dateien `Nordlinie-01.md`, `C6.md`, `C6-Logistik-Policy.md` und das globale Regelwerk `Logistik.md` geprueft. Ergebnis: Der kanonische Soll-Fluss bleibt `Entnahme -> Transport -> Ankunft -> Belege/Quittungen -> Verantwortliche`; die alten Unterorte `C6-Schleuse.md` und `C6-Lagerhalle.md` bleiben nur noch Kompatibilitaetsstubs und definieren keinen eigenen autoritativen Buchungsfall mehr.
- Im spezifischen RAW-Logistikcanvas `RAW-canvas-2025-10-16T13-05-00-000Z.normalized.txt` ist die Transportlage weiter nur generisch belegt: `AktiveFracht:C6→D5(Materialrueckfuehrung),D5→C6(Bauteile,Werkzeuge,Versorgungsgueter)` bei `Transportmittel:manuellerTransport,Tragegestell(ReflexAssist),keineBahnverbindung`.
- Im Chat-RAW ist fuer den laufenden Vor-Ort-Prozess nur der Rahmen hart sichtbar: `melden sich noch bei D5 ab` vor dem Rueckweg bzw. der Verlagerung und danach `Ankunft` plus `Bestandsaufnahme` in C6. Diese Stellen tragen den Missionsablauf, aber keine belastbare Item-Buchung.
- Ein weiterer Inventartreffer `Die Vorraete aus der C6-Expedition (Filter, Energiezellen, Werkzeuge) sind korrekt eingerechnet.` ist als Konsistenzsatz vorhanden, belegt aber keine neue D5->C6-Entnahme oder C6-Zielbuchung fuer den offenen Materiallauf.
- Konsequenz: Der offene Punkt darf derzeit nur auf `generischer Transportkontext plus Prozessrahmen` verengt werden. Ohne explizite Entnahme, Zielbuchung im C6-Hauptort/Lagerkontext und Quittung/Verantwortliche bleibt jede harte Mengenpromotion gesperrt.

Nachpruefung D5-Quellorte (2026-03-27 08:25)
--------------------------------------------

- Der D5-Ursprung ist jetzt enger eingrenzbar als im ersten Recheck. `RAW-canvas-2025-10-20T12-05-00-000Z` belegt fuer D5 ein `Materiallager_unter_Bahnsteig` mit Lastenaufzug (`2000kg`) und klarer Nutzung fuer `Schwerlast, Rohstahl, Kabeltrommeln, Energiezellenpaletten`; damit existiert ein belastbarer physischer Quellort fuer schwere Reparatur- und Versorgungsgueter.
- Parallel ist der Werkstatt-/Transportpfad belegt: `Draisine-Transportmodul.md` fuehrt den Prototyp explizit als `aus Werkstattbestand (D5)` und fuer Materiallauf-Unterstuetzung; Chat-RAW haelt fest, dass Jonas, Pahl und Lumen an der Draisine arbeiten sollten bzw. dafuer freigegeben wurden.
- Damit laesst sich die offene Herkunft enger formulieren: Der Lauf `D5 -> C6` stammt plausibel aus `Materiallager unter Bahnsteig` und/oder `Werkstattbestand D5`, nicht nur aus einem abstrakten Stationsvorrat.
- Die harte Schwelle bleibt dennoch unveraendert: Es fehlt weiterhin die eigentliche Entnahmebuchung aus einem dieser Quellorte, ausserdem fehlen die saubere Zielbuchung in C6 und ein Quittungs-/Verantwortlichenanker. Fuer Inventarmathematik bleibt der Punkt also blockiert; fuer eine spaetere kanonische Definition ist der Ursprung nun nur besser gerahmt.

Nachpruefung C6-Zielseite (2026-03-27 08:29; Autoritaetspfad nachgezogen 2026-04-27 06:06)
---------------------------------------------------------------------------------------------

- Der C6-Empfang ist jetzt enger eingrenzbar als im ersten Recheck. Der Hauptort `C6.md` definiert inzwischen den autoritativen Funktionsrahmen aus Empfangskante, Logistik-/Stagingraum und Kernsektor; `C6-Schleuse.md` und `C6-Lagerhalle.md` bleiben nur noch stabile Verweisziele fuer alte Prozess- und Inventarlinks.
- Im Chat-RAW ist der konkrete Ablauf inzwischen staerker: Nach `melden sich noch bei D5 ab` folgen `Eintreffen in C6`, `Bestandsaufnahme`, der explizite Satz `der Empfang der Ware muss bestaetigt werden` und danach die Aussage, dass die Ware `zusammen mit der aus D5 an die Baustellen gebracht` wird.
- Damit laesst sich die offene Zielseite enger formulieren: Der Lauf `D5 -> C6` endet plausibel in einem bestaetigten Empfang in C6 mit anschliessender operativer Verteilung an Baustellen, nicht nur in abstrakter `Ankunft`.
- Die harte Schwelle bleibt aber auch hier unveraendert: Es fehlt weiterhin die eigentliche Inventar-/Lagerbuchung im C6-Hauptort bzw. dessen Lagerkontext, ausserdem fehlen Charge, Verantwortliche im Logformat und eine saubere Zielzeile im Inventarlog. Fuer Inventarmathematik bleibt der Punkt also blockiert; fuer eine spaetere kanonische Definition ist die Zielseite nun nur besser gerahmt.

Nachpruefung C6-Zielanker und Definitionsschwelle (2026-03-27 08:33)
--------------------------------------------------------------------

- Die engste Zusatzquelle fuer den Zielanker liegt nicht im Chat, sondern im fruehen Logistiksystem: `RAW-canvas-2025-10-16T13-05-00-000Z` fuehrt in `logistik_novapolis_v2` explizit `AktiveFracht:C6->D5(Materialrueckfuehrung),D5->C6(Bauteile,Werkzeuge,Versorgungsgueter)`. Das bestaetigt den Lauf nicht nur als Erzaehlkontext, sondern als systemisch gefuehrte Transportlage.
- `RAW-canvas-2025-10-16T12-55-00-000Z` legt fuer `logistik_c6_v2` zugleich konkrete Zielstrukturen an: `Lager:Primaerlager(C6-Bereich3),Sekundaerlager(Kontrollraum)` sowie einen lokalen Fracht-/Lagerkontext fuer C6. Diese Stellen liefern jedoch keine Buchungszeile fuer den spaeteren D5-Materiallauf, sondern nur den vorhandenen Lagerrahmen.
- Damit ist die konservative Schwelle jetzt klarer: Sicher formulierbar ist ein `missionierter, systemisch angelegter Versorgungslauf D5 -> C6` mit `bestaetigtem Empfang`, `Bestandsaufnahme` und `nachgelagerter Baustellenverteilung`.
- Weiterhin nicht sicher formulierbar sind `Charge`, `welcher Teil in Primaer- oder Sekundaerlager landete`, `wer genau quittierte` und `welche Item-Mengen dadurch in C6 neu eingebucht wurden`. Genau deshalb bleibt der Punkt fuer harte Inventarfortschreibung weiter gesperrt.

Nicht automatisch promoten
--------------------------

- Rohdatenhinweise wie `D5 produziert +10 Energiezellen/Tag`, `Gesamt Novapolis: -12 Energiezellen Nettoverlust` oder aggregierte Bestandsbehauptungen sind nur Kandidaten.
- Solche Angaben duerfen erst nach Quellabgleich gegen Missionslog, Logistik und betroffene Inventare in SSOT uebernommen werden.
- Der Pilot ist deshalb ein RAW-abgestuetzter Abgleichslauf, kein Freifahrtschein fuer Mengenretcons.

Arbeitsreihenfolge fuer den Pilot
---------------------------------

1. Baseline sichern
   - Aktuelle drei Zielinventare unveraendert lesen und die vorhandenen Punkte nach `verbucht`, `potenzial`, `offen` clustern.
  - Offene Stellen markieren, an denen bereits ein Szenen-, Missions- oder RAW/Staging-Anker existiert.
2. C6 zuerst schaerfen
   - C6 als Engpass-Ort behandeln; kritische Gueter aus `scene-2026-01-16-a.md` priorisieren.
   - Nur Eintraege nachziehen, die bereits als Fund, Prioritaet oder Missionsanker belegt sind.
3. D5 danach abgleichen
   - D5 nur als Hauptbasis/Empfangs- und Werkstattkontext fortschreiben.
   - Keine C6-Bestaende stillschweigend nach D5 kopieren; jede Verschiebung braucht einen expliziten Transferbeleg.
4. Fraktionsaggregat Novapolis zuletzt aktualisieren
   - Das Fraktionsinventar bleibt die aggregierte Sicht aus D5/C6.
   - Nur aggregieren, was in den Teilinventaren oder im Missionslog belastbar ist.
5. Bewegungslog ergaenzen
   - Jede neue Verbuchung braucht mindestens Quelle, Status und letzten Aenderungsanker.

Konkrete Pilot-Items
--------------------

| Prioritaet | Item | Zieldatei | Beleglage |
| --- | --- | --- | --- |
| 1 | Filter | C6-inventar, D5-inventar, Novapolis-inventar | C6-Funde und T0-Lage belegt |
| 1 | Energiezellen | C6-inventar, D5-inventar, Novapolis-inventar | C6-Funde und T0-Lage belegt |
| 1 | Werkzeuge / Mechanik-Werkzeug | C6-inventar, D5-inventar, Novapolis-inventar | D5/C6/Werkstattkontext belegt |
| 2 | Adapter / Fitting (DN60) | C6-inventar, D5-inventar | als kritischer Bedarf belegt |
| 2 | Schweissausruestung (kompakt) | C6-inventar, D5-inventar | als kritischer Bedarf belegt |
| 3 | Hydrofilter-Behaelter (Reserve) | C6-inventar, D5-inventar | Potenzial belegt, Einbindung offen |
| 3 | Kugeln (neu/gebraucht) | Novapolis-inventar | Referenz vorhanden, Mengen weiterhin offen |

Definition of Done fuer heute
-----------------------------

- Die drei Zielinventare sind gegenseitig widerspruchsfrei.
- Alle heute angefassten Items sind auf kanonische Item-Namen aus dem Waren-Index ausgerichtet.
- Neue Eintraege nennen mindestens Status und Belegquelle.
- Unbelegte Mengen bleiben explizit `tbd` statt implizit geraten.
- `novapolis-dev/docs/todo.rp.md` und `novapolis-dev/docs/donelog.md` dokumentieren den Pilot-Lauf.

Zweiter Arbeitsstrang: Skill-Mapping vorbereiten
------------------------------------------------

- Referenzbasis:
  - `novapolis-dev/docs/specs/annotation-spec.md`
  - `novapolis-rp/database-rp/00-admin/AI-Behavior-Mapping.md`
- Start-Scope fuer v1:
  - `reparieren` fuer D5-/Werkstattkontext,
  - `wache` fuer C6-/Sicherheitskontext,
  - `funk` oder `wahrnehmung` fuer Monitoring/Funkscan.
- Heute vorbereiten, noch nicht final entscheiden:
  - zugeordnete Matrix-Dimensionen je Skill,
  - Baseline pro Rolle,
  - ein kleines Beispiel fuer Ronja, Jonas und Kora.

Empfohlene Check-Reihenfolge nach dem Pilot
-------------------------------------------

1. `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/process/rp-inventory-backfill-pilot-2026-03-20.md' 'novapolis-dev/docs/todo.rp.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md'`
2. `& .\.venv\Scripts\python.exe scripts/check_frontmatter.py 'novapolis-dev/docs/process/rp-inventory-backfill-pilot-2026-03-20.md' 'novapolis-dev/docs/todo.rp.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md'`
3. Sobald echte RP-SSOT-Dateien unter `novapolis-rp/database-rp/` angefasst werden: `npm --prefix novapolis-rp/coding/tools/validators run validate:rp`
