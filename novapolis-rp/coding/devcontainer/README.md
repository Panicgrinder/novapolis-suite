---
stand: 2025-11-06 15:22
update: MD003 Setext + YAML Frontmatter
checks: markdownlint-cli2 PASS (single file)
---

Devcontainer – Docs/Markdown Lint
=================================

Dieser Devcontainer bietet eine Node-Umgebung (Node 22) mit vorinstalliertem `markdownlint-cli2`.

Hinweise:

- Die Konfiguration liegt bewusst unter `coding/devcontainer/` (kein aktiver VS Code `.devcontainer/` am Repo-Root).
- Öffnen mit VS Code Dev Containers (Optional):
  1) Befehlspalette → "Dev Containers: Open Folder in Container..."
  2) Falls VS Code einen `.devcontainer` erwartet, diesen Ordner manuell auswählen oder die Datei temporär an den Root spiegeln.
- Alternativ steht eine VS Code Task bereit, die `markdownlint-cli2` in einem Docker-Container ohne lokalen Node-Install ausführt (siehe `.vscode/tasks.json`).

Vorinstalliert:

- `markdownlint-cli2`
- `markdownlint-cli2-formatter-default`

Konfiguration:

- Die Regeln werden aus `.markdownlint-cli2.jsonc` im Repo-Root gelesen.

