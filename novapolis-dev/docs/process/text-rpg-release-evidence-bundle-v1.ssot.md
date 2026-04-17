---
stand: 2026-04-18 00:55
update: Diese SSOT zieht fuer den ersten Text-RPG-Vertikalslice jetzt die gemeinsamen Release-Belege aus Quality-Run, Product Gate, Referenzfaellen, Sim-Export und Workspace-Status zusammen.
checks: snapshot-lock PASS (2026-04-18 00:55); markdownlint=PASS; frontmatter=PASS
---

Text-RPG Release Evidence Bundle v1
===================================

Zweck
-----

Diese SSOT zieht die bislang getrennten Freigabebelege fuer den ersten suiteweiten Text-RPG-Vertikalslice zu einem einzigen Release-Pfad zusammen. Sie verhindert, dass Root, Product Gate, Runbook und Sim-Export denselben Freigabestand nur indirekt oder mit unterschiedlichen Mindestannahmen lesen.

Scope
-----

- repoweite Quality-Baseline des aktuellen Workspace-Stands
- produktbezogene Gate- und Referenzbelege fuer den ersten Text-RPG-Slice
- Sim-seitiger Export- und Laufzeitbeleg ausserhalb des Editors
- Root- und Dev-Protokollierung des Freigabestands

Nicht-Ziele
-----------

- keine neue Parallel-Gate-Definition neben `Text-RPG Product Gate v1`
- kein Ersatz fuer `standalone-beta-gates.ssot.md`
- keine CI-Automatisierung des Godot-Exports in diesem Lauf

Kanonische Bundle-Bausteine
---------------------------

### 1. Repoweite Baseline

- Pflichtbeleg: `Checks: full`
- Erwartung: der aktuelle Repo-Stand bleibt ueber Lint, Typing, Tests, Coverage und Doku-Gates gruen.
- Referenzquelle fuer die Reportkette bleibt `.tmp/results/reports/checks_report_*.md`.

### 2. Produkt-Gate

- Pflichtbeleg: `Checks: text-rpg product gate`
- Erwartung: derselbe Vertikalslice bleibt ueber RP-Pfad, Sessionvertrag, Referenzartefakte, Sim-Anschluss und `gm_session`-Triage konsistent.
- Zielquelle bleibt `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md`.

### 3. Deterministische Referenzfaelle

- Pflichtbeleg: `Tests: text-rpg reference session`
- Referenzfaelle:
  - `novapolis_agent/eval/config/text_rpg_reference_session.v1.json`
  - `novapolis_agent/eval/config/text_rpg_reference_session_handover_slot31_40.v1.json`
- Erwartung: `savegame.json`, `world_log.jsonl`, `pc_log.jsonl`, `replay_manifest.json` und die Slot-/Turn-Anker bleiben fuer Basislauf und Handover-Folgefall konsistent.

### 4. Sim-Release-Beleg

- Pflichtbeleg: Export-Smoke nach `novapolis-dev/docs/process/sim-export-release-path.ssot.md`
- Vorlauf: `Checks: sim headless verify`
- Laufzeitbeleg: `novapolis-sim/exports/windows/NovapolisSim.exe` startet ohne Editor-Overlay, laedt Hub-Oberflaeche und reagiert in einem kurzen Bedienpfad konsistent.

### 5. Workspace- und Release-Protokollierung

- Pflichtbelege:
  - `WORKSPACE_STATUS.md`
  - `novapolis-dev/docs/donelog.md`
  - `DONELOG.md`
- Erwartung: Release-Stand, Reportbezug und offene Restrisiken werden nicht nur implizit im Repo belassen, sondern sichtbar in Root- und Dev-Protokollen festgehalten.

Bundle-Reihenfolge
------------------

1. `Checks: full`
2. `Checks: text-rpg product gate`
3. `Tests: text-rpg reference session` fuer denselben Stand absichern
4. Sim-Export und den exportierten Smoke gemaess `sim-export-release-path.ssot.md` durchziehen
5. Release-Status in `WORKSPACE_STATUS.md`, `novapolis-dev/docs/donelog.md` und `DONELOG.md` protokollieren

Release-Reife und harte Grenzen
-------------------------------

- Ein isolierter PASS von `Checks: full` ist fuer diesen Slice nicht release-ausreichend.
- Ein isolierter PASS von `Checks: text-rpg product gate` ist fuer diesen Slice ebenfalls nicht release-ausreichend.
- Ohne erreichbare lokale Modellruntime fuer `Eval: suite gm_session (12, asgi)` bleibt das Bundle unvollstaendig, selbst wenn alle statischen oder deterministischen Belege gruen sind.
- Ohne exportierten Windows-Smoke fuer `novapolis-sim/exports/windows/NovapolisSim.exe` bleibt das Bundle unvollstaendig, selbst wenn Editor- und Headless-Smokes gruen sind.
- Clean-Checkout-Belege wie `--allow-empty` beim Sim-Offline-Check bleiben zulaessig fuer Grundvalidierung, ersetzen aber nicht die Release-Laufzeit fuer den produktiven Slice.

Verknuepfte Istquellen
----------------------

- `README.md`
- `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md`
- `novapolis_agent/docs/runbook.md`
- `novapolis-dev/docs/process/sim-export-release-path.ssot.md`
- `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md`
- `WORKSPACE_STATUS.md`
- `novapolis-dev/docs/donelog.md`
- `DONELOG.md`

Definition of Done
------------------

- Root-README, Product Gate, Runbook und Sim-Export-SSOT zeigen auf dieselbe Bundle-Quelle.
- Die Bundle-Quelle nennt dieselben Pflichtbelege fuer Quality, Product Gate, Referenzfaelle, Export-Smoke und Protokollierung.
- Die Release-Reife grenzt klar ab, welche Teile ohne lokale Modellruntime oder ohne exportierten Sim-Smoke nicht als fertig gelten.