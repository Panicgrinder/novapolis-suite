---
stand: 2026-03-27 15:47
update: Letzter Governance-Folgepunkt umgesetzt: Snapshot-/Pre-Commit-Retry-Pfad ist jetzt operativ gehaertet.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '.github/copilot-instructions.md' '.github/copilot-instructions-headings.md' 'novapolis-dev/docs/donelog.md' 'novapolis-dev/docs/todo.dev.md' 'novapolis-dev/docs/todo.index.md' 'DONELOG.md' PASS (2026-03-27 15:47); .\.venv\Scripts\python.exe scripts/check_frontmatter.py '.github/copilot-instructions-headings.md' 'novapolis-dev/docs/donelog.md' 'novapolis-dev/docs/todo.dev.md' 'novapolis-dev/docs/todo.index.md' 'DONELOG.md' PASS (EXITCODE=0, 2026-03-27 15:47); .\.venv\Scripts\python.exe scripts/check_todo_index_sync.py --repo-root . --write-index-meta PASS (2026-03-27 15:47); .\.venv\Scripts\python.exe scripts/check_logs_policy.py --repo-root . PASS (2026-03-27 15:47)
---

<!-- markdownlint-disable MD041 -->

Dev-DONELOG (Current Window)
============================

Hinweis
-------

- Aktives Fenster: nur Eintraege der letzten 14 Tage mit operativer Relevanz.
- Historik bleibt vollstaendig in den Archivdateien unter `novapolis-dev/archive/docs/donelogs/` erhalten.
- Technische Laufdetails gehoeren in Reports unter `.tmp/results/reports/` und werden hier nur zusammengefasst.

Current-Window Eintraege
------------------------

Dev/Governance: Snapshot-/Pre-Commit-Retry-Pfad operativ gehaertet (2026-03-27 15:05)
---------------------------------------------------------------------------------------

- `scripts/pre_commit.py` fuehrt das Snapshot-Gate jetzt erst nach markdownlint, Frontmatter-Validator und optionalen RP-Hard-Gates aus. Damit verbrauchen spaete Hook-Abbrueche oder automatische Markdown-Fixes die Snapshot-Freshness nicht mehr vorzeitig.
- Die dokumentierte Regel `R-SNAP` spiegelt die operative Hook-Reihenfolge jetzt explizit; Governance-Text und Hook-Iststand liegen damit wieder auf derselben technischen Achse.
- Mit diesem Schritt ist der letzte offene Governance-Folgepunkt aus `todo.dev.md` geschlossen. Das Dev-Board steht damit wieder bei `offen: 0`.

Dev/Governance: Python-Workspace-Tasks auf `process` vereinheitlicht (2026-03-27 14:51)
--------------------------------------------------------------------------------------

- In `.vscode/tasks.json` laufen die verbliebenen Python-basierten Tasks jetzt durchgaengig als `process` statt als `shell`; damit faellt der lokale `pwsh /d /c`-Fehlpfad auch fuer Eval-, Daten-, Trainings- und Utility-Tasks weg.
- Bewusst unveraendert blieben nur echte Shell-Aufrufe ueber `pwsh`, etwa fuer `tree`-Erzeugung oder HTTP-basierte TTS-Hilfstasks. Die Ausnahme ist damit technisch begruendet statt historisch gewachsen.
- Der dritte offene Governance-Punkt aus `todo.dev.md` ist damit geschlossen; als letzter offener Dev-Punkt bleibt der operative Snapshot-/Pre-Commit-Retry-Pfad.

Dev/Governance: Kern-Governance auf eine eindeutige Normschicht reduziert (2026-03-27 14:51)
---------------------------------------------------------------------------------------------

- Die Kerndatei `.github/copilot-instructions.md` benennt jetzt die `Regel-ID-Landepunkte (Kern)` explizit als einzige bindende Ebene fuer Runtime-Entscheidungen; der `Regel-ID-Index (Kern)` bleibt Navigation und die `Regelmatrix (Kern)` ist nur noch Kurzreferenz.
- Der bisherige TL;DR-Block wurde von parallel gepflegten Regeltexten auf knappe Verweise pro Regel-ID umgestellt. Damit sinkt die Driftflaeche, ohne dass operative Orientierung verloren geht.
- Der Headings-Index spiegelt die neue Normschichtung mit; damit ist der zweite offene Governance-Punkt aus `todo.dev.md` geschlossen und als naechster Dev-Punkt bleibt die systematische Task-Umstellung von `shell` auf `process` offen.

Dev/Governance: Quellenstand von Kern-SSOT und Headings-Index wieder zusammengezogen (2026-03-27 14:41)
-------------------------------------------------------------------------------------------------------

