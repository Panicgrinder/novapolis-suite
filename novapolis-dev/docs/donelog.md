---
stand: 2026-02-21 20:53
update: RP-TODO-Hygiene dokumentiert (Archiv entkoppelt, Risiko-Markierung ergänzt).
checks: "npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/todo.rp.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-21 20:38); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py novapolis-dev/docs/todo.rp.md novapolis-dev/docs/donelog.md PASS (2026-02-21 20:38)"
---

<!-- markdownlint-disable MD005 MD007 MD032 MD041 -->
<!-- Migration: Quelle aus dem frueheren coding-Hub, uebernommen am 2025-10-29 -->
<!-- Relocated aus dem ehemaligen Novapolis-RP Development-Hub nach `novapolis-dev/docs/donelog.md` am 2025-10-29 -->

Hinweis (2026-01-08)
-------------------

- Aeltere Eintraege koennen noch `.ps1`-Aufrufe nennen (historisch). Aktuelle Wrapper/Entry-Points laufen ueber Python (`scripts/*.py`).

RP: TODO-Board Hygiene (Archiv entkoppelt) (2026-02-21 20:35)
--------------------------------------------------------------

- `novapolis-dev/docs/todo.rp.md` vollstaendig auf aktuellen Risikostand nachgeschaerft (Legacy-Namen/Pfade, bestehende vs. neue Canvas-Aufgaben).
- Archivblock im `<details>` explizit als historisch markiert (`nicht aktiv abarbeiten`) und mit Re-Aktivierungsregel versehen.
- Ziel: Fehlsteuerung vermeiden (kein versehentliches Abarbeiten veralteter Backlog-Punkte ohne Soll-Ist-Abgleich).
- Checks: markdownlint-cli2 PASS (scoped), check_frontmatter.py PASS (scoped).

RP: Index Sidecar-Policy Nachzug (2026-02-21 20:09)
---------------------------------------------------

- `database-rp/index.json` an die README-Sidecar-Policy angeglichen: README-Eintraege erwarten keine JSON-Sidecars.
- Senn-Daru im Index auf den kanonischen Novapolis-Charakterpfad inkl. Sidecar verankert (`01-factions/novapolis/02-characters/Senn-Daru.{md,json}`).
- Legacy-Eintrag `person_index_np` auf `person-index-np` korrigiert (MD+JSON).
- Verifikation: Index-Konsistenzcheck erfolgreich (`total=97`, `missing=0`).

CI/RP: validate-rp Workflow + Sim-README ohne PS1 (2026-02-17 04:05)
---------------------------------------------------------------

- `.github/workflows/validate-rp.yml`: Windows-Job von PS1-Wrappern auf direkte `npm`-Validator-Aufrufe umgestellt.
- `novapolis-sim/README.md`: PS1-Wrapper-Referenzen entfernt; Headless/Smoke als direkte Godot-CLI/PowerShell-Einzeiler dokumentiert.
- Checks: markdownlint-cli2 PASS (scoped); check_frontmatter.py PASS (scoped).

Dev-Hub: Index Single-Root/Wrapper-Policy (2026-02-17 01:04)
------------------------------------------------------------

- Veralteten Multi-Root/"keine Wrapper"-Hinweis in `novapolis-dev/docs/index.md` entfernt und an das aktuelle Single-Root-Setup angepasst.
- PS1-spezifischen Workaround aus dem Index entfernt; Verweis auf Hub-Doku fuer Validator-Workflows gesetzt.
- Checks: markdownlint-cli2 PASS (scoped); check_frontmatter.py PASS (scoped).

Dev-Hub: Multi-Root/PS1 Navi-Sweep (2026-02-17 02:46)
-----------------------------------------------------

- `novapolis-dev/docs/process/betriebsmodi-sicherheitsprotokoll-notizen.md`: Multi-Root Hinweis als Regression-Fallback formuliert.
- `novapolis-dev/README.md`: Link-Scanner Verweis auf `python scripts/scan_links.py` umgestellt und Output-Pfade korrigiert.
- `single-root-todo.md` (archived): Wrapper-Hinweis auf Python-Wrapper aktualisiert.
 - Checks: markdownlint-cli2 PASS (scoped); check_frontmatter.py PASS (scoped).

Backups Tooling: Python-Ports + Doku-Links (2026-02-17 03:28)
------------------------------------------------------------

- `scripts/update_backups_manifest.py`: Manifest-Schema + `manifest.v1.sha256sum.txt` (SHA-256) wieder konsistent zum archivierten PS1-Original.
- `scripts/rotate_backups.py`: Tiered Retention (Daily/Weekly/Monthly/Yearly) + Dry-Run/Apply + `rotation.log` konsistent zum archivierten PS1-Original.
- Doku-Links von `.ps1` auf `.py` umgestellt: `Backups/README.md`, `Backups/AUDIT.md`, `novapolis-dev/docs/readme.hub.md`, `single-root-todo.md`.
- Checks: markdownlint-cli2 PASS (scoped); check_frontmatter.py PASS (scoped); checks_types.py PASS (pyright+mypy, CWD=novapolis_agent).

RP: Novapolis Characters Sidecar Sync (2026-02-16 13:06)
-------------------------------------------------------

- JSON-Sidecars in `database-rp/01-factions/novapolis/02-characters/` gegen das Markdown-Frontmatter normalisiert (kanonische Key-Reihenfolge, Typen; Drift-Fix bei last_seen/primary_location/last_updated).
- Ausfuehrung: `scripts/rp_canon_sync.py --write --json-only --only-dir 02-characters --only-faction novapolis`.
- Checks: `scripts/run_checks_and_report.py` PASS (Report: `.tmp/results/reports/checks_report_20260216_130706.md`).

RP: Novapolis Doctrine maschinenlesbar (2026-02-16 12:51)
--------------------------------------------------------

- Novapolis Doctrine unter `database-rp/01-factions/novapolis/00-doctrine/` um strukturierte, maschinenlesbare Metadaten erweitert.
- Diplomatie: Zuständigkeiten/Freigaben (Ronja/Kora/Pahl) + Kernregeln (Außenhandel über C6, Protokollpflicht) ergänzt.
- Logistik: Rollen/Schnittstellen (Nika/Jonas/Kora/Pahl) + Transferregeln D5↔C6 als Kurzregeln ergänzt.
- History: Chronik-Regeln (Anker über Scenes/Missionslog, keine stillen Retcons) ergänzt.
- Checks: `scripts/run_checks_and_report.py` PASS (Report: `.tmp/results/reports/checks_report_20260216_125337.md`).

RP: Tick-Regeln & Simulation (Postflight-Nachtrag) (2026-02-13 09:52)
--------------------------------------------------------------------

- `database-rp/00-admin/Tick-Regeln-Simulation.md` angelegt/standardisiert und in `database-rp/00-admin/index-rules.md` verlinkt.
- Postflight/Receipt nachgezogen (Governance-Nachpflege).
- Checks: markdownlint-cli2 PASS; check_frontmatter.py PASS.

RP: Novapolis Leadership + Economy Subdocs (2026-02-16 12:27)
------------------------------------------------------------

- Leadership/Rollen in Novapolis konsolidiert (Ronja/Kora/Nika/Pahl) und Personenindex aktualisiert.
- Nachnamen ergänzt (Pahl Brenner, Marei Falk) inkl. Sidecar-Sync.
- Wirtschaftsunterlagen unter `01-factions/novapolis/06-handel-diplomatie/` konsolidiert (Märkte/Handelsplätze, Preisbänder).
- Checks: `scripts/run_checks_and_report.py` PASS (Report: `.tmp/results/reports/checks_report_20260216_122544.md`).

RP: README Sidecar-Policy (2026-02-16 12:33)
--------------------------------------------

- Policy festgelegt: README-Dateien benoetigen keine JSON-Sidecars.
- Legacy `README.json` Sidecars entfernt (Handel/Diplomatie-READMEs der Fraktionen sowie `database-rp/06-scenes/README.md`).
- Checks: `scripts/run_checks_and_report.py` PASS (Report: `.tmp/results/reports/checks_report_20260216_123226.md`).

RP: Process-Workflow Konsolidierung (2026-02-11 01:59)
-----------------------------------------------------

- Prozess-/Workflow-Inhalte (Curation, Validatoren, Export/Ingest, Metadata, Simulation, Schreibstil, Naming-Policy) nach `database-rp/00-admin/Process-Workflow.md` uebertragen.
- `index-rules.md` um Verweis und Abschnitts-ID ergaenzt.
- Checks: not run.

RP: Process-Workflow Erweiterung (2026-02-11 02:09)
---------------------------------------------------

- fehlende Abschnitte aus Dev/RP ergaenzt (Scenes, Checks, Stub-Mapping, Governance, FinalGate, Canvas-Rescue).
- Checks: not run.

RP: Process-Workflow MD031-Fix (2026-02-11 03:29)
-------------------------------------------------

- Leerzeile vor Codeblock (Beispiel-Frontmatter) ergaenzt.
- Checks: `scripts/run_checks_and_report.py` PASS.

RP: Sim-State-Schema (2026-02-11 05:25)
---------------------------------------

- Sim-State-Schema in `database-rp/00-admin/Sim-State-Schema.md` angelegt und in `index-rules.md` verlinkt.
- Checks: not run.

RP: Sim-State-Schema Sidecars/Index (2026-02-11 05:26)
------------------------------------------------------

- JSON-Sidecars fuer Process-Workflow und Sim-State-Schema angelegt.
- `database-rp/index.json` aktualisiert.
- Checks: not run.

RP: Frontmatter/Markdownlint Fixes (2026-02-10 22:50)
----------------------------------------------------

- Frontmatter in Admin/Readmes normalisiert (inkl. Reference-Campaign-State inline-Keys).
- Markdownlint-Fix: Leerzeilen um Tabelle in `Marktpreise-inventar.md`.
- Checks: `scripts/run_checks_and_report.py` PASS.

RP: Waren-Index Filter-Split (2026-02-10 16:51)
----------------------------------------------

- Filterposten in `Waren-Index.md` getrennt: Luftfilter (Gasmasken, Einrichtungen) und Wasserfilter (portabel, stationaeres Filtermaterial).
- Checks: not run.

RP: Waren-Index + Marktpreise Skalen (2026-02-10 17:06)
-------------------------------------------------------

- Neue Items aus Szenen im Waren-Index ergaenzt (u. a. Werkzeugtasche, Messausruestung, Sensoren, Artefakt/Datenkern).
- Marktpreise-Baseline: Skalen fuer Verfuegbarkeit/Tauschwert + kompakte Item-Tabelle ergaenzt.
- Checks: not run.

RP: D5/C6 Inventar-Logs Sonderfunde (2026-02-10 17:09)
-------------------------------------------------------

- D5/C6 Inventar-Logs um Sonderfunde als [FACT?] ergaenzt (Werkzeugtasche, Artefakt 7A, Datenkern/Datenwuerfel).
- Checks: not run.

RP: RAW-Waren aufgenommen (2026-02-10 17:24)
-------------------------------------------

- Waren-Index um RAW-Items (handelbar/stationaer) ergaenzt; Datenkern in stationaer/tragbar gesplittet.
- Marktpreise-Baseline: Item-Tabelle um RAW-Waren erweitert.
- Checks: not run.

RP: Curated-Konfliktliste/uncertainties (2026-02-09 02:36)
---------------------------------------------------------

- Offene Konfliktpunkte in `uncertainties.md` ergänzt (Inventar, Draisine, C6-Gerücht).
- Curated-Konfliktliste aktualisiert (Top-10/Offen).
- Markdownlint FAIL: MD010 in `novapolis-rp/database-curated/staging/chat-export-complete.finalgate.md`.

RP: Curated-Konflikt-Report Refresh (2026-02-09 02:46)
------------------------------------------------------

- Markdownlint erneut ausgefuehrt: PASS.
- Report ueberschrieben: [.tmp/results/reports/curated_conflicts_postflight_20260112_0657.md](../../.tmp/results/reports/curated_conflicts_postflight_20260112_0657.md)
- `scripts/extract_curated_conflicts.py --out .tmp/results/reports/curated_conflicts_postflight_20260112_0657.md` PASS.

RP: FinalGate/Review Links (2026-02-09 02:54)
----------------------------------------------

- FinalGate/Review um Konfliktliste und Report-Link ergaenzt.

Checks: full (2026-02-09 02:59)
-------------------------------

- `scripts/run_checks_and_report.py` PASS.

RP: Weltwirtschaftssystem Entwurf (2026-02-09 04:53)
----------------------------------------------------

- Entwurf in `.tmp/results/world-economy-system.draft.md` angelegt (Makro/Meso/Mikro, postapokalyptische Leitplanken).

RP: Weltwirtschaftssystem Preis-Index (2026-02-09 05:28)
--------------------------------------------------------

- Preisanker (Basispreis), Index-Skalen und Anti-Doppelzaehlung im Entwurf ergaenzt.

RP: Weltwirtschaftssystem Ebenentrennung (2026-02-09 07:18)
-----------------------------------------------------------

