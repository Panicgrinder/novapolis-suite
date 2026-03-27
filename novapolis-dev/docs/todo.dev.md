---
stand: 2026-03-27 09:54
update: Neue Hygiene-Folgeaufgabe fuer die Board-Metadaten im TODO-Index aus dem aktuellen Iststand abgeleitet; Dev offen 0 -> 1.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260327_011507.md
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

- [ ] [Jetzt] Board-Metadaten im `novapolis-dev/docs/todo.index.md` gegen die aktuellen Board-Staende haerten.
  - Akzeptanzkriterium: `letzte Aenderung`, Open-Counts und `aeltester offener Punkt` spiegeln `todo.dev.md`, `todo.rp.md`, `todo.agent-board.md` und `todo.sim.md` ohne manuelle Nachpflege oder sichtbare Datumsdrift.
  - Evidenz: `novapolis-dev/docs/todo.index.md` zeigt aktuell fuer Agent/Sim/RP noch aeltere `letzte Aenderung`-Werte (`2026-03-11` bzw. `2026-03-05`), obwohl die Boards bereits auf `stand: 2026-03-27 01:16` stehen.

- [x] [Jetzt] Full-Gate wieder gruen machen (`ruff`, `black`, `pytest/coverage >= 80`) und den aktuell roten Sammellauf stabilisieren.
  - Akzeptanzkriterium: `scripts/run_checks_and_report.py` liefert `overall=PASS` mit Reportpfad und ohne rote Pflichtchecks.
  - Evidenz: `.tmp/results/reports/checks_report_20260311_072150.md`.
  - Abschluss 2026-03-11: Full-Gate wieder gruen; Coverage-Gate `>=80%` wieder erreicht (aktueller Lauf: `80.45%`).
- [x] [Jetzt] Coverage-Sprint Richtung `91%` starten (Welle 1: skriptnahe Low-Coverage-Module).
  - Akzeptanzkriterium: Nettoanstieg der Gesamt-Coverage gegen Baseline (`76.24%`) ist messbar dokumentiert und die Wellenplanung fuer die naechsten Hauptluecken steht.
  - Evidenz: neue/erweiterte Tests in `novapolis_agent/tests/scripts/` plus Coverage-Report `.tmp/results/reports/checks_report_20260318_052318.md` (`93.69%`; Uplift gegen Baseline `76.24%`).
  - Abschluss 2026-03-18: Der Welle-1-Scope hat den Zielkorridor bereits ueberschritten; verbleibende Testausbauten laufen nicht mehr als akuter Gate-Blocker, sondern als normale Qualitaetshygiene.
- [x] [Als naechstes] Modernes Community-/Maintainer-Doku-Paket ergaenzen (`SUPPORT.md`, Issue-/PR-Templates, `RELEASE.md`, `GOVERNANCE.md` oder `MAINTAINERS.md`).
  - Akzeptanzkriterium: Einstieg, Meldewege und Release-/Maintainer-Prozess sind fuer externe Contributors ohne implizites Wissen auffindbar.
  - Evidenz: `SUPPORT.md`, `RELEASE.md`, `MAINTAINERS.md`, `.github/ISSUE_TEMPLATE/`, `.github/pull_request_template.md`, `README.md`.
  - Abschluss 2026-03-18: Root-Community-Oberflaeche ist jetzt vollstaendig verlinkt; der naechste offene Dev-Punkt bleibt die KPI-Trendansicht.
- [x] [Als naechstes] ADR-Ordner von "bereit" auf "aktiv genutzt" heben (mind. `ADR-0001`, `ADR-0002`).
  - Akzeptanzkriterium: zentrale Entscheidungen (z. B. DONELOG-Ebenen, Quality-Gate-Sequenz) sind als akzeptierte ADRs dokumentiert.
  - Evidenz: `docs/adr/0001-donelog-ebenen.md`, `docs/adr/0002-quality-gate-sequenz.md`, `docs/adr/README.md`.
  - Abschluss 2026-03-18: Der ADR-Ordner enthaelt jetzt zwei akzeptierte Grundsatzentscheidungen und wird aktiv als Governance-Ablage genutzt.
- [x] [Jetzt] Punkt-3-Strategie aktivieren: Coverage-Steuerung auf realistische Zielkorridore (`85-90%`) fuer grosse Pfade umstellen und `90%` als verbindliches Qualitaetsziel fest verankern.
  - Akzeptanzkriterium: dokumentierte Gate-Logik mit Hard-Gate (`>=80%`) plus verbindlichem Qualitaetsziel (`>=90%`) inkl. Nachweispflicht bei Unterschreitung.
  - Evidenz: `novapolis-dev/docs/tests.md` (Abschnitte `Gate-Logik` und `Coverage-Strategie`).
- [x] [Spaeter] Root-Backlog O11 schliessen: externes Beta-Installblatt fuer Dritte erstellen und mit Dev-Hub synchronisieren.
  - Akzeptanzkriterium: ein Dritter kann Setup/Run/Troubleshooting fuer die Standalone-Beta ohne Insiderwissen ausfuehren.
  - Evidenz: `novapolis-dev/docs/process/standalone-beta-installblatt.md`, `README.md`, `todo.root.md`.
  - Abschluss 2026-03-18: Das Installblatt deckt Voraussetzungen, Setup, Start, Verifikation, Go/No-Go und Troubleshooting in externer Leserperspektive ab.
- [x] [Spaeter] Cadence-KPI-Review als Trendansicht verankern (nicht nur Einzelwerte je Slot).
  - Akzeptanzkriterium: KPI-Verlauf (4 Kernmetriken) ist fuer mindestens 4 aufeinanderfolgende Slots vergleichbar dokumentiert.
  - Evidenz: `novapolis-dev/docs/meta/dev-kpi-trends.md`.
  - Abschluss 2026-03-19: Die vier Kernmetriken (`todo_index_drift`, `active_docs_stale`, `placeholder_conflicts`, `logs_policy_violations`) sind ueber vier dokumentierte Slots in einer dedizierten Trendansicht vergleichbar zusammengefuehrt.

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


