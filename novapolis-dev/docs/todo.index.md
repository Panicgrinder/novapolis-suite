---
stand: 2026-04-07 21:38
update: Der TODO-Index fuehrt jetzt auch den zuvor separaten Typenrest in eval_utils und rag als geschlossen; alle Modul-Boards bleiben auf offen 0.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260407_213201.md
---

<!-- markdownlint-disable MD022 MD041 -->

TODO-Index (Novapolis-Dev)
==========================

Übersicht
---------

- RP-Module: `docs/todo.rp.md` — Aufgaben, Kanon-/Canvas-Arbeit, Logs (offen: 0)
- Dev-Module: `docs/todo.dev.md` — Tooling, Lint/CI, Validatoren, Doku-Infra (offen: 0)
- Agent-Module: `docs/todo.agent-board.md` — Backend (FastAPI/Ollama), Tests/Typing, Scripts (offen: 0)
- Sim-Module: `docs/todo.sim.md` — Godot/Visualisierung, API-Polling, Exportprofile (offen: 0)
- Root-Backlog: `todo.root.md` — suiteweiter Querschnitts-Backlog und Meta-Aufgaben (nicht Teil der Modul-Open-Counts oben)

Statushinweise (aktuell)
------------------------

- Agent v5.16: Der kanonische Agent-Typenlauf ist jetzt vollstaendig warnungsfrei. Nach dem Nachlauf in `novapolis_agent/utils/eval_utils.py` und `novapolis_agent/utils/rag.py` liefert `.tmp/results/reports/checks_types_20260407_205737.log` fuer `pyright -p pyrightconfig.json` jetzt `0 errors, 0 warnings`; `mypy --config-file mypy.ini app scripts` bleibt gruen. Der zuvor noch getrennte Restpfad ausserhalb des aktiven Produktpfads ist damit ebenfalls geschlossen.

- Agent v5.15: Die Pyright-Warnungen im aktiven Produktpfad sind eingeengt. `app/api/chat.py`, `app/api/sim.py`, `app/main.py` und `app/tts/providers.py` fuehren JSON-/Cache- und Session-Payloads jetzt ueber engere Coercion- bzw. TypedDict-Pfade; der erneute `pyright -p pyrightconfig.json` meldet im Produktpfad keine Warnungen mehr, `mypy --config-file mypy.ini app scripts` bleibt gruen, und der gezielte Pytest-Block fuer Chat, Sim und TTS ist PASS (`offen: 1 -> 0`).

- Agent v5.14: Der kanonische Agent-Typenlauf ist zwar wieder gruen, aber der aktive Produktpfad traegt noch konkrete Pyright-Warnungen. `.tmp/results/reports/checks_types_20260407_170654.log` meldet weiterhin `Unknown`-/teilweise unbekannte Payload-Typen in `app/api/chat.py`, `app/api/sim.py`, `app/main.py` und `app/tts/providers.py`; `novapolis-dev/docs/todo.agent-board.md` fuehrt diese Warnungswelle deshalb jetzt als offenen Folgepunkt (`offen: 0 -> 1`).

- Dev v5.15: Der kanonische Typenlauf ist wieder belastbar. `scripts/checks_types.py` bindet Pyright und Mypy jetzt explizit an `novapolis_agent/pyrightconfig.json` und `novapolis_agent/mypy.ini`, fuehrt beide Kommandos mit `cwd=novapolis_agent` aus, und `.vscode/tasks.json` startet denselben Wrapper wieder aus dem Repo-Root statt auf implizites CWD-Verhalten zu setzen. Der frische Typen-Postflight `.tmp/results/reports/checks_types_postflight_20260407_170654.md` zeigt `pyright=0` und `mypy=0`; der anschliessende Full-Check `.tmp/results/reports/checks_report_20260407_171142.md` ist komplett PASS (`offen: 1 -> 0`).

- Dev v5.14: Der kanonische Typenlauf ist aktuell kein belastbarer Gate-Pfad. `scripts/checks_types.py` ruft Pyright und Mypy vom Repo-Root aus mit `pyrightconfig.json` und `mypy.ini` auf, obwohl diese Konfigurationen nur unter `novapolis_agent/` existieren; `.vscode/tasks.json` startet zwar denselben Wrapper fuer `novapolis_agent`, aber der Wrapper ignoriert diesen Scope durch seine eigene Root-Aufloesung. Im Report `.tmp/results/reports/checks_types_20260407_165332.log` fallen deshalb bereits eine nicht lesbare Pyright-Config am Repo-Root und `Cannot find config file 'mypy.ini'` an, waehrend ein gezielter Mypy-Lauf auf den aktuellen Text-RPG-Slice PASS liefert. `novapolis-dev/docs/todo.dev.md` fuehrt die Reparatur deshalb wieder als offenen Infrastrukturpunkt (`offen: 0 -> 1`).

- Root v1.4: Der suiteweite Text-RPG-Produktpfad ist jetzt auf denselben belegten Slice reduziert. `todo.root.md` verweist fuer Startpunkt, Sessionvertrag, Produkt-Gate und Beta-Gates nur noch auf `rp-start-chooser.ssot.md`, `text-rpg-session-contract-v1.md`, `text-rpg-product-gate-v1.ssot.md`, `standalone-beta-gates.ssot.md` sowie die Modul-Boards; damit ist der Root-Metablock `Slice -> MVP -> Beta` nicht mehr offen, sondern auf die kanonischen Modul- und Gate-SSOTs verdichtet.

- RP v5.47: Der spaetere Live-Dialogpfad ist im Produkt-Iststand bereits nicht mehr nur Planung. `novapolis_agent/app/main.py` und `app/tts/providers.py` fuehren Live-TTS ueber den produktiven `coqui`-Provider mit Hash-Cache und sessionbezogenem Artefaktpfad `runtime/sessions/<session>/<channel>/...`; `novapolis-sim/scripts/Main.gd` konsumiert dieselben `tts_manifest`-Eintraege bereits fuer Live-Audio im Hub, und `novapolis-dev/docs/todo.rp.md` fuehrt den Punkt deshalb jetzt als geschlossen (`offen: 1 -> 0`).