- Klarstellung: allgemeine Regeln/Skalen hier, Bedarfe/Nachfrage in Fraktionsdokumenten.

RP: Weltwirtschaftssystem Hygiene (2026-02-09 07:49)
----------------------------------------------------

- Index-Skalen sprachlich geschaerft; Zeitangaben als Heuristik markiert; Qualitaet als sekundaerer Faktor klargestellt.

RP: Weltwirtschaftssystem Hygiene 2 (2026-02-09 13:40)
------------------------------------------------------

- Distanz vs Risiko in Preisbildung/Grundannahmen getrennt; Update-Zyklus als temporaerer Override formuliert; Offene Entscheidungen an Fraktionsdokumente gebunden.

Skripte: Checks-Logging (2026-02-09 03:15)
------------------------------------------

- `scripts/run_checks_and_report.py` um Fortschrittsausgaben ergaenzt.

RP: Staging-uncertainties Sync (2026-02-09 03:31)
-------------------------------------------------

- `novapolis-rp/database-curated/staging/reports/uncertainties.md` aus Dev-Hub synchronisiert.

RP: resolved.md FACT-Tags (2026-02-09 04:12)
--------------------------------------------

- FACT-Tag-Liste in `novapolis-rp/database-curated/staging/reports/resolved.md` ergaenzt.

RP: Anomalie/Draisine Entscheidungen (2026-02-09 04:23)
------------------------------------------------------

- C6-Anomalie als Geruecht/Signalrauschen verankert.
- Draisine/Transportmodul mit konservativer Schaetzung in Reference/Projekt ergaenzt.
- Konfliktlisten/uncertainties aktualisiert (nur Kugeln offen).

Doku-Checks (2026-02-09 01:46)
------------------------------

- `check_frontmatter.py` + `markdownlint-cli2` fuer RP-SSOT + Logs ausgefuehrt (PASS, Scope siehe Frontmatter).

RP: FinalGate Admin/Inventar-Patches (2026-02-09 01:59)
-------------------------------------------------------

- Logistik-Policy um Inventar-Transferregeln und Waehrungshinweis erweitert.
- D5/C6/Novapolis-Inventare: Transfer-Policy verankert; doppelter Frontmatter-Block im Fraktionsinventar entfernt.
- FinalGate-Record/Review fuer chat-export-complete auf SSOT-Patches aktualisiert.

RP: Curated-Validator PASS (2026-02-09 02:05)
---------------------------------------------

- H1 in `novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md` ergaenzt (Validator-Fix).
- `npm --prefix novapolis-rp/coding/tools/validators run validate:rp` PASS.

RP: Logistik Waehrungseintrag (2026-02-09 02:10)
-----------------------------------------------

- [novapolis-rp/database-rp/00-admin/Logistik.md](../../novapolis-rp/database-rp/00-admin/Logistik.md) um Waehrungseintrag in Materialien/Bestande erweitert.

RP: Curated-Konflikt-Report Refresh (2026-02-09 02:20)
------------------------------------------------------

- Report ueberschrieben: [.tmp/results/reports/curated_conflicts_postflight_20260112_0657.md](../../.tmp/results/reports/curated_conflicts_postflight_20260112_0657.md)
- `scripts/extract_curated_conflicts.py --out .tmp/results/reports/curated_conflicts_postflight_20260112_0657.md` PASS.

RP: Slugs ergaenzt + Audit gruen (2026-02-09 01:44)
--------------------------------------------------

- Fehlende `slug`-Felder in Doctrine/Ops ergaenzt; `checks_rp_consistency.py --strict` jetzt ohne Warnungen.
- Log: `.tmp/results/reports/checks_rp_consistency_20260209_014430.log`.

RP: Broken Links Fix + Audit (2026-02-08 22:54)
-----------------------------------------------

- Links in `database-rp` bereinigt (curated/ops/RAW/Neutralgruppen-Platzhalter). Konsistenz-Audit erneut gelaufen: errors=0, warnings=1 (missing_slug=30).
- Log: `.tmp/results/reports/checks_rp_consistency_20260208_225406.log`.

RP: Konsistenz-Audit (2026-02-08 22:48)
--------------------------------------

- Audit fuer `novapolis-rp/database-rp` gelaufen: `scripts/check_frontmatter.py` PASS, `scripts/checks_rp_consistency.py --strict` FAIL, markdownlint PASS.
- Log: `.tmp/results/reports/checks_rp_consistency_20260208_224814.log` (16 Fehler, 1 Warnung, 30 missing slug).

RP: Chat-Staging-Lauf (2026-02-08 09:24)
----------------------------------------

- `scripts/run_rp_chat_staging.py` ausgefuehrt (OK: Chat-RAW-Staging aktualisiert, entries=8). Keine weiteren Checks.

RP: RAW-Exports Quelle korrigiert (2026-02-08 07:48)
---------------------------------------------------

- Kanonische RAW-Quelle in [novapolis-rp/database-raw/99-exports/README.md](../../novapolis-rp/database-raw/99-exports/README.md) auf RAW 2025-10-27T09-16 aktualisiert; Legacy-Hinweis zu `chat-export-complete.txt` beibehalten.

Dev-Hub: readme.hub Pfad-Drift (2026-02-04 23:06)
-------------------------------------------------

- Schritt 4 in [readme.hub.md](readme.hub.md) korrigiert: `database-rp/database-rp/*` → `database-rp/*`.

RP: Batch C (00-admin) - Restdrifts (2026-02-04 21:23)
------------------------------------------------------

- Links in [novapolis-rp/database-rp/00-admin/Index-Handel-Diplomatie.md](../../novapolis-rp/database-rp/00-admin/Index-Handel-Diplomatie.md), [novapolis-rp/database-rp/00-admin/Ereignislog-Weltgeschehen.md](../../novapolis-rp/database-rp/00-admin/Ereignislog-Weltgeschehen.md), [novapolis-rp/database-rp/00-admin/Current-State.md](../../novapolis-rp/database-rp/00-admin/Current-State.md), [novapolis-rp/database-rp/00-admin/Reference-Campaign-State.md](../../novapolis-rp/database-rp/00-admin/Reference-Campaign-State.md) und [novapolis-rp/database-rp/00-admin/Curated-Konfliktliste.md](../../novapolis-rp/database-rp/00-admin/Curated-Konfliktliste.md) auf relative Pfade normalisiert.

RP: Batch C (Rest-Links) - Normalisierung (2026-02-04 21:01)
------------------------------------------------------------

- Links und RAW-Quellen in [novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/Relationslog-Novapolis.md](../../novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/Relationslog-Novapolis.md), [novapolis-rp/database-rp/01-factions/novapolis/02-characters/Jonas-Merek.md](../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Jonas-Merek.md), [novapolis-rp/database-rp/01-factions/novapolis/02-characters/Reflex.md](../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Reflex.md), [novapolis-rp/database-rp/01-factions/haendlerbund/02-characters/Kora-Malenkov.md](../../novapolis-rp/database-rp/01-factions/haendlerbund/02-characters/Kora-Malenkov.md) und [novapolis-rp/database-rp/01-factions/haendlerbund/02-characters/Marven-Kael.md](../../novapolis-rp/database-rp/01-factions/haendlerbund/02-characters/Marven-Kael.md) auf relative Pfade normalisiert.
RP: Batch C (Handel/Diplomatie) - README Links (2026-02-04 11:03)
-----------------------------------------------------------------

- Relative Links in den Handel/Diplomatie-READMEs von Arkologie A1, Eisenkonklave, Schattenbund und Fluesterkollektiv normalisiert.

RP: Batch C (Haendlerbund/Schienenbund) - Slug/Links (2026-02-04 10:28)
---------------------------------------------------------------------

- `caravan_moves` in Charakter-Dependencies (md/json) auf `caravan-moves` konsolidiert; Slug in [novapolis-rp/database-rp/01-factions/haendlerbund/05-projects/caravan-moves.md](../../novapolis-rp/database-rp/01-factions/haendlerbund/05-projects/caravan-moves.md) aktualisiert.
- Diplomatie-READMEs auf relative Links umgestellt in [novapolis-rp/database-rp/01-factions/haendlerbund/06-handel-diplomatie/README.md](../../novapolis-rp/database-rp/01-factions/haendlerbund/06-handel-diplomatie/README.md) und [novapolis-rp/database-rp/01-factions/schienenbund/06-handel-diplomatie/README.md](../../novapolis-rp/database-rp/01-factions/schienenbund/06-handel-diplomatie/README.md).

RP: Batch C (weitere Fraktionen) - Links/Naming (2026-02-04 09:21)
---------------------------------------------------------------

- `caravan_moves` auf `caravan-moves` umbenannt (md/json) und Referenzen in Fraktionsdokumenten nachgezogen (u. a. Händlerbund-Index, G7, Eisenkonklave, Jonas/Draisine, C6-Logistik-Policy).
- Fraktionsakten/SSOTs auf relative Links zu 00-admin und Novapolis normalisiert (Relationslog-Novapolis, Handel-Diplomatie-Haendlergilde, Senn-Daru, Pahl, Liora-Navesh).
- Admin-Index/Registry-Referenzen aktualisiert in [novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md](../../novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md), [novapolis-rp/database-rp/00-admin/Curated-Konfliktliste.md](../../novapolis-rp/database-rp/00-admin/Curated-Konfliktliste.md) und [novapolis-rp/database-rp/index.json](../../novapolis-rp/database-rp/index.json).

RP: Batch C (Inventare) - Links (2026-02-04 09:34)
--------------------------------------------------

- Schienenbund- und Eiserne-Enklave-Inventare: 00-admin-Links korrekt relativiert in [novapolis-rp/database-rp/01-factions/schienenbund/04-inventory/Schienenbund-inventar.md](../../novapolis-rp/database-rp/01-factions/schienenbund/04-inventory/Schienenbund-inventar.md) und [novapolis-rp/database-rp/01-factions/eisenkonklave/04-inventory/Eiserne-Enklave-inventar.md](../../novapolis-rp/database-rp/01-factions/eisenkonklave/04-inventory/Eiserne-Enklave-inventar.md).

RP: Batch C (Novapolis) - Naming/Links (2026-02-04 09:08)
--------------------------------------------------------

- Novapolis Personenindex: Dateiname auf `person-index-np` umgestellt, Links relativisiert in [novapolis-rp/database-rp/01-factions/novapolis/02-characters/person-index-np.md](../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/person-index-np.md) und Verweise in [novapolis-rp/database-rp/01-factions/novapolis/02-characters/Lyra-Hest.md](../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Lyra-Hest.md) aktualisiert.
- Händlerbund-Referenzen auf neuen Personenindex umgestellt in [novapolis-rp/database-rp/01-factions/haendlerbund/02-characters/Senn-Daru.md](../../novapolis-rp/database-rp/01-factions/haendlerbund/02-characters/Senn-Daru.md) sowie Index-Links in [novapolis-rp/database-rp/01-factions/haendlerbund/06-handel-diplomatie/Index-Haendlergilde.md](../../novapolis-rp/database-rp/01-factions/haendlerbund/06-handel-diplomatie/Index-Haendlergilde.md).
- Novapolis Handel/Diplomatie-Index auf relative Links umgestellt in [novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/README.md](../../novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/README.md).

RP: Batch B (00-admin + 00-ops) - Links/H1 (2026-02-04 09:01)
-------------------------------------------------------------

- 00-admin: H1 in [novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md](../../novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md) ergänzt (Validator-Fix) und Index-Links in [novapolis-rp/database-rp/00-admin/Index-Handel-Diplomatie.md](../../novapolis-rp/database-rp/00-admin/Index-Handel-Diplomatie.md) auf relative Pfade umgestellt.
- 00-admin/00-ops: Ops-Referenzen in [novapolis-rp/database-rp/00-admin/Logistik.md](../../novapolis-rp/database-rp/00-admin/Logistik.md) und [novapolis-rp/database-rp/00-ops/C6-Logistik-Policy.ops.md](../../novapolis-rp/database-rp/00-ops/C6-Logistik-Policy.ops.md) korrigiert (Links auf 00-ops/00-admin).
RP: Doku/TODO-Sync (2026-02-01 13:25)
-----------------------------------

- `novapolis-rp/README.md` auf aktuelle RP-Pfade (database-rp, database-raw/99-exports) korrigiert.
- `novapolis-dev/docs/todo.rp.md` Validator-Hinweise von `run_validate_all.ps1` auf `npm --prefix novapolis-rp/coding/tools/validators run validate:*` umgestellt und Links auf migrierte Canvas-Rescue-Dokus nachgezogen.
- Root `todo.root.md` auf Migration/Override-Status abgeglichen.