- `.github/copilot-instructions.md` und `.github/copilot-instructions-headings.md` verweisen jetzt wieder auf denselben aktuellen Governance-Zeitanker; der Drift lag nur noch in Kopf-/Quellenmetadaten, nicht in der eigentlichen Abschnittsstruktur.
- Die Abschnittsliste des Headings-Index blieb inhaltlich tragfaehig; nachgezogen wurden daher bewusst nur Quellenstand, Update-/Check-Hinweise und der zugehoerige Dev-Board-/Index-Sync.
- Damit ist der erste offene Governance-Punkt aus `todo.dev.md` geschlossen; der naechste offene Dev-Punkt bleibt die Redundanzreduktion in der Kern-Governance.

Dev/Governance: Review auf Aktualitaet, Redundanz und Verbesserungspotential in Board-Folgearbeit ueberfuehrt (2026-03-27 14:32)
------------------------------------------------------------------------------------------------------------------------

- Der Review bestaetigt keinen akuten Governance-Bruch mehr, aber vier klare Folgeachsen: Die Kern-SSOT und ihr Headings-Index sind metadatenmaessig hinter dem echten Regelstand, zentrale Regeln liegen redundant auf mehreren Ebenen, ein Teil der Python-Workspace-Tasks laeuft weiter als `shell`, und der Snapshot-Retry-Pfad ist zwar jetzt sauber dokumentiert, operativ aber noch nicht robust genug.
- Diese Befunde sind jetzt als konkrete Dev-Punkte im offiziellen Board verankert: Quellenstand/Headings-Index angleichen, Kern-Governance auf eine normative Hauptebene reduzieren, verbleibende Python-Tasks auf `process` pruefen und den Snapshot-/Pre-Commit-Retry-Pfad technisch haerten.
- Der Index wurde im selben Lauf auf den neuen Dev-Open-Count und den aeltesten offenen Governance-Punkt synchronisiert.

Dev/Governance: Finaler Snapshot-Sync fuer den Commitlauf gezogen (2026-03-27 14:22)
------------------------------------------------------------------------------------

- Vor dem Commit wurde der Snapshot-Lock erneut frisch gesetzt und die aktiven `stand`-Felder auf denselben Zeitanker synchronisiert, damit der zuvor dokumentierte Governance-Fix nicht selbst wieder am Freshness-Gate scheitert.
- Der Lauf ist inhaltlich unveraendert gegenueber 10:33; es handelt sich um den technischen Commit-/Push-Sync fuer denselben Governance-Fixblock.

Dev/Governance: Snapshot-Retry-Pfad und Python-Tasks gegen Hook-/Workspace-Iststand gehaertet (2026-03-27 10:33)
--------------------------------------------------------------------------------------------------------------

- `R-SNAP` nennt jetzt explizit das praktische Gate-Verhalten fuer Retry-Faelle: `stand` muss frisch zu `now` bleiben, der Lock ebenfalls, und ein nach Hook-Abbruch wiederholter Commit beginnt wieder bei Snapshot-Lock plus `stand`-Sync statt mit altem Lock weiterzulaufen.
- Die Markdown-Instructions dokumentieren die kanonische Einzelausnahme fuer `.github/copilot-instructions.md` jetzt konsistent, damit die historische Kopfzeilenform `Stand:`/`Checks:` nicht mehr im Konflikt mit der allgemeinen Legacy-Kopfzeilenregel steht.
- Die betroffenen Python-Workspace-Tasks (`coverage`, `todo index sync`, `logs policy` und verwandte Checks) laufen jetzt als `process` statt `shell`; damit faellt der lokale `pwsh /d /c`-Fehlpfad weg, der die eigentlichen Python-Checks zuvor faelschlich rot machte.

RP/Inventory: RAW-Rettungsstand vor Handverteilung und Verbrauchsrechnung festgezogen (2026-03-27 09:46)
------------------------------------------------------------------------------------------------------

- Der offizielle RP-Backlog haelt jetzt explizit fest, was aus RAW vor manueller Fraktionsverteilung noch belastbar gerettet werden kann: quantifizierter C6-Startsnapshot, teilquantifizierter D5-Startanker, generischer Transferpfad `D5 -> C6`, semiformeller C6-Zielanker sowie einzelne Energie- und Materialdeltas.
- Ebenso ist jetzt getrennt dokumentiert, was nur weich rettbar bleibt: Rollen-, Freigabe- und Prozesslogik fuer D5/C6/Novapolis.
- Weiterhin manuell zu setzen bleiben aktuelle Fraktionssummen, standortscharfe Restbestaende, mehrtaegige Verbrauchsreihen und konkrete Transfermengen pro Lauf; genau dafuer wurde ein erneuter Sicherheits-Recheck ueber die RAW-Daten gestartet.

RP/Inventory: C6-Zielanker fuer den D5-Materiallauf auf Logistiksystem-Ebene geschaerft (2026-03-27 08:33)
-------------------------------------------------------------------------------------------------------

