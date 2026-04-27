---
stand: 2026-04-27 02:30
update: Haendlerbund fuehrt jetzt ein konservatives Betriebsmodell T0 fuer G7 als externe Zentrale und C6 als eingebettete Niederlassung.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_022916.md
slug: haendlerbund-betriebsmodell-t0
category: canon
version: "0.1"
---

Haendlerbund - Betriebsmodell T0
================================

Zweck
-----

- Dieser SSOT zieht fuer den Haendlerbund ein konservatives Betriebsmodell T0 nach.
- Er verdichtet `G7` als externe Zentrale und `C6` als belegte eingebettete Niederlassung, ohne daraus ein flaechiges Stationsnetz mit festen Vollbasen zu machen.

Guardrails
----------

- Der Haendlerbund bleibt ein mobiler Handels- und Versorgungsblock.
- `G7` ist der belastbare Eigenkern; `C6` ist der belastbare Partner- und Niederlassungsanker im Novapolis-Raum.
- Weitere Niederlassungen, Manifeste, Vorratsmengen und feste Konvoistaerken bleiben ohne neue Belegkette offen.

Kernlesart T0
-------------

| Bereich | Status | Funktionsprofil | Lesart |
| --- | --- | --- | --- |
| [G7](../03-locations/G7.md) | aktiv | Leitstelle, Handels- und Routenleitstand, Sicherheitsfreigabe | aktive externe Zentrale des Haendlerbunds |
| [C6](../../novapolis/03-locations/C6.md) | aktiv, aber eingebettet | Handelsstuetzpunkt, Uebergabe- und Niederlassungsfenster unter Novapolis-Rahmen | belegte eingebettete Niederlassung |
| `G7 <-> C6` | aktiver Korridor | Konvoilogik, Deal-Fenster und Versorgungsabgleich | primaerer Aussen- und Niederlassungspfad |

Leitungs- und Freigabekette
---------------------------

- Mara Quell fuehrt Ziele, Freigaben und Krisenentscheidungen aus `G7`.
- Tovin Rek steuert Handelsfenster, Lieferprioritaeten und Routenplanung.
- Runa Fehr bindet Bewegung, Begleitschutz und Transit an Sicherheits- und Risikoampeln.
- H-47 fuehrt den belegten Partnerpfad in `C6`, ohne `G7` als Eigenkern zu ersetzen.

Betriebsprioritaeten
--------------------

| Prioritaet | Lesart | Guardrail |
| --- | --- | --- |
| Versorgungskontinuitaet | Umlauf und Reserve muessen zwischen Zentrale und Niederlassung tragfaehig bleiben | keine freien Vollbestandsketten behaupten |
| Verhandlungsfaehigkeit | Austausch lebt von belastbaren Deal-Fenstern statt offenen Maerkten | keine pauschale Fraktionsintegration setzen |
| Sicherheitsfreigabe | jede Bewegung koppelt Handel an Schutz, Begleitschutz und Rueckzugsoptionen | keine route ohne Risiko- und Freigabelogik |
| Flexibilitaet | Niederlassungen sind Partnerfenster, nicht zweite unabhaengige Reiche | keine weiteren Basen ohne Evidenz |

Spielbare Konfliktlinien
------------------------

- Zentrale gegen Niederlassung: `G7` fuehrt, aber `C6` bestimmt, wie tief der Haendlerbund real im Novapolis-Raum verankert ist.
- Versorgung gegen Vorsicht: Mehr Umlauf erzeugt mehr Chancen, aber auch mehr Sicherheitsbedarf.
- Deal-Fenster gegen Abhaengigkeit: Erfolgreiche Kooperation staerkt `C6`, kann aber `G7` politisch enger an Partnerlogiken binden.
- Mobilitaet gegen Verfestigung: Der Haendlerbund braucht Zentrale und Niederlassungen, darf aber nicht in starre Stationaerlogik kippen.

Alltagslesart fuer Spiel und Szenen
----------------------------------

- `G7` wirkt als schmale, aktive Kommando- und Handelszentrale statt als offener Basar.
- `C6` ist fuer den Haendlerbund kein zweites Mutterhaus, sondern ein eingebettetes Deal- und Versorgungsfenster.
- Handel ist im Haendlerbund immer an Route, Rueckzug und Freigabe gekoppelt.

Verknuepfte Quellen
-------------------

- [Haendlerbund](../Haendlerbund.md)
- [G7](../03-locations/G7.md)
- [Haendlerbund-inventar](../04-inventory/Haendlerbund-inventar.md)
- [haendlerbund-nahraum-t0](./haendlerbund-nahraum-t0.md)
- [rp-startbogen-haendlerbund-g7](../../../../../novapolis-dev/docs/process/rp-startbogen-haendlerbund-g7.ssot.md)
