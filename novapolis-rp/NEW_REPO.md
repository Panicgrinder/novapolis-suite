# NEW_REPO – Schnellstart für ein neues Novapolis‑RP Repository

Zweck: Vorlage/Anleitung, um ein eigenständiges Git‑Repository für Novapolis‑RP anzulegen und zu initialisieren.

Schnellstart (lokal → GitHub):

1) Neues Verzeichnis anlegen und initialisieren:

```powershell
mkdir Novapolis-RP; cd Novapolis-RP
git init
```

2) Dateien hinzufügen (Beispielkopie):

```powershell
# Kopiere vorhandene Projektdateien in dieses Verzeichnis oder erstelle neue
# Beispiel: kopiere den Inhalt von F:\Novapolis-RP in das neue Repo (lokal)
# Robuste Kopieroptionen können robocopy verwenden
robocopy "F:\Novapolis-RP" "." /E /NFL /NDL /NJH /NJS /nc
```

3) Committen und initialen Branch setzen:

```powershell
git add .
git commit -m "Initial import Novapolis-RP"
git branch -M main
```

4) Remote anlegen und push (ersetze `<GIT_URL>`):

```powershell
git remote add origin <GIT_URL>
git push -u origin main
```

Hinweise:
- Wenn du kein Remote anlegen möchtest, kannst du das Repo lokal betreiben.
- Wenn du möchtest, kann ich das Remote‑Setup vorbereiten (README, .gitignore, LICENSE). Sag mir nur: "erstelle README/.gitignore/LICENSE" oder gib die Ziel‑URL an.

Empfohlene Ergänzungen vor dem Push:
- `README.md` (Projektbeschreibung)
- `.gitignore` (z. B. für `.venv`, `__pycache__`, `*.pyc`)
- `LICENSE` (falls Open‑Source gewünscht)
- `novapolis-dev/docs/donelog.md` und `novapolis-dev/docs/todo.md` für laufende Dokumentation

---

Wenn du bereit bist, kann ich zusätzlich eine `README.md` und `.gitignore` anlegen und lokale Dateien direkt committen (ohne Remote). Soll ich das tun?