- `logistik_novapolis_v2` fuehrt den Lauf `D5 -> C6 (Bauteile, Werkzeuge, Versorgungsgueter)` jetzt als explizite aktive Fracht; zusammen mit Chat-RAW ist der Materiallauf damit nicht nur erzählerisch, sondern auch systemisch gerahmt.
- `logistik_c6_v2` liefert fuer C6 mit `Primaerlager (Bereich 3)` und `Sekundaerlager (Kontrollraum)` den vorhandenen Lagerrahmen, ohne aber den konkreten Lauf dort als Charge oder Inventarlog-Zeile einzubuchen.
- Als konservative Definition bleibt deshalb nur ein `missionierter Versorgungslauf D5 -> C6 mit bestaetigtem Empfang, Bestandsaufnahme und anschliessender Baustellenverteilung`; Mengen, konkrete Lagerzuordnung und Quittung wurden bewusst nicht promoted.

RP/Inventory: C6-Zielseite fuer den D5-Materiallauf gegen RAW nachgeschaerft (2026-03-27 08:29)
---------------------------------------------------------------------------------------------

- Chat-RAW belegt jetzt auf der C6-Seite nicht nur `Ankunft` und `Bestandsaufnahme`, sondern auch den expliziten Schritt, dass `der Empfang der Ware bestaetigt werden` muss; anschliessend soll die Ware zusammen mit weiterer D5-Fracht an die Baustellen gebracht werden.
- Damit ist die Zielseite des Laufs enger auf `bestaetigter Empfang in C6 mit operativer Weiterverteilung` rahmbar; `C6-Schleuse` und `C6-Lagerhalle` liefern dafuer den passenden Prozessrahmen, aber weiterhin keinen konkreten Logeintrag.
- Weil weiter keine explizite Schleusen-/Lagerbuchung, keine Charge und keine saubere Quittungszeile im Inventarlog vorliegen, wurde bewusst keine neue Inventarmenge promoted.

RP/Inventory: D5-Quellorte fuer den C6-Materiallauf gegen RAW nachgeschaerft (2026-03-27 08:25)
---------------------------------------------------------------------------------------------

- `RAW-canvas-2025-10-20T12-05-00-000Z` belegt in D5 ein Materiallager unter dem Bahnsteig mit Lastenaufzug und Nutzung fuer Schwerlast, Rohstahl, Kabeltrommeln und Energiezellenpaletten; damit ist erstmals ein konkreter physischer Quellort fuer den Materiallauf greifbar.
- `Draisine-Transportmodul.md` plus Chat-RAW belegen parallel Werkstattbestand, Materiallauf-Unterstuetzung und den Fokus von Jonas, Pahl und Lumen auf den Transportpfad; dadurch ist der Ursprung des Laufs enger auf `Materiallager und/oder Werkstattbestand D5` rahmbar.
- Weil weiterhin keine explizite Entnahmebuchung, keine standortscharfe C6-Zielbuchung und keine Quittung/Verantwortlichenzeile vorliegen, wurde bewusst keine neue Inventarmenge promoted.

RP/Inventory: D5->C6-Transferkette erneut gegen Umfeld und RAW geprueft (2026-03-27 08:14)
----------------------------------------------------------------------------------------

- Der Recheck bestaetigt den generischen Transportanker im RAW-Logistikcanvas `RAW-canvas-2025-10-16T13-05-00-000Z`: `D5 -> C6 (Bauteile, Werkzeuge, Versorgungsgueter)` bei manuellem Transport ohne Bahnverbindung.
- Im Chat-RAW sind fuer denselben Ablauf lediglich `Abmeldung in D5` sowie anschliessend `Ankunft` und `Bestandsaufnahme` in C6 hart sichtbar; das reicht fuer Prozessrahmen, aber nicht fuer Bestandsbuchung.
- Weil weiterhin keine explizite Entnahme, keine Zielbuchung in `C6-Schleuse` oder `C6-Lagerhalle` und keine Quittung/Verantwortlichen belegt sind, bleibt der RP-Punkt offen und es wurde bewusst keine Fraktionssumme oder Item-Menge promoted.

Dev/Backlog: Folgepunkte nach Wochenabschluss konkretisiert (2026-03-27 04:34)
-------------------------------------------------------------------------

- `todo.rp.md` fuehrt den verbleibenden Inventar-Backfill jetzt nicht mehr nur als Sammelpunkt, sondern getrennt nach Transferkette `D5 -> C6`, Delta-Struktur fuer `Novapolis-inventar.md` und Realabgleich fuer das Skill-Mapping-V1.
- `todo.sim.md` enthaelt erstmals einen aktiven Punkt fuer die beiden bekannten Sim-Asset-Warnungen aus dem Wochenabschluss (`summary=fail:0,warn:2`), statt sie nur im Kontexttext zu nennen.
- `todo.dev.md` fuehrt den sichtbaren Drift in den Board-Metadaten von `todo.index.md` als eigenen Hygiene-Punkt; `todo.root.md` und `todo.index.md` sind auf denselben Folgebacklog synchronisiert.

