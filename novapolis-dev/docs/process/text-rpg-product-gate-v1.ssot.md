---
stand: 2026-04-14 21:08
update: Das Product Gate prueft jetzt zusaetzlich den gemeinsamen Turn-, Resume- und Replay-Rahmen fuer Sim-vor-RP gegen Sessionvertrag und Slice-2-Handover.
checks: markdownlint=PASS; frontmatter=PASS; todo-index-sync=PASS
---

Text-RPG Product Gate v1
========================

Zweck
-----

Diese SSOT definiert den kanonischen technischen Freigabepfad fuer den ersten spielbaren Text-RPG-Slice. Der Gate-Pfad verbindet RP-Quellstand, Sessionvertrag, Agent-Pruefung, Log-/Replay-Vertrag und Sim-Smoke zu einem reproduzierbaren Produktlauf.

Scope
-----

- RP-Start- und Folgekorridor-SSOTs fuer den aktuellen Produktpfad
- Agent-Sessionvertrag und Runbook
- Sim-/Replay-Anschluss fuer denselben Slice

Quellenbasis
------------

- `novapolis-dev/docs/specs/text-rpg-session-contract-v1.md`
- `novapolis-dev/docs/specs/annotation-spec.md`
- `novapolis-dev/docs/specs/scheduler-spec.md`
- `novapolis_agent/docs/runbook.md`
- `novapolis-dev/docs/process/rp-text-rpg-startpaket-slot-00-05-2026-04-05.md`
- `novapolis-dev/docs/process/rp-folgekorridor-slot-00-05.ssot.md`
- `novapolis-dev/docs/process/rp-folgekorridor-slot-06-10.ssot.md`
- `novapolis-dev/docs/process/rp-folgekorridor-slot-11-15.ssot.md`
- `novapolis-dev/docs/process/rp-folgekorridor-slot-16-20.ssot.md`
- `novapolis-dev/docs/process/rp-folgekorridor-slot-21-25.ssot.md`
- `novapolis-dev/docs/process/rp-folgekorridor-slot-26-30.ssot.md`
- `novapolis-dev/docs/process/rp-folgekorridor-slot-31-35.ssot.md`
- `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md`

Wahrheitsrahmen
---------------

- Das Product Gate hat jetzt einen kanonischen Wrapper-Task `Checks: text-rpg product gate`; die Einzel-Tasks bleiben fuer Diagnose und Teilretries erhalten.
- Die feste Referenz-Session unter `novapolis_agent/eval/config/text_rpg_reference_session.v1.json` liefert einen deterministischen Artefaktbeleg fuer Savegame, `world_log`, `pc_log` und Replay-Manifest.
- Der GM-Session-Teil bleibt runtime-gebunden: ohne erreichbare lokale Modellruntime am produktiven Chat-Pfad scheitert dieser Gate-Abschnitt weiterhin hart.
- Die Gate-Definition bleibt verbindlich: neue Runtime- oder Sim-Artefakte muessen sich an diesen Ablauf haengen, nicht umgekehrt.
- Der gemeinsame Folgeanker hinter `slot 30` heisst `Text-RPG Slice 2 Handover v1`; spaetere Gate- und Referenzfaelle hinter dem ersten Slice muessen an dieselbe SSOT haengen statt einen freien Zweitpfad zu eroeffnen.

Slice-2-Handover
----------------

- `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md` ist die gemeinsame Quelle fuer den Folgepfad hinter `slot 30`.
- Das Product Gate selbst erweitert damit noch keinen neuen Runtime-Block, benennt aber verbindlich, auf welchen Handover spaetere RP-, Agent- und Sim-Folgearbeit referenzieren muessen.
- `novapolis-dev/docs/process/rp-folgekorridor-slot-31-35.ssot.md` fuehrt den ersten fachlichen Ausbau dieses Handover jetzt als vierte Kampagnenstufe aus.
- Sobald Sim den Resume-Anker operativ nutzt, wird derselbe Handover auch fuer den naechsten Produkt-Gate-Ausbau vollstaendig ueber RP, Agent und Sim belegt.

Kanonischer Gate-Block
----------------------

Der Produktlauf heisst verbindlich `Text-RPG Product Gate v1`.

Aktueller operativer Wrapper-Task:

1. `Checks: text-rpg product gate`

Der Wrapper fuehrt aktuell diese Stufen in derselben kanonischen Reihenfolge aus:

1. `Checks: full`
2. `Tests: pytest (api+streaming)`
3. `Tests: text-rpg reference session`
4. `Checks: sim epoch assets`
5. `Eval: suite gm_session (12, asgi)`
6. `Eval: summarize gm session KPIs`

Die einzelnen Task-Labels bleiben weiterhin als diagnostische Teilpfade verfuegbar. Der Gate-Name bleibt die kanonische Klammer fuer Board, Runbook und Wrapper-Skript.

Gate-Stufen
-----------

### Stufe 1 - RP-Quellstand und Pfadkontinuitaet

- Startpaket, Reveal-Matrizen und der aktuelle Folgekorridor muessen denselben Produktpfad abbilden.
- Hard Fail bei fehlender Anschluss-SSOT, widerspruechlichem Slot-Fortschritt oder nicht mehr belegten Startpfaden.

### Stufe 2 - Sessionvertrags-Drift

