---
stand: 2026-04-07 11:46
update: Das Text-RPG Product Gate v1 referenziert jetzt den erweiterten RP-Produktpfad bis `slot 30` als kanonischen Folgekorridor.
checks: snapshot-lock PASS (2026-04-07 11:46); markdownlint PASS; frontmatter PASS
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

Wahrheitsrahmen
---------------

- Das Product Gate ist aktuell ein definierter Standardlauf, noch kein voll automatisierter Ein-Klick-Wrapper.
- Bis echte Session-Artefakte produktiv erzeugt werden, bleibt ein Teil des Gates dokument- und vertragsgetrieben.
- Die Gate-Definition ist trotzdem verbindlich: neue Runtime- oder Sim-Artefakte muessen sich an diesen Ablauf haengen, nicht umgekehrt.

Kanonischer Gate-Block
----------------------

Der Produktlauf heisst verbindlich `Text-RPG Product Gate v1`.

Aktueller operativer Task-Block:

1. `Checks: full`
2. `Tests: pytest (api+streaming)`
3. `Checks: sim epoch assets`

Diese drei vorhandenen Task-Labels bilden die aktuelle ausfuehrbare Huelle. Der Gate-Name selbst bleibt die kanonische Klammer fuer Board, Runbook und spaetere Wrapper-Skripte.

Gate-Stufen
-----------

### Stufe 1 - RP-Quellstand und Pfadkontinuitaet

- Startpaket, Reveal-Matrizen und der aktuelle Folgekorridor muessen denselben Produktpfad abbilden.
- Hard Fail bei fehlender Anschluss-SSOT, widerspruechlichem Slot-Fortschritt oder nicht mehr belegten Startpfaden.

### Stufe 2 - Sessionvertrags-Drift

- Der Sessionvertrag v1 ist die kanonische Quelle fuer Session-, Slot- und Patchrahmen.
- Hard Fail bei Drift zwischen Runbook, spaeteren API-Modellen und dem vertraglich benoetigten Kernset aus `campaign_id`, `session_id`, `scene_id`, `slot_id`, `turn_id`, `options`, `state_patches`.

### Stufe 3 - Agent-API- und Streaming-Smoke

- Der Agent-Pfad muss mindestens die API-/Streaming-Gates gruen halten.
- Hard Fail bei OpenAPI-/Schema-Drift, Streaming-Regressionen oder fehlendem Grundpfad fuer den Sessionbetrieb.

### Stufe 4 - Log- und Replay-Vertrag

- Sobald Session-Artefakte vorliegen, muessen `world_log`, `pc_log` und `state_patches` als gemeinsamer Lauf pruefbar sein.
- Hard Fail bei fehlenden Artefakten, ungueltigen `state_patches`, Slot-Mismatch zwischen Logs oder Replay-Widerspruechen.
- Solange diese Artefakte noch nicht produktiv erzeugt werden, bleibt diese Stufe als definierter Pflichtblock fuer die naechste Implementierungswelle bestehen.

### Stufe 5 - Sim-Anschluss

- Der Sim-Pfad muss mindestens denselben Slice als Smoke sichtbar pruefen koennen.
- Hard Fail bei ungueltigen Slotwerten, nicht lesbaren Epoch-Dateien oder Artefakten ausserhalb des vertraglichen Session-/Slot-Rahmens.

Gate-Erfolg
-----------

`Text-RPG Product Gate v1` gilt nur dann als PASS, wenn:

- RP-Pfad, Sessionvertrag und Runbook denselben Slice beschreiben,
- die aktuelle Agent-API-/Streaming-Pruefung gruen ist,
- der Sim-Asset-/Epoch-Pfad fuer denselben Slice nicht widerspricht,
- und neue Session-/Replay-Artefakte spaeter ohne Parallelvertrag an denselben Gateblock andocken.

Runbook-Verankerung
-------------------

Das Runbook fuehrt denselben Gate-Namen und denselben operativen Task-Block. Ein spaeterer dedizierter Wrapper oder Task darf den Ablauf vereinfachen, aber nicht semantisch veraendern.

Guardrails
----------

- Kein separater Produkt-Gate-Pfad fuer Agent, RP und Sim mit voneinander abweichenden Slice-Namen.
- Kein Replay- oder Logformat ausserhalb des Sessionvertrags v1.
- Kein Gate-PASS nur auf Basis isolierter Lint-/Pytest-Ergebnisse ohne RP- und Sim-Bezug.

Definition of Done
------------------

- Der End-to-End-Gate-Pfad besitzt einen kanonischen Namen.
- Board, Runbook und Produktdoku verweisen auf denselben Gate-Block.
- Die harten Fail-Klassen fuer Vertrags-, Log- und Slot-Drift sind benannt.
- Der Pfad ist fuer eine spaetere technische Automatisierung vorbereitet, ohne den aktuellen Ist-Stand zu ueberbehaupten.