Alias-Stopword Fix & Tagging 009-001 Refresh (2025-12-10 17:49)
-------------------------------------------------------------------
- `novapolis-rp/coding/tools/curation/tag_chunks_from_yaml.py` erweitert: neue Stopword-Liste verhindert, dass generische Tokens wie „verbindungstunnel" als Alias registriert werden (Slipstream für C6-E3 vs. D5-C6).
- Guard-Lauf: `python ... --range 009-001 --dry-run` → `alias_collisions = {}`, `unresolved_dependencies = []`; anschließend Write-Run ohne `--dry-run`, wodurch `.tagged` 009→001, `lexicon.json` und `unresolved.json` aktualisiert wurden.
- Auswirkungen: In `part-002.tagged.txt` entfallen die `[LOC:verbindungstunnel-c6-e3]`-Markierungen bei generischen Erwähnungen, während strukturierte Tabellen weiterhin via `[LOC:c6]`, `[LOC:d5]` und `[PROJ:nordlinie-01]` referenzieren.
- Dokumentation & Checks: `todo.root.md`, `/.tmp/results/todo.cleaned.md`, `DONELOG.md`, `novapolis-dev/docs/donelog.md`, `WORKSPACE_STATUS.md` aktualisiert; targeted `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'todo.root.md' 'DONELOG.md' 'novapolis-dev/docs/donelog.md' 'WORKSPACE_STATUS.md' '.tmp/results/todo.cleaned.md'` PASS sowie `python scripts/check_frontmatter.py` auf denselben Dateien PASS.

Tree-Snapshots & STOP-Plan 009-001 Nachbereitung (2025-12-08 17:55)
--------------------------------------------------------------------
- `tree /A /F > workspace_tree_full.txt`, `tree /A > workspace_tree.txt` und `python scripts/update_workspace_tree_dirs.py` erneut ausgeführt; alle drei Artefakte spiegeln jetzt den Stand vom 2025-12-08 17:50 wider (Volume Games → Root `F:/VS Code Workspace/Main`).
- Targeted `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'todo.root.md DONELOG.md novapolis-dev/docs/donelog.md WORKSPACE_STATUS.md .tmp/results/todo.cleaned.md'` PASS sowie `python scripts/check_frontmatter.py todo.root.md .tmp/results/todo.cleaned.md DONELOG.md novapolis-dev/docs/donelog.md WORKSPACE_STATUS.md` PASS; Scope deckt sämtliche STOP-Plan-Dokumente ab.
- Dokumentation synchronisiert: `todo.root.md`, `/.tmp/results/todo.cleaned.md`, `DONELOG.md`, `WORKSPACE_STATUS.md` und dieses Donelog führen dieselben Receipts; Alias-Follow-up „Verbindungstunnel“ bleibt als separates Item bestehen.

- Backups & Snapshot: `AI-Behavior-Mapping-20251201-081946.{md,json}` erneut abgelegt; zusätzlich `Backups/tagging-009-001-prewrite.txt` über `git ls-tree -l HEAD -- "novapolis-rp/database-curated/reviewed/chat-export (1)"` erstellt (Blob-IDs + Größen dokumentieren den Zustand vor dem Write-Run).
- Guard-Lauf (`--dry-run`): `unresolved_dependencies = []`, Alias-Kollisionen ausschließlich `verbindungstunnel-c6-e3` ↔ `verbindungstunnel-d5-c6`, keine `unknown_tokens`. JSON-Output direkt aus dem Skript-Terminal übernommen (Skript schreibt aktuell kein separates Log).
- Write-Lauf: identisches Kommando ohne `--dry-run`; neue `.tagged` 009→001 sowie aktualisierte `index_review.json`, `lexicon.json`, `unresolved.json` (Zeitstempel 2025-12-01 14:47). Nachbereitung: targeted markdownlint + `python scripts/check_frontmatter.py` (Scope: Root/Dev TODO/DONELOG/Status) am 2025-12-01 PASS; Tree-Snapshots auffrischen und Alias-Collision „Verbindungstunnel“ als separates Follow-up aufnehmen.

Tagging-Doku Sync & STOP-Plan Update (2025-11-30 08:13)
--------------------------------------------------------

- Root-/Hub-Dokumente nach dem 015-010 Refresh abgestimmt: `todo.root.md`, `/.tmp/results/todo.cleaned.md`, `DONELOG.md`, `WORKSPACE_STATUS.md` sowie dieser Donelog spiegeln nun dieselben Receipts, Standwerte und Tree-Notizen wider; keine neuen Skriptläufe erforderlich.
- Folgeaufgabe vorbereitet: STOP-Plan für Range 009-001 inkl. Backups (`AI-Behavior-Mapping.{md,json}` → `Backups/tagging-pipeline/AI-Behavior-Mapping-20251130-*.{md,json}`), Snapshot `Backups/tagging-009-001-prewrite.txt` (Hash/Size der reviewed Outputs), Dry-Run/Write-Befehle und Nachbereitungs-Checks (targeted `markdownlint-cli2`, `python scripts/check_frontmatter.py`, Tree-Snapshots) dokumentiert.
- Arbeitsanweisungen im Root-/Temp-TODO aktualisiert, damit Copilot/GPT dieselbe Guard-Sequenz für die nächste Etappe kennt (Backups → Dry-Run → Write → Doku/Lint → Tree → Postflight).

Tagging-Pipeline 015-010 – Refresh & Dokumentation (2025-11-27 22:10)
---------------------------------------------------------------------

- Backups/Snapshot: `AI-Behavior-Mapping.{md,json}` erneut nach `Backups/tagging-pipeline/AI-Behavior-Mapping-20251127-220319.{md,json}` kopiert; `Backups/tagging-015-010-prewrite.txt` jetzt mit SHA256/Size pro reviewed Datei (index/lexicon/unresolved + part-019…010).
- Guard-Lauf: `python novapolis-rp/coding/tools/curation/tag_chunks_from_yaml.py --yaml-root novapolis-rp/database-rp --chunks-root "novapolis-rp/database-curated/staging/chunks/chat-export (1)" --out-root "novapolis-rp/database-curated/reviewed/chat-export (1)" --range 015-010 --dry-run` PASS (`unresolved_dependencies=[]`, alias_collisions unverändert, canonicalized N7 total 2).
- Write-Run: gleicher Befehl ohne `--dry-run`; `.tagged` 015→010, `index_review.json`, `lexicon.json`, `unresolved.json` aktualisiert; Log `reports/tagging-20251127T212031Z.log` archiviert.
- Nachbereitung: Tree-Snapshots (`workspace_tree_full.txt`, `workspace_tree.txt`, `workspace_tree_dirs.txt`) regeneriert; targeted markdownlint + Frontmatter-Validator über `todo.root.md`, `.tmp/results/todo.cleaned.md`, `DONELOG.md`, `novapolis-dev/docs/donelog.md`, `WORKSPACE_STATUS.md` PASS; Root-/Hub-Doku synchronisiert und Todo-ID-Liste aktualisiert.
- 2025-11-30 08:13: Root-/Hub-Dokumente erneut auf diesen Stand gebracht (keine neuen Läufe) und Range 009-001 als Folgeaufgabe verlinkt.

Tagging-Pipeline 009-001 – Plan & Freigabe (2025-11-27 03:20)
-------------------------------------------------------------

- Update 2025-11-30 08:13: Plan mit Hash-Snapshot `Backups/tagging-009-001-prewrite.txt` ergänzt und in Root-/Temp-TODO gespiegelt; nächste Ausführung wartet weiterhin auf Freigabe nach Dry-Run.
- Scope: `coding/tools/curation/tag_chunks_from_yaml.py` mit Range `009-001` (descending). Inputs: `novapolis-rp/database-curated/staging/chunks/chat-export (1)/chat-export (1).part-009.txt` bis `...part-001.txt`. Erwartete Outputs: `part-009.tagged.txt` … `part-001.tagged.txt` + aktualisierte `index_review.json`, `unresolved.json`, `lexicon.json` sowie ein neuer Report unter `novapolis-rp/database-curated/reviewed/chat-export (1)/reports/`.
- Backups/Snapshots vor Write erneut ausführen:
  - `novapolis-rp/database-rp/00-admin/AI-Behavior-Mapping.{md,json}` nach `Backups/tagging-pipeline/AI-Behavior-Mapping-20251127-0320.{md,json}` kopieren.
  - Struktur-Snapshot: `tree /A /F "novapolis-rp/database-curated/reviewed/chat-export (1)" > Backups/tagging-009-001-prewrite.txt` (separater Timestamp, keine Überschreibung des 015-010-Files).
  - Optional: Hash-/Line-Count-Check der Eingabe-Chunks via `python coding/tools/curation/text_stats.py --chunks-root ... --range 009-001` um Drifts zwischen Staging/Reviewed früh zu erkennen.
- Guard-Lauf (DryRun): `python coding/tools/curation/tag_chunks_from_yaml.py --yaml-root novapolis-rp/database-rp --chunks-root "novapolis-rp/database-curated/staging/chunks/chat-export (1)" --out-root "novapolis-rp/database-curated/reviewed/chat-export (1)" --range 009-001 --dry-run`.
  - Abbruch wenn neue alias_collisions ≠ {"C6" ↔ "c6-nord"} oder wenn `unresolved_dependencies` weitere Slugs (Echo/Reflex-Wissensstand-Trainingsstand etc.) ausgibt.
  - Dry-Run-Log sichern (`reports/tagging-DRY-20251127T*.log`), Review-Link im DONELOG/TODO referenzieren.
- Write-Run nach Freigabe: gleicher Befehl ohne `--dry-run`. Erwartung: neue `.tagged`-Dateien, aktualisierte `index_review.json` + `lexicon.json`, Report `reports/tagging-20251127T*.log`.
- Nachbereitung: `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/donelog.md'` + `python scripts/check_frontmatter.py novapolis-dev/docs/donelog.md`. Zusätzlich `DONELOG.md`, `todo.root.md`, `/.tmp/results/todo.cleaned.md`, `WORKSPACE_STATUS.md`, `workspace_tree*.txt` synchronisieren; Postflight-Receipt anhängen.
- STOP-Gate: Nur fortfahren, wenn Backups vorhanden, Dry-Run PASS meldet und Alias-/Dependency-Probleme dokumentiert bzw. behoben sind. Alias-Kollision `C6` vs. `c6-nord` + unresolved Slugs (Echo, Reflex-Wissensstand-Trainingsstand, Archivplatzhalter) separat adressieren, bevor weitere Ranges (<=000) geplant werden.

Lexikon- & Dependency-Sweep (2025-11-27 03:29)
-----------------------------------------------

- Aliaskonflikt `C6` vs. `c6-nord` im Tagging-Skript behoben (Slug-Tokens für Multiword-Locations filtern); Redirects `n7`/`N7` ergänzt.
- Fehlende Slugs ergänzt (`ai_behavior_index_v2`, `logistik`, `missionslog`, Wissenstands-Canvas von Echo/Reflex) und `caravan_moves` vereinheitlicht (`caravan_moves`).
- Neue Admin/Faktions-Stubs erstellt: `Cluster-Index`, `Relationslog-Eisenkonklave`, `Handel-Diplomatie-Haendlergilde`, `Index-Haendlergilde`, `Eisenkonklave` (inkl. JSON-Sidecars) – decken bisher unresolved Dependencies ab.
- Validierung: `python scripts/check_frontmatter.py` (11 Dateien) PASS, Dry-Run `python novapolis-rp/coding/tools/curation/tag_chunks_from_yaml.py --range 015-010 --dry-run` zeigt `unresolved_dependencies = []`, verbleibende `alias_collisions` nur bei Doppel-Titeln (`Echo`, `Reflex`, `(v1)`, `Verbindungstunnel`). Folgeaufgabe: Heuristik für Wissensstands-Canvas & `(v1)`-Token planen.

Tagging-Pipeline 015-010 – Plan & Freigabe (2025-11-26 05:22)
-------------------------------------------------------------

- Scope: `coding/tools/curation/tag_chunks_from_yaml.py` mit Range `015-010` (descending). Inputs: `novapolis-rp/database-curated/staging/chunks/chat-export (1)/chat-export (1).part-015.txt` bis `...part-010.txt`. Outputs sollen als `part-015.tagged.txt` … `part-010.tagged.txt` unter `novapolis-rp/database-curated/reviewed/chat-export (1)/` landen.
- Backups/Snapshots vor Write:
  - Kopie von `novapolis-rp/database-rp/00-admin/AI-Behavior-Mapping.{md,json}` nach `Backups/tagging-pipeline/AI-Behavior-Mapping-20251126-0522.{md,json}`.
  - `tree /A /F "novapolis-rp/database-curated/reviewed/chat-export (1)" > Backups/tagging-015-010-prewrite.txt` (ersetzt ältere `outputs/tagging/015-010`-Referenz).
