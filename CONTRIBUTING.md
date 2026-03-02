---
stand: 2026-03-02 22:24
update: Beitragspfad mit DCO-Sign-off und Rechtezusicherung fuer gemischtes Lizenzmodell eingefuehrt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'README.md' 'LICENSES.md' 'CONTRIBUTING.md' 'TRADEMARKS.md' 'DONELOG.md' 'novapolis-rp/README.md' 'novapolis-dev/docs/donelog.md' PASS (2026-03-02 22:18); .\.venv\Scripts\python.exe scripts/check_frontmatter.py 'README.md' 'LICENSES.md' 'CONTRIBUTING.md' 'TRADEMARKS.md' 'DONELOG.md' 'novapolis-rp/README.md' 'novapolis-dev/docs/donelog.md' PASS (EXITCODE=0, 2026-03-02 22:18)
---
Contributing
============

Kurzfassung
-----------

- Nutze Pull Requests fuer Aenderungen.
- Signiere jeden Commit mit DCO (`Signed-off-by`).
- Reiche nur Inhalte ein, an denen du die noetigen Rechte besitzt.
- Beachte die Lizenzzuordnung in `LICENSES.md`.

DCO Sign-off (verpflichtend)
----------------------------

Fuehre Commits mit Sign-off aus:

```powershell
git commit -s -m "Kurze Aussage zum Change"
```

Das erzeugt automatisch eine `Signed-off-by:`-Zeile im Commit.

Rechtezusicherung
-----------------

Mit einem Beitrag bestaetigst du, dass:

- du den Beitrag selbst erstellt hast oder die noetigen Rechte besitzt,
- du den Beitrag unter den fuer den Zielpfad geltenden Lizenzbedingungen
  beisteuern darfst,
- keine vertraulichen Daten oder fremde geschuetzte Inhalte ohne Erlaubnis
  eingebracht werden.

Lizenzrouting fuer Beitraege
----------------------------

- Codebeitraege in MIT-Pfaden folgen MIT (`LICENSE`, `novapolis_agent/LICENSE`).
- Beitraege in `novapolis-rp/` folgen der dortigen Inhalts-/Datenlizenz.
- Beitraege in `novapolis_agent/eval/datasets/` folgen der dortigen
  Inhalts-/Datenlizenz.

Qualitaetsanforderungen
-----------------------

- Linting, Typchecks und Tests sollen lokal gruen sein.
- Dokumentationsaenderungen muessen mit den zugehoerigen TODO/DONELOG-Pfaden
  konsistent sein.
