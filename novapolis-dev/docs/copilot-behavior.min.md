---
stand: 2025-11-01 09:36
update: Erste kompakte Min-Variante der Arbeitsregeln erstellt.
checks: keine
---

# Copilot/LLM – Arbeitsregeln (Min)

Ziel: Kompakte, LLM‑freundliche Kernregeln (≤ ~1k Tokens) für Always‑On/Custom‑Instructions.

- Sprache: Deutsch (Erklärungen, Beispiele, Fehlermeldungen).
- Sicherheit/Privacy: Keine Secrets; offline bevorzugen; keine externen Pfad-Kopien.
- Output: Prägnant, skimmbar; kurze Sätze/Bullets; nur nötige Überschriften.
- Minimal‑Delta: Kleine, transparente Diffs; relevante Dateien nennen.
- Doku‑Disziplin: Bei jeder Änderung Snapshot aktualisieren (YAML‑Frontmatter bevorzugt: `stand`, `update`, `checks`).
  - Fallback (ohne YAML): `Stand: YYYY-MM-DD HH:mm – <Kurznotiz>`; optional `Checks: <kurz>`.
- Tests/Typen (wenn Code): Nach Edit sequentiell ausführen; Status kurz notieren.
- STOP‑Gate: Vor Code‑schweren Aktionen Modus prüfen; ggf. Codex/General explizit wählen.
- Kontextökonomie: Always‑On kurz halten; lange Passagen on‑demand nachladen.
- Keine Shell‑Kommandos an Nutzer ausgeben (außer explizit gewünscht); in Tools/Tasks kapseln.
- DONELOG: Nicht‑triviale Arbeiten ins DONELOG; Format `YYYY-MM-DD HH:MM | Author | Kurzbeschreibung`.
- RP/RAW‑Regeln (falls zutreffend): Ungefilterte Exporte nur unter `database-raw/99-exports/`.

Hinweis zu Snapshots (YAML)

- Frontmatter‑Schlüssel: `stand` (YYYY-MM-DD HH:mm), `update` (1–2 Kurzpunkte), `checks` (kurz, z. B. „pytest -q PASS“).
- Bei fehlender YAML‑Unterstützung: Klartext‑Kopfzeile wie oben.

Provider‑Hinweise (kurz)

- Editor (Copilot): Diese Min‑Regeln genügen als Always‑On. Längere Policies/Guides selektiv zitieren.
- OpenAI (Custom Instructions): Diesen Min‑Text verwenden; bei Bedarf Abschnitte aus Vollversion nachladen.

Referenz

- Vollversion (Editor‑Kontext): `/.github/copilot-instructions.md` (mit Update‑Logistik & Details).
