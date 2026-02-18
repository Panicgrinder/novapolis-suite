---
stand: 2026-02-16 18:44
update: Phase-1 Charakter-Mindestumfang und Kernrollen-Checkpoint nach Fraktionsabgleich abgehakt.
checks: "Charakter-Count je Fraktion (PowerShell) PASS: arkologie-a1=3, eisenkonklave=3, fluesterkollektiv=3, haendlerbund=3, novapolis=42, schattenbund=4, schienenbund=3"
---

RP Base TODO
============
Zielbild
--------

- Stabile RP-Basis ohne Drift: Orte, Personen, Projekte, Inventare und Chronik sind konsistent.
- Canon ist in Schichten organisiert: Core (unumstoesslich) → Reference (Objekte) → Narrative (Scenes/Chronik).
- Backlog-Daten (RAW/curated) werden kontrolliert nach SSOT promoted (keine stillen Retcons).

Scope / SSOT
------------

- SSOT: `novapolis-rp/database-rp/`
- RAW (ungefiltert): `novapolis-rp/database-raw/99-exports/`
- Curated (Arbeitsstand): `novapolis-rp/database-curated/staging/` → `reviewed/` → `final/`

Befund-Integration (2026-01-12)
------------------------------

Kurzfassung des aktuellen Zustands (Repo-Scan):

- SSOT ist vorhanden und bereits gut strukturiert in `novapolis-rp/database-rp/` (Admin/Core + Reference-Objekte + Narrative/Scenes) mit YAML-Frontmatter und (mindestens fuer Kernobjekte) JSON-Sidecars.
- SSOT-Index existiert: `novapolis-rp/database-rp/index.json` listet aktuell u. a. `scene-2025-10-27-a/b/c` sowie Character/Location/Inventory/Project/Admin-Dateien.
- RAW ist umfangreich und korrekt getrennt in `novapolis-rp/database-raw/99-exports/` (Chat-Exports, viele RAW-Canvas-Snapshots, PDFs).
- Curation ist technisch gut aufgestellt (`database-curated/staging/manifest.json` + Normalisierung/Chunking/Hash/Delta/Stats/Review-Artefakte) und hat bereits ein explizites Promotion-Gate nach `final/`.
- Validatoren sind vorhanden (RP/Curated):
  - RP-Mindestregeln (Heading + leichte Frontmatter-Typchecks).
  - Scene-XREF-Check (Refs muessen slug-only sein) inkl. einiger Co-Occurrence-Regeln.

Was fuer eine belastbare Basis noch fehlt (und hier als Tasks nachgezogen wird):

- Schema-Haerte fehlt: Templates existieren, aber ein harter Gate-Validator fuer Pflichtfelder/Typen pro Kategorie (character/location/inventory/project/scene) ist noch nicht als "Fail-fast" erkennbar.
- Cross-Refs sind noch nicht ganzheitlich: aktuell stark Scene-fokussiert; global fehlen Checks wie slug-Unique, dangling refs in `dependencies/owners/locations/connections`, sowie Abgleich von Logs/Indices gegen existierende Entities.
- Abdeckung/Completeness: "Narrative" ist fuer ein stabiles Gedaechtnis typischerweise unterrepraesentiert (mehr Chronik-Anker/Scenes oder systematische Extraktion aus RAW/curated noetig).
- Simulation: Grunddaten fehlen (Inventar-Mengen/Einheiten, Logistik-Konten, Fraktionsstatus-Variablen, Zeit/Tick-Modell, Weltknoten/Handelsrouten).
- "Current State" als Single Entry Point ist vorhanden, aber noch nicht als Ableitung/Gate erzwungen.

Kompaktstatus (Uebernahme aus Zusammenfassung)
---------------------------------------------

Was bereits steht (Kernpunkte)

