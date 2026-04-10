---
stand: 2026-04-10 13:22
update: Diese SSOT zieht den Folgepfad hinter slot 30 als gemeinsamen Handover fuer Root, RP, Agent und Sim auf denselben Namen und Vertragsrahmen.
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=FAIL; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=FAIL; black=FAIL; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260410_131501.md
---

Text-RPG Slice 2 Handover v1
============================

Zweck
-----

Diese SSOT fixiert den gemeinsamen Handover hinter `slot 30` fuer den naechsten produktiven Text-RPG-Ausbau. Sie verhindert, dass Root, RP, Agent und Sim denselben Anschluss mit unterschiedlichen Namen, freien Zusatzannahmen oder voneinander geloesten Resume-Pfaden weiterfuehren.

Gemeinsamer Name
----------------

- Der Folgepfad hinter `slot 30` heisst verbindlich `Text-RPG Slice 2 Handover v1`.
- Root-Backlog, Product Gate, Agent-Runbook, RP-Folgekorridor und Sim-Folgearbeit verwenden denselben Namen fuer diesen Uebergang.

Quellenbasis
------------

- `novapolis-dev/docs/process/rp-folgekorridor-slot-31-35.ssot.md`
- `novapolis-dev/docs/process/rp-folgekorridor-slot-26-30.ssot.md`
- `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md`
- `novapolis-dev/docs/specs/text-rpg-session-contract-v1.md`
- `novapolis_agent/docs/runbook.md`
- `novapolis-sim/scripts/Main.gd`

Handover-Anker
--------------

- `slot 30` bleibt der kanonische Abschluss- und Wiederanlaufpunkt des ersten belegten Produktpfads.
- Der Handover nutzt denselben Sessionvertrag wie der erste Slice: `campaign_id`, `session_id`, `scene_id`, `slot_id`, `turn_id`, `state_patches`, `world_log`, `pc_log` und `replay_manifest.json` bleiben die verbindlichen Vertragsanker.
- `resume_checkpoint_id` ist der operative Resume-Hebel fuer Sim- und Replay-Folgearbeit; er darf nicht als rein dekoratives Label behandelt werden.
- Die belegten Anschlussraeume bleiben fuer diesen Handover auf `D5`, `C6`, `G7`, `E2` und `F1` beschraenkt, bis eine spaetere RP-SSOT weitere Raeume explizit freigibt.

Modulrollen
-----------

### Root

- Root fuehrt nur den gemeinsamen Handover und verweist fuer Ausgestaltung auf RP-, Agent- und Sim-SSOTs.
- Root darf keinen zweiten, freieren Namen fuer denselben Folgepfad etablieren.

### RP

- RP fuehrt den Handover entweder als `slot 31-35` oder als explizit modulare Episode auf demselben Vertragsrahmen fort.
- Reveal-, Missions- und Ortsbezug bleiben an die bereits belegten Raeume und den bestehenden Produktpfad gebunden.
- Der erste konkrete Ausbau liegt jetzt in `novapolis-dev/docs/process/rp-folgekorridor-slot-31-35.ssot.md`.

### Agent

- Product Gate, Referenz-Session und Runbook muessen den Handover als naechsten gemeinsamen Ausbau hinter `slot 30` benennen.
- Neue Gate- oder Referenzfaelle hinter `slot 30` duerfen nur auf demselben Session- und Artefaktvertrag aufbauen.

### Sim

- Der Hub muss `resume_checkpoint_id` und `replay_manifest` aus demselben Sessionvertrag fuer den Handover nutzbar machen.
- Replay-/Resume-Bedienung darf keinen parallelen Artefaktpfad neben dem bestehenden Session-Store aufziehen.

Artefakt- und Gate-Vertrag
--------------------------

- `savegame.json`, `world_log.jsonl`, `pc_log.jsonl` und `replay_manifest.json` bleiben der verpflichtende Artefaktkern.
- Der Handover gilt nur dann als sauber, wenn RP-Folgekorridor, Product Gate, Runbook und Sim-Folgearbeit denselben Resume-Anker benutzen.
- Diagnose- oder Hygiene-Arbeit in Dev und Agent darf den Namen oder Vertragsrahmen des Handover nicht still umbiegen.

Guardrails
----------

- Kein zweiter Slice-2-Name neben `Text-RPG Slice 2 Handover v1`.
- Keine freien neuen Stationen, Fraktionen, Crews oder Tiefennetzpfade fuer den Handover.
- Kein neuer Replay- oder Resume-Pfad ausserhalb des bestehenden Sessionvertrags.
- Kein Gate-PASS hinter `slot 30`, der nur auf einzelnen Tests beruht, ohne den Resume- und Artefaktvertrag mitzudenken.

Definition of Done
------------------

- Root-Backlog, Product Gate und Agent-Runbook verweisen auf diese SSOT.
- RP- und Sim-Folgepunkte benennen denselben Handover statt freier Folgeformeln.
- Der weitere Ausbau hinter `slot 30` bleibt auf demselben Session- und Artefaktvertrag verankert.
- Der erste fachliche Ausbau hinter `slot 30` liegt als eigene RP-SSOT fuer `slot 31-35` oder als gleichwertige modulare Episode vor.
