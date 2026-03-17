---
stand: 2026-03-17 16:58
update: Dev-Hub-D5 um Migrationsdoku-Drift gegen die aktuelle Board-SSOT erweitert.
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=FAIL; logs-policy=PASS; ruff=FAIL; black=FAIL; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260317_064114.md
---

<!-- markdownlint-disable MD022 MD041 -->

TODO (Novapolis-Dev)
====================

Hinweis
-------

- Dieses Dokument buendelt Aufgaben fuer das Dev-Modul (Tooling, Lint/CI, Validatoren, Doku-Infra).
- RP-Aufgaben liegen in `docs/todo.rp.md`. Agent-Aufgaben liegen in `docs/todo.agent-board.md`.
- Vollstaendig erledigte Bloecke werden nach `novapolis-dev/archive/todo.dev.archive.md` verschoben.

Offene Aufgaben (Dev)
---------------------

- [x] [Jetzt] Full-Gate wieder gruen machen (`ruff`, `black`, `pytest/coverage >= 80`) und den aktuell roten Sammellauf stabilisieren.
  - Akzeptanzkriterium: `scripts/run_checks_and_report.py` liefert `overall=PASS` mit Reportpfad und ohne rote Pflichtchecks.
  - Evidenz: `.tmp/results/reports/checks_report_20260311_072150.md`.
  - Abschluss 2026-03-11: Full-Gate wieder gruen; Coverage-Gate `>=80%` wieder erreicht (aktueller Lauf: `80.45%`).
- [ ] [Jetzt] Coverage-Sprint Richtung `91%` starten (Welle 1: skriptnahe Low-Coverage-Module).
  - Akzeptanzkriterium: Nettoanstieg der Gesamt-Coverage gegen Baseline (`76.24%`) ist messbar dokumentiert und die Wellenplanung fuer die naechsten Hauptluecken steht.
  - Evidenz: neue/erweiterte Tests in `novapolis_agent/tests/scripts/` plus Coverage-Report (`80.45%` nach Welle 1).
- [ ] [Jetzt] Aktive Root-/Dev-Dokuoberflaechen auf den letzten grünen Sammellauf synchronisieren.
  - Akzeptanzkriterium: `README.md`, `novapolis-dev/README.md`, `WORKSPACE_INDEX.md`, `WORKSPACE_STATUS.md`, `todo.root.md` und `novapolis-dev/docs/todo.agent-board.md` tragen keinen veralteten FAIL-Receipt mehr und verweisen konsistent auf den zuletzt belegten aktiven Lauf.
  - Evidenz: `novapolis-dev/docs/todo.index.md` und `novapolis-dev/docs/donelog.md` verweisen bereits auf `checks_report_20260311_072546.md`, waehrend `README.md`, `novapolis-dev/README.md` und `WORKSPACE_INDEX.md` noch `checks_report_20260305_005843.md` und `WORKSPACE_STATUS.md`, `todo.root.md`, `novapolis-dev/docs/todo.agent-board.md` noch `checks_report_20260310_153947.md` tragen.
- [ ] [Als naechstes] VS-Code-Task-Launcher-Drift (`pwsh ... /d /c`, Exit 64) reproduzierbar pruefen und absichern.
  - Akzeptanzkriterium: betroffene Tasks lassen sich im VS-Code-Launcher ohne technischen Wrapper-Fehler starten oder der bekannte Launcher-Grenzfall ist mit belastbarem Workaround in Task/Runbook dokumentiert.
  - Evidenz: `WORKSPACE_STATUS.md` dokumentiert den Launcher-Fehler fuer `Tests: coverage (fail-under)` und `Checks: sim epoch assets` am 2026-03-03 sowie erneut im Wochenabschlussfenster am 2026-03-10.
- [ ] [Als naechstes] Modernes Community-/Maintainer-Doku-Paket ergaenzen (`SUPPORT.md`, Issue-/PR-Templates, `RELEASE.md`, `GOVERNANCE.md` oder `MAINTAINERS.md`).
  - Akzeptanzkriterium: Einstieg, Meldewege und Release-/Maintainer-Prozess sind fuer externe Contributors ohne implizites Wissen auffindbar.
  - Evidenz: neue Dateien unter Root bzw. `.github/` + Verweise in `README.md`.
