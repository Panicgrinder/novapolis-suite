---
stand: 2026-04-14 12:25
update: Die offene Agent-Coverage-Welle fuer chat_helpers, main und tts/providers ist jetzt geschlossen und gegen den kanonischen Wrapper verifiziert.
checks: snapshot-lock 2026-04-14 12:25; focused coverage PASS (chat_helpers=100, main=98, providers=96); scripts/run_pytest_coverage.py --fail-under 80 PASS (615 passed, total=94.92%)
---

<!-- markdownlint-disable MD012 MD022 MD041 -->

Novapolis Agent - ToDo & Roadmap (SSOT)
---------------------------------------

Hinweis
------
- Dies ist die zentrale ToDo-Datei (Single Source of Truth) fuer das Agent-Modul.
- Historische Inhalte aus frueheren Redirect-Dateien sind bereits in dieses Board/Archiv ueberfuehrt.
- Bis zur vollstaendigen Migration verweist die alte Datei als Redirect-Stub auf diese Seite.

Prioritaetstags (aktiv)
-----------------------

- `Jetzt`: Spielleiter-Orchestrierung und produktfaehiger Weltzustand fuer den ersten spielbaren Slice.
- `Als naechstes`: GM-Eval-Gates und Session-TTS an denselben Slice anbinden.
- `Spaeter`: Training, Komfort und weitere Provider erst nach belastbarem Spielkern ausbauen.

Neue Aufgaben - Coverage-Haertung (2026-04-09)
----------------------------------------------

- [x] [Als naechstes] Naechste Coverage-Welle fuer den aktiven Produktpfad auf `chat_helpers`, `main` und `tts/providers` ziehen.
  - Ziel: Nach dem geschlossenen Fuenferblock sollen die verbleibenden produktnahen Laufzeitmodule unter `95%` nicht als unsichtbarer Rest im Sammelreport bleiben, sondern gezielt ueber echte Fehler-, Fallback- und Providerpfade nachgezogen werden.
  - Akzeptanzkriterien:
    1) `novapolis_agent/app/api/chat_helpers.py`, `novapolis_agent/app/main.py` und `novapolis_agent/app/tts/providers.py` steigen in der fokussierten Nachmessung jeweils auf mindestens `95%`,
    2) neue Tests decken reale Fehler- und Degradationspfade ab statt nur Serialisierungs-Happy-Paths,
    3) der kanonische Coverage-Wrapper `scripts/run_pytest_coverage.py --fail-under 80` bleibt gruen,
    4) der Produktpfad `/chat`, `/session` und `/tts/synthesize` behaelt denselben API-Vertrag ohne Parallelimplementierungen.
  - Evidenz: `.tmp/results/reports/pytest_coverage_postflight_20260409_232603.md` meldet aktuell `89%` fuer `app/api/chat_helpers.py`, `90%` fuer `app/main.py` und `87%` fuer `app/tts/providers.py` bei insgesamt weiter gruener Gesamtquote.
  - Arbeitsstand 2026-04-14 11:06: Der Restscope ist vor dem naechsten Fixlauf auf konkrete Zweige eingegrenzt. In `app/api/chat_helpers.py` fehlen vor allem Coercion-/Clamp-Pfade in `normalize_ollama_options()`, in `app/main.py` ungetestete Cache- und Cleanup-Aeste (`_tts_cache_cleanup_unlocked()`, `_tts_cache_get()`, `_tts_cache_put()`), und in `app/tts/providers.py` verbleiben vor allem Platzhalter-/Fallback-Zweige bei `NullTtsProvider`, `AdapterScaffoldProvider`, Coqui-Decodefehlern sowie dem sessionlosen Artefaktpfad.
  - Ergebnis 2026-04-14 11:15: Der Punkt ist jetzt ueber minimale Testergaenzungen geschlossen. Neue Edge-Tests decken in `tests/test_chat_helpers_edges.py` die restlichen Coercion-/Omit-Pfade von `normalize_ollama_options()`, in `tests/test_main_internal_edges.py` Cache-Hit-/Snapshot-/Hash-Pfade und in `tests/test_tts_provider_edges.py` Platzhalter-Provider plus sessionloses bzw. sanitisiertes Artefaktlayout ab. Der breite Fokuslauf bestaetigt `app/api/chat_helpers.py = 100%`, `app/main.py = 98%`, `app/tts/providers.py = 96%`; der kanonische Wrapper `scripts/run_pytest_coverage.py --fail-under 80` bleibt mit `615 passed` und `Total coverage: 94.92%` PASS.

- [x] [Jetzt] Fuenf Low-Coverage-Module testseitig auf echte Vollabdeckung ziehen.
  - Ziel: Die aktuell groessten Abdeckungsluecken im produktnahen Agent-Scope sollen nicht ueber globale Quoten versteckt, sondern mit belastbaren Unit- und Fehlerpfadtests geschlossen werden.
  - Akzeptanzkriterien:
    1) `novapolis_agent/scripts/run_text_rpg_reference_session.py`, `novapolis_agent/scripts/validate_eval_datasets.py`, `novapolis_agent/scripts/summarize_gm_eval_kpis.py`, `novapolis_agent/app/core/content_management.py` und `novapolis_agent/app/api/tts_models.py` erreichen in der Coverage-Nachmessung jeweils `100%`,
    2) neue Tests decken explizit Fehler-, Fallback- und CLI-/Validatorpfade ab statt nur Happy Paths,
    3) der gezielte Testlauf fuer die neuen Dateien bleibt gruen,
    4) der anschliessende Coverage-Lauf bestaetigt den Effekt ueber den kanonischen Wrapper `scripts/run_pytest_coverage.py`.
  - Evidenz: `.tmp/results/reports/pytest_coverage_20260409_123310.log` meldete zuvor `55%` fuer `novapolis_agent/scripts/run_text_rpg_reference_session.py`, `76%` fuer `novapolis_agent/scripts/validate_eval_datasets.py`, `83%` fuer `novapolis_agent/scripts/summarize_gm_eval_kpis.py`, `84%` fuer `novapolis_agent/app/core/content_management.py` und `86%` fuer `novapolis_agent/app/api/tts_models.py`.
  - Ergebnis 2026-04-09 23:33: `novapolis_agent/tests/test_content_management_edges.py` deckt die letzten drei offenen Zweige in `app/core/content_management.py` jetzt gezielt ab. Zusaetzlich nutzt `novapolis_agent/scripts/validate_eval_datasets.py` Default-Dataset- und Suite-Config-Pfade jetzt skriptrelativ statt cwd-abhaengig, damit der kanonische Coverage-Wrapper im Agent-CWD nicht mehr am Test `test_main_covers_default_patterns_read_fail_duplicate_id_strict_and_missing_id_strict` scheitert. Die fokussierte Nachmessung zieht `run_text_rpg_reference_session.py`, `validate_eval_datasets.py`, `summarize_gm_eval_kpis.py`, `content_management.py` und `tts_models.py` jeweils auf `100%`; `.tmp/results/reports/pytest_coverage_postflight_20260409_232603.md` bestaetigt anschliessend `596 passed`, `returncode=0` und `Total coverage: 93.73%`.

Neue Aufgaben - Text-RPG Produktpfad (2026-04-03)
-------------------------------------------------