- Guard-Lauf (DryRun): `pwsh -File scripts/tagging_pipeline_run.ps1 -Pipeline 015-010 -Mode DryRun` lt. ursprünglichem Plan gibt es nicht mehr; Ersatz: `python coding/tools/curation/tag_chunks_from_yaml.py --yaml-root novapolis-rp/database-rp --chunks-root "novapolis-rp/database-curated/staging/chunks/chat-export (1)" --out-root "novapolis-rp/database-curated/reviewed/chat-export (1)" --range 015-010 --dry-run`. Protokoll im Terminal + Exitcode dokumentieren, Abbruch bei Abweichungen.
- Write-Run (Wrapper-Äquivalent): derselbe Befehl ohne `--dry-run`, gestartet erst nach obiger Freigabe. Erwartet: neue `.tagged.txt`-Dateien (015→010), aktualisiertes `index_review.json`, `unresolved.json`, `lexicon.json`, frischer Report `reports/tagging-YYYYMMDDTHHMMSSZ.log`.
- Nachbereitung laut STOP-Plan: `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/donelog.md'` + `python scripts/check_frontmatter.py novapolis-dev/docs/donelog.md` sowie Updates in `DONELOG.md`, `todo.root.md`, `/.tmp/results/todo.cleaned.md`, `WORKSPACE_STATUS.md`, ggf. `workspace_tree*.txt`. Postflight-Receipt nach Abschluss.
- STOP bestätigt (2025-11-26 05:22) – keine Ausführung bevor Dry-Run und Backups dokumentiert sind.

Ausführung & Nachbereitung (2025-11-26 05:35)
-------------------------------------------

- Backups/Snapshots erstellt: `AI-Behavior-Mapping.{md,json}` unter `Backups/tagging-pipeline/AI-Behavior-Mapping-20251126-0522.*`, Tree-Snapshot `Backups/tagging-015-010-prewrite.txt` für `novapolis-rp/database-curated/reviewed/chat-export (1)/`.
- Guard-Lauf: `python coding/tools/curation/tag_chunks_from_yaml.py --yaml-root novapolis-rp/database-rp --chunks-root "novapolis-rp/database-curated/staging/chunks/chat-export (1)" --out-root "novapolis-rp/database-curated/reviewed/chat-export (1)" --range 015-010 --dry-run` → PASS. Summaries bestätigt (015→010, Canonicalized N7 total=2, Alias-Kollisionen wie erwartet).
- Write-Run (gleiches Kommando ohne `--dry-run`): neue Dateien `part-015.tagged.txt` … `part-010.tagged.txt`, `index_review.json`/`unresolved.json`/`lexicon.json` aktualisiert, Report `reports/tagging-20251126T043409Z.log` erzeugt (LOC-only Hinweise, Canonicalized N7→c6-nord total 2).
- Checks laut Plan: `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/donelog.md'` PASS, `python scripts/check_frontmatter.py novapolis-dev/docs/donelog.md` PASS.
- Offene Folgearbeiten: Alias-Kollision „C6“ weiter beobachten; nächste Ranges 009-001 vorbereiten; Root- und Hub-Dokumente synchronisieren (DONELOG/TODO/WSTATUS/workspace_tree*).

Doku-Sweep: markdownlint konsolidiert (2025-11-07 09:59)
-----------------------------------------------------

- Repo-weiter Check: `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md'` → 132 Dateien, 0 Fehler.
- Referenzen zum markdownlint-Befehl erneut geprüft (naked npx, korrektes Quoting mit einfachen Anführungszeichen). Keine inhaltlichen Änderungen.

SSOT-Verhalten konsolidiert; Duplikate gelöscht (2025-11-07 06:31)
-----------------------------------------------------------------

- Verhalten/Arbeitsregeln zentralisiert in `.github/copilot-instructions.md` (SSOT).
- Alte Dokumente gelöscht: `novapolis_agent/docs/AGENT_BEHAVIOR.md`, `novapolis-dev/docs/copilot-behavior.md`.
- Referenzen repo-weit auf SSOT aktualisiert (Root/Agent/Dev-Hub); Root-DONELOG ergänzt.
- Checks: markdownlint-cli2 (docs focused) PASS.

Archiv-TODOs & Issue-Template Setext (2025-11-07 04:56)
------------------------------------------------------

- Archiv-TODO-Dateien unter `novapolis-dev/archive/todo.*.archive.md` auf Setext-Stil (H1/H2) gebracht; Frontmatter (stand/update/checks) synchronisiert.
- `.github/ISSUE_TEMPLATE/feature_request.md` auf Setext-Stil umgestellt; Markdownlint repo-weit (`**/*.md`, 132 Dateien) PASS dokumentiert.
- Checks: `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md'` PASS.

Staging-Reports - Setext/Frontmatter konsolidiert (2025-11-07 02:29)
--------------------------------------------------------------------

- Reports unter `novapolis-rp/database-curated/staging/reports/*.md` auf YAML-Frontmatter und Setext-Überschriften gebracht; lokale Markdownlint-Overrides in `staging/.markdownlint.json` und `staging/reports/.markdownlint.json` entfernt.
- Lint-Scope-Runs: staging reports (10 Dateien) PASS; dev/agent docs PASS. Repo-weites Pattern-Quoting in Tasks/Terminal korrigiert.
- Follow-up: Lange TODO-Dateien (MD003-Konsistenz) separat bereinigen.

Lint-Tooling & Status-Docs Sync (2025-11-07 02:19)
--------------------------------------------------

- VS Code Task angepasst: markdownlint-Aufruf mit korrekt gequotetem Pattern ('**/*.md').
- Repo-weiten markdownlint-Lauf und MD003-Backlog in den Status-Dokumenten festgehalten.
- Status-Dokumente synchronisiert: `todo.root.md`, `WORKSPACE_STATUS.md`, `single-root-todo.md`.

TODO/Status-Update (2025-11-07 01:39)
-------------------------------------

- `todo.root.md` erweitert (Single-Repo-Governance-Reminder, Aufgaben zu Markdownlint-Overrides, Staging-Report-Migration, Metadata-Skripte, Archiv-Ablage).
- `WORKSPACE_STATUS.md` synchronisiert (aktueller Hinweis auf neue Aufgaben).
- Keine Builds/Tests ausgeführt (Dokumentationspflege).

Workspace-Konfliktanalyse (2025-11-07 01:27)
--------------------------------------------

- Bestehende Markdownlint-Overrides unter `novapolis-rp/database-curated/staging/.markdownlint.json` und `.../reports/.markdownlint.json` identifiziert (deaktivieren zentrale Regeln MD003/MD012/MD047). Empfehlung: Overrides evaluieren, Konfiguration an globale Policy anpassen oder entfernen.
- Staging-Reports (`novapolis-rp/database-curated/staging/reports/*.md`) ohne YAML-Frontmatter/Setext-Headings erfasst; Kandidaten für Migration in den Dev-Hub bzw. Konvertierung in Setext-Format.
- Doppelte Metadata-Initialisierungsskripte konsolidiert (2026-02-18): `novapolis-rp/coding/tools/metadata/init_metadata.py` als kanonische Implementierung festgelegt und dokumentiert; `init-metadata.js` entfernt.
- Legacy-Notiz `novapolis_agent/analysis_chat_routers.md` (Triple-Quote-Stub) als Alt-Dokument markiert.

Chat-Neustart-Prompt entfernt (2025-11-06 03:07)
---------------------------------------------

- Veraltete Datei `docs/prompts/chat-restart.md` gelöscht; Index-Verweis entfernt.
- Hinweis im Root-DONELOG/TODO aktualisiert (siehe entsprechende Einträge).
- Checks: `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc "novapolis-dev/docs/index.md"` PASS.

Workspace Tree - Refresh (2025-11-06 03:34)
-----------------------------------------

- Tasks ausgeführt: `Workspace tree: full`, `Workspace tree: directories`, `Workspace tree: summary (dirs)`.
- Artefakte aktualisiert: `workspace_tree_full.txt`, `workspace_tree.txt`, `workspace_tree_dirs.txt`.
- Follow-up: Root-Status (`WORKSPACE_STATUS.md`), Root-DONELOG und Agent-DONELOG ergänzt.

Markdownlint-Stub entfernt (2025-11-06 03:18)
--------------------------------------------

- `novapolis-rp/coding/tools/validators/run_lint_markdown.ps1` gelöscht; README-Hinweis angepasst.
- `.github/copilot-instructions.md` Abschnitt zu Markdownlint aktualisiert (keine Stub-Nennung mehr).
- Checks: `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc "novapolis-rp/coding/tools/validators/README.md"` PASS.

Frontmatter-Migration - Docs Sweep (2025-11-02T23:23:00+01:00)
Docs-Snapshot - Lint-Regeln synchronisiert (2025-11-05 18:33)

- Regeln präzisiert: markdownlint via pwsh und `npx --yes markdownlint-cli2` (keine Wrapper).
- Task-Labels in `.vscode/tasks.json` auf „Lint: markdownlint-cli2 …“ vereinheitlicht.
- Checks: markdownlint-cli2 (docs focused) FAIL - MD003/heading-style in `novapolis-dev/docs/donelog.md` und vielfach in `single-root-todo.md` (pro Datei konsistenter Stil erforderlich).


- `docs/donelog.md` und `docs/tests.md` um YAML-Frontmatter ergänzt; Status-Header inkl. Lint-Ergebnis aktualisiert.
- Checks: markdownlint-cli2 (docs focused) PASS.

Frontmatter-Migration - Agent Docs Sweep (2025-11-02T23:36:00+01:00)

- `novapolis_agent/docs/{AGENT_BEHAVIOR,ARCHIVE_PLAN,CONTEXT_ARCH,customization,REPORTS,training}.md` und `novapolis_agent/docs/reports/overnight-20251022.md` mit YAML-Frontmatter versehen.
- Checks: markdownlint-cli2 (docs focused) PASS.

Frontmatter-Migration - Abschluss (2025-11-02T23:44:00+01:00)

- RP-Docs unter `novapolis-rp/**/docs/**` sind Redirect-/Mirror-Stubs (SSOT: `novapolis-dev/docs/**`), daher keine Migration erforderlich.
- Checks: markdownlint-cli2 (all md) PASS.

Workspace Tree - Aktualisierung (2025-11-03T00:18:00+01:00)

- Tasks ausgeführt: "Workspace tree: full", "Workspace tree: directories", "Workspace tree: summary (dirs)".
- Aktualisierte Artefakte: `workspace_tree_full.txt`, `workspace_tree.txt`, `workspace_tree_dirs.txt`.
- Checks: markdownlint-cli2 (all md) PASS.

Frontmatter-Migration - TODO-SSOTs (2025-11-02T22:48:00+01:00)

- `docs/todo.{index,dev,sim}.md` mit vollständiger YAML-Frontmatter versehen (`---`-Delimiter ergänzt); Inhalte unverändert.
- Hinweis im Root-Single-Root-Plan bleibt gültig (Migration Etappe 1-3 wird fortgesetzt).
- Checks: markdownlint-cli2 (docs focused) PASS.

Single Root TODO (Root) angelegt (2025-11-02 10:02)

- Neue Datei `single-root-todo.md` im Repo-Root erstellt (Scaffold mit YAML-Frontmatter, Modul-Links, Root-Aufgaben).
- Lint: markdownlint-cli2 PASS.

Monorepo Single Root - Umstellungsplan ergänzt (2025-11-02 10:10)
Coverage-Gate erreicht (2025-11-09 17:51)
----------------------------------------

- Gesamt-Coverage via Wrapper `scripts/run_pytest_coverage.ps1`: 81.66% (fail-under 80 bestanden).
- Neue Tests decken interne Chat-API-Zweige (Stream/Non-Stream), Memory-Truncation-Kantenfälle und Script-Fallbacks ab.
- Governance-Dokument `.github/copilot-instructions.md` Zeitstempel aktualisiert; Root- und Agent-DONELOG Frontmatter angepasst.
- Checks: pytest coverage PASS; markdownlint (repo-weit) zuvor PASS.


- In `single-root-todo.md` Abschnitt „Monorepo Single Root - Umstellungsplan (Schritt für Schritt)“ hinzugefügt (Etappen 0-5, Akzeptanzkriterien, optionale PowerShell-Befehle).
- Lint: markdownlint-cli2 PASS.

Canvas-Rettung Sprint 1 - C6/E3 Linienabgleich (2025-11-02T13:30:00+01:00)

- Neue Location-Canvas `database-rp/03-locations/Verbindungstunnel-C6-E3.{md,json}` angelegt (Status, Nutzung als Evakuierungsroute für 20 E3-Flüchtlinge, Aufgabenliste); Index (`database-rp/index.json`) erweitert und Metadaten mit C6/E3 verknüpft.
- `database-rp/03-locations/C6.md` um Bevölkerung/Verbindungen ergänzt (20 Evakuierte aus E3, 4 Karawanenmitglieder, aktive Tunnel); Sidecar `C6.json` Dependencies auf beide Tunnel gesetzt.
- Lexikon `database-curated/reviewed/chat-export (1)/lexicon.json` aktualisiert (Slug/Aliasse für C6-E3-Tunnel, neue Bewohner-Kontexte beibehalten).

Canvas-Rettung Sprint 1 - Behavior-Signaturen & Validator (2025-11-02T12:45:00+01:00)

- Anchor-Signaturen für Echo, Lumen, Liora, Lyra, Senn und Varek kuratiert (`AI-Behavior-Mapping.md` aktualisiert, Quelle auf Canvas verwiesen, Sidecar-Zeitstempel synchronisiert).
- Charakter-Canvases (`02-characters/*.md` + JSON) um Verhaltenseinträge ergänzt; Skill-Listen auf Leerzeichen-Indents umgestellt, Markdownlint-Ausnahmen (MD025) lokalisiert.
- Validator `coding/tools/validators/behavior_matrix_check.py` erweitert (Signatur-Format/Quellen-Check + Psymatrix-Diff >5-Punkte-Schwelle), README und TODO mit Ausführungshinweis aktualisiert; Task als erledigt markiert.