- RP v5.46: Die ersten Build-Time-OGG-Kandidaten des Produktpfads sind jetzt nicht mehr nur ein offener Sammelpunkt. `novapolis-dev/docs/process/rp-ogg-summary-kandidaten-slot-00-30.ssot.md` markiert fuer `world` und `pc` die belastbaren Handover-, Kontakt- und Episodenkanten ueber `slot 00-30`, bleibt dabei am bestehenden Audio-Namensschema `epoch{dd}_slot{hh}_{channel}.ogg` und trennt diese Offline-Kandidaten bewusst vom spaeteren Live-Dialogpfad (`offen: 2 -> 1`).

- Agent v5.13: Der erste Text-RPG-Slice fuehrt jetzt denselben Sessionvertrag end-to-end durch Chat- und TTS-Lauf. `novapolis_agent/app/api/chat.py` injiziert den Session-Snapshot als internen Orchestrator-Block und schreibt `pc_log` plus geparste `state_patches` ueber `novapolis_agent/app/api/sim.py` in denselben Session-Store zurueck; `novapolis_agent/app/api/tts_models.py`, `novapolis_agent/app/main.py` und `novapolis_agent/app/tts/providers.py` heben denselben Session-/Slot-/Kanalrahmen in `/tts/synthesize`, Cache-Key, TTS-Manifest und sessionbezogenen Coqui-Artefaktpfad (`offen: 2 -> 0`).

- Agent v5.12: Die erste dedizierte Spielleiter-Regression laeuft jetzt nicht mehr nur ueber allgemeine RPG-Suiten, sondern als eigener Session-Gate. `novapolis_agent/eval/config/suites.json` fuehrt `gm_session`, `novapolis_agent/eval/datasets/rpg/rpg_gm_session_core.v1.jsonl` prueft Kontinuitaet, Reveal-Disziplin, Optionsqualitaet und Patch-Lesbarkeit, `novapolis_agent/scripts/run_eval.py` schreibt `slug/category/tags` reproduzierbar in die Resultatdateien, und `novapolis_agent/scripts/summarize_gm_eval_kpis.py` trennt Blocker-Faelle von Beobachtungen fuer Board-Triage (`offen: 3 -> 2`).

- Agent v5.10: Der Persistenz- und Replay-Folgepunkt ist jetzt als minimaler Session-Store im Sim-Modul geschlossen. `novapolis_agent/app/api/sim.py` schreibt pro Session `savegame.json`, `world_log.jsonl`, `pc_log.jsonl` und `replay_manifest.json`, liefert Resume-/Replay-Daten ueber `PUT /session/{session_id}`, `GET /session/{session_id}` und `GET /session/{session_id}/replay`, und `novapolis_agent/tests/test_api_sim_state.py` plus `tests/tests_sim_api.py` sichern Write-, Reload-, Manifest- und 404-Pfade ab (`offen: 4 -> 3`).

- Agent v5.11: Der Sessionvertrag materialisiert sich jetzt nicht mehr nur in SSOT und Sim-Artefakten, sondern auch im aktiven API-Rahmen. `novapolis_agent/app/api/models.py` fuehrt fuer `/chat` jetzt `contract_version`, Session-/Slot-Metadaten, `session_status`, `replay_checkpoint_id` und `log_channels`; `novapolis_agent/app/api/sim.py` validiert und persistiert denselben Rahmen in Savegame und Replay und normalisiert `state_patches` auf denselben Session-/Slot-/Tick-Kontext; `novapolis_agent/tests/test_models_chat_options.py`, `test_api_chat_internal_branches.py`, `test_api_sim_state.py`, `tests/tests_sim_api.py` und `test_openapi_contract.py` decken den Schnitt ab (`offen: 3 -> 3`).

- RP v5.45: Der Produktpfad fuehrt jetzt hinter dem episodischen Uebergabeanker eine modulare Anschlussstufe statt nur eines losen Folgehinweises. `novapolis-dev/docs/process/rp-folgekorridor-slot-26-30.ssot.md` fuehrt den erweiterten Korridor ueber D5/C6, `G7` und `E2/F1` bis `slot 30`; `rp-folgekorridor-slot-21-25.ssot.md`, `rp-text-rpg-startpaket-slot-00-05-2026-04-05.md` und `text-rpg-product-gate-v1.ssot.md` verweisen im selben Lauf auf denselben erweiterten Produktpfad (`offen: 2 -> 2`).

- Agent v5.8: Der Spielleiter-Orchestrator fuehrt Projektkontext jetzt nicht mehr nur als lose Nebenbloecke, sondern im selben kontrollierten Lauf. `novapolis_agent/app/api/models.py` fuehrt `retrieval_query`; `novapolis_agent/app/api/chat.py` faltet bei aktiviertem Orchestrator Kontextnotizen und RP-/Projekt-Retrieval in denselben Systemblock und laesst die getrennten `[Kontext-Notizen]`-/`[RAG]`-Bloecke in diesem Pfad bewusst weg; `novapolis_agent/tests/test_api_chat_internal_branches.py` deckt die gebuendelte Injektion ab (`offen: 4 -> 4`).

- Sim v5.3: Der bisher freie Hub-Chat zeigt jetzt einen ersten echten Sessionpfad statt nur lose Nachrichten. `novapolis-sim/scripts/Main.gd` sendet den Hub-Aufruf mit Sessionrahmen und Orchestrator-Hinweisen an `/chat`, haelt eine laufende Session-ID und bereitet Antworten als `Szene/Konsequenz/Optionen/State-Patches` im bestehenden Panel auf (`offen: 4 -> 4`).

- Sim v5.4: Die Replay-/Epoch-Bridge nutzt jetzt denselben Sessionvertrag wie der Live-Lauf. `novapolis-sim/scripts/Main.gd` zieht `world_log`, `pc_log`, `slot_id`, `slot_index`, Resume-Checkpoint und `artifact_paths` ueber `GET /session/{session_id}` vom Sim-API-Host nach, rendert denselben Stand in der vorhandenen Epochenansicht und markiert `tts_manifest` als live verfuegbaren Audiopfad statt nur `res://data/epochs` zu lesen (`offen: 4 -> 3`).

- Sim v5.5: Der Hub ist jetzt als minimaler Live-Spielclient des ersten Text-RPG-Slice geschlossen. `novapolis-sim/scripts/Main.gd` sendet die laufende Spielereingabe mit Sessionrahmen an `/chat`, zeigt Session, Slot/Scene, Szene, Konsequenz, Optionen, State-Patches und Protokoll direkt im Hub an und zieht den sichtbaren Stand anschliessend ueber `GET /session/{session_id}` aus demselben Sessionvertrag nach (`offen: 3 -> 2`).