- [ ] [Als naechstes] ADR-Ordner von "bereit" auf "aktiv genutzt" heben (mind. `ADR-0001`, `ADR-0002`).
  - Akzeptanzkriterium: zentrale Entscheidungen (z. B. DONELOG-Ebenen, Quality-Gate-Sequenz) sind als akzeptierte ADRs dokumentiert.
  - Evidenz: `docs/adr/0001-*.md`, `docs/adr/0002-*.md`.
- [ ] [Als naechstes] Active-Surface-Index auf reale `last_check`-Stände der Governance-Dokumente nachziehen.
  - Akzeptanzkriterium: `novapolis-dev/docs/active-surface-index.md` bildet juengste inhaltliche Pruefungen der aktiven Boards/Logs nachvollziehbar ab und laeuft nicht mehrere Aenderungswellen hinterher.
  - Evidenz: `novapolis-dev/docs/active-surface-index.md` fuehrt fuer `donelog.md`, `todo.index.md`, `todo.dev.md`, `todo.rp.md`, `todo.agent-board.md` und `todo.sim.md` weiterhin `last_check = 2026-03-04`, obwohl diese Oberflaechen im aktuellen Arbeitsfenster mehrfach bis 2026-03-13 mutiert und geprueft wurden.
- [ ] [Als naechstes] Legacy-Metadatei `novapolis-dev/docs/meta/todo.json` auf aktive TODO-SSOT umstellen oder gezielt ausmustern.
  - Akzeptanzkriterium: Metadaten unter `novapolis-dev/docs/meta/**` verweisen nicht mehr auf das entfernte Sammelboard `novapolis-dev/docs/todo.md` und tragen keine irrefuehrende RP-Altzuordnung als aktive Quelle.
  - Evidenz: `novapolis-dev/docs/meta/todo.json` enthaelt aktuell `title = "TODO (Novapolis-RP)"`, `source = "novapolis-dev/docs/todo.md"` und `origin = "novapolis-rp/development/docs/todo.md"`, obwohl die aktive Board-Struktur inzwischen ueber `todo.dev.md`, `todo.rp.md`, `todo.agent-board.md` und `todo.sim.md` laeuft.
- [ ] [Als naechstes] Historische Dev-Migrationsdoku auf die aktive Board-SSOT abgrenzen oder nachziehen.
  - Akzeptanzkriterium: `novapolis-dev/migrations/docs-migration-2025-10-29.md` transportiert keine aktive TODO- oder Index-Struktur mehr, die dem heutigen Split-Board-Modell widerspricht; falls die Datei rein historisch bleiben soll, ist das fuer Leser klar erkennbar.
  - Evidenz: `novapolis-dev/migrations/docs-migration-2025-10-29.md` dokumentiert weiterhin die Migration nach `novapolis-dev/docs/todo.md` und nennt `legacy coding -> todo.md` als Zielpfad, obwohl die aktive TODO-SSOT heute ueber `todo.dev.md`, `todo.rp.md`, `todo.agent-board.md` und `todo.sim.md` laeuft.
- [x] [Jetzt] Punkt-3-Strategie aktivieren: Coverage-Steuerung auf realistische Zielkorridore (`85-90%`) fuer grosse Pfade umstellen und `90%` als verbindliches Qualitaetsziel fest verankern.
  - Akzeptanzkriterium: dokumentierte Gate-Logik mit Hard-Gate (`>=80%`) plus verbindlichem Qualitaetsziel (`>=90%`) inkl. Nachweispflicht bei Unterschreitung.
  - Evidenz: `novapolis-dev/docs/tests.md` (Abschnitte `Gate-Logik` und `Coverage-Strategie`).
- [ ] [Spaeter] Root-Backlog O11 schliessen: externes Beta-Installblatt fuer Dritte erstellen und mit Dev-Hub synchronisieren.
  - Akzeptanzkriterium: ein Dritter kann Setup/Run/Troubleshooting fuer die Standalone-Beta ohne Insiderwissen ausfuehren.
  - Evidenz: neues Installblatt + Referenz in `todo.root.md`.