Dev/Process: Wochenabschluss 2026-03-27 komplett abgeschlossen (2026-03-27 01:16)
-------------------------------------------------------------------------------

- `scripts/run_checks_and_report.py` liefert nach dem Doku-Refresh wieder `overall=PASS`; Coverage bleibt bei `93.69%`, alle Governance-Gates sind gruen, und der Reportpfad ist `.tmp/results/reports/checks_report_20260327_011507.md`.
- Die beiden stale ACTIVE-Boards `todo.agent-board.md` und `todo.sim.md` wurden im selben Slot aufgefrischt; damit stehen `todo_index_drift=0`, `active_docs_stale=0`, `placeholder_conflicts=0` und `logs_policy_violations=0` wieder konsistent im KPI-Block.
- Der separate Coverage-Lauf endet mit Exit `0`; `scripts/check_sim_epoch_assets.py --repo-root . --allow-empty --check-slot-consistency` bleibt ohne harte Fehler (`summary=fail:0,warn:2`).

RP/Inventory Governance: Ebenenmodell und Pflicht-Deltas fuer Metro-Warenbestand festgezogen (2026-03-20 13:51)
---------------------------------------------------------------------------------------------------------------

- `todo.rp.md` fuehrt jetzt die feste Promotionskette `Charakter -> Team/POI -> Station -> Fraktion -> Metro`, abgeleitet aus den bereits vorhandenen RP-Artefakten statt aus einem neuen Parallelsystem.
- Die Pflichtartefakte je Ebene sind explizit benannt: Charakter-Canvas, POI-/Lokations-Canvas, Stationsinventar, Fraktionsinventar sowie die Admin-Ebene fuer Metro/T0.
- Neue Bestandsfortschreibung soll ab jetzt nur noch ueber die vier Minimal-Deltas `Transfer`, `Verbrauch`, `Handel` und `Bilanz` nach oben promoted werden.

RP/Inventory: Materiallauf in D5 und C6 standortscharf nachgezogen (2026-03-20 11:49)
-------------------------------------------------------------------------------

- D5 und C6 fuehren den missionierten Materiallauf jetzt beide als lokalen Review-Anker, damit die Luecke nicht nur im Fraktionsinventar haengt.
- D5 dokumentiert den fehlenden Quellabgang, C6 die fehlende Zielbuchung in Lagerhalle/Schleuse.
- Mengen, Charges und Quittungen bleiben weiterhin offen; es wurde nichts neu quantifiziert.

RP/Inventory: Guetermission D5 -> C6 als Transferanker verankert (2026-03-20 11:40)
-------------------------------------------------------------------------------

- Das aktive Missionslog fuehrt jetzt einen eigenen Anker fuer den Materiallauf `D5 -> C6`; belegt sind Richtung, Zweck und der fehlende Stuecklistenentscheid vor dem Lauf.
- Im Fraktionsinventar ist damit die Transportrichtung nicht mehr nur implizit aus RAW ableitbar, sondern im aktiven SSOT benannt.
- Offen bleibt weiterhin die Item-Kette `Entnahme -> Transport -> Ankunft -> Quittung`; deshalb wurde keine harte Fraktionssumme promoted.

RP/Inventory: Transfer- und Verbrauchskette fuer Novapolis geprueft (2026-03-20 11:33)
--------------------------------------------------------------------------------------

- Belegt sind jetzt drei harte Anker fuer den Backfill: D5-Startsnapshot, quantifizierter C6-Startsnapshot und der Tagesabschluss Tag 12 -> 13 mit Energie- und Materialdelta.
- Ebenfalls belegt ist eine generische Logistikrichtung aus `logistik_novapolis_v2`: `D5 -> C6 (Bauteile, Werkzeuge, Versorgungsgueter)` sowie `C6 -> D5 (Materialrueckfuehrung)`.
- Nicht belegt ist weiter die vollstaendige Item-Kette `Entnahme -> Transport -> Ankunft -> Quittung`; genau diese Luecke verhindert weiterhin eine harte Fraktionssumme in `Novapolis-inventar`.

RP/Inventory: D5-Startsnapshot aus RAW als Stationsanker nachgezogen (2026-03-20 07:22)
-------------------------------------------------------------------------------------

- `RAW-canvas-2025-10-16T12-00-00-000Z` belegt fuer D5 ein fruehes Stationsinventar mit `Union-Kisten (3)`, Ersatzrohren/Ventilkomponenten, defekter Reparaturstation und zu `60 %` lesbaren Schaltplaenen.
- Der Befund ist stark genug fuer einen lokalen D5-Startanker und einen vorsichtigen Hinweis im Fraktionsinventar, aber nicht fuer aktuelle Summen ohne spaetere Transfer-/Verbrauchskette.
- Der bisherige PoD-Mangel bleibt bestehen; missionierte Zustellungen oder spaetere Umbuchungen wurden weiterhin nicht frei erfunden.