- Sim v5.6: Der Sim-Offline-Check kennt jetzt eine explizite Profiltrennung statt Restwarnungen im Clean-Checkout. `scripts/check_sim_epoch_assets.py` wertet `--allow-empty` nun als kanonisches Clean-Checkout-Profil, der Lauf `--repo-root . --allow-empty --check-slot-consistency` endet im aktuellen Repo-Stand mit `summary=fail:0,warn:0`, und `novapolis-sim/README.md` dokumentiert die Bootstrap-Pfade `novapolis-sim/data/epochs/` und `novapolis-sim/assets/audio/` gegenueber dem Vollstand-Pfad (`offen: 2 -> 0`).

- Agent v5.7: Der offene Spielleiter-Orchestrator ist jetzt nicht mehr nur Konzept, sondern als erster Runtime-Hook im bestehenden Chat-Pfad angelegt. `novapolis_agent/app/api/models.py` fuehrt opt-in Felder fuer Sitzungsrahmen, `public_context`, `hidden_context`, Scheduler- und Patch-Hinweise; `novapolis_agent/app/api/chat.py` injiziert daraus einen kontrollierten Systemblock in `/chat` und `/chat/stream`, waehrend `novapolis_agent/tests/test_models_chat_options.py` und `novapolis_agent/tests/test_api_chat_internal_branches.py` den Hook absichern (`offen: 4 -> 4`).

- Agent v5.6: Die lokale Laufzeitbasis des ersten Slices ist jetzt nicht mehr nur `Ollama` als Runtime, sondern auch im Default-Modell festgezogen. `novapolis_agent/app/core/settings.py` und die Root-`.env.example` fuehren `qwen2.5:7b` jetzt als bevorzugtes Baseline-Modell fuer 8-GB-VRAM-Systeme; `novapolis_agent/README.md` und `novapolis_agent/docs/runbook.md` dokumentieren denselben Betriebsstandard (`offen: 4 -> 4`).

- RP v5.44: Der Produktpfad reicht jetzt hinter die erste Kampagnenstufe, ohne den Kanon ueber `E2/F1` hinaus frei auszudehnen. `novapolis-dev/docs/process/rp-folgekorridor-slot-21-25.ssot.md` fuehrt die naechste Kampagnenstufe ueber `E2`, `F1`, Rueckkopplung und episodischen Uebergabeanker; `rp-folgekorridor-slot-16-20.ssot.md` und `rp-text-rpg-startpaket-slot-00-05-2026-04-05.md` verweisen darauf (`offen: 2 -> 2`).

- Dev v5.22: Der technische Produkt-Gate-Pfad ist jetzt als verbindliche SSOT statt als loser Boardpunkt definiert. `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md` fuehrt den kanonischen Gate-Namen `Text-RPG Product Gate v1`, die Gate-Stufen und den aktuellen operativen Task-Block; `novapolis_agent/docs/runbook.md` fuehrt denselben Namen fuer den Betriebsweg (`offen: 1 -> 0`).

- Agent v5.5: Der Session- und Kampagnenvertrag des ersten Text-RPG-Slice ist jetzt als eigene SSOT festgezogen. `novapolis-dev/docs/specs/text-rpg-session-contract-v1.md` trennt Kampagne, Session, Szene, Slot, Zug, `state_patches` und Log-Kanaele verbindlich; `novapolis_agent/docs/runbook.md` fuehrt denselben Vertrag als operativen Referenzanker, waehrend Orchestrator, Persistenz und GM-Gates als verbleibende Implementierungswellen offen bleiben (`offen: 5 -> 4`).

- RP v5.43: Der Neutralpfad deckt jetzt auch `E2` und `F1` als eigenstaendige Starts ab, und der fruehere F1-Konflikt im C6-Kontext ist aktiv geradegezogen. `C6.md` fuehrt `F1` nun konsistent als realen T0-Knoten; `novapolis-rp/database-rp/03-locations/E2.md` und `F1.md` sowie `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-e2.ssot.md` und `rp-startbogen-freie-gruppen-f1.ssot.md` heben beide auf `full_slice` (`offen: 2 -> 2`).

- RP v5.42: Der fraktionslose Pfad dehnt sich jetzt in weitere aktive Neutralraeume aus. `novapolis-rp/database-rp/03-locations/C1.md` und `D1.md` geben zwei weiteren T0-Knoten konservative Ortsanker; `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-c1.ssot.md` und `rp-startbogen-freie-gruppen-d1.ssot.md` heben beide auf `full_slice`, und die Startgebiete-Reveal-Matrix fuehrt sie explizit mit (`offen: 2 -> 2`).

- RP v5.41: Der fraktionslose Pfad besitzt jetzt mehr als einen echten Start, und der Produktpfad reicht bis in eine erste Kampagnenfolge. `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-b1.ssot.md` und `rp-startbogen-freie-gruppen-c3.ssot.md` heben die neutralen Puffer `B1/C3` auf `full_slice`; `novapolis-dev/docs/process/rp-folgekorridor-slot-16-20.ssot.md` fuehrt die Folge hinter `slot 15` als Kampagnenast weiter (`offen: 2 -> 2`).

- RP v5.40: Der erste Langzeitast des Produktpfads ist jetzt kanonisch, und die ersten neutralen Pufferstationen sind keine reinen Codepunkte mehr. `novapolis-dev/docs/process/rp-folgekorridor-slot-11-15.ssot.md` fuehrt die Langzeitfolgen fuer Innen-, Aussen- und Pufferpfad; `novapolis-rp/database-rp/03-locations/A2.md`, `B1.md` und `C3.md` geben dem fraktionslosen Mobilitaetspfad konservative Ortsanker, die in A2-Startbogen und Startgebiete-Reveal-Matrix eingebunden sind (`offen: 2 -> 2`).

- RP v5.39: Die Reveal-Logik endet nicht mehr bei `D5/C6`, und der erste Mehrslot-Korridor laeuft jetzt belegt ueber `slot 05` hinaus. `novapolis-dev/docs/process/rp-startgebiete-reveal-matrix.ssot.md` fixiert die Sichtbarkeitsklassen fuer `A1/B2/H12/F9/K4/G7/A2`; `novapolis-dev/docs/process/rp-folgekorridor-slot-06-10.ssot.md` fuehrt Tunnel, Materiallauf, C6-Empfang und Aussenkontakt als kanonische Folge-Slots weiter (`offen: 2 -> 2`).

