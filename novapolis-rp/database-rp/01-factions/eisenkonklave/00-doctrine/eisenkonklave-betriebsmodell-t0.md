---
stand: 2026-04-27 02:30
update: Eisenkonklave fuehrt jetzt ein konservatives Betriebsmodell T0 fuer H12, Freigabekette und Schadenskorridor.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_022916.md
slug: eisenkonklave-betriebsmodell-t0
category: canon
version: "0.1"
---

Eisenkonklave - Betriebsmodell T0
=================================

Zweck
-----

- Dieser SSOT zieht fuer die Eisenkonklave ein konservatives Betriebsmodell T0 nach.
- Er verdichtet den aktiven Kernknoten `H12` und den beschaedigten Zulauf `H3 -> H12`, ohne daraus ein flaechiges Stationsreich zu machen.

Guardrails
----------

- Die Eisenkonklave bleibt ein enger Kontroll-, Werkstoff- und Schutzblock.
- `H12` ist der belastbare Kern; der Zulauf ist Funktions- und Druckraum, kein zweiter voll ausgearbeiteter Fraktionskern.
- Mengen, Konvoistaerken, Waffenlisten und freie Produktionsvolumina bleiben offen, solange keine neue Belegkette vorliegt.

Kernlesart T0
-------------

| Bereich | Status | Funktionsprofil | Lesart |
| --- | --- | --- | --- |
| [H12](../03-locations/H12.md) | aktiv | Kommando, Sicherheitsfreigabe, selektive Handels- und Versorgungsfenster | aktiver Eisenkonklave-Kern |
| `H3 -> H12` | beschaedigter Zulauf | Versorgung, Transit und Oeffnung unter Schaden und magnetischer Interferenz | verletzlicher Betriebs- und Sicherheitskorridor |

Freigabekette und Rollen
------------------------

- Varek Solun fuehrt H12 ueber Priorisierung, Kontrolle und den Schutz eigener Module.
- Kaspar Dorn haelt nur die Handelsfenster offen, die materiell und politisch tragbar bleiben.
- Yara Kest erzwingt Sicherheitsfreigaben fuer Transit, Konvois und jede kontrollierte Oeffnung.

Betriebsprioritaeten
--------------------

| Prioritaet | Lesart | Guardrail |
| --- | --- | --- |
| Kontrolle | H12 bleibt zuerst Leitungs- und Sicherungsknoten | keine freie Offenheitslogik |
| Versorgung | Material und Zulauf muessen trotz Schadenskorridor beweglich bleiben | keine still verschwundene Schadenlage |
| Handelsfenster | Tausch ist moeglich, aber nur selektiv und freigegeben | kein offener Markt |
| Werkstoff- und Schutzlogik | die Eigenlage bleibt an Werkstoff-, Instandsetzungs- und Schutzgueter gebunden | kein beliebiges Vollinventar |

Spielbare Konfliktlinien
------------------------

- Kontrolle gegen Oeffnung: Jeder Versuch, H12 wirtschaftlich zu oeffnen, vergroessert Sicherheitsdruck und Zulaufrisiko.
- Versorgung gegen Verriegelung: Ueberhaerte Sicherung schuetzt den Kern, kann ihn aber zugleich materiell ausduennen.
- Werkstofflogik gegen Zeitdruck: Was instandgesetzt oder abgesichert werden muesste, konkurriert mit dem Drang, handlungsfaehig zu bleiben.
- Aussenbeziehungen gegen Eigenkern: Haendlerbund-Fenster, Schienenbund-Feindschaft und umkaempfte Arkologie-Bezuege ziehen an derselben kleinen Freigabekette.

Alltagslesart fuer Spiel und Szenen
----------------------------------

- `H12` wirkt nach innen diszipliniert, zweckgebunden und sicherheitslastig.
- Der Schadenskorridor ist kein Randdetail, sondern bestimmt jede Entscheidung ueber Bewegung, Versorgung und Risiko.
- Selektiver Handel ist in H12 nie Normalitaet, sondern immer Ausnahme unter Freigabe.

Verknuepfte Quellen
-------------------

- [Eisenkonklave](../Eisenkonklave.md)
- [H12](../03-locations/H12.md)
- [Eiserne-Enklave-inventar](../04-inventory/Eiserne-Enklave-inventar.md)
- [eisenkonklave-nahraum-t0](./eisenkonklave-nahraum-t0.md)
- [rp-startbogen-eisenkonklave-h12](../../../../../novapolis-dev/docs/process/rp-startbogen-eisenkonklave-h12.ssot.md)
