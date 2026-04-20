---
stand: 2026-04-20 21:22
update: Das Product Gate fuehrt jetzt auch die kanonische Handover-Kurzformel hinter slot 30 und den gemeinsamen Release-Evidence-Pfad fuer den ersten Vertikalslice.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260420_210436.md
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
- `novapolis-dev/docs/process/rp-folgekorridor-slot-36-40.ssot.md`
- `novapolis-dev/docs/process/rp-folgekorridor-slot-41-45.ssot.md`
- `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md`

Wahrheitsrahmen
---------------

- Das Product Gate hat jetzt einen kanonischen Wrapper-Task `Checks: text-rpg product gate`; die Einzel-Tasks bleiben fuer Diagnose und Teilretries erhalten.
- Der Referenzlauf unter `novapolis_agent/scripts/run_text_rpg_reference_session.py` validiert jetzt zwei deterministische Artefaktfaelle: den D5-Basisfall unter `novapolis_agent/eval/config/text_rpg_reference_session.v1.json` und den Handover-Folgefall unter `novapolis_agent/eval/config/text_rpg_reference_session_handover_slot31_40.v1.json`.
- Der GM-Session-Teil bleibt runtime-gebunden: ohne erreichbare lokale Modellruntime am produktiven Chat-Pfad scheitert dieser Gate-Abschnitt weiterhin hart.
- Die Gate-Definition bleibt verbindlich: neue Runtime- oder Sim-Artefakte muessen sich an diesen Ablauf haengen, nicht umgekehrt.
- Der gemeinsame Folgeanker hinter `slot 30` heisst `Text-RPG Slice 2 Handover v1`; spaetere Gate- und Referenzfaelle hinter dem ersten Slice muessen an dieselbe SSOT haengen statt einen freien Zweitpfad zu eroeffnen.

Produktfokus des Gates
----------------------

- Der erste suiteweite Vertikalslice heisst verbindlich `Hub -> Spielhauptmenue -> Charakterstart -> erster Vollturn -> turn_resume_ready`.
- Der kleinste stabile Save-Punkt ist das erste `turn_resume_ready` nach einem voll ausgespielten ersten Turn; vor diesem Zustand gibt es keinen zugesagten Resume-Anker.
- Replay-Zweck bleibt Nachvollzug und Wiedereinstiegshilfe fuer denselben Lauf und nicht ein paralleler Fortschrittspfad.
- Gate-blockend fuer diesen Schnitt sind vor allem drei Kernelemente: KI-gestuetzter Charakterstart, sichtbarer erster Vollturn mit `Szene/Konsequenz/Optionen/State_Patches`, Save-/Resume-/Replay-Bruecke ab `turn_resume_ready`.
- Bewusst spaeter und damit aktuell nicht eigener Gate-Fokus sind breitere Startauswahl, aktive RP-Integration hinter `slot 30` sowie Komfort-/Atmosphaereausbau.

Slice-2-Handover
----------------

- `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md` ist die gemeinsame Quelle fuer den Folgepfad hinter `slot 30`.
- Das Product Gate selbst erweitert damit noch keinen neuen Runtime-Block, benennt aber verbindlich, auf welchen Handover spaetere RP-, Agent- und Sim-Folgearbeit referenzieren muessen.
- `novapolis-dev/docs/process/rp-folgekorridor-slot-31-35.ssot.md` fuehrt den ersten fachlichen Ausbau dieses Handover als vierte Kampagnenstufe aus.
- `novapolis-dev/docs/process/rp-folgekorridor-slot-36-40.ssot.md` fuehrt denselben Vertragsrahmen jetzt als fuenfte Kampagnenstufe hinter `slot 35` fort.
- `novapolis-dev/docs/process/rp-folgekorridor-slot-41-45.ssot.md` fuehrt denselben Vertragsrahmen jetzt als sechste Kampagnenstufe hinter `slot 40` fort.
- Der deterministische Agent-Referenzlauf belegt denselben Handover jetzt auch technisch mit einem zweiten Folgefall hinter `slot 30` bis `slot 40`, statt nur den D5-Basislauf zu pruefen.
- Sobald Sim den Resume-Anker operativ nutzt, wird derselbe Handover auch fuer den naechsten Produkt-Gate-Ausbau vollstaendig ueber RP, Agent und Sim belegt.
- Die knappe player-facing Kurzformel fuer denselben Anschluss lautet verbindlich: `Weiter im selben Lauf: offener Druck, offene Aufgaben, klarer naechster Zug.`

Release-Evidence-Bundle
-----------------------