- RP v5.38: Der erste Mehrslot-Korridor ist jetzt kanonisch statt nur als Arbeitsfenster notiert, und die duennen Full-Slice-Kerne fuehren konservative lokale Unterraeume samt Nebenstart-Hooks. `novapolis-dev/docs/process/rp-folgekorridor-slot-00-05.ssot.md` fixiert die Slots `00-05` mit Missions-, Reveal- und Fail-Forward-Vertrag; `A1.md`, `H12.md`, `B2.md`, `F9.md`, `K4.md` sowie die Startboegen `A1/H12/B2/F9/K4/G7` binden Mind-Cluster, Unterraeume und Hook-Linsen explizit an (`offen: 3 -> 2`).

- RP v5.37: Der Mind-Cluster-Unterbau endet nicht mehr am ersten Novapolis-Kerncast. Neue `*-mind-cluster.md` fuer den direkten Anschlusscast `Arlen/Lumen/Marven/Marei/Lyra/Senn` sowie fuer die Full-Slice-Kerne `A1/B2/H12/F9/K4` schliessen die restliche Luecke zwischen Startboegen und beziehungsnaher SSOT; die zugehoerigen Charakterdateien verweisen jetzt auf die Cluster, und die veralteten Lueckenhinweise in `rp-startbogen-novapolis-d5.ssot.md` und `rp-startbogen-novapolis-c6.ssot.md` sind entfernt (`offen: 3 -> 3`).

- RP v5.36: Der erste Novapolis-Startkorridor besitzt jetzt den fehlenden verdeckten und operativen Unterbau. Neue Mind-Cluster-SSOTs fuer `Reflex/Jonas/Pahl/Kora/Echo`, startkorridor-taugliche `knowledge`-/`actions`-Bloecke in `D5.md`, `C6.md`, `Nordlinie-01.md` und den Kernfiguren sowie `rp-startkorridor-reveal-matrix.ssot.md` schliessen die drei Folgepunkte fuer Sphaeren, Scheduler-Readiness und Reveal-Grenzen in einem Lauf (`offen: 6 -> 3`).

- RP v5.35: Die restlichen belegten Fraktionskerne sind jetzt nicht mehr nur Auswahlrahmen. `novapolis-dev/docs/process/rp-startbogen-arkologie-a1.ssot.md`, `rp-startbogen-schienenbund-b2.ssot.md`, `rp-startbogen-eisenkonklave-h12.ssot.md`, `rp-startbogen-schattenbund-f9.ssot.md` und `rp-startbogen-fluesterkollektiv-k4.ssot.md` definieren fuer `A1/B2/H12/F9/K4` je einen konservativen Minimalstart; `rp-start-chooser.ssot.md` fuehrt damit alle derzeit freigegebenen Kernstationen als `full_slice` (`offen: 7 -> 6`).

- RP v5.34: Der erste Novapolis-Start ist jetzt kanonisch statt nur als Arbeitsblatt beschrieben. `novapolis-dev/docs/process/rp-startbogen-novapolis-d5.ssot.md` definiert den Default-Start in D5, `rp-startbogen-novapolis-c6.ssot.md` grenzt `C6` als parallelen Novapolis-Start ab, und `rp-start-chooser.ssot.md` fuehrt beide jetzt als `full_slice`. Das fruehere offene Startpaket ist damit geschlossen; als neuer Nachfolger bleibt die Promotion der restlichen Fraktionskerne `A1/B2/H12/F9/K4` offen (`offen: 7 -> 7`).

- RP v5.33: Der Produktpfad fuehrt jetzt einen echten Start-Chooser statt nur eine lose Mehrfachstart-Notiz. `novapolis-dev/docs/process/rp-start-chooser.ssot.md` trennt Startmodus, Gebietswahl, Dichtegrad und Reveal-Regeln; `rp-startbogen-freie-gruppen-a2.ssot.md` liefert den ersten fraktionslosen Neutralstart und `rp-startbogen-haendlerbund-g7.ssot.md` den ersten externen Fraktionsstart. Damit ist der Folgepunkt `Rahmenstart -> echter Startbogen` fuer mindestens einen externen und einen fraktionslosen Start geschlossen (`offen: 8 -> 7`).

- RP v5.32: Das Startmodell fuehrt jetzt mehrere Startoptionen statt nur eines Default-Slices. `novapolis-dev/docs/process/rp-text-rpg-startpaket-slot-00-05-2026-04-05.md` trennt nun `Novapolis-Default`, `Fraktionsstart`, `Fraktionslos / Freie Gruppen` und `Neutralstart`, bindet freie Gebietswahl an `Fraktionen-Taxonomie.md`, `Stationskontroll-Matrix.md` und `Metrokarte-T0.md` und markiert externe Bereiche bewusst als `Rahmenstart`, solange lokale Startboegen noch fehlen (`offen: 7 -> 8`).

- RP v5.31: Startpaket und der erste Mehrslot-Korridor sind nicht mehr nur als offene Schlagworte notiert, sondern als Arbeitsblatt zerlegt. `novapolis-dev/docs/process/rp-text-rpg-startpaket-slot-00-05-2026-04-05.md` fuehrt jetzt Primärlinse `Ronja/Reflex in D5`, die parallele C6-Linse, Reveal-Grenzen, Fail-Forward-Klassen und die Arbeitsfenster `slot 00-05`; der RP-Open-Count blieb dabei zunaechst bewusst unveraendert (`offen: 7 -> 7`).

- Root v1.3: Der Produktpfad zum KI-geleiteten Text-RPG ist erstmals als suiteweite Folgearbeit sichtbar. `todo.root.md` verankert jetzt den vertikalen Slice `Spielerinput -> Spielleitung -> Weltmutation -> PC-Rueckmeldung -> Logs/Audio/UI`, trennt MVP/Beta/Product-Gates und haelt die Priorisierung `spielbarer Kern vor Weltbreite/Komfort` auf Root-Ebene fest (`offen: unveraendert`).

- Dev v5.21: Der fehlende technische Produkt-Gate-Pfad ist als eigener Dev-Punkt geoefnet. Statt nur Einzelchecks fuer Chat, Sim, TTS und Eval zu fahren, fuehrt `todo.dev.md` jetzt einen End-to-End-Lauf vom RP-Kontext ueber Agent-Session und State-/Log-Artefakte bis zur Sim-/Replay-Sicht als neue Dev-Folgearbeit (`offen: 0 -> 1`).

