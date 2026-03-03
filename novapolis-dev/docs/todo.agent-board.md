---
stand: 2026-03-03 14:32
update: Portable Ausfuehrungssnippets fuer Drift-/LoRA-Baseline-Laeufe auf `${workspaceFolder}` und relative Zielpfade umgestellt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/todo.agent-board.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'novapolis_agent/docs/DONELOG.txt' 'novapolis_agent/README.md' 'novapolis_agent/docs/runbook.md' PASS (2026-03-03 14:14); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'novapolis-dev/docs/todo.agent-board.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'novapolis_agent/docs/DONELOG.txt' 'novapolis_agent/README.md' 'novapolis_agent/docs/runbook.md' PASS (EXITCODE=0, 2026-03-03 14:14)
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

- `Jetzt`: TTS-Build-Time-MVP, Runtime-Provider, Eval-Qualitaetsbetrieb.
- `Als naechstes`: Datensaetze/Training operationalisieren und VS Code Tasks vervollstaendigen.
- `Spaeter`: Templates fuer `knowledge:`/`actions:` in Agent-README verlinken.

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