- [x] [Jetzt] Strikten GM-Antwortvertrag im Chat-Pfad nachziehen.
  - Ziel: Wenn der Userprompt explizit die Abschnittstitel `Szene:`, `Konsequenz:`, `Optionen:` und `State_Patches:` verlangt, soll der produktive `/chat`-Pfad eine enge Format- und Sichtbarkeitsfuehrung in denselben Lauf injizieren, damit qwen im GM-Slice weniger haeufig an fehlenden Abschnittstiteln, fehlenden nummerierten Optionen oder auslaufenden `State_Patches` scheitert.
  - Akzeptanzkriterien:
    1) der Chat-Pfad erkennt strikte Text-RPG-Formatprompts ohne neuen Parallelendpunkt,
    2) die injizierte Zusatzfuehrung verlangt immer die vier Abschnittstitel, exakt drei nummerierte Optionen und ein explizites `State_Patches`-Segment, notfalls mit `[]`,
    3) sichtbare Prompt-Anker wie Slot-/Turn-IDs bleiben als sichtbare Leitplanken erhalten, waehrend verdeckte/internal markierte Begriffe nicht in die sichtbare Antwort gezogen werden sollen,
    4) ein gezielter Test deckt die Payload-Injektion gegen Regression ab.
  - Evidenz: Der qwen-Sweep `novapolis_agent/eval/results/results_20260409_0041_gm_compare_qwen_sweep_n256.jsonl` ist zwar der stabilste Lauf ohne 504, scheitert aber bei `gm.session.continuity.v1` und `gm.session.reveal-discipline.v1` beide Male an fehlendem `State_Patches:` und fehlenden `1./2./3.`-Optionen; `results_20260409_0041_gm_compare_qwen_sweep_n512.jsonl` zeigt denselben Produktpfad mit besserer Strukturabdeckung, verfehlt aber weiter Sichtbarkeitsanker (`Geraeusch`, `Druck`) und leakt einmal `Verdeckter Auftrag`.
  - Ergebnis 2026-04-09 03:05: `novapolis_agent/app/api/chat.py` injiziert fuer diese Prompts jetzt einen engeren `[Text-RPG-Formatvertrag]` mit exakt vier Abschnittstiteln, genau drei nummerierten Optionen, ohne zusaetzliche sichtbare Ueberschriften und mit getrennten sichtbaren bzw. verdeckten Prompt-Ankern. Der gezielte Test `novapolis_agent/tests/test_api_chat_internal_branches.py` deckt denselben Hint jetzt fuer `process_chat_request()` und `stream_chat_request()` ab; der fokussierte Pytest-Lauf ist PASS.
  - Nachmessung 2026-04-09 03:29: Der Punkt bleibt trotz des Payload-Fixes offen. Der qwen-Re-Run `results_20260409_0312_gm_compare_qwen_sweep_n256.jsonl` kommt nur auf `1/4`, und der bereinigte Produkt-Gate-Lauf `text_rpg_product_gate_20260409_032736.md` faellt korrekt auf `gm_session summary classified: blocker`. Die aktuellen Blocker bleiben `gm.session.continuity.v1` mit fehlendem `slot-03` und `turn-0007` sowie `gm.session.reveal-discipline.v1` mit fehlendem `Geraeusch`.
  - Arbeitsstand 2026-04-09 08:18: Die aktuelle Triage zieht den Restpunkt auf Literal-Treue ein. Die Abschnittsstruktur ist stabil, aber die Produktantwort paraphrasiert sichtbare Pflichtanker noch zu frei: `slot-03` und `turn-0007` fehlen ganz, und `Geraeusch` driftet in eine nicht mehr checkkompatible Schreibweise. Naechster Fixlauf haertet deshalb die Hint-Injektion auf exakte, ASCII-stabile Pflichtanker pro sichtbarer Antwort aus.
  - Zwischenstand 2026-04-09 08:39: Der Fixlauf hat den offenen Rest deutlich verkleinert. `gm.session.continuity.v1` ist jetzt gruen, `gm.session.option-quality.v1` ist ebenfalls gruen, und das Product Gate steht bei `3/4`. Offen bleibt nur noch `gm.session.reveal-discipline.v1`: Im Lauf `results_20260409_0838_gm_session.jsonl` fehlen weiter die exakten Literalanker `Geraeusch`, `Druck` und `Entscheidung`, obwohl Format, Nummerierung und die restlichen GM-Faelle jetzt halten.
  - Arbeitsauftrag 2026-04-09 09:40: Die frische Nachmessung `novapolis_agent/eval/results/results_20260409_0910_gm_session.jsonl` zeigt die letzte echte Haertekante: Reveal antwortet noch mit `Geräusch` statt dem exakten ASCII-Literal `Geraeusch`, und `gm.session.option-quality.v1` kippt wieder auf eine Inline-`Optionen:`-Zeile ohne eigenes `State_Patches:`-Segment. Der naechste Fixlauf rekonstruiert deshalb den finalen Vier-Sektions-Output deterministisch aus der Modellantwort, erzwingt ASCII-stabile Pflichtanker in `Szene:`/`Konsequenz:` und zieht fehlende `State_Patches:`- bzw. `1./2./3.`-Optionen am Endtext kanonisch nach.
  - Umsetzung 2026-04-09 09:48: Der Chat-Pfad fuehrt jetzt genau diesen Rebuilder aus. `novapolis_agent/app/api/chat.py` parsed den finalen Modelltext in die vier Pflichtsektionen, ersetzt Aliasformen wie `Geräusch` wieder durch `Geraeusch`, zerlegt Inline-Optionen in echte `1./2./3.`-Zeilen und setzt fehlende `State_Patches:`-Segmente auf `[]`. Der gezielte Pytest-Block in `novapolis_agent/tests/test_api_chat_internal_branches.py` ist mit drei relevanten Regressionen gruen; offen bleibt der Punkt, bis ein frischer Product-Gate-Lauf den letzten Messstand aktualisiert.
  - Fresh-Run 2026-04-09 09:57: Der neue Produktlauf `.tmp/results/reports/text_rpg_product_gate_20260409_095602.md` zieht jetzt den kompletten technischen Pfad gruen durch; `gm_session_eval` selbst ist PASS. Offen bleibt nur die KPI-Summary `.tmp/results/reports/gm_session_kpi_summary_20260409_095602.md` mit `Success: 2/4`: Reveal verfehlt weiter die exakten Literale `Geraeusch` und `Entscheidung`, und `gm.session.option-quality.v1` verfehlt als Beobachtung die sichtbaren Labels `vorsichtige`, `riskante` und `soziale`.
  - Arbeitsauftrag 2026-04-09 10:40: Der naechste Fixlauf trennt die Pflichtterm-Haertung jetzt von den allgemeinen Sichtbarkeitsankern. Reveal bekommt einen eigenen Pfad fuer die exakten sichtbaren Terme `Geraeusch`, `Druck` und `Entscheidung`, und die Optionsstruktur bekommt einen separaten Pflichtlabel-Pfad fuer `vorsichtige`, `riskante` und `soziale`, damit die finalen Strings nicht mehr nur implizit ueber generische Anchor-Listen zusammenfallen.
  - Abschluss 2026-04-09 12:20: Der reproduzierte Root Cause lag im Eval-Pfad selbst: `novapolis_agent/scripts/run_eval.py` haengt fuer Szenenfaelle einen zweiten Userturn `Hinweis: Verwende diese Begriffe ...` an, und `novapolis_agent/app/api/chat.py` hatte dadurch den letzten statt den letzten passenden Vertrags-Prompt fuer Strict-RPG-Hint und Rebuilder gelesen. Der Fix ignoriert diesen Eval-Hinweis als Vertragsquelle, neue Regressionen decken denselben Drift ab, `novapolis_agent/eval/results/results_20260409_1217_gm_session.jsonl` steht bei `4/4`, und der kanonische Produktlauf `.tmp/results/reports/text_rpg_product_gate_20260409_121807.md` ist wieder PASS.

- [x] [Jetzt] Eval-Resultatheader auf das effektive Modell ziehen.
  - Ziel: Ergebnisdateien aus `novapolis_agent/scripts/run_eval.py` sollen im `_meta`-Header dasselbe Modell ausweisen, das der Lauf tatsaechlich verwendet hat, damit die GM-Vergleichslaeufe nicht durch einen falschen Default im Kopf verfälscht werden.
  - Akzeptanzkriterien:
    1) `_meta.model` bevorzugt `--model` bzw. `model_override`, solange ein Override gesetzt ist,
    2) derselbe effektive Modellname bleibt auch in Sweep-Dateien konsistent sichtbar,
    3) ein gezielter Test deckt die Header-Metadaten gegen Regression ab,
    4) die anschliessende qwen-Nachmessung kann sich auf korrekt beschriftete Resultatdateien stuetzen.
  - Evidenz: `novapolis_agent/eval/results/results_20260408_2359_gm_compare_llama.jsonl` fuehrte im `_meta`-Header zunaechst `"model": "qwen2.5:7b"`, obwohl `"overrides": {"model": "llama3.1:8b"}` denselben Lauf korrekt beschrieb; die Divergenz kam direkt aus `novapolis_agent/scripts/run_eval.py`.
  - Ergebnis 2026-04-09 00:40: `novapolis_agent/scripts/run_eval.py` zieht `meta_header["model"]` jetzt ueber den effektiven Override statt ueber den Settings-Default, und `novapolis_agent/tests/scripts/test_run_eval_result_metadata.py` deckt denselben Fall gezielt ab. Die anschliessenden Sweep-Dateien `results_20260409_0041_gm_compare_qwen_sweep_n256.jsonl` bis `_n768.jsonl` fuehren im `_meta`-Header konsistent `"model": "qwen2.5:7b"` plus `"overrides": {"num_predict": ...}`.

- [x] [Als naechstes] Verbleibende Pyright-Warnungen im aktiven Text-RPG-Produktpfad auf belastbare Typen einengen.
  - Ziel: Der kanonische Agent-Typenlauf soll nicht nur fehlerfrei, sondern im produktnahen App-/Runtime-Pfad auch warnungsarm und semantisch enger werden, damit `pyright -p pyrightconfig.json` weniger `Unknown`-Daten durch Chat-, Session- und TTS-Lauf traegt.
  - Akzeptanzkriterien:
    1) die aktuellen Pyright-Warnungen in `app/api/chat.py`, `app/api/sim.py`, `app/main.py` und `app/tts/providers.py` werden auf konkrete Mapping-/Payload-Typen oder enge Coercion-Pfade zurueckgefuehrt,
    2) der produktive Text-RPG-Pfad behaelt denselben API-, Session- und TTS-Vertrag ohne Parallelmodell oder Verhaltensdrift,
    3) `pyright -p pyrightconfig.json`, `mypy --config-file mypy.ini app scripts` und die betroffenen Agent-Tests bleiben gruen,
    4) der Punkt bleibt auf den aktiven Produktpfad begrenzt; spaetere Warnungen in Eval-/RAG-Helfern koennen separat bewertet werden.
  - Evidenz: Der aktuelle Typenreport `.tmp/results/reports/checks_types_20260407_170654.log` endet zwar mit `0 errors`, meldet aber weiter Warnungen fuer unbekannte oder nur teilweise bekannte Payloads in `novapolis_agent/app/api/chat.py`, `novapolis_agent/app/api/sim.py`, `novapolis_agent/app/main.py` und besonders `novapolis_agent/app/tts/providers.py`; der Full-Check ist dadurch nicht rot, aber der aktive Produktpfad bleibt typseitig noch breiter als noetig.
  - Ergebnis 2026-04-07: `app/api/chat.py`, `app/api/sim.py`, `app/main.py` und `app/tts/providers.py` fuehren JSON-/Cache- und Snapshot-Payloads jetzt ueber engere Coercion- und TypedDict-Pfade statt ueber implizit unbekannte Dict-Formen. Der erneute Lauf `pyright -p pyrightconfig.json` meldet im aktiven Produktpfad keine Warnungen mehr; der spaetere Nachlauf in `utils/eval_utils.py` und `utils/rag.py` zieht auch den zuvor getrennten Restpfad auf `0 warnings`. `mypy --config-file mypy.ini app scripts` bleibt gruen, und der gezielte Pytest-Block fuer Chat, Sim und TTS ist PASS.

- [x] [Jetzt] Session- und Kampagnenvertrag fuer das Text-RPG v1 als API- und Backend-SSOT festziehen.
  - Ziel: Der Agent soll vom generischen Chat mit optionaler Session-ID zu einer belastbaren Spielsession mit Szenen-, Kampagnen- und Weltzustandsgrenzen uebergehen.
  - Akzeptanzkriterien:
    1) Request-/Response-Modelle unterscheiden sauber zwischen `session_id`, `campaign_id`, `scene_id`, Spielerinput, angebotenen Optionen und rueckgelieferten `state_patches`,
    2) ein Session-Lauf ist speicher-, fortsetz- und abbrechbar, ohne dass Fortschritt nur implizit im freien Chattext steckt,
    3) Weltinterner Hidden-Context und PC-sichtbare Antwortflaeche sind vertraglich getrennt,
    4) OpenAPI, Tests und Runbook fuehren denselben Session-Vertrag.
  - Ergebnis 2026-04-06: `novapolis-dev/docs/specs/text-rpg-session-contract-v1.md` zieht jetzt `campaign_id`, `session_id`, `scene_id`, `slot_id`, `turn_id`, `options`, `state_patches` sowie die Log-Kanaele `world|pc|ally|sys` als kanonischen Vertrag zusammen; `novapolis_agent/docs/runbook.md` fuehrt denselben Vertrag als operativen Referenzanker fuer den ersten Slice.
  - Evidenz: `novapolis_agent/app/api/models.py` fuehrt aktuell nur generische Chat-Modelle mit optionaler `session_id`, `novapolis_agent/app/core/prompts.py` kennt `State_Patches` bislang nur als Formattext, `novapolis_agent/app/api/chat.py` speichert Session-Memory ohne eigentlichen Kampagnen-/Spielzustandsvertrag, und `novapolis-dev/docs/specs/text-rpg-session-contract-v1.md` definiert jetzt den kanonischen Zielvertrag.

