---
stand: 2025-11-14 16:55
update: Dokumentation zur Integration des Checks-Wrapper-Skripts `python scripts/run_checks_and_report.py` ergänzt.
checks: archiviert
---

Checks: full — Integration des zentralen Wrapper-Skripts
=====================================================

Kurz: Das zentrale Checks‑Wrapper-Skript `scripts/run_checks_and_report.py` führt Lint → Typen → Tests (mit Coverage) in der empfohlenen Reihenfolge aus und erzeugt Receipts unter `.tmp-results/reports/`.

Warum: Vereinheitlicht Prüfläufe, vereinfacht Receipt-/Postflight-Erzeugung und ersetzt die ältere PowerShell-Variante.

Wie lokal ausführen

```powershell
# im Repo-Root (Windows / pwsh)
& .\.venv\Scripts\python.exe -m pip install --upgrade pip setuptools
& .\.venv\Scripts\python.exe scripts\run_checks_and_report.py
```

Ergebnisse & Receipts

- Receipt-Dateien werden unter `.tmp-results/reports/checks_report_<ts>.md` geschrieben.
- Bei Fehlern erstellt der Wrapper strukturierte Exit-Codes und einen Postflight-Meta-Block (siehe Receipt-Ende).

Policy / Hinweise

- Wrapper-Policy: Mehrschrittige Prüfläufe sollen über `pwsh -File` oder das zentrale Python-Skript ausgeführt werden. Inline `-Command`-Ketten sind zu vermeiden.
- STOP-Gate: Bei Zweifeln oder möglichen destruktiven Aktionen (z. B. Cleanup) immer STOP und Rückfrage vor Mutationen.
- Frontmatter: Nach Änderungen an Dokumenten `stand`, `update`, `checks` synchronisieren; Receipt-Referenzen in `WORKSPACE_STATUS.md`/`DONELOG.md` verlinken.

Weitere Infos

- Receipt-Beispiele: `.tmp-results/reports/checks_report_20251114_162424.md`
- Related files: `.github/copilot-instructions.md`, `WORKSPACE_STATUS.md`, `DONELOG.md`, `todo.root.md`.
