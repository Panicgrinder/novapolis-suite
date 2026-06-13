---
stand: 2026-06-13 09:17
update: Der alte Runtime-Typordner `characters/` ist nach Redirect-Zielpruefung archiviert; aktive Figuren liegen unter `entities/characters`.
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=PASS; frontmatter=PASS; path-portability=FAIL; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=FAIL; logs-policy=PASS; ruff=FAIL; black=FAIL; pytest=FAIL; pyright=SKIP; mypy=PASS; report=.tmp\results\reports\checks_report_20260613_091615.md
---

RP Runtime Staging
==================

Zweck
-----

Dieser Pfad ist die kontrollierte Laufzeit- und Arbeitsflaeche fuer RP im Chat.

- Hier landen neue oder veraenderte Fakten zuerst als Arbeitsstand.
- Nichts unter `rp-runtime/` ist automatisch RP-SSOT.
- Promotion in `novapolis-rp/database-rp/**` erfolgt erst nach Review oder expliziter User-Freigabe.

Aktive Struktur
---------------

- `sessions/<session-id>/scene-log.md`
- `sessions/<session-id>/transcript.jsonl`
- `entities/<type>/<slug>/entity.md`
- `entities/<type>/<slug>/mind.md`
- `entities/<type>/<slug>/relationships.md`
- `entities/<type>/<slug>/inventory.md`
- `entities/<type>/<slug>/state.md`
- `entities/<type>/<slug>/roster.md`

Namespaces
----------

- `entities/characters/<slug>/` fuer Figuren und handlungsfaehige Einzelentitaeten
- `entities/locations/<slug>/` fuer Orte, Stationen und lokale Roster
- `entities/projects/<slug>/` fuer Projekt- oder Reparaturachsen
- `entities/assets/<slug>/` fuer technische oder materielle Laufzeittraeger
- `entities/factions/<slug>/` fuer aktive Fraktionsoberflaechen

Legacy-Struktur
----------------

Die frueheren Typordner `mind/`, `inventories/`, `state/` und `relationships/` sind keine aktiven Zielordner mehr. Sie bleiben nur als Redirect-Flaechen fuer alte Links und Migrationshistorie erhalten. Der fruehere Typordner `characters/` wurde nach vollstaendiger Zielpruefung unter `novapolis-dev/archive/quarantine/rp-runtime-characters-legacy-20260429-0229/characters/` archiviert.

Routing-Matrix
--------------

- Szenenzuege, verdichtete Turn-Protokolle und Kurzauswertung: `sessions/<session-id>/scene-log.md`
- ungekuerzter RP-/Admin-Chatverlauf: `sessions/<session-id>/transcript.jsonl`
- Figurenanlage oder Figurenupdate: `entities/characters/<slug>/entity.md`
- Mind-/Sphaerenverschiebung, geistnaher Zustand oder relationale Delta-Lesart: `entities/characters/<slug>/mind.md`
- gerichtete Beziehungs- oder Loyalitaetsverschiebung: `entities/<type>/<slug>/relationships.md`
- Inventar-, Transfer- oder Ressourcenupdate: `entities/<type>/<slug>/inventory.md`
- Welt-, Orts-, Fraktions- oder Projektstatus: `entities/<type>/<slug>/state.md`
- Gruppen-, Bewohner- oder Schichtoberflaechen: `entities/<type>/<slug>/roster.md`

Regel fuer Mischfaelle
----------------------

- Ein RP-Zug mit mehreren Folgen landet nicht nur in einer Datei.
- Der Ablauf geht immer nach `sessions/<session-id>/scene-log.md`.
- Jede zusaetzliche belastbare Folge wird parallel in die passende Dossierdatei geschrieben.
- Sekundaerdateien bleiben knapp, referenzieren aber nach Moeglichkeit Session und Turn.

Vertragsregeln
--------------