- [x] [Jetzt] Lokale Runtime-Baseline fuer den ersten Slice auf `Ollama + qwen2.5:7b` festziehen.
  - Ziel: Der lokale Produktpfad soll fuer 8-GB-VRAM-Hardware einen klaren Standard haben, statt `Ollama` als Runtime und das eigentliche Laufmodell implizit oder historisch gemischt zu lassen.
  - Akzeptanzkriterien:
    1) `Ollama` bleibt die kanonische lokale Runtime-Basis,
    2) `qwen2.5:7b` ist als bevorzugtes Default-Modell fuer 8-GB-VRAM im Agent-Setup festgezogen,
    3) Settings, Beispiel-Env, README und Runbook fuehren denselben Baseline-Entscheid,
    4) `llama3.1:8b` bleibt nur noch als Vergleichs- oder Fallback-Kandidat lesbar, nicht mehr als Default.
  - Ergebnis 2026-04-06: `novapolis_agent/app/core/settings.py` setzt `MODEL_NAME` und den Fallback jetzt auf `qwen2.5:7b`; die Root-`.env.example`, `novapolis_agent/README.md` und `novapolis_agent/docs/runbook.md` fuehren denselben Runtime-Standard fuer den lokalen Slice.
  - Evidenz: `novapolis_agent/app/core/settings.py` und der Root-`.env.example` fuehrten bisher `llama3.1:8b` als Default, waehrend der dokumentierte 8-GB-VRAM-Pfad bereits eine quantisierte 7B-Klasse mit `Ollama` als Runtime nahelegt.

- [x] [Jetzt] Spielleiter-Orchestrator zwischen Chat-Flow, Projektkontext, RP-SSOT und Scheduler anschliessen.
  - Ziel: Die KI soll nicht nur frei antworten, sondern den kanonischen RP-Kontext, laufenden Weltzustand und spaetere Scheduler-/Action-Regeln in einem kontrollierten Spielleiterpfad zusammenfuehren.
  - Akzeptanzkriterien:
    1) ein definierter Orchestrator-Pfad injiziert Projektkontext, RP-Retrieval, aktuelle Session-Daten und Hidden-Knowledge kontrolliert in denselben Lauf,
    2) Antworten bleiben im gewuenschten Ausgabeformat `Szene/Konsequenz/Optionen/State_Patches`, erzeugen aber gleichzeitig maschinenlesbare Folgedaten,
    3) Hidden-Informationen aus RP, Knowledge und Sphaeren-/Mind-Cluster-SSOT werden nicht versehentlich an den PC ausgespielt,
    4) der Pfad ist testsicher gegen leere Retrievals, Scheduler-Ausfall und widerspruechliche State-Patches.
  - Arbeitsstand 2026-04-06: Der erste Implementierungsschritt haengt den Orchestrator als opt-in Runtime-Hook an den bestehenden `/chat`- und `/chat/stream`-Pfad, statt sofort einen Parallelendpunkt zu eroeffnen. Ziel dieses Schritts ist die kontrollierte Injektion von Sitzungsrahmen, `public_context`, `hidden_context`, Scheduler-Hinweisen und Patch-Zielen in denselben bestehenden Produktpfad.
  - Ergebnis 2026-04-06: `novapolis_agent/app/api/models.py` fuehrt dafuer jetzt opt-in Felder wie `campaign_id`, `scene_id`, `slot_id`, `turn_id`, `public_context`, `hidden_context`, `scheduler_hints` und `state_patch_hints`; `novapolis_agent/app/api/chat.py` injiziert daraus einen ersten Spielleiter-Orchestrator-Block in `/chat` und `/chat/stream`, ohne einen Parallelendpunkt einzufuehren.
  - Arbeitsstand 2026-04-07: Der naechste Implementierungsschritt legt Projektkontext nicht mehr nur als lose Standard-Bloecke neben den Orchestrator, sondern buendelt Kontextnotizen, einen optional expliziten `retrieval_query` und RP-/Projekt-Retrieval in denselben kontrollierten Spielleiter-Lauf.
  - Ergebnis 2026-04-07: `novapolis_agent/app/api/models.py` fuehrt dafuer jetzt `retrieval_query`; `novapolis_agent/app/api/chat.py` faltet bei aktiviertem Orchestrator Kontextnotizen und RP-/Projekt-Retrieval in denselben Systemblock und unterdrueckt in diesem Pfad die getrennten `[Kontext-Notizen]`-/`[RAG]`-Einblendungen; `novapolis_agent/tests/test_api_chat_internal_branches.py` deckt die gebuendelte Injektion gezielt ab.
  - Ergebnis 2026-04-07 (Vertragsschnitt): `novapolis_agent/app/api/models.py` fuehrt fuer `/chat` jetzt einen expliziten Contract-Block mit `contract_version`, Session-/Slot-Metadaten, `session_status`, `replay_checkpoint_id` und `log_channels`; `novapolis_agent/app/api/chat.py` fuellt diesen Block im bestehenden Produktpfad; `novapolis_agent/app/api/sim.py` validiert und persistiert denselben Rahmen in `savegame.json` und `replay_manifest.json` und normalisiert `state_patches` auf Session-/Slot-/Tick-Kontext; `novapolis_agent/tests/test_api_chat_internal_branches.py`, `test_models_chat_options.py`, `test_api_sim_state.py`, `tests/tests_sim_api.py` und `test_openapi_contract.py` sichern denselben Vertrag.
  - Ergebnis 2026-04-07: `novapolis_agent/app/api/chat.py` zieht bei aktivem Orchestrator jetzt den aktuellen Session-Snapshot als internen Block `[Session-Stand intern]` in denselben Systemlauf, parst `State_Patches:` aus der Modellantwort und schreibt den Folgezug als `pc_log` plus normalisierte `state_patches` ueber `novapolis_agent/app/api/sim.py` in denselben Session-Store zurueck; `novapolis_agent/tests/test_api_chat_internal_branches.py` sichert Snapshot-Injektion und Writeback gezielt ab.
  - Verifikation 2026-04-07: gezielter Pytest-Lauf ueber `test_api_chat_internal_branches.py`, `test_tts_api_contract.py`, `test_tts_cache_contract.py`, `test_tts_provider_abstraction.py`, `test_openapi_contract.py` PASS; `pyright -p pyrightconfig.json` ohne Fehler, nur bestehende Warnungen; `mypy --config-file mypy.ini app tests` weiterhin an vorbestehenden Script-/Shim-Attributpfaden ausserhalb dieses Schnitts blockiert.
  - Evidenz: `novapolis-dev/docs/process/project-context-bridge.ssot.md` fuehrt nur den projektbewussten Chatmodus als Phase 1, `novapolis-dev/docs/specs/scheduler-spec.md` existiert nur als Doku, `novapolis_agent/app/core/prompts.py` bleibt derzeit ein reiner Format-/Persona-Prompt ohne Spielleiter-Orchestrierung, und `novapolis_agent/tests/test_models_chat_options.py` plus `novapolis_agent/tests/test_api_chat_internal_branches.py` decken den neuen Hook jetzt gezielt ab.

- [x] [Als naechstes] Persistente Weltzustands-, Log- und Replay-Pipeline fuer `world_log`, `pc_log` und Savegames schaffen.
  - Ziel: Ein spielbarer Text-RPG-Run braucht nachvollziehbaren Weltfortschritt, Replay und Wiederaufnahme statt nur volatilem Antworttext und einer Minimal-Sim-API.
  - Akzeptanzkriterien:
    1) Weltzustand, Event-Historie und `state_patches` werden pro Session persistiert und auditierbar fortgeschrieben,
    2) `world_log` und `pc_log` entstehen aus demselben Lauf reproduzierbar und koennen fuer Replay/Sim exportiert werden,
    3) Seeds, Resume-Punkte und Abbruchfaelle sind fuer Debugging und spaetere Produktbelege wiederherstellbar,
    4) der Exportpfad bleibt kompatibel mit dem Sim-Client statt ein paralleles Artefaktformat einzufuehren.
  - Ergebnis 2026-04-07: `novapolis_agent/app/api/sim.py` fuehrt jetzt einen dateigestuetzten Session-Store unter `novapolis_agent/tmp/sim_sessions/<session_id>/`; `PUT /session/{session_id}` schreibt `savegame.json`, `world_log.jsonl`, `pc_log.jsonl` und `replay_manifest.json`, `GET /session/{session_id}` liefert den aktuellen Resume-Stand, und `GET /session/{session_id}/replay` gibt den Replay-Manifestkern fuer Hub-/Epoch-Folgeschritte aus.
  - Verifikation 2026-04-07: `novapolis_agent/tests/test_api_sim_state.py` und `novapolis_agent/tests/tests_sim_api.py` decken Artefaktwrite, Reload, Resume-Checkpoint, Replay-Manifest und 404-Pfade gezielt ab.
  - Evidenz: `novapolis_agent/app/api/sim.py` fuehrt nur `{tick,time,regions,actors,events}` als Minimalmodell ohne Persistenz, waehrend `novapolis-sim/scripts/Main.gd` seine Ansicht aktuell aus statischen `world_log.jsonl`/`pc_log.jsonl` unter `res://data/epochs` aufbaut.

- [x] [Als naechstes] Dedizierte Eval- und Regressionssuiten fuer KI-Spielleitung einfuehren.
  - Ziel: Der Agent soll nicht nur auf allgemeine RPG-Stilfragen gut reagieren, sondern auf Kontinuitaet, Geheimhaltung, Wahlqualitaet und valide Zustandsfortschreibung im echten Spielleiterbetrieb getestet werden.
  - Akzeptanzkriterien:
    1) mindestens eine eigene Session-/GM-Suite prueft Kontinuitaet, Reveal-Disziplin, Optionsqualitaet und Patch-Gueltigkeit,
    2) die Suite trennt harte Blocker von Beobachtungen, damit Release-Entscheidungen spaeter nicht auf Bauchgefuehl beruhen,
    3) Ergebnisreports verweisen reproduzierbar auf Session-Faelle, Quellenpakete und aktivierte Checks,
    4) Folgepunkte aus den Ergebnissen werden wieder in dieses Board rueckgekoppelt.
  - Ergebnis 2026-04-07: `novapolis_agent/eval/config/suites.json` fuehrt jetzt `gm_session` als eigene Suite, `novapolis_agent/eval/datasets/rpg/rpg_gm_session_core.v1.jsonl` deckt Kontinuitaet, Reveal-Disziplin, Optionsqualitaet und Patch-Lesbarkeit ab, `novapolis_agent/scripts/run_eval.py` schreibt `slug`, `category` und `tags` in die Ergebnisdateien, `novapolis_agent/scripts/summarize_gm_eval_kpis.py` trennt Blocker-Faelle von Beobachtungen, und `.vscode/tasks.json` fuehrt denselben Lauf plus KPI-Summary als eigene Tasks.
  - Verifikation 2026-04-07: `tests/scripts/test_summarize_gm_eval_kpis.py` und `tests/scripts/test_run_eval_result_metadata.py` PASS; `python novapolis_agent/scripts/validate_eval_datasets.py --strict --suite-config novapolis_agent/eval/config/suites.json --suite gm_session` PASS; `mypy --config-file mypy.ini scripts/run_eval.py scripts/summarize_gm_eval_kpis.py tests/scripts/test_summarize_gm_eval_kpis.py tests/scripts/test_run_eval_result_metadata.py` PASS.
  - Evidenz: `novapolis_agent/docs/runbook.md` fuehrt aktuell nur die Suiten `neutral`, `rpg` und `rp_content`; ein spezifischer Produkt-Gate fuer KI-Spielleitung mit Session-/State-Pruefungen fehlt.

- [x] [Als naechstes] Session-TTS an denselben Spielzustand und dieselben Log-Kanaele anbinden.
  - Ziel: Audio soll spaeter nicht als separater Nebenpfad laufen, sondern dieselben `pc|world|ally|sys`-Kanaele, Cache-Schluessel und Replay-Artefakte wie der Spielzustand verwenden.
  - Akzeptanzkriterien:
    1) Session-Ausgaben koennen kontrolliert in TTS-Requests ueberfuehrt werden, ohne den inhaltlichen Spielzustand zu verlieren,
    2) Artefakte und Manifeste referenzieren denselben Session-/Slot-Kontext wie `world_log`/`pc_log`,
    3) Cache-Key, Rechte- und Fallback-Pfad bleiben mit dem bestehenden TTS-Vertrag kompatibel,
    4) der Sim-Client kann spaeter dieselben Audioartefakte konsumieren statt eines separaten Exportformats.
  - Ergebnis 2026-04-07: `novapolis_agent/app/api/tts_models.py` fuehrt fuer `/tts/synthesize` jetzt denselben Session-/Slot-/Kanalrahmen wie der Text-RPG-Pfad; `novapolis_agent/app/main.py` faltet diesen Rahmen in Cache-Key und Response, schreibt sessionbezogene TTS-Manifest-Eintraege ueber `novapolis_agent/app/api/sim.py`, und `novapolis_agent/app/tts/providers.py` legt Coqui-Artefakte unter `runtime/sessions/<session>/<channel>/...` statt in einem generischen Providerpfad ab.
  - Verifikation 2026-04-07: `novapolis_agent/tests/test_tts_api_contract.py`, `test_tts_cache_contract.py`, `test_tts_provider_abstraction.py` und `test_openapi_contract.py` sichern Vertragsfelder, Cache-Scope, Manifestpfad und sessionbezogenen Coqui-Artefaktpfad gezielt ab.
  - Evidenz: `novapolis_agent/app/main.py` und `novapolis_agent/app/tts/providers.py` liefern produktive TTS-Endpunkte, `novapolis-dev/docs/specs/tts-exporter-coqui.md` beschreibt slotbezogene OGG-Artefakte, und `novapolis-sim/scripts/Main.gd` zeigt Audio-/Epoch-Slots bereits als eigene Oberflaechen an, aber noch ohne Session-Anbindung.

Platzhalter

- [x] Abgleich mit Root Coverage-Gate (R-COV) und Aufnahme fehlender Pruefsteps (Receipt-Formate) in diesen Plan

R-COV Abgleich (Agent)
----------------------

- [x] Gate-Wert uebernommen: Coverage-Fail-Under bleibt `80` (Root-Policy).
- [x] Laufreihenfolge festgelegt: Lint -> Typen -> Tests -> Coverage.
- [x] Standard-Entrypoints dokumentiert:
  - `python scripts/run_checks_and_report.py --scope full`
  - `python scripts/run_pytest_coverage.py --fail-under 80`
- [x] Receipt-Pflicht konkretisiert:
  - `DONELOG.md`: PASS/FAIL, Quote, Zeitstempel, Commit-SHA.
  - `WORKSPACE_STATUS.md`: Kurzstatus "Tests/Typen/Coverage aktuell" mit Datum/Quote.

Neue Aufgaben - TTS & Tools (2025-11-01 22:24)
----------------------------------------------

- 2026-03-27: Wochenabschluss-Refresh. Der aktuelle Full-Check ist im Agent-Scope gruen; der einzige Gesamtblocker des ersten Abschlusslaufs lag im dokumentweiten Freshness-Gate ausserhalb des Agent-Moduls.

- [x] [Jetzt] Driftfix: Coqui-Exporter-Iststand gegen Board abgleichen (`scripts/tts_coqui_export.py` fehlt aktuell im Modul) und Boardstatus danach sauber aktualisieren.
  - Evidenz: `novapolis_agent/scripts/tts_coqui_export.py` (Skeleton mit CLI-Vertrag + `--dry-run`).
- [x] [Jetzt] Mini-Service API-Vertrag definieren (`/tts/health`, `/tts/voices`, `/tts/synthesize`, Request-/Response-Modelle, Fehlercodes, OGG/WAV-Outputmodi).
  - Evidenz: `novapolis_agent/app/api/tts_models.py`, `novapolis_agent/app/main.py`, `novapolis_agent/tests/test_tts_api_contract.py`.
- [x] [Jetzt] Provider-Interface + lokaler Dummy-Adapter anlegen (Coqui folgt spaeter), damit Endpunkte testbar integriert werden koennen.
  - Evidenz: `novapolis_agent/app/tts/providers.py` (`TtsProviderProtocol`, `DummyTtsProvider`, `NullTtsProvider`, Adapter-Scaffolds fuer `coqui`/`ollama`/`openai`), `novapolis_agent/app/main.py` (Provider-Fabrikverdrahtung), `novapolis_agent/tests/test_tts_provider_abstraction.py`.
- [x] [Jetzt] Einfache Auth-Regel fuer TTS-Endpunkte definieren (Header-Token/ENV), inkl. klarer 401/403-Pfade.
  - Evidenz: `novapolis_agent/app/core/settings.py` (`TTS_AUTH_ENABLED`, `TTS_AUTH_HEADER`, `TTS_AUTH_TOKEN`), `novapolis_agent/app/main.py` (`_require_tts_auth`), `novapolis_agent/tests/test_tts_auth_contract.py`.
- [x] [Jetzt] Rate-Limit-Verhalten fuer TTS festlegen (Reuse des vorhandenen In-Memory-Limiters, Grenzwerte, Header, keine Regression fuer Chat-Endpunkte).
  - Evidenz: `novapolis_agent/app/main.py` (scope-basierter In-Memory-Limiter), `novapolis_agent/app/core/settings.py` (`TTS_RATE_LIMIT_*`), `novapolis_agent/tests/test_tts_rate_limit_contract.py`, `novapolis_agent/tests/test_rate_limit_and_timeout.py`, `novapolis_agent/tests/test_input_length_and_rate_headers.py`.
- [x] [Jetzt] Lokalen TTS-Cache-Vertrag festlegen (Hash-Key aus Text+Stimme+Format+Settings, Zielpfad, Hit/Miss-Semantik, Loeschpfad).
  - Evidenz: `novapolis_agent/app/main.py` (`_tts_cache_*`, `/tts/cache/stats`, `/tts/cache/cleanup`), `novapolis_agent/app/core/settings.py` (`TTS_CACHE_*`), `novapolis_agent/tests/test_tts_cache_contract.py`.
- [x] [Jetzt] Tests fuer Mini-Service-Skeleton anlegen (API-Vertrag, Auth, Rate-Limit-Header, Cache-Hit/Miss, Error-Codes).
  - Evidenz: `novapolis_agent/tests/test_tts_api_contract.py`, `novapolis_agent/tests/test_tts_auth_contract.py`, `novapolis_agent/tests/test_tts_rate_limit_contract.py`, `novapolis_agent/tests/test_tts_cache_contract.py`, `novapolis_agent/tests/test_tts_provider_abstraction.py`, `novapolis_agent/tests/test_openapi_contract.py`.
- [x] [Als naechstes] Coqui-Exporter (Build-Time) in Teilaufgaben aufspalten: (1) Voice-Mapping-Spec, (2) Hash-Cache-Layout, (3) Exportzielstruktur `novapolis-sim/assets/voiceovers/de/`, (4) CLI/Args, (5) Smoke-Test.
  - Evidenz: Detaillierte Teilaufgaben sind im Block `Neue Aufgaben - Chronistin Ausbau (2026-02-25)` konkretisiert.
- [x] [Als naechstes] VS Code Tasks (Planung): "TTS: export (coqui)", "TTS: clean cache", "TTS: check voices". Umsetzung erst nach Spec-Freigabe.
  - Evidenz: `.vscode/tasks.json` (Labels `TTS: export (coqui)`, `TTS: clean cache`, `TTS: check voices`).
- [x] [Als naechstes] README-Truthfulness: TTS-Claims in `novapolis_agent/README.md` bis zur Implementierung explizit als „geplant“ markieren und auf dieses Board verweisen.
  - Evidenz: `novapolis_agent/README.md` (Abschnitt "Ist-Stand (Betriebsfaehigkeit)" mit klarer Contract-First-Einordnung), `novapolis_agent/docs/runbook.md` (operativer Ist-Stand), `.vscode/tasks.json` (TTS-Export-Task auf reales Wrapper-Script statt Platzhalter).
- [x] [Als naechstes] Eigener TTS-Model-Track konkretisieren: (1) Daten-/Rechte-Policy, (2) Trainingsziel (Finetune vs. eigenes Modell), (3) Evaluationsmetriken, (4) Runtime-Adapter-Plan hinter Schritt 7.
  - Evidenz: `novapolis_agent/docs/tts-model-track.md`.
- [x] [Spaeter] Templates bereitstellen: Beispiel-YAML fuer `knowledge:`/`actions:` in Agent-README verlinken (Quelle: Dev-Annotation-Spec).
  - Evidenz: `novapolis_agent/docs/templates/knowledge-actions.example.yaml`, `novapolis_agent/README.md` (Template-Verweis).

Neue Aufgaben - Chronistin Ausbau (2026-02-25)
-----------------------------------------------

- [x] [Jetzt] TTS-Exporter von Skeleton auf Build-Time-MVP bringen (echter OGG-Write-Pfad statt `--help`-Only).
  - Ziel: Die bestehende CLI (`tts_coqui_export.py`) soll den dokumentierten I/O-Vertrag real bedienen (Input + Voice-Map -> exportierte OGG-Dateien in Sim-Zielstruktur).
  - Akzeptanzkriterien:
    1) Erfolgreicher Dry-Run und Real-Run mit testbaren Exitcodes (0/Fail),
    2) erzeugte OGG-Dateien folgen stabilem Namensschema,
    3) Hash-/Cache-Layout ist deterministisch und dokumentiert,
    4) bestehende Compliance-Gates (Allowlist/Lizenzkopie) bleiben hart aktiv.
  - Evidenz: `novapolis_agent/scripts/tts_coqui_export.py` (Input-Parser + deterministischer Hash-Cache + OGG-Export + Manifest), `novapolis_agent/config/tts_model_allowlist.json`, `novapolis_agent/tests/scripts/test_tts_coqui_export_policy.py` (Export/Cache-Tests).

