---
stand: 2026-04-27 02:30
update: Haendlerbund fuehrt jetzt den unmittelbaren Nahraum T0 fuer G7 und den Korridor G7-C6 konservativ aus.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_022916.md
slug: haendlerbund-nahraum-t0
category: canon
version: "0.1"
---

Haendlerbund - Nahraum T0
=========================

Zweck
-----

- Dieser SSOT zieht den unmittelbaren Haendlerbund-Nahraum konservativ um `G7` nach.
- Er verdichtet die externe Zentrale, die belegte Niederlassung in `C6` und den primaeren Korridor dazwischen, ohne weitere Niederlassungen oder Handelsbasen zu erfinden.

Scope
-----

- Kernknoten: [G7](../03-locations/G7.md)
- eingebettete Niederlassung: [C6](../../novapolis/03-locations/C6.md)
- Arbeitskorridor: `G7 <-> C6`

Raumringe
---------

| Ring | Bereich | Lesart |
| --- | --- | --- |
| 0 | `G7` | aktive externe Zentrale aus Leitstelle, Handels- und Routenleitstand und Sicherheitsfreigabe |
| 1 | `G7 <-> C6`, `C6` | aktiver Deal-, Uebergabe- und Niederlassungsraum unter Partnerrahmen |

Ausbau- und Zustandsstatus
--------------------------

| Bereich | Kontrolle | Status | Zustandslesart | Funktionswert im Nahraum |
| --- | --- | --- | --- | --- |
| [G7](../03-locations/G7.md) | Haendlerbund | aktiv | stabilster Punkt des Fraktionsblocks | Leitstelle, Sicherheits- und Handelskern |
| [C6](../../novapolis/03-locations/C6.md) | Novapolis mit Haendlerbund-Niederlassung | aktiv | eingebetteter Partnerraum, nicht Vollkern des Haendlerbunds | Handelsstuetzpunkt, Uebergabe, Versorgung |
| `G7 <-> C6` | aktiver Korridor unter Freigabe | aktiv | Route, Deal-Fenster und Rueckzugsachse | Konvoi-, Austausch- und Risikoachse |

Korridore und Zonen
-------------------

### Kern `G7`

- `G7` ist der einzige belastbare Eigenkern des Haendlerbunds im unmittelbaren Nahraum.
- Leitstelle, Handelsplanung und Sicherheitsfreigabe liegen hier dichter beieinander als in einer offenen Marktstation.

### Niederlassungsfenster `C6`

- `C6` bleibt belegter Handelsstuetzpunkt und die wichtigste eingebettete Niederlassung des Haendlerbunds.
- Gerade die Einbettung unter Novapolis-Rahmen macht `C6` strategisch wertvoll, aber nicht zu einer zweiten Haendlerbund-Zentrale.

### Korridor `G7 <-> C6`

- Der Korridor ist Deal-, Konvoi- und Rueckzugsraum zugleich.
- Jede Bewegung koppelt Handelschancen an Verhandlungslage, Sicherheitsampeln und Partnervertrauen.

Gefahren- und Druckachsen
-------------------------

| Achse | Bereich | Lesart | Schwere |
| --- | --- | --- | --- |
| Konvoirisiko | `G7 <-> C6` | Versorgung und Handel bleiben an sichere Umlaeufe gebunden | hoch |
| Abhaengigkeitsdruck | `C6` | ein zu starker Fokus auf die Niederlassung kann `G7` politisch einengen | mittel bis hoch |
| Sicherheitsdruck | `G7` | Transit, Zutritt und Schutz von Ladung ziehen an denselben knappen Freigaben | hoch |
| Versorgungsfenster | Gesamtbild | Handel muss tragfaehig bleiben, ohne Bestandsphantasien zu erzeugen | mittel |

Verdeckte Orte (konservativ)
----------------------------

Hinweise

- Die folgenden Raumtypen sind Funktionslesarten und keine bereits belegten Unterraeume.

| Bereich | Wahrscheinlicher Raumtyp | Lesart | Guardrail |
| --- | --- | --- | --- |
| `G7` | Leitnischen, Routenbriefingpunkte, gesicherte Umschlagraeume | Fuehrung, Handel und Sicherheit greifen eng ineinander | keine konkrete Innenarchitektur erfinden |
| `C6` | Uebergabezonen, Lagerfenster unter Partneraufsicht, Dealraeume | eingebettete Niederlassung statt Vollbasis | keine Haendlerbund-Kontrolle ueber ganz C6 behaupten |
| `G7 <-> C6` | Zwischenuebergaben, Rueckzugsfenster, abgestimmte Konvoisegmente | aktiver Arbeitskorridor statt freie Hauptstrasse | keine weiteren Basen oder Routen setzen |

Guardrails
----------

- `G7` bleibt der aktive Kern; `C6` bleibt eine eingebettete Niederlassung und begruendet keinen zweiten Eigenkern.
- Der Nahraum-SSOT ersetzt keine Ortsdatei, sondern ordnet die belegte Zentralen- und Niederlassungslogik.
- Keine harten Manifest-, Mengen- oder Partnerlisten ohne neue Evidenz.
