---
stand: 2026-04-29 03:56
update: In entity-centric Runtime-Dossier migriert; Inhalt bleibt Arbeitsstand ohne Kanon-Promotion.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260429_035444.md
---
Runtime Inventory - D5
======================

Status
------

- slug: d5
- holder_or_location: D5
- state: Probe
- review_state: working

Entries
-------

- item: Schweißgeraet
  amount: tbd
  unit: Bedarf
  source: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 1, Turn 5
  confidence: belegt im SSOT-Bedarf; im Runtime-Zug jetzt als harter Sofortblocker gegliedert
- item: Adapter DN60
  amount: tbd
  unit: Bedarf
  source: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 1, Turn 5
  confidence: belegt im SSOT-Bedarf; im Runtime-Zug jetzt als harter Sofortblocker gegliedert
- item: Metallprofil (mittel)
  amount: `2 transferiert / 2 eingesetzt / 0 Tunnelrest`
  unit: Stueck
  source: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 7
  confidence: konservative Review-Buchung aus kleiner realer Teilbereitstellung
- item: Metallprofil (kurz)
  amount: `4 transferiert / 4 eingesetzt / 0 Tunnelrest`
  unit: Stueck
  source: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 7, Turn 8
  confidence: konservative Review-Buchung aus kleiner realer Teilbereitstellung plus ausgeschopftem Tunnelrest
- item: Stuetzklemme
  amount: `4 transferiert / 4 eingesetzt / 0 Tunnelrest`
  unit: Stueck
  source: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 7
  confidence: konservative Review-Buchung aus kleiner realer Teilbereitstellung
- item: Lasche / Knotenblech
  amount: `2 transferiert / 2 eingesetzt / 0 Tunnelrest`
  unit: Stueck
  source: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 7
  confidence: konservative Review-Buchung aus kleiner realer Teilbereitstellung
- item: Ausgleichsplatte
  amount: `2 transferiert / 2 eingesetzt / 0 Tunnelrest`
  unit: Stueck
  source: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 7, Turn 8
  confidence: konservative Review-Buchung aus kleiner realer Teilbereitstellung plus ausgeschopftem Tunnelrest
- item: Schraubensatz (mittel)
  amount: `4 transferiert / 4 eingesetzt / 0 Tunnelrest`
  unit: Satz
  source: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 7, Turn 8
  confidence: konservative Review-Buchung aus kleiner realer Teilbereitstellung plus ausgeschopftem Tunnelrest
- item: Bolzen-Mutter-Satz (stark)
  amount: `1 transferiert / 1 eingesetzt / 0 Tunnelrest`
  unit: Satz
  source: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 7
  confidence: konservative Review-Buchung aus kleiner realer Teilbereitstellung
- item: Klebmasse (schwach)
  amount: `1 transferiert / 1 eingesetzt / 0 Tunnelrest`
  unit: Kartusche
  source: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 7
  confidence: konservative Review-Buchung aus kleiner realer Teilbereitstellung

Recent Changes
--------------

- Der gebundene Prototypbestand der Draisine wird ab jetzt in `../../assets/draisine-transportmodul/inventory.md` getrennt gefuehrt statt weiter implizit in der D5-Bedarfsnotiz mitzuschwingen.
- Dieses D5-Inventar bleibt damit auf D5-seitigen Tunnelbedarf, reale Turn-7/8-Materialbewegung und offene Projektblocker fuer Nordlinie fokussiert.
- Der eigentliche Projektbedarf von Nordlinie 01 liegt ab jetzt zusaetzlich in `../../projects/nordlinie-01/inventory.md`, damit `inventory.md` nicht gleichzeitig Ortsbestand, Altverbrauch und gesamte Projektbedarfskalkulation tragen muss.
- Ronja meldet nach Abschluss eines D5-seitigen Tunnelabschnitts den Bedarf fuer Folgearbeit knapp nach D5 durch.
- Der Eintrag ist bewusst Bedarfs- und keine Transfernotiz; tatsaechliche Entnahme oder Lieferung bleibt offen, bis D5 reagiert.
- D5 bestaetigt den Bedarf und priorisiert ihn intern, liefert im laufenden Zug aber weder Schweißgeraet noch DN60-Adapter sofort aus.
- Bis zum Ende von Turn 6 bleibt der Runtime-Stand damit bei Bedarf und Werkstattpriorisierung; konkrete Ausgabe, Behelfslieferung oder Transport sind bis dahin noch offen.
- Die erste Materialerfassung des Folgeabschnitts trennt jetzt harte Sofortblocker (`Schweißgeraet`, `Adapter DN60`) von markierten Folgebedarfen (`Stuetzelemente` an klar benannten Schwachzonen).
- Nach der gegliederten Bedarfsskizze aus Turn 5 und der konkreten Werkstattantwort aus Turn 6 ist die schmale Werkstattvorbereitung fuer Stuetzelemente belastbar belegt, ohne Schweißgeraet oder DN60 mitzufiktionalisieren.
- In Turn 7 ist dieser kleine Behelfssatz real in den Tunnelzug uebergegangen, wurde an ersten Schwachzonen eingesetzt und bleibt transport- und setzseitig an Ronjas Arbeitszug mit koerpernaher Reflex-Assistenz gebunden; fuer den Satz liegt nun eine konservative Klassenbuchung mit Tunnelrest vor.
- In Turn 8 wird keine neue D5-Lieferung nachgezogen; Ronja und Reflex verbauen nur noch den verbliebenen Tunnelrest, um eine vibrierende Kante fuer den naechsten Leseschritt zu beruhigen und den engeren Fehlerkorridor sauber zu erfassen.
- Offen bleiben ueber den kleinen Turn-7-Satz hinaus jede weitere Werkstattzusage, die chargenscharfe Vorhistorie in D5 und alle Folgeabgaenge oder Ruecklaeufe.

