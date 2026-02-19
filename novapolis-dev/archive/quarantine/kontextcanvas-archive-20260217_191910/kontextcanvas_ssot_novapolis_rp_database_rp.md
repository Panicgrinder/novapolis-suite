Titel: Kontextcanvas – SSOT-Fokus novapolis-rp/database-rp

Zweck
Dieses Canvas ist eine kompakte, belegbare Arbeitskarte fuer die Pflege der RP-SSOT in novapolis-rp/database-rp. Es fasst die groben Bestandszahlen, die Einstiegspunkte, die relevanten Regeln (Naming/Terminologie), die Validatoren und den Link-Audit-Status zusammen. Es ist bewusst so geschrieben, dass es beim Vorlesen stabil bleibt und als Planungsgrundlage fuer Batch-Arbeit taugt.

Repo-Rahmen
Das Repository ist als Suite organisiert: Agent-Backend, RP-Datenbasis, Dev-Dokumentation und Simulation liegen getrennt, aber gemeinsam versioniert. Der SSOT-Teil fuer RP liegt im Modul novapolis-rp. 

Scope-Inventar nach Datenlage
Hinweis zur Metrik: Die gelieferten Zahlen unterscheiden zwischen „nur Markdown“ und „Markdown+JSON“. Fuer die Rang-Entscheidung sind beide relevant, aber sie muessen sauber getrennt bleiben.

1) 01-factions
- Groesster Anteil: 169 Markdown-Dateien.
- md+json Gesamt: 274 Treffer.
- Fraktionen (7): arkologie-a1, eisenkonklave, fluesterkollektiv, haendlerbund, novapolis, schattenbund, schienenbund.
- Fraktionsweise Handel/Diplomatie: pro Fraktion existiert 06-handel-diplomatie mit mehreren Akten.

2) 06-scenes
- 47 Markdown-Dateien.
- Funktion: Narrative Schicht mit Templates und Gates laut README.

3) 00-admin
- 19 Markdown-Dateien.
- md+json Gesamt: 31 Treffer.
- Funktion: Admin-Hubs, Taxonomie, Indexe, Reference- und Memory-Bundles.

4) 00-ops
- 2 Dateien (Markdown).
- Funktion: nicht-diegetische Regeln/Sim-Logik getrennt von Lore.

5) 04-inventory (top-level)
- 2 Markdown-Dateien: Marktpreise-inventar, Freie-Gruppen-inventar.
- md+json Gesamt: 4 Treffer.

6) 06-handel-diplomatie (Top-Level)
- Existiert nicht als eigener Top-Level-Ordner in database-rp.
- Stattdessen: Admin-Hub (Index-Handel-Diplomatie) plus fraktionslokale 06-handel-diplomatie-Ordner.

Einstiegspunkte (Entry Points)
SSOT-Startpunkt
- Current-State.md: als „Single Entry Point“ fuer den aktuellen spielrelevanten Stand.

Admin-Navigation
- Cluster-Index.md: Cluster-/Knoten-Uebersicht.
- Fraktionen-Taxonomie.md: Taxonomie/Fraktionsbeziehungen.
- Index-Handel-Diplomatie.md: Hub, der explizit referenziert statt zu duplizieren.
- Reference-Campaign-State.md: Referenzlage.
- memory-bundle.md: gebuendelter Kontext.

Ops
- 00-ops/README.md: Regeln/Systemnotes, nicht-diegetisch.

Scenes
- 06-scenes/README.md: Definitionen, Templates, Gate-Commands.

Fraktionen
- Pro Fraktion README.md als Struktur- und Zweckbeschreibung.

Naming- und Terminologie-Regeln
Kanonische Quelle
- novapolis-dev/docs/naming-policy.md ist die referenzierte Naming-Policy.

Kernregeln (Kurzfassung)
- ASCII bevorzugt; keine Leerzeichen, keine Unterstriche; Bindestrich als Trenner.
- Umlaute transliterieren: ae/oe/ue; ss fuer ß.
- Dateiendungen klein (z.B. .md).
- Eigennamen duerfen Grossbuchstaben tragen, aber Dateinamen bleiben regelkonform.
- Es existiert ein Naming-Validator (check-names) mit einem Apply-Modus, der Umbenennungen und Link-Nachzug implizieren kann.