Markdownlint zentralisiert (2025-11-01T15:30:00+01:00)

- VS Code Tasks für Markdownlint gestrichen; zentraler Lauf bleibt. Lokal erfolgt Lint direkt im bestehenden Terminal via npx.
- `novapolis_agent/.vscode/tasks.json`: Markdownlint-Wrapper-Tasks gestrichen; lokal nur noch direkter `npx`-Befehl.
- `.github/workflows/markdownlint.yml`: Windows-Job lintet ausschließlich via `npx`; `run_lint_markdown.ps1` wird nicht mehr aufgerufen.
- `run_lint_markdown.ps1` zu einem Hinweisskript degradiert (Exit 1); Doku (`novapolis-dev/docs/index.md`, `novapolis-rp/coding/tools/validators/README.md`) verweist auf den direkten `npx`-Aufruf.

- 2025-11-01 13:08 — Prompt für Chat-Neustart ergänzt (`docs/prompts/chat-restart.md`); Index-Link gesetzt; Curation-Writer für UTF-8+LF+EOF gehärtet und Orchestrator `build_staging_reports.py`+PS1 hinzugefügt. Lint weiter grün.

Canvas-Rettung Sprint 1 - Jonas Merek (2025-11-02T13:55:00+01:00)

- Charakter-Canvas `database-rp/02-characters/Jonas-Merek.md` auf Version 1.0 gehoben; Werte/Skills aus RAW übernommen, Rollen (Werkstatt/Logistik/Terminal) konsolidiert, Sicherheits- & Proximity-Protokolle ergänzt.
- Korruptes RAW-Makel („Schuld am Tod der Schwester“) aufgelöst - Schwesterstatus gemäß FACT `[JONAS-SIS]` als „vermisst/unklar“ dokumentiert, Schuldflag als subjektives Kommentar markiert.
- JSON-Sidecar synchronisiert (Version, Tags, Dependencies `missionslog`, `ai_behavior_index_v2`); `char-block-nord-sources.md` und TODO aktualisiert.
- Verweise auf FACTs `[PROXIMITY]`, `[COMMS-PROTO]`, `[C6-FIRST]`, `[FR-KNOWLEDGE]` eingepflegt; Validierungsintervall notiert.

- 2025-11-01 13:08 — Prompt für Chat-Neustart ergänzt (`docs/prompts/chat-restart.md`); Index-Link gesetzt; Curation-Writer für UTF-8+LF+EOF gehärtet und Orchestrator `build_staging_reports.py`+PS1 hinzugefügt. Lint weiter grün.

Canvas-Rettung Sprint 1 - Marven Kael (2025-11-02T14:45:00+01:00)

- Neues Charakter-Canvas `database-rp/02-characters/Marven-Kael.md` erstellt; Konvoi-/Handelsrolle aus RAW übernommen, Sicherheits- und Verhandlungsprotokolle festgeschrieben, Zugehörigkeit zur Händlergilde betont.
- FACT `[CARAVAN-LEADERSHIP]` umgesetzt: klare Trennung zwischen externem Konvoi (Marven), interner Logistik (Kora) und Vermittlung (Arlen); `[FR-KNOWLEDGE]` berücksichtigt (keine Novapolis-Koordinaten).
- JSON-Sidecar ergänzt (Version 1.0, Tags `karawane`/`haendlerbund`, Dependencies `caravan_moves`, `ai_behavior_index_v2`, `missionslog`, `logistik`, `c6`); Quellenreport aktualisiert, dev TODO abgehakt.
- Risiko- und Zielsetzungen dokumentiert (Entscheidungsstarre, Crewschutz, Handelsabkommen); Validierungsintervall notiert.

Canvas-Rettung Sprint 1 - Arlen Dross (2025-11-02T15:05:00+01:00)

- Charakter-Canvas `database-rp/02-characters/Arlen-Dross.md` auf Version 1.0 gehoben; Diplomatie-/Vermittlerrolle gegenüber Novapolis ausgearbeitet, Abgrenzung zu Kora (Logistik) und Marven (Konvoi) gemäß FACT `[CARAVAN-LEADERSHIP]` dokumentiert.
- Wissensmatrix und Sicherheitslinien ergänzt: `[FR-KNOWLEDGE]` respektiert (keine Novapolis-Koordinaten), Reflex als unkalkulierbare Variable mit klaren Freigabesignalen beschrieben, Routine/Validierungszyklen aus RAW übernommen.
- JSON-Sidecar erstellt (Tags `karawane`/`haendlerbund`/`diplomatie`, Dependencies `caravan_moves`, `ai_behavior_index_v2`, `missionslog`, `logistik`, `c6`, `handel_diplomatie_haendlergilde_v1`, `index_haendlergilde_v1`); Quellenreport `char-block-nord-sources.md`, TODO und Personenindex aktualisiert.
- Risiko-/Zielkatalog ergänzt (Entscheidungsparalyse mitigieren, Handelsprotokoll standardisieren, Crew-Moderation sichern); Signals-Beispiele und Systemverknüpfungen dokumentiert.

Canvas-Rettung Sprint 1 - Pahl (2025-11-02T15:25:00+01:00)

- Charakter-Canvas `database-rp/02-characters/Pahl.md` erstellt; Gesundheitsstatus (Reha, Atemprotokolle) aus RAW verifiziert, Rollen (Systemaufsicht, Wartungsplanung, Hausregeln) gemäß FACT `[HOUSE-RULES]`/`[LOGISTICS]` beschrieben.
- Wissens- und Sicherheitsmatrix ergänzt (Atemlog, Belastungsgrenzen, Validierungsintervall, Eskalationspfade „Regel Blau/Rot“), Interaktionshinweise aus Chatpassagen zum Lagerzugang integriert.
- JSON-Sidecar angelegt (Tags `technik`/`novapolis`/`gesundheit`, Dependencies `d5`, `logistik`, `missionslog`, `ai_behavior_index_v2`, `ronja-kerschner`, `jonas-merek`, `reflex`); Quellenreport aktualisiert, dev TODO abgehakt.
- Ziele/Risiken erweitert (Reha abschließen, Systemhandbuch v1.0, Wartungsschnittstelle D5↔C6); Signals-Beispiele dokumentiert.

Canvas-Rettung Sprint 1 - Pahl Herkunfts-Abgleich (2025-11-02T15:50:00+01:00)

- FACT `[PAHL-RESCUE]` in `database-curated/staging/reports/resolved.md` aufgenommen: C6-Reaktorunfall, Rettung durch Ronja/Reflex, Transfer & Reha unter Jonas.
- Canvas `Pahl.md`/`Pahl.json` angepasst (Herkunft, Dependency `c6`, Quellenblock), Memory-Bundle und Personenindex synchronisiert, Quellenreport `char-block-nord-sources.md` erweitert.
- RAW-Flag-Hinweis belassen, aber kanonische Herkunft auf `[PAHL-RESCUE]` gestellt.

Canvas-Rettung Sprint 1 - Reflex (2025-11-02T16:05:00+01:00)

- Charakter-Canvas `database-rp/02-characters/Reflex.md` auf Version 1.0 gehoben; Symbiose-Stufe I (Frequenzband 7.3-8.0 Hz), Detachment-/Stop-Regeln, Instanzleitung und Signalsätze aus RAW/Entity synchronisiert.
- JSON-Sidecar aktualisiert (Tags `instanz`/`sicherheit`/`symbiose`, Dependencies auf Ronja/Lumen/Echo + Missionslog/Logistik); Quellenreport und Memory-Bundle auf neuen Kanonstand gebracht.
- TODO-Checkpoint für Reflex abgeschlossen; `[REFLEX-*]`-FACTs mit Canvas verknüpft, Instanz-Training in `Reflex-Wissensstand-Trainingsstand.md` referenziert.

Copilot - Moduswechsel/Erinnerungen/STOP-Gate (2025-11-02T16:55:00+01:00)

- `.github/copilot-instructions.md`: Abschnitt „Modell-Profile & Moduswechsel (GPT-5 ↔ GPT-5 Codex)“ ergänzt; Erinnerung/Prompting-Policy ohne 1×/Session-Limit (Opt-out: „Bitte nicht erinnern“); STOP-Gate vor Code-Aktionen mit expliziter Moduswahl.
- `novapolis-dev/docs/copilot-behavior.md`: Spiegel der Regeln aufgenommen (Moduswechsel, Reminder, STOP-Gate).
- `WORKSPACE_STATUS.md`: „Aktueller Arbeitsmodus“ dokumentiert (Modus: General, Stop-Gate: an, Erinnerungen: aktiv).

Validator-Tooling Docker-Pfadfix (2025-11-02T16:30:00+01:00)

- Node-Validatoren (`validate-*.js`, `check-*.js`) auf `import.meta.url`-basierte Repo-Root-Ermittlung umgestellt, damit Docker-Läufe die JSON/Markdown-Pfade finden.
- `validate-all.js` Exitcode- und Status-Logging überarbeitet; Status-Datei-Schreibpfad repariert.
- `run_validate_all.ps1` erfolgreich im Container (`node:22-alpine`) ausgeführt, temporäre Artefakte (`node_modules`, `.last-run`) entfernt.

Canvas-Rettung Sprint 1 - Ronja Kerschner (2025-11-01T17:12:00+01:00)

- Charakter-Canvas `database-rp/02-characters/Ronja-Kerschner.md` auf Version 1.0 aktualisiert; Status-/Systemabschnitte aus RAW `char_ronja_v2` übernommen und Drift („Vallin“) gemäß `resolved.md #[NAME-RONJA]` dokumentiert.
- JSON-Sidecar (`Ronja-Kerschner.json`) synchronisiert; Routine- und Systemverknüpfungen mit Review-Hinweis auf logistik-/inventar-v1 markiert.
- TODO-Boards (`novapolis-dev/docs/todo.md`, Root `TODO.md`) aktualisiert; Aufgabe „Ronja Kerschner“ auf erledigt gesetzt.
- Quellenhinweise erweitert (Canvas-Quellenblock + `char-block-nord-sources.md` Ronja-Abschnitt aktualisiert); Metadaten-Zeitstempel angepasst.

Canvas-Rettung Sprint 1 - Echo Metadatenabgleich (2025-11-01T16:35:00+01:00)

- Canvas `database-rp/02-characters/Echo.md` um Front-Matter ergänzt (Titel, Version, Zugehörigkeit, Standort, Dependencies) und Markdown-Formatierung mit Leerzeichen/Abständen an Vorlagen angepasst.
- JSON-Sidecar `database-rp/02-characters/Echo.json` auf dieselben Metafelder synchronisiert (last_updated, tags, affiliations, primary_location, dependencies).
- Keine Inhaltsänderungen; Fokus auf formale Angleichung für Lint/Validator-Kompatibilität.

Canvas-Rettung Sprint 1 - Liora Navesh (2025-11-01T16:25:00+01:00)

- Charakter-Canvas `database-rp/02-characters/Liora-Navesh.md` + JSON-Sidecar erstellt; Arkologie-A1-Taxonomie und Validierungsintervall übernommen, Novapolis/D5 weiterhin als unbekannt markiert, SÜDFRAGMENT-Signale und A9-Protokolle hervorgehoben.
- Quellenreport `char-block-nord-sources.md` aktualisiert; Flag-Hinweise (Secrecy, Taxonomie) als abgearbeitet vermerkt und Curated-Verweis ergänzt.
- `novapolis-dev/docs/todo.md` → Liora-Aufgabe als erledigt mit Zeitstempel 2025-11-01T16:20+01:00 markiert; last-updated synchronisiert.
- Personenindex `database-rp/00-admin/person_index_np.md` um Liora ergänzt (Rolle, Zugehörigkeit Arkologie A1, Fokus auf SÜDFRAGMENT, keine Novapolis-Kenntnisse).
- JSON-Sidecar verweist auf Canvas und Abhängigkeiten (`ai_behavior_index_v2`, `relationslog_arkologie_v1`, `ereignislog_weltgeschehen_v1`, `cluster_index_v1`).

Canvas-Rettung Sprint 1 - Varek Solun (2025-11-01T15:55:00+01:00)

- Charakter-Canvas `database-rp/02-characters/Varek-Solun.md` + JSON-Sidecar erstellt; Standortcode H12 (Alias „Sektor_H3“) harmonisiert, Wissensstand gemäß FACT SECRECY auf Gerüchte begrenzt.
- Quellen/Drift-Notizen in `char-block-nord-sources.md` aktualisiert; Flag-Hinweise (Novapolis-Außenwissen, Standortcodierung) als erledigt markiert.
- `novapolis-dev/docs/todo.md` und Root-`TODO.md` → Varek-Aufgabe als erledigt vermerkt (Zeitstempel 2025-11-01T15:45+01:00).
- Personenindex `database-rp/00-admin/person_index_np.md` um Varek ergänzt (Rolle, Zugehörigkeit, Verlinkung).
- JSON-Sidecar referenziert Metadaten + Quelle; Routine- und Systemverknüpfungen dokumentiert.