- Agent v5.4: Das Agent-Board fuehrt jetzt erstmals den eigentlichen Spielleiter-Produktpfad statt nur Chat/TTS/Eval-Einzelbausteinen. Neu verankert sind Session-/Kampagnenvertrag, Spielleiter-Orchestrierung, persistenter Weltzustand mit `world_log`/`pc_log`/Replay, eine eigene GM-Eval-Suite und die spaetere Session-TTS-Kopplung (`offen: 0 -> 5`).

- RP v5.30: Das RP-Board fuehrt jetzt den inhaltlichen Produktpfad fuer den ersten spielbaren Slice statt nur Restarbeit im Inventar-/TTS-Strang. Neu offen sind Startpaket, Sphaeren-/Mind-Cluster-Rollout fuer die Kernbesetzung, scheduler-ready Knowledge-/Actions-Abdeckung, Reveal-/Geheimhaltungsmatrix und ein fail-forward Mehrslot-Korridor `slot 00-05` (`offen: 2 -> 7`).

- Sim v5.2: Das Sim-Board fuehrt jetzt neben den bekannten Asset-Warnungen den fehlenden Produktpfad fuer Spieleroberflaeche und Replay. Neu offen sind ein Live-Spielclient fuer laufende Sessions sowie eine Replay-/Epoch-Bridge auf denselben Session-/Slot-Vertrag statt rein statischer `res://data/epochs`-Artefakte (`offen: 2 -> 4`).

- Root v1.2: Der letzte aktive Root-eval-Rest ist final geschlossen. Lokale Kontext-Notizen-Defaults, Eval-Standardpfade und die RAG-Fallbacks laufen jetzt ueber `novapolis_agent/eval/...`; der ehemalige Root-Ordner `eval/` liegt nachvollziehbar unter `novapolis-dev/archive/quarantine/root-cleanup-20260328_0501-root-eval-rest/eval`, ein nach den Abschluss-Checks erneut erzeugter lokaler Stub wurde zusaetzlich unter `novapolis-dev/archive/quarantine/root-cleanup-20260328_0632-root-eval-rest-postchecks/eval` abgelegt, und die Tree-Artefakte wurden danach erneut neu erzeugt (`offen: unveraendert`).

- Dev v5.21: Der aktive Stub-/Runbook-/Tool-Scope fuehrt jetzt unterscheidbare Dateinamen statt austauschbarer Unterordner-READMEs. Umbenannt wurden u. a. `docs/adr/adr-index.md`, `novapolis_agent/scripts/scripts-overview.md`, `novapolis_agent/eval/eval-overview.md`, `novapolis-dev/logs/logs-policy.md`, `novapolis-rp/coding/tools/validators/validator-suite.md` und `novapolis-rp/database-raw/99-exports/raw-export-policy.md`; aktive Querverweise sind im selben Lauf nachgezogen. Bewusst unveraendert blieben die kanonischen Root-/Modul-Einstiege sowie fachliche RP-Landingpages unter `novapolis-rp/database-rp/01-factions/**` (`offen: 1 -> 0`).

- Agent v5.3: Der historische Null-Export-Drift im Export-/Kurationspfad ist geschlossen. `export_finetune.py` liefert jetzt laute Diagnostik statt stiller `0`-Exports, `curate_dataset_from_latest.py` nimmt das neueste exportierbare Resultset statt blind des neuesten Dateinamens, und ein temp-basierter Real-Lauf erzeugte fuer `results_20260226_0306_quality_de_round7b_repeat3.jsonl` wieder `20` Export-Eintraege plus Pack-Split `18/2` (`offen: 1 -> 0`).

- Agent v5.2: Der Artefakt-Cleanup gruppiert Retention jetzt auf Run-/Artefaktgruppen-Ebene statt pro Datei. `outputs/` bleibt im Dry-Run als ganze Laufgruppen zusammen, und fuer `novapolis_agent/eval/results` werden nur noch ganze Cluster statt gemischter Dateireste markiert; als einziger offener Agent-Punkt bleibt damit wieder der Export-/Kurationspfad gegen historische Results-Drift (`offen: 1 -> 1`).

- Agent v5.1: Die Kontext-Notizen-Migration ist abgeschlossen. `CONTEXT_NOTES_PATHS`, `open_context_notes.py`, `README.md` und die Eval-/RAG-Defaults fuehren jetzt konsistent auf `novapolis_agent/eval/...`, womit das Agent-Board wieder nur den historischen Export-/Kurationspfad offen fuehrt (`offen: 2 -> 1`).

- Root v1.1: Der zweite kleine Root-Cleanup ist abgeschlossen. `extensions.installed.txt`, `extensions.status.txt` und `desktop.ini` liegen jetzt gesammelt unter `novapolis-dev/archive/quarantine/root-cleanup-20260328_0330-local-snapshots/`; die Root-Tree-Artefakte wurden direkt per Terminal regeneriert, weil die vorhandenen Shell-Tasks lokal weiter am bekannten `pwsh /d /c`-Fehlpfad scheitern (`offen: unveraendert`).

- Root v1.0: Der sichere Root-Cleanup ist vollzogen. `combined.json`, `lint.out`, `md003_scan.out`, `.tmp-datasets/` und `reports/` liegen jetzt gesammelt unter `novapolis-dev/archive/quarantine/root-cleanup-20260328_0238/`; aktive Shims und der noch referenzierte Hinweis `eval/config/context.local.md` blieben bewusst im Root-Scope (`offen: unveraendert`).

- Dev v5.20: Der dokumentierte Stil- und Konsistenzlauf ist abgeschlossen. Hochfrequenz-Dateien, aktive Dev-SSOTs und die ersten Modul-Runbooks fuehren jetzt denselben PASS-/PowerShell-/Root-Wrapper-Stil; im aktiven Scope blieben beim Restscan nur ignorierte Drittanbieter-READMEs unter `node_modules` ausserhalb des Arbeitsbereichs uebrig (`offen: 1 -> 0`).

- Dev v5.19: Der naechste Doku-Hygienelauf ist vor seinem Start als eigener Phasenplan dokumentiert. Hochfrequenz-Dateien gehen zuerst, danach aktive Dev- und Modul-Doku; Archive und Quarantaene bleiben bewusst ausserhalb des Sweep-Scope (`offen: 0 -> 1`).

- Index v2.2: `todo.root.md` steht jetzt explizit in der Uebersicht; weitere `todo*.md` unter `novapolis-dev/archive/**` und `novapolis-dev/archive/quarantine/**` bleiben historische bzw. quarantänisierte Nebenpfade und zaehlen nicht zum aktiven Backlog.

