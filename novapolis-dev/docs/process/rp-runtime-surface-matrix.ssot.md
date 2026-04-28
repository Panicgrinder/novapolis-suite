---
stand: 2026-04-28 05:46
update: Diese SSOT fuehrt fuer den aktiven Nordlinie-Hauptpfad jetzt auch den vollstaendigen belegten Runtime-Traegersatz aus Figuren-, Mind- und Ortsdateien statt nur den ersten Mind-Slice.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260428_052348.md; snapshot-lock PASS (2026-04-28 05:46)
---

RP Runtime Surface Matrix
=========================

Zweck
-----

Diese SSOT beantwortet fuer den aktiven RP-Baum die operative Frage, welche Dateien vor einem laufenden ERP-/RP-Test wirklich als Runtime-Flaeche gebraucht werden.

- Ziel ist nicht, `database-rp/**` blind zu spiegeln.
- Ziel ist eine kleine, belastbare Runtime-Surface fuer aktiv veraenderliche Laufzeittraeger.
- Alles andere bleibt bewusst SSOT-only, bis eine explizite Laborfrage eine eigene Laufzeitspur verlangt.

Kernregel
---------

- Vor einem RP-Lauf muessen die kanonischen Runtime-Pfade und Vorlagen existieren.
- Vor einem konkreten RP-Lauf muessen nicht alle moeglichen Runtime-Dateien vorab angelegt sein.
- Angelegt werden im Voraus nur die Typflaechen und die aktuell benoetigten Traegerdateien des laufenden Strangs.

Aktive Runtime-Klassen
----------------------

| RP-SSOT-Klasse | Beispiel im RP-Baum | Runtime-Pflicht | Runtime-Ziel | Regel |
| --- | --- | --- | --- | --- |
| Szenen / Laufender Turn | `database-rp/06-scenes/**`, laufender Chat | ja | `rp-runtime/sessions/<session-id>/scene-log.md` | Live-Turns laufen immer ueber `sessions/`, nicht als neue SSOT-Szene |
| Rohspur / ungekuerzter Verlauf | laufender Chat | ja, wenn Transcript genutzt wird | `rp-runtime/sessions/<session-id>/transcript.jsonl` | append-only Rohspur, nie direkte SSOT |
| Charaktere | `01-factions/*/02-characters/*.md` | ja, wenn Figur im Lauf neu entsteht oder sich belastbar aendert | `rp-runtime/characters/<slug>.md` | nur aktive Figuren, keine Vorab-Spiegelung aller Charaktere |
| Mind-Cluster | `01-factions/*/07-mind-clusters/*.md` | ja, wenn geistnahe oder relationale Wirkung im Lauf relevant ist | `rp-runtime/mind/<slug>.md` | Delta-Arbeitsstand gegen bestehende Mind-Cluster-SSOT |
| Beziehungen / Loyalitaeten | `06-handel-diplomatie/Relationslog*.md` oder beziehungsnahe SSOT | ja, wenn eine einzelne Beziehungsachse belastbar kippt | `rp-runtime/relationships/<slug>.md` | fuer Achsen, die nicht im vollen Mind-Delta aufgehen |
| Inventare / Transfers | `04-inventory/*.md` | ja | `rp-runtime/inventories/<slug>.md` | nur reale Bewegungen oder belastbare Bedarfe |
| Welt-, Orts-, Projektstatus | `03-locations/*.md`, `05-projects/*.md` | ja | `rp-runtime/state/<slug>.md` | fuer Orte, Projekte, Krisen- oder Fraktionsstand |

SSOT-only-Klassen
-----------------