RP/Inventory: C6-Startsnapshot mit Stückzahlen aus RAW/Staging nachgezogen (2026-03-20 07:14)
-------------------------------------------------------------------------------------------

- `inventar_c6_v2` und `logistik_c6_v2` liefern fuer C6 erstmals einen harten Bestandssnapshot mit konkreten Stueckzahlen statt nur Bedarfskategorien.
- Nachgezogen wurden nur datierte C6-Startwerte; D5 und `Novapolis-inventar` bleiben unveraendert, weil kein gleich starker D5-/Aggregatbeleg vorliegt.
- Der Deal-Anker `scene-2026-01-14-b` bleibt fuer Inventarbewegungen weiterhin zu weich, solange PoD, Lieferkette und Abholpunkt nicht belegt sind.

RP/Skills: Skill-Mapping-V1 um zweite Referenzreihe erweitert (2026-03-20 07:08)
-----------------------------------------------------------------------------

- `annotation-spec.md` fuehrt jetzt zusaetzliche V1-Beispiele fuer `Pahl`, `Reflex`, `Lumen` und `Echo`, gestuetzt auf Personenindex, Charakterblaetter und Behavior-Register.
- `Pahl` bleibt trotz Sicherheitsfreigaben konservativ im Rollenfit `wartung_technik`; `Reflex` und `Echo` werden als `sicherung_monitoring`, `Lumen` als `wartung_technik` gelesen.
- Der Ausbau verbreitert die Referenzbasis, ohne neue Rollen-Baselines, Modifier-Logik oder persistente Charakter-Skillwerte einzufuehren.

RP/Skills: Skill-Mapping-V1 aus Verhaltensmatrix verankert (2026-03-20 06:59)
--------------------------------------------------------------------------

- `annotation-spec.md` enthaelt jetzt eine konservative Novapolis-V1 fuer `reparieren`, `wache`, `funk` und `wahrnehmung` mit Rollen-Baselines fuer `wartung_technik`, `stationsleitung` und `sicherung_monitoring`.
- Die V1 bleibt absichtlich klein: keine zweite Wahrheit in Charakterdateien, keine direkte Modifier-Verrechnung, keine versteckten Progressionsboni.
- Beispielableitungen fuer Ronja, Jonas und Kora sind im Spec ergänzt und schliessen den offenen RP-TODO-Block zu Skill-Gewichten/Formelbeispielen.

RP/Inventory: Material-Backfill Tag 12->13 fuer Tunnelarbeiten eingetragen (2026-03-20 06:52)
--------------------------------------------------------------------------------------------

- Aus Staging wurde nur der belegte Verbrauch uebernommen: `1,3 t Baustoffe`, `120 m Schienenprofil`, `18 m² Betonplatten` sowie `2` beschaedigte Werkzeuge.
- Die Tagesabrechnung liefert keine belastbare D5/C6-Aufteilung dieser Entnahmen; deshalb bleibt die Standortzuordnung offen und wird nur als gemeinsames Delta gefuehrt.
- Es wurden keine Restbestände retconnt; Material- und Werkzeugrestmengen bleiben bis zu belegten Vor-/Nachher-Staenden `tbd`.

RP/Inventory: Energie-Backfill Tag 12->13 fuer D5/C6/Novapolis eingetragen (2026-03-20 06:45)
--------------------------------------------------------------------------------------------

- Aus RAW/Staging plus Logistik-Modell wurde nur die belegte Energiebilanz uebernommen: D5 `+10 Produktion / -8 Grundlast / -12 Export`, C6 `+12 Verbrauch / +10 Zufuhr`, Fraktion gesamt `-12 Netto`.
- Absolute Speicher- oder Startmengen wurden bewusst nicht retconnt; diese bleiben bis zu belastbaren Vor-/Nachher-Staenden offen.
- Materialverbrauch und Werkzeugschaden aus demselben Lauf bleiben vorerst im Log-/Backfill-Kontext und werden nicht als absolute Inventarmenge promoted.

RP/Inventory: Erster konservativer D5/C6/Novapolis-Abgleich abgeschlossen (2026-03-20 06:36)
----------------------------------------------------------------------------------------------

- `D5-inventar` fuehrt keine C6-Bestaende mehr als lokale Bestandszeilen; die fruehere Vermischung wurde auf Standortdrift zurueckgebaut.
- `C6-inventar` fuehrt Filter, Energiezellen und Werkzeuge jetzt explizit als lokal belegten Kontext ohne freie Stueckzahlen; `Adapter DN60` und `Schweissausruestung` bleiben Bedarf.
- `Novapolis-inventar` bleibt als konservatives Aggregat offen fuer spaetere Mengen-/Transferzeilen statt unbelegte Summen zu behaupten.

RP/Inventory: Erster echter Abgleichslauf fuer D5/C6/Novapolis gestartet (2026-03-20 06:28)
-------------------------------------------------------------------------------