- Index v2.1: Neue Folgepunkte sind jetzt explizit verankert: RP wurde vom Sammelpunkt auf Transferkette/Delta-Struktur/Realabgleich aufgefaechert, Sim fuehrt die bekannten Asset-Warnungen erstmals als aktiven Punkt, Dev den sichtbaren Metadaten-Drift im Index selbst.

- RP v5.29: Skill-Mapping-V1 ist jetzt gegen reale RP-Pfade dokumentiert. `annotation-spec.md` fuehrt den Realabgleich fuer `Ronja/Reflex` im Materiallauf `D5 -> C6`, fuer `Pahl` als faktisches D5-Kommando und fuer `Kora/Echo` im C6-Schutz-/Logistikkontext; die Baselines bleiben konservativ, nur fuer `Pahl` ist ein szenengebundener Kontext-Lift `funk/wache +1` statt eines Rollenwechsels festgehalten (`offen: 3 -> 2`).

- RP v5.27: Der Schattenbund fuehrt jetzt erstmals einen belegten Relations- und Beschaffungsrahmen statt nur T0-Abschirmhuelle. `Relationslog-Schattenbund.md`, `Handelslog-Schattenbund.md`, `Missionslog-Schattenbund.md` und `Schattenbund-inventar.md` dokumentieren nun den konservativen Rahmen `Novapolis = unbekannt`, `Eisenkonklave = feindselig`, `Arkologie = verdeckt` samt verdeckter Kette `Jarek Voan -> Sera Nol -> Nyra Vehl`; Mengen, Routen und benannte Gegenparteien bleiben bewusst offen (`offen: 3 -> 3`).

- RP v5.28: Das Fluesterkollektiv fuehrt jetzt erstmals einen belegten Minimalrahmen jenseits der reinen T0-Huelle. `Relationslog-Fluesterkollektiv.md`, `Handelslog-Fluesterkollektiv.md`, `Missionslog-Fluesterkollektiv.md` und `Fluesterkollektiv-inventar.md` dokumentieren nun den konservativen Rahmen `Novapolis = unbekannt` samt indirekter Kette `Corin Mael -> Sera Kaal -> Iris Vey`; benannte Gegenparteien, Routen und Mengen bleiben bewusst offen (`offen: 3 -> 3`).

- RP v5.26: Arkologie-A1 fuehrt jetzt erstmals einen belegten Aussenrahmen statt nur T0-Versorgungshuelle. `Relationslog-Arkologie-A1.md`, `Handelslog-Arkologie-A1.md`, `Missionslog-Arkologie-A1.md` und `Arkologie-inventar.md` dokumentieren nun den konservativen Rahmen `Haendlerbund = beschraenkt`, `Eisenkonklave = umkaempft`, `Novapolis = unbekannt` samt Handels-, Sicherheits- und Biosicherheitskette `Nera Vossen -> Borin Khade -> Liora Navesh`; Mengen, Routen und Einzeldeals bleiben bewusst offen (`offen: 3 -> 3`).

- RP v5.25: Die Eisenkonklave fuehrt jetzt erstmals einen belegten Handelsanker statt nur Rohrahmen. `Missionslog-Eisenkonklave.md`, `Handelslog-Eisenkonklave.md` und `Eiserne-Enklave-inventar.md` dokumentieren nun den konservativen Rahmen `Haendlerbund = handel_gelegentlich` samt Freigabekette `Kaspar Dorn -> Yara Kest`; konkrete Dealmengen, Routen und Tauschlisten bleiben bewusst offen (`offen: 3 -> 3`).

- RP v5.24: Der Haendlerbund ist von der reinen Rahmenwert-Huelle auf einen belegten Aufbaupfad gezogen. `Missionslog-Haendlerbund.md`, `caravan-moves.md` und `Haendlerbund-inventar.md` fuehren jetzt `H-47`, `C6 als Handelsstuetzpunkt`, `G7 als externer Kontaktpunkt` und die ersten Austauschklassen `Energie/Reparaturen/Kommunikationszugang <-> Nahrungsmittel/Filter/Grundbedarfsgueter`; Mengen und Manifeste bleiben bewusst offen (`offen: 3 -> 3`).

- RP v5.23: Die externen Fraktionsinventare fuehren jetzt denselben konservativen `rahmenwert`-Stand wie Matrix, Arbeitsledger und `Warenueberblick-T0.md`. Arkologie-A1, Schienenbund, Haendlerbund, Eisenkonklave, Schattenbund und Fluesterkollektiv zeigen jetzt explizite T0-Rahmen, Herkunftslogik und dokumentierte `RAHMENWERT`-Logs statt leerer `tbd`-Huellen; neue Mengen wurden bewusst nicht gesetzt (`offen: 3 -> 3`).

- RP v5.22: Der offene Warenlauf ist jetzt konservativ geschlossen. `Missionslog-Novapolis.md`, `D5-inventar.md`, `C6-inventar.md` und `Novapolis-inventar.md` fuehren dieselbe belegte Prozessspur `Entnahme/Packen in D5 -> Abmeldung -> Transport mit ReflexAssist -> Eintreffen/Bestandsaufnahme/Empfang in C6`; parallel fuehrt `Novapolis-inventar.md` jetzt das geforderte Delta-/Bilanzformat mit Bedarfsblock statt generischer Sammelnotizen (`offen: 6 -> 3`).

- RP v5.21: Das operative Arbeitsledger fuer die finale Metro-Warenzuteilung ist jetzt als eigenes Arbeitsblatt angelegt. Die Matrix ist damit in `fix`, `rahmenwert` und `handentscheidung` mit sichtbaren Zielpfaden, Stationsbezug und Updatepfad fuer die Zielinventare ueberfuehrt; als offene RP-Reste bleiben Transferkette, Delta-/Bilanzformat und der spaetere Realabgleich (`offen: 7 -> 6`).