Turn Delta Ledger
-----------------

Turn 7 - Reale Teilbereitstellung aus D5
----------------------------------------

- delta_kind: transfer-plus-erster-einsatz
- source_holder: D5-Werkstatt
- target_scope: markierte Schwachzonen im D5-seitigen Tunnelabschnitt von Nordlinie 01
- belegt_geliefert:
  - `metallprofil-mittel`: 2 Stueck
  - `metallprofil-kurz`: 3 Stueck sicher belegt im Ersteinsatz; 1 weiteres Stueck bleibt bis Turn 8 als Tunnelrest lesbar
  - `klemme`: 4 Stueck
  - `lasche-knotenblech`: 2 Stueck
  - `ausgleichsplatte`: 1 Stueck sicher belegt im Ersteinsatz; 1 weiteres Stueck bleibt bis Turn 8 als Tunnelrest lesbar
  - `schraubensatz-mittel`: 3 Saetze sicher belegt im Ersteinsatz; 1 weiterer Satz bleibt bis Turn 8 als Tunnelrest lesbar
  - `bolzen-mutter-satz-stark`: 1 Satz
  - `klebmasse-schwach`: 1 Kartusche
- belegt_eingesetzt:
  - Der Satz wird an ersten markierten Schwachzonen eingesetzt und verbessert dort Sicherung und Lesbarkeit.
  - Zwei Stellen lassen sich sichtbar beruhigen; lose Kanten stehen nicht mehr sofort auf Druck, ein kurzer Abschnitt wirkt beim Nachsetzen weniger fragil.
- ort_und_verarbeitung:
  - belegt: Ronja setzt das Material risikobasiert an bereits markierten Schwachzonen ein, Reflex traegt und stabilisiert koerpernah als Exoskelett-Assistenz.
  - offen: Der Turn benennt fuer den Ersteinsatz noch keine vollstaendig komponentenscharfe Zuordnung jeder einzelnen Klasse zu einem exakt benannten Punkt.
- evidence_chain:
  - `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 7
  - `database-rp/01-factions/novapolis/05-projects/Nordlinie-01-Stuetzbaukasten.md`, konservative Beispielbuchung Turn 7

Turn 8 - Restverbrauch ohne neue D5-Lieferung
---------------------------------------------

- delta_kind: restverbrauch-ohne-neuen-transfer
- source_holder: verbleibender Tunnelrest aus Turn 7
- target_scope: `Schottertasche Nordkante`
- belegt_geliefert:
  - keine neue D5-Lieferung
- belegt_eingesetzt:
  - `metallprofil-kurz`: 1 Stueck
  - `ausgleichsplatte`: 1 Stueck
  - `schraubensatz-mittel`: 1 Satz
- ort_und_verarbeitung:
  - belegt: Ronja setzt das verbliebene kurze Metallprofil zusammen mit der letzten Ausgleichsplatte und dem letzten mittleren Schraubensatz an die vibrierende Nordkante, damit die `Schottertasche Nordkante` fuer den naechsten Leseschritt nicht sofort wieder aufreisst.
  - belegt: Reflex haelt den Druck koerpernah und unterstuetzt die Verarbeitung weiter als Exoskelett-Assistenz.
- result:
  - Kein weiterer Tunnelrest fuer `metallprofil-kurz`, `ausgleichsplatte` und `schraubensatz-mittel`.
  - Weitere materielle Fortschreibung bleibt bis zu einer explizit realen neuen D5-Lieferung gesperrt.
- evidence_chain:
  - `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 8
  - `../../projects/nordlinie-01/state.md`, Named Problem Clusters / `Schottertasche Nordkante`

Evidenzgrenze
-------------

- Der Runtime-Diff belegt Lieferung, erste Verarbeitung und Restverbrauch des kleinen Turn-7/8-Satzes.
- Nicht voll belegt bleibt fuer Turn 7 die exakte komponentenscharfe Zuordnung aller Einzelteile auf jeweils einzeln benannte Schwachzonen.
- Diese Luecke bleibt absichtlich offen und wird erst bei spaeterer expliziter Scene- oder State-Evidenz weiter geschlossen.

Promotion Notes
---------------

- Kleiner Turn-7-Satz ist jetzt restseitig ausgeschopft; weitere materielle Folgezuege erst nach explizit realer D5-Lieferung promoten
- Draisine-Eigenbestand, kleiner Werkstattverbrauchsrahmen und spaetere echte Draisine-Abgaenge laufen ab jetzt ueber `../../assets/draisine-transportmodul/inventory.md`, nicht ueber diese D5-Bedarfsnotiz.
- Nordlinie-Reparaturbedarf und Cluster-Materialschnitt laufen ab jetzt ueber `../../projects/nordlinie-01/inventory.md`; dieses D5-Inventar bleibt der ortsgebundene Quell- und Bedarfstraeger.