Canvas-Rettung Vorbereitungsrunde (2025-11-01T14:30:00+01:00)

- Canvas-Rettungsplan in `database-curated/staging/reports/canvas-rescue-plan.md` ausgearbeitet (Prioritäten A-C, Workflow, Sprint-Checkpoints, Prüfpfade).
- Quellenaggregation `char-block-nord-sources.md` erstellt (RAW-Referenzen, Drift-Overrides für Ronja/Jonas, Flag-Hinweise gebündelt).
- TODO-Board `novapolis-dev/docs/todo.md` auf Canvas-Rettung Sprint 1 fokussiert, Altbacklog in Archiv-Section überführt.
- Hinweis gesetzt: Jede Canvas-Migration → JSON-Sidecar + DONELOG-Eintrag obligatorisch.

Root-Dokumentation (2025-11-01T00:00:00Z)

- Root-Übersichten `WORKSPACE_STATUS.md`, `TODO.md`, `README.md`, `DONELOG.md` auf Stand 2025-11-01 gebracht (Health-Checks, Aufgaben, Querlinks).
- Tree-Snapshots (`workspace_tree*.txt`) als fällige Folgeaufgabe markiert.

Dev-Hub QA (2025-11-01)

- Modul `novapolis-dev` vollständig geprüft: Primärdokumente, Meta-Sidecars und Platzhalterverzeichnisse vorhanden; keine offenen Drift-Punkte.
- Rolle des Dev-Hubs bestätigt - Dokumentations-/Planungsdrehscheibe, Datenströme verbleiben in `novapolis-rp` (`database-raw`, `database-curated`, `database-rp`).

Agent-Runtime entkoppelt (2025-10-31)

- `novapolis-rp/agents/cvn_agent/` vollständig entfernt; Root-README, RP-README und Ignore-Regeln auf das eigenständige `novapolis_agent`-Repository umgestellt.
- Verweise auf das gebündelte Runtime-Paket bereinigt (`requirements.txt`, `.github/copilot-instructions.md`).
- Obsoletes Patch `_cvn_agent_removal.patch` gelöscht; RP-Workspace enthält nur noch Daten/Docs.
- Leeres Paketverzeichnis `novapolis-rp/agents/` entfernt; keine Agent-Stubs mehr im RP-Repo.

Workspace-Status Snapshot (2025-10-31)

- Gesamtübersicht `WORKSPACE_STATUS.md` auf Root-Ebene angelegt (Stand 2025-10-31) inkl. Health-Checks, Risiken, Empfehlungen.
- Vollständigen Verzeichnisbaum via `tree /A /F` erzeugt und als `workspace_tree.txt` im Root abgelegt.
- Root-`TODO.md` um Verweis auf Statusbericht ergänzt (Pflegezyklus vermerkt).
- Redundante Snapshot-Datei `workspace_tree_full.txt` als Backup abgelegt; zusätzlich kompaktes Verzeichnis-Listing `workspace_tree_dirs.txt` erzeugt.
- README-Hinweise für `.tmp-datasets/` und `.tmp-results/` ergänzt, Zweck der temporären Artefakte dokumentiert.
- Archivierungsplan in `TODO.md` konkretisiert (ZIP-Rotation, Manifest/Script-Aufgaben); Status-Doku verweist jetzt auf koordinierte Snapshot-Aktualisierung.
- Redundanten Snapshot `workspace_tree_compact.txt` entfernt, da `workspace_tree_dirs.txt` die kompakte Ansicht abdeckt.

Relocation Follow-up (2025-10-31)

- Datenpools `database-curated`, `database-raw`, `database-rp` wieder unter `novapolis-rp/` verankert; Dev Hub verweist nur noch auf diese Quelle (`README.md`, `docs/todo.md`).
- `novapolis_agent/docs/TODO.md` um aktuellen RAG-Status aktualisiert (Tests & Doku als erledigt markiert).
- Zentrale Markdown-Lint-Checks via `.github/workflows/markdownlint.yml` reaktiviert; rp-spezifische Duplikat-Workflows entfernt (`docs-lint.yml`, redundante Schritte in `validate.yml`).

Dev Hub Konsolidierung (2025-10-29)

- Dev Hub vom ehemaligen RP-Development-Hub nach `novapolis-dev/docs` verlegt; Referenzen aktualisiert und Meta-Sidecars harmonisiert.
- Legacy `development/docs` bereinigt; Meta-Sidecars geprüft; `.github/copilot-instructions.md` im RP-Repo ergänzt.
- 2025-10-29: Meta sidecars normalized: origin → full legacy path; migrated_at added.
- 2025-10-29: Dev Hub polish (README/index), VS Code Copilot instructions verlinkt; Residual-Sweep ohne Treffer.

VS Code Launch-Konfigurationen (2025-10-28)

- `.vscode/launch.json` hinzugefügt:
  - PowerShell-Runner: `validate:data (ps1)`, `lint:names (ps1)`, `system:check (windows)` (Markdownlint direkt via `npx` oder Root-Task).
  - Node-Varianten: `validate:data (node/npm)`, `lint:names (node)`, `lint:markdown (npx)`, `validate:data (status)`.
  - Ziel: Checks direkt per Startmenü (Run and Debug) nutzbar; identische Pfade wie Tasks/Wrapper.

Dokumentation/Tasks aktualisiert (2025-10-27T20:06:30+01:00)

- `novapolis-dev/docs/index.md` (vormals Coding-Index): Abschnitt "Validierung & Tasks" ergänzt (Validatoren, Lint, Systemcheck); Verweise auf `tools/validators/` und Devcontainer; `last-updated` angepasst.
- `novapolis-dev/docs/copilot-behavior.md` (vormals Coding-Copilot-Policy): Prozessregeln präzisiert - vor Push lokale Tasks ausführen (validate/data, lint/markdown, optional lint/names); Szenen-Front-Matter und Co-Occurrence beachten.
- `novapolis-dev/docs/todo.md` (vormals Coding-TODO): Status synchronisiert - Rückwärts-Review bis part-001 abgehakt; Day-Switch-Canvas abgehakt; QA-Punkt zu Szenen-Front-Matter in "etabliert" (✓) und "Backfill" (offen) aufgeteilt; `last-updated` angepasst.

Canvas-Verbesserungen (2025-10-27)
Linter-Wrapper (2025-10-27T20:12:30+01:00)

- `coding/tools/validators/run_check_names.ps1` hinzugefügt: stabiler Aufruf des Name-Linters ohne PowerShell `-Command`-Quoting; nutzt Docker (falls vorhanden) oder Node/npm, sonst Exit 1 mit klarer Meldung.
- `coding/tools/validators/README.md` ergänzt (Wrapper-Hinweis); `novapolis-dev/docs/index.md` mit Fallback-Befehl verlinkt.

PS1-Tasks ergänzt (2025-10-27T20:18:30+01:00)

- `.vscode/tasks.json`: zusätzliche Tasks ohne Inline-`-Command` aufgenommen:
  - `lint:names (ps1)` → `run_check_names.ps1`
  - `validate:data (ps1)` → `run_validate_all.ps1`
  - `lint:markdown (ps1)` → `run_lint_markdown.ps1` (veraltet seit 2025-11-01; bitte Root-Task bzw. `npx` verwenden).
- Neue Wrapper: `run_validate_all.ps1`, `run_lint_markdown.ps1` (Docker bevorzugt; sonst lokal; klare Fehlermeldung bei fehlenden Voraussetzungen; Markdownlint-Wrapper obsolet seit 2025-11-01).

CI erweitert (2025-10-27T22:40:00+01:00)

- `.github/workflows/validate.yml` aufgeteilt:
  - Linux-Job (Node 20) mit npm cache; führt Validatoren, Name-Check, Markdown-Lint aus.
  - Windows-Job (PS1-Wrapper) - führt `run_validate_all.ps1`, `run_check_names.ps1`, `run_lint_markdown.ps1` aus, um PowerShell-Skripte in CI mitzuprüfen (Wrapper seit 2025-11-01 ohne Markdownlint-Einsatz).
- Validator-Fixes:
  - Ajv 2020-12 für kuratiertes Manifest (`validate-curated.js`).
  - Front-Matter-Validator (`validate-rp.js`): `last-updated` tolerant (String/Date), H1-Allowlist für `00-admin/system-prompt.md`.

Markdown-Lint Wrapper gefixt (2025-10-27T22:55:00+01:00) - veraltet seit 2025-11-01

- `coding/tools/validators/run_lint_markdown.ps1`: Fallbacks ergänzt (veraltet seit 2025-11-01)
  - absolute `node.exe` Erkennung; direkter Aufruf von `npx-cli.js` via `node.exe` (unabhängig von PATH)
  - Reihenfolge: Docker → node+npx-cli.js → npx.cmd → Fehlermeldung
  - Behebt Fehler "'node' is not recognized" bei fehlendem PATH.
- `00-admin/Canvas-Admin-Day-Switch-Debug.md`: ATSD-Definition ergänzt, Systemmeldungs-Template aufgenommen, Fehlerfälle/Recovery ergänzt.
- `00-admin/Canvas-T+0-Timeline.md`: Marker-Raster (Beginn/Ereignisse/Ende) und Delta-Log ergänzt.
- `00-admin/canon-canvas.draft.md`: Front-Matter (last-updated, status) hinzugefügt; Tippfehler "Akologie"→"Arkologie" korrigiert; Revision vermerkt.
- `06-scenes/scene-2025-10-27-a.md`: Erste Szenen-Kachel mit Front-Matter (characters/locations/inventoryRefs) und Cross-Links angelegt; Timeline T+0 verlinkt.
- RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-20-000Z.txt` (Quelle: Canvas; Entität Reflex - Wurzelgewebe D5 v1; TIMESTAMP: 2025-10-16_03:25).
- Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-20-000Z.flags.txt` (vorsichtig_behandeln; Grund: Regeln [REFLEX-*] abgleichen; „Entfernen möglich“ vs [REFLEX-DETACH] klären; Frequenzband/Terminologie synchronisieren).
- RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-10-000Z.txt` (Quelle: Canvas; Charakter Dr. Liora Navesh v1; TIMESTAMP: 2025-10-16_03:25).
- Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-10-000Z.flags.txt` (vorsichtig_behandeln; Grund: [FR-KNOWLEDGE] wahren; H-47/SÜDFRAGMENT gegen [EVENT-TIMELINE] prüfen; Arkologie_A1 Taxonomie mit Cluster/Relations harmonisieren).
- RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-00-000Z.txt` (Quelle: Canvas; Charakter Varek Solun v1; TIMESTAMP: 2025-10-16_03:25).
- Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: [FR-KNOWLEDGE] wahren; H-47-Routenstatus prüfen; Standort-Taxonomie H12 vs „Sektor_H3“ harmonisieren vor Promotion).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T08-07-00-000Z.txt` (Quelle: Canvas; Relationslog Novapolis v1; TIMESTAMP: 2025-10-16_08:07).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T08-07-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Namens-/ID-Drift - System „novapolis_logistik_v1“ vs. Schema `logistik_novapolis_v*`; Händlerkontakt „Senn Daru“ unbekannt; gegen Händlergilde-Kanon prüfen/normalisieren).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T11-05-00-000Z.txt` (Quelle: Canvas; AI Behavior Index v2; TIMESTAMP: 2025-10-16_11:05).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T11-05-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Globales Matrix-Canvas - Versionsabgleich mit [BEHAVIOR-VERSION] und `ai_psymatrix_index_v1`; Modifikatoren-/Code-Format vereinheitlichen, Mappings dokumentieren).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T05-34-00-000Z.txt` (Quelle: Canvas; Ereignislog Weltgeschehen v1; TIMESTAMP: 2025-10-16_05:34).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T05-34-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Timeline/Namensabgleich - H-47 Identität offen; "Allianz" gegen [SECRECY]/[FR-KNOWLEDGE] prüfen; mit Missionslog/Sim-Woche synchronisieren).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T13-05-00-000Z.txt` (Quelle: Canvas; Logistik Novapolis v2; TIMESTAMP: 2025-10-16_13:05).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T13-05-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Konsistenzprüfung Link-Graph v2; Curation vormerken).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T12-55-00-000Z.txt` (Quelle: Canvas; Logistik C6 v2; TIMESTAMP: 2025-10-16_12:55).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T12-55-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Verknüpfungen referenzieren `logistik_novapolis_v1` trotz v2; vor Promotion angleichen/begründen).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T12-30-00-000Z.txt` (Quelle: Canvas; Inventar C6 v2; TIMESTAMP: 2025-10-16_12:30).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T12-30-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Systemverknüpfungen referenzieren `logistik_novapolis_v1`; v2-Set angleichen oder begründen).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T12-00-00-000Z.txt` (Quelle: Canvas; Station D5 - Basis (legacy)); TIMESTAMP: 2025-10-16_12:00).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T12-00-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Legacy-Snapshot; mit D5 v2.1/Kanon abgleichen, erst danach promoten).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T14-12-00-000Z.txt` (Quelle: Canvas; Charakter Jonas v2; TIMESTAMP: 2025-10-16_14:12).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T14-12-00-000Z.flags.txt` (vorsichtig_behandeln, korrupt; Grund: Konflikt mit Kanon [JONAS-SIS] - Schwester gilt als vermisst/unklar, nicht tot; bei Ingest normalisieren und Review-Hinweis setzen).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T14-56-20-000Z.txt` (Quelle: Canvas; Charakter Arlen Dross v2; TIMESTAMP: 2025-10-16_14:56).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T14-56-20-000Z.flags.txt` (vorsichtig_behandeln; Grund: Führungs-/Titel-Overlap mit Kora/Marven, vor Promotion klären).

