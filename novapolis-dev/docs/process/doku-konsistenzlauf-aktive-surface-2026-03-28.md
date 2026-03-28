---
stand: 2026-03-28 06:53
update: Geplanter Konsistenzlauf fuer Hochfrequenz-Dateien und aktive Doku vor dem eigentlichen Arbeitsbeginn als Phasenplan dokumentiert.
checks: markdownlint PASS; frontmatter PASS; todo-index PASS; logs-policy PASS (2026-03-28 00:43)
---

Doku-Konsistenzlauf: Aktive Surface und Hochfrequenz-Dateien (2026-03-28)
==========================================================================

Ziel
----

- Vor dem eigentlichen Durchlauf den Scope, den Stilrahmen und die Reihenfolge fuer einen konsistenten Doku-Review explizit festhalten.
- Zuerst die am haeufigsten genutzten Einstiegspunkte stabilisieren, danach die restliche aktive Doku im selben Stilrahmen nachziehen.

Scope
-----

- Hochfrequenz-Dateien im aktiven Reader-Surface:
  - `README.md`
  - `WORKSPACE_INDEX.md`
  - `WORKSPACE_STATUS.md`
  - `todo.root.md`
  - `novapolis-dev/README.md`
  - `novapolis_agent/README.md`
  - `novapolis-rp/README.md`
  - `novapolis-sim/README.md`
  - `novapolis-dev/docs/todo.index.md`
  - aktive Modul-Boards unter `novapolis-dev/docs/todo.*.md`
- Restliche aktive Doku:
  - `novapolis-dev/docs/**`
  - aktive Modul-Doku mit Arbeits- oder Runbook-Charakter unter `novapolis_agent/docs/**`
- Nicht im aktiven Scope:
  - `novapolis-dev/archive/**`
  - Quarantaene-, Snapshot- und Historikpfade, ausser ein aktiver Text verweist falsch auf sie.

Stilrahmen
----------

- Frontmatter bleibt knapp und einheitlich ueber `stand`, `update` und `checks`.
- Kommandos und Setup-Hinweise nutzen portable Repo- oder Root-`.venv`-Pfade statt lokaler Sonderpfade.
- Aktive, historische und quarantänisierte Pfade werden explizit getrennt.
- Modulnamen, Titel, Statushinweise und Board-Begriffe verwenden dieselben Bezeichnungen ueber Root-, Hub- und Modultexte hinweg.
- Truthfulness geht vor Schoenheit: Ein Text gilt nur dann als konsistent, wenn er den realen Betriebszustand korrekt beschreibt.

Phasenplan
----------

1. Referenzrahmen fixieren.
   - Root- und Dev-Board fuehren das Vorhaben mit Ziel, Akzeptanzkriterien und Evidenz.
   - Index und DONELOGs spiegeln den offenen Dev-Punkt vor Start der eigentlichen Umsetzung.
2. Hochfrequenz-Dateien pruefen.
   - Einstiegspunkte und aktive Reader-Surface auf Titel, Frontmatter, Statusnarrativ, Pfade, Kommandos und aktive Verweise scannen.
   - Nur klare Driftpunkte sammeln; noch keine Breitenreparatur ausser bei offensichtlichen Widerspruechen.
3. Aktive Dev-Doku vereinheitlichen.
   - `novapolis-dev/docs/**` ausser Archivpfaden gegen denselben Stilrahmen pruefen.
   - TODO-/DONELOG-/Index-Relationen und Begriffe fuer aktive vs. historische Doku mitziehen.
4. Modul-Doku nachziehen.
   - Arbeits- und Runbook-Dokumente unter `novapolis_agent/docs/**` und README-nahe Modultexte auf dieselben Stilentscheidungen ziehen.
   - Modul-spezifische Sonderfaelle nur dokumentieren, nicht wegabstrahieren.
5. Abschluss-Quercheck.
   - TODO/DONELOG/Index synchronisieren.
   - Markdownlint, Frontmatter, TODO-Index-Sync und Logs-Policy erneut laufen lassen.

Nicht-Ziele
-----------

- Keine Archivbereinigung als Selbstzweck.
- Keine inhaltlichen Retcons an RP-, Agent- oder Sim-Sachlogik, solange es nur um Stil- und Dokumentkonsistenz geht.
- Keine grossen Strukturumbauten, wenn ein kleiner, lokaler Diff denselben Konsistenzgewinn liefert.

Definition of Done
------------------

- Die Hochfrequenz-Dateien fuehren denselben Stil- und Betriebsrahmen ohne sichtbare Altpfade oder Statuswidersprueche.
- Aktive Doku ist gegen denselben Stilrahmen geprueft; Archive bleiben bewusst aus dem aktiven Scope herausgehalten.
- Alle beruehrten TODO-/DONELOG-/Index-Dateien sind im selben Lauf nachgezogen.
- Die Doku-Gates fuer den jeweiligen Aenderungslauf sind gruen.