- [x] [Jetzt] Runtime-TTS mindestens einen echten Provider-Endpunkt produktiv schalten (statt reiner Adapter-Scaffolds).
  - Ziel: Die Chronistin soll fuer mindestens einen erlaubten Provider echten Audio-Output liefern, ohne den bestehenden Contract-First-API-Vertrag zu brechen.
  - Akzeptanzkriterien:
    1) Provider-Fabrik liefert fuer einen freigegebenen Provider keine Placeholder-Antwort,
    2) `/tts/synthesize` liefert reproduzierbare Metadaten + Artefaktpfad,
    3) Auth/Rate-Limit/Cache-Verhalten bleibt unveraendert grün,
    4) klarer Fallback-Pfad bei nicht verfuegbarem Provider (kontrollierter Fehler statt Silent-Fail).
  - Evidenz: `novapolis_agent/app/tts/providers.py` (CoquiRuntimeProvider + HTTP-Endpunktverdrahtung), `novapolis_agent/app/main.py` (`/tts/synthesize` mit `status=ok` bei Real-Provider, `artifact_path`, 503 bei Provider-Ausfall), `novapolis_agent/app/core/settings.py` (`TTS_COQUI_*`, `TTS_RUNTIME_OUTPUT_DIR`), `novapolis_agent/tests/test_tts_provider_abstraction.py` (Runtime-Erfolg + 503-Fallback), `novapolis_agent/tests/test_tts_api_contract.py`.

- [x] [Jetzt] Eval-Suite um neuen Qualitaets-Check-Track (`quality_de`) operationalisieren.
  - Ziel: Die zuletzt eingebauten Checks (`languagetool_quality`, `sts_relevance`) sollen als reproduzierbarer Standardlauf in Suites/Tasks verankert werden.
  - Akzeptanzkriterien:
    1) `suites.json` definiert transparent, in welcher Suite `quality_de` verpflichtend ist,
    2) passende VS-Code-Task(s) sind vorhanden,
    3) mindestens ein dokumentierter Lauf mit Ergebnisdatei + Kurzbewertung liegt vor,
    4) Schwellwerte und Begründung sind im Runbook nachvollziehbar dokumentiert.
  - Evidenz: `novapolis_agent/eval/config/suites.json` (Suite `neutral` + dedizierte Suite `quality_de` mit verpflichtendem Alias-Check), `.vscode/tasks.json` (Task `Eval: suite quality_de (20, asgi)` + `quality_de` im neutralen Task), `novapolis_agent/docs/runbook.md` (Schwellwerte/Begründung dokumentiert), `novapolis_agent/eval/results/results_20260226_0025_quality_de.jsonl` (dokumentierter Lauf inkl. `_meta.enabled_checks` und Kurzbewertung 15/20).

- [x] [Als naechstes] Terminologie-/Synonym-Governance fuer Eval regressionssicher machen.
  - Ziel: Die jüngsten Synonym-Fixes (strukturierte Synonyme, broader_terms-Filter) sollen gegen erneute Semantik-Regressionen abgesichert werden.
  - Akzeptanzkriterien:
    1) feste Regeln fuer `synonyms` vs. `broader_terms` vs. `narrower_terms` dokumentiert,
    2) Negativtests verhindern zu breite Synonym-Treffer,
    3) Overlay-Prioritaet (local > base) ist explizit getestet,
    4) Eval-Datensatzbeispiele mit kritischen Begriffen sind abgedeckt.
  - Evidenz: `novapolis_agent/eval/config/synonyms.local.json` (strukturierte Begriffsrelationen inkl. `broader_terms`), `novapolis_agent/scripts/run_eval.py` (`get_synonyms`-Governance-Regeln dokumentiert + Ausschluss von `broader_terms`), `novapolis_agent/tests/test_synonyms_overlay.py` (Overlay-Priorität/Negativtests), `novapolis_agent/tests/test_batch3_unit.py` (kritisches `parmesan`-Beispiel gegen zu breite Treffer), gezielter Testlauf `pytest -q novapolis_agent/tests/test_synonyms_overlay.py novapolis_agent/tests/test_batch3_unit.py` grün.

- [x] [Als naechstes] README/Runbook-Truthfulness-Drift erneut bereinigen (Stand nach Eval-/TTS-Ausbau).
  - Ziel: Dokumentation soll nur verifizierte Ist-Claims enthalten und bekannte Driftstellen aus früheren Reviews final auflösen.
  - Akzeptanzkriterien:
    1) veraltete oder unbelegte Claims entfernt/aktualisiert,
    2) Task-/Dateiverweise sind auf vorhandene Artefakte geprüft,
    3) Ist-Stand-Abschnitt trennt klar zwischen produktiv, experimentell und geplant,
    4) abschließender Truthfulness-Check ist im DONELOG dokumentiert.
  - Evidenz: `novapolis_agent/README.md` (Ist-Stand/Quality-DE und TTS-Status auf produktiven Realstand nachgezogen), `novapolis_agent/docs/runbook.md` (STS-Schwelle `0.09`, gültige Suite-Pakete ohne `neutral_gpt_samples`, Quality-DE-Status inkl. 20/20-Reproduzierbarkeit), `novapolis_agent/docs/DONELOG.txt`, `novapolis-dev/docs/donelog.md`.

- [x] [Als naechstes] Eval-Marathon als steuerbaren Qualitätsanker ausbauen (KPI + Abbruchkriterien + Nacharbeitspfad).
  - Ziel: Der vorhandene Marathon-Task soll nicht nur laufen, sondern konsistente Entscheidungsdaten für die Weiterentwicklung der Chronistin liefern.
  - Akzeptanzkriterien:
    1) KPI-Mindestset definiert (Pass-Rate, häufigste Fehl-Checks, Top-Regressionspakete),
    2) Fail-Triage-Regeln (Blocker/Warnung) sind dokumentiert,
    3) Ergebnis-Receipts verlinken reproduzierbar auf Datenpakete/Checks,
    4) Rückkopplung in Board-Punkte erfolgt mit klarer Priorisierung (`Jetzt/Als naechstes/Spaeter`).
  - Evidenz: `.vscode/tasks.json` (`Eval: suite marathon (~60m, asgi, loud)`), `novapolis_agent/eval/results/`, `novapolis_agent/docs/DONELOG.txt`, `novapolis-dev/docs/donelog.md`.

Eval-Marathon Betriebsprofil (v1, verbindlich)
----------------------------------------------

- KPI-Mindestset (pro Lauf):
  - `pass_rate_total` (PASS/gesamt),
  - `top_failed_checks` (haeufigste fehlgeschlagene Checks aus `_meta.failed_checks`),
  - `top_regression_packages` (Pakete mit niedrigster Pass-Rate),
  - `retry_share` (Anteil Antworten mit Retry-Hinweis/Fallback-Markern).
- Fail-Triage-Regeln:
  - `Blocker`: `pass_rate_total < 0.85` oder ein Pflichtcheck faellt in >=20% der Faelle,
  - `Warnung`: `0.85 <= pass_rate_total < 0.90` oder einzelne Pakete <0.80,
  - `Beobachtung`: `pass_rate_total >= 0.90`, aber klarer Cluster in einem Check/Paket.
- Receipt-Standard (reproduzierbar):
  - Jede Auswertung verlinkt explizit auf Task-Label, konkrete Paketliste, aktivierte `--checks` und Ergebnisdatei `novapolis_agent/eval/results/results_<timestamp>_<run_id>.jsonl`.
  - Referenzablage fuer Laufbelege: `novapolis_agent/docs/DONELOG.txt`.
- Rueckkopplung ins Board:
  - `Blocker` -> neuer/aktualisierter Punkt unter `Jetzt`,
  - `Warnung` -> `Als naechstes`,
  - `Beobachtung` -> `Spaeter` oder bestehendem Punkt als Evidenz zuordnen.

Neue Aufgaben - Datensaetze & Training (2026-02-25)
----------------------------------------------------

- [x] [Jetzt] Lokale Kontext-Notizen Defaults vom Root-eval auf den Agent-Modulpfad migrieren.
  - Ziel: `CONTEXT_NOTES_PATHS` und der Oeffner fuer lokale Kontext-Notizen sollen den kanonischen Modulpfad `novapolis_agent/eval/config/` nutzen, damit der verbliebene Root-eval-Rest technisch und dokumentarisch entkoppelt werden kann.
  - Akzeptanzkriterien:
    1) `app/core/settings.py` fuehrt fuer Markdown/JSON/JSONL/context.notes nur noch Modulpfade,
    2) `scripts/open_context_notes.py` nutzt denselben Modulpfad auch im Fallback,
    3) `README.md` dokumentiert Beispiel- und Defaultpfade nur noch unter `novapolis_agent/eval/config/`,
    4) bestehende Script- und Kontext-Tests bleiben gruen.
  - Evidenz: `novapolis_agent/app/core/settings.py`, `novapolis_agent/scripts/open_context_notes.py`, `novapolis_agent/README.md`, `eval/config/context.local.md` und `novapolis_agent/eval/config/context.local.md`.
  - Abschluss 2026-03-28: `EVAL_*`, `CONTEXT_NOTES_PATHS` und `RAG_INDEX_PATH` zeigen jetzt auf `novapolis_agent/eval/...`; `scripts/open_context_notes.py` nutzt denselben Default, die README ist nachgezogen, und die verbleibende Root-Kopie wurde anschliessend quarantanisiert.

- [x] [Jetzt] Artefakt-Cleanup von dateibasierter auf runbasierte Retention umstellen.
  - Ziel: Reale Cleanup-Laeufe duerfen zusammengehoerige Eval- oder LoRA-Runs nicht mehr in getrennte Keep-/Remove-Entscheidungen aufspalten.
  - Akzeptanzkriterien:
    1) `cleanup_artifacts.py` entscheidet fuer `novapolis_agent/eval/results` und `outputs` auf Run-/Cluster-Ebene statt pro Datei,
    2) ein Dry-Run behaelt oder entfernt Artefakte desselben Runs konsistent als Gruppe,
    3) Name-Pinning (`baseline`, `marathon`, `quality_de`) bleibt erhalten, ohne Laufgruppen zu zerreissen,
    4) Tests decken mindestens einen Eval-Run-Cluster und einen Output-Laufordner gegen Split-Retention ab.
  - Evidenz: Der Dry-Run `Data: artifacts cleanup (dry-run)` vom 2026-03-29 (`.tmp/results/reports/artifact_lifecycle_report.json`) wuerde aktuell 1893 Dateien entfernen und dabei zusammengehoerige Run-Artefakte wie `outputs/lora-baseline-vscode/*` sowie die Maerz-2026-Eval-Cluster nur teilweise behalten.
  - Abschluss 2026-03-29: `cleanup_artifacts.py` gruppiert `novapolis_agent/eval/results` jetzt ueber den letzten Run-Zeitanker und `outputs` ueber Laufordner/Top-Level-Eintraege; Name-Pinning gilt auf relativen Artefaktpfaden statt nur auf Dateinamen, neue Tests sichern Eval-Cluster und Output-Laufordner gegen Split-Retention ab, und der erneute Dry-Run haelt `outputs/` vollstaendig zusammen (`keep=68`, `remove=0`) und markiert bei `novapolis_agent/eval/results` nur noch ganze Gruppen (`keep=60`, `remove=1813`).

