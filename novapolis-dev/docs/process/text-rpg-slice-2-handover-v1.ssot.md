---
stand: 2026-04-20 21:22
update: Der Slice-2-Handover fuehrt jetzt auch die kanonische player-facing Kurzformel hinter slot 30 und verweist auf den gemeinsamen Release-Evidence-Pfad.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260420_210436.md
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

- `novapolis-dev/docs/process/rp-folgekorridor-slot-41-45.ssot.md`
- `novapolis-dev/docs/process/rp-folgekorridor-slot-31-35.ssot.md`
- `novapolis-dev/docs/process/rp-folgekorridor-slot-36-40.ssot.md`
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
- Der Wiederanlauf hinter `slot 30` fuehrt denselben Turn-Rahmen weiter: aeusserer Turn bleibt `30 Minuten`, Verdichtung bleibt ein eingebettetes `1-Minuten`-Fenster innerhalb desselben `turn_id`, und Carry-Over bleibt ueber denselben Sessionvertrag lesbar.
- Die belegten Anschlussraeume bleiben fuer diesen Handover auf `D5`, `C6`, `G7`, `E2` und `F1` beschraenkt, bis eine spaetere RP-SSOT weitere Raeume explizit freigibt.

Player-facing Uebergabeformel
-----------------------------

- Die knappe player-facing Kurzformel fuer den ersten aktiven Anschluss hinter `slot 30` lautet verbindlich: `Weiter im selben Lauf: offener Druck, offene Aufgaben, klarer naechster Zug.`
- `Weiter im selben Lauf` verhindert, dass der Handover wie ein zweiter Startschirm oder ein freier Episodenwechsel gelesen wird; derselbe Session-, Save-, Resume- und Replay-Vertrag bleibt aktiv.
- `offener Druck` und `offene Aufgaben` spiegeln den lesbaren Carry-Over aus Lage, Reichweite und angefangener Arbeit, ohne einen zweiten Namen neben `Text-RPG Slice 2 Handover v1` zu etablieren.
- `klarer naechster Zug` verpflichtet RP, Agent und Sim darauf, den Folgeblock nicht als vage Fortsetzung, sondern als direkt anschlussfaehigen Handlungsraum zu praesentieren.

Resume- und Turn-Kontext
------------------------

- Ein Resume hinter `slot 30` ist nur dann sauber, wenn `resume_checkpoint_id`, `slot_id`, letzter abgeschlossener `turn_id` und die noch offenen Carry-Over-Arbeiten auf denselben Handover zeigen.
- `turn_resume_ready` bleibt auch hinter `slot 30` der einzige kanonische Zustand, aus dem Checkpoint, Resume oder Replay weiterlaufen duerfen.
- Ein Verdichtungsfenster darf im Replay als Untersegment erscheinen, aber keinen zweiten aeusseren Resume-Pfad neben dem Handover erzeugen.
- Der erste Wiedereinstieg nach dem Handover muss dadurch sowohl fuer RP als auch fuer Sim lesbar machen, welche Arbeiten `begonnen`, `unterbrochen` oder `offen` in den Folgeblock getragen werden.
- Derselbe Wiedereinstieg muss zusaetzlich sichtbares Turn-Feedback und Anschlusslogik aus demselben Vertragsrahmen rekonstruieren koennen, statt Folge-Slots nur als nackten Checkpoint zu zeigen.

Modulrollen
-----------

### Root

- Root fuehrt nur den gemeinsamen Handover und verweist fuer Ausgestaltung auf RP-, Agent- und Sim-SSOTs.
- Root darf keinen zweiten, freieren Namen fuer denselben Folgepfad etablieren.
- Root fuehrt fuer denselben Folgepfad dieselbe Kurzformel `Weiter im selben Lauf: offener Druck, offene Aufgaben, klarer naechster Zug.`

### RP

- RP fuehrt den Handover aktuell als `slot 31-35`, `slot 36-40` und `slot 41-45` auf demselben Vertragsrahmen fort; spaetere modulare Episoden bleiben daran gebunden.
- Reveal-, Missions- und Ortsbezug bleiben an die bereits belegten Raeume und den bestehenden Produktpfad gebunden.
- Die ersten drei konkreten Ausbauten liegen jetzt in `novapolis-dev/docs/process/rp-folgekorridor-slot-31-35.ssot.md`, `novapolis-dev/docs/process/rp-folgekorridor-slot-36-40.ssot.md` und `novapolis-dev/docs/process/rp-folgekorridor-slot-41-45.ssot.md`.
- Der erste Folgeblock `slot 31-35` fuehrt fuer den aktiven Wiedereinstieg dieselbe Kurzformel ohne Abweichung oder Zweitnamen.

