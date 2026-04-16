---
stand: 2026-04-17 01:04
update: Der Sessionvertrag fuehrt jetzt zusaetzlich die kompakte Budget- und Zeitlogik fuer den Sim-vor-RP-Turn auf demselben Vertragsblock.
checks: snapshot-lock PASS (2026-04-17 01:04); markdownlint=PASS; frontmatter=PASS
---

Text-RPG Session- und Kampagnenvertrag v1
=========================================

Zweck
-----

Diese SSOT definiert den kanonischen Vertragsrahmen fuer einen spielbaren Text-RPG-Lauf im Novapolis-Workspace. Sie zieht die Grenze zwischen Kampagne, Session, Szene, Slot, Spielerinput, Spielleiterantwort, `state_patches` sowie den nachgelagerten Log- und Replay-Artefakten fest.

Scope
-----

- Agent-Runtime und API im Modul `novapolis_agent/`
- RP-Produktpfad aus den aktiven Start- und Folgekorridor-SSOTs
- Log-, Replay- und Sim-Anschluss fuer denselben Session-Kontext

Quellenbasis
------------

- `novapolis_agent/app/api/models.py`
- `novapolis_agent/app/api/chat.py`
- `novapolis_agent/app/api/sim.py`
- `novapolis_agent/docs/runbook.md`
- `novapolis-dev/docs/specs/annotation-spec.md`
- `novapolis-dev/docs/specs/scheduler-spec.md`
- `novapolis-dev/docs/process/project-context-bridge.ssot.md`
- `novapolis-dev/docs/process/rp-text-rpg-startpaket-slot-00-05-2026-04-05.md`
- `novapolis-dev/docs/process/rp-startkorridor-reveal-matrix.ssot.md`
- `novapolis-dev/docs/process/rp-startgebiete-reveal-matrix.ssot.md`

Ist-Stand und Drift
-------------------

- `ChatRequest` und `ChatOptions` fuehren aktuell nur einen generischen Chat-Vertrag mit optionaler `session_id`.
- Der aktuelle Chat-Flow speichert Session-Memory, aber keinen expliziten Kampagnen-, Szenen- oder Slotzustand.
- Die Sim-API fuehrt derzeit nur einen Minimalzustand `{tick, time, regions, actors, events}` ohne Produktvertrag fuer `world_log`, `pc_log`, Replay oder Savegames.
- Die RP-SSOTs fuehren bereits einen belastbaren Start- und Folgekorridor, brauchen dafuer aber einen maschinenlesbaren Sessionrahmen statt freiem Chatgedaechtnis.

Kernobjekte
-----------

- `campaign_id`: langlebiger Rahmen fuer denselben Kampagnenast.
- `session_id`: konkreter Spielrun innerhalb einer Kampagne.
- `scene_id`: aktuelle Szene oder Fokuslinse innerhalb der Session.
- `slot_id`: kanonischer Fortschrittsanker entlang eines RP-Folgekorridors.
- `turn_id`: einzelner Spielerzug innerhalb derselben Szene.
- `request_id`: technischer Requestanker fuer Debugging, Logs und Retries.
- `resume_checkpoint_id`: kanonischer Wiederanlaufanker an stabilen Turn-Grenzen.
- `replay_epoch_id`: spaeterer Exportanker fuer Sim-/Replay-Chunks.

Lebenszyklus
------------

Eine Session laeuft kanonisch ueber folgende Statuswerte:

- `created`: Vertrag und Startanker existieren, aber noch kein Zug ist gelaufen.
- `active`: Session verarbeitet Spielerzuege und erzeugt `state_patches`.
- `paused`: Session ist bewusst angehalten und spaeter fortsetzbar.
- `completed`: Session oder Episodenbogen ist regulär abgeschlossen.
- `aborted`: Session wurde mit nachvollziehbarem Abbruchgrund beendet.

Turn-, Verdichtungs- und Resume-Rahmen
--------------------------------------

- Der aeussere Produktzug bleibt `1 Turn = 30 Minuten` Ingame-Zeit.
- Verdichtung ist ein Turn-internes Reaktionsfenster mit `1 Tick = 1 Minute`.
- Verdichtung erzeugt keinen zweiten aeusseren Zugvertrag neben `turn_id`, sondern bleibt Unterstruktur desselben Turns.
- `resume_checkpoint_id` darf nur an stabilen Turn-Grenzen materialisiert oder ersetzt werden, nicht mitten in einer laufenden Verdichtung ohne explizite Sonderregel.
- Carry-Over bleibt Teil desselben Sessionvertrags und darf nicht als lokale UI-Notiz oder freier Sim-Sonderpfad ausweichen.