- RP v5.18: Der RAW-Rettungsstand vor manueller Verteilung ist jetzt explizit dokumentiert. Hart rettbar bleiben C6-Startsnapshot, D5-Teilanker, generische Transferpfade und einzelne Tagesdeltas; weich rettbar sind Rollen- und Prozesslogik. Aktuelle Fraktionssummen, Restbestaende und konkrete Verbrauchsreihen bleiben weiter Handarbeit.
- RP v5.19: Die operative Zuteilungsmatrix fuer die finale Metro-Warenverteilung liegt jetzt als eigenes Arbeitsblatt vor und ist im Recheck auf alle aktiven Fraktionen ausdifferenziert. Novapolis bleibt darin ausdruecklich getrennt, weil die aktive SSOT nur eine lokale Kernfraktion in frueher Aufbauphase belegt; die externen Fraktionen werden einzeln ueber ihre T0-Warenbilder und Inventarklassen gerahmt (`offen: 6 -> 6`).
- RP v5.20: Nach der fraktionsscharfen Matrix ist jetzt auch der direkte Folgepfad verankert: Die finale Handverteilung soll erst ueber ein explizites Arbeitsledger laufen, bevor D5/C6/Fraktionsinventare weitergezogen werden (`offen: 6 -> 7`).

- RP v5.17: Die C6-Zielseite hat jetzt einen semiformellen Logistikanker: `logistik_novapolis_v2` fuehrt `D5 -> C6 (Bauteile, Werkzeuge, Versorgungsgueter)` als aktive Fracht, `logistik_c6_v2` benennt Primaer-/Sekundaerlager in C6. Definierbar ist damit ein missionierter Versorgungslauf mit bestaetigtem Empfang und Weiterverteilung, nicht aber eine harte Lagerbuchung oder Inventarmenge.

- RP v5.16: C6-Zielseite fuer die Transferkette gegen RAW nachgeschaerft. Bestaetigt sind jetzt nicht nur `Ankunft/Bestandsaufnahme`, sondern auch ein expliziter Empfangsanker plus anschliessende Verteilung an die Baustellen; unbelegt bleiben aber weiter Schleusen-/Lagerbuchung, Charge und Quittungszeile im Inventarlog.

- RP v5.15: D5-Quellorte fuer die Transferkette gegen RAW nachgeschaerft. Bestaetigt sind jetzt ein physischer Quellort `Materiallager unter Bahnsteig` sowie Werkstatt-/Transportmodul-Kontext in D5; unbelegt bleiben aber weiter Entnahmezeile, Zielbuchung in Schleuse/Lagerhalle und Quittung.

- RP v5.14: Transferkette `D5 -> C6` erneut gegen Umfeld und RAW gegengeprueft. Bestaetigt sind jetzt der generische Frachtanker in `logistik_novapolis_v2` sowie der Prozessrahmen `Abmeldung in D5 -> Ankunft/Bestandsaufnahme in C6`; unbelegt bleiben aber weiter Entnahmezeile, Zielbuchung in Schleuse/Lagerhalle und Quittung.