| RP-SSOT-Klasse | Beispiel im RP-Baum | Standardentscheidung | Warum |
| --- | --- | --- | --- |
| Regel- und Governance-SSOT | `00-admin/rp-terminologie.ssot.md`, `Reference-Campaign-State.md`, `Fraktionen-Taxonomie.md`, `Tags-Taxonomie.md` | SSOT-only | Diese Dateien setzen Rahmen, sie sind kein laufender Zugtraeger |
| Karten, Graphen, Indizes | `Metrokarte-T0.md`, `Metrograph.md`, `Cluster-Index.md`, `Nordlinie-D5-C6-Index.md` | SSOT-only | Navigation und Aggregation, keine primäre Runtime-Fuehrung |
| Doctrine / Historie | `01-factions/*/00-doctrine/**` | SSOT-only | Langsame Weltgrundlage statt laufende Turn-Flaeche |
| Preisbaender / Marktmodelle | `06-handel-diplomatie/novapolis-pricebands.md`, `novapolis-markets.md` | SSOT-only | Referenzrahmen fuer Bewertung, nicht selbst Runtime-Ereignis |
| Ops-Policies | `00-ops/*.ops.md`, `03-locations/*-Policy.md` | SSOT-only, Wirkung laeuft ueber `state/` oder `inventories/` | Policies werden nicht pro Turn neu gespiegelt; nur ihre Folgen werden runtime-relevant |
| Historische SSOT-Szenen | `database-rp/06-scenes/*.md` | SSOT-only | Archivierte oder kanonisierte Szenen werden nicht 1:1 als Runtime-Datei dupliziert |
| Trainingsstand-/Wissensstand-Anhaenge | `*Wissensstand-Trainingsstand.md` | SSOT-only, ausser explizitem Laborauftrag | Diese Flaechen sind Referenz- oder Trainingsnahe Helfer, keine Standard-Runtime |

Vor dem naechsten RP-Lauf wirklich noetig
-----------------------------------------

Vor einer sauberen Fortsetzung des aktiven Nordlinie-Strangs muessen vorhanden sein:

1. die kanonischen Runtime-Typflaechen `sessions`, `characters`, `mind`, `relationships`, `inventories`, `state`,
2. die aktive Session-Datei,
3. die aktuell benoetigten Traegerdateien fuer den konkreten Strang.

Fuer Nordlinie D5-C6 heisst das aktuell mindestens:

- `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`
- `state/nordlinie-01.md`
- `state/d5.md`
- `inventories/d5.md`
- `characters/ronja-kerschner.md`
- `characters/reflex.md`
- `characters/jonas-merek.md`
- `characters/pahl-brenner.md`
- `characters/lumen.md`
- `mind/ronja-kerschner.md`
- `mind/reflex.md`
- `mind/jonas-merek.md`
- `mind/pahl-brenner.md`
- `mind/lumen.md`

Dabei gilt fuer den aktuellen Hauptpfad bewusst ebenfalls:

- Kein eigenes `state/novapolis.md`, solange sich der Delta-Druck nur ueber `Nordlinie-01` und `D5` konkret belegen laesst.
- Kein neues `inventories/c6.md` oder eigener C6-Figurenblock fuer den Hauptpfad, solange C6 im Runtime-Zug nur als vorsichtige Gegenseite ohne ausformulierte neue Personen- oder Materialbewegung auftaucht.
- Keine separate `relationships/`-Datei nur fuer Jonas-Lumen, solange die Kopplung vollstaendig ueber Figuren- und Mind-Runtime nachvollziehbar bleibt.

Nicht notwendig vorab:

- eine leere Runtime-Datei fuer jeden Ort, jedes Projekt, jeden Charakter und jede SSOT-Datei in `database-rp/**`
- ein Vollspiegel des ganzen `00-admin`-Ordners
- ein 1:1-Shadow fuer alte `06-scenes/**`

Operative Folge
---------------

- Vor dem Weiterspielen muss die Runtime-Surface vollständig als Typgeruest stehen.
- Vor dem Weiterspielen muessen nur die aktuell benoetigten Traegerdateien existieren.
- Weitere Runtime-Dateien werden erst angelegt, wenn der laufende Strang sie real braucht.

Verknuepfte Quellen
-------------------

- `novapolis-rp/database-curated/staging/rp-runtime/README.md`
- `novapolis-rp/database-curated/staging/rp-runtime/mind/README.md`
- `novapolis-dev/docs/process/rp-labor-review-und-promotion-matrix.ssot.md`