- Der vorbereitete Pilot wurde in den eigentlichen SSOT-Abgleich ueberfuehrt.
- Erster harter Driftpunkt: `D5-inventar` fuehrte C6-Bestaende, obwohl RAW/Staging und die Szenenanker die strikte Standorttrennung verlangen.
- Die drei Zielinventare `D5-inventar`, `C6-inventar` und `Novapolis-inventar` werden jetzt konservativ auf lokale bzw. aggregierte Beleglage zurueckgefuehrt.

RP/Prep: RAW- und Staging-Lage fuer Inventare/Items nachgezogen (2026-03-20 06:21)
-------------------------------------------------------------------------------

- Die erste Pilotfassung war zu stark SSOT-zentriert; der fehlende Schritt "RAW gezielt durchsuchen" wurde explizit nachgezogen.
- Belegte Suchpfade fuer den heutigen Pilot sind jetzt im Arbeitsblatt verankert, insbesondere `database-raw/99-exports/chat-export*.txt` sowie die kuratierten Staging-Artefakte `chat-export-complete.finalgate.md` und `chat-export (1).review.md`.
- Ergebnis: Der Mengen-Backfill ist jetzt als RAW-abgestuetzter Abgleichslauf dokumentiert, nicht nur als Fortschreibung aus bestehender SSOT.

RP/Prep: Pilotpaket fuer D5/C6/Novapolis-Backfill vorbereitet (2026-03-20 06:12)
-------------------------------------------------------------------------------

- Neues Arbeitsblatt `novapolis-dev/docs/process/rp-inventory-backfill-pilot-2026-03-20.md` angelegt.
- Der heutige Start-Scope ist damit explizit auf `D5-inventar`, `C6-inventar` und `Novapolis-inventar` begrenzt; Guardrails und Belegquellen sind vorab benannt.
- `novapolis-dev/docs/todo.rp.md` und `novapolis-dev/docs/todo.index.md` wurden auf diesen vorbereiteten Pilot-Scope synchronisiert.

Dev/KPI: Trendansicht fuer Hygiene-Cadence verankert (2026-03-19 11:01)
-----------------------------------------------------------------------

- `novapolis-dev/docs/meta/dev-kpi-trends.md` angelegt und die vier Kernmetriken (`todo_index_drift`, `active_docs_stale`, `placeholder_conflicts`, `logs_policy_violations`) ueber vier dokumentierte Slots vergleichbar zusammengefuehrt.
- Der aktuelle Slot 2026-03-19 ist direkt ueber `scripts/check_todo_index_sync.py`, `scripts/check_doc_freshness.py` und `scripts/check_logs_policy.py` belegt; offene Placeholder-/Truthfulness-Konflikte im aktiven Dev-Bestand wurden zusaetzlich gegengeprueft.
- `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.index.md` auf `Dev offen: 0` synchronisiert.

Dev/Beta: Externes Installblatt fuer die Standalone-Beta angelegt (2026-03-18 22:47)
-------------------------------------------------------------------------------

- `novapolis-dev/docs/process/standalone-beta-installblatt.md` neu angelegt; der Text richtet sich explizit an Dritte ohne implizites Repo-Wissen.
- Abgedeckt sind Voraussetzungen, Setup, API-/Sim-Start, Verifikation, Go/No-Go und Troubleshooting.
- `README.md`, `todo.root.md`, `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.index.md` auf den geschlossenen O11-Stand synchronisiert.

Dev/Community: Maintainer- und Contributor-Paket aufgebaut (2026-03-18 22:40)
-------------------------------------------------------------------------

- Root-Docs `SUPPORT.md`, `RELEASE.md` und `MAINTAINERS.md` als scanbare Einstiegsschicht fuer Support, Release-Rahmen und Verantwortlichkeiten angelegt.
- Root-GitHub-Templates unter `.github/ISSUE_TEMPLATE/` sowie `.github/pull_request_template.md` ergaenzt.
- `README.md`, `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.index.md` auf den neuen Iststand synchronisiert; Dev-Open-Count reduziert sich auf `2`.

Dev/Architecture: ADR-Ordner aktiviert (2026-03-18 22:36)
---------------------------------------------------------

- `docs/adr/0001-donelog-ebenen.md` als akzeptierte Entscheidung fuer die normalisierten DONELOG-Ebenen angelegt.
- `docs/adr/0002-quality-gate-sequenz.md` als akzeptierte Entscheidung fuer die verbindliche Reihenfolge `Lint -> Typen -> Tests -> Coverage` und die Coverage-Zweistufenlogik angelegt.
- `docs/adr/README.md` um einen aktiven ADR-Index erweitert; `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.index.md` auf `Dev offen: 3` synchronisiert.

Dev/Governance: Status- und Board-Sync auf PASS-Referenzlauf gezogen (2026-03-18 22:20)
-------------------------------------------------------------------------------