- Der Sessionvertrag v1 ist die kanonische Quelle fuer Session-, Slot- und Patchrahmen.
- Hard Fail bei Drift zwischen Runbook, spaeteren API-Modellen und dem vertraglich benoetigten Kernset aus `campaign_id`, `session_id`, `scene_id`, `slot_id`, `turn_id`, `options`, `state_patches`.
- Hard Fail ebenfalls, wenn der operative Lauf den jetzt kanonischen Turn-Rahmen (`turn_window_minutes=30`, optionales Verdichtungsfenster mit `tick_minutes=1`, `resume_checkpoint_id`, `carry_over`) nicht auf denselben Vertragsblock legt.

### Stufe 3 - Agent-API- und Streaming-Smoke

- Der Agent-Pfad muss mindestens die API-/Streaming-Gates gruen halten.
- Hard Fail bei OpenAPI-/Schema-Drift, Streaming-Regressionen oder fehlendem Grundpfad fuer den Sessionbetrieb.

### Stufe 4 - Log- und Replay-Vertrag

- Die feste Referenz-Session muss `world_log`, `pc_log`, `state_patches`, `savegame.json` und `replay_manifest.json` fuer denselben Slice deterministisch erzeugen und verifizieren.
- Hard Fail bei fehlenden Artefakten, ungueltigen `state_patches`, Slot-Mismatch zwischen Logs oder Replay-Widerspruechen.
- Hard Fail ebenfalls, wenn `resume_checkpoint_id`, letzter stabiler `turn_id`, `slot_id` oder eingebettete Verdichtungssegmente desselben Turns zwischen Savegame, Logs und Replay auseinanderlaufen.
- Produktive Chat-Laeufe duerfen spaeter weitere Artefakte erzeugen, muessen aber denselben Vertrags- und Dateirahmen halten wie die Referenz-Session.

### Stufe 5 - Sim-Anschluss

- Der Sim-Pfad muss mindestens denselben Slice als Smoke sichtbar pruefen koennen.
- Hard Fail bei ungueltigen Slotwerten, nicht lesbaren Epoch-Dateien oder Artefakten ausserhalb des vertraglichen Session-/Slot-Rahmens.
- Hard Fail ebenfalls, wenn Sim fuer denselben Lauf einen parallelen Turn- oder Resume-Pfad fuehrt statt `slot_id`, `turn_id`, `resume_checkpoint_id` und denselben RP-Startanker aus Sessionvertrag und RP-Produkt-SSOT zu nutzen.

### Stufe 6 - GM-Session-Eval und KPI-Triage

- Der produktive Slice muss zusaetzlich denselben Sessionpfad ueber die dedizierte Suite `gm_session` pruefen.
- Die KPI-Summary muss auf genau die Resultatdatei desselben Gate-Laufs zeigen und Blocker-Faelle von Beobachtungen trennen.
- Hard Fail bei nicht erreichbarer Modellruntime, fehlender Resultatdatei oder fehlender KPI-Summary fuer den aktuellen Lauf.

Gate-Erfolg
-----------

`Text-RPG Product Gate v1` gilt nur dann als PASS, wenn:

- RP-Pfad, Sessionvertrag und Runbook denselben Slice beschreiben,
- die aktuelle Agent-API-/Streaming-Pruefung gruen ist,
- die feste Referenz-Session fuer denselben Slice Artefakte und Replay-Vertrag gruen bestaetigt,
- der gemeinsame Turn-, Verdichtungs- und Resume-Rahmen zwischen Sessionvertrag, Replay und Sim nicht driftet,
- der Sim-Asset-/Epoch-Pfad fuer denselben Slice nicht widerspricht,
- der `gm_session`-Eval-Lauf eine Ergebnisdatei fuer denselben Gate-Lauf erzeugt,
- und die KPI-Summary auf genau diese Resultatdatei verweist.

Runbook-Verankerung
-------------------

Das Runbook fuehrt denselben Gate-Namen und denselben operativen Task-Block. Ein spaeterer dedizierter Wrapper oder Task darf den Ablauf vereinfachen, aber nicht semantisch veraendern.
Das Runbook fuehrt denselben Gate-Namen, denselben Wrapper-Task und dieselbe Referenz-Session-Datei. Diagnose-Tasks duerfen kuerzer sein, aber nicht vom Gate-Vertrag abweichen.

Guardrails
----------

- Kein separater Produkt-Gate-Pfad fuer Agent, RP und Sim mit voneinander abweichenden Slice-Namen.
- Kein Replay- oder Logformat ausserhalb des Sessionvertrags v1.
- Kein Gate-PASS nur auf Basis isolierter Lint-/Pytest-Ergebnisse ohne RP- und Sim-Bezug.

Definition of Done
------------------

- Der End-to-End-Gate-Pfad besitzt einen kanonischen Namen.
- Board, Runbook, Tasking und Produktdoku verweisen auf denselben Wrapper-Task.
- Die feste Referenz-Session ist als aktive Gate-Datei dokumentiert.
- Die harten Fail-Klassen fuer Vertrags-, Log-, Slot- und GM-Runtime-Drift sind benannt.
- Der Pfad ist technisch automatisiert, ohne den lokalen Modellruntime-Bedarf des GM-Eval-Teils zu verschweigen.
