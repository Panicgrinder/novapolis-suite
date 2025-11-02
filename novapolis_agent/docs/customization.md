---
stand: 2025-11-02 23:36
update: YAML-Frontmatter ergänzt; Inhalt unverändert
checks: markdownlint-cli2 (docs focused) PASS
---

# Anpassung des Novapolis Agents

Diese Anleitung erklärt, wie Sie den Novapolis Agent ohne die üblichen Einschränkungen
von KI-Assistenten verwenden können. Sie haben volle Kontrolle über den Inhalt und
die Regeln, die in Ihrer privaten Installation des Agents gelten.

## Übersicht

Der Novapolis Agent wurde so konzipiert, dass Sie ihn vollständig an Ihre Bedürfnisse anpassen können.
Als privater Benutzer haben Sie die Möglichkeit, Einschränkungen zu entfernen und den
Agent genau so zu konfigurieren, wie Sie es für Ihre Zwecke benötigen.

## Verfügbare Modi

Der Novapolis Agent unterstützt drei verschiedene Modi:

1. **Standard-Modus**: Rollenspiel als Chronistin von Novapolis mit allgemeinen Inhalten
2. **Evaluierungs-Modus**: Sachliche Antworten ohne Rollenspiel (für Tests)
3. **Uneingeschränkter Modus**: Vollständig anpassbarer Modus ohne externe Filterung

## Anpassung des uneingeschränkten Modus

Um den Novapolis Agent ohne Einschränkungen zu verwenden, können Sie:

1. Den uneingeschränkten Prompt anpassen:

   ```bash
   python scripts/customize_prompts.py --customize-unrestricted
   ```

2. Eigene Regeln definieren:

   ```bash
   python scripts/customize_prompts.py --create-rules
   ```

3. Den uneingeschränkten Modus beim Aufruf aktivieren:

   ```bash
   curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{"messages":[{"role":"user","content":"Deine Anfrage"}],"unrestricted_mode":true}'
   ```

## Wichtige Dateien für die Anpassung

- `app/core/prompts.py`: Enthält alle System-Prompts
- `examples/unrestricted_prompt_example.txt`: Beispiel für einen uneingeschränkten Prompt

## Datenschutz und Verantwortung

Da der Novapolis Agent auf Ihrem lokalen System läuft und Ollama als Backend verwendet,
bleiben alle Ihre Anfragen und Anpassungen privat. Sie allein sind für die Art der
Inhalte verantwortlich, die Sie generieren.

Denken Sie daran, dass der uneingeschränkte Modus vollständig unter Ihrer Kontrolle steht.
Sie können den Systemprompt nach Ihren Vorstellungen gestalten, ohne die Einschränkungen,
die normalerweise bei öffentlichen KI-Diensten gelten würden.

## Beispiel für einen uneingeschränkten Prompt

In der Datei `examples/unrestricted_prompt_example.txt` finden Sie ein Beispiel für
einen uneingeschränkten Prompt, den Sie als Ausgangspunkt verwenden können.

## LLM‑Optionen (Sampling/Decoding) anpassen

Neben den Prompts können Sie auch die LLM‑Optionen (Sampling/Decoding) feinsteuern. Es gibt zwei Ebenen:

1) Globale Defaults per `.env` (Server‑Start lädt `app/core/settings.py` Werte aus ENV)
2) Pro‑Request‑Overrides in `ChatRequest.options` (überschreiben Defaults punktuell)

Unterstützte Optionen (Auszug):

- Temperatur/Sampling: `temperature`, `top_p`, `top_k`, `min_p`, `typical_p`, `tfs_z`
- Länge/Kontext: `num_predict` (Alias: `max_tokens`), `num_ctx`
- Penalties: `repeat_penalty`, `repeat_last_n`, `presence_penalty`, `frequency_penalty`, `penalize_newline`
- Steuerung/Seed: `seed`, `stop` (String oder Liste), `host` (Ollama‑Base‑URL)
- Mirostat: `mirostat` (0/1/2), `mirostat_tau`, `mirostat_eta`

### Globale Defaults per .env

Diese Werte setzen sinnvolle Standard‑Parameter, die bei fehlenden Request‑Overrides greifen.

```ini
# Sampling
TEMPERATURE=0.7
TOP_P=0.9
TOP_K=40
MIN_P=0.0
TYPICAL_P=1.0
TFS_Z=1.0

# Mirostat
MIROSTAT=0
MIROSTAT_TAU=5.0
MIROSTAT_ETA=0.1

# Penalties/Context
PENALIZE_NEWLINE=false
REPEAT_PENALTY=1.1
REPEAT_LAST_N=64
# Optionaler Kontext‑Default (wenn gesetzt, wird übernommen)
# NUM_CTX_DEFAULT=4096

# Länge & Sicherheit
REQUEST_MAX_TOKENS=512
```

Hinweise:
- `eval_mode` deckelt `temperature` automatisch auf maximal `0.25`.
- `stop` darf ein einzelner String oder eine Liste von Strings sein (intern zu Liste normalisiert).
- Werte werden konservativ geprüft/geklammert (z. B. `top_p|min_p|typical_p|tfs_z` in [0,1]; `mirostat` ∈ {0,1,2}).

### Pro‑Request Overrides (HTTP Beispiele)

curl (JSON):

```bash
curl -X POST http://127.0.0.1:8000/chat \
   -H "Content-Type: application/json" \
   -d '{
      "messages": [{"role":"user","content":"Schreibe zwei Sätze über Nova."}],
      "options": {
         "temperature": 0.4,
         "top_p": 0.8,
         "num_predict": 128,
         "stop": ["\n\n"],
         "mirostat": 2,
         "mirostat_tau": 5.0,
         "mirostat_eta": 0.1
      }
   }'
```

PowerShell (Invoke‑RestMethod):

```powershell
$body = @{
   messages = @(@{ role = "user"; content = "Erkläre typical_p kurz." })
   options  = @{ temperature = 0.3; typical_p = 0.9; top_k = 50; penalize_newline = $true }
} | ConvertTo-Json -Depth 4

Invoke-RestMethod -Uri "http://127.0.0.1:8000/chat" -Method Post -Body $body -ContentType "application/json"
```

Weitere Details und die vollständige Liste der Optionen finden Sie auch in der README unter
„LLM‑Optionen (Ollama) – Defaults & Overrides“.