Done Log (Novapolis-RP)
=======================

**Hinweis (2025-10-29):** Dieses Done-Log liegt nun unter `novapolis-dev/docs/donelog.md`. Historische Einträge behalten Bezüge auf den "Development-Hub" inhaltlich bei, ohne die alten Pfadangaben.

2025-10-23
- Workspace-Struktur auf F:\Novapolis-RP erstellt (00-admin, 01-canon, 02-characters, 03-locations, 04-inventory, 05-projects, 06-scenes, 99-exports).
- README.md, todo.md, donelog.md angelegt.
- Memory-Bundle und System-Prompt vorbereitet (00-admin/).
- Erste Charakter-/Orts-/Projektdateien werden als Templates folgen.

2025-10-27
- Curation-Staging eingerichtet: `database-curated/` mit `staging/` und `final/`.
- Leitfäden und Manifest ergänzt (`database-curated/README.md`, `database-curated/staging/README.md`, `database-curated/staging/manifest.json`).
- Erste Datei zur Bearbeitung vorgemerkt: `database-raw/99-exports/chat-export (1).txt` (Status: pending).
- Audit-Tools hinzugefügt: `coding/tools/curation/text_stats.py`, `segment_hash.py`, `delta_report.py`.
- Reports erzeugt unter `database-curated/staging/reports/`:
  - `text-stats.md` (Zeilen/Bytes/Tokens)
  - `segment-hash-w5.txt` (5-Zeilen-Window Dupe-Hashes)
  - `delta-*.md` (Vergleiche zwischen Exportständen)
- Normalisierung & Chunking durchgeführt:
  - `database-curated/staging/chat-export (1).normalized.txt`
  - Re-Chunking: 500-Zeilen-Chunks (`database-curated/staging/chunks/chat-export (1)/chat-export (1).part-*.txt`, 22 Chunks)
  - `database-curated/staging/chunks/chat-export (1)/index.json`
  - Views: `database-curated/staging/recent-500.txt`, `recent-1000.txt`, Reverse-Chunks unter `.../reverse/`
  - Unklarheiten-Liste erstellt: `database-curated/staging/reports/uncertainties.md`
  - Kanon-Canvas (Draft) vorbereitet: `database-rp/00-admin/canon-canvas.draft.md` (vorläufig, kein Wiedereinstiegspunkt)

- ToDo aktualisiert: JSONL als optional/pausiert markiert; TXT-Normalisierung + 500er-Chunks (Index/Views) vermerkt; Review-Aufgabe „part-021 annotieren“ ergänzt (`novapolis-dev/docs/todo.md`).
 - Review erweitert: Abschnitt für `Chunk part-021 (global 10001-10500)` mit [FACT?]/[OPEN] hinzugefügt in `database-curated/staging/chat-export (1).review.md`.
 - Unklarheiten mit Evidenz angereichert (Fraktionen, Layout/2t-Aufzug, Tunnel-Länge, Energie/Logistik-Verknüpfungen, Day-Switch, A/T/S/D, Draisine): `database-curated/staging/reports/uncertainties.md` aktualisiert.
 - Review weiter ergänzt: `Chunk part-020 (global 9501-10000)` ergänzt (Weekly-Sim/Canvas-Audit, Reflex-Regeln, Anomalien) mit [FACT?]/[OPEN].
 - Unklarheiten erweitert: `database-curated/staging/reports/uncertainties.md` → [CARAVAN-LEADERSHIP].
 - Report hinzugefügt: `database-curated/staging/reports/overlap-arlen-dross.md` (Overlap-Check, Vorschlag Titel-Entzerrung: Arlen als Händler/Vermittler).

2025-10-27 (später)
- Admin-Canvas angelegt: `database-rp/00-admin/Canvas-T+0-Timeline.md` (Tagesanker, Sequenz, Debug-Hinweise, Links)
- Admin-Canvas angelegt: `database-rp/00-admin/Canvas-Admin-Day-Switch-Debug.md` (Tageswechsel-Prozedur, ATSD+Canvas-Zahl, Logs, Testfälle)
- Cross-Links ergänzt: `database-rp/03-locations/C6.md` ↔ `database-rp/01-factions/novapolis/03-locations/C6-Logistik-Policy.md`; Index-Link in `00-admin/Logistik.md` ergänzt

- 2026-02-02 13:17: RP-Refactor: C6/D5 Logistik-Policies aus `database-rp/00-admin` nach `database-rp/01-factions/novapolis/03-locations/` verschoben; Ops aus `00-admin/ops` nach `00-ops` verschoben; Referenzen und `database-rp/index.json` umgebogen.

- 2026-02-02 14:57: RP-Refactor: Fraktionsbezogene Indizes aus `database-rp/00-admin` entfernt (`person_index_np.*`, `Index-Haendlergilde.*`) und in Fraktionspfade verschoben; Referenzen und `database-rp/index.json` aktualisiert.
- Missionslog aktualisiert: Abschnitt „Prozess L.1 - Missionsfluss“ mit Verweis zur C6-Logistik-Policy hinzugefügt
 - AI-Behavior-Mapping angelegt: `database-rp/00-admin/AI-Behavior-Mapping.md` (Zustände/Trigger/Interaktionen: Reflex + Hooks Ronja/Jonas; Links zu Charakter-Canvas)
 - last-updated ergänzt: `novapolis-dev/docs/index.md`, `novapolis-dev/docs/todo.md` (ISO-8601 mit Zeitzone)
 - Karawanen-Canvas angelegt: `database-rp/05-projects/caravan_moves.md` (Zeitplan, Routen, Risiken, Abhängigkeiten, Links)
 - Fraktionsinventar-Gerüste erstellt (Policy Y.1):
  - `database-rp/04-inventory/Novapolis-inventar.md`
  - `database-rp/04-inventory/Arkologie-inventar.md`
  - `database-rp/04-inventory/Schienenbund-inventar.md`
  - `database-rp/04-inventory/Eiserne-Enklave-inventar.md`
  - `database-rp/04-inventory/Haendlerbund-inventar.md`
  - `database-rp/04-inventory/Freie-Gruppen-inventar.md`
 - Personen aktualisiert (2025-10-27T16:58:26+01:00):
  - `database-rp/00-admin/person_index_np.md` - Einträge für Lyra Hest (Stellv. Leitung Zivil/Logistik) und Senn Daru (Händler/Vermittler) ergänzt; last-updated gesetzt.
  - `database-rp/02-characters/Lyra-Hest.md` neu angelegt (Rolle, Zugehörigkeit, Stärken, Notizen, Verlinkungen).
 - Korrektur (2025-10-27T17:02:55+01:00):
  - `database-rp/00-admin/person_index_np.md` - Jonas Merek Zugehörigkeit von C6 → D5 angepasst; Link auf D5 gesetzt; last-updated aktualisiert.

- Personen/Canvas aktualisiert (2025-10-27T17:11:18+01:00):
  - `database-rp/02-characters/Ronja-Kerschner.md` - Canvas umfassend ergänzt (Rollen, Zugehörigkeit/Standort, Wissensstand, Safety, Ziele, Beziehungen, Links); last-updated gesetzt; Cross-Links zu AI-Behavior-Mapping/Missionslog hinzugefügt. Grundlage: `database-curated/staging/reports/uncertainties.md` ([REFLEX-*], [FR-KNOWLEDGE], [JEALOUSY-GLOVES], [REFLEX-DETACH], [ROLES]).

- Behavior/Emotionen präzisiert (2025-10-27T17:32:08+01:00):

- `database-rp/02-characters/Ronja-Kerschner.md` - Consent-Zeile geschärft (Angst→Schutz-Umhüllung möglich; „Stop“=sofort lösen; Rückfrage bei Unklarheit), last-updated aktualisiert.
  - `database-rp/00-admin/AI-Behavior-Mapping.md` - Leitplanke „Affekt-Gewichtung“ ergänzt (Kind-/Gefühlslogik ohne Regelbruch: Stop priorisiert, Training→Rückfrage).
  - `database-rp/02-characters/Reflex.md` - Abschnitt „Emotionale Dynamik (kanonisch)“ hinzugefügt (Beschützertrieb, Verlustangst/Eifersucht, Affekt-Gewichtung, Heuristik statt Regelwissen). Quellen: kuratierte Beschlüsse ([PROXIMITY], [JEALOUSY-GLOVES], [REFLEX-CONTROL]) + RAW-Chat-Passagen (Besitzergreifend/Schutz/Umhüllung, Exo-Idee, Instanz-Überwachung C6).

Behavior/Safety Klarstellungen (2025-10-27T17:55:04+01:00)
- `database-rp/02-characters/Ronja-Kerschner.md`: Consent-Gate erweitert um „Überreaktionen kurz/reversibel; danach Rückfrage/Regulation; Sprache priorisiert (außer unmittelbare Gefahr)“; kleiner „Signals“-Block (Request/Stop) ergänzt. RAW-Evidenz: Chat ~251 (Dämpfung testen), ~413 (Stufe I/Neopren), ~847 (gewünschte Kontrolle), ~3619-3624 (Coverage/Stop), ~3252 (Handschutz), ~2094/2428 (Instanz/Ort).
- `database-rp/02-characters/Reflex.md`: Fähigkeit „temporäre sensorische Reduktion (kurz; revert-on-stop)“ ergänzt; Abschnitt „Risiken/Leitplanken (Stufe I)“ mit Overreach-Flag (Hände/Gesicht) + Mitigation/Duration. RAW-Evidenz: Chat ~346/351 (Verlustangst/Verweigerung Lösen), ~3619-3624 (Kontrollüberhang/Stop), ~3252 (Hand/Face), Canvas: ent_d5_reflex_v1 (Stufe I, keine Penetration), char_reflex_v2 (Impulsdämpfung, autonome Reaktion).
- `database-rp/00-admin/AI-Behavior-Mapping.md`: Mikro-Protokolle ergänzt - EPP (Trigger/Aktion/Guardrails/Training-Hook) und „Jealousy-Gloves“ (Face-Coverage nur mit Consent, außer unmittelbare Gefahr). RAW-Evidenz wie oben; Canvas-Verweise: Reflex v2, ent_d5_reflex_v1.

Repo-Sync (2025-10-27T18:10:05+01:00)
- Commit `ffdbf61` gepusht: „chore: Admin/Location/Inventory-Updates + neue Canvases“.
- Umfang: 16 Dateien geändert (277 ⊕, 4 ⊖).
  - Neu: Admin-Canvases `database-rp/00-admin/Canvas-T+0-Timeline.md`, `database-rp/00-admin/Canvas-Admin-Day-Switch-Debug.md`.
  - Neu: Charakter `database-rp/02-characters/Lyra-Hest.md`.
  - Neu: Inventar-Übersichten `database-rp/04-inventory/*-inventar.md` (Novapolis, Arkologie, Schienenbund, Eiserne Enklave, Händlerbund, Freie Gruppen).
  - Neu: Projekte `database-rp/05-projects/caravan_moves.md`.
  - Updates: `novapolis-dev/docs/index.md`, `novapolis-dev/docs/todo.md`, Admin (`database-rp/00-admin/Logistik.md`, `.../Missionslog.md`, `.../person_index_np.md`), Location `database-rp/03-locations/C6.md`.
− Ergebnis: Branch up-to-date, Working Tree clean.

Stempel + Cross-Links (2025-10-27T18:13:52+01:00)
- Admin-Canvases auf ISO-Zeitstempel gebracht:
  - `database-rp/00-admin/Canvas-Admin-Day-Switch-Debug.md`
  - `database-rp/00-admin/Canvas-T+0-Timeline.md`
- `database-rp/00-admin/Logistik.md`: last-updated vereinheitlicht; Links zu Admin-Canvases (Day-Switch & Debug, Timeline T+0) ergänzt.
- `database-rp/02-characters/Lyra-Hest.md`: Front-Matter (`last-updated`) ergänzt; Cross-Links zu Logistik, Missionslog, Personenindex hinzugefügt.