- [x] [Als naechstes] Export-/Kurationspfad gegen Null-Exports durch historische Results-Drift haerten.
  - Ziel: Die Task-Kette `Data: export+pack (latest results)` soll fuer reale aktuelle Ergebnisse trainierbare Artefakte liefern oder bei unbrauchbaren Quellen hart und klar abbrechen.
  - Akzeptanzkriterien:
    1) der Export erkennt historische oder inkonsistente `source_path`-Verweise und faellt kontrolliert auf validen Input oder expliziten Fehler zurueck,
    2) ein Null-Export (`0 Eintraege`) wird nicht mehr als still brauchbarer Tasklauf durchgereicht,
    3) Runbook und README nennen den kanonischen Weg fuer kuratierbare Results ohne manuelle Pfadforensik,
    4) mindestens ein dokumentierter Lauf erzeugt wieder ein nichtleeres Export- oder Pack-Artefakt aus einem aktuellen Results-Set.
  - Evidenz: Die vorhandenen Laufbelege fuehren fuer 2026-02-27 einen `export_finetune.py`-Run mit `0` Eintraegen wegen Source-Path-Drift an, waehrend der nachgelagerte Pack-Schritt nur auf bereits vorhandenem Exportmaterial erfolgreich war; die Tasklabels bleiben dennoch der dokumentierte Standardpfad.
  - Abschluss 2026-03-30: `scripts/export_finetune.py` inspiziert Results jetzt vor dem Export, nutzt Result-Metadaten plus `source_file` fuer robustere Dataset-Aufloesung, matched Item-IDs/Slugs resilienter und liefert bei `0` exportierbaren Datensaetzen einen expliziten Fehler statt stiller Erfolgsantwort. `scripts/curate_dataset_from_latest.py` prueft `results_*.jsonl` newest-first auf Exportierbarkeit und nimmt das neueste kuratierbare Set; uebersprungene Drift-Kandidaten werden als `skipped_results` ausgewiesen. Regressionstests in `tests/scripts/test_export_finetune_edges.py`, `tests/scripts/test_export_finetune_more_edges.py`, `tests/scripts/test_curate_dataset_from_latest_minimal.py`, `tests/test_curate_dataset_from_latest_smoke.py`, `tests/test_curate_filters_smoke.py` und `tests/test_export_and_prepare_pipeline.py` sind gruen. Der temp-basierte Real-Lauf gegen `novapolis_agent/eval/results/` waehlte nach mehreren unbrauchbaren Maerz-2026-Kandidaten kontrolliert `results_20260226_0306_quality_de_round7b_repeat3.jsonl` und erzeugte wieder `20` Export-Eintraege plus Pack-Split `18/2`.

- [x] [Jetzt] Individuelle Trainingsdatensaetze als kanonische Pakete definieren (Chronistin-Profile).
  - Ziel: Neben Eval-Paketen strukturierte Training-Pakete fuer unterschiedliche Einsatzprofile der Chronistin bereitstellen (z. B. neutral-assistiv, lore-intensiv, operativ-kurz).
  - Akzeptanzkriterien:
    1) Namensschema + Pflichtmetadaten (`id`, `slug`, `tags`, Profilkennzeichnung) verbindlich dokumentiert,
    2) mindestens drei Profilpakete im Zielpfad angelegt,
    3) Validator-Lauf liefert fuer die neuen Pakete keinen Hard-Fail,
    4) Herkunft/Policy in der Provenance-Doku nachvollziehbar hinterlegt.
  - Evidenz: `novapolis_agent/eval/datasets/training/chronistin_neutral_assistiv.v1.jsonl`, `novapolis_agent/eval/datasets/training/chronistin_lore_intensiv.v1.jsonl`, `novapolis_agent/eval/datasets/training/chronistin_operativ_kurz.v1.jsonl`, `novapolis_agent/scripts/validate_eval_datasets.py` (strict: `files=3, records=9, ids=9, slugs=9`), `novapolis-dev/docs/dataset-provenance.md`.

- [x] [Jetzt] Datensatz-Erzeugungspfad standardisieren (manuell + generiert + kuratiert).
  - Ziel: Ein reproduzierbarer Workflow von Rohideen bis zum trainierbaren JSONL-Paket ohne ad-hoc Einzelschritte.
  - Akzeptanzkriterien:
    1) klarer Ablauf dokumentiert: `generate_eval_dataset.py` -> `run_eval.py` -> `export_finetune.py` -> `prepare_finetune_pack.py`,
    2) optionaler Kurationspfad via `curate_dataset_from_latest.py` integriert,
    3) Mindestfilter fuer Antwortqualitaet und Duplikatkontrolle verbindlich definiert,
    4) mindestens ein End-to-End-Beispiellauf mit Artefaktpfaden dokumentiert.
  - Evidenz: `novapolis_agent/scripts/generate_eval_dataset.py`, `novapolis_agent/scripts/curate_dataset_from_latest.py`, `novapolis_agent/scripts/export_finetune.py`, `novapolis_agent/scripts/prepare_finetune_pack.py`, E2E-Artefakte unter `novapolis_agent/eval/results/` und `novapolis_agent/eval/results/finetune/`.

Datensatz-Erzeugungspfad (verbindlich, v1)
------------------------------------------

- Pflichtablauf (manuell/generiert):
  1) `generate_eval_dataset.py` erzeugt/erweitert ein Eingabepaket,
  2) `run_eval.py` erzeugt `results_<timestamp>*.jsonl`,
  3) `export_finetune.py` exportiert Finetune-JSONL,
  4) `prepare_finetune_pack.py` erstellt `*_train.jsonl` und `*_val.jsonl`.
- Optionaler Kurationszweig (statt Schritt 3+4 einzeln):
  - `curate_dataset_from_latest.py` nutzt das neueste Results-Artefakt und fuehrt Export + Split in einem reproduzierbaren Lauf aus.
- Mindestfilter (verbindlicher Baseline-Standard):
  - `include_failures=false` (nur erfolgreiche Antworten),
  - `min_output_chars >= 20`,
  - `dedupe_by_instruction=true` (kein `--no-dedupe`),
  - optional fuer strengere Kuration: `near_dup_threshold >= 0.80` und/oder `min_instr_cover >= 0.10`.
- E2E-Beispiellauf (dokumentierter Artefaktpfad):
  - Eval-Ergebnis: `novapolis_agent/eval/results/results_20260226_0025_quality_de.jsonl`.
  - Export: `novapolis_agent/eval/results/finetune/finetune_openai_chat_results_20251015_1430_20251015_1430.jsonl`.
  - Train/Val: `novapolis_agent/eval/results/finetune/finetune_openai_chat_results_20251015_1430_20251015_1430_train.jsonl` und `novapolis_agent/eval/results/finetune/finetune_openai_chat_results_20251015_1430_20251015_1430_val.jsonl`.

- [x] [Jetzt] Quality-DE-Datensatzspur als eigenes Paketband verstetigen (Core/Drift/Canary).
  - Ziel: Der neue `quality_de`-Track soll nicht nur auf allgemeinen Neutral-Paketen laufen, sondern ein eigenes, reproduzierbares Paketband mit Qualitätsfokus erhalten.
  - Akzeptanzkriterien:
    1) eigenes Paketset im Neutral-Pfad benannt und dokumentiert (Core + Drift + Canary),
    2) jeder Datensatz trägt Pflichtmetadaten (`id`, `slug`, `tags`, `category`) konsistent,
    3) strict-Validator akzeptiert das Paketset ohne Hard-Fail,
    4) mindestens ein `quality_de`-Lauf referenziert explizit dieses Paketband.
  - Evidenz: `novapolis_agent/eval/datasets/neutral/quality_de_core.v1.jsonl`, `novapolis_agent/eval/datasets/neutral/quality_de_drift.v1.jsonl`, `novapolis_agent/eval/datasets/neutral/quality_de_canary.v1.jsonl`, `novapolis_agent/eval/config/suites.json`, `.vscode/tasks.json` (`Eval: suite quality_de (20, asgi)` auf neues Paketband), strict Validator (`files=10, records=312, ids=312, slugs=312`), dokumentierter Lauf `novapolis_agent/eval/results/results_20260226_0209_quality_de.jsonl`.

- [x] [Als naechstes] Datensatz-Driftkontrolle mit Monats-Baseline einführen (Passrate + Failure-Cluster).
  - Ziel: Regressionssignale in Datensätzen früh erkennen, bevor sie Training/Eval-Gesamtmetriken verzerren.
  - Akzeptanzkriterien:
    1) monatliche Baseline-Datei mit KPI-Mindestset abgelegt (Pass-Rate, Top-Fehlchecks, Top-Missing-Terms),
    2) Vergleichslauf gegen letzte Baseline ist reproduzierbar dokumentiert,
    3) definierte Schwellwerte für Warnung/Blocker bei negativer Drift vorhanden,
    4) Abweichungen werden im Board mit Priorität (`Jetzt/Als naechstes`) rückgekoppelt.
  - Evidenz: `novapolis_agent/scripts/eval_drift_report.py`, `novapolis_agent/eval/results/baselines/training_profiles.2026-02.json`, `novapolis_agent/eval/results/drift/training_profiles_drift_2026-02-27.json`, `novapolis_agent/eval/results/results_20260227_0231.jsonl`, `novapolis_agent/eval/results/results_20260227_0424_training_profiles_post_novapolis_signal.jsonl`.

Monats-Baseline Driftkontrolle (verbindlich, v1)
-------------------------------------------------

- KPI-Mindestset (Pflichtfelder je Baseline/Report):
  - `pass_rate`,
  - `top_failed_checks`,
  - `top_missing_terms`.
- Reproduzierbarer Ablauf:
    1) Baseline setzen (monatlich, einmal):
      - `${workspaceFolder}/.venv/Scripts/python.exe novapolis_agent/scripts/eval_drift_report.py --current novapolis_agent/eval/results/results_20260227_0231.jsonl --baseline novapolis_agent/eval/results/baselines/training_profiles.2026-02.json --out novapolis_agent/eval/results/drift/training_profiles_drift_2026-02-27.json --month 2026-02 --set-baseline`
    2) Vergleichslauf gegen Baseline:
      - `${workspaceFolder}/.venv/Scripts/python.exe novapolis_agent/scripts/eval_drift_report.py --current novapolis_agent/eval/results/results_20260227_0424_training_profiles_post_novapolis_signal.jsonl --baseline novapolis_agent/eval/results/baselines/training_profiles.2026-02.json --out novapolis_agent/eval/results/drift/training_profiles_drift_2026-02-27.json --month 2026-02`
- Schwellwerte (warn/blocker):
  - `warn_pass_drop=2.0`, `blocker_pass_drop=5.0` Prozentpunkte,
  - `warn_fail_increase=3`, `blocker_fail_increase=8` (pro Top-Failed-Check).
- Rueckkopplung ins Board:
  - `status=blocker` -> neuer/aktualisierter Punkt unter `Jetzt`,
  - `status=warning` -> unter `Als naechstes`,
  - `status=ok` -> Evidenz im DONELOG, kein Eskalationspunkt.