- `WORKSPACE_STATUS.md`, `todo.root.md`, `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.index.md` vom veralteten 2026-03-10/11-Stand auf den dokumentierten PASS-Lauf `checks_report_20260318_052318.md` gehoben.
- Der Dev-Punkt `Coverage-Sprint Richtung 91%` wurde evidenzbasiert abgeschlossen; der aktuelle Referenzwert liegt bei `93.69%` statt der zuvor noch gefuehrten Zwischenmarke `80.45%`.
- Open-Count im Dev-Board/Index reduziert (`5 -> 4`); naechster offener Dev-Schwerpunkt ist jetzt das Community-/Maintainer-Doku-Paket.

Dev/Docs: RP-Brainstorming archiviert, ACTIVE-Oberflaeche bereinigt (2026-03-18 05:20)
-------------------------------------------------------------------------------

- `novapolis-dev/docs/brainstorming.rp.md` aus dem aktiven Dev-Bestand entfernt und nach `novapolis-dev/archive/docs/others/brainstorming.rp.archive.2026-03-18.md` ueberfuehrt.
- `novapolis-dev/docs/active-surface-index.md` auf den neuen Ist-Stand synchronisiert; der RP-Brainstorming-Eintrag zaehlt nicht mehr zur ACTIVE-Oberflaeche.
- `.github/instructions/mind-cluster.instructions.md` vom toten Aktivpfad bereinigt; Brainstorming-Regel bleibt generisch fuer kuenftige aktive Brainstorming-Dokumente bestehen.

Dev/Quality: Full-Gate wieder gruen + Coverage-Welle 1 gestartet (2026-03-11 07:24)
-------------------------------------------------------------------------------

- `scripts/run_checks_and_report.py` liefert wieder `overall=PASS` (inkl. `ruff`, `black`, `pyright`, `mypy`, `pytest`, Coverage-Gate `>=80%`).
- Coverage-Anstieg fuer den 91%-Pfad gestartet: Baseline `76.24%` auf `80.45%` angehoben.
- Testausbau in `novapolis_agent/tests/scripts/` begonnen (u. a. `test_build_project_context_index.py`, Erweiterungen in `test_summarize_marathon_kpis.py`, `test_build_eval_from_rp.py`, `test_check_dependency_profiles.py`).

Dev/Tests: Punkt 3 aktiviert, 90%-Ziel verankert (2026-03-11 07:07)
--------------------------------------------------------------------

- `novapolis-dev/docs/tests.md` von Alt-Prequel-Notizen auf aktuelle Test-/Coverage-Governance umgestellt (Hard Gate `>=80%`, verbindliches Qualitaetsziel `>=90%`, selektive `100%` nur fuer kleine kritische Module).
- `novapolis-dev/docs/process/abschluss-routine.ssot.md` um verbindliche Coverage-Zweistufenlogik erweitert und Nachweispflicht bei `<90%` fixiert.
- `novapolis-dev/docs/todo.dev.md` um einen abgeschlossenen Punkt-3-Eintrag ergaenzt; `novapolis-dev/docs/todo.index.md` auf den neuen Statushinweis synchronisiert.

Dev/Qualitaet: Folgezyklus gestartet, Punkt 1 begonnen (2026-03-11 06:57)
--------------------------------------------------------------------------

- `novapolis-dev/docs/todo.dev.md` um neue offene Optimierungspunkte erweitert (Gate-Stabilisierung, modernes Doku-Paket, ADR-Aktivierung, O11-Installblatt, KPI-Trendansicht).
- Punkt 1 aktiv gestartet: Ruff/Black-Restbefunde aus dem letzten Sammellauf in `scripts/check_todo_index_sync.py`, `novapolis_agent/scripts/build_eval_from_rp.py`, `novapolis_agent/scripts/summarize_marathon_kpis.py` und `novapolis_agent/tests/scripts/test_prepare_pack_smoke.py` behoben.
- Zwischenstand Coverage: Lint/Format sind fuer den betroffenen Scope gruen, Full-Gate bleibt wegen Coverage-Abstand (`76.24%` bei Ziel `>=80%`) offen.

Dev/Process: Woechentliche Hygiene-Cadence verankert (2026-03-11 06:49)
-----------------------------------------------------------------------

- Offener Dev-Board-Punkt abgeschlossen: 60-Minuten-Wochenslot fuer Drift-Scan, Donelog-Cleanup und TODO/Index-Abgleich verbindlich in `novapolis-dev/docs/process/abschluss-routine.ssot.md` dokumentiert.
- KPI-Protokollschema fixiert (`todo_index_drift`, `active_docs_stale`, `placeholder_conflicts`, `logs_policy_violations`) und Nachweisziel auf `novapolis-dev/docs/donelog.md` plus Root-Summary bei Abweichungen festgelegt.
- `novapolis-dev/docs/todo.index.md` auf `Dev offen: 0` und Metadaten (`keiner (offen: 0)`) synchronisiert.

Dev/Tooling: TODO-Index-CLI Rueckwaertskompatibel (2026-03-11 06:43)
---------------------------------------------------------------------