- [ ] [Spaeter] Cadence-KPI-Review als Trendansicht verankern (nicht nur Einzelwerte je Slot).
  - Akzeptanzkriterium: KPI-Verlauf (4 Kernmetriken) ist fuer mindestens 4 aufeinanderfolgende Slots vergleichbar dokumentiert.
  - Evidenz: KPI-Abschnitt in `novapolis-dev/docs/donelog.md` oder dedizierte Dev-KPI-Uebersicht.

- [x] [Jetzt] Active-Surface-Index fuer `novapolis-dev/docs/**` erstellen (ACTIVE/REFERENCE/HISTORICAL + Owner + last_check).
  - Akzeptanzkriterium: Eine scanbare Uebersicht mit klarer Klassifikation aller aktiven Dev-Dokumente liegt vor.
  - Evidenz: `novapolis-dev/docs/active-surface-index.md`.
- [x] [Jetzt] Truthfulness-Drift in `novapolis-dev/README.md` korrigieren (u. a. `integrations/` nicht mehr als Platzhalter; `roadmaps/` nur bei realem Verzeichnis).
  - Akzeptanzkriterium: Strukturabschnitt beschreibt ausschliesslich den Iststand.
  - Evidenz: `novapolis-dev/README.md` (Struktur/Primary-Docs-Abschnitt).
- [x] [Jetzt] `novapolis-dev/docs/specs/tts-exporter-coqui.md` auf Iststand nachziehen (Platzhalter-Narrativ entfernen, Implementierungsgrad explizit markieren).
  - Akzeptanzkriterium: Keine Widersprueche mehr zwischen Spec, Tasking und Modul-Iststand.
  - Evidenz: `novapolis-dev/docs/specs/tts-exporter-coqui.md` (CLI Iststand + Task-Status).
- [x] [Als naechstes] Donelog-Hygiene einfuehren: aktives Fenster definieren (Current-Window) und aeltere Bloecke sauber ins Historik-Archiv auslagern.
  - Akzeptanzkriterium: `novapolis-dev/docs/donelog.md` bleibt fuer operative Arbeit kurz und scanbar; Historie bleibt erhalten.
  - Evidenz: `novapolis-dev/docs/donelog.md` (Current-Window), `novapolis-dev/archive/docs/donelogs/donelog_dev.window-archive.pre-2026-02-20.md` (Archivfenster).
- [x] [Als naechstes] Logs-Policy fuer `novapolis-dev/logs/` durchsetzen (Umgang mit `*.tmp.md` festlegen und konsistent umsetzen).
  - Akzeptanzkriterium: Keine policy-widrigen Rohlogs im aktiven Log-Pfad oder Policy explizit angepasst und dokumentiert.
  - Evidenz: `scripts/check_logs_policy.py`, `novapolis-dev/logs/README.md`, Verschiebung nach `novapolis-dev/archive/quarantine/logs/`.
- [x] [Als naechstes] Stand-Freshness-SLA festlegen (`ACTIVE <= 14 Tage`, `REFERENCE <= 60 Tage`) und als wiederkehrenden Check im Dev-Modul verankern.
  - Akzeptanzkriterium: Alle aktiven Dev-Dokumente haben frische `stand`-Werte oder dokumentierte Ausnahmen.
  - Evidenz: `scripts/check_doc_freshness.py`, `novapolis-dev/docs/active-surface-index.md`, Integration in `scripts/run_checks_and_report.py`.
- [x] [Spaeter] TODO-Index-Sync automatisiert absichern (Check/Guard: bei Aenderung von `todo.*.md` muss `todo.index.md` im selben Lauf geaendert sein).
  - Akzeptanzkriterium: Drift zwischen Modul-Boards und `todo.index.md` wird technisch verhindert statt nur manuell entdeckt.
  - Evidenz: `scripts/check_todo_index_sync.py`, Integration in `scripts/run_checks_and_report.py`.
- [x] [Spaeter] Woechentliche Hygiene-Cadence etablieren (Drift-Scan, Donelog-Cleanup, TODO/Index-Abgleich) inkl. KPI-Tracking.
  - Akzeptanzkriterium: Fester 60-Minuten-Wochenslot mit dokumentierten KPIs (`todo_index_drift`, `active_docs_stale`, `placeholder_conflicts`, `logs_policy_violations`).
  - Evidenz: `novapolis-dev/docs/process/abschluss-routine.ssot.md` (Abschnitt `Woechentliche Hygiene-Cadence (60 Minuten)` + KPI-Protokollschema).


