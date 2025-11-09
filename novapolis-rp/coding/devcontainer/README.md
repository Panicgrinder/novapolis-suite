---
stand: 2025-11-07 06:45
update: Policy: markdownlint nur via npx --yes (keine Global-Installs)
checks: markdownlint-cli2 PASS (single file)
---

Devcontainer – Docs/Markdown Lint
=================================

Dieser Devcontainer bietet eine Node-Umgebung (Node 22). Markdownlint wird gemäß Policy ausschließlich via `npx --yes markdownlint-cli2` ausgeführt (keine globalen Installationen).

Hinweise:

- Die Konfiguration liegt bewusst unter `coding/devcontainer/` (kein aktiver VS Code `.devcontainer/` am Repo-Root).
- Öffnen mit VS Code Dev Containers (Optional):
  1) Befehlspalette → "Dev Containers: Open Folder in Container..."
  2) Falls VS Code einen `.devcontainer` erwartet, diesen Ordner manuell auswählen oder die Datei temporär an den Root spiegeln.
- Lint-Ausführung: Bitte ausschließlich via `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md'` (im Container-Terminal).

Vorinstalliert:

- VS Code Extension `markdownlint` (Editor-Hinweise); keine globalen CLI-Installationen.

Konfiguration:

- Die Regeln werden aus `.markdownlint-cli2.jsonc` im Repo-Root gelesen.