Devcontainer & Lint-Task (2025-10-27)
- Altes Artefakt entfernt: `.devcontainer/devcontainer.json` (am Repo-Root).
- Neuer Devcontainer abgelegt unter `coding/devcontainer/`:
  - `coding/devcontainer/devcontainer.json` (Node 22; installiert `markdownlint-cli2`).
  - `coding/devcontainer/README.md` (Nutzung/ Hinweise).
 - VS Code Task hinzugefügt: `.vscode/tasks.json` → "lint:markdown (docker)" führt `markdownlint-cli2` in einem Node-Docker-Container aus (ohne lokale Node-Installation).
  Hinweis: `.vscode/tasks.json` ist per `.gitignore` (team-Policy) nicht versioniert; lokal nutzbar. Für geteilte Nutzung alternativ Devcontainer öffnen.

VS Code Settings - automatische Freigaben (2025-10-27)
- Workspace-Einstellungen ergänzt (`.vscode/settings.json`):
  - `task.allowAutomaticTasks: "on"` - automatische Tasks erlauben
  - `security.workspace.trust.untrustedFiles: "open"`, `security.workspace.trust.enabled: true` - weniger Blocker bei unbekannten Dateien (nur in vertrauenswürdigen Repos nutzen)
  - `remote.autoForwardPorts: true`, `remote.autoForwardPortsSource: "hybrid"` - Auto-Portforwarding (Remote/Container)
  - `extensions.autoCheckUpdates: true`, `extensions.autoUpdate: true` - Extension-Updates automatisch prüfen/installieren

Systemcheck-Task (2025-10-27)
- Werkzeug ergänzt: `coding/tools/diagnostics/systemcheck.ps1` - prüft Firmware-Virtualisierung, Windows-Features (VirtualMachinePlatform, WSL), WSL-Default-Version/Status sowie Docker-CLI. Ausgabe mit PASS/WARN/FAIL-Hinweisen; nur Diagnose, Exitcode 0.
- VS Code Task hinzugefügt: `.vscode/tasks.json` → "system:check (windows)" (führt das Skript via PowerShell mit `-ExecutionPolicy Bypass` aus).
- Follow-up notiert: Root-Artefakt `.devcontainer/devcontainer.json` ist wieder vorhanden; Entfernung in separatem Cleanup-Commit.

Validierung & CI (2025-10-27)
- Validator-Paket hinzugefügt: `coding/tools/validators/` (Node 20+, Ajv, fast-glob, gray-matter)
  - Skripte: `src/validate-curated.js` (Schema-Check Manifest), `src/validate-rp.js` (Markdown-Basisregeln), `src/check-crossrefs.js` (Szenen↔Chars/Orte/Inventar), `src/validate-all.js` (Aggregator)
  - Schema: `schemas/curated-manifest.schema.json`
- CI aktualisiert: `.github/workflows/validate.yml` installiert Dependencies und führt `npm --prefix coding/tools/validators run validate` aus; anschließend Markdown-Lint.
- VS Code Task ergänzt: `.vscode/tasks.json` → `validate:data (auto)` (Docker bevorzugt, sonst lokal npm) für einheitliche lokale Ausführung.
- Hinweis/README: `coding/tools/validators/README.md` mit Nutzung und empfohlener Szenen-Front-Matter.

Benennung vereinheitlichen (2025-10-27)
- Policy erstellt: `novapolis-dev/docs/naming-policy.md` (ASCII, Bindestrich-Trennung, Umlaute → ae/oe/ue/ss, Endungen klein, keine Leerzeichen/Klammern).
- Name-Linter hinzugefügt: `coding/tools/validators/src/check-names.js` (Scope: `database-rp/**`).
- CI erweitert: Name-Check als zusätzlicher Step in `.github/workflows/validate.yml` (Dry-Run, bricht bei Verstößen ab).
- VS Code Task: `lint:names (auto)` zum lokalen Dry-Run (Docker bevorzugt; alternativ Node/npm).
 - Dry-Run ausgeführt: 0 Verstöße in `database-rp/**` - keine Umbenennungen erforderlich.

Co-Occurrence-Regel (2025-10-27)
- Validator erweitert: `coding/tools/validators/src/check-crossrefs.js` prüft jetzt Bezugspaare in Szenen:
  - Ronja-Kerschner → Reflex
  - Jonas-Merek → Lumen
  - Kora-Malenkov → Echo
- Szenen-Leitfaden aktualisiert: `database-rp/06-scenes/README.md` mit Abschnitt "Co-Occurrence (Bezugspaare)".
- Szene aktualisiert: `database-rp/06-scenes/scene-2025-10-27-a.md` → `characters` um „Lumen“ ergänzt (wegen Jonas→Lumen).
- Charakter-Stubs hinzugefügt: `database-rp/02-characters/Lumen.md`, `.../Kora-Malenkov.md`, `.../Echo.md` (Minimalinhalt, Cross-Links).

Charakter-Canvas vereinheitlicht (2025-10-27)
- Vorlage: `database-rp/02-characters/Ronja-Kerschner.md` als Strukturvorbild (Meta/Rollen/Zugehörigkeit/Wissensstand/Safety/Ziele/Beziehungen/Links)
- Überarbeitet:
  - `database-rp/02-characters/Jonas-Merek.md` - Struktur nach Vorlage; Inhalte/Platzhalter ergänzt
  - `database-rp/02-characters/Lumen.md` - Instanz-spezifische Struktur (Kopplung an Jonas)
  - `database-rp/02-characters/Kora-Malenkov.md` - Leitung C6, Kopplung Echo
  - `database-rp/02-characters/Echo.md` - Instanz-spezifische Struktur (Kopplung an Kora)
  - `database-rp/02-characters/Reflex.md` - Zugehörigkeit/Ziele/Beziehungen/Links ergänzt
  - `database-rp/02-characters/Lyra-Hest.md` - Sektionen/Platzhalter ergänzt
  - `database-rp/02-characters/Senn-Daru.md` - Sektionen/Platzhalter ergänzt

Reflex - Guards & Wissens-/Trainings-Canvases (2025-10-28)
  - `02-characters/Reflex.md`: Meta aktualisiert; Guards unter Kokon/Overreach ergänzt (Lebensgefahr + dynamisches Ausmaß/Dauer; weitere Aspekte werden erlernt).
  - Wissens-/Trainings-Status ausgelagert:
    - `02-characters/Reflex-Wissensstand-Trainingsstand.md`
    - `02-characters/Lumen-Wissensstand-Trainingsstand.md`
    - `02-characters/Echo-Wissensstand-Trainingsstand.md`

Hybrid-Metadaten angereichert (2025-10-28)
- Tool hinzugefügt: `coding/tools/metadata/enrich_metadata.py` (füllt fehlende Felder aus Front-Matter/H1; nicht-destruktiv, Markdown bleibt unverändert).
- Task ergänzt: `.vscode/tasks.json` → `gpt:enrich:metadata` (läuft über `with_lock.ps1`, bevorzugt `.venv`-Python).
- Sidecar-JSON aktualisiert: 241 Dateien angereichert (chapter/characters/locations/tags); zentrale Index-Logik unverändert (append-only).

YAML-Front-Matter Schema & Validator (2025-10-28T18:30:00+01:00)
- Enricher erweitert: YAML-Front-Matter zwischen `---` wird gelesen; JSON-Schema vereinheitlicht (`title/category/slug/version/last_updated/last_change/tags/affiliations/locations/dependencies[/characters]/source`). Legacy-Felder (`chapter`, singulares `location`) werden migriert/entfernt.
- Validator hinzugefügt: `coding/tools/metadata/validate_frontmatter.py` (Pflichtfelder, Kategorie-Spezifika, Slug-Format, ISO-Zeit, Referenzen per Slug). Task: `.vscode/tasks.json` → `gpt:validate:frontmatter`.

Tagging-Pipeline (YAML-getrieben) - erster Lauf (2025-10-28T09:59:20Z)

- Neues Tool: `coding/tools/curation/tag_chunks_from_yaml.py` (lexicon aus Front-Matter; Aliase; line-level Tags [CHAR|LOC|PROJ|ENT], [TIME], [FACT?]; Streaming; Windows-Pfad-safe; optional PyYAML Fallback).
- Ausführung (dry-run): Range 019-016 - Summaries geprüft; Aliase/Slugs validiert; Dateinamensschema `*.part-XYZ.txt` automatisch erkannt.
- Ausführung (write): Ergebnisse unter `database-curated/reviewed/chat-export (1)/` erzeugt:
  - `part-019.tagged.txt`, `part-018.tagged.txt`, `part-017.tagged.txt`, `part-016.tagged.txt`
  - `index_review.json` (per-File Lines/Chars/Tag-Counts/Top-Slugs)
  - `unresolved.json` (Dependencies: echo, reflex-wissensstand-trainingsstand; alias collisions: none)
  - `lexicon.json` (by_slug + aliases Dump)
  - Warnings: `reports/tagging-20251028T095920Z.log` (LOC-only-Hinweise; non-blocking)
- Nächste Schritte: ggf. Alias-Ergänzungen, dann Ranges 015-010 und 009-001 taggen.

Tagging-Pipeline - Heuristiken erweitert + Re-Run 019-016 (2025-10-28T11:10:05Z)

- Ergänzt: N7→c6-nord Kanonisierung (metro-kontextsensitiv, ±3 Zeilen Fenster; Redirects/Deprecated im Lexikon).
- Ergänzt: [NOTE] für Meta-Zeilen (Warnungen für LOC-only unterdrückt), [EVENT] konservativ, [MISSION] Kategorie (C6-Nord, versiegelt/gesperrt/Untersuchung im ±3-Zeilen-Fenster).
- Ergänzt: Sektor-Codes (E3/F1/…) als Fallback-Orte, Titel-Alias-Erweiterung (Vor-/Nachname), Co-Occurrence-Vorschläge (Report-only).
- Retag-Modus: `--retag-in`/`--retag-out` (nur a/b/c Regeln; idempotent).
- Ausführung: 019-016 neu getaggt; `index_review.json`, `unresolved.json`, `lexicon.json` aktualisiert. Logs: `reports/tagging-20251028T111005Z.log` inkl. "Canonicalized N7→c6-nord total: 1".
- Folgearbeiten: Alias-Kollision "C6" (c6 vs c6-nord) entscheiden; fehlende Entities (`Echo`, `Reflex-Wissensstand-Trainingsstand`) anlegen/umbiegen; nächste Ranges 015-010, 009-001.

Sim-Visualisierung angebunden (2025-10-29T15:50:00Z)
2025-11-12 01:38 | Copilot | DONELOG-Sync (Dev-Hub): Frontmatter aktualisiert; zentraler Vorbereitungseintrag vor Repo-weitem Prüfskript (damals PowerShell, inzwischen `python scripts/run_checks_and_report.py`).

Postflight
----------
Meta: Modus=Postflight, Modell=GPT-5, Arbeitsverzeichnis=F:\VS Code Workspace\Main, RepoRoot=F:\VS Code Workspace\Main, PSScriptRoot=F:\VS Code Workspace\Main\scripts, PSVersion=7.5.4, Aufruf=python F:\VS Code Workspace\Main\scripts\run_checks_and_report.py, SHA256=65570151AA983A6A3784D89B589486A214B8A171D1BA22766C1BF17C49F54E30, STOP-Gate=aktiv, Wrapper-Policy=erfüllt, Quellen=F:\VS Code Workspace\Main\.github\copilot-instructions.md;F:\VS Code Workspace\Main\novapolis-dev\docs\donelog.md;F:\VS Code Workspace\Main\scripts\run_checks_and_report.py, Aktion=Automatisierter Checklauf (Dev-Hub Bezug; PowerShell-Variante archiviert)
Prüfung: ruff=FAIL, black=FAIL, markdownlint=FAIL (global), frontmatter=FAIL (global), pyright=FAIL, mypy=FAIL, pytest=STOP (>40 Dateien), coverage=SKIP, PSScriptAnalyzerExit=1
Regeln: IDs=R-WRAP,R-STOP,R-FM,R-LINT,R-CTX,R-SEC,R-LOG,R-COV,R-TIME,R-SAFE,R-IDX
Todos: offen=n/a, BeispielFix=Baseline dokumentiert, ReRun=nach Style/Type-Fixes, Fällig=2025-11-12 01:45

- `novapolis_agent`: FastAPI-Miniserver `app/api/sim.py` ergänzt (`GET /world/state`, `POST /world/step`), Task/Launch für Uvicorn, pytest-Abdeckung (`tests/tests_sim_api.py`).
- `novapolis-sim`: Godot-4-Mini-Client (Autoload `SimClient`, Szene `Main.tscn`) pollt die API und zeigt Tick/Zeit inkl. Status bei Offline-Agent.
- `novapolis-rp`: README-Abschnitt „Visualisierung“ ergänzt; Donelog/TODO synchronisiert.

Godot Headless - Quick Verification (2025-11-16)
--------------------------------------------

- 2025-11-16 04:54: Headless Load: `novapolis-sim/project.godot` geladen headless mit Godot Engine `v4.5.1.stable.official.f62fdbde1` — Ladeprobe PASS. Log: `.tmp-results/logs/godot_headless_20251116_045407.log`. Kurzer Scan auf Schlüsselwörter (`ERROR|ERR|CRITICAL|WARNING|Traceback`) ergab keine Treffer. (Scan & Log im Repo: siehe Pfad oben.)