- Zielbild ist klar: SSOT in `novapolis-rp/database-rp/`, Pipeline RAW → curated → SSOT, Canon-Schichtung Core → Reference → Narrative.
- SSOT ist strukturiert; Index `novapolis-rp/database-rp/index.json` existiert; RAW ist sauber getrennt; Curation hat Manifest + Promotion-Gate.
- Validatoren existieren (RP/Curated) und erzwingen bereits Basisregeln; Scene-XREF ist slug-only.

Groesste Wissensluecken / offene Luecken (Top)

- Schema-Haerte (Fail-fast) pro Kategorie fehlt noch als klares Gate: Pflichtfelder/Typen fuer character/location/inventory/project/scene.
- Cross-Refs global noch nicht ganzheitlich: slug-Unique, dangling refs (dependencies/owners/locations/connections), Index/Log-Abgleich gegen Entities.
- Narrative-Abdeckung ist tendenziell zu duenn: mehr Chronik-Anker/Scenes oder systematische Extraktion aus RAW/curated.
- Sim-Input-Luecken: Inventar-Bestaende, Logistik-Konten, Fraktionsstatus und Zeit/Tick fehlen als harte Werte.
- World-Graph (externe Knoten/Routen/Gefahrenzonen) ist zu duenn fuer Simulation.

Naechste harte Gates (Minimalziel)

- Validator-Gates haerten (RP + curated): Pflichtfelder + Crossrefs + slug-Unique als harte FAILs.
- Unresolved-Listen aus `database-curated/reviewed/**/unresolved.json` priorisieren und in Decisions ueberfuehren.
- Abdeckung erhoehen: zusaetzliche Scenes aus RAW/curated ableiten oder begruenden.

Arbeitsprinzipien (Gates)
------------------------

- Keine Canon-Aenderung ohne: (1) Konfliktliste, (2) Entscheidung, (3) Update in SSOT.
- Konflikte werden als "Decision" dokumentiert (kurz: Problem → Entscheidung → Auswirkungen).
- Wenn etwas im Export steht, aber Canon widerspricht: erst als `FACT?` aufnehmen, dann entscheiden.

Arbeits-Prompts (Staffelung / copy & paste)
------------------------------------------

Hinweis: Jeder Prompt ist bewusst klein geschnitten. Erst wenn ein Prompt abgeschlossen ist (und ggf. in SSOT nachgezogen wurde), zum naechsten wechseln.

1) Konfliktliste extrahieren (aus Curated-Review)