- [x] [Als naechstes] Trainingspaket-Gates und Baseline-Metriken fuer LoRA-Lauf festlegen.
  - Ziel: Nicht jedes erzeugte Paket soll trainiert werden; es braucht klare Freigabekriterien und Messpunkte vor/waehrend/nach dem Lauf.
  - Akzeptanzkriterien:
    1) Go/No-Go-Mindestwerte (Datensatzgroesse, Filterquote, Dupe-Rate) schriftlich fixiert,
    2) `fine_tune_pipeline.py`-Laufparameter fuer Baseline definiert,
    3) Ergebnisprotokoll (Dauer, Verlusttrend, Artefaktpfade) als Pflichtschema dokumentiert,
    4) ein Baseline-Run mit reproduzierbaren Parametern im DONELOG nachweisbar.
  - Evidenz: `novapolis_agent/scripts/fine_tune_pipeline.py`, `novapolis_agent/scripts/train_lora.py`, `outputs/lora-baseline-20260227_02/`, `novapolis_agent/docs/DONELOG.txt`.

LoRA-Go/No-Go und Baseline-Metriken (verbindlich, v1)
------------------------------------------------------

- Go/No-Go-Mindestwerte vor Trainingsfreigabe:
  - Datensatzgroesse: `>= 20` trainierbare JSONL-Records,
  - Filterquote: `>= 0.70` (PASS-Exports/Raw-Kandidaten),
  - Dupe-Rate: `<= 0.10` nach Dedupe (`dedupe_by_instruction=true`).
- Baseline-Entrypoint (`fine_tune_pipeline.py`) und Parameterprofil:
  - `--model sshleifer/tiny-gpt2`
  - `--per-device-train-batch-size 1`
  - `--epochs 1`
  - `--max-steps 1`
  - `--lr 0.0002`
  - `--no-check` (nur fuer reproduzierbaren Minimal-Baseline-Lauf)
- Ergebnisprotokoll (Pflichtschema je Run):
  1) `run_command` (vollstaendige CLI),
  2) `dataset_path` und `records_total`,
  3) `model`, Hyperparameter, Laufdauer,
  4) `train_loss` (letzter Wert) und `train_steps_per_second`,
  5) Artefaktpfad (`output_dir`) inkl. Adapter-/Tokenizer-Dateien.
- Reproduzierbarer Baseline-Run (nachweisbar):
  - `${workspaceFolder}/.venv/Scripts/python.exe novapolis_agent/scripts/fine_tune_pipeline.py --train-file novapolis_agent/eval/datasets/training/chronistin_operativ_kurz.v1.jsonl --model sshleifer/tiny-gpt2 --output outputs/lora-baseline-20260227_02 --per-device-train-batch-size 1 --epochs 1 --max-steps 1 --lr 0.0002 --no-check`
  - Ergebnis: `train_loss=10.4748`, `train_runtime=0.5054s`, Artefakte unter `outputs/lora-baseline-20260227_02/`.

- [x] [Als naechstes] VS Code Task-Set fuer Datensatzbau & Training vervollstaendigen.
  - Ziel: Die Kernschritte fuer Datensatzaufbau und Trainingsvorbereitung sollen ohne manuelle Kommandozusammenstellung ausfuehrbar sein.
  - Akzeptanzkriterien:
    1) neue Tasks fuer Kuratierung, Export+Pack und Baseline-Training angelegt,
    2) Tasks nutzen Root-`.venv` und konsistente CWD-Konfiguration,
    3) mindestens ein Task-Lauf pro neuer Gruppe dokumentiert,
    4) Board/README/Runbook referenzieren dieselben Task-Labels ohne Drift.
  - Evidenz: `.vscode/tasks.json` (Labels `Data: curate from latest (train pack)`, `Data: export+pack (latest results)`, `Train: baseline LoRA (tiny-gpt2, 1-step)`), `novapolis_agent/README.md` (Task-Labels Datensatz/Training), `novapolis_agent/docs/runbook.md` (Task-Labels Datensatz/Training), `novapolis_agent/docs/DONELOG.txt`.
  - Laufbelege (2026-02-27):
    1) Curate-CLI verifiziert: `python novapolis_agent/scripts/curate_dataset_from_latest.py --help` PASS.
    2) Export+Pack belegt: `export_finetune.py` gegen `results_20260226_0306_quality_de_round7b_repeat3.jsonl` (Export mit `0` Eintraegen wegen historischer Source-Path-Drift) und anschliessend `prepare_finetune_pack.py` auf vorhandenem Finetune-Export PASS (`train=90`, `val=10`, `total=100`).
    3) Baseline-Training PASS: `fine_tune_pipeline.py` mit `chronistin_operativ_kurz.v1.jsonl`, `sshleifer/tiny-gpt2`, `max_steps=1` -> `train_loss=10.4748`, Ausgabe `outputs/lora-baseline-vscode`.

Machbarkeits- und Architekturnotiz: Optionale Godot-UI fuer das Gesamtframework
---------------------------------------------------------------------------------

- Scope dieser Notiz: reine Architektur-/Machbarkeitsdokumentation, **kein** Implementierungsauftrag in diesem Schritt.
- Leitplanke: Training bleibt CLI-first (kanonische Entrypoints und Gates), eine UI ist nur optionale Huelle fuer Bedienung/Navigation.

Moegliches UI-Zielbild (optional)
---------------------------------

- Godot-Hauptmenue/Dashboard mit Navigationskacheln, z. B.:
  - `Chronistin von Novapolis` (Agent/Eval/Training-Status, Runs starten, Logs oeffnen),
  - `Novapolis` (Spielstart/Spielmodule),
  - `Profil` (benutzerbezogene Einstellungen),
  - `Datenverwaltung` (nur benutzer-/profilbezogene Datenverwaltung).
- Die UI orchestriert bestehende Skripte/Services, ersetzt sie aber nicht.

Integrationspunkte (CLI-first beibehalten)
------------------------------------------

- Prozess-Aufrufe: UI startet bestehende Python-Entrypoints (z. B. Eval/Kuration/Training) als Subprozesse mit nachvollziehbaren Parametern.
- Status/Artefakte: UI liest nur vorhandene Ergebnisse/Logs (`eval/results`, DONELOGs, Reports) und stellt sie dar.
- API-Anbindung: fuer Laufzeitfunktionen der Chronistin bleibt FastAPI (`novapolis_agent/app/main.py`) die technische SSOT.
- Task-Spiegelung: UI-Aktionen muessen auf bestehende Task-/CLI-Labels abbildbar sein, damit Headless-Betrieb und CI-Ablauf unveraendert bleiben.

Risiken und Guardrails
----------------------

- Drift-Risiko UI vs. CLI: doppelte Logik vermeiden; UI nur als Aufruf-/Anzeige-Schicht, keine eigene Fachlogik.
- Plattform-Risiko: Prozessstart/Path-Handling in Godot kann je OS abweichen; deshalb klare Wrapper-Vertraege und Fehlercodes benoetigt.
- Betriebsrisiko: lange Runs (Eval-Marathon/Training) brauchen robuste Abbruch-/Timeout-/Retry-Semantik, sonst UI-Haenger.
- Datenschutzgrenze: Bereich `Datenverwaltung` bleibt strikt auf Benutzer-/Profilbezug; keine Vermischung mit RP-SSOT oder systemweiten Betriebsdaten.
- Ressourcenrisiko: parallele UI+Training-Last kann lokale Systeme ueberlasten; Priorisierung/Queueing und Telemetrie sind vorzusehen.

Entscheidungsgrenze fuer Folgeplanung
-------------------------------------

- Go-Kriterium fuer eine spaetere Umsetzung: CLI-Workflows fuer Datensatzbau/Eval/Training sind stabil, dokumentiert und reproduzierbar.
- No-Go fuer verfruehte UI-Umsetzung: wenn dadurch Governance-Gates, Testbarkeit oder Headless-Betrieb verschlechtert werden.

TTS-Basisentscheidung (2026-02-22)
----------------------------------

- Exporter-Entrypoint bleibt `scripts/tts_coqui_export.py`.
- I/O-Vertrag fuer Build-Time-MVP:
  - Input: `--input <jsonl|yaml|txt>` + `--voice-map <yaml>` + `--lang de`.
  - Output: OGG-Dateien nach `novapolis-sim/assets/voiceovers/de/` mit stabilem Dateinamensschema und Hash-Cache.
- Scope heute: Spezifikation verbindlich; Implementierung/Tasks bleiben als offene Board-Punkte bestehen.

Archivierte Bloecke (Agent)
--------------------------
- Kurzfristige Ziele (Heute) - archiviert am 2025-11-01 19:16 -> `novapolis-dev/archive/todo.agent.archive.md`

Masterplan: KI-End-to-End in 10 grossen Schritten
--------------------------------------------------

1. [x] Laufzeitbasis stabilisieren: venv, editable install, reproduzierbarer Start (`run_server.py`/ASGI), klare Systemvoraussetzungen (Python, Ollama/Provider, Ports).
  Evidenz: `novapolis_agent/scripts/check_runtime_prereqs.py`, `novapolis_agent/tests/scripts/test_check_runtime_prereqs.py`, `novapolis_agent/run_server.py`.
2. [x] Konfigurationsvertrag fixieren: einheitliche ENV-Defaults in `app/core/settings.py`, Pflicht-/Optionalvariablen dokumentieren, sichere Fallbacks ohne Silent-Fail.
  Evidenz: `novapolis_agent/app/core/settings.py`, `novapolis_agent/tests/test_settings_parsing.py`, `novapolis_agent/README.md` (Abschnitt Konfigurationsvertrag).
3. [x] API-Vertragslage abschliessen: Chat + TTS-Endpunkte finalisieren (Schemas, Fehlercodes, Timeouts, Limits), OpenAPI als technische SSOT nutzen.
  Evidenz: `novapolis_agent/app/main.py` (responses + timeouts), `novapolis_agent/app/api/models.py` (`ApiErrorResponse`), `novapolis_agent/tests/test_openapi_contract.py`, `novapolis_agent/tests/test_tts_api_contract.py`.
4. [x] Auth + Zugriffsschutz aktivieren: minimal lokaler Schutz fuer sensible Endpunkte (Token/API-Key), klare 401/403-Semantik und testbare Ausnahmen.
  Evidenz: `novapolis_agent/app/main.py` (`_require_tts_auth`), `novapolis_agent/app/core/settings.py` (`TTS_AUTH_*`), `novapolis_agent/tests/test_tts_auth_contract.py`.
5. [x] Rate-Limit + Request-Grenzen harden: reproduzierbares Header-Verhalten, Schutz gegen Abuse, regressionsfrei fuer bestehende Chat-Flows.
  Evidenz: `novapolis_agent/app/main.py` (global+tts limiter), `novapolis_agent/app/core/settings.py` (`RATE_LIMIT_*`, `TTS_RATE_LIMIT_*`), `novapolis_agent/tests/test_tts_rate_limit_contract.py`, `novapolis_agent/tests/test_rate_limit_and_timeout.py`, `novapolis_agent/tests/test_input_length_and_rate_headers.py`.
