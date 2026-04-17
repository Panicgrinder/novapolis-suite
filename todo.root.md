---
stand: 2026-04-17 07:12
update: Der Root-Backlog fuehrt nach dem erneuten Workspace-Scan wieder fuenf suiteweite Folgepunkte; die Modul-Boards werden parallel ebenfalls neu befuellt.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260417_071110.md
---

TODO-Uebersicht (Novapolis Suite)
=================================

Kurzstatus
----------

- Der zuvor aktive Root-Backlog ist vollstaendig abgeschlossen, validiert und in `novapolis-dev/archive/todo.root.archive.md` archiviert.
- Nach dem erneuten Workspace-Scan fuehrt die aktive Root-Datei wieder fuenf neue suiteweite Querschnittspunkte; die Modul-Boards werden parallel ebenfalls neu auf je fuenf Punkte gezogen.
- Die Modul-Boards stehen vor dem Index-Sync nicht mehr bei `0`; Root bleibt weiterhin bewusst ausserhalb dieser Modul-Open-Counts.
- Historische Sammelbasis bleibt `novapolis-dev/archive/todo.root.archive.md`; der fruehere Vollsnapshot unter `novapolis-dev/archive/quarantine/todo-root-snapshot-20260222_1234.md` bleibt zusaetzliche Evidenz.
- Neue Root-Punkte nur anlegen, wenn der Arbeitszuschnitt wirklich suiteweit ist und nicht sauber in Dev, Agent, RP oder Sim gehoert.

Neue Punkte (Backlog)
---------------------

- [ ] [Jetzt] Fail-Forward-Sprache fuer blockierte oder deutlich ueberzogene Plaene als suiteweiten Produktvertrag festziehen.
  - Ziel: Der erste Vertikalslice soll bei blockierten, riskanten oder klar ueberzogenen Spielerplaenen nicht nur implizit robust wirken, sondern dieselbe Recovery-Sprache in Produktmodell, Turn-Budget-SSOT, Agent-Antworten und Sim-Lesart fuehren.
  - Akzeptanzkriterien:
    1) `novapolis-dev/docs/process/text-rpg-turn-budget-model-v1.ssot.md` definiert klare Recovery-Klassen fuer blockiert, teilmoeglich und verschoben,
    2) `text-rpg-pre-rp-product-model-v1.ssot.md`, `text-rpg-product-gate-v1.ssot.md` und `novapolis_agent/docs/runbook.md` verwenden danach dieselben Begriffe,
    3) die Sim-UI-IA fuehrt dieselbe Lesart fuer Rueckmeldung und Folgeschritt ohne Parallelformel,
    4) der Root-Punkt schliesst den in der Produkt-SSOT explizit offenen Rest statt einen neuen Metatext zu erzeugen.
  - Evidenz: `novapolis-dev/docs/process/text-rpg-pre-rp-product-model-v1.ssot.md` fuehrt unter `Restfrage` und `Entscheidungsraster` die Recovery-Sprache fuer blockierte bzw. ueberzogene Plaene weiterhin explizit als offen.

- [ ] [Jetzt] Sichtbare Druck-, Knappheits- und Warnsignale fuer den ersten suiteweiten Vertikalslice zwischen Produktmodell und Sim-UI festziehen.
  - Ziel: Vor weiterem Komfortausbau soll klar sein, welche Drucksignale der Spieler im Hub und im ersten Live-Slice zwingend sehen muss, damit wirtschaftliche Lage, Risiko und Fail-Forward nicht nur in SSOT-Texten bleiben.
  - Akzeptanzkriterien:
    1) `text-rpg-pre-rp-product-model-v1.ssot.md` und `sim-ui-menue-ia.ssot.md` fuehren dieselben Pflichtsignale,
    2) die Signale unterscheiden knapp zwischen Warnung, Knappheit, Ueberzug und stiller Hintergrundlage,
    3) `novapolis-sim/README.md` und der produktive Sim-Pfad verweisen auf dieselbe IA-Lesart,
    4) der Punkt bleibt suiteweit und verteilt sich nicht unkoordiniert auf Root, Sim und Agent.
  - Evidenz: Die Produkt-SSOT fuehrt die konkrete UI-Lesart fuer Drucksignale noch als offenen Rest; die Sim-IA-SSOT beschreibt den Menuebaum, aber nicht dieselbe kanonische Warnsignal-Matrix.

