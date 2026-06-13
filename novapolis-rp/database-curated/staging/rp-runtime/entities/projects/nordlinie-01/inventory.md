---
stand: 2026-06-13 09:17
update: Nordlinie-Inventar fuehrt jetzt Schuttbruch aus dem C6-Schuttkeil als angefragte Pruefoption, nicht als gebuchten Bestand.
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=PASS; frontmatter=PASS; path-portability=FAIL; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=FAIL; logs-policy=PASS; ruff=FAIL; black=FAIL; pytest=FAIL; pyright=SKIP; mypy=PASS; report=.tmp\results\reports\checks_report_20260613_091615.md
---
Runtime Inventory - Nordlinie 01
================================

Status
------

- slug: nordlinie-01
- holder_or_location: Nordlinie 01 / Verbindungstunnel D5-C6
- state: Arbeitsstand
- review_state: working

Entries
-------

- item: Schweissgeraet
  amount: tbd
  unit: Bedarf
  source: `database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md`; `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 10, Turn 11
  confidence: SSOT- und Runtime-belegt als harter Hauptblocker fuer den Engbogen und den weiteren Reparaturverbund
- item: Adapter / Fitting (DN60)
  amount: tbd
  unit: Bedarf
  source: `database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md`; `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 10, Turn 11
  confidence: SSOT- und Runtime-belegt als harter Hauptblocker zusammen mit dem Schweissgeraet
- item: Anschlusssicherung
  amount: tbd
  unit: Bedarf
  source: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 10, Turn 11
  confidence: runtime-belegt als Teil der gemeinsamen Bedarfskalkulation, aber noch nicht stueckzahlscharf
- item: Verbindungsmaterial
  amount: tbd
  unit: Bedarf
  source: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 10, Turn 11
  confidence: runtime-belegt fuer Leitungsseite und C6-Vorlauf, aber noch nicht stueckzahlscharf
- item: Stuetzbaukasten-Nachsicherung
  amount: `kleiner bis mittlerer Satz Bedarf`
  unit: Satz
  source: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 10; `database-rp/01-factions/novapolis/05-projects/Nordlinie-01-Stuetzbaukasten.md`
  confidence: runtime- und SSOT-nahe belegt als Folgebedarf fuer Nachsicherung und Unterfuetterung
- item: Unterfuetterung
  amount: `kleiner bis mittlerer Satz Bedarf`
  unit: Satz
  source: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 10, Turn 11
  confidence: runtime-belegt als technischer Folgebedarf, noch nicht komponentenscharf zerlegt
- item: Raeumkapazitaet Kontaktseite
  amount: tbd
  unit: Bedarf
  source: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 10
  confidence: runtime-belegt fuer `Schuttkeil Kontaktseite`, aber noch nicht als zaehlbare Ressource aufgeloest
- item: Freiraeumung
  amount: tbd
  unit: Bedarf
  source: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 10, Turn 11
  confidence: runtime-belegt als vorgelagerter Folgebedarf vor weiterem Lastwechsel oder Materialdurchsatz
- item: Schuttbruch aus `Schuttkeil Kontaktseite`
  amount: tbd
  unit: Pruefoption
  source: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 12
  confidence: angefragt, aber nicht bestaetigt; keine gebuchte Materialgewinnung, kein Einsatz und keine Tragfaehigkeit belegt

Repair Cluster Mapping
----------------------

- `Uebergang Engbogen`:
  - harter Kernbedarf: `Schweissgeraet`, `Adapter / Fitting (DN60)`
  - Folgebedarf: `Anschlusssicherung`, `Freiraeumung`
- `Haltepunktpaar Leitungszug`:
  - Folgebedarf: `Verbindungsmaterial`, `Anschlusssicherung`, Freilegung/Einzelpruefung
- `Schottertasche Nordkante`:
  - Folgebedarf: `Stuetzbaukasten-Nachsicherung`, `Unterfuetterung`
  - Pruefoption: Bruchstuecke aus `Schuttkeil Kontaktseite`, falls C6 Eignung, Groesse und Gewinnungsrisiko bestaetigt
- `Schuttkeil Kontaktseite`:
  - Folgebedarf: `Raeumkapazitaet Kontaktseite`, `Freiraeumung`
  - Pruefoption: kontrolliertes Zerschlagen mit moeglicher Wiederverwendung geeigneter Bruchstuecke fuer `Schottertasche Nordkante`
- `Randauflage Suedlauf`:
  - Folgebedarf: `Stuetzbaukasten-Nachsicherung`, `Unterfuetterung`
- `Leitungsaufnahme C6-Vorlauf`:
  - Folgebedarf: `Verbindungsmaterial`, `Anschlusssicherung`, saubere Freilegung

First Fixed Component Cuts
--------------------------

- `Uebergang Engbogen`:
  - `1x Schweissgeraet`
  - `1x Adapter / Fitting (DN60)`
  - `1x Sicherungssatz`
- `Haltepunktpaar Leitungszug`:
  - `1x Sicherungssatz`
  - `1x Dichtungsmanschette`
  - `1x Kabelspule` als Tragrahmen fuer den benoetigten Kabelanschnitt und die Freilegungsarbeit
- `Schottertasche Nordkante`:
  - `1x Metallprofil (mittel)`
  - `2x Stuetzklemme`
  - `1x Lasche / Knotenblech`
  - `1x Ausgleichsplatte`
  - `1x Schraubensatz (mittel)`