Validatoren und Checks
Node-Validatoren (novapolis-rp/coding/tools/validators)
- validate:curated: kuratiertes Material validieren.
- validate:rp: RP-SSOT Regeln/Schema.
- validate:crossrefs: Cross-References pruefen.
- check:names: Naming-Lint (Apply-Modus moeglich).
- validate: Orchestrator.

Python-Checks (Repo-root scripts)
- check_frontmatter.py: Frontmatter-Pflichtfelder, Timestamps/Patterns.
- checks_rp_consistency.py: Konsistenz-Audit (u.a. lokale Links, H1, Slug-Regeln, Reports).

Link-Audit (drei Kategorien)
A) Reale relative Markdown-Links
- In Admin, Scenes und vielen Fraktionsakten vorhanden.
- Auffaellig: 04-inventory zeigt in der gelieferten Suche keine relativen Link-Matches.

B) Pfad-Erwaehnungen als Klartext/Code
- Pfade werden haeufig in Backticks oder als Plain-Text genannt, statt als klickbare Links.
- Das ist fuer Menschen und fuer Agenten schlechter, weil es Navigation, Crossrefs und Automatisierung erschwert.

C) Legacy-Terminologie „Haendlergilde/Händlergilde“
- Mehrere Treffer in Diplomatie- und Index-Dateien.
- Wichtig: In der gelieferten Zusammenfassung ist „vollstaendige Trefferliste“ nicht wirklich vollstaendig, wenn „vollstaendig“ Fundstellen meint. Es ist eher eine kuratierte Liste. Das muss im Batch-Modus klar definiert werden.

Auffaelligkeiten (fuer fruehe Priorisierung)
- Handel/Diplomatie-Indexe fuehren Pfade teils nur als Code-Text statt als echte Links.
- Legacy-Begriffe tauchen sichtbar auf und muessen entweder als Audit-Flag oder als Migrationsauftrag behandelt werden.
- Freie-Gruppen-inventar: Hinweis auf doppelte Frontmatter/meta-artige Segmente, potenzieller frueher Korrupionskandidat.

Batch-Plan (normalisiert)
Batch A: Mechanik und Regeln (einmalig, repo-weit)
- Ziel: Naming-Policy als harte Leitplanke, Validatoren als Gate-Kette.
- Output: klare Umbenenn-/Link-Fix-Liste (noch keine Edits im selben Schritt, wenn du Audit sauber trennen willst).

Batch B: SSOT-Hubs (00-admin + 00-ops)
- Ziel: Entry Points, Indexe, Taxonomie, Ops-Trennung.
- Fokus: echte relative Links statt Pfad-Text, ohne Inhalte neu zu schreiben.

Batch C: Fraktionen (01-factions) fraktionsweise
- Ziel: pro Fraktion Scaffold/Links/Dateinamen stabilisieren, dann Inhalte.
- Besonderheit: novapolis ist der groesste Cluster, also ggf. granular splitten.

Batch D: Scenes und Inventory quer
- Scenes: Crossrefs/Slug-Disziplin (Templates, Gates).
- Inventory: globale Referenzen, Frontmatter-Konsistenz, Linkbarkeit.

STOP-Gate (hier musst du eine klare Norm setzen)
1) „Vollstaendige Trefferliste“ im Link-Audit: bedeutet das jede betroffene Datei oder jede einzelne Fundstelle pro Datei?
2) Legacy-Begriffe: nur Audit-Flag oder Migration (Umbenennen/Terminologie-Refactor)?
3) Batch-Definition: Soll Batch A „Mechanik“ strikt vor allen anderen laufen und keinerlei Content-Aenderungen enthalten?
4) Naming-Apply: Darf der Apply-Modus automatisch umbenennen oder nur als Dry-Run genutzt werden?
5) Szenen-Frontmatter: werden die README-Pflichten als harte Norm (Validation-Gate) behandelt oder nur als Doku-Fakt?

Projekt-Ablage (Vorschlag fuer die Suite)
- Datei: novapolis-dev/docs/kontextcanvas-database-rp.md
- Inhalt: exakt dieses Canvas.
- Zweck: als dauerhafter, repo-naher Einstieg fuer Menschen und Agenten.