- RP v5.13: Das RP-Board fuehrt jetzt die feste Promotionskette `Charakter -> Team/POI -> Station -> Fraktion -> Metro` sowie die Pflicht-Deltas `Transfer`, `Verbrauch`, `Handel`, `Bilanz`; der offene Backfill ist damit als Gesamtprozess statt als lose Inventarsammlung beschrieben.
- RP v5.10: Transfer- und Verbrauchskette fuer Novapolis gegen RAW, Staging, Logistik und Missionslog geprueft; belastbar sind Bilanz- und Frachtanker, aber nicht die Item-Kette `Entnahme -> Transport -> Ankunft -> Quittung`.
- RP v5.11: Die Guetermission `D5 -> C6` ist jetzt im aktiven Missionslog als Transferanker verankert; fuer harte Fraktionssummen fehlen aber weiter Mengen-, Zielbuchungs- und Quittungszeilen.
- RP v5.12: D5- und C6-Teilinventare fuehren denselben Materiallauf jetzt als lokale Review-Anker; der Gap ist standortscharf dokumentiert, aber weiter nicht quantifiziert.
- RP v5.9: D5-Startsnapshot aus `RAW-canvas-2025-10-16T12-00-00-000Z` nachgezogen; mit C6 liegen jetzt zwei lokale Fruehanker vor, aber noch keine harte Fraktionssumme.
- RP v5.8: C6-Startsnapshot mit exakten Stueckzahlen aus `inventar_c6_v2` und `logistik_c6_v2` nachgezogen; D5 und Fraktionssummen bleiben ohne Gegenbeleg bewusst offen.
- RP v5.7: Skill-Mapping-V1 im Spec um eine zweite Referenzreihe fuer `Pahl`, `Reflex`, `Lumen` und `Echo` erweitert; RP offen bleibt `3`.
- RP v5.6: Skill-Mapping-V1 fuer `reparieren`, `wache`, `funk` und `wahrnehmung` im Spec verankert; RP offen `5 -> 3`.
- RP v5.5: Material-Delta Tag 12->13 fuer Tunnelarbeiten nachgezogen; Verbrauch ist belegt, aber Rest- und Standortmengen bleiben bewusst offen.
- RP v5.4: Energie-Tagesabschluss Tag 12->13 fuer D5/C6/Novapolis aus Staging plus Logistik nachgezogen; absolute Zellstaende bleiben bewusst `tbd`.
- RP v5.3: Erster konservativer Inventar-Abgleich fuer D5/C6/Novapolis abgeschlossen; D5 fuehrt keine C6-Bestaende mehr als lokalen Bestand.
- RP v5.2: Eigentlicher Inventar-Abgleich fuer D5/C6/Novapolis gestartet; erster harter Driftpunkt ist die fruehere Vermischung von C6-Bestaenden im D5-Inventar.
- RP v5.1: Pilotpaket fuer D5/C6/Novapolis-Backfill vorbereitet; RP offen bleibt `5`, aber der Start-Scope ist jetzt konkret dokumentiert.
- Dev v5.9: KPI-Trendansicht fuer die Hygiene-Cadence angelegt; Dev offen `1 -> 0`.
- Dev v5.10: Snapshot-/Retry-Governance gegen den realen Hook-Iststand geschaerft und die betroffenen Python-Tasks von `shell` auf `process` umgestellt; der lokale `pwsh /d /c`-Fehlpfad ist fuer Coverage-, TODO-Index- und Logs-Checks entfernt.
- Dev v5.11: Governance erneut gegen Aktualitaet, Redundanz und operatives Verhalten geprueft. Neu im Board stehen jetzt: Headings-/Quellenstand der Kern-SSOT nachziehen, Regelduplikate in der Kern-Governance reduzieren, verbleibende Python-Tasks auf `process` pruefen und den Snapshot-Retry-Pfad operativ haerten.
- Dev v5.12: Kern-SSOT `.github/copilot-instructions.md` und `.github/copilot-instructions-headings.md` wieder auf denselben aktuellen Quellenstand gezogen; der erste Governance-Folgepunkt ist damit geschlossen (`offen: 4 -> 3`).
- Dev v5.13: Kern-Governance normativ gestrafft. TL;DR verweist nur noch auf Regel-IDs, die `Regel-ID-Landepunkte (Kern)` sind explizit als bindende Ebene markiert, und die Matrix ist jetzt nur noch Kurzreferenz (`offen: 3 -> 2`).
- Dev v5.14: Verbleibende Python-Workspace-Tasks in `.vscode/tasks.json` von `shell` auf `process` vereinheitlicht; bewusste Shell-Ausnahmen bleiben nur fuer `pwsh`-Aufrufe (`offen: 2 -> 1`).
- Dev v5.15: Snapshot-/Pre-Commit-Retry-Pfad operativ gehaertet. Das Snapshot-Gate laeuft in `scripts/pre_commit.py` jetzt erst nach markdownlint, Frontmatter und RP-Hard-Gates; der Dev-Governance-Block ist damit komplett geschlossen (`offen: 1 -> 0`).
- Dev v5.16: Review-Nachlauf behoben. `scripts/snapshot_gate.py` prueft Freshness jetzt fuer alle betroffenen Markdown-Dateien statt nur bei `stand:`-Diff, und `scripts/pre_commit.py` kommentiert markdownlint nicht mehr irrefuehrend als optional (`offen: 0 -> 0`).
- Dev v5.17: Die aktive Reader-Surface ist wieder als Folgepunkt offen. Root-/Dev-/Modul-READMEs fuehren teils noch Vor-Maerz-Receipts, Altpfade oder Vor-Single-Root-Onboarding und sollen auf den aktuellen PASS-/`.venv`-Stand gezogen werden (`offen: 0 -> 1`).
- Dev v5.18: Reader-Surface-Sync abgeschlossen. Root-/Dev-/Modul-READMEs und `WORKSPACE_INDEX.md` fuehren jetzt den aktuellen Single-Root-/PASS-Kontext ohne alte FAIL-Header, lokale `venv`-Altpfade oder Sibling-Verweise (`offen: 1 -> 0`).
- Agent v5.0: Der dokumentierte Export-/Pack-Standardpfad fuehrt noch einen historischen Null-Export-Fall mit Source-Path-Drift; als neuer Folgepunkt ist jetzt ein lauter Fail oder ein nichtleerer aktueller Export statt stiller `0`-Records verankert (`offen: 0 -> 1`).
- Dev v5.8: O11 geschlossen; externes Standalone-Beta-Installblatt fuer Dritte dokumentiert (`offen: 2 -> 1`).
- Dev v5.7: Community-/Maintainer-Paket umgesetzt (`SUPPORT.md`, `RELEASE.md`, `MAINTAINERS.md`, Root-Issue-/PR-Templates); Dev offen `3 -> 2`.
- Dev v5.6: ADR-Ordner aktiv genutzt; `ADR-0001` und `ADR-0002` als akzeptierte Governance-Entscheidungen aufgenommen (`offen: 4 -> 3`).
- Dev v5.5: Coverage-Sprint Richtung `91%` abgeschlossen und deutlich ueberschritten (`76.24% -> 93.69%`, `offen: 5 -> 4`).
- Dev v5.3: Coverage-Punkt 3 gestartet; 90%-Qualitaetsziel jetzt verbindlich in Dev-Tests/Abschlussprozess verankert.
- Dev v5.4: Punkt 1 (Full-Gate) geschlossen; Coverage-Welle 1 Richtung `91%` gestartet (`76.24% -> 80.45%`).
- Dev v5.2: Folgezyklus fuer Gate-Stabilisierung und modernes Doku-Basispaket gestartet (`offen: 0 -> 5`).
- Dev v5.1: Woechentliche Hygiene-Cadence mit KPI-Tracking verbindlich dokumentiert (`offen: 1 -> 0`).
- Sim v5.0: Sim-Board konsolidiert, verbleibende Mikrodrift geschlossen (`offen: 1 -> 0`).
- Sim v5.1: Der verbleibende Sim-Restpunkt ist jetzt in Problem und Folgepfad getrennt: neben der Warnungsentscheidung liegt ein eigener Bootstrap-Punkt fuer Clean-Checkout vs. Vollstand auf dem Board (`offen: 1 -> 2`).
- Index v2.0: Operative Anzeige erweitert um Board-Metadaten (letzte Aenderung, aeltester offener Punkt, Widerspruchscheck).

Board-Metadaten (automationsrelevant)
-------------------------------------

| Board | letzte Aenderung | aeltester offener Punkt | Widerspruch "keine offenen" |
| --- | --- | --- | --- |
| Dev (`docs/todo.dev.md`) | 2026-04-07 | keiner (offen: 0) | nein |
| RP (`docs/todo.rp.md`) | 2026-04-07 | keiner (offen: 0) | nein |
| Agent (`docs/todo.agent-board.md`) | 2026-04-07 | keiner (offen: 0) | nein |
| Sim (`docs/todo.sim.md`) | 2026-04-07 | keiner (offen: 0) | nein |


Hinweise (Index)
----------------

- Aktive TODO-Quellen sind `todo.root.md` plus die vier Modul-Boards in `novapolis-dev/docs/`; gleichnamige Dateien unter `novapolis-dev/archive/**` oder `novapolis-dev/archive/quarantine/**` sind Historie, Snapshots oder Arbeitsquarantäne.
- Vollständig erledigte Abschnitte (H2/H3, alle [x]) bitte manuell in `novapolis-dev/archive/todo.<modul>.archive.md` verschieben; unter der Abschnittsüberschrift `archived_at: YYYY-MM-DD HH:MM` ergänzen. Übersicht aller Archive: `novapolis-dev/archive/README.md`.
- Validierung bei Änderungen: markdownlint via `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc` und Frontmatter-Check via `scripts/check_frontmatter.py`.
- Automationscheck: `scripts/check_todo_index_sync.py` liefert zusaetzlich Metadaten zu letzter Board-Aenderung, aeltestem offenen Punkt und Widerspruchen.

Verweise
--------

- Root-Übersicht: `todo.root.md` (Kurzüberblick, Meta-Aufgaben, Links)
- DONELOG-Zentralstruktur: `novapolis-dev/archive/docs/donelogs/INDEX.md`





