---
stand: 2026-04-27 02:30
update: Eisenkonklave fuehrt jetzt den unmittelbaren Nahraum T0 fuer H12 und den Schadenskorridor konservativ aus.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_022916.md
slug: eisenkonklave-nahraum-t0
category: canon
version: "0.1"
---

Eisenkonklave - Nahraum T0
==========================

Zweck
-----

- Dieser SSOT zieht den unmittelbaren Eisenkonklave-Nahraum konservativ um `H12` nach.
- Er verdichtet den aktiven Kern und den beschaedigten Zulauf, ohne unbelegte Zusatzstationen oder verdeckte Nebenreiche zu erfinden.

Scope
-----

- Kernknoten: [H12](../03-locations/H12.md)
- Zulauf: `H3 -> H12` als belegter Schadens- und Sicherheitskorridor

Raumringe
---------

| Ring | Bereich | Lesart |
| --- | --- | --- |
| 0 | `H12` | aktiver Eisenkonklave-Kern aus Kommando, Freigabe und selektiver Oeffnung |
| 1 | `H3 -> H12` | beschaedigter Zulauf, der Versorgung, Transit und Sicherung zugleich belastet |

Ausbau- und Zustandsstatus
--------------------------

| Bereich | Kontrolle | Status | Zustandslesart | Funktionswert im Nahraum |
| --- | --- | --- | --- | --- |
| [H12](../03-locations/H12.md) | Eisenkonklave | aktiv | stabilster Punkt des lokalen Blocks | Kommandobunker, Leitstand, Versorgungs- und Handelszelle |
| `H3 -> H12` | kein eigener Kern, aber durch H12 hart gefiltert | beschaedigt | magnetische Interferenz und Korridorschaden begrenzen jede Bewegung | Zulauf fuer Versorgung, Transit und Risiko |

Korridore
---------

### Kern `H12`

- `H12` ist der einzige belastbare Eisenkonklave-Kernknoten im unmittelbaren Nahraum.
- Kommando, Sicherheit und selektive Oeffnung liegen hier dichter beieinander als in einem offenen Fraktionsnetz.

### Zulauf `H3 -> H12`

- Der Zulauf bleibt Schadens- und Reparaturkorridor statt normaler Rueckseite.
- Magnetische Interferenz macht jeden Transit planungs- und sicherheitsintensiv.
- Dadurch entsteht ein Nahraum, der nicht aus Expansion, sondern aus kontrollierter Belastung lesbar wird.

Gefahren- und Druckachsen
-------------------------

| Achse | Bereich | Lesart | Schwere |
| --- | --- | --- | --- |
| Korridorschaden | `H3 -> H12` | jede Bewegung bleibt technisch und organisatorisch riskant | hoch |
| Sicherheitsdruck | `H12` | Oeffnung, Handel und Transit werden sofort gegen Kontrolle gerechnet | hoch |
| Versorgungsdruck | `H12` plus Zulauf | Verriegelung schuetzt, kann aber auch Materialfluss und Tempo drosseln | mittel bis hoch |
| Aussenbezug | `H12` | Haendlerbund, Schienenbund und Arkologie ziehen an derselben kleinen Freigabekette | mittel |

Verdeckte Orte (konservativ)
----------------------------

Hinweise

- Die folgenden Raumtypen sind Funktionslesarten und keine bereits belegten Unterraeume.

| Bereich | Wahrscheinlicher Raumtyp | Lesart | Guardrail |
| --- | --- | --- | --- |
| `H12` | Kontrollnischen, Materialvorhaenge, leitstandsnahe Sperrraeume | Kommando und Sicherheit sind eng verflochten | keine konkrete Innenarchitektur erfinden |
| `H3 -> H12` | Reparaturbuchten, stoerungsnahe Engstellen, abgeschirmte Transitabschnitte | Schaden- und Filterraum statt normaler Passage | keine zusaetzlichen Stationsknoten behaupten |

Guardrails
----------

- `H12` bleibt der aktive Kern; der Zulauf begruendet keinen zweiten vollstaendigen Orts- oder Fraktionskern.
- Der Nahraum-SSOT ersetzt keine Ortsdatei, sondern ordnet die belegte Korridorlogik.
- Keine harten Waffen-, Konvoi- oder Bestandszahlen ohne neue Evidenz.