- `scripts/check_todo_index_sync.py` unterstuetzt wieder legacy Aufrufe mit `--root` (Alias auf `--repo-root`) und akzeptiert `--strict` als Deprecated-Noop.
- Ziel: Bestehende Wrapper-/Task-Aufrufe bleiben lauffaehig, waehrend die neue CLI (`--repo-root`, `--write-index-meta`) aktiv bleibt.

Dev/Docs: Receipt-Hygiene fuer Governance-Dokus finalisiert (2026-03-11 04:49)
------------------------------------------------------------------------

- `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CHANGELOG.md`, `docs/adr/README.md` von temporaeren `checks: pending`-Markern auf echte Receipt-Zeilen umgestellt.
- `novapolis-dev/docs/donelog.md` Frontmatter auf denselben Lauf synchronisiert.
- Ergebnis: aktive Governance-Dokumente sind jetzt konsistent mit den laufenden Markdown-/Frontmatter-Gates.

Dev/Docs: README-Kompaktmodus + TODO-Index-Autowrite (2026-03-11 05:12)
------------------------------------------------------------------------

- `README.md` und `novapolis-dev/README.md` auf aktive Leseoberflaeche gestrafft; historische/temporäre Details explizit auf Archiv-/Statusquellen verwiesen.
- `scripts/check_todo_index_sync.py` um Auto-Write erweitert (`--write-index-meta`): Open-Counts und Board-Metadaten in `novapolis-dev/docs/todo.index.md` werden jetzt automatisch synchronisiert.
- Integration nachgezogen: `scripts/run_checks_and_report.py` und Task `Checks: todo index sync` verwenden den Auto-Write-Flag.
- Ergebnis: weniger manuelle Indexpflege und schnellere Onboarding-Lesbarkeit in den Haupt-READMEs.

Dev/Docs: Optimierungsbatch Aktiv-vs-Archiv + TODO-Konsistenz (2026-03-11 03:58)
-------------------------------------------------------------------------------

- `novapolis-dev/docs/todo.sim.md`: verbleibende offene Referenz-Checkbox (`scheduler-spec`) auf erledigt gesetzt; Sim-Board damit konsistent auf `offen: 0`.
- `novapolis-dev/docs/todo.index.md`: Sim-Open-Count von `1` auf `0` synchronisiert und Statushinweis `Sim v5.0` ergänzt.
- `README.md`: Archivregeln praezisiert (zentrales Dev-Archiv als Doku-SSOT; modulinterne Archive nur fuer technische/operative Artefakte).

Dev/Docs: Informationsarchitektur-Runde v2 (2026-03-11 04:27)
--------------------------------------------------------------

- Aktive Oberflaechen entlastet: `todo.sim.md` auf offene Punkte + Kurzkontext reduziert.
- TODO-Index operativ gestrafft: `todo.index.md` auf Kernstatus reduziert und um Board-Metadaten erweitert.
- `scripts/check_todo_index_sync.py` erweitert: Open-Count-Konsistenz, Widerspruchserkennung (`keine offenen` bei offenen Checkboxen) und Diagnoseausgaben.
- Archiv-/Log-Matrix in Root-`README.md` und `novapolis-dev/README.md` vereinheitlicht.
- Repo-Standards ergaenzt: `SECURITY.md`, `CODE_OF_CONDUCT.md`, `.github/CODEOWNERS`, `CHANGELOG.md`, `docs/adr/README.md`.

Dev/Docs: Root-DONELOG auf Summary-Ebene normalisiert (2026-03-11 04:46)
-------------------------------------------------------------------------

- `DONELOG.md` wurde auf einen bewusst kurzen Root-Summary-/Release-Log umgestellt.
- Detailhistorie bleibt im Archivpfad `novapolis-dev/archive/docs/donelogs/donelog_root.md` erhalten.
- Ziel: niedrigere kognitive Last auf Root-Ebene bei unveraenderter Nachvollziehbarkeit.

Dev/Docs: README-Finish fuer aktive Lesbarkeit (2026-03-11 04:46)
------------------------------------------------------------------

- Root-`README.md` um explizite Verweise auf `SECURITY.md`, `CODE_OF_CONDUCT.md`, `.github/CODEOWNERS`, `CHANGELOG.md` und `docs/adr/` ergaenzt.
- `novapolis-dev/README.md` von einem veralteten, ausserhalb des Frontmatters stehenden Checks-Receipt bereinigt und den Abschnitt `Checks & Reports` auf einen stabilen Dauertext umgestellt.
- Ergebnis: weniger Betriebsrauschen in aktiven READMEs und klarere Onboarding-Fuehrung fuer Maintainer/Contributors.

Archivhinweis
-------------

- Aeltere Current-Window-Eintraege bleiben unveraendert in Git-Historie und den Donelog-Archiven.
- Dieses aktive Dokument wird bewusst kurz gehalten und dient als menschlich lesbare Entscheidungs- und Fortschrittsansicht.
