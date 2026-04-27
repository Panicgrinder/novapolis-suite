---
stand: 2026-04-27 02:30
update: Novapolis fuehrt jetzt den unmittelbaren Nahraum T0 fuer D5, C6 und den D5-C6-Korridor konservativ aus.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_022916.md
slug: novapolis-nahraum-t0
category: canon
version: "0.1"
---

Novapolis - Nahraum T0
======================

Zweck
-----

- Dieser SSOT zieht den unmittelbaren Novapolis-Nahraum konservativ um `D5` nach.
- Er verdichtet die aktive Kernbasis, den teilaktiven Aussenposten `C6` und den aktiven D5-C6-Korridor, ohne E3 oder weitere Raeume vorzeitig in den Betriebsraum zu ziehen.

Scope
-----

- Kernbasis: [D5](../03-locations/D5.md)
- Aussenposten: [C6](../03-locations/C6.md)
- Arbeitskorridor: `D5 <-> C6`

Raumringe
---------

| Ring | Bereich | Lesart |
| --- | --- | --- |
| 0 | `D5` | aktiver Kern aus Basisbetrieb, Werkstatt, Kontrolle und Fraktionsleitung |
| 1 | `D5 <-> C6`, `C6` | aktiver Projekt- und Versorgungskorridor plus teilaktiver Aussenposten |

Ausbau- und Zustandsstatus
--------------------------

| Bereich | Kontrolle | Status | Zustandslesart | Funktionswert im Nahraum |
| --- | --- | --- | --- | --- |
| [D5](../03-locations/D5.md) | Novapolis | aktiv | stabilster Punkt des Fraktionsblocks | Hauptbasis, Kontrollraum, Werkstatt, Versorgung |
| `D5 <-> C6` | Novapolis, aber nur im Projekt- und Arbeitsmodus | aktiv | begehbar und bespielbar, aber nicht normalisiert | Nordlinie, Transfer, Rueckmeldung, Freigabe |
| [C6](../03-locations/C6.md) | Novapolis | teilaktiv | nutzbar, aber unter Sicherungs-, Monitoring- und Versorgungslast | Aussenposten, Staging, Monitoring, lokaler Schutz |

Korridore und Zonen
-------------------

### Kern `D5`

- `D5` ist der einzige belastbare Novapolis-Kern im unmittelbaren Nahraum.
- Hier liegen Leitung, Basisversorgung, Werkstatt und die dichteste soziale Stabilitaet der Fraktion.

### Arbeitskorridor `D5 <-> C6`

- Der Korridor bleibt aktiver Projekt- und Transferraum statt freie Normalverbindung.
- Nordlinie, Materiallauf und Sicherheitsfreigaben machen ihn funktional zentral und zugleich verletzlich.

### Aussenposten `C6`

- `C6` ist aktiv genug fuer Spiel- und Betriebslogik, aber nicht stabil genug fuer eine zweite Vollbasislesart.
- Genau diese Teilaktivitaet macht C6 zum groessten Druckspeicher der Fraktion.

Gefahren- und Druckachsen
-------------------------

| Achse | Bereich | Lesart | Schwere |
| --- | --- | --- | --- |
| Materialdruck | `D5 <-> C6` | Nordlinie und Transfer binden knappe Werkstatt- und Versorgungsposten | hoch |
| Versorgungslast | `C6` | 27 Personen, Evakuierungsfolge und Aussenpostenbetrieb ziehen Reservegueter schnell leer | hoch |
| Sicherheits- und Monitoringdruck | `C6` | Signale, Marker und Anomalieraum erzwingen Filterung statt freier Offenheit | hoch |
| E3-Risiko | Randlage hinter `C6` | wirkt als bestaetigter Risikomarker, aber nicht als aktiver Betriebsraum | mittel |

Verdeckte Orte (konservativ)
----------------------------

Hinweise

- Die folgenden Raumtypen sind Funktionslesarten und keine bereits belegten Unterraeume.

| Bereich | Wahrscheinlicher Raumtyp | Lesart | Guardrail |
| --- | --- | --- | --- |
| `D5` | werkstattnahe Nischen, Kontrollraumvorfelder, kleine Versorgungsraeume | Kernbetrieb und Leitung greifen eng ineinander | keine freie Basisarchitektur erfinden |
| `D5 <-> C6` | Trage-, Sicherungs- und Uebergabesegmente | Projektkorridor statt Routineweg | keine volle Tunnelnormalisierung behaupten |
| `C6` | Kernzonen, Sicherungsraeume, Stagingpunkte | Aussenpostenbetrieb unter Teilfreigabe | keine Vollsicherheit oder Vollkontrolle setzen |

Guardrails
----------

- `D5` bleibt der aktive Kern; `C6` begruendet keinen zweiten gleichwertigen Fraktionskern.
- Der Nahraum-SSOT ersetzt keine Ortsdatei, sondern ordnet die belegte D5-C6-Logik.
- Keine harten Mengen-, Markt- oder Ausbaugrade ueber die belegten D5/C6-Pfade hinaus ohne neue Evidenz.
