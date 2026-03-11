---
stand: 2026-03-11 04:52
update: SECURITY-Policy fuer Responsible Disclosure und Supportfenster angelegt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc SECURITY.md CODE_OF_CONDUCT.md CHANGELOG.md docs/adr/README.md PASS (2026-03-11 04:49); .\.venv\Scripts\python.exe scripts/check_frontmatter.py SECURITY.md CODE_OF_CONDUCT.md CHANGELOG.md docs/adr/README.md PASS (EXITCODE=0, 2026-03-11 04:49)
---

Security Policy
===============

Supported Scope
---------------

- Dieses Repository wird auf `main` aktiv gepflegt.
- Sicherheitsrelevante Fixes werden priorisiert behandelt.

Responsible Disclosure
----------------------

- Bitte keine Security-Luecken oeffentlich in Issues oder Discussions posten.
- Meldung per E-Mail an: `security@novapolis.local`.
- Betreff-Format: `SECURITY: <kurzer Titel>`.
- Erwarteter Mindestinhalt:
  - betroffener Pfad/Komponente
  - reproduzierbare Schritte
  - erwartetes vs. beobachtetes Verhalten
  - potenzielle Auswirkung
  - optional: Vorschlag fuer Mitigation

SLA (Zielwerte)
---------------

- Eingangsbestätigung: innerhalb von 3 Werktagen.
- Erste Triage-Rueckmeldung: innerhalb von 7 Werktagen.
- Koordinierte Offenlegung erst nach Freigabe durch Maintainer.

Safe Harbor
-----------

- Forschung in gutem Glauben wird nicht sanktioniert, sofern:
  - keine Daten exfiltriert oder veraendert werden,
  - keine Persistenz eingebracht wird,
  - keine Service-Verfuegbarkeit absichtlich gestoert wird.

Out of Scope
------------

- Social Engineering gegen Maintainer oder Dritte.
- DDoS/Lasttests gegen produktive Systeme ohne Freigabe.
- Findings in bereits archivierten, nicht-aktiven Artefakten ohne Auswirkung auf aktive Pfade.