- [ ] [Als naechstes] Eine knappe player-facing Uebergabeformel fuer den ersten aktiven RP-Anschluss hinter `slot 30` kanonisieren.
  - Ziel: Der vorhandene Slice-2-Handover-Vertrag soll nicht nur technisch und intern korrekt sein, sondern auch eine kurze, spielerseitige Produktformel erhalten, die den Wechsel vom Pre-RP-Slice in den RP-Folgeblock lesbar macht.
  - Akzeptanzkriterien:
    1) `text-rpg-pre-rp-product-model-v1.ssot.md`, `text-rpg-slice-2-handover-v1.ssot.md` und der naechste RP-Folgeblock fuehren dieselbe kurze Formel,
    2) die Formulierung bleibt anschlussfaehig an `turn_resume_ready`, Save/Replay und die bestehenden RP-Slots,
    3) Root-, RP- und Agent-Doku fuehren danach keinen zweiten Namen fuer denselben Anschluss,
    4) die Formel ist knapp genug fuer Produkt-Gate, Runbook und Workspace-Status.
  - Evidenz: `text-rpg-pre-rp-product-model-v1.ssot.md` benennt die knappe player-facing Uebergabeformel hinter `slot 30` weiterhin als offenen Rest trotz geschlossenem Handover-Vertrag.

- [ ] [Als naechstes] Ein suiteweites Release-Evidence-Bundle fuer den ersten Vertikalslice aus Produkt-Gate, Referenzfaellen, Export- und Workspace-Belegen zusammenziehen.
  - Ziel: Der Workspace soll fuer den ersten echten Slice nicht nur mehrere gruene Teil-SSOTs besitzen, sondern einen kompakten Freigabepfad, der Root, Dev, Agent, RP und Sim mit denselben Pflichtbelegen zusammenhaelt.
  - Akzeptanzkriterien:
    1) das Bundle referenziert mindestens `Checks: full`, `Checks: text-rpg product gate`, die deterministischen Referenzfaelle, den Sim-Export-Smoke und den aktuellen Workspace-Status,
    2) Root-README, Produkt-Gate-SSOT, Runbook und Sim-Export-SSOT zeigen auf denselben Freigabepfad,
    3) die Belege bleiben reportfaehig und release-tauglich statt nur in mehreren Dokus verteilt,
    4) der Pfad beschreibt klar, welche Teile ohne lokale Modellruntime oder Godot-Export nicht als release-reif gelten.
  - Evidenz: Produkt-Gate, Referenzfaelle, Sim-Export-SSOT und Workspace-Status liegen aktuell als getrennte, funktionierende Teilquellen vor; ein kompakter suiteweiter Release-Bundle-Pfad ist in der aktiven Root-Oberflaeche noch nicht hinterlegt.

- [ ] [Spaeter] Die suiteweite Hygiene-Cadence fuer den jetzt neu geoeffneten April-Arbeitsstand mit frischem KPI-/Board-Refill wieder als aktiven Root-Takt verankern.
  - Ziel: Nach dem erneuten Workspace-Scan und der Wiederbefuellung aller Boards soll die naechste Cadence nicht nur implizit aus frueheren Eintraegen folgen, sondern als aktiver suiteweiter Takt fuer KPI- und Boardpflege wieder sichtbar sein.
  - Akzeptanzkriterien:
    1) `abschluss-routine.ssot.md`, `todo.root.md` und `WORKSPACE_STATUS.md` fuehren denselben naechsten Cadence-Rahmen,
    2) die Kennzahlen `todo_index_drift`, `active_docs_stale`, `placeholder_conflicts` und `logs_policy_violations` bleiben explizit an den Root-Takt gebunden,
    3) der neue Takt setzt auf den nach dem Board-Refill realen April-Stand auf,
    4) der Root-Punkt bleibt Metagovernance und wandert nicht in einzelne Modul-Boards ab.
  - Evidenz: Der letzte explizit dokumentierte gruene Hygiene-Cadence-Schnitt im Workspace-Status liegt am 2026-04-08; seither wurden die Boards mehrfach geschlossen und erneut geprueft, aber noch nicht auf einen neuen Root-Takt gezogen.

Hinweise
--------

- Abgeschlossene oder historisierte Root-Bloecke in `novapolis-dev/archive/todo.root.archive.md` verschieben.
- Bei neuen Root-Punkten TODO/DONELOG/WORKSPACE_STATUS und `novapolis-dev/docs/todo.index.md` im selben Lauf synchron halten.