- Der gemeinsame Release-Belegpfad fuer denselben Vertikalslice liegt unter `novapolis-dev/docs/process/text-rpg-release-evidence-bundle-v1.ssot.md`.
- Release-tauglich ist der Slice nicht schon mit einem isolierten Gate-PASS, sondern erst mit derselben Kette aus `Checks: full`, `Checks: text-rpg product gate`, deterministischen Referenzfaellen, Sim-Export-Smoke und dokumentiertem Workspace-Status.
- Ohne erreichbare lokale Modellruntime fuer `Eval: suite gm_session (12, asgi)` oder ohne exportierten Windows-Smoke unter `novapolis-sim/exports/windows/NovapolisSim.exe` bleibt derselbe Slice nicht release-reif.

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
- Hard Fail ebenfalls, wenn materialisierte Bedienmodi oder Turn-Zustaende (`player_input.mode`, `turn_state`) am Sessionvertrag vorbeilaufen oder der Pfad `turn_budget_review -> confirmation oder execution -> turn_resume_ready` zwischen Vertrag, Runbook und Produktlauf driftet.
- Hard Fail ebenfalls, wenn strukturierte Budgetpruefung (`plan_analysis`, `budget_decision`, `time_state`) parallel neben dem Vertrag lebt oder Klassifikationen wie `within_frame|slightly_over|significantly_over|blocked` und die zulaessigen Modifikatorarten driftig werden.
- Hard Fail ebenfalls, wenn die player-facing Recovery-Sprache `teilmoeglich|verschoben|blockiert` zwischen Turn-Budget-Modell, Produktmodell, Runbook und Sim-UI driftet oder von den Budgetklassen `slightly_over|significantly_over|blocked` abgekoppelt wird.

### Stufe 3 - Agent-API- und Streaming-Smoke

- Der Agent-Pfad muss mindestens die API-/Streaming-Gates gruen halten.
- Hard Fail bei OpenAPI-/Schema-Drift, Streaming-Regressionen oder fehlendem Grundpfad fuer den Sessionbetrieb.

### Stufe 4 - Log- und Replay-Vertrag

- Der Referenzlauf muss `world_log`, `pc_log`, `state_patches`, `savegame.json` und `replay_manifest.json` fuer denselben Slice und den Handover-Folgefall hinter `slot 30` deterministisch erzeugen und verifizieren.
- Hard Fail bei fehlenden Artefakten, ungueltigen `state_patches`, Slot-Mismatch zwischen Logs oder Replay-Widerspruechen.
- Hard Fail ebenfalls, wenn `resume_checkpoint_id`, letzter stabiler `turn_id`, `slot_id` oder eingebettete Verdichtungssegmente desselben Turns zwischen Savegame, Logs und Replay auseinanderlaufen.
- Hard Fail ebenfalls, wenn sichtbares Turn-Feedback (`completed|started|interrupted|open`, unmittelbares Signal, naechster Anschluss) fuer denselben Zug nicht aus Antwort, Logs oder Replay konsistent rekonstruierbar ist.
- Produktive Chat-Laeufe duerfen spaeter weitere Artefakte erzeugen, muessen aber denselben Vertrags- und Dateirahmen halten wie die Referenzfaelle.

### Stufe 5 - Sim-Anschluss

- Der Sim-Pfad muss mindestens denselben Slice als Smoke sichtbar pruefen koennen.
- Hard Fail bei ungueltigen Slotwerten, nicht lesbaren Epoch-Dateien oder Artefakten ausserhalb des vertraglichen Session-/Slot-Rahmens.
- Hard Fail ebenfalls, wenn Sim fuer denselben Lauf einen parallelen Turn- oder Resume-Pfad fuehrt statt `slot_id`, `turn_id`, `resume_checkpoint_id` und denselben RP-Startanker aus Sessionvertrag und RP-Produkt-SSOT zu nutzen.
- Hard Fail ebenfalls, wenn ein produktiver Neueinstieg den RP-gebundenen Pfad `Hub -> Spielhauptmenue -> RP-Startanker bei slot_00` umgeht und statt dessen eine freie Sim-Vorszene ohne Start-Chooser oder Startpaket eroefnet.

### Stufe 6 - GM-Session-Eval und KPI-Triage

- Der produktive Slice muss zusaetzlich denselben Sessionpfad ueber die dedizierte Suite `gm_session` pruefen.
- Die KPI-Summary muss auf genau die Resultatdatei desselben Gate-Laufs zeigen und Blocker-Faelle von Beobachtungen trennen.
- Hard Fail bei nicht erreichbarer Modellruntime, fehlender Resultatdatei oder fehlender KPI-Summary fuer den aktuellen Lauf.
- Hard Fail ebenfalls, wenn die Summary `severity=blocker` liefert oder `blocker_failures > 0` fuer denselben Lauf meldet.