- RP-SSOT bleibt `novapolis-rp/database-rp/**`.
- `rp-runtime/` ist absichtlich fluechtiger, aber nachvollziehbarer als freie Chat-Improvisation.
- `transcript.jsonl` bleibt append-only Rohspur und ist weder RP-SSOT noch direkt trainierbar.
- Jeder Eintrag soll kenntlich machen, ob er `Probe`, `Arbeitsstand`, `review_required` oder `promotion_ready` ist.
- Jeder laufende Strang braucht zusaetzlich eine klare Einordnung als `Hauptweltpfad`, `Laborpfad`, `verworfen` oder `bewusst pausiert`, damit keine stillen Zeitlinienmischungen in den Kanon rueberlaufen.
- Nicht jede Datei unter `database-rp/**` braucht einen 1:1-Runtime-Spiegel. Runtime-pflichtig sind nur aktiv veraenderliche Laufzeittraeger in `sessions/` und `entities/`; Taxonomien, Preisbaender, Regel-SSOTs, Doctrines, Indizes und historische Szenen bleiben SSOT-only, bis eine explizite Laborfrage etwas anderes verlangt.
- Keine belastbare Aussage ohne Beleg: Als sicher gilt im ERP/RP nur, was in `database-rp/**`, im aktuellen `rp-runtime/**` oder in sauber benannter Session-Evidenz lesbar ist.
- Wenn fuer den laufenden RP-Zug eine belastbare Aussage gebraucht wird, aber der passende Runtime-Traeger fehlt, wird die noetige Dossierdatei zuerst aus bestehender SSOT, Governance und aktueller Session-Evidenz abgeleitet angelegt oder aktualisiert.
- Vor jeder individuellen Entitaetsaktion werden das handelnde Dossier und relevante Ziel-Dossiers gemeinsam geladen. Eine Entitaet darf nicht aus einem isolierten Figurenblatt heraus handeln.
- Nach dem Zug werden betroffene Dossierdateien im selben Lauf aktualisiert oder mit `keine neue Mind-Delta`, `keine neue Relationship-Delta` beziehungsweise `carry_forward_confirmed` bewusst stabil gehalten.
- Beziehungen werden als gerichtete Eintraege (`observer_id -> target_id`) in `relationships.md` des jeweiligen Observers gefuehrt; eine Datei pro Beziehungskante ist kein Standardmodell.
- Aggregate wie `C6-Bewohner` koennen als Roster- oder Gruppenruntime gefuehrt werden, solange keine einzelne Person daraus individuell handelt. Sobald eine einzelne Bewohnerentitaet handelt, wird vorher ein individueller Runtime-Schnitt angelegt oder aktualisiert.
- Wenn weder SSOT noch Runtime eine Aussage tragen, bleibt sie `offen`, `Probe` oder blockiert den Zug; freie Zwischenbehauptungen sind kein zulaessiger Ersatz fuer fehlende Evidenz.

Promotion-Pfad
--------------

1. Szene oder Verwaltungsakt im Chat erzeugt ein Arbeitsartefakt unter `rp-runtime/`
2. Rohchat kann parallel append-only in `sessions/<session-id>/transcript.jsonl` mitlaufen
3. Review auf Kanontreue, Belastbarkeit und Stil
4. Erst danach gezielte Uebernahme nach `database-rp/**` oder in andere kuratierte Artefakte

Labornutzen
-----------

- Weitere RP-Fortsetzung unter Laborbedingungen ist ausdruecklich sinnvoll, solange Hauptweltpfad und Probe-/Nebenpfade sauber getrennt markiert bleiben.
- Der Laborpfad liefert dem Projekt mehr Rohdaten fuer Stil, Weltverdichtung, Review und spaetere Curation, aber nicht automatisch mehr Kanon oder direkt trainierbare Daten.
- Mehr Daten helfen nur dann, wenn Session, Rohspur, Verdichtung, Dossiers und Promotionsentscheidung sauber aufeinander verweisen.
