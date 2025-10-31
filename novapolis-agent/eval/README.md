# Evaluierungswerkzeug für den Novapolis Agent

Dieses Verzeichnis enthält Tools und Daten zur Evaluierung des Novapolis Agents.

Struktur:

- `datasets/`: Eingabedateien für die Evaluierung (Prompts), z. B. `eval-*.json` oder `.jsonl`
- `config/`: Konfiguration (z. B. `synonyms.json` für Keyword-Prüfungen)
- `results/`: Ausgabedateien der Evaluierung (generiert, `results_*.jsonl`)

 Hinweis: Private, lokale Synonyme können in `config/synonyms.local.json` gepflegt werden (git-ignoriert). Diese werden automatisch mit `config/synonyms.json` gemerged. Eine Vorlage liegt als `config/synonyms.local.sample.json` bei.

## Profile & Synonyme

- Profile: `config/profiles.json` enthält vorkonfigurierte Lauf-Presets für die Evaluierung (Quiet/ASGI/Eval-Modus, Checks, Temperatur). Aktuell verfügbar:
  - `default`: allgemeine Defaults (eval_mode=true, quiet, ASGI)
  - `fast`: schneller Lauf mit reduzierten Checks (must_include, keywords_any)
  - `chai`: Beispielprofil mit zusätzlichem not_include-Check
  - `eval_conservative`: sehr konservativ für strenge Evaluierungen (niedrige Temperatur, alle relevanten Checks inkl. rpg_style)
  - `creative_balanced`: kreativer, ausgewogener Lauf (höhere Temperatur, eval_mode=false, Checks: keywords_any, regex)
  - `fast_low_latency`: schnelle, latenzoptimierte Runs (moderate Temperatur, wenige Checks; eval_mode=true)

  Diese Profile werden im Konsolen-UI (`scripts/eval_ui.py`) angeboten und setzen u. a. `--asgi`, `--eval-mode`, `--quiet` und die aktiven Checktypen. Modell/Host/Temperatur sowie Sampling-Optionen wie `top_p` und `num_predict` können pro Profil hinterlegt werden; zusätzlich lassen sich Werte zur Laufzeit per CLI-Flags in `scripts/run_eval.py` überschreiben.

- Synonyme: `config/synonyms.json` bildet Basis; `config/synonyms.local.json` (gitignored) wird automatisch darübergelegt (Merge). Beispiel: `config/synonyms.local.sample.json`.

Hinweis zu Policies mit Profilen:
- Beispielregeln pro Profil sind in `config/policy.sample.json` hinterlegt (z. B. spezifische `forbidden_terms` für `eval_conservative`). Diese werden gemerged (default → profiles[profile_id]) und greifen, wenn `POLICIES_ENABLED=true` gesetzt ist.

 Hinweis: Einige VS Code Tasks nutzen bereits Profil/Checks-Presets (z. B. „Eval: run (ASGI, quiet)“).

## Format der Datasets (JSON/JSONL)

```json
{
  "id": "eval-001",
  "messages": [
    {"role": "user", "content": "Stelle dich kurz vor."}
  ],
  "checks": {
    "must_include": ["Begriff1", "Begriff2", "Begriff3"]
  }
}
```

- `id`: Eindeutige ID des Testfalls
- `messages`: Liste von Nachrichten, die an den Chat-Endpunkt gesendet werden
- `checks`: Prüfbedingungen für die Antwort
  - `must_include`: Liste von Begriffen, die in der Antwort enthalten sein müssen