```text
Bitte lies `novapolis-rp/database-curated/staging/*.review.md` (insb. den grossen Chat-Review) und extrahiere eine Konfliktliste.

Ausgabeformat:
- Top 10 Konflikte (kurzer Titel + 2-3 Saetze Kontext)
- Pro Konflikt: betroffene SSOT-Dateien (vermutet) + ob das eher Core/Reference/Narrative ist
- Pro Konflikt: Empfohlene Prioritaet (P0/P1)

update: Simulations-Readiness-Luecken ergaenzt; Current-State-Notiz aktualisiert.
checks: not run (not requested)
Wir muessen den N7-Status festnageln.

Bitte schlage 2-3 plausible Entscheidungen vor (Option A/B/C), jeweils mit:
- Entscheidung (1 Satz)
- Welche Canon-Dateien (SSOT) angepasst werden muessen

Danach: Bitte empfehle genau 1 Option als Default und begruende kurz.
```

3) Decision Record #2: E2/E3 + Gasunfall + Jonas Herkunft

```text
Bitte klaere die Konflikte um E2/E3 (Gasunfall-Station) und Jonas Herkunft.

Ausgabe:
- Konfliktbeschreibung (kurz)
- Entscheidungsvorschlag (ein kanonischer Satz, der in Core stehen kann)
- Liste: Welche Dateien muessen geaendert werden (mindestens Admin/Timeline, evtl. Characters/Locations)
```

4) Decision Record #3: C6 Linien/Abzweige (Naming + Status)

```text
Bitte definiere ein konsistentes Linienmodell fuer C6 (Linien/Abzweige, Bezeichnungen, Status), so dass D5/E3/F1 und "unbekannt" sauber abbildbar sind.

Ausgabe:
- Mini-Schema (z. B. Linie = Hauptast, Abzweig = Nebenast)
- Namensregeln
- Mapping: D5/E3/F1 -> welche Linie/Abzweig
- Betroffene Dateien
```

5) Decision Record #4: Energie-/Verbrauchsmodell (Buchungen)

```text
Bitte formuliere ein minimales Energie-/Verbrauchsmodell fuer D5/C6:
- Welche Konten existieren?
- Was wird taeglich gebucht (Tagesabschluss)?
- Welche Werte sind "spielbar" (RP) und welche sind nur Hintergrund?

Ausgabe als Bulletliste + 1 Beispielbuchung.
```

6) Decision Record #5: Tunnel-Fortschritt Methodik

```text
Bitte loese den Fortschritts-Konflikt (40% vs >60%) ueber eine klare Methodik:
- Was misst "Fortschritt" (z. B. Erkundungsgrad, Sicherung, Ausbau)?
- Wie wird er berichtet (Missionslog vs Projektstatus vs Scene)?
- Wie lassen wir alte Angaben als "damals" vs "jetzt" konsistent wirken?
```

7) Fraktionen-Taxonomie + Wissensmatrix

```text
Bitte definiere das Fraktions-Set ("vier Hauptfraktionen" vs weitere Gruppen) als Taxonomie:
- Hauptfraktionen (max 4) + Neben-/Splittergruppen
- Wissensmatrix: Wer weiss was ueber Tunnel/E3/N7 (high/medium/low)
- Welche Infos duerfen in Core vs Reference vs Narrative
```

8) Timeline T+0 operationalisieren

```text
Bitte mache `novapolis-rp/database-rp/00-admin/Canvas-T+0-Timeline.md` brauchbar:
- Definiere T+0 (Tag/Datum/Uhrzeitfenster)
- Erstelle mindestens 5 Marker (Start, 2-3 Schluesselevents, Ende)
- Verlinke Marker auf Scenes (neu oder bestehend)
```

9) Scenes: 3 Chronik-Anker ausarbeiten

```text
Bitte erstelle/aktualisiere mindestens 3 Scenes als Chronik-Anker:
- Jede Scene: Kurzsummary, Entscheidungen, Konsequenzen/Statusaenderungen, Links (Orte/Projekte/Missionslog)
- Keine Retcons ohne Decision-Verweis
```

10) Umsetzungs-Patch (SSOT Updates)

```text
Bitte setze die beschlossenen Decisions als konkrete Aenderungen in SSOT um.

Ausgabe:
- Liste der zu aendernden Dateien
- Pro Datei: was genau aendern (kurz)
- Danach: Welche Checks laufen lassen (Frontmatter, markdownlint, rp_consistency)
```

P0: Entscheidungen (Stabilitaets-Killer zuerst)
----------------------------------------------

- [x] N7-Status final: existiert nicht vs. Bereich in C6 vs. versiegelt (und was im Canon ueberhaupt sichtbar bleibt).
- [x] E2/E3 klaeren: Gasunfall-Station + Jonas Herkunft (einmal festnageln).
- [x] Fraktions-Anzeigenamen: "Händlerbund"/"Schienenbund" umgesetzt (IDs/Slugs bleiben unverändert).
- [x] C6 Linien/Abzweige: Anzahl + Bezeichnungen + Status (D5, E3, F1, "unbekannt"?)
- [x] Energie-/Verbrauchsmodell: D5/C6 Konten, Tagesabschluss, Reaktor/Generator, was gebucht wird.
- [x] Tunnel-Fortschritt: Berechnungs- und Reporting-Methodik (40% vs >60% Konflikte aufloesen).
- [x] Fraktionen-Set: "vier Hauptfraktionen" vs. weitere Gruppen (Taxonomie + Wissensmatrix).

P0: Basis-Integritaet (Drift-Guards)
-----------------------------------

- [x] SSOT-Index driftfrei: `novapolis-rp/database-rp/index.json` deckt alle relevanten SSOT-Dokumente ab (inkl. Scenes a/b/c + JSON-Sidecars; verifiziert via `checks_rp_consistency.py --strict`).
- [x] Sidecar-Regel klarziehen: Option A als Zielbild (SSOT-/Index-Dokumente haben JSON-Sidecar; Drift wird per `checks_rp_consistency.py --strict` frueh sichtbar; **READMEs sind ausgenommen**).
- [x] Referenzstandard festnageln: Slug ist die einzige Referenz-ID (Scenes/Tagging/Missionslog/Links/Dependencies); Dateiname ist nur Ablageform.
- (Teil-Gate) Slug ist Pflichtfeld für `category` (character/location/inventory/project/scene) via `npm run validate:rp`.
- (Teil-Gate) Crossrefs werden slug-only gegen SSOT-`slug` validiert (kein Basename-/Foldername-Fallback) via `npm run validate:crossrefs`.
- [x] Slug-Unique erzwingen: keine Doppelungen von `slug:` ueber alle SSOT-Dateien hinweg (Gate: `npm run validate:rp`).

P0: Canon-Core einfrieren
------------------------

- [x] Core-Datei bestaetigen: `novapolis-rp/database-rp/00-admin/memory-bundle.md` ist "immer zuerst laden".
- [x] Core enthaelt nur:
  - Setting/Leitmotiv/Regeln
  - harte Basisfakten zu Hauptpersonen
  - harte Basisfakten zu Hauptorten (D5/C6/E3 + Tunnel)
  - aktive Projekte und offene Faeden (nur Titel + 1 Satz)
- [x] Alles, was nicht "hart" ist, wandert raus in Reference/Narrative.

P0: Lokalitaet stabilisieren (Ortsgraph)
---------------------------------------

- [x] Ortsgraph als Index definieren (minimal): D5 ↔ Tunnel ↔ C6 ↔ Tunnel ↔ E3.
- [x] Pro Ort: Pflichtfelder (Status, Bevoelkerung, Infrastruktur, Verbindungen, Risiken, offene Aufgaben).
- [x] Konsistenzregel: Connections muessen beidseitig passen (z. B. D5 nennt C6, C6 nennt D5).

P1: Chronik / Geschichte stabilisieren
-------------------------------------

- [x] Zeitanker festlegen: Was bedeutet T+0 (Tag/Datum/Uhrzeit-Fenster)?
- [x] Timeline-Datei aus `tbd` holen (mindestens 5 Marker): Start, 2-3 Schluesselereignisse, Ende.
- [x] Scenes-Definition operationalisieren: jede Scene hat
  - Kurzsummary
  - Entscheidungen
  - Konsequenzen / Statusaenderungen
  - Links (Orte/Projekte/Missionslog/Logistik)
- [x] Mindestens 3 Scenes als Chronik-Anker: `scene-2025-10-27-a/b/c` (Inhalt).
- [x] Scenes a/b/c als SSOT-Objekte vollstaendig machen: JSON-Sidecars vorhanden + `database-rp/index.json` referenziert alle drei (verifiziert via `checks_rp_consistency.py --strict`).
- [x] Scene-Frontmatter normalisieren: `characters`/`locations` nutzen Slugs in a/b/c.
- [x] Missionslog als Truth fuer "aktiv/abgeschlossen" benutzen; Scenes verlinken Eintraege.
- [x] Abdeckung erhoehen: erfuellt (aktuell 47 SSOT-Scenes unter `database-rp/06-scenes/`, alle mit Kurzbeschreibung).
- [x] Current-State Snapshot definieren: eine Datei (oder generierter Index), die den "aktuellen Stand" der Welt in 1-2 Seiten abbildet (aktive Projekte, Status Hauptchars, relevante Ressourcen, offene Faeden) und konsistent zu Scenes/Missionslog ist.
- [x] Current-State als Gate: Ableitbarkeit/Validierung des Snapshots gegen Missionslog/Inventare erzwingen.

P1: Curation Backlog → Canon Workflow
------------------------------------

- [x] Aus `database-curated/staging/*.review.md` eine Konfliktliste + FACT?-Liste ziehen.
- [x] Pro FACT?: Zuordnung
  - Core? (ja/nein)
  - Reference-Objekt? (welche Datei)
  - Narrative? (welche Scene)
- [x] RAW/Flags-Inventur: Exporte in `database-raw/99-exports/` vollständig erfasst (Total 50; RAW 33; Flags 17; RAW ohne Flags 16; Flags ohne RAW 0).
- [x] Staging-Baseline neu erzeugt (Canvas-RAW + RAW-Chat: Normalisierung/Chunking/Stats), um Delta- und Review-Läufe reproduzierbar zu machen.
- [x] Promotion-Regel: Erst Decisions, dann SSOT-Edit, dann (optional) Tagging/Review nachziehen.
- [x] Provenienz-Kette vervollstaendigen: `database-curated/staging/manifest.json` um reviewed/final Outputs und Run-Metadaten erweitern (welches Script, welche Version, welche Checksums).
- [x] Final-Gate definieren: Welche Kriterien muessen erfuellt sein, damit reviewed → final promoted wird (mindestens: Validatoren gruen, Konflikte entschieden, SSOT angepasst, Receipt dokumentiert).
- [x] Unresolved-Listen abarbeiten: `database-curated/reviewed/**/unresolved.json` priorisieren und Konflikte in Decisions überführen (aktuell beide unresolved-Dateien leer, keine offenen Konflikte zu überführen).
- [x] Delta/Overlap-Reports geschlossen: Konsolidierung + Rollen-Split in `reports/resolved.md` dokumentiert.
- [x] SSOT-Updates Rollen-Split: C6-Canvas + C6-Logistik-Policy auf Kora/Marven/Arlen synchronisiert (Personenindex war bereits konsistent).
- [x] Delta-Review Batch 1 (chat-export/RAW) entschieden: alle 5 Punkte = C (zusammenführen/prüfen).
- [x] Dedupe/Consolidation: `chat-export-consolidated.normalized.txt` + Dedupe-Report erstellt.
- [x] PDF-Extraktion (low-trust): Texte extrahiert, aber wegen UI-Artefakten als unbrauchbar archiviert (keine Pipeline-Nutzung).

P2: Validatoren / Checks (nach jeder Canon-Welle)
-------------------------------------------------

- [x] Markdownlint scoped: betroffene RP-SSOT-Dateien (Hinweis: `.tmp/**` ist per Config standardmäßig ignored).
- [x] RP-Validatoren: `npm run validate:rp` (RP) und `npm run validate:curated` (Curated), falls Node-Umgebung vorhanden.
- [x] RP-Consistency: `python scripts/checks_rp_consistency.py --strict` (wenn Canon-Dateien angefasst wurden).
- [x] Validator-Gates haerten: RP-Frontmatter (Pflichtfelder je Kategorie) + Crossrefs/Links/Slug-Unique als harte FAILs definieren (nicht nur Best-Effort), damit Drift frueh stoppt.
- (Teilfortschritt) `slug` ist jetzt Pflichtfeld je Kernkategorie (character/location/inventory/project/scene).
- (Teilfortschritt) Crossrefs sind slug-only (kein Basename-/Foldername-Fallback).
- [x] Crossref-Check ausweiten: nicht nur Scenes, sondern auch `dependencies`, Projekt-Owners/Locations, Location-Connections (Fraktions-Slugs als erlaubte Tokens).
- [x] Curated-Validatoren konsolidieren: `validate-curated` nach Staging-Neulauf ausführen und Findings als Fixliste protokollieren (Schema auf genutzte Typen/Status erweitert; Lauf PASS).

Startpaket vor Phase 1 (Fraktionen auf nutzbares Niveau)
---------------------------------------------------------

Ziel
----

- Vor dem eigentlichen Ausbau wird fuer jede Fraktion eine belastbare Mindestbasis hergestellt: Fuehrung, Kernteam, Kernorte, Grundbeziehungen.

Pflichtstandard je Fraktion (MVP)
---------------------------------

- [x] Lead-Rolle gesetzt: Jede Fraktion hat genau 1 aktive Anfuehrung (Anfuehrer:in) als SSOT-Charakter mit klarer Verantwortung und Entscheidungsmandat.
- [x] Charakter-Mindestumfang: mindestens 3 spielbare Charaktere pro Fraktion (inkl. Anfuehrung), jeweils mit Rolle, Motivation, Risiko/Makel, 2 Beziehungen und 1-2 RP-Hooks.
- [ ] Orts-Mindestumfang: mindestens 3 nutzbare Orte pro Fraktion (1 Basis, 1 Betriebs-/Versorgungsort, 1 Konflikt-/Kontaktort) mit Verbindungen/Status.
- [ ] Relations-Mindestumfang: pro Fraktion mindestens 2 aktive Aussenbeziehungen (Status + letzter Kontakt + naechster Trigger).
- [ ] Inventar-Mindestumfang: pro Fraktion ein spielbarer Kernbestand mit kritischen Engpaessen (nicht nur Meta-Huelle).

Priorisierte Ausbau-Reihenfolge (objektiv)
------------------------------------------

- [ ] Welle 1 (niedrigste Character-Abdeckung): `arkologie-a1`, `fluesterkollektiv`, `schienenbund`.
- [ ] Welle 2 (niedrige Character-Abdeckung): `eisenkonklave`, `schattenbund`.
- [ ] Welle 3 (Mittelstand harmonisieren): `haendlerbund`.
- [ ] Welle 4 (Feinschliff/Konsolidierung): `novapolis` (Crossrefs, Inventar-/Relations-Tiefe, offene Sidecars).

Operative Definition fuer Phase 1 (Characters)
----------------------------------------------

- [x] Pro Fraktion zuerst Anfuehrung finalisieren (Slug, Zugehoerigkeit, Standort, Mandat, Stellvertretung/Vertretungsregel).
- [x] Danach 2 weitere Kernrollen anlegen (z. B. Ops/Logistik + Diplomatie/Sicherheit) mit sauberer Aufgabenabgrenzung.
- [x] Character-JSON und Character-MD muessen paarig sein; keine neuen MD-only Charaktere in Phase 1.
- [ ] Jeder neue Charakter verlinkt mindestens 1 Ort und 1 Fraktionsdokument (Dependencies/Crossrefs).
- [ ] Nach jeder Fraktion Kurz-Review: Plausibilitaet, Rollentrennung, keine Duplikatfunktionen.

Abnahmekriterien fuer den Start in Phase 2
------------------------------------------

- [x] Alle 7 Fraktionen haben eine klare aktive Anfuehrung.
- [x] Keine Fraktion liegt unter 3 spielbaren Charakteren.
- [ ] Offene Character-Luecken sind als TODOs priorisiert und terminiert.
- [x] Crossrefs fuer neue Charaktere validierbar (slug-only, keine dangling refs).

Definition of Done (RP Base)
----------------------------

- P0 Decisions sind getroffen (N7, E2/E3, C6 Linien, Energie, Fortschritt, Fraktionen).
- `memory-bundle.md` ist "ruhig" (nur seltene Aenderungen, klarer Scope).
- Mindestens 3 Scenes sind als Chronik-Anker befuellt (nicht nur Platzhalter).
- `database-rp/index.json` ist driftfrei (Scenes/Sidecars/Index konsistent).
- Referenzstandard ist stabil: Slugs als IDs (keine Mischung aus Dateinamen-Token).
- Curated-Provenienz ist nachvollziehbar (staging → reviewed → final mit Run-Metadaten).
- Validatoren/Checks laufen im relevanten Scope gruen.
- Jede Fraktion besitzt mindestens eine aktive, eindeutig benannte Anfuehrung als SSOT-Charakter.