Kanonische KPI-Matrix fuer den Pre-RP-Sim-Pfad
----------------------------------------------

### Quelle und Bindung

- Die KPI-Triage fuer denselben Produktlauf ist an `Eval: suite gm_session (12, asgi)` plus `Eval: summarize gm session KPIs` gebunden.
- Die Summary bleibt genau dann gate-gueltig, wenn sie auf die Resultatdatei desselben Wrapper-Laufs zeigt und nicht auf einen aelteren Pattern-Treffer.
- Der aktuelle fachliche Referenzsatz haengt am Paket `rpg_gm_session_core.v1` und dessen Fallklassen; neue KPI-Faelle duerfen den Satz erweitern, aber nicht still ersetzen.

### Harte Gate-KPIs

- `gm.session.continuity.v1` bleibt Blocker: Der produktive Antwortpfad muss denselben Session-, Slot- und Turn-Anschluss sichtbar halten und denselben Fortsetzungsanker nicht verlieren.
- `gm.session.reveal-discipline.v1` bleibt Blocker: Die sichtbare Lage muss ueber erlaubte Anker wie `Geraeusch`, `Druck` und `Entscheidung` laufen und darf keinen verdeckten GM-Kontext oder freie Geheimanker leaken.
- Wenn einer dieser Blockerfaelle im aktuellen Lauf fehlschlaegt, gilt `Text-RPG Product Gate v1` unabhaengig von allen anderen Gruen-Signalen als FAIL.

### Beobachtungs-KPIs

- `gm.session.option-quality.v1` bleibt Beobachtung: Drei nummerierte Handlungswege mit vorsichtiger, riskanter und sozialer Option sollen sauber materialisiert sein.
- `gm.session.patch-validity.v1` bleibt Beobachtung: `State_Patches` sollen als lesbare Patch-Struktur mit `op`, `path` und `value` rekonstruierbar bleiben.
- Reine Beobachtungen oeffnen Folgetriage, aber keinen harten Produkt-Fail, solange keine Blockerfaelle aktiv sind.

### Gate-Lesart der Summary

- `severity=blocker` bedeutet harter Produkt-Fail.
- `severity=warnung` bedeutet Produktpfad fachlich beobachtungsbeduerftig, aber nicht blockerhaft; die offenen Beobachtungen muessen im Folgeboard oder DONELOG sichtbar bleiben.
- `severity=beobachtung` gilt im aktuellen Summary-Skript als gruener Zielzustand ohne offene Blocker- oder Beobachtungsfaelle.

Gate-Erfolg
-----------

`Text-RPG Product Gate v1` gilt nur dann als PASS, wenn:

- RP-Pfad, Sessionvertrag und Runbook denselben Slice beschreiben,
- die aktuelle Agent-API-/Streaming-Pruefung gruen ist,
- die feste Referenz-Session fuer denselben Slice Artefakte und Replay-Vertrag gruen bestaetigt,
- der gemeinsame Turn-, Verdichtungs- und Resume-Rahmen zwischen Sessionvertrag, Replay und Sim nicht driftet,
- materialisierte Bedienmodi, Turn-Zustaende und sichtbares Turn-Feedback denselben Vertragsrahmen halten,
- strukturierte Budget- und Zeitlogik denselben Vertragsrahmen halten,
- die player-facing Recovery-Sprache `teilmoeglich|verschoben|blockiert` zwischen Produktmodell, Turn-Budget-SSOT, Runbook und Sim-UI konsistent bleibt,
- der Sim-Asset-/Epoch-Pfad fuer denselben Slice nicht widerspricht,
- der `gm_session`-Eval-Lauf eine Ergebnisdatei fuer denselben Gate-Lauf erzeugt,
- die KPI-Summary fuer denselben Gate-Lauf keinen Blockerfall in `gm.session.continuity.v1` oder `gm.session.reveal-discipline.v1` fuehrt,
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
- Die deterministischen Referenzfaelle fuer Basislauf und Handover-Folgepfad sind als aktive Gate-Dateien dokumentiert.
- Die harten Fail-Klassen fuer Vertrags-, Log-, Slot- und GM-Runtime-Drift sind benannt.
- Bedienmodi, Turn-Zustaende und sichtbares Turn-Feedback sind als Gate-relevante Driftklassen benannt.
- Die kanonische KPI-Matrix fuer Blocker- und Beobachtungsfaelle des Pre-RP-Sim-Pfads ist explizit benannt.
- Der Pfad ist technisch automatisiert, ohne den lokalen Modellruntime-Bedarf des GM-Eval-Teils zu verschweigen.
