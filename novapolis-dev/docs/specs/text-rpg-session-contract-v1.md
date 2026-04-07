---
stand: 2026-04-07 10:20
update: Der Text-RPG-Sessionvertrag v1 definiert jetzt den kanonischen Session-, Kampagnen- und Patch-Rahmen fuer den ersten spielbaren Slice.
checks: snapshot-lock PASS (2026-04-07 10:20); markdownlint PASS; frontmatter PASS
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
- `replay_epoch_id`: spaeterer Exportanker fuer Sim-/Replay-Chunks.

Lebenszyklus
------------

Eine Session laeuft kanonisch ueber folgende Statuswerte:

- `created`: Vertrag und Startanker existieren, aber noch kein Zug ist gelaufen.
- `active`: Session verarbeitet Spielerzuege und erzeugt `state_patches`.
- `paused`: Session ist bewusst angehalten und spaeter fortsetzbar.
- `completed`: Session oder Episodenbogen ist regulär abgeschlossen.
- `aborted`: Session wurde mit nachvollziehbarem Abbruchgrund beendet.

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
    "channel": "pc"
  },
  "client_hints": {
    "resume_from": null,
    "seed": 42,
    "profile_id": "context_bridge"
  }
}
```

Minimal verbindlich sind `campaign_id`, `session_id`, `scene_id`, `slot_id`, `turn_id` und `player_input.utterance`.

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
  "session_status": "active"
}
```

Antworttext und Folgedaten bleiben Teil derselben Antwort und werden nicht in getrennte Nebenpfade aufgespalten.

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
- optional `replay_manifest.json`

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
- Runbook und Produkt-Gate koennen auf denselben Vertrag verweisen.