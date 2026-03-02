---
stand: 2026-03-02 22:24
update: Pfadbasierte Lizenzmatrix fuer Hybrid-Schutz eingefuehrt (Code MIT, Content/Data restriktiv getrennt).
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'README.md' 'LICENSES.md' 'CONTRIBUTING.md' 'TRADEMARKS.md' 'DONELOG.md' 'novapolis-rp/README.md' 'novapolis-dev/docs/donelog.md' PASS (2026-03-02 22:18); .\.venv\Scripts\python.exe scripts/check_frontmatter.py 'README.md' 'LICENSES.md' 'CONTRIBUTING.md' 'TRADEMARKS.md' 'DONELOG.md' 'novapolis-rp/README.md' 'novapolis-dev/docs/donelog.md' PASS (EXITCODE=0, 2026-03-02 22:18)
---
Lizenzmatrix
============

Zweck
-----

Diese Datei legt verbindlich fest, welche Lizenz fuer welche Pfade in diesem
Repository gilt.

Reihenfolge und Prioritaet
--------------------------

- Spezifischere, untergeordnete Lizenzdateien haben Vorrang vor allgemeineren.
- Wenn in einem Unterordner eine eigene Lizenzdatei liegt, gilt diese fuer
  diesen Unterbaum.
- Falls keine speziellere Regel vorhanden ist, gilt die Root-Lizenz `LICENSE`.

Pfad-zu-Lizenz Zuordnung
------------------------

- `LICENSE` (MIT): Software-Code im Repository, sofern nicht explizit
  abweichend lizenziert.
- `novapolis_agent/LICENSE` (MIT): Agent-Softwaremodul.
- `novapolis-rp/LICENSE` (NCDL v1.0): RP-Content, Lore- und Datenmaterial in
  `novapolis-rp/`.
- `novapolis_agent/eval/datasets/LICENSE.txt` (NCDL v1.0): Eval-/Trainings-
  Datensaetze in `novapolis_agent/eval/datasets/`.
- Vendor-/Drittanbieter-Lizenzen gelten unveraendert in ihren jeweiligen
  Unterpfaden (z. B. `novapolis_agent/docs/vendor_licenses/**`).

Marken
------

Namens- und Markenrechte sind nicht Teil der Open-Source-Codefreigabe. Siehe
`TRADEMARKS.md`.

Hinweis
-------

Diese Datei ist eine technische Lizenzzuordnung fuer den Arbeitsbetrieb im
Repository und ersetzt keine individuelle Rechtsberatung.