Minimaler RP-Adapter-Scope fuer den ersten Integrationsschnitt
--------------------------------------------------------------

- Akzeptiert ist nur ein Adapter, der denselben Handover hinter `slot 30` liest und keine zweite Produktnaht neben `Text-RPG Slice 2 Handover v1` eroefnet.
- Pflichtanker bleiben `campaign_id`, `session_id`, `scene_id`, `slot_id`, `turn_id`, `resume_checkpoint_id`, `state_patches`, `world_log`, `pc_log` und `replay_manifest.json`.
- Der erste Integrationsschnitt darf RP-seitig genau den bereits belegten Folgepfad bis `slot 40` herstellen, inklusive lesbarem Resume-Anker und Carry-Over-Zustand.
- Der Adapter darf RP-spezifische Darstellung, Folgeoptionen und Reveal-Grenzen auf diesem Vertragsrahmen sichtbar machen, muss dafuer aber keine neue Sessionklasse, keine neue Ticklogik und keinen eigenen Save-/Replay-Pfad einfuehren.
- Nicht Teil dieses Minimal-Scope sind freie neue Orte, neue Fraktionssysteme, ein zweiter Startwaehler oder neue Parallelformate fuer Save, Replay oder Resume.
- Der Integrationsschnitt gilt erst dann als sauber, wenn Sim, RP, Product Gate und Runbook denselben Adapter als Fortsetzung desselben Handover und nicht als separaten Produktpfad lesen.

### Agent

- Product Gate, Referenz-Session und Runbook muessen den Handover als naechsten gemeinsamen Ausbau hinter `slot 30` benennen.
- Neue Gate- oder Referenzfaelle hinter `slot 30` duerfen nur auf demselben Session- und Artefaktvertrag aufbauen.
- Der deterministische Agent-Referenzlauf umfasst jetzt den D5-Basisfall und den Handover-Folgefall `novapolis_agent/eval/config/text_rpg_reference_session_handover_slot31_40.v1.json` bis `slot 40`.
- Product Gate und Runbook fuehren fuer denselben Anschluss dieselbe Kurzformel statt einer eigenen Gateway- oder Runtime-Umschreibung.

### Sim

- Der Hub muss `resume_checkpoint_id` und `replay_manifest` aus demselben Sessionvertrag fuer den Handover nutzbar machen.
- Der Wiedereinstieg hinter `slot 30` bleibt derselbe Bedienpfad `Hub -> Spielhauptmenue -> Resume/Checkpoint`; Sim darf dafuer keinen separaten Schnellpfad neben dem kanonischen Einstieg eroefnen.
- Replay-/Resume-Bedienung darf keinen parallelen Artefaktpfad neben dem bestehenden Session-Store aufziehen.
- Sim darf hinter `slot 30` keinen eigenen Turn- oder Tick-Hauptvertrag erfinden; Verdichtung bleibt auch hier Unterstruktur desselben Handover-Zugs.

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
- Kein Resume hinter `slot 30` ohne gemeinsamen Anker aus `slot_id`, `turn_id`, `resume_checkpoint_id` und lesbarem Carry-Over-Zustand.
- Kein Gate-PASS hinter `slot 30`, der nur auf einzelnen Tests beruht, ohne den Resume- und Artefaktvertrag mitzudenken.

Definition of Done
------------------

- Root-Backlog, Product Gate und Agent-Runbook verweisen auf diese SSOT.
- RP- und Sim-Folgepunkte benennen denselben Handover statt freier Folgeformeln.
- Produktmodell, Handover-SSOT, RP-Folgeblock, Product Gate und Runbook fuehren dieselbe player-facing Kurzformel fuer den Anschluss hinter `slot 30`.
- Der weitere Ausbau hinter `slot 30` bleibt auf demselben Session- und Artefaktvertrag verankert.
- Die ersten fachlichen Ausbauten hinter `slot 30` liegen als eigene RP-SSOTs fuer `slot 31-35`, `slot 36-40` und `slot 41-45` vor.
- Der minimal akzeptierte RP-Adapter-Scope fuer den ersten Integrationsschnitt ist explizit benannt und fuehrt keinen zweiten Resume-, Save- oder Produktpfad ein.
- Der zweite deterministische Agent-Referenzfall hinter `slot 30` liegt als eigene Referenzdatei vor und nutzt denselben Session- und Artefaktvertrag bis `slot 40`.