Vertragsrahmen v1
-----------------

### Request-Huelle

Ein produktfaehiger Spielzug fuehrt mindestens diese Felder:

```json
{
  "contract_version": "text_rpg_session_v1",
  "campaign_id": "camp_novapolis_default",
  "session_id": "sess_2026_04_06_0001",
  "scene_id": "scene_d5_maintenance",
  "slot_id": "slot_00",
  "turn_id": "turn_0001",
  "player_input": {
    "utterance": "Ich pruefe den Port vorsichtig und halte Reflex bereit.",
    "selected_option_ids": ["opt_safe_probe"],
    "intent": "inspect",
    "mode": "hybrid",
    "channel": "pc"
  },
  "client_hints": {
    "resume_from": null,
    "seed": 42,
    "profile_id": "context_bridge"
  },
  "turn_context": {
    "turn_mode": "standard",
    "turn_window_minutes": 30,
    "tick_minutes": null,
    "turn_state": "turn_planning",
    "resume_checkpoint_id": null
  }
}
```

Minimal verbindlich sind `campaign_id`, `session_id`, `scene_id`, `slot_id`, `turn_id` und `player_input.utterance`.
Wenn Turn- oder Replay-Kontext materialisiert wird, gehoeren `turn_context.turn_mode`, `turn_context.turn_window_minutes` und der aktuelle `resume_checkpoint_id` auf denselben Vertragsblock.
Wenn Eingabemodus oder sichtbarer Turn-Zustand materialisiert werden, gehoeren `player_input.mode` und `turn_context.turn_state` auf denselben Vertragsblock statt in freie UI-Nebenpfade.

### Response-Huelle

Die Spielleiterantwort fuer denselben Zug fuehrt mindestens diese Felder:

```json
{
  "contract_version": "text_rpg_session_v1",
  "campaign_id": "camp_novapolis_default",
  "session_id": "sess_2026_04_06_0001",
  "scene_id": "scene_d5_maintenance",
  "slot_id": "slot_00",
  "turn_id": "turn_0001",
  "scene_text": "...",
  "consequence_summary": "...",
  "options": [],
  "state_patches": [],
  "log_refs": {
    "world": "world_log",
    "pc": "pc_log",
    "ally": [],
    "sys": []
  },
  "session_status": "active",
  "resume_checkpoint_id": "rcp_slot_00_turn_0001",
  "turn_context": {
    "turn_mode": "standard",
    "turn_window_minutes": 30,
    "tick_minutes": null,
    "turn_state": "turn_resume_ready",
    "budget_class": "within_frame"
  },
  "carry_over": [],
  "turn_feedback": {
    "completed": [],
    "started": [],
    "interrupted": [],
    "open": [],
    "immediate_signal": "Die Lage beruhigt sich fuer den Moment.",
    "next_hook": "Der naechste Turn kann die offene Wartung fortsetzen."
  }
}
```

Antworttext und Folgedaten bleiben Teil derselben Antwort und werden nicht in getrennte Nebenpfade aufgespalten.

Turn-Kontext
------------

Jede produktfaehige Turn-Antwort darf zusaetzlich einen kompakten `turn_context` fuehren. Sobald er vorhanden ist, gelten mindestens diese Felder:

- `turn_mode`: `standard|dense`
- `turn_window_minutes`: im aktuellen Produktpfad `30`
- `tick_minutes`: `1` im Verdichtungsfenster, sonst `null`
- `turn_state`: `turn_idle|turn_briefing|turn_planning|turn_budget_review|turn_confirmation_required|turn_execution|turn_dense_mode|turn_resolution|turn_resume_ready`
- `budget_class`: `within_frame|slightly_over|significantly_over|blocked`

Wenn `turn_mode=dense` gilt, bleibt `turn_id` trotzdem der aeussere Vertrag. Ticks erscheinen nur als Unterstruktur in Replay, Logs oder Laufzeitdarstellung.

Spielerinput und Turn-Lebenszyklus
----------------------------------