- `Schuttkeil Kontaktseite`:
  - `1x Metallprofil (mittel)`
  - `2x Metallprofil (kurz)`
  - `2x Stuetzklemme`
  - `1x Lasche / Knotenblech`
  - `1x Ausgleichsplatte`
  - `1x Schraubensatz (mittel)`
- `Randauflage Suedlauf`:
  - `1x Metallprofil (mittel)`
  - `1x Metallprofil (kurz)`
  - `2x Stuetzklemme`
  - `1x Ausgleichsplatte`
  - `1x Schraubensatz (mittel)`
- `Leitungsaufnahme C6-Vorlauf`:
  - `1x Sicherungssatz`
  - `1x Dichtungsmanschette`
  - `1x Kabelspule` als Tragrahmen fuer den benoetigten Kabelanschnitt und die Freilegungsarbeit

Component-Cut Notes
-------------------

- Diese erste feste Komponentenliste ist eine konservative Arbeitsstueckliste fuer den Folgezug, keine bereits erfolgte Lieferung.
- Sie zieht nur bestehende SSOT- oder SSOT-nahe Klassen aus `Waren-Index`, `Nordlinie-01-Stuetzbaukasten` und den aktiven Inventar-SSOTs.
- `Kabelspule` steht hier als Bestandsanker fuer den benoetigten `Kabelanschnitt`; die uebergeordnete Spule bleibt Stations-/Lagergut, waehrend der kleine Montageabschnitt jetzt als eigene Warenklasse im SSOT lesbar ist.
- Die Liste ersetzt nicht spaetere feinere Aufschluesselung, verhindert aber, dass die Reparaturcluster weiter nur als vage Satzbedarfe stehenbleiben.

T12 Reuse Probe
---------------

- Ronja fragt `C6`, ob der `Schuttkeil Kontaktseite` so zerschlagen werden kann, dass brauchbare Bruchstuecke die `Schottertasche Nordkante` stabilisieren.
- Diese Idee ist eine Pruefoption und keine Bestandsbuchung. Es fehlen noch C6-Antwort, Materialeignung, grobe Menge, Bruchstueckgroesse und Risikobewertung fuer den Kontaktpunkt.
- Erst nach bestaetigter Eignung duerfen daraus `eingesetzt`, `transferiert` oder `Rest`-Werte entstehen.

Existing Material Boundary
--------------------------

- Der kleine Turn-7/8-Satz bleibt ein bereits belegter Altvorgang und wird hier nicht als neuer offener Bedarf doppelt verbucht.
- Belegt ausgeschopft sind aus diesem Altvorgang insbesondere:
  - `Metallprofil (kurz)`
  - `Ausgleichsplatte`
  - `Schraubensatz (mittel)`
- Weitere neue Folgebedarfe muessen deshalb wieder als reale D5-Lieferung oder explizite neue Runtime-Bindung auftauchen.
- Schuttbruch aus dem C6-Schuttkeil ist bis zur Antwort keine neue Runtime-Bindung, sondern nur eine angefragte Wiederverwendungsoption.

Recent Changes
--------------

- Turn 10 hat den bis dahin verteilten Reparaturbedarf erstmals als gemeinsame Bedarfskalkulation von D5- und C6-Haelfte lesbar gemacht.
- Turn 11 spiegelt denselben Bedarf zurueck nach D5, trennt ihn aber klar vom Draisine-Eigenbestand.
- T12 oeffnet eine Wiederverwendungspruefung: Der C6-Schuttkeil koennte, falls geeignet, zugleich geraeumt und als Stabilisierungsmaterial fuer die D5-seitige Schottertasche genutzt werden.
- Dieser Traeger fuehrt den Nordlinie-Bedarf deshalb ab jetzt getrennt von `../../locations/d5/inventory.md` und `../../assets/draisine-transportmodul/inventory.md`.
- Die benannten Reparaturcluster fuehren jetzt zusaetzlich eine erste feste Komponentenliste statt nur offener Satzlogik.
- Die benoetigte kleine Leitungsarbeit kann jetzt kanonisch ueber `Kabelanschnitt` statt nur indirekt ueber `Kabelspule` benannt werden; `Schienenprofil` und `Betonplatte` bleiben dagegen weiter grobere, nur im Fraktions-/Stationsverbrauch belegte Klassen des weiteren Korridors.

Evidence Chain
--------------

- `database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md`
- `database-rp/01-factions/novapolis/05-projects/Nordlinie-01-Stuetzbaukasten.md`
- `database-rp/01-factions/novapolis/03-locations/Verbindungstunnel-D5-C6.md`
- `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 10
- `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 11
- `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 12
- `state.md`
- `../../locations/d5/inventory.md`

Promotion Notes
---------------

- Dieser Traeger fuehrt Bedarf und Reparaturklassen, nicht bereits erledigte Materiallieferungen.
- Mengen erst dann von `tbd` oder Satzlogik auf feste Stuecklisten heben, wenn ein Folgezug die jeweilige Reparaturflaeche komponentenscharf belegt.
- Die hier notierten `First Fixed Component Cuts` sind konservative Arbeitsstuecklisten fuer den naechsten Folgezug; reale Abbuchungen bleiben davon getrennt.
- Neue reale Materialabgaenge aus D5 oder C6 muessen zusaetzlich in den ortsgebundenen Runtime-Inventaren verbucht werden.
- Schuttbruch aus `Schuttkeil Kontaktseite` erst nach C6-Bestaetigung als Materialbewegung oder Einsatz promoten.