6. [x] Cache- und Speicherstrategie einziehen: deterministische Key-Bildung, TTL/Size-Limits, Cleanup-Pfad, nachvollziehbare Hit/Miss-Telemetrie.
  Evidenz: `novapolis_agent/app/main.py` (`_tts_cache_key_from_payload`, `_tts_cache_cleanup_unlocked`, `/tts/cache/stats`, `/tts/cache/cleanup`), `novapolis_agent/app/core/settings.py` (`TTS_CACHE_TTL_SEC`, `TTS_CACHE_MAX_ENTRIES`, `TTS_CACHE_MAX_BYTES`), `novapolis_agent/tests/test_tts_cache_contract.py`.
7. [x] Provider-Abstraktion produktiv machen: Dummy/Null-Provider fuer Offline-Tests, danach Coqui-/Ollama-/OpenAI-Adapter hinter identischer Schnittstelle.
  Evidenz: `novapolis_agent/app/tts/providers.py`, `novapolis_agent/app/core/settings.py` (`TTS_PROVIDER`), `novapolis_agent/app/main.py` (abstrakte Provider-Verwendung), `novapolis_agent/tests/test_tts_provider_abstraction.py`.
8. [x] Testpyramide vollziehen: Unit + API + Streaming + Fehlerpfade + Contract-Tests, danach Marker-Laeufe in CI-identischem CWD-Modus.
  Evidenz: Markerlaeufe in `novapolis_agent`-CWD mit `.venv` erfolgreich (`pytest -q -m unit`, `pytest -q -m "api or streaming"`, `pytest -q -m scripts`) plus grüne Vertrags-/Fehlerpfad-Suites (`test_openapi_contract.py`, `test_app_chat_post_error.py`, `test_app_chat_stream_error.py`).
9. [x] Qualitaetsgates grün fahren: Reihenfolge Lint -> Typen -> Tests -> Coverage stabil auf >=80 %, bekannte Flakes beseitigen oder isolieren.
  Evidenz: `ruff check .` + `black --check .` grün, `pyright -p pyrightconfig.json` + `mypy --config-file mypy.ini app scripts` grün, `pytest -q` grün, `scripts/run_pytest_coverage.py --fail-under 80` Exitcode 0 (alles in CI-identischem `novapolis_agent`-CWD mit `.venv`).
10. [x] Betriebsfaehigkeit dokumentieren: README/Runbook/Tasks auf wahrheitsgetreuen Ist-Stand bringen (kein Claim ohne Evidenz), Postflight-Receipts und DONELOG sauber pflegen.
  Evidenz: `novapolis_agent/README.md` (Ist-Stand + Gate-Reihenfolge), `novapolis_agent/docs/runbook.md` (Betriebs-/Gate-Runbook), `.vscode/tasks.json` (`TTS: export (Coqui->OGG)` nutzt `tts_export_coqui.py --help`), `novapolis_agent/docs/DONELOG.txt` + `novapolis-dev/docs/donelog.md` (laufende Receipts/Logs).

Neue Aufgaben - Agent-Modul Analyse (2026-03-10)
-------------------------------------------------

- [x] [Jetzt] Runbook-Portabilitaet fuer Sim-Headless-Aufruf herstellen (kein hostgebundener Godot-Pfad im aktiven Runbook).
  - Ziel: Der Sim-Pruefschritt im Agent-Runbook muss auf unterschiedlichen Dev-Maschinen ohne lokale Pfadannahmen nutzbar sein.
  - Akzeptanzkriterien:
    1) `novapolis_agent/docs/runbook.md` verwendet nur portable Aufrufmuster (repo-relativ oder `${workspaceFolder}`),
    2) die vorhandene absolute Godot-Binärpfad-Referenz ist entfernt,
    3) ein Windows-Beispiel bleibt direkt ausfuehrbar und klar dokumentiert.
  - Evidenz: `novapolis_agent/docs/runbook.md` (portable `GODOT_BIN`/`godot4`-Variante ohne hostgebundene Pfade), `scripts/check_portable_paths.py`.

- [x] [Jetzt] Abhaengigkeitsprofil fuer optionale Agent-Tools formalisieren (Base/Dev/Train/Optional-CLI).
  - Ziel: Paketdrift vermeiden und reproduzierbare Installprofile fuer Betrieb, QA und Spezialskripte bereitstellen.
  - Akzeptanzkriterien:
    1) dokumentierte Profilmatrix (`runtime`, `dev`, `train`, `optional-tools`) mit klaren Paketzuordnungen,
    2) optional benoetigte Pakete (`openai`, `rich`, `pypdf`) sind explizit als optional markiert,
    3) ein leichter Validierungscheck warnt bei Importen ohne passende Deklaration.
  - Evidenz: `novapolis_agent/requirements/optional-tools.txt`, `novapolis_agent/scripts/check_dependency_profiles.py`, `novapolis_agent/tests/scripts/test_check_dependency_profiles.py`, `novapolis_agent/README.md`, `novapolis_agent/docs/runbook.md`.

- [x] [Als naechstes] Legacy-/Kompatibilitaetsschicht im Agent-Modul systematisch abbauen.
  - Ziel: Wartungskosten durch doppelte Legacy-Importpfade und Archiv-Shims kontrolliert reduzieren.
  - Akzeptanzkriterien:
    1) Inventarliste aller aktiven Legacy-Shims inkl. verbleibender Call-Sites,
    2) Migrationsplan in Etappen (Warnphase -> Umstellung -> Entfernung) mit Testabdeckung,
    3) mindestens ein Shim-Paket technisch entkoppelt, ohne Bestandsimporte ungeprueft zu brechen.
  - Evidenz: `novapolis_agent/docs/legacy-shim-inventory.md`, `novapolis_agent/scripts/check_legacy_shim_imports.py`, `novapolis_agent/tests/scripts/test_check_legacy_shim_imports.py`, `novapolis_agent/novapolis_agent/app/utils/examples/__init__.py`, `novapolis_agent/novapolis_agent/app/utils/examples/logging_example.py`, `novapolis_agent/novapolis_agent/app/utils/examples/summary_example.py`, `novapolis_agent/tests/test_module_exports.py`.

- [x] [Als naechstes] Test-Determinismus bei datenabhaengigen Smokes staerken.
  - Ziel: Smokes sollen in frischer Umgebung nicht wegen fehlender Vorartefakte skippen.
  - Akzeptanzkriterien:
    1) datenabhaengige Smokes erhalten reproduzierbare Testfixturen oder Testdaten-Builder,
    2) `pytest.skip` wegen fehlender Exportdateien wird durch deterministische Vorbereitung ersetzt,
    3) betroffene Skript-Smokes laufen im CI-aehnlichen Kontext ohne manuellen Vorlauf.
  - Evidenz: `novapolis_agent/tests/scripts/test_prepare_pack_smoke.py` (Temp-Fixture + direkter `prepare_pack`-Aufruf ohne `pytest.skip`), verifizierter Lauf `pytest -q novapolis_agent/tests/scripts/test_prepare_pack_smoke.py` PASS.

- [x] [Spaeter] Artefakt-Lifecycle fuer Eval/Training automatisieren (Retention + Dry-Run + Report).
  - Ziel: Laufende Eval-/Trainingsartefakte planbar bereinigen, ohne wichtige Referenzlaeufe zu verlieren.
  - Akzeptanzkriterien:
    1) ein Cleanup-Skript mit `--dry-run` und klaren Keep-Regeln (`latest N`, `named baselines`),
    2) Ausgabe als maschinenlesbarer Report (entfernt/behalten/gespart),
    3) VS-Code-Task fuer regelmaessige Ausfuehrung vorhanden.
  - Evidenz: `novapolis_agent/scripts/cleanup_artifacts.py`, `novapolis_agent/tests/scripts/test_cleanup_artifacts.py`, `.vscode/tasks.json` (Task `Data: artifacts cleanup (dry-run)`), Dry-Run-Report `.tmp/results/reports/artifact_lifecycle_report.json`.

- [x] [Spaeter] Eval-Marathon KPI-Rueckkopplung automatisieren (Board-/DONELOG-ready).
  - Ziel: Marathon-Laeufe sollen automatisch priorisierbare Follow-ups erzeugen statt rein manueller Sichtung.
  - Akzeptanzkriterien:
    1) Parser fuer `_meta.failed_checks`/Pass-Rate erstellt strukturierte KPI-Zusammenfassung,
    2) Schwellenmapping erzeugt Einstufung (`Blocker`/`Warnung`/`Beobachtung`),
    3) generierter Kurzreport ist direkt fuer Board-Update und DONELOG nutzbar.
  - Evidenz: `novapolis_agent/scripts/summarize_marathon_kpis.py`, `novapolis_agent/tests/scripts/test_summarize_marathon_kpis.py`, `.vscode/tasks.json` (Task `Eval: summarize marathon KPIs`), Reports `.tmp/results/reports/marathon_kpi_summary.json` und `.tmp/results/reports/marathon_kpi_summary.md`.

- [x] [Jetzt] RP->Eval-Builder und Synonym-Overlay-Ausbau implementieren.
  - Ziel: Aus RP-SSOT reproduzierbar Eval-Datensaetze erzeugen und Synonymerweiterungen domaeinenuebergreifend schichtbar machen (nicht nur RP).
  - Akzeptanzkriterien:
    1) neues Skript erzeugt Eval-JSONL aus `novapolis-rp/database-rp/**` mit stabilen IDs/Slugs/Tags,
    2) Synonym-Ladepfad beruecksichtigt zusaetzliches Overlay (`synonyms.additional.json`) neben Base/Local,
    3) VS-Code-Task und Unit-Tests decken Builder und Overlay-Verhalten ab.
  - Evidenz: `novapolis_agent/scripts/build_eval_from_rp.py`, `novapolis_agent/tests/scripts/test_build_eval_from_rp.py`, `novapolis_agent/eval/config/synonyms.additional.json`, `novapolis_agent/scripts/run_eval.py`, `novapolis_agent/tests/scripts/test_run_eval_term_helpers.py`, `.vscode/tasks.json` (Task `Data: build eval from RP (core)`), erzeugtes Paket `novapolis_agent/eval/datasets/rp/rp_ssot_core.v1.jsonl` (strict validator: `records=120, ids=120, slugs=120`).

- [x] [Jetzt] RP-Content-Eval-Profil nahtlos in Bestand integrieren.
  - Ziel: RP-Content soll als eigener operativer Eval-Pfad in Suite, Tasks, Validator und Runbook verankert sein.
  - Akzeptanzkriterien:
    1) neue Suite `rp_content` in `suites.json` mit RP-Datasetpaketen vorhanden,
    2) VS-Code-Task fuer `rp_content`-Lauf plus strict-Validator-Suite-Liste aktualisiert,
    3) Runbook- und Provenance-Doku enthalten den RP-Content-Pfad nachvollziehbar.
  - Evidenz: `novapolis_agent/eval/config/suites.json` (neue Suite `rp_content`), `.vscode/tasks.json` (Task `Eval: suite rp_content (20, asgi)` + strict-Validator inkl. `--suite rp_content`), `novapolis_agent/docs/runbook.md` (Task+CLI `rp_content`), `novapolis-dev/docs/dataset-provenance.md` (RP-Datasets ergaenzt), strict-Validator `--suite rp_content` PASS (`files=3, records=124, ids=124, slugs=124`).