- `player_input.mode` fuehrt den aktiven Bedienmodus als `free_text|guided|hybrid`.
- `guided` steht fuer reine Vorauswahl, `free_text` fuer freien Plantext, `hybrid` fuer Vorauswahl mit optionaler Freitext-Ergaenzung.
- `turn_state` fuehrt denselben sichtbaren Lebenszyklus fuer Briefing, Planung, Budgetpruefung, optionale Bestaetigung, Ausspielung, optionale Verdichtung, Aufloesung und Resume-Bereitschaft.
- `turn_resume_ready` bleibt der einzige kanonische Zustand, aus dem Checkpoint, Resume oder Replay weitergefuehrt werden duerfen.
- Rueckfragen ohne bestaetigten Ausspielpfad verlassen den Vertragsrahmen nicht, sondern bleiben in `turn_planning` oder kehren aus `turn_budget_review` dorthin zurueck.

Optionen
--------

Jede Option fuehrt mindestens:

- `option_id`: stabiler Auswahlanker innerhalb des Zuges
- `label`: kurze lesbare Option
- `intent`: maschinenlesbare Absichtsklasse
- `risk`: `low|medium|high`
- `visibility`: `pc_visible|allies_only|world_only|rumor|log_reflex`
- `expected_patch_scopes`: betroffene Patch-Scope-Klassen

State-Patches
-------------

Jeder `state_patch` fuehrt mindestens:

- `patch_id`
- `scope`: `world|session|pc|mission|reveal|resource|relationship|inventory`
- `op`: `set|append|increment|unlock|consume|emit_log|mark_visibility`
- `path`: stabiler Zielpfad innerhalb des Zustandsmodells
- `value`: neuer oder angehaengter Wert
- `visibility`: `pc_visible|allies_only|world_only|rumor|log_reflex`
- `evidence_refs`: Verweise auf RP- oder Produkt-SSOTs
- `replay_epoch_id`: optionaler spaeterer Replay-Chunk-Anker

Nicht zulaessig sind freie Textpatches ohne `scope`, `op` und `path`.

Carry-Over und Wiederaufnahme
-----------------------------

- `carry_over` fuehrt nur Aufgaben weiter, die als `begonnen`, `unterbrochen` oder `offen` real in den Folgeturn wirken.
- Jeder Carry-Over-Eintrag soll mindestens `task_id`, `state`, einen kurzen `resume_hint` und optional vorbereitete Mittel oder geoeffnete Zugaenge tragen.
- Zulaessige Zustandswerte sind `begonnen`, `unterbrochen` und `offen`.
- Wenn eine Session fortgesetzt wird, verweist `resume_checkpoint_id` auf denselben Turn- und Slotrahmen, aus dem `carry_over`, `world_log`, `pc_log` und `state_patches` lesbar rekonstruiert werden koennen.

Sichtbares Turn-Feedback
------------------------

- `turn_feedback` bleibt optional, ist aber der kanonische Vertragsblock fuer sichtbare Turn-Rueckmeldung, sobald dieselbe Information nicht nur implizit in Freitext lebt.
- `turn_feedback.completed`, `started`, `interrupted` und `open` trennen sichtbar, was erledigt, begonnen, unterbrochen oder offengeblieben ist.
- `turn_feedback.immediate_signal` fuehrt mindestens ein direkt lesbares Rueckmeldesignal wie Zustandsaenderung, Reaktion, Risiko oder neuen Anschluss.
- `turn_feedback.next_hook` fuehrt den naechsten spielbaren Anschluss, ohne dafuer einen Parallelpfad ausserhalb von `carry_over`, `pc_log` oder `world_log` zu erfinden.

Kompakte Budget- und Zeitlogik
------------------------------

- `plan_analysis`, `budget_decision` und `time_state` bleiben optionale Vertragsbloecke fuer Zuege, in denen Budgetpruefung oder Zeitlogik strukturiert materialisiert werden.
- `plan_analysis.steps[]` fuehrt pro atomarem Schritt mindestens `step_id`, `label`, `step_class`, `base_minutes` und `estimated_minutes`.
- Zulaessige `step_class`-Werte sind `very_short|short|medium|long|multi_stage`.
- Wenn Modifikatoren strukturiert materialisiert werden, fuehrt jeder Eintrag mindestens `kind`, `effect_minutes` und `reason`.
- Zulaessige `kind`-Werte sind `condition|environment|tools|support|routine|transition`.
- `budget_decision.class` bleibt auf `within_frame|slightly_over|significantly_over|blocked` begrenzt.
- `time_state` fuehrt mindestens `turn_budget_minutes`, `consumed_minutes` und `remaining_minutes`; `dense_mode_minutes` bleibt optional.

Budget- und Zeit-Guardrails
---------------------------

- Eine harte Blockade wird zuerst geprueft; wenn sie greift, endet die Minutenrechnung fuer den betroffenen Schritt und `budget_decision.class=blocked`.
- `base_minutes` kommen aus einer dokumentierten Referenzlogik und nicht aus freiem Dramatisieren pro Zug.
- Mehrschrittplaene duerfen einen expliziten Uebergangsaufschlag tragen; dieser laeuft als `kind=transition` innerhalb derselben Analyse statt als separater Schattenpfad.
- `multi_stage` kennzeichnet Arbeit, die nicht sauber in einen einzelnen `30`-Minuten-Turn passt und deshalb ueber `carry_over` oder Folgezuege weiterlaufen muss.
- Die strukturierten Budget- und Zeitbloecke ersetzen den Spielertext nicht, sondern machen dieselbe Bewertung nur fuer Vertrag, Replay und Gate nachvollziehbar.

Sichtbarkeit und Log-Kanaele
----------------------------

- `world_log`: vollstaendige Weltwahrheit und verdeckte Folgedaten
- `pc_log`: nur direkt oder regelkonform sichtbare Rueckmeldungen
- `ally_log`: kontrollierte Gruppen- oder Verbundsicht
- `sys_log`: technische oder Debug-/Gate-Hinweise ausserhalb des Spielertexts

Die Reveal-Klassen aus den RP-Matrizen bleiben verbindlich. `world_only`- oder rohe Mind-Cluster-Daten duerfen nicht in `scene_text`, `options` oder `pc_log` auftauchen.

Persistenzartefakte
-------------------

Ein spaeterer produktiver Lauf soll pro Session mindestens folgende Artefakte fuehren:

- `session_manifest.json`
- `state_patches.jsonl`
- `world_log.jsonl`
- `pc_log.jsonl`
- optional `ally_log.jsonl`
- `replay_manifest.json`

`session_manifest.json` oder `replay_manifest.json` muessen dabei den letzten stabilen `resume_checkpoint_id`, den aktiven `slot_id`, den zuletzt abgeschlossenen `turn_id` und gegebenenfalls eingebettete Verdichtungssegmente desselben Turns lesbar halten.

Diese SSOT definiert den Namen und die Pflichtrolle dieser Artefakte, nicht bereits ihre volle Runtime-Implementierung.

Kompatibilitaetsbruecke zum Ist-Stand
------------------------------------

- Phase 0 bleibt der bestehende `/chat`-Pfad mit optionaler `session_id`.
- Neue Sessionfelder werden nicht rueckwirkend in freie Chatnotizen ausgelagert, sondern spaeter auf echte Request-/Response-Modelle gehoben.
- Solange die Runtime noch nicht auf den Vollvertrag angehoben ist, bleibt diese SSOT die kanonische Quelle fuer OpenAPI-, Test- und Runbook-Nachzug.

Synchronisationspflicht
-----------------------

Die folgenden Oberflaechen sollen auf diesen Vertrag verweisen oder ihn materialisieren:

- OpenAPI-Modelle im Agent-Modul
- API- und Streaming-Tests
- Runbook-Bedienpfad
- spaetere Replay-/Sim-Bruecke

Out of Scope
------------

- Konkrete Endpunktnamen jenseits des bestehenden `/chat`-Pfads
- Speicherung in einer bestimmten Datenbank oder Dateistruktur
- TTS-spezifische Kanal- oder Cache-Implementierung
- Vollstaendige Scheduler-Engine

Definition of Done
------------------

- Kampagne, Session, Szene, Slot und Zug sind als getrennte Vertragsobjekte benannt.
- `state_patches` besitzen einen kanonischen Minimalrahmen statt freier Textanhaenge.
- Sichtbarkeit und Log-Kanaele sind gegen RP-Reveal-Regeln sauber getrennt.
- Turn-, Verdichtungs-, Carry-Over- und Resume-Rahmen bleiben auf demselben Sessionvertrag lesbar.
- Eingabemodi, Turn-Zustand und sichtbares Turn-Feedback bleiben auf demselben Sessionvertrag lesbar, sobald sie materialisiert werden.
- Runbook und Produkt-Gate koennen auf denselben Vertrag verweisen.