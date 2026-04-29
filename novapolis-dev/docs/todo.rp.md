---
title: "TODO (Novapolis-RP)"
date: 2025-11-12 08:59
tags: [doc]
stand: 2026-04-29 03:56
update: Der alte RP-Runtime-Typordner `characters/` ist nach vollstaendiger Zielpruefung archiviert; der RP-Boardstand bleibt offen: 0.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260429_035444.md
---
<!-- markdownlint-disable MD012 MD022 MD041 -->
TODO (Novapolis-RP)
-------------------

<!-- Migration: Quelle aus dem frueheren coding-Hub, uebernommen am 2025-10-29 -->
<!-- Relocated aus dem ehemaligen Novapolis-RP Development-Hub nach `novapolis-dev/docs/todo.rp.md` am 2025-10-29 -->

Prioritaetstags (aktiv)
-----------------------

- `Jetzt`: Startpaket, Sphaeren-/Mind-Cluster-SSOT und scheduler-ready Startkorridor fuer den ersten spielbaren Slice.
- `Als naechstes`: Reveal-/Geheimhaltungsregeln und fail-forward Folgekorridor fuer mehrere Slots sauber kanonisieren.
- `Spaeter`: TTS-Block (OGG-Kandidaten + Live-Dialog-Cache) erst nach belastbarem Spielkern ausrollen.

Offene Aufgaben (RP)
--------------------

- Aktuell keine offenen RP-Aufgaben.

Abgeschlossene Eintraege (Bestand)
----------------------------------

- [x] [Jetzt] RP-Runtime auf entity-centric Dossiers nach Option 1 migrieren.
  - Ziel: Vor dem naechsten ERP/RP-Zug soll die Runtime von der flachen Typordnerstruktur auf entitaetszentrierte Dossiers umgestellt werden, solange die aktive Runtime noch klein ist. `sessions/` bleibt top-level; alle entitaetsbezogenen Arbeitsdaten wandern nach `entities/<type>/<slug>/`.
  - Akzeptanzkriterien:
    1) [novapolis-rp/database-curated/staging/rp-runtime/README.md](../../novapolis-rp/database-curated/staging/rp-runtime/README.md), [.github/instructions/rp-docs.instructions.md](../../.github/instructions/rp-docs.instructions.md) und [.github/instructions/mind-cluster.instructions.md](../../.github/instructions/mind-cluster.instructions.md) beschreiben nicht mehr das Relationship-Einzelkantenmodell, sondern den Dossier-Guard,
    2) unter `rp-runtime/entities/` existiert die neue Struktur mit typisierten Namespaces wie `characters/`, `locations/`, `projects/`, `assets/` und `factions/` sowie knappen Templates,
    3) die vorhandenen aktiven Runtime-Traeger aus `characters/`, `mind/`, `inventories/`, `state/` und `relationships/` sind in passende Dossiers migriert, ohne neue unbelegte Entitaeten, Scores, Mengen oder Kanon-Promotions zu erfinden,
    4) `relationships.md` wird pro Entitaet gerichtet als `observer_id -> target_id` gefuehrt; keine neue Standardpraxis fuer eine Datei pro Beziehungskante,
    5) alte Typordner enthalten danach keine aktiven Daten mehr, sondern klar markierte Migrations-/Redirect-Hinweise,
    6) Board, Index, Logs und Checks fuehren denselben Migrationslauf im selben Lauf.
  - Evidenz: Der aktuelle Runtime-Baum war noch klein genug fuer einen klaren Schnitt: [novapolis-dev/archive/quarantine/rp-runtime-characters-legacy-20260429-0229/characters/README.md](archive/quarantine/rp-runtime-characters-legacy-20260429-0229/characters/README.md), [novapolis-rp/database-curated/staging/rp-runtime/mind/README.md](../../novapolis-rp/database-curated/staging/rp-runtime/mind/README.md), [novapolis-rp/database-curated/staging/rp-runtime/inventories/README.md](../../novapolis-rp/database-curated/staging/rp-runtime/inventories/README.md), [novapolis-rp/database-curated/staging/rp-runtime/state/README.md](../../novapolis-rp/database-curated/staging/rp-runtime/state/README.md) und [novapolis-rp/database-curated/staging/rp-runtime/relationships/README.md](../../novapolis-rp/database-curated/staging/rp-runtime/relationships/README.md) fuehrten noch getrennte Typordner.
  - Ergebnis 2026-04-29 02:02: [novapolis-rp/database-curated/staging/rp-runtime/entities/README.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/README.md) ist jetzt die aktive entitaetszentrierte Runtime-Oberflaeche. Figuren-, Mind-, Orts-, Inventar-, Projekt-, Asset-, Fraktions- und Relationship-Arbeitsstaende liegen in Dossiers unter `entities/<type>/<slug>/`; die alten Typordner bleiben nur als Redirect-Flaechen fuer alte Links. Beziehungen laufen als gerichtete Eintraege in `relationships.md` des jeweiligen Observers.
  - Nachtrag 2026-04-29 02:29: Der alte Typordner `characters/` wurde nach Pruefung aller 14 Redirects unter `novapolis-dev/archive/quarantine/rp-runtime-characters-legacy-20260429-0229/characters/` archiviert. Aktive Figuren liegen damit nur noch unter [novapolis-rp/database-curated/staging/rp-runtime/entities/characters/README.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/characters/README.md); der Boardstand bleibt bei `RP=0`.

- [x] [Jetzt] Entitaets-/Mind-Konsolidierungsregel verankern und C6-Runtime-Traeger fuer Hauptpfad nachziehen.
  - Ziel: Vor dem naechsten ERP/RP-Zug sollen Entitaetsdaten und zugehoerige Mind-/Runtime-Daten als gemeinsame Pflichtflaeche festgeschrieben werden; zugleich braucht `C6` fuer den aktuellen Hauptpfad einen aktuellen Runtime-Inventartraeger sowie eine Bewohner-/Vor-Ort-Entitaetenoberflaeche.
  - Akzeptanzkriterien:
    1) die passenden Rule-/Instruction-Flaechen erzwingen, dass vor und nach jeder individuellen Entitaetsaktion Entitaets- und Mind-/Runtime-Daten gemeinsam geladen, konsolidiert und aktualisiert oder explizit als `keine neue Mind-Delta` markiert werden,
    2) `rp-runtime` fuehrt den aktuellen C6-Hauptpfad nicht mehr nur ueber `state/c6.md`, sondern auch mit aktuellem Inventartraeger statt dem verworfenen H-47-Probeinventar,
    3) alle C6-Bewohner und handlungsfaehigen Vor-Ort-Entitaeten sind im Runtime-Baum mindestens als Roster-/Arbeitsstand sichtbar; individuelle Runtime- und Mind-Dateien entstehen fuer Entitaeten mit eigenem SSOT-Mind-Cluster und laufender Handlungsrelevanz,
    4) Board, Index, Logs und Checks fuehren denselben Nachzug im selben Lauf.
  - Evidenz: Der aktuelle Review zeigte Mind-Runtime-Drift gegen Turn 11; [novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md) belegt 27 humanoide Personen in `C6`, [novapolis-rp/database-rp/01-factions/novapolis/02-characters/C6-Bewohner.md](novapolis-rp/database-rp/01-factions/novapolis/02-characters/C6-Bewohner.md) fuehrt den Bewohner-Roster, und [novapolis-rp/database-curated/staging/rp-runtime/inventories/c6.md](novapolis-rp/database-curated/staging/rp-runtime/inventories/c6.md) ist noch als verworfener H-47-Probeanker markiert.
  - Ergebnis 2026-04-29 01:30: [.github/instructions/rp-docs.instructions.md](../../.github/instructions/rp-docs.instructions.md), [.github/instructions/mind-cluster.instructions.md](../../.github/instructions/mind-cluster.instructions.md) und [novapolis-rp/database-curated/staging/rp-runtime/README.md](../../novapolis-rp/database-curated/staging/rp-runtime/README.md) erzwingen jetzt den Entitaets-/Mind-Paarlauf vor und nach individuellen Entitaetsaktionen. [novapolis-rp/database-curated/staging/rp-runtime/inventories/c6.md](../../novapolis-rp/database-curated/staging/rp-runtime/inventories/c6.md) fuehrt den aktuellen C6-Hauptpfad-Bestand, [novapolis-rp/database-curated/staging/rp-runtime/entities/locations/c6/roster.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/locations/c6/roster.md) den Bewohner-/Vor-Ort-Roster und Marei, Marven sowie Arlen liegen jeweils mit Character- und Mind-Runtime vor. Kora/Echo sind auf Turn 11 als `carry_forward_confirmed` konsolidiert; der Index steht wieder bei `RP=0`.

- [x] [Jetzt] Sammelklassen in passende externe Handelsflaechen ausserhalb Novapolis nachziehen.
  - Ziel: Die bereits im Waren-Index geschlossenen Sammelklassen sollen in den verbleibenden passend belegten Handelsdokus ausserhalb von Novapolis sichtbar mitgefuehrt werden, damit externe Handelsoberflaechen denselben Kanon lesen wie Inventar und Waren-Index.
  - Akzeptanzkriterien:
    1) der Nachzug bleibt auf Handelsflaechen mit hartem Inventar- oder Relationsbeleg fuer dieselben Sammelklassen beschraenkt,
    2) keine neue Fraktion oder neue offene Handelsroute wird ohne vorhandenen Deal-/Inventaranker aufgemacht,
    3) aeltere unschaerfe Handelsbegriffe werden nur dort ersetzt oder ergaenzt, wo dieselben Klassen fuer die Fraktion bereits als belegt lesbar sind,
    4) Board, Index und Logs fuehren denselben Nachzug im selben Lauf.
  - Evidenz: Die Suche durch `01-factions/**/06-handel-diplomatie/` zeigt ausserhalb von Novapolis derzeit nur [novapolis-rp/database-rp/01-factions/fluesterkollektiv/06-handel-diplomatie/Handelslog-Fluesterkollektiv.md](novapolis-rp/database-rp/01-factions/fluesterkollektiv/06-handel-diplomatie/Handelslog-Fluesterkollektiv.md) als belastbare Handelsflaeche mit noch unscharfer Formulierung `Informationskanaele`; [novapolis-rp/database-rp/01-factions/fluesterkollektiv/04-inventory/Fluesterkollektiv-inventar.md](novapolis-rp/database-rp/01-factions/fluesterkollektiv/04-inventory/Fluesterkollektiv-inventar.md) fuehrt bereits `Informationsgueter`, `Tarn-/Signaltechnik` und `Batterien` als aktive Fraktionsklassen.
  - Ergebnis 2026-04-29 00:55: [novapolis-rp/database-rp/01-factions/fluesterkollektiv/06-handel-diplomatie/Handelslog-Fluesterkollektiv.md](novapolis-rp/database-rp/01-factions/fluesterkollektiv/06-handel-diplomatie/Handelslog-Fluesterkollektiv.md) fuehrt jetzt die belegten Spezial- und Handelsklassen `Informationsgueter`, `Tarn-/Signaltechnik` und `Batterien` explizit auf der externen Handelsoberflaeche mit, ohne neue Gegenparteien, Lieferfenster oder Mengen zu erfinden. [novapolis-dev/docs/todo.index.md](novapolis-dev/docs/todo.index.md) und die Logs fuehren den Nachzug im selben Lauf wieder auf `RP=0`.

- [x] [Jetzt] Neue Sammelklassen in Warenueberblick T0 und betroffene Handelsdokus nachziehen.
  - Ziel: [novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md](novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md) sowie die direkt betroffenen Handelsdokus unter `01-factions/**/06-handel-diplomatie/` sollen denselben Kanon fuer die frisch ergaenzten Sammelklassen fuehren, damit T0-Lage, Markt-/Relationssicht und Waren-Index nicht wieder auseinanderlaufen.
  - Akzeptanzkriterien:
    1) T0 fuehrt die bereits belegten breiten Handelsklassen nur dort nach, wo dafuer ein aktiver Handels- oder Marktanker vorliegt,
    2) betroffene Handelsdokus ersetzen aeltere Oberbegriffe wie `Informationen` oder `medizinische Versorgung` durch die bereits geschlossenen SSOT-Klassen, ohne freie neue Detailwaren zu erfinden,
    3) der Nachzug bleibt auf bereits belegte Novapolis-/C6-Handelsflaechen beschraenkt,
    4) Board, Index und Logs fuehren denselben Nachzug im selben Lauf.
  - Evidenz: [novapolis-rp/database-rp/00-admin/Waren-Index.md](novapolis-rp/database-rp/00-admin/Waren-Index.md) fuehrt jetzt `Rohmaterialien`, `Medizinische Gueter`, `Informationsgueter`, `Tarn-/Signaltechnik` und `Batterien`; [novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md](novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md) fuehrte diese neuen Sammelklassen noch nicht sichtbar mit; [novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/novapolis-markets.md](novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/novapolis-markets.md) nutzte weiter die aelteren Marktbegriffe `Informationen` und `medizinische Versorgung`, waehrend [novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/Relationslog-Novapolis.md](novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/Relationslog-Novapolis.md) bereits `Rohmaterialien` und `medizinische Gueter` fuehrte.
  - Ergebnis 2026-04-29 00:50: [novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md](novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md) fuehrt jetzt `Rohmaterialien`, `Medizinische Gueter` und `Informationsgueter` explizit als belegte breite Novapolis-/C6-Handels- und Bedarfsklassen auf T0-Ebene. [novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/Relationslog-Novapolis.md](novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/Relationslog-Novapolis.md), [novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/novapolis-markets.md](novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/novapolis-markets.md) und [novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/novapolis-pricebands.md](novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/novapolis-pricebands.md) fuehren denselben Kanon jetzt ebenfalls, ohne freie neue Handelskorridore jenseits der belegten Novapolis-/C6-Oberflaeche zu erfinden.

- [x] [Jetzt] Waren-Index proaktiv um belegte Sammelklassen erweitern.
  - Ziel: [novapolis-rp/database-rp/00-admin/Waren-Index.md](novapolis-rp/database-rp/00-admin/Waren-Index.md) soll vor dem naechsten ERP/RP-Fortschritt nicht nur bereits konkrete Einzelwaren, sondern auch die bereits benutzten breiten Handels- und Inventarklassen fuehren, damit offensichtliche Gueterkorridore nicht bei jedem Folgeschritt erneut in die SSOT gezogen werden muessen.
  - Akzeptanzkriterien:
    1) neue Eintraege bleiben auf bereits belegte Sammelklassen aus aktiven Inventar-, Markt- oder Relations-SSOTs beschraenkt,
    2) keine freien Detailwaren oder Packlisten ohne belegten RP-Anker,
    3) die Hinweise im Waren-Index machen klar, wann breite Sammelklassen zulaessig sind,
    4) Board, Index und Logs fuehren denselben Nachzug im selben Lauf.
  - Evidenz: [novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/Relationslog-Novapolis.md](novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/Relationslog-Novapolis.md) fuehrt `Rohmaterialien` und `medizinische Gueter`; [novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/novapolis-markets.md](novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/novapolis-markets.md) fuehrt breite Marktklassen wie `medizinische Versorgung` und `Informationen`; [novapolis-rp/database-rp/01-factions/fluesterkollektiv/04-inventory/Fluesterkollektiv-inventar.md](novapolis-rp/database-rp/01-factions/fluesterkollektiv/04-inventory/Fluesterkollektiv-inventar.md) fuehrt `Informationsgueter`, `Tarn-/Signaltechnik` sowie `Batterien` innerhalb von Verbrauchsmaterial.
  - Ergebnis 2026-04-29 00:35: [novapolis-rp/database-rp/00-admin/Waren-Index.md](novapolis-rp/database-rp/00-admin/Waren-Index.md) fuehrt jetzt zusaetzlich die Sammelklassen `Rohmaterialien`, `medizinische Gueter`, `Informationsgueter`, `Tarn-/Signaltechnik` und `Batterien`. Die Hinweise erlauben breite Sammelklassen jetzt explizit nur dann, wenn aktive Inventar-, Handels- oder Markt-SSOTs sie bereits als eigenen Gueterkorridor fuehren. [novapolis-dev/docs/todo.index.md](novapolis-dev/docs/todo.index.md) und die Logs fuehren den Nachzug im selben Lauf wieder auf `RP=0`.

- [x] [Jetzt] Neue Warenklassen in betroffene RP-Inventare und Runtime-Traeger nachziehen.
  - Ziel: Die frisch erweiterten Klassen aus [novapolis-rp/database-rp/00-admin/Waren-Index.md](novapolis-rp/database-rp/00-admin/Waren-Index.md) und [novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md](novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md) sollen in den direkt betroffenen Inventar- und Runtime-Traegern denselben Wortschatz fuehren, damit der naechste ERP/RP-Lauf nicht wieder zwischen Katalog, Inventar und Runtime driftet.
  - Akzeptanzkriterien:
    1) betroffene Inventar-SSOTs unter `01-factions/**/04-inventory/` fuehren die neuen Klassen dort sichtbar mit, wo sie bereits als Verbrauchs-, Handels- oder Projektanker belegt sind,
    2) betroffene Runtime-Inventare unter `database-curated/staging/rp-runtime/inventories/` nutzen denselben Kanon-Wortschatz fuer die bereits belegten Klassen,
    3) keine neuen Inventar- oder Runtime-Flaechen werden ohne vorhandenen Beleg geoeffnet,
    4) Board, Index und Logs fuehren denselben Nachzug im selben Lauf.
  - Evidenz: `D5-inventar`, `C6-inventar`, `Novapolis-inventar`, `Haendlerbund-inventar`, `inventories/nordlinie-01.md` und `inventories/draisine-transportmodul.md` fuehren bereits die betroffenen Sachverhalte `Kabelanschnitt`, `Schienenprofil`, `Betonplatten` sowie `Nahrungsmittel`/`Grundbedarfsgueter`, aber noch nicht ueberall im frisch geschlossenen Kanon-Wortschatz.
  - Ergebnis 2026-04-29 00:27: [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md), [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md), [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md) und [novapolis-rp/database-rp/01-factions/haendlerbund/04-inventory/Haendlerbund-inventar.md](novapolis-rp/database-rp/01-factions/haendlerbund/04-inventory/Haendlerbund-inventar.md) fuehren die kanonischen Klassen jetzt dort mit, wo sie bereits belegt waren. [novapolis-rp/database-curated/staging/rp-runtime/inventories/nordlinie-01.md](novapolis-rp/database-curated/staging/rp-runtime/inventories/nordlinie-01.md) und [novapolis-rp/database-curated/staging/rp-runtime/inventories/draisine-transportmodul.md](novapolis-rp/database-curated/staging/rp-runtime/inventories/draisine-transportmodul.md) halten denselben Wortschatz jetzt auch im Runtime-Slice; der Punkt ist nach `markdownlint`, `check_frontmatter` und `validate:rp` wieder geschlossen.

- [x] [Jetzt] Waren-Index und Warenueberblick T0 entlang der aktiven RP-Waren- und Teilelage erweitern.
  - Ziel: Die beiden Admin-SSOTs sollen vor dem naechsten ERP/RP-Lauf die aktuell schon belegten, aber noch nicht sauber gefuehrten RP-passenden Waren- und Teileklassen nachziehen, damit kommende Runtime- und Szenenzuege nicht wieder auf impliziten Sammelbegriffen aufsetzen.
  - Akzeptanzkriterien:
    1) [novapolis-rp/database-rp/00-admin/Waren-Index.md](novapolis-rp/database-rp/00-admin/Waren-Index.md) fuehrt mindestens die bereits belegten und wiederverwendbaren RP-passenden Waren-/Teileklassen aus den aktiven Inventar-, Projekt- und Handels-SSOTs nach,
    2) [novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md](novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md) spiegelt denselben Nachzug auf T0-/Arbeitslageebene, ohne neue Mengenretcons oder freie Weltsummen zu erfinden,
    3) die Erweiterung bleibt evidence-first und fuegt keine blossen Runtime-Arbeitsworte ohne belastbare SSOT-/Log-Anker als neue kanonische Warenklasse ein,
    4) Board, Index und Logs fuehren denselben SSOT-Nachzug im selben Lauf.
  - Evidenz: Die aktiven RP-SSOTs fuehren bereits konkrete, wiederverwendbare Waren- und Teilebegriffe wie `Kabelanschnitt`, `Schienenprofil`, `Betonplatten` sowie den Handelsaustausch `Nahrungsmittel` und `Grundbedarfsgueter`, waehrend der weltweite Waren-Index und der T0-Ueberblick diese Lage bisher nur teilweise oder gar nicht fuehren.
  - Ergebnis 2026-04-29 00:20: [novapolis-rp/database-rp/00-admin/Waren-Index.md](novapolis-rp/database-rp/00-admin/Waren-Index.md) fuehrt jetzt `Kabelanschnitt`, `Schienenprofil`, `Betonplatte`, `Nahrungsmittel (Grundbedarf)` und `Grundbedarfsgueter` als aktive RP-passende Warenklassen. [novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md](novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md) spiegelt denselben Schnitt auf T0-Lageebene, trennt die neuen Warenklassen von blosser Runtime-Satzlogik und haelt `Anschlusssicherung`/`Verbindungsmaterial` bewusst weiter ausserhalb des kanonischen Warenkatalogs.

- [x] [Jetzt] Fraktionsruntime fuer Novapolis und Haendlerbund anlegen und Nordlinie-Komponentenliste pro Reparaturcluster festziehen.
  - Ziel: Die bereits aktiven Fraktionen `Novapolis` und `Haendlerbund` sollen im laufenden Hauptpfad eigene Runtime-Traeger erhalten; zugleich soll der Reparaturbedarf von Nordlinie 01 ueber die bisherige Satzlogik hinaus auf eine erste feste, clusternahe Komponentenliste gezogen werden.
  - Akzeptanzkriterien:
    1) unter `state/` liegen eigene Runtime-Traeger fuer `novapolis` und `haendlerbund`,
    2) beide Traeger bleiben evidence-first und aggregieren nur die im aktuellen Hauptpfad wirklich aktiven Orts-, Projekt- und Inventarachsen,
    3) `inventories/nordlinie-01.md` fuehrt fuer die benannten Reparaturcluster nicht mehr nur Sammelbedarfe, sondern eine erste feste Komponentenlesart aus bestehenden Waren- und Stuetzbaukastenklassen,
    4) angrenzende Runtime-Dateien und Logs verweisen auf denselben neuen Fraktions- und Materialschnitt.
  - Evidenz: `D5`, `C6`, `G7`, `Nordlinie 01`, das Draisine-Modul sowie die Fraktionsinventare von `Novapolis` und `Haendlerbund` sind im aktiven Hauptpfad bereits belegte Laufzeitachsen; bisher fehlen aber eigene Fraktions-States im Runtime-Baum. Fuer Nordlinie 01 liegt der Reparaturbedarf bereits cluster- und materialnah vor, aber noch nicht als erste feste Komponentenliste je Cluster.
  - Ergebnis 2026-04-28 22:52: [novapolis-rp/database-curated/staging/rp-runtime/state/novapolis.md](novapolis-rp/database-curated/staging/rp-runtime/state/novapolis.md) und [novapolis-rp/database-curated/staging/rp-runtime/state/haendlerbund.md](novapolis-rp/database-curated/staging/rp-runtime/state/haendlerbund.md) fuehren jetzt eigene Runtime-Fraktionsstates fuer die aktiven Hauptpfadachsen. [novapolis-rp/database-curated/staging/rp-runtime/inventories/nordlinie-01.md](novapolis-rp/database-curated/staging/rp-runtime/inventories/nordlinie-01.md) fuehrt zusaetzlich eine erste feste Komponentenliste pro Reparaturcluster, darunter feste Arbeitsstuecklisten fuer `Uebergang Engbogen`, `Haltepunktpaar Leitungszug`, `Schottertasche Nordkante`, `Schuttkeil Kontaktseite`, `Randauflage Suedlauf` und `Leitungsaufnahme C6-Vorlauf`.

- [x] [Jetzt] Draisine-Warenscope im Runtime-Traeger entlang bestehender SSOT erweitern und Nordlinie-Reparaturbedarf als eigenen Runtime-Traeger nachziehen.
  - Ziel: Der neue Draisine-Traeger soll nicht bei den vier bereits gebundenen Posten stehenbleiben, sondern die naechsten belegten Gueterklassen aus SSOT sichtbar abgrenzen; zugleich soll der Reparaturbedarf von Nordlinie 01 nicht weiter nur in Szene, State und D5-Bedarfsnotiz verteilt bleiben, sondern einen eigenen Runtime-Traeger nach bestehendem `inventories/`-Muster erhalten.
  - Akzeptanzkriterien:
    1) `inventories/draisine-transportmodul.md` fuehrt neben dem gebundenen Ist-Bestand auch die naechsten SSOT-gebundenen Gueter- und Werkzeugklassen sauber getrennt als noch nicht gebundene Projektklassen,
    2) `inventories/nordlinie-01.md` existiert als eigener Runtime-Traeger fuer den belegten Reparaturbedarf des Tunnelprojekts,
    3) der Nordlinie-Traeger trennt harte Blocker, Folgebedarf je Reparaturflaeche und den bereits ausgeschopften Turn-7/8-Satz von neuen offenen Bedarfen,
    4) `state/nordlinie-01.md` und direkt angrenzende Runtime-Traeger verweisen auf denselben neuen Materialschnitt.
  - Evidenz: Turn 10 und Turn 11 fuehren die gemeinsame Bedarfskalkulation fuer Nordlinie bereits mit `Schweißgeraet`, `DN60`, Anschlusssicherung, Verbindungsmaterial, Nachsicherung, Unterfuetterung, Raeumung und Freiraeumung; im Runtime-Baum fehlt dafuer aber noch ein eigener Inventartraeger. Beim Draisine-Traeger liegen zusaetzlich bereits SSOT-Hinweise auf `Kabelanschnitt` sowie den D5-seitigen Werkzeugkontext vor.
  - Ergebnis 2026-04-28 22:46: [novapolis-rp/database-curated/staging/rp-runtime/inventories/draisine-transportmodul.md](novapolis-rp/database-curated/staging/rp-runtime/inventories/draisine-transportmodul.md) fuehrt jetzt zusaetzlich die naechsten SSOT-gebundenen Projektklassen `Kabelanschnitt`, `Werkzeugkit`, `Werkzeugsatz (Mechanik)`, `Wartungsschluessel` und `Druckmesser` als noch ungebundene Projektumgebung. [novapolis-rp/database-curated/staging/rp-runtime/inventories/nordlinie-01.md](novapolis-rp/database-curated/staging/rp-runtime/inventories/nordlinie-01.md) fuehrt zugleich den eigenen Reparaturtraeger fuer `Schweißgeraet`, `Adapter / Fitting (DN60)`, `Anschlusssicherung`, `Verbindungsmaterial`, Nachsicherung, Unterfuetterung, Raeumkapazitaet und Freiraeumung sowie die Zuordnung auf die benannten Reparaturflaechen. [novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md](novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md) und [novapolis-rp/database-curated/staging/rp-runtime/inventories/d5.md](novapolis-rp/database-curated/staging/rp-runtime/inventories/d5.md) fuehren denselben Schnitt mit.

- [x] [Jetzt] Eigenen Runtime-Traeger fuer das Draisine-Transportmodul im aktiven Nordlinie-Pfad anlegen.
  - Ziel: Der Draisine-Stand soll nicht laenger nur verteilt ueber `scene-log.md`, `state/d5.md`, `state/nordlinie-01.md`, das Projektblatt und D5-Inventar lesbar sein, sondern als eigener Runtime-Traeger nach bestehendem `inventories/`-Muster vorliegen.
  - Akzeptanzkriterien:
    1) unter `novapolis-rp/database-curated/staging/rp-runtime/inventories/` liegt ein eigener Draisine-Traeger statt einer freien Sammelerzaehlung,
    2) der Traeger trennt belegten gebundenen Werkstattbestand, offene Fehlstellen und den vom Draisine-Eigenbedarf getrennten Tunnel-/Nordlinie-Bedarf,
    3) verwendete Warenklassen und Begriffe folgen vorhandener SSOT (`Waren-Index`, `D5-inventar`, `Draisine-Transportmodul`) statt neuen Freitext-Klassen,
    4) die direkt betroffenen Runtime- und Logdateien verweisen auf denselben neuen Traeger.
  - Evidenz: Aktuell gibt es im Runtime-Baum keinen eigenen Draisine-Traeger; der Stand liegt verteilt in `scene-log.md`, `state/d5.md`, `state/nordlinie-01.md`, `inventories/d5.md` sowie im SSOT-Projektblatt `Draisine-Transportmodul.md`. Fuer feste Betraege und spaetere saubere Verbrauchslogik reicht diese Verteilung nicht mehr.
  - Ergebnis 2026-04-28 22:39: `inventories/draisine-transportmodul.md` fuehrt jetzt einen eigenen Runtime-Traeger nach bestehendem Inventar-Muster. Der Traeger trennt belegten Prototypbestand (`Schmieroel`, `Lagerfett (Technik)`, `Sicherungssatz`, `Dichtungsmanschette`), den konservativen Werkstatt-Verbrauchsrahmen und den weiterhin getrennt gefuehrten Nordlinie-/Tunnelbedarf `Schweißgeraet` und `Adapter / Fitting (DN60)`. `state/d5.md`, `state/nordlinie-01.md` und `inventories/d5.md` verweisen im selben Lauf auf diesen Trennschnitt.

- [x] [Jetzt] Turn 10 per Admin-Nachzug auf getrennte Lesart fuer C6-Tunneltrupp und C6-Station ziehen.
  - Ziel: Der aktuelle Folgezug darf nicht so stehenbleiben, als kaeme nur Ronjas D5-Seite mit melderelevanten Reparaturbefunden am Kontaktpunkt an. Der `C6-Tunneltrupp` braucht fuer seine Tunnelhaelfte eigene benannte Arbeitsstellen, waehrend die `C6-Station` unter `Kora` davon getrennt als Ruecklauf- und Innenbetriebsflaeche lesbar bleibt.
  - Akzeptanzkriterien:
    1) `scene-log.md` fuehrt Turn 10 nicht mehr als still einseitige Ronja-Liste, sondern mit eigenem C6-Tunnelbefund,
    2) `state/c6.md` trennt `C6-Tunneltrupp` und `C6-Station` explizit statt beide in einer Sammelflaeche zu verschmelzen,
    3) `state/nordlinie-01.md` benoetigt keinen still reparaturfreien C6-Halbraum mehr, sondern fuehrt die C6-seitigen Arbeitsstellen sichtbar mit,
    4) der Lauf bleibt ein Admin-Nachzug und oeffnet keinen neuen Turn 11.
  - Evidenz: Deine Admin-Anmerkung zeigt die Drift im aktuellen Turn-10-Stand direkt: Wenn nur Ronjas Seite konkrete Befunde mitbringt, wirkt die Tunnelhaelfte Richtung `C6` implizit zu sauber. Genau diese Fehllesart soll jetzt korrigiert werden.
  - Ergebnis 2026-04-28 22:13: `scene-log.md`, `state/c6.md` und `state/nordlinie-01.md` trennen jetzt sauber zwischen `C6-Tunneltrupp` und `C6-Station`. Der Tunneltrupp fuehrt fuer seine Haelfte die Arbeitsstellen `Schuttkeil Kontaktseite`, `Randauflage Suedlauf` und `Leitungsaufnahme C6-Vorlauf`; `Kora` bleibt der getrennte Ruecklauf der Station. Turn 10 steht damit nicht mehr auf einer implizit reparaturfreien C6-Haelfte.

- [x] [Jetzt] Turn 9 nach Admin-Auswertung auf den festgeschriebenen Arbeitsstand zurueckziehen.
  - Ziel: Der bereits ausgespielte Weltzug soll nicht frei fortgeschrieben, sondern auf die ausdrueckliche Admin-Klarstellung synchronisiert werden: C6 arbeitet ebenfalls am Tunnel, Kora bleibt in der Stationsverwaltung, die nicht im Tunnel eingesetzten Gefluechteten erhalten eine sichtbare Stationsfunktion, Mara bleibt in C6 beim Aufbau des H-47-Aussenpostens und G7 bleibt mangels Meldung ohne neue Novapolis-Information.
  - Akzeptanzkriterien:
    1) `scene-log.md` fuehrt Turn 9 mit bilateraler Tunnelarbeit und mindestens bestaetigter Wahrnehmung der beiden Trupps statt mit freiem G7-Weltzug,
    2) `state/c6.md` benennt Kora explizit als Stations- statt Tunnelachse und fuehrt die Gefluechteten ausserhalb des Tunneltrupps mit konkreten Aufgaben,
    3) `state/g7.md` und `characters/mara-quell.md` fuehren keinen aktiven G7-Informations- oder Reaktionsstand fuer Novapolis, solange Mara in C6 bleibt und nichts gemeldet hat,
    4) der Korrekturlauf bleibt bei Admin-Nachzug und oeffnet keinen neuen Turn 10.
  - Evidenz: Deine Admin-Auswertung konkretisiert den bereits laufenden Hauptpfad scharf: D5 ist in Ordnung, C6 arbeitet ebenfalls am Tunnel, Kora verwaltet C6, die Gefluechteten brauchen sichtbare Nicht-Tunnel-Aufgaben, Mara bleibt lore-konform in C6 und G7 hat ohne Meldung keinen neuen Wissensstand.
  - Ergebnis 2026-04-28 21:36: `scene-log.md`, `state/nordlinie-01.md`, `state/c6.md`, `state/g7.md` und `characters/mara-quell.md` fuehren Turn 9 jetzt als Admin-Nachzug statt als freien G7-Weltzug. Die Tunneltrupps aus `D5` und `C6` haben vorsichtige gegenseitige Wahrnehmung, `Kora` bleibt in der Stationsverwaltung, die nicht eingesetzten Gefluechteten tragen den C6-Innenbetrieb, `Mara` bleibt in `C6`, und `G7` bleibt ohne frische Novapolis-Meldung.

- [x] [Jetzt] Turn 9 als offenen Weltzug fuer den aktiven Nordlinie-Hauptpfad ausspielen und die neu betroffenen Runtime-Traeger im selben Lauf anlegen.
  - Ziel: Der naechste RP-Zug soll im Labor nicht nur Ronjas Tunnelperspektive, sondern den gleichzeitig laufenden Weltzustand der direkt angeschlossenen Achsen `D5`, `C6` und `H-47/G7` sichtbar machen, ohne den Hauptpfad zu verlassen oder unbelegte Fernfraktionen frei zu simulieren.
  - Akzeptanzkriterien:
    1) `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md` fuehrt einen einzelnen Turn 9 als offenen Weltzug mit getrennten Teilfenstern fuer Tunnel, D5-Werkstatt, C6-Innenlage und die belegte H-47-/Mara-Kante,
    2) der Zug bleibt evidence-first: kein freier Vollerfolg, keine neue Lieferbehauptung ohne Runtime-/SSOT-Traeger, keine pauschale "alle Fraktionen"-Simulation ausserhalb der direkt belegten Anschlussachsen,
    3) alle in Turn 9 neu aktiv ausgespielten Figuren- oder Ortsachsen besitzen danach die noetigen Runtime-Dateien unter `characters/`, `mind/`, `state/`, `inventories/` oder `relationships/`,
    4) verworfene Probe-Sessions wie `c6-h47-handelsfenster-01` werden nicht heimlich weitergeschrieben, sondern nur ihre belegten Anschlussachsen kontrolliert in den aktuellen Hauptweltzug ueberfuehrt,
    5) TODO-Index, Root-/Modul-DONELOG und Root-Status fuehren denselben neuen RP-Arbeitsstand im selben Lauf nach.
  - Evidenz: `Nordlinie-D5-C6-Index.md` fixiert den Nordlinie-Strang als aktuellen Weltstand, `state/nordlinie-01.md` nennt bereits D5 und C6 als gekoppelte Arbeitsachsen, und C6/H-47 liegt als belegter, aber verworfener Probe-Einstieg vor; fuer einen offenen Weltzug fehlten vor dem Lauf noch die aktiven Runtime-Traeger mindestens fuer `Kora`, `Echo` und eine sauber in den Hauptpfad ueberfuehrte H-47-/Mara-Reaktion.
  - Ergebnis 2026-04-28 21:17: `scene-log.md` fuehrt Turn 9 jetzt als offenen Weltzug ueber `Tunnel`, `D5`, `C6` und `G7/H-47`, ohne freie Lieferungen zu erfinden. Neue Runtime-Traeger fuer `Kora`, `Echo` und `G7` liegen jetzt vor; `state/c6.md` und `characters/mara-quell.md` sind in den aktuellen Hauptpfad nachgezogen. Der Slice bleibt bewusst eng: verdichtete D5-Anforderung, vorbereitete C6-Annahmekante, bestaetigungsorientierter Haltemodus bei Mara/G7.

- [x] [Jetzt] Expliziten Inventar-Diff fuer den kleinen Nordlinie-Turn-7/8-Satz nachziehen.
  - Ziel: Die Runtime-Inventarspur soll nicht nur Endmengen fuehren, sondern den kleinen Behelfssatz aus D5 als turn-scharfen Delta-Block mit klarer Trennung zwischen Lieferung, Einsatz und offener Evidenzgrenze lesbar machen.
  - Akzeptanzkriterien:
    1) `inventories/d5.md` fuehrt einen expliziten Delta-Block fuer Turn 7 und den Restverbrauch in Turn 8,
    2) fuer jeden Delta-Block ist sichtbar, was belegt geliefert, was belegt eingesetzt und was nur teilweise ortsscharf belegt ist,
    3) komponentenscharfe Einsatzorte werden nur dort benannt, wo der Scene-Log sie wirklich traegt,
    4) offene Orts- oder Chargenluecken bleiben ausdruecklich offen statt implizit glattgezogen.
  - Evidenz: Turn 7 belegt reale Teilbereitstellung und Verarbeitung, `inventories/d5.md` fuehrt bisher aber nur den konsolidierten Mengenstand statt eines ausdruecklichen turn-scharfen Inventar-Diffs.
  - Ergebnis 2026-04-28 05:09: `inventories/d5.md` fuehrt jetzt einen expliziten `Turn Delta Ledger` fuer Turn 7 und Turn 8. Turn 7 trennt reale Lieferung, belegten Ersteinsatz und offene Ortsschaerfe; Turn 8 zieht den Restverbrauch ohne neue D5-Lieferung komponentenscharf bis zur `Schottertasche Nordkante` nach. Die verbleibende Evidenzluecke fuer die vollstaendige komponentenscharfe Ortung des gesamten Turn-7-Satzes bleibt sichtbar offen.

- [x] [Jetzt] Evidence-Pflicht fuer ERP/RP explizit als Runtime-Regel verankern.
  - Ziel: Im ERP/RP sollen keine Aussagen mehr als belastbar ausgegeben werden, wenn sie weder durch SSOT noch durch bestehende Runtime-Dateien belegt sind; wenn fuer eine belastbare Aussage eine Runtime-Datei fehlt, muss sie zuerst aus SSOT und Governance abgeleitet angelegt werden.
  - Akzeptanzkriterien:
    1) die agentuebergreifende RP-Instructions-Datei nennt explizit die Regel `keine Aussage ohne Beleg` und trennt zwischen `belegt`, `offen` und `Runtime zuerst anlegen`,
    2) der RP-Agent fuer das Szenenlabor zieht dieselbe Regel fuer ausgespielte Zuege und Admin-Bestaetigungen nach,
    3) die Runtime-README beschreibt die operative Folge: neue belastbare Aussagen brauchen entweder vorhandene Runtime-Evidenz oder vorab angelegte Runtime-Dateien auf Basis der SSOT,
    4) unklare oder nur implizite Ableitungen bleiben STOP oder offen, statt frei ausgespielt zu werden.
  - Evidenz: Die bisherige RP-Governance verbietet bereits freie Kanonisierung und fordert Runtime-Nachzuege, nennt aber die Kernregel `keine Aussage ohne Beleg oder Runtime-Niederschrift` noch nicht als expliziten Standard fuer ERP/RP.
  - Ergebnis 2026-04-28 04:56: [.github/instructions/rp-docs.instructions.md](.github/instructions/rp-docs.instructions.md) fuehrt jetzt agentuebergreifend die Regel `keine Aussage ohne Beleg` samt Pflicht zur SSOT-abgeleiteten Runtime-Anlage, [.github/agents/novapolis-rp-szenenlabor.agent.md](.github/agents/novapolis-rp-szenenlabor.agent.md) zieht dieselbe Logik fuer Turns und Admin-Bestaetigungen nach, und [novapolis-rp/database-curated/staging/rp-runtime/README.md](novapolis-rp/database-curated/staging/rp-runtime/README.md) macht die operative Folge fuer den Runtime-Baum explizit.

- [x] [Jetzt] Runtime-Traegersatz des aktiven Nordlinie-Stands vervollstaendigen.
  - Ziel: Der aktuelle Hauptweltpfad `d5-c6-nordlinie-sanierung-01` soll nicht nur Projekt-, Inventar- und Mind-Spuren fuehren, sondern auch die aktiven Charakter- und Orts-Traeger sauber als Runtime-Dateien abbilden.
  - Akzeptanzkriterien:
    1) `rp-runtime/characters/` fuehrt fuer den aktuellen Hauptweltpfad mindestens `Ronja`, `Reflex`, `Jonas`, `Pahl` und die an Jonas gekoppelte Begleitinstanz `Lumen`,
    2) `rp-runtime/state/` fuehrt einen aktuellen D5-Arbeitsstand fuer Werkstatt-, Freigabe- und Begleitlogik des Nordlinie-Laufs,
    3) Jonas-Lumen-Kopplung und Begleitung sind im Runtime-Stand explizit statt nur implizit aus SSOT ableitbar,
    4) der Nachzug bleibt auf die aktuell belegten Laufzeittraeger beschraenkt; nicht belegte Fraktions- oder Inventarflaechen werden bewusst nicht blind vorgespiegelt.
  - Evidenz: Im aktuellen Hauptweltpfad benennt `state/nordlinie-01.md` die aktiven Figuren `Ronja`, `Reflex`, `Jonas` und `Pahl`, waehrend `rp-runtime/characters/` bislang nur `mara-quell.md` aus einem verworfenen Probe-Einstieg fuehrt; zusaetzlich verlangt `Jonas-Merek.md` die laufende Begleitung durch die gekoppelte Instanz `Lumen`.
  - Ergebnis 2026-04-28 04:50: `rp-runtime/characters/` fuehrt jetzt die aktiven Runtime-Figurenblaetter fuer `Ronja`, `Reflex`, `Jonas`, `Pahl` und `Lumen`; `rp-runtime/state/d5.md` zieht den aktuellen Werkstatt- und Freigabestand nach, `rp-runtime/mind/lumen.md` fuehrt die fehlende Begleitinstanz als eigenen Runtime-Mind-Arbeitsstand, und `rp-runtime/mind/jonas-merek.md` sowie `state/nordlinie-01.md` benennen Jonas-Lumen-Kopplung jetzt explizit. Die aktualisierte Surface-Matrix haelt zugleich fest, dass fuer den aktuellen Hauptpfad keine pauschale Fraktions- oder C6-Vollspiegelung noetig ist, solange dort keine neuen belastbaren Figuren-, Inventar- oder Ortsdeltas ausgespielt werden.

- [x] [Jetzt] Runtime-Mind-Fuehrung fuer RP-Laborpfad und aktive Surface sauber einziehen.
  - Ziel: Der laufende RP-Test soll Mind-/Sphaerenwirkung nicht nur implizit in Szene und State tragen, sondern ueber einen eigenen Runtime-Pfad kontrolliert erfassen; gleichzeitig soll klar werden, welche RP-SSOT-Flaechen wirklich eine Runtime-Entsprechung brauchen und welche bewusst SSOT-only bleiben.
  - Akzeptanzkriterien:
    1) `novapolis-rp/database-curated/staging/rp-runtime/` fuehrt einen eigenen Pfad fuer Mind-/Sphaeren-Arbeitsstaende inklusive README und Vorlage,
    2) der aktive Nordlinie-Kerncast `Ronja`, `Reflex`, `Jonas` und `Pahl` besitzt dort je einen ersten Runtime-Mind-Arbeitsstand oder eine explizite, belegte Ausnahme,
    3) eine RP-Doku im aktiven Scope trennt belastbar zwischen runtime-pflichtigen Surface-Klassen und SSOT-only-Flaechen statt pauschal den ganzen `database-rp` zu spiegeln,
    4) vor der Fortsetzung des ERP-/RP-Laufs ist klar dokumentiert, dass nicht jede RP-Datei vorab als Runtime-Datei angelegt werden muss, sondern nur die aktiv benoetigten Laufzeittraeger plus die kanonischen Vorlagen.
  - Evidenz: `rp-runtime/README.md` kannte zuvor nur `sessions`, `characters`, `relationships`, `inventories` und `state`, waehrend `07-mind-clusters/**` im RP-SSOT fuer den Nordlinie-Kerncast bereits existierte, aber gegenueber dem Laufstand bis Turn 8 nicht als Runtime-Arbeitsstand nachgezogen wurde.
  - Ergebnis 2026-04-28 04:44: `novapolis-rp/database-curated/staging/rp-runtime/mind/` fuehrt jetzt README, Vorlage und die ersten vier Nordlinie-Arbeitsstaende fuer `Ronja`, `Reflex`, `Jonas` und `Pahl`. `novapolis-rp/database-curated/staging/rp-runtime/README.md` zieht den neuen Typ in die Routing-Matrix, und `novapolis-dev/docs/process/rp-runtime-surface-matrix.ssot.md` trennt fuer den gesamten RP-Baum zwischen runtime-pflichtigen Laufzeittraegern und bewusst SSOT-only-Flaechen. Damit ist explizit festgezogen, dass vor dem Weiterspielen nicht der ganze `database-rp` vorgespiegelt werden muss, sondern nur die kanonischen Runtime-Typen plus die aktuell benoetigten Traegerdateien.

- [x] [Jetzt] Runtime-Warenfluss im Nordlinie-Laborpfad von narrativer Teilbereitstellung auf belastbare Mengen- und Restbuchung heben.
  - Ziel: Der kleine D5->Tunnel-Behelfssatz aus dem Nordlinie-Laborpfad soll nicht nur als erzaehlte Teilbereitstellung lesbar sein, sondern als nachvollziehbarer Warenfluss mit belastbarer Mengen- und Restlogik.
  - Akzeptanzkriterien:
    1) [novapolis-rp/database-rp/00-admin/Waren-Index.md](novapolis-rp/database-rp/00-admin/Waren-Index.md) fuehrt die benoetigten Gueterklassen fuer den Nordlinie-/Stationspfad explizit und ohne Sammelnebel,
    2) die Materialarten des Nordlinie-Stuetzbaukastens sind in einer eigenen SSOT als komponentenbasierter Baukasten statt als fertige Lagerstuetzen festgezogen,
    3) [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md) und [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md) fuehren einen konservativen aktuellen Stationsbestand, der Altbestand, Evakuierungsmitnahme und Fundlage sauber trennt,
    4) `scene-log.md` und `inventories/d5.md` fuehren denselben Transferanlass und denselben Zielkontext,
    5) Quelle/Bestandstraeger, Ziel/Verwendung und mindestens eine zaehlbare Groesse pro transferiertem Gut sind benannt,
    6) Einsatz, Verbrauch und verbleibender Restbestand werden getrennt behandelt statt implizit zusammengeschoben,
    7) wenn exakte Zahlen weiter fehlen, bleibt die Luecke explizit als offene Evidenz markiert und wird nicht still mit Scheinpraezision gefuellt.
  - Evidenz: [novapolis-rp/database-rp/00-admin/Waren-Index.md](novapolis-rp/database-rp/00-admin/Waren-Index.md) existiert bereits als Katalog-SSOT; [novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md](novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md) modelliert D5/C6 explizit als fruehe Aufbauphase aus `legacy`, `evac_e3` und `scavenged`; [novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md](novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md) und [novapolis-rp/database-curated/staging/rp-runtime/inventories/d5.md](novapolis-rp/database-curated/staging/rp-runtime/inventories/d5.md) belegen fuer Turn 7 eine reale kleine Teilbereitstellung; [novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01-Stuetzbaukasten.md](novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01-Stuetzbaukasten.md) fixiert die Materialarten als Komponentenklassen statt als fertige Stuetze.
  - Ergebnis 2026-04-27 06:06: Der kleine Turn-7-Satz ist jetzt zwischen Runtime-Log, Runtime-Inventar, [novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01-Stuetzbaukasten.md](novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01-Stuetzbaukasten.md) und [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md) konsistent als kleine Teilbereitstellung mit Transfer, Einsatz und Tunnelrest lesbar. [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md) fuehrt den C6-seitigen Empfangs- und Stagingpfad jetzt ueber den Hauptort [novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md), waehrend [novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6-Schleuse.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6-Schleuse.md) und [novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6-Lagerhalle.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6-Lagerhalle.md) nur noch stabile Kompatibilitaetsziele bleiben. Exakte spaetere C6-Lagerbuchungen ausserhalb dieses kleinen Runtime-Satzes bleiben weiterhin sichtbar offen und werden nicht frei erfunden.

- [x] [Als naechstes] Den Metro-Gesamtrahmen im Warenueberblick nach den Einzelbelegen wieder belastbar verdichten.
  - Ziel: Nach den standort- und fraktionsnahen Nachzuegen soll die Metro-Ebene wieder eine nachvollziehbare, evidence-first verdichtete Lesart erhalten, ohne ungesicherte Summen zu behaupten.
  - Akzeptanzkriterien:
    1) Metro-Ebene verweist nachvollziehbar auf die aktualisierten Einzelbelege,
    2) neutrale Stationslager und Gesamtmengen bleiben nur dort offen, wo Belege fehlen,
    3) Matrix, Warenueberblick und Inventarpfade fuehren dieselbe Aggregationslogik,
    4) die Verdichtung bleibt mit Start-, Folge- und Reveal-SSOT kompatibel.
  - Evidenz: Das Arbeitsledger fuehrt `Metro gesamt` und mehrere neutrale Lagerlagen weiterhin explizit als `tbd`, bis die belastbaren Einzelketten geschlossen sind.
  - Ergebnis 2026-04-18 07:08: `Warenueberblick-T0.md` aggregiert jetzt evidence-first nur die belegten D5/C6-Aufbaupfade, den Haendlerbund-Korridor `G7 <-> C6` und die T0-Bandbreiten der uebrigen externen Fraktionen; neutrale Stationslager und Weltsummen bleiben explizit offen. `rp-metro-warenzuteilung-matrix-2026-03-27.md` und `rp-metro-warenzuteilung-arbeitsledger-2026-03-30.md` fuehren dieselbe Aggregationslogik, ohne freie Summen oder Lagerwelten zu behaupten. Das RP-Board steht damit bei `offen: 0`.

- [x] [Als naechstes] Externe Stations- und Fraktionsinventare im Warenzuteilungsledger dort nachziehen, wo neue Belegketten ueber den reinen Rahmenwert hinausreichen.
  - Ziel: Die externen Fraktionen sollen nur dort von pauschalem `tbd` weggezogen werden, wo echte Belege fuer stationsscharfe oder mengennahe Aussagen vorliegen.
  - Akzeptanzkriterien:
    1) Arkologie, Schienenbund, Haendlerbund, Eisenkonklave, Schattenbund und Fluesterkollektiv bleiben evidence-first,
    2) neue Quantifizierung erfolgt nur mit konkreter Belegkette,
    3) Rahmenwerte und harte Zahlen werden sauber getrennt,
    4) `Warenueberblick-T0.md` und die Fraktionsinventare widersprechen sich danach nicht.
  - Evidenz: `rp-metro-warenzuteilung-arbeitsledger-2026-03-30.md` fuehrt fuer alle externen Fraktionen stationsscharfe Lageranteile und Mengen weiterhin bewusst als `tbd`.
  - Ergebnis 2026-04-18 06:52: `rp-metro-warenzuteilung-matrix-2026-03-27.md` und `rp-metro-warenzuteilung-arbeitsledger-2026-03-30.md` ziehen nur dort ueber den reinen Rahmenwert hinaus, wo die Beleglage es traegt: beim Haendlerbund als konkretem G7-<->-C6-Austauschkorridor mit `H-47`, aktivem Handelsstuetzpunkt `C6` und belegten Austauschklassen `Energie`, `technische Reparaturen`, `Kommunikationszugang` gegen `Nahrungsmittel`, `Filter` und `Grundbedarfsgueter`. Arkologie-A1, Schienenbund, Eisenkonklave, Schattenbund und Fluesterkollektiv bleiben bewusst auf Rahmenwert, weil weiterhin keine belastbaren Mengen- oder Stationsketten vorliegen. Das RP-Board sinkt damit von `2` auf `1` offenen Punkt; uebrig bleibt nur noch der Metro-Gesamtrahmen im Warenueberblick.

- [x] [Als naechstes] Das Verbrauchsdelta Tag 12->13 fuer Novapolis standortscharf zwischen D5 und C6 aufteilen.
  - Ziel: Der belegte Verbrauchsanker fuer Novapolis soll fuer den produktnahen Folgepfad nicht fraktionsweit abstrakt bleiben, sondern auf die beiden aktiven Kernorte heruntergebrochen werden.
  - Akzeptanzkriterien:
    1) `Novapolis-inventar.md`, `D5-inventar.md` und `C6-inventar.md` fuehren dieselbe standortscharfe Lesart,
    2) offene Anteile bleiben sichtbar, wenn Belege fehlen,
    3) Missions- und Materialpfad profitieren direkt von derselben Split-Logik,
    4) keine freie Quantifizierung ohne Belegkette.
  - Evidenz: Das Arbeitsledger fuehrt den standortscharfen Split des Verbrauchsdeltas Tag 12 -> 13 fuer D5 vs. C6 weiterhin explizit als offenen Handentscheid.
  - Ergebnis 2026-04-18 06:44: `Novapolis-inventar.md`, `D5-inventar.md` und `C6-inventar.md` fuehren den Materialverbrauch Tag 12 -> 13 jetzt deckungsgleich als `C6-/Nordlinie-Baustellenverbrauch` bei D5-seitiger Quell-/Transferlast. `rp-metro-warenzuteilung-matrix-2026-03-27.md` und `rp-metro-warenzuteilung-arbeitsledger-2026-03-30.md` ziehen dieselbe konservative Standortlesart nach, ohne neue Mengen, Chargen oder Restbestaende zu setzen. Offen bleiben damit nur die konkrete D5-Abbuchung je Posten, die C6-Lagerbuchung und die Restbestandszahlen nach Tag 13. Das RP-Board sinkt damit von `3` auf `2` offene Punkte; der aelteste offene Punkt wechselt auf die externen Stations- und Fraktionsinventare im Warenzuteilungsledger.

- [x] [Jetzt] Die D5->C6-Transferkette im Warenledger von `tbd` auf echte Belegzeilen fuer Entnahme, Transport, Ankunft und Quittung ziehen.
  - Ziel: Der erste produktrelevante Materiallauf soll nicht nur narrativ und missionsseitig sichtbar sein, sondern im Warenpfad ueber nachvollziehbare Belegschritte geschlossen werden.
  - Akzeptanzkriterien:
    1) Missionslog, D5-Inventar und C6-Inventar fuehren dieselbe Transferkette,
    2) Quelle, Ziel, verantwortlicher Rahmen und Quittungslogik sind benannt,
    3) offene Mengen oder Teilbelege bleiben sichtbar statt implizit gefuellt,
    4) der Schritt bleibt an reale RP-SSOT gebunden und erfindet keine freie Lagerwelt.
  - Evidenz: `novapolis-dev/docs/process/rp-metro-warenzuteilung-arbeitsledger-2026-03-30.md` fuehrt die Transferkette `D5 -> C6` weiterhin ausdruecklich als `tbd` mit offenem Belegpfad.
  - Ergebnis 2026-04-18 06:37: `rp-metro-warenzuteilung-arbeitsledger-2026-03-30.md` uebernimmt den D5->C6-Lauf jetzt explizit als belegte Prozesskette mit Quelle `D5-Materiallager unter dem Bahnsteig und/oder Werkstattbestand`, D5-seitigem `Entnahme/Packen -> Abmeldung`, Transport `manuellerTransport` mit `Tragegestell(ReflexAssist)` sowie C6-seitigem `Eintreffen -> Bestandsaufnahme -> Empfangsbestaetigung -> Baustellenverteilung`. `rp-metro-warenzuteilung-matrix-2026-03-27.md`, `Missionslog-Novapolis.md`, `D5-inventar.md`, `C6-inventar.md` und `Novapolis-inventar.md` fuehren damit denselben konservativen Belegrahmen, waehrend Mengen, Charge und konkrete Lagerbuchung weiter sichtbar offen bleiben. Das RP-Board sinkt damit von `4` auf `3` offene Punkte; der aelteste offene Punkt wechselt auf den standortscharfen Split des Verbrauchsdeltas Tag 12->13.

- [x] [Jetzt] Den Folgekorridor hinter `slot 40` als `slot 41-45` unter demselben Slice-2-Handover-Vertrag ausarbeiten.
  - Ziel: Der spielbare RP-Pfad soll nach der inzwischen belegten fuenften Kampagnenstufe nicht wieder nur als impliziter Folgegedanke stehen bleiben, sondern denselben Resume-, Reveal- und Artefaktrahmen in die naechste Stufe fortsetzen.
  - Akzeptanzkriterien:
    1) hinter `rp-folgekorridor-slot-36-40.ssot.md` liegt eine eigene Folge-SSOT fuer `slot 41-45` oder ein gleichwertig benannter Block vor,
    2) `turn_resume_ready`, Carry-Over-Arbeit und Restdruck bleiben auf demselben Vertrag,
    3) Product-Gate-, Handover- und RP-Quellen zeigen auf denselben Folgepfad,
    4) der Ausbau bleibt evidence-first an belegte Orte und bestehende Start-/Folgekorridore gebunden.
  - Evidenz: `novapolis-dev/docs/process/rp-folgekorridor-slot-36-40.ssot.md` fuehrt unter `Weiterer Ausbau` den naechsten Folgeblock hinter `slot 40` weiterhin nur als offenen Anschluss.
  - Ergebnis 2026-04-18 06:32: `novapolis-dev/docs/process/rp-folgekorridor-slot-41-45.ssot.md` fuehrt jetzt den sechsten Kampagnenblock hinter `slot 40` auf demselben Slice-2-Handover-, Resume- und Reveal-Vertrag fuer `D5`, `C6`, `G7`, `E2` und `F1` fort. `rp-folgekorridor-slot-36-40.ssot.md`, `text-rpg-slice-2-handover-v1.ssot.md` und `text-rpg-product-gate-v1.ssot.md` zeigen im selben Lauf auf denselben neuen Folgepfad statt nur auf einen offenen Anschluss. Das RP-Board sinkt damit von `5` auf `4` offene Punkte, und der aelteste offene Punkt wechselt auf die D5->C6-Transferkette im Warenledger.

- [x] [Als naechstes] `Text-RPG Slice 2 Handover v1` als belastbare Anschluss-SSOT `slot 31-35` oder gleichwertige modulare Episode ausarbeiten.
  - Ziel: Der RP-Produktpfad soll hinter dem ersten belegten Episodenanker nicht wieder nur als Hinweis enden, sondern denselben Start-/Reveal-/Resume-Rahmen in die naechste spielbare Stufe fortsetzen.
  - Akzeptanzkriterien:
    1) hinter `rp-folgekorridor-slot-26-30.ssot.md` liegt eine eigene Anschluss-SSOT fuer `slot 31-35` oder ein explizit gleichwertiger Episodenpfad vor,
    2) der Ausbau bleibt auf belegte Raeume und Kontakte (`D5`, `C6`, `G7`, `E2`, `F1`) oder sauber dokumentierte Anschlussanker beschraenkt,
    3) Missionslog-, Reveal- und Sessionvertragsbezug bleiben fuer denselben Produktpfad lesbar,
    4) Product-Gate-SSOT und Root-Backlog koennen danach denselben neuen Anschluss nennen statt nur den Stand bis `slot 30`.
  - Evidenz: `novapolis-dev/docs/process/rp-folgekorridor-slot-26-30.ssot.md` endet im Abschnitt `Weiterer Ausbau` explizit damit, dass der Pfad hinter `slot 30` als `slot 31-35` oder modular benannte Episode weitergefuehrt werden soll; `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md` fixiert dafuer jetzt den gemeinsamen Handover-Rahmen ueber Root, Agent und Sim.
  - Ergebnis 2026-04-10 00:11: `novapolis-dev/docs/process/rp-folgekorridor-slot-31-35.ssot.md` fuehrt den ersten fachlichen Ausbau hinter `slot 30` jetzt als vierte Kampagnenstufe auf demselben Resume-, Reveal- und Artefaktrahmen aus. `text-rpg-slice-2-handover-v1.ssot.md` und `text-rpg-product-gate-v1.ssot.md` verweisen im selben Lauf auf die neue RP-SSOT; das RP-Board steht damit wieder bei `offen: 0`.

- [x] [Jetzt] Spielstartpaket und Slot-00-05-Korridor als evidence-first Arbeitsblatt zerlegen.
  - Ziel: Die offenen RP-Punkte fuer Startpaket und Mehrslot-Korridor sollen vor der eigentlichen Kanonisierung nicht abstrakt bleiben, sondern als belastbare Arbeitsstruktur mit Beleglage, Reveal-Grenzen und Fail-Forward-Klassen vorliegen.
  - Ergebnis 2026-04-05: `novapolis-dev/docs/process/rp-text-rpg-startpaket-slot-00-05-2026-04-05.md` fuehrt jetzt Primärlinse, Startort, Stakes, Startkern, Reveal-Regeln, mehrere Startoptionen, einen fraktionslosen Pfad, freie Gebietswahl, die Arbeitsfenster `slot 00-05` sowie die Folge-Reihenfolge fuer Mind-Cluster-, Knowledge- und Actions-Ausbau evidence-first zusammen.

- [x] [Jetzt] Spielstartpaket fuer den ersten spielbaren Novapolis-Run als kanonische SSOT anlegen.
  - Ziel: Der spaetere KI-Spielleiter soll einen eindeutigen Startpunkt mit Ort, Zeitpunkt, Stakeholdern und erstem Entscheidungsraum bekommen statt nur verteilter Lore-, Missions- und Inventaranteile.
  - Akzeptanzkriterien:
    1) mehrere Startoptionen sind explizit benannt: mindestens `Novapolis-Default`, `Fraktionsstart` und `Fraktionslos / Freie Gruppen`,
    2) Startbereich und Fraktionsmodus sind getrennt waehlbar; mindestens die belegten Kernraeume und Neutral-/Transitbereiche sind als Auswahlklassen sichtbar,
    3) der Start verweist auf bestehende Missions-, Orts-, Inventar-, Knowledge- und Mind-Cluster-SSOTs statt Inhalte zu doppeln,
    4) offene Luecken im Startpaket bleiben sichtbar als `tbd` oder eigener Folgepunkt,
    5) der erste Slice ist als belastbarer Einstieg fuer Agent, Sim und spaetere Replay-/TTS-Pfade lesbar.
  - Arbeitspakete laut Arbeitsblatt:
    1) Primärlinse `Ronja/Reflex in D5` gegen Parallelfaden `Kora/Echo in C6` festziehen,
    2) Mehrfachstart-Matrix `Default-Slice | Fraktionsstart | Fraktionslos | Neutralstart` festziehen,
    3) Startbereich und Fraktionsmodus sauber trennen,
    4) Reveal-Grenzen `pc_visible|allies_only|world_only|rumor` direkt am Startbogen benennen,
    5) offene Kanon-Luecken sichtbar halten (keine stillen Auffuellungen).
  - Ergebnis 2026-04-05: `novapolis-dev/docs/process/rp-startbogen-novapolis-d5.ssot.md` ist jetzt der kanonische Default-Start fuer den ersten Novapolis-Run; `novapolis-dev/docs/process/rp-startbogen-novapolis-c6.ssot.md` grenzt `C6` als eigenen parallelen Novapolis-Start ab; `novapolis-dev/docs/process/rp-start-chooser.ssot.md` fuehrt beide zusammen mit Fraktions- und fraktionslosen Starts auf derselben Auswahl- und Reveal-Schicht.
  - Evidenz: `novapolis-dev/docs/process/rp-text-rpg-startpaket-slot-00-05-2026-04-05.md`, `novapolis-dev/docs/process/rp-start-chooser.ssot.md`, `novapolis-dev/docs/process/rp-startbogen-novapolis-d5.ssot.md`, `novapolis-dev/docs/process/rp-startbogen-novapolis-c6.ssot.md`, `novapolis-dev/docs/specs/annotation-spec.md`, `novapolis-dev/docs/specs/scheduler-spec.md`, `Missionslog-Novapolis.md`, `D5.md`, `C6.md`, `Fraktionen-Taxonomie.md`, `Stationskontroll-Matrix.md`, `Metrokarte-T0.md`, `Freie-Gruppen-inventar.md`.

- [x] [Als naechstes] Verbleibende Fraktionskerne `A1`, `B2`, `H12`, `F9` und `K4` von `framing_start` auf echte Startboegen heben.
  - Ziel: Nach D5, C6, G7 und A2 sollen auch die verbleibenden belegten Fraktionskerne einen ersten belastbaren Entscheidungsraum erhalten, statt nur als auswählbarer Rahmenknoten sichtbar zu sein.
  - Akzeptanzkriterien:
    1) jeder Kern fuehrt mindestens Basisstation, Startkern, Stakes und ersten Entscheidungsraum,
    2) Rahmenstart und voll tragfaehiger Start bleiben im Chooser sichtbar getrennt,
    3) neue Startboegen bleiben an echte Orts-, Fraktions- und Topologie-SSOTs gebunden,
    4) offene lokale Luecken werden pro Start explizit markiert statt aufgefuellt.
  - Ergebnis 2026-04-05: `rp-startbogen-arkologie-a1.ssot.md`, `rp-startbogen-schienenbund-b2.ssot.md`, `rp-startbogen-eisenkonklave-h12.ssot.md`, `rp-startbogen-schattenbund-f9.ssot.md` und `rp-startbogen-fluesterkollektiv-k4.ssot.md` heben jetzt alle verbleibenden Kernstationen auf echte Minimal-Startboegen; `rp-start-chooser.ssot.md` fuehrt damit alle derzeit freigegebenen Kernstationen als `full_slice`.
  - Evidenz: `novapolis-dev/docs/process/rp-start-chooser.ssot.md`, `Fraktionen-Taxonomie.md`, `Stationskontroll-Matrix.md`, `Metrokarte-T0.md`, `A1.md`, `B2.md`, `H12.md`, `F9.md`, `K4.md`, `novapolis-dev/docs/process/rp-startbogen-arkologie-a1.ssot.md`, `novapolis-dev/docs/process/rp-startbogen-schienenbund-b2.ssot.md`, `novapolis-dev/docs/process/rp-startbogen-eisenkonklave-h12.ssot.md`, `novapolis-dev/docs/process/rp-startbogen-schattenbund-f9.ssot.md`, `novapolis-dev/docs/process/rp-startbogen-fluesterkollektiv-k4.ssot.md`.

- [x] [Jetzt] Mind-Cluster- und Sphaeren-SSOT fuer die Kernbesetzung des Startkorridors ausrollen.
  - Ziel: Beziehungen, geistnahe Zustaende und verdeckte Dynamik der ersten spielrelevanten Figuren duerfen nicht implizit im Fliesstext bleiben, sondern sollen im geregelten Sphaerenmodell vorliegen.
  - Akzeptanzkriterien:
    1) alle Kernfiguren und unmittelbaren Fraktionskontakte des ersten Slice besitzen je eine eigene `*-mind-cluster.md`,
    2) observer-/target-Richtung, Pflichtfelder, Reason-Codes und angewandte Regeln sind validator-konform,
    3) Charakterdateien verweisen nur noch auf diese SSOTs statt beziehungsnahe Doppelungen zu tragen,
    4) mindestens die startrelevanten Vertrauens-, Loyalitaets-, Bedrohungs- und Konfliktachsen sind belegt oder bewusst `tbd` markiert.
  - Priorisierte Reihenfolge fuer den Startkorridor:
    1) Reflex,
    2) Jonas,
    3) Pahl,
    4) Kora,
    5) Echo.
  - Ergebnis 2026-04-05: Fuer `Reflex`, `Jonas`, `Pahl`, `Kora` und `Echo` liegen jetzt eigene `*-mind-cluster.md`-SSOTs vor; die Charakterdateien verweisen auf diese Cluster statt Beziehungs- und Verhaltensduplikate mitzuschleppen.
  - Evidenz: `novapolis-dev/docs/process/rp-text-rpg-startpaket-slot-00-05-2026-04-05.md`, `novapolis-rp/database-rp/00-admin/mind-cluster-template.md`, `.github/instructions/mind-cluster.instructions.md`, `novapolis-rp/database-rp/01-factions/novapolis/07-mind-clusters/reflex-mind-cluster.md`, `jonas-merek-mind-cluster.md`, `pahl-brenner-mind-cluster.md`, `kora-malenkov-mind-cluster.md`, `echo-mind-cluster.md`.

- [x] [Jetzt] Scheduler-ready Knowledge-/Actions-Abdeckung fuer Startorte, Missionsanker und Kernfiguren schliessen.
  - Ziel: Der erste Slice soll nicht nur erzaehlbar, sondern aus aktiver SSOT auch plan- und simulierbar sein.
  - Akzeptanzkriterien:
    1) die startrelevanten Orte, Missionen und Figuren fuehren die benoetigten `knowledge:`- und `actions:`-Felder in der aktiven SSOT,
    2) Dauer, Locks, Ressourcen, Interruptfaehigkeit und Reveal-Kanaele reichen fuer einen ersten Scheduler-/GM-Lauf aus,
    3) Knowledge-Eintraege unterscheiden sichtbar zwischen Weltwahrheit, Gruppenwissen und PC-Sicht,
    4) der Startkorridor benoetigt fuer seine Kernentscheidungen keine impliziten Chat-Absprachen ausserhalb der SSOT.
  - Startkorridor-Scope:
    1) `D5.md`,
    2) `C6.md`,
    3) `Missionslog-Novapolis.md`,
    4) `Nordlinie-01.md`,
    5) die startrelevanten Charakterdateien des Kerncasts.
  - Ergebnis 2026-04-05: `D5.md`, `C6.md`, `Nordlinie-01.md` sowie der Kerncast `Ronja/Reflex/Jonas/Pahl/Kora/Echo` fuehren jetzt startkorridor-taugliche `knowledge:`- und `actions:`-Bloecke mit Reveal-Kanaelen, Voraussetzungen, Outputs und Risiken; `Missionslog-Novapolis.md` bleibt der Missionsanker fuer die D5-C6-Kette.
  - Evidenz: `novapolis-dev/docs/process/rp-text-rpg-startpaket-slot-00-05-2026-04-05.md`, `novapolis-dev/docs/specs/annotation-spec.md`, `D5.md`, `C6.md`, `Nordlinie-01.md`, `Missionslog-Novapolis.md`, `Ronja-Kerschner.md`, `Reflex.md`, `Jonas-Merek.md`, `Pahl-Brenner.md`, `Kora-Malenkov.md`, `Echo.md`.

- [x] [Als naechstes] Reveal-, Geheimhaltungs- und Wissensgrenzen fuer Spielleitung vs. PC-Sicht als Startbogen-Matrix festziehen.
  - Ziel: Die KI-Spielleitung soll spaeter eindeutig wissen, was Weltwahrheit bleibt, was nur als Geruecht auftauchen darf und was der PC in welchem Kanal sehen darf.
  - Akzeptanzkriterien:
    1) fuer den Startbogen ist pro Informationsklasse geklaert, ob sie `world_only`, `npc_only`, `pc_visible`, `allies_only`, `rumor` oder `log/reflex`-gebunden ist,
    2) Reveal-Pfade ueber Funk, Log, Reflex-Link, Geruecht oder direkte Beobachtung sind explizit benannt,
    3) geheime Sphaeren-/Mind-Cluster-Daten und verdeckte Fraktionslagen bleiben klar von PC-Text getrennt,
    4) die Matrix verweist auf reale Orte, Figuren und Missionsanker statt nur auf abstrakte Regeltexte.
  - Ergebnis 2026-04-05: `novapolis-dev/docs/process/rp-startkorridor-reveal-matrix.ssot.md` trennt jetzt fuer `D5`, `C6`, `Nordlinie`, Missionslog und Mind-Cluster-Daten sauber zwischen `pc_visible`, `allies_only`, `npc_only`, `world_only`, `rumor` und `log/reflex` samt Reveal-Pfaden und Guardrails.
  - Evidenz: `novapolis-dev/docs/process/rp-text-rpg-startpaket-slot-00-05-2026-04-05.md`, `annotation-spec.md`, `novapolis-dev/docs/process/rp-startkorridor-reveal-matrix.ssot.md`; die Canvas-Rescue-Unterlagen fuehren `[FACT] [KNOWLEDGE]`, `[FACT] [SECRECY]`, `[FACT] [FR-KNOWLEDGE]`, `[FACT] [WORLD-TURNS]` und sind damit jetzt in eine aktive Startbogen-Matrix ueberfuehrt.

- [x] [Als naechstes] Externe Fraktionsstarts und fraktionslosen Neutralstart von Rahmenstart auf echte Startboegen heben.
  - Ziel: Mehrere Startoptionen sollen nicht nur als Auswahlidee existieren, sondern fuer mindestens einen externen Fraktionsstart und einen fraktionslosen Start einen belastbaren ersten Entscheidungsraum besitzen.
  - Akzeptanzkriterien:
    1) mindestens ein externer Fraktionsstart besitzt Basisstation, Startkern, Stakes und ersten Entscheidungsraum,
    2) der fraktionslose Start fuehrt einen neutralen oder transitiven Startbereich plus Anschlusslogik an Kontakt, Handel, Gefahr oder Fraktion,
    3) Rahmenstarts und voll tragfaehige Starts bleiben sichtbar getrennt,
    4) die Auswahl `Bereich frei waehlen` bleibt an reale Stations- und Kontroll-SSOTs gebunden.
  - Ergebnis 2026-04-05: `novapolis-dev/docs/process/rp-startbogen-haendlerbund-g7.ssot.md` hebt `G7` als ersten externen Fraktionsstart auf `full_slice`; `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-a2.ssot.md` liefert den ersten fraktionslosen Neutralstart in `A2`; `novapolis-dev/docs/process/rp-start-chooser.ssot.md` bindet beide an dieselben Start- und Gebietswahl-Regeln.
  - Evidenz: `Fraktionen-Taxonomie.md`, `Stationskontroll-Matrix.md`, `Metrokarte-T0.md`, `Freie-Gruppen-inventar.md`, `G7.md`, `novapolis-dev/docs/process/rp-startbogen-haendlerbund-g7.ssot.md`, `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-a2.ssot.md`, `novapolis-dev/docs/process/rp-start-chooser.ssot.md`.

- [x] [Jetzt] Erweiterten Mind-Cluster-Rollout fuer Anschlusscast und externe Full-Slice-Kerne nachziehen.
  - Ziel: Der Mind-Cluster-Unterbau soll nicht beim ersten Novapolis-Startkorridor enden, sondern auch den aktuell freigegebenen Anschlusscast und die externen Full-Slice-Kerne als beziehungsnahe SSOT abdecken.
  - Akzeptanzkriterien:
    1) fuer den direkten Anschlusscast `Arlen`, `Lumen`, `Marven`, `Marei`, `Lyra` und `Senn` liegen eigene `*-mind-cluster.md`-Dateien oder bewusst dokumentierte Ausnahmen vor,
    2) fuer die Kernfiguren der Startboegen `A1`, `B2`, `H12`, `F9` und `K4` liegen je eigene Mind-Cluster-SSOTs vor,
    3) Charakterdateien mit beziehungsnahen Doppelungen oder Verhaltenssignaturen verweisen auf diese SSOTs statt dieselben Bloecke lokal zu tragen,
    4) Startboegen und Arbeitsblatt fuehren keine veralteten Hinweise mehr auf bereits geschlossene Mind-Cluster-Luecken.
  - Scope laut Startboegen und aktuellem Anschlusscast:
    1) `Arlen-Dross.md`, `Lumen.md`, `Marven-Kael.md`, `Marei-Falk.md`, `Lyra-Hest.md`, `Senn-Daru.md`,
    2) `Liora-Navesh.md`, `Nera-Vossen.md`, `Borin-Khade.md`,
    3) `Varek-Solun.md`, `Kaspar-Dorn.md`, `Yara-Kest.md`,
    4) `Helia-Vorn.md`, `Rian-Kord.md`, `Tera-Solm.md`,
    5) `Nyra-Vehl.md`, `Jarek-Voan.md`, `Sera-Nol.md`,
    6) `Iris-Vey.md`, `Corin-Mael.md`, `Sera-Kaal.md`.
  - Ergebnis 2026-04-05: fuer den direkten Anschlusscast `Arlen`, `Lumen`, `Marven`, `Marei`, `Lyra` und `Senn` sowie fuer die Full-Slice-Kerne von `A1`, `B2`, `H12`, `F9` und `K4` liegen jetzt eigene `*-mind-cluster.md`-Dateien vor; die Charakter-SSOTs verweisen auf diese Cluster, und die veralteten D5/C6-Arbeitsluecken sind gestrichen.
  - Evidenz: `novapolis-dev/docs/process/rp-startbogen-haendlerbund-g7.ssot.md`, `rp-startbogen-arkologie-a1.ssot.md`, `rp-startbogen-schienenbund-b2.ssot.md`, `rp-startbogen-eisenkonklave-h12.ssot.md`, `rp-startbogen-schattenbund-f9.ssot.md`, `rp-startbogen-fluesterkollektiv-k4.ssot.md`, `novapolis-dev/docs/process/rp-text-rpg-startpaket-slot-00-05-2026-04-05.md`, `.github/instructions/mind-cluster.instructions.md`.

- [x] [Als naechstes] Ersten spielbaren Folgekorridor `slot 00-05` mit Konsequenzklassen und Fail-Forward sauber kanonisieren.
  - Ziel: Aus dem Startpaket soll ein mehrslotiger Spielbogen werden, der Entscheidungen, Konsequenzen, Ressourcenfolgen und Eskalationen nachvollziehbar traegt, ohne bei einem Fehlentscheid sofort in Sackgassen zu enden.
  - Akzeptanzkriterien:
    1) mindestens die ersten 3-5 spielbaren Entscheidungsfenster sind als Folgekorridor mit moeglichen Konsequenzklassen beschrieben,
    2) Ressourcen-, Missions-, Beziehungs- und Gefahrenfolgen sind pro Fenster sichtbar benannt,
    3) harte Dead Ends werden vermieden; stattdessen existieren dokumentierte Fail-Forward-Pfade,
    4) der Korridor bleibt mit Missionslog, Inventaren, Knowledge und Mind-Clustern kompatibel.
  - Vorstruktur laut Arbeitsblatt:
    - Slot 00: D5 Wartungsauftrag/Wartungsgang,
    - Slot 01: D5 Terminal/Port/System-Link,
    - Slot 02: D5 Werkstatt-/Funk-Weiterlauf und Pahl-Kontext,
    - Slot 03: C6 Sicherung/Markierung als Parallelfaden,
    - Slot 04: C6 Abschluss/Übergabe als kontrollierter Reveal,
    - Slot 05: D5 Grundriss-/Nordlinie-Entscheidungsfenster.
  - Ergebnis 2026-04-05: `novapolis-dev/docs/process/rp-folgekorridor-slot-00-05.ssot.md` kanonisiert jetzt die Slots `00-05` mit primaerer Linse, Konsequenzklassen, fail-forward-faehigen Ausweichpfaden sowie einem Missions-/Reveal-/Persistenzvertrag; das Arbeitsblatt verweist nur noch auf diese Folge-SSOT.
  - Evidenz: `novapolis-dev/docs/process/rp-text-rpg-startpaket-slot-00-05-2026-04-05.md`, `novapolis-dev/docs/process/rp-folgekorridor-slot-00-05.ssot.md`, `scheduler-spec.md`, `Missionslog-Novapolis.md`, `Nordlinie-01.md`.

- [x] [Als naechstes] Lokale Tiefenschaerfe und Nebenstart-Hooks fuer die Full-Slice-Kerne an die neuen Mind-Cluster anbinden.
  - Ziel: Die bereits freigegebenen Full-Slice-Starts sollen nicht bei einem reinen Minimalbogen stehen bleiben, sondern pro Kernstation belastbare Unterraeume, lokale Konfliktherde und anschlussfaehige Nebenstart-Linsen erhalten.
  - Akzeptanzkriterien:
    1) die noch duennen Kernstationen `A1`, `H12`, `B2`, `F9` und `K4` fuehren konservative lokale Unterraeume oder Funktionszonen statt nur `tbd`,
    2) die zugehoerigen Startboegen benennen pro Kern mindestens eine lokale Leitungs-, Handels- und Sicherheitslinse,
    3) die neuen Mind-Cluster-SSOTs der Kernfiguren sind im Startkontext explizit angebunden,
    4) Nebenstart-Hooks bleiben als Hook markiert und werden nicht still zu voll ausgearbeiteten Zusatzstartboegen promoted.
  - Ergebnis 2026-04-05: `A1.md`, `H12.md`, `B2.md`, `F9.md` und `K4.md` fuehren jetzt belastbare Status-, Bevoelkerungs-, Infrastruktur- und Tiefenschaerfe-Bloecke; die Startboegen von `A1/H12/B2/F9/K4` sowie `G7` binden ihre Mind-Cluster explizit an und nennen lokale Unterraeume sowie konservative Nebenstart-Hooks.
  - Evidenz: `A1.md`, `H12.md`, `B2.md`, `F9.md`, `K4.md`, `rp-startbogen-arkologie-a1.ssot.md`, `rp-startbogen-eisenkonklave-h12.ssot.md`, `rp-startbogen-schienenbund-b2.ssot.md`, `rp-startbogen-schattenbund-f9.ssot.md`, `rp-startbogen-fluesterkollektiv-k4.ssot.md`, `rp-startbogen-haendlerbund-g7.ssot.md`, die zugehoerigen `*-mind-cluster.md`-Dateien.

- [x] [Als naechstes] Reveal-Matrix auf die weiteren Full-Slice- und Neutralstarts ausdehnen.
  - Ziel: Die KI-Spielleitung soll nicht nur fuer `D5/C6`, sondern auch fuer die freigegebenen weiteren Startgebiete klar unterscheiden koennen, was unmittelbarer Startkontext, internes Gruppenwissen, Geruecht oder reine Weltlage bleibt.
  - Akzeptanzkriterien:
    1) mindestens `A1`, `B2`, `H12`, `F9`, `K4` sowie die angrenzenden Startpfade `G7` und `A2` sind mit Reveal-Klassen dokumentiert,
    2) pro Startgebiet sind lokale Sichtbarkeit, interne Freigabelogik und `world_only`-Grenzen erkennbar,
    3) die Matrix verweist auf reale Startboegen und Orts-SSOTs statt freie Metaregeln zu wiederholen,
    4) rohe Mind-Cluster- oder verdeckte Fraktionslagen bleiben auch in der erweiterten Matrix strikt aus dem PC-Text getrennt.
  - Ergebnis 2026-04-05: `novapolis-dev/docs/process/rp-startgebiete-reveal-matrix.ssot.md` fixiert jetzt Reveal-, Geheimhaltungs- und Wissensgrenzen fuer `A1`, `B2`, `H12`, `F9`, `K4`, `G7` und `A2` samt Pfaden `pc_visible`, `allies_only`, `world_only` und `rumor`.
  - Evidenz: `rp-startbogen-arkologie-a1.ssot.md`, `rp-startbogen-schienenbund-b2.ssot.md`, `rp-startbogen-eisenkonklave-h12.ssot.md`, `rp-startbogen-schattenbund-f9.ssot.md`, `rp-startbogen-fluesterkollektiv-k4.ssot.md`, `rp-startbogen-haendlerbund-g7.ssot.md`, `rp-startbogen-freie-gruppen-a2.ssot.md`, `A1.md`, `B2.md`, `H12.md`, `F9.md`, `K4.md`, `G7.md`, `Stationskontroll-Matrix.md`, `Metrokarte-T0.md`.

- [x] [Als naechstes] Folgekorridor hinter `slot 05` auf echte Slots fuer Tunnel, Materiallauf und Aussenkontakt ausbauen.
  - Ziel: Der erste Mehrslot-Korridor soll nach der internen Startphase nicht abstrakt abbrechen, sondern in belegte Folge-Slots fuer Nordlinie, Materiallauf, C6-Empfang und den ersten Aussenkontakt uebergehen.
  - Akzeptanzkriterien:
    1) mindestens `slot 06-10` sind als Folge-SSOT beschrieben,
    2) Tunnel-/Projektarbeit, Materiallauf und Aussenkontakt sind als getrennte Entscheidungsfenster sichtbar,
    3) der Folgekorridor bleibt kompatibel mit Missionslog, Reveal-Matrix und bestehenden Startboegen,
    4) die neue Folgeform fuehrt Schwerpunktverzweigungen statt harter Dead Ends ein.
  - Ergebnis 2026-04-05: `novapolis-dev/docs/process/rp-folgekorridor-slot-06-10.ssot.md` fuehrt jetzt Slots fuer Nordlinie-Priorisierung, den belegten Materiallauf `D5 -> C6`, C6-Empfang/Verteilung, das Kontaktfenster `G7 <-> C6` und die anschliessende Schwerpunktwahl nach innen oder aussen.
  - Evidenz: `rp-folgekorridor-slot-00-05.ssot.md`, `rp-folgekorridor-slot-06-10.ssot.md`, `rp-startbogen-haendlerbund-g7.ssot.md`, `rp-startbogen-freie-gruppen-a2.ssot.md`, `Missionslog-Novapolis.md`, `Nordlinie-01.md`, `D5.md`, `C6.md`, `G7.md`.

- [x] [Als naechstes] Langzeit-Folgekorridor hinter `slot 10` als erste echte Schwerpunktfolge kanonisieren.
  - Ziel: Der Produktpfad soll nach der ersten Innen-/Aussenwahl nicht abbrechen, sondern belastbare Folge-Slots fuer Langzeitkosten, Puffernutzung und Schwerpunktsetzung fuehren.
  - Akzeptanzkriterien:
    1) mindestens `slot 11-15` sind als eigene Folge-SSOT beschrieben,
    2) Innen-, Aussen- und Pufferpfad sind als unterschiedliche Schwerpunktentscheidungen sichtbar,
    3) die Folge-Slots bleiben an bestehende Orts-, Reveal- und Missions-SSOTs gebunden,
    4) Langzeitfolgen laufen ueber Druck, Kosten und Spezialisierung statt ueber harte Dead Ends.
  - Ergebnis 2026-04-05: `novapolis-dev/docs/process/rp-folgekorridor-slot-11-15.ssot.md` fuehrt jetzt Langzeitfolgen fuer Nordlinie-/Materialpfad, neutrale Pufferknoten `A2/B1/C3`, Aussenkontakt `G7` und die erste dauerhafte Schwerpunktwahl.
  - Evidenz: `rp-folgekorridor-slot-06-10.ssot.md`, `rp-folgekorridor-slot-11-15.ssot.md`, `rp-startbogen-freie-gruppen-a2.ssot.md`, `rp-startbogen-haendlerbund-g7.ssot.md`, `A2.md`, `B1.md`, `C3.md`, `Missionslog-Novapolis.md`, `Nordlinie-01.md`, `Metrokarte-T0.md`.

- [x] [Als naechstes] Neutrale Pufferknoten `A2`, `B1` und `C3` als lokale Orts-SSOTs verdichten.
  - Ziel: Der fraktionslose und mobile Pfad soll nicht nur ueber abstrakte Stationscodes laufen, sondern fuer die ersten Pufferknoten konservative Ortsanker mit Risiko- und Anschlusslogik besitzen.
  - Akzeptanzkriterien:
    1) `A2`, `B1` und `C3` liegen als eigene Orts-SSOTs vor,
    2) jede Datei fuehrt Status, Infrastruktur, Risiken und eine minimale lokale Tiefenschaerfe ohne freie NPC-Erfindung,
    3) `rp-startbogen-freie-gruppen-a2.ssot.md` bindet diese Orts-SSOTs explizit an,
    4) Reveal- und Folgekorridor-SSOTs koennen die Knoten ohne implizite Leerstellen referenzieren.
  - Ergebnis 2026-04-05: `novapolis-rp/database-rp/03-locations/A2.md`, `B1.md` und `C3.md` fuehren jetzt konservative Orts-SSOTs fuer aktive bzw. teilaktive Neutralpuffer; der A2-Startbogen und die Startgebiete-Reveal-Matrix binden diese Knoten explizit an.
  - Evidenz: `A2.md`, `B1.md`, `C3.md`, `rp-startbogen-freie-gruppen-a2.ssot.md`, `rp-startgebiete-reveal-matrix.ssot.md`, `Metrokarte-T0.md`, `Stationskontroll-Matrix.md`, `A1.md`, `B2.md`.

- [x] [Als naechstes] Weitere Neutralstarts `B1` und `C3` von Orts-SSOT auf eigene Startboegen heben.
  - Ziel: Der mobile/fraktionslose Produktpfad soll nach `A2` nicht auf einen einzigen Neutralstart beschraenkt bleiben, sondern fuer den Vorpuffer `B1` und den teilaktiven Schwellenraum `C3` eigene belastbare Einstiegsfenster besitzen.
  - Akzeptanzkriterien:
    1) fuer `B1` und `C3` liegen je eigene Startboegen mit Startkern, Stakes und erstem Entscheidungsraum vor,
    2) beide Startboegen bleiben strikt an die neutralen Orts-SSOTs und T0-Topologie gebunden,
    3) Start-Chooser und Arbeitsblatt fuehren die neuen Neutralstarts als `full_slice`,
    4) keine benannten NPC oder Fraktionsrechte werden frei erfunden.
  - Ergebnis 2026-04-05: `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-b1.ssot.md` und `rp-startbogen-freie-gruppen-c3.ssot.md` heben `B1` und `C3` jetzt auf eigenstaendige neutrale Startboegen; der Start-Chooser fuehrt damit drei fraktionslose/neutralnahe Full-Slice-Einstiege `A2/B1/C3`.
  - Evidenz: `B1.md`, `C3.md`, `rp-startbogen-freie-gruppen-b1.ssot.md`, `rp-startbogen-freie-gruppen-c3.ssot.md`, `rp-start-chooser.ssot.md`, `rp-text-rpg-startpaket-slot-00-05-2026-04-05.md`, `Metrokarte-T0.md`, `Stationskontroll-Matrix.md`.

- [x] [Als naechstes] Folgekorridor hinter `slot 15` auf erste Kampagnenfolge `slot 16-20` erweitern.
  - Ziel: Der Produktpfad soll hinter der ersten Langzeitpriorisierung nicht erneut abbrechen, sondern einen belastbaren Anschluss fuer Kampagnenrichtung, Mobilitaet, Kontakt und Rueckkopplung besitzen.
  - Akzeptanzkriterien:
    1) mindestens `slot 16-20` liegen als eigene Folge-SSOT vor,
    2) die Slots fuehren Innen-, Aussen- und Mobilitaetspfad in erste stabile Kampagnenformen ueber,
    3) `slot 16-20` bleibt an vorhandene Orts-, Reveal- und Start-SSOTs gebunden,
    4) Konsequenzen laufen weiter ueber Druck, Kosten und Schwerpunktwahl statt ueber harte Dead Ends.
  - Ergebnis 2026-04-05: `novapolis-dev/docs/process/rp-folgekorridor-slot-16-20.ssot.md` fuehrt jetzt die erste Kampagnenfolge fuer wiederkehrende Innenstabilisierung, neutrale Mobilitaetsfenster `B1/C3`, Aussenpfad `G7` und die Rueckkopplung zwischen diesen Schwerpunkten.
  - Evidenz: `rp-folgekorridor-slot-11-15.ssot.md`, `rp-folgekorridor-slot-16-20.ssot.md`, `rp-startbogen-freie-gruppen-b1.ssot.md`, `rp-startbogen-freie-gruppen-c3.ssot.md`, `rp-startbogen-haendlerbund-g7.ssot.md`, `B1.md`, `C3.md`, `Missionslog-Novapolis.md`, `Metrokarte-T0.md`.

- [x] [Als naechstes] Weitere Neutralstarts `C1` und `D1` von T0-Knoten auf eigene Startboegen heben.
  - Ziel: Der fraktionslose Produktpfad soll nicht nur an den ersten Pufferstationen haengen bleiben, sondern auch auf weitere aktive Neutralraeume mit eigener Startlogik ausgedehnt werden.
  - Akzeptanzkriterien:
    1) fuer `C1` und `D1` liegen je eigene Orts-SSOTs und Startboegen vor,
    2) beide Starts bleiben strikt an T0-Topologie und Statusbelege gebunden,
    3) Start-Chooser und Reveal-Matrix fuehren die neuen Neutralstarts explizit,
    4) keine lokalen Crews, Fraktionsrechte oder Anschlusslagen ohne Beleg werden erfunden.
  - Ergebnis 2026-04-05: `novapolis-rp/database-rp/03-locations/C1.md` und `D1.md` sowie `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-c1.ssot.md` und `rp-startbogen-freie-gruppen-d1.ssot.md` heben die beiden aktiven T0-Neutralraeume jetzt auf eigene spielbare Einstiege; Start-Chooser und Startgebiete-Reveal-Matrix binden sie explizit an.
  - Evidenz: `C1.md`, `D1.md`, `rp-startbogen-freie-gruppen-c1.ssot.md`, `rp-startbogen-freie-gruppen-d1.ssot.md`, `rp-start-chooser.ssot.md`, `rp-startgebiete-reveal-matrix.ssot.md`, `Metrokarte-T0.md`, `Stationskontroll-Matrix.md`.

- [x] [Als naechstes] `E2` und `F1` aus dem aktiven Konfliktstand auf echte Neutralstarts heben.
  - Ziel: Die aktiven Neutralraume `E2` und `F1` sollen trotz des frueheren C6-Codename-Konflikts auf konsistente Orts- und Start-SSOTs gezogen werden.
  - Akzeptanzkriterien:
    1) `C6.md` fuehrt `F1` nicht mehr als stationslosen Codename gegen den aktiven T0-Stand,
    2) `E2` und `F1` liegen je als eigene Orts-SSOT und als eigener Startbogen vor,
    3) Reveal-Matrix und Start-Chooser fuehren beide neuen Neutralstarts explizit,
    4) keine unbelegten Direktverbindungen, Crews oder Detailretcons werden hinzugefuegt.
  - Ergebnis 2026-04-05: `C6.md` fuehrt `F1` jetzt konsistent als realen T0-Knoten mit nur unbelegtem direktem C6-Pfad; `novapolis-rp/database-rp/03-locations/E2.md` und `F1.md` sowie `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-e2.ssot.md` und `rp-startbogen-freie-gruppen-f1.ssot.md` heben beide auf spielbare Neutralstarts.
  - Evidenz: `C6.md`, `E2.md`, `F1.md`, `rp-startbogen-freie-gruppen-e2.ssot.md`, `rp-startbogen-freie-gruppen-f1.ssot.md`, `rp-startgebiete-reveal-matrix.ssot.md`, `rp-start-chooser.ssot.md`, `Missionslog-Novapolis.md`, `Jonas-Merek.md`, `Metrokarte-T0.md`, `Stationskontroll-Matrix.md`.

- [x] [Als naechstes] Folgekorridor hinter `slot 20` auf `slot 21-25` mit `E2/F1` und episodischem Uebergabeanker erweitern.
  - Ziel: Der Produktpfad soll hinter der ersten Kampagnenstufe nicht nur laenger werden, sondern die duennen Reichweitenraeume `E2/F1`, die Rueckkopplung zu D5/C6/G7 und einen save-/replay-faehigen Uebergabeanker fuer die naechste Episode fuehren.
  - Akzeptanzkriterien:
    1) mindestens `slot 21-25` liegen als eigene Folge-SSOT vor,
    2) `E2` und `F1` werden nur entlang ihrer belegten T0- und Konfliktlogik genutzt,
    3) der Korridor bleibt an vorhandene Orts-, Reveal- und Start-SSOTs gebunden,
    4) hinter `slot 25` ist ein lesbarer Episoden- oder Folgekorridor-Anker sichtbar statt eines freien Abrisses.
  - Ergebnis 2026-04-06: `novapolis-dev/docs/process/rp-folgekorridor-slot-21-25.ssot.md` fuehrt jetzt die naechste Kampagnenstufe ueber `E2`, `F1`, Rueckkopplung zwischen Innen-, Kontakt- und Neutralpfad sowie einen episodischen Uebergabeanker; `rp-folgekorridor-slot-16-20.ssot.md` und das Startpaket verweisen im selben Lauf auf diese Anschluss-SSOT.
  - Evidenz: `rp-folgekorridor-slot-16-20.ssot.md`, `rp-folgekorridor-slot-21-25.ssot.md`, `rp-startbogen-freie-gruppen-e2.ssot.md`, `rp-startbogen-freie-gruppen-f1.ssot.md`, `rp-startbogen-haendlerbund-g7.ssot.md`, `E2.md`, `F1.md`, `C6.md`, `Missionslog-Novapolis.md`, `Metrokarte-T0.md`.

- [x] [Als naechstes] Folgekorridor hinter `slot 25` auf `slot 26-30` mit Resume-Klarheit und modularem Anschluss ausbauen.
  - Ziel: Der Produktpfad soll hinter dem ersten episodischen Uebergabeanker einen wiederaufnehmbaren Folgeblock besitzen, der D5/C6/G7 sowie die duennen Neutralraeume `E2/F1` weiter nutzt, ohne freie Stations- oder Tiefennetzlogik zu erfinden.
  - Akzeptanzkriterien:
    1) mindestens `slot 26-30` liegen als eigene Anschluss-SSOT vor,
    2) der Korridor bleibt an bestehende Start-, Reveal- und Orts-SSOTs gebunden,
    3) jeder Slot bleibt als Resume-/Save-/Replay-Anker desselben Produktpfads lesbar,
    4) hinter `slot 30` ist ein klarer Folgeanker fuer weitere Slots oder modulare Episoden sichtbar.
  - Ergebnis 2026-04-07: `novapolis-dev/docs/process/rp-folgekorridor-slot-26-30.ssot.md` fuehrt jetzt die modulare Anschlussstufe hinter `slot 25`; `rp-folgekorridor-slot-21-25.ssot.md`, das Startpaket und `text-rpg-product-gate-v1.ssot.md` verweisen im selben Lauf auf denselben erweiterten Produktpfad bis `slot 30`.
  - Evidenz: `rp-folgekorridor-slot-21-25.ssot.md`, `rp-folgekorridor-slot-26-30.ssot.md`, `rp-startbogen-freie-gruppen-e2.ssot.md`, `rp-startbogen-freie-gruppen-f1.ssot.md`, `rp-startbogen-haendlerbund-g7.ssot.md`, `rp-startbogen-novapolis-d5.ssot.md`, `rp-startbogen-novapolis-c6.ssot.md`, `text-rpg-product-gate-v1.ssot.md`, `text-rpg-session-contract-v1.md`, `Missionslog-Novapolis.md`.

Aktiver Vorbereitungspunkt (2026-03-20)
---------------------------------------

- [x] [Jetzt] Heutiges Pilotpaket fuer Mengen-Backfill und Skill-Mapping vorbereitet.
  - Ziel: den offenen RP-Folgepunkt ohne Scope-Drift in einen konkreten Arbeitsslot fuer heute ueberfuehren.
  - Evidenz: `novapolis-dev/docs/process/rp-inventory-backfill-pilot-2026-03-20.md`.
  - Pilot-Scope: `D5-inventar`, `C6-inventar`, `Novapolis-inventar`.
  - Korrektur 2026-03-20 06:21: RAW und Staging fuer Inventar-/Item-Belege sind jetzt explizit mit durchsucht und im Pilotblatt verankert.
  - Abgleichstart 2026-03-20 06:28: D5/C6/Novapolis werden jetzt gegen RAW, Staging, Szenen und Missionslog gegengeprueft; erster harter Driftpunkt ist `D5-inventar` mit dort gefuehrten C6-Bestaenden trotz Trennungsregel.
  - Ergebnis 2026-03-20 06:36: erster konservativer Abgleich ist abgeschlossen; D5 fuehrt keine C6-Posten mehr lokal, C6 ist als lokaler Belegkontext ohne freie Mengen geschaerft, Novapolis bleibt aggregiert-konservativ.
  - Ergebnis 2026-03-20 06:45: belegter Energie-Tagesabschluss fuer Tag 12 -> 13 ist in D5/C6/Novapolis nachgezogen; nur Bilanz- und Transferlogik, keine neuen absoluten Zellmengen.
  - Ergebnis 2026-03-20 06:52: belegter Materialverbrauch fuer Tag 12 -> 13 ist als Delta eingetragen (`1,3 t Baustoffe`, `120 m Schienenprofil`, `18 m² Betonplatten`, `2` beschaedigte Werkzeuge); Rest- und Standortmengen bleiben offen.
  - Ergebnis 2026-03-20 07:14: `inventar_c6_v2` und `logistik_c6_v2` liefern einen harten C6-Startsnapshot mit Stueckzahlen (`Luftfilter(3)`, `Ersatzrohre(12)`, `Kabelspulen(6)`, `Schmieroel(5)`, `Strommodule(2)`, `Wasserkanister(4)`, `Werkzeugsets(2)`, `Sensorpaket(1)`, `Rationen(9)`, `Wasserflaschen(10)`, `Schutzanzuege(2)`, `Ersatzmasken(3)`).
  - Ergebnis 2026-03-20 07:22: `RAW-canvas-2025-10-16T12-00-00-000Z` liefert fuer D5 einen fruehen Stationsanker mit `Union-Kisten (3)`, Ersatzrohren/Ventilkomponenten, defekter Reparaturstation und `60 %` lesbaren Schaltplaenen; fuer Fraktionssummen fehlt weiter die spaetere Transfer- und Verbrauchskette.
  - Ergebnis 2026-03-20 11:33: Die fehlende Transferkette ist jetzt konkret eingegrenzt. Belegt sind allgemeine Frachtarten (`D5 -> C6: Bauteile/Werkzeuge/Versorgungsgueter`, `C6 -> D5: Materialrueckfuehrung`) und die Tagesbilanz Tag 12 -> 13, aber nicht die Item-Kette `Entnahme -> Transport -> Ankunft -> Quittung`.
  - Folge fuer den offenen Punkt: Solange keine standortscharfen Abbuchungen und keine belegten Zielbuchungen vorliegen, bleibt `Novapolis-inventar` bewusst ohne harte Fraktionssumme.
  - Ergebnis 2026-03-20 11:40: Die Guetermission `D5 -> C6` ist jetzt als eigener Missionsanker im aktiven SSOT verankert. Sie taugt fuer Richtungs- und Kontextbeleg, aber weiterhin nicht fuer Mengenpromotion, weil Item-Entnahme und Quittung fehlen.
  - Ergebnis 2026-03-20 11:49: D5- und C6-Teilinventar fuehren den Materiallauf jetzt ebenfalls als lokale Review-Anker. Damit ist der Gap standortscharf dokumentiert, ohne neue Mengen oder stillschweigende Buchungen zu erfinden.
  - Ergebnis 2026-03-27 08:33: Die C6-Zielseite ist jetzt auch auf Systemebene enger gerahmt. `logistik_novapolis_v2` fuehrt `D5 -> C6 (Bauteile, Werkzeuge, Versorgungsgueter)` als aktive Fracht, `logistik_c6_v2` benennt fuer C6 `Primaerlager (Bereich 3)` und `Sekundaerlager (Kontrollraum)`. Das taugt als semiformeller Zielanker fuer einen missionierten Versorgungslauf, aber nicht als konkrete Zielbuchung oder Charge.
  - Folge fuer den offenen Punkt 2026-03-27 08:33: Konservativ definierbar ist derzeit hoechstens `missionierter Versorgungslauf D5 -> C6 mit bestaetigtem Empfang, Bestandsaufnahme und nachgelagerter Baustellenverteilung`. Nicht definierbar bleiben Item-Mengen, exakte Lagerzuordnung des konkreten Laufs und Inventarlog-Quittung.
  - Ergebnis 2026-03-27 09:46: Vor manueller Verteilung ist der RAW-Rettungsstand jetzt klar abgegrenzt. Hart rettbar sind ein quantifizierter C6-Startsnapshot, ein teilquantifizierter D5-Startanker, der generische Transferpfad `D5 -> C6`, der semiformelle C6-Empfangs-/Zielanker sowie einzelne Tagesdeltas fuer Energie und Materialverbrauch.
  - Folge fuer den offenen Punkt 2026-03-27 09:46: Weich rettbar sind Rollen-, Freigabe- und Prozesslogik fuer D5/C6/Novapolis. Manuell gesetzt werden muessen weiterhin aktuelle Fraktionssummen, standortscharfe Restbestaende, mehrtaegige Verbrauchsreihen sowie konkrete Transfermengen pro Lauf.

- [x] [Jetzt] Ebenenmodell, Pflichtartefakte und Delta-Formate fuer den metro-weiten Warenbestand aus dem vorhandenen RP-Modul abgeleitet.
  - Ziel: den offenen Backfill von einer losen Inventarsammlung auf eine feste Promotionskette `Charakter -> Team/POI -> Station -> Fraktion -> Metro` umstellen.
  - Evidenzbasis: `00-admin/Logistik.md`, `00-admin/Waren-Index.md`, `00-admin/Warenueberblick-T0.md`, `00-admin/Metrokarte-T0.md`, `00-admin/Stationskontroll-Matrix.md`, `00-admin/Fraktionen-Taxonomie.md`, die vorhandenen Fraktionsinventare unter `01-factions/*/04-inventory/`, die Novapolis-Orte/POIs unter `01-factions/novapolis/03-locations/`, `Missionslog-Novapolis.md`, `person-index-np.md`, `novapolis-markets.md`, `novapolis-pricebands.md` sowie die szenischen `inventoryRefs` unter `06-scenes/`.
  - Verbindliches Ebenenmodell:
    - Charakter: personengebundene Ausruestung, mitgetragene Verbrauchsgueter und explizite Ausgabe-/Rueckgabevorgaenge; keine stillen privaten Lagerbestaende ohne Rollen- oder Szenenanker.
    - Team/POI: operative Zwischenebene fuer Werkstatt, Lagerhalle, Schleuse, Konvoi oder feste Arbeitsgruppe; fuehrt Ausgabe, Annahme, Quarantaene, Puffer und lokale Arbeitsverbraeuche.
    - Station: kanonisches Standortinventar aggregiert die POI-/Teamlage je Station und fuehrt standortscharfe Delta- und Restlogik.
    - Fraktion: aggregiert nur bestaetigte Stationsstaende, fraktionsweite Bilanzen und belegte Handels-/Transferstroeme.
    - Metro: fuehrt nur vergleichende T0-/Wochenlage je Fraktion, Station und Warengruppe; keine implizite Welt-Gesamtsumme ohne belastbare Fraktionspfade.
  - Pflichtartefakte je Ebene:
    - Charakter: Charakter-Canvas plus Missions-/Szenenbezug; eigene Inventarseite nur bei wiederkehrendem Besitz, Ausgabehoheit oder dauerhafter Rollenlast.
    - Team/POI: Orts-/POI-Canvas plus zugehoeriges Inventar- oder Logistikziel fuer Ausgabe, Eingang, Quarantaene und Lagerlauf.
    - Station: Lokations-Canvas plus Stationsinventar und Missions-/Logistikverweise.
    - Fraktion: Fraktionsinventar plus Missionslog; bei Aussenfluss zusaetzlich Handelslog oder Relationslog.
    - Metro: Admin-Artefakte `Metrokarte-T0`, `Stationskontroll-Matrix`, `Warenueberblick-T0` und `Fraktionen-Taxonomie` als Vergleichs- und Guardrail-Ebene.
  - Delta-Formate (Minimalset, aus vorhandenem RP-Bestand abgeleitet):
    - `Transfer`: Datum, Status, Item/Warengruppe, Menge/Einheit oder `tbd`, `von`, `nach`, Anlass, Beleg, Verantwortliche/Quittung.
    - `Verbrauch`: Datum, Status, Item/Warengruppe, Menge/Einheit oder `tbd`, Entnahmeort, Zweck/Projekt, Beleg.
    - `Handel`: Datum, Status, Item/Warengruppe, Menge/Einheit oder `tbd`, Gegenpartei, Abrechnung/Band, Uebergabepunkt, Beleg.
    - `Bilanz`: Zeitraum, Ebene, Delta je Warengruppe oder Energiekonto, bekannte Vor-/Nachher-Staende oder `tbd`, Belegkette.
  - Promotionsregel: `Scene/RAW -> Missionslog oder Logistik -> Teilinventar/POI -> Stationsinventar -> Fraktionsinventar -> Metro-Ueberblick`; ohne sauberen Uebergabeschritt wird nicht nach oben promoted.

- [x] [Jetzt] Operative Zuteilungsmatrix fuer die finale Metro-Warenverteilung aus aktiver SSOT und RAW-Rettungsstand abgeleitet.
  - Ziel: vor der finalen Handverteilung alle belastbaren RP-Daten in eine Arbeitsmatrix `hart gesetzt | konservativ geschaetzt | manuell zu entscheiden` ueberfuehren.
  - Evidenz: `novapolis-dev/docs/process/rp-metro-warenzuteilung-matrix-2026-03-27.md`.
  - Ergebnis 2026-03-27 16:12: Die Matrix fuehrt Metro-Rahmen, Novapolis-T0-Lage, D5-/C6-Startanker, Tagesdeltas und den Versorgungslauf `D5 -> C6` in genau dieser Dreiteilung zusammen.
  - Folge fuer die finale Handverteilung 2026-03-27 16:12: Direkt gesetzt werden koennen die belegten D5-/C6-Anker und Tagesdeltas; offen fuer Handentscheid bleiben aktuelle Fraktionssummen, konkrete Transfermengen, Restbestaende je Station und exakte Mengen der uebrigen Hauptfraktionen.
  - Recheck 2026-03-27 16:19: Die Matrix ist jetzt fraktionsscharf fuer Arkologie-A1, Schienenbund, Haendlerbund, Eiserne Enklave/Eisenkonklave, Schattenbund und Fluesterkollektiv nachgezogen. Novapolis bleibt darin ausdruecklich gesondert, weil die aktive SSOT nur eine lokale Kernfraktion in frueher Aufbauphase belegt, nicht aber eine etablierte Metro-Hauptfraktion mit normalisiertem Handelsnetz.

- [x] [Jetzt] Finale Metro-Warenzuteilung aus der Matrix in ein operatives Arbeitsledger ueberfuehren.
  - Ziel: Die Dreiteilung `hart gesetzt | konservativ geschaetzt | manuell zu entscheiden` soll in ein belastbares Zuteilungsblatt fuer Stationen und Fraktionen ueberfuehrt werden.
  - Akzeptanzkriterien:
    1) jeder verteilte Posten ist als `fix`, `rahmenwert` oder `handentscheidung` markiert,
    2) Station, Fraktion und Zielpfad pro Posten sind sichtbar,
    3) offene Handentscheidungen bleiben explizit als `tbd` statt implizit gesetzt,
    4) das Ergebnis verweist sauber auf Matrix, Inventarebene und den spaeteren Updatepfad fuer D5/C6/Fraktionsinventare.
  - Evidenz: `novapolis-dev/docs/process/rp-metro-warenzuteilung-matrix-2026-03-27.md` fuehrt die benoetigte Dreiteilung bereits vollstaendig; im Board selbst fehlt aber noch der direkte Uebergang in ein operatives Verteilungsledger fuer die finale Handarbeit.
  - Abschluss 2026-03-30: `novapolis-dev/docs/process/rp-metro-warenzuteilung-arbeitsledger-2026-03-30.md` fuehrt die Matrix jetzt als operatives Ledger mit getrennten Tabellen fuer `fix`, `rahmenwert` und `handentscheidung`, sichtbaren Zielpfaden sowie einem expliziten Updatepfad fuer `D5-inventar.md`, `C6-inventar.md`, `Novapolis-inventar.md` und die externen Fraktionsinventare.

- [x] [Jetzt] Externe Fraktionsinventare auf konservative T0-Rahmenwerte aus Matrix und Arbeitsledger angleichen.
  - Ziel: Die externen Fraktionen sollen denselben `rahmenwert`-Stand fuehren wie Matrix und Arbeitsledger, ohne stillschweigend Mengen zu setzen.
  - Akzeptanzkriterien:
    1) jedes externe Fraktionsinventar fuehrt ein explizites T0-Rahmenbild statt leerer `tbd`-Huellen,
    2) keine Datei setzt neue Bestandsmengen oder stationsscharfe Lagerzahlen,
    3) Warenueberblick-T0 und Arbeitsledger bleiben die sichtbaren Quellanker,
    4) RP-Validator bleibt gruen.
  - Evidenz: `novapolis-dev/docs/process/rp-metro-warenzuteilung-arbeitsledger-2026-03-30.md`, `novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md`, `novapolis-rp/database-rp/01-factions/*/04-inventory/*.md`.
  - Abschluss 2026-03-31: `Arkologie-inventar.md`, `Schienenbund-inventar.md`, `Haendlerbund-inventar.md`, `Eiserne-Enklave-inventar.md`, `Schattenbund-inventar.md` und `Fluesterkollektiv-inventar.md` fuehren jetzt je einen expliziten T0-Rahmen mit Herkunftslogik, nicht-quantifizierten Bestandsklassen und einem dokumentierten `RAHMENWERT`-Logeintrag.

- [x] [Jetzt] Haendlerbund vom generischen Rahmenwert auf einen belegten H-47/C6-Handelsanker nachziehen.
  - Ziel: Den Haendlerbund nicht nur als generischen Umlaufraum, sondern mit einem konkreten, belegten Aufbaupfad `H-47 -> C6-Handelsstuetzpunkt -> geregelte Handelszyklen` dokumentieren.
  - Akzeptanzkriterien:
    1) `Missionslog-Haendlerbund.md` fuehrt mindestens einen belegten H-47/C6-Missionsanker,
    2) `caravan-moves.md` fuehrt belegte Route, Kontaktpunkte und Austauschklassen statt nur `tbd`,
    3) `Haendlerbund-inventar.md` uebernimmt denselben Handelsanker ohne Mengensetzung,
    4) RP-Validator bleibt gruen.
  - Evidenz: `novapolis-rp/database-raw/99-exports/RAW-canvas-2025-10-16T05-34-00-000Z.txt`, `novapolis-rp/database-raw/99-exports/RAW-canvas-2025-10-16T08-07-00-000Z.txt`, `novapolis-rp/database-rp/01-factions/haendlerbund/03-locations/G7.md`, `novapolis-rp/database-rp/01-factions/haendlerbund/06-handel-diplomatie/Handel-Diplomatie-Haendlergilde.md`.
  - Abschluss 2026-03-31: `Missionslog-Haendlerbund.md`, `caravan-moves.md` und `Haendlerbund-inventar.md` fuehren jetzt denselben belegten H-47/C6-Aufbaupfad mit aktiviertem Handelsstuetzpunkt, Austauschklassen und offen gelassenen Mengen/Manifesten.

- [x] [Jetzt] Eisenkonklave vom reinen Rahmenwert auf belegte Handelsfenster mit Haendlerbund nachziehen.
  - Ziel: Die Eisenkonklave soll nicht nur als Werkstoff-/Schutzgüterraum erscheinen, sondern einen belegten, konservativen Handelsanker mit Freigabekette fuehren.
  - Akzeptanzkriterien:
    1) `Missionslog-Eisenkonklave.md` fuehrt mindestens einen belegten Handels-/Sicherheitsanker,
    2) `Handelslog-Eisenkonklave.md` fuehrt den belegten Rahmen `handel_gelegentlich` statt Stub,
    3) `Eiserne-Enklave-inventar.md` uebernimmt denselben Handelsrahmen ohne Mengensetzung,
    4) RP-Validator bleibt gruen.
  - Evidenz: `novapolis-rp/database-raw/99-exports/RAW-canvas-2025-10-16T16-55-00-000Z.txt`, `novapolis-rp/database-rp/01-factions/eisenkonklave/06-handel-diplomatie/Relationslog-Eisenkonklave.md`, `novapolis-rp/database-rp/01-factions/eisenkonklave/02-characters/Kaspar-Dorn.md`, `novapolis-rp/database-rp/01-factions/eisenkonklave/02-characters/Yara-Kest.md`.
  - Abschluss 2026-03-31: `Missionslog-Eisenkonklave.md`, `Handelslog-Eisenkonklave.md` und `Eiserne-Enklave-inventar.md` fuehren jetzt denselben konservativen Händlerbund-Anker `handel_gelegentlich` inklusive Handelsleitung, Sicherheitsfreigabe und offen gelassenen Dealmengen.

- [x] [Jetzt] Arkologie-A1 vom reinen Rahmenwert auf belegten Haendlergilden-Kanal und Konfliktanker nachziehen.
  - Ziel: Arkologie A1 soll nicht nur als stabiler Aussenblock erscheinen, sondern den belegten Rahmen `Haendlerbund = beschraenkt`, `Eisenkonklave = umkaempft`, `Novapolis = unbekannt` sichtbar in Missions-, Handels-, Relations- und Inventarlogik fuehren.
  - Akzeptanzkriterien:
    1) `Relationslog-Arkologie-A1.md` fuehrt die belegten Statuswerte statt `tbd`,
    2) `Missionslog-Arkologie-A1.md` und `Handelslog-Arkologie-A1.md` fuehren denselben beschraenkten Haendlergilden-Kanal mit Nera/Borin/Liora,
    3) `Arkologie-inventar.md` uebernimmt dieselbe Aussenlage ohne Mengensetzung,
    4) RP-Validator bleibt gruen.
  - Evidenz: `novapolis-rp/database-raw/99-exports/RAW-canvas-2025-10-16T16-55-00-000Z.txt`, `novapolis-rp/database-raw/99-exports/RAW-canvas-2025-10-16T03-25-10-000Z.txt`, `novapolis-rp/database-rp/01-factions/arkologie-a1/02-characters/Nera-Vossen.md`, `novapolis-rp/database-rp/01-factions/arkologie-a1/02-characters/Borin-Khade.md`, `novapolis-rp/database-rp/01-factions/arkologie-a1/02-characters/Liora-Navesh.md`.
  - Abschluss 2026-03-31: `Relationslog-Arkologie-A1.md`, `Handelslog-Arkologie-A1.md`, `Missionslog-Arkologie-A1.md` und `Arkologie-inventar.md` fuehren jetzt denselben konservativen Arkologie-Rahmen aus beschraenktem Haendlergilden-Kanal, umkaempfter Eisenkonklave-Lage und weiterhin unbekanntem Novapolis-Kontakt.

- [x] [Jetzt] Schattenbund vom reinen Rahmenwert auf belegten Relations- und Beschaffungsrahmen nachziehen.
  - Ziel: Der Schattenbund soll nicht nur als opportunistischer Rahmenraum erscheinen, sondern die belegte Aussenlage `Novapolis = unbekannt`, `Eisenkonklave = feindselig`, `Arkologie = verdeckt` sowie die verdeckte Beschaffungskette `Jarek -> Sera -> Nyra` sichtbar fuehren.
  - Akzeptanzkriterien:
    1) `Relationslog-Schattenbund.md` fuehrt die belegten Statuswerte statt `tbd`,
    2) `Handelslog-Schattenbund.md` und `Missionslog-Schattenbund.md` fuehren denselben verdeckten Beschaffungsrahmen,
    3) `Schattenbund-inventar.md` uebernimmt dieselbe Aussenlage ohne Mengensetzung,
    4) RP-Validator bleibt gruen.
  - Evidenz: `novapolis-rp/database-raw/99-exports/RAW-canvas-2025-10-16T16-55-00-000Z.txt`, `novapolis-rp/database-rp/01-factions/schattenbund/02-characters/Jarek-Voan.md`, `novapolis-rp/database-rp/01-factions/schattenbund/02-characters/Sera-Nol.md`, `novapolis-rp/database-rp/01-factions/schattenbund/02-characters/Nyra-Vehl.md`.
  - Abschluss 2026-04-01: `Relationslog-Schattenbund.md`, `Handelslog-Schattenbund.md`, `Missionslog-Schattenbund.md` und `Schattenbund-inventar.md` fuehren jetzt denselben konservativen Schattenbund-Rahmen aus unbekanntem Novapolis-Kontakt, feindseliger Eisenkonklave-Lage, verdeckter Arkologie-Beziehung und verdeckten Beschaffungsfenstern ueber Zwischenhaendler.

- [x] [Jetzt] Fluesterkollektiv vom reinen Rahmenwert auf belegten Minimalrahmen nachziehen.
  - Ziel: Das Fluesterkollektiv soll nicht nur als Informationsraum erscheinen, sondern den belastbaren Minimalrahmen `Novapolis = unbekannt` sowie die interne Kette `Corin -> Sera -> Iris` sichtbar in Relations-, Handels-, Missions- und Inventarlogik fuehren.
  - Akzeptanzkriterien:
    1) `Relationslog-Fluesterkollektiv.md` fuehrt mindestens den belegten Status `Novapolis = unbekannt` statt reiner `tbd`-Huelle,
    2) `Handelslog-Fluesterkollektiv.md` und `Missionslog-Fluesterkollektiv.md` fuehren denselben konservativen Rahmen indirekter Kanaele ohne benannte Gegenparteien,
    3) `Fluesterkollektiv-inventar.md` uebernimmt dieselbe Aussenlage ohne Mengensetzung,
    4) RP-Validator bleibt gruen.
  - Evidenz: `novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/Relationslog-Novapolis.md`, `novapolis-rp/database-rp/01-factions/fluesterkollektiv/02-characters/Corin-Mael.md`, `novapolis-rp/database-rp/01-factions/fluesterkollektiv/02-characters/Sera-Kaal.md`, `novapolis-rp/database-rp/01-factions/fluesterkollektiv/02-characters/Iris-Vey.md`.
  - Abschluss 2026-04-01: `Relationslog-Fluesterkollektiv.md`, `Handelslog-Fluesterkollektiv.md`, `Missionslog-Fluesterkollektiv.md` und `Fluesterkollektiv-inventar.md` fuehren jetzt denselben konservativen Minimalrahmen aus unbekanntem Novapolis-Kontakt sowie indirekten Kanal- und Sicherheitsketten ohne benannte Gegenparteien oder Mengen.

Canvas-Rettung - Sprint 1 (Stand 2025-11-01)
--------------------------------------------
Archiv-Hinweis (manuell, bis Validator bereit)
----------------------------------------------

- Sobald ein Abschnitt (H2/H3) vollständig abgehakt ist ([x] überall) und - für RP - kanonisiert, bitte den gesamten Block manuell nach `novapolis-dev/archive/todo.<modul>.archive.md` verschieben (neuester oben).
- Direkt unter der Abschnitts-Überschrift im Archiv eine Zeile ergänzen: `archived_at: YYYY-MM-DD HH:MM`.
- Automatisierung folgt erst nach Struktur-Review/Validator (Dry-Run only). Keine halb fertigen Blöcke verschieben.

Plan Charakter-Review (laufend)
-------------------------------

Reihenfolge
-----------

- Ronja Kerschner → Abgleich `resolved.md`, RAW `char_ronja_v2` + Flag, Rollenmatrix, Ziele, Systemverknüpfungen, Drift-Notizen. *(erledigt 2025-11-01T17:10+01:00)*
- Jonas Merek → RAW `RAW-canvas-2025-10-16T14-12-00-000Z.*`, Schwesterstatus gemäß `[FACT][JONAS-SIS]`, Werkstatt-/Tunnelinfos konsolidieren. *(erledigt 2025-11-02T13:55+01:00)*
- Lumen → Jonas-Quellen + `[FACT][PROXIMITY]`, Fähigkeiten/Kopplung und Trainings-Canvas aktualisieren. *(validiert erledigt 2026-02-21)*
- Kora Malenkov → RAW `RAW-canvas-2025-10-16T14-56-00-000Z.txt`, paranoide Vorsicht, C6-Linienstatus (FACT `C6-LINES`), Echo-Interaktion. *(erledigt 2025-11-02T14:20+01:00)*
- Senn Daru → Relationslog `RAW-canvas-2025-10-16T08-07-00-000Z.*`, Handels-/Diplomatie-Notizen, Wissensgrenzen. *(validiert erledigt 2026-02-21)*
- Marven Kael → RAW `RAW-canvas-2025-10-16T14-56-10-000Z.*`, Konvoi-/Handelsleitung (`[FACT][CARAVAN-LEADERSHIP]`), Beziehungen Händlergilde/Novapolis. *(erledigt 2025-11-02T14:45+01:00)*
- Arlen Dross → RAW `RAW-canvas-2025-10-16T14-56-20-000Z.*`, Vermittlerrolle, Reflex-Einschätzung. *(erledigt 2025-11-02T15:05+01:00)*
- Pahl → RAW `RAW-canvas-2025-10-16T14-41-00-000Z.*`, Gesundheitsstatus, Risiken, Energie-/Generatorwissen. *(erledigt 2025-11-02T15:25+01:00)*
- Reflex (Primärinstanz) → RAW `char_reflex_v2`, FACTs `[REFLEX-*]` (Frequenzband, Detach, Speech), Wissens-/Trainings-Canvas synchronisieren. *(erledigt 2025-11-02T16:05+01:00)*

Arbeitsschritte pro Charakter
-----------------------------

- Quellen sammeln: `database-curated/staging/reports/resolved.md`, `.../uncertainties.md`, zugehörige RAW-/Flag-Dateien, overlap-Reports.
- Canvas aktualisieren (Werte, Skills, Motivation, Wissensmatrix, Beziehungen, Ziele, Risiken) und Systemverknüpfungen prüfen.
- Zugehörige Wissens-/Trainings-Canvases mitziehen (Instanzen).
- Behavior-Signatur gegen Anchor-Register prüfen; Drift-Flags dokumentieren.
- JSON-Sidecar, `char-block-nord-sources.md`, `person-index-np.md`, DONELOGs (`novapolis-dev/docs/donelog.md`, Root `DONELOG.md`) und TODO-Status aktualisieren.
- Nach einem Bündel Updates Validator laufen lassen (`npm --prefix novapolis-rp/coding/tools/validators run validate:rp` + optional `npm --prefix ... run validate:crossrefs`).

Archivstatus (2026-02-22)
-------------------------

- Vollständig erledigte Blöcke `Aktiv jetzt (sicher)`, `Priorität B - Logistik & Inventar` und `Priorität C - Systeme, Indizes, Ereignisse` wurden nach `novapolis-dev/archive/todo.rp.archive.md` verschoben.

Arbeitsregeln & Referenzen
--------------------------

- Workflow siehe `novapolis-dev/docs/process/rp-canvas-rescue/canvas-rescue-plan.md`.
- Quellen + Drift-Notizen in `novapolis-dev/docs/process/rp-canvas-rescue/char-block-nord-sources.md` berücksichtigen.
- FACT-Beschlüsse aus `novapolis-dev/docs/process/rp-canvas-rescue/resolved.md` vor Promotion prüfen.
- Jede Migration mit JSON-Sidecar und DONELOG-Eintrag dokumentieren (`novapolis-dev/docs/donelog.md`).
- Flags (`vorsichtig_behandeln`, `korrupt`) sichtbar übernehmen, bis Review abgeschlossen ist.

Linkübersicht
-------------

- Plan: `novapolis-dev/docs/process/rp-canvas-rescue/canvas-rescue-plan.md`
- Quellen: `novapolis-dev/docs/process/rp-canvas-rescue/char-block-nord-sources.md`
- RAW: `database-raw/99-exports/`
- Kanon/Policies: `novapolis-dev/docs/process/rp-canvas-rescue/resolved.md`, `.github/copilot-instructions.md`

<details>
<summary>Archiviertes Backlog (ausgelagert)</summary>

- Volltext ausgelagert nach `novapolis-dev/archive/todo.rp.historical-backlog.md`.
- Inhalt bleibt historisch/nicht aktiv; Reaktivierung nur per explizitem Soll-Ist-Abgleich gegen aktuelle SSOT-Dateien.

</details>
Neue Aufgaben - Zeitmodell, Annotation & Logs (2025-11-01 22:24)
----------------------------------------------------------------

Prioritaet 0 - Gesamtbild T0 (vor Detailmengen)
-----------------------------------------------

Ziel
----

- Zuerst ein belastbares Gesamtbild aufbauen (Karte, Kontrolle, Warenlage), danach Detailmengen pro Station schrittweise nachziehen.
- Keine neuen unbelegten Canon-Behauptungen; unbekannte Punkte bleiben explizit `tbd`/`unklar`.

Umsetzungsreihenfolge (MVP)
---------------------------

- [x] P0.1 Metro-Topologie als Arbeitskarte T0 anlegen (Stationen, Verbindungen, Status pro Knoten/Kante).
- [x] P0.2 Stationskontrolle je Fraktion erfassen (gesichert/umkaempft/verlassen/unklar + Confidence).
- [x] P0.3 Warenueberblick T0 je Fraktion/Station als Bandbreitenmodell erfassen (`none|low|medium|high` statt Scheingenauigkeit).
- [x] P0.4 Herkunftslabel pro Warenposten verpflichtend setzen (`legacy|evac_e3|scavenged|produced|unknown`).
- [x] P0.5 D5/C6 sauber als fruehe Aufbauphase markieren (kein etablierter Handel; Bestand nur aus Altbestand/Funden/E3-Mitnahme).
  - Evidenz: `novapolis-rp/database-rp/00-admin/Metrokarte-T0.md`, `novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md`, `novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md`.

Scope-Guardrails
----------------

- [x] D5/C6: Keine Handelsnormalisierung simulieren, solange Handelsbeziehungen im RP noch nicht etabliert sind.
- [x] Etablierte Fraktionen: Grundvorräte zulassen, aber Stationenlage explizit als unvollstaendig kennzeichnen.
- [x] Mengenpraezision erst nach P0.1-P0.4 erhoehen; bis dahin nur Bandbreiten + Quellenanker.

Konkrete Deliverables
---------------------

- [x] Admin: Metrokarte-T0 (Knoten/Kanten + Statusmodell) unter `00-admin`.
- [x] Admin: Fraktionskontroll-Matrix Stationen (Fraktion x Station x Status x Confidence).
- [x] Admin: Warenueberblick-T0 (globales Raster + Herkunftssystem).
- [x] Fraktionen: Minimal-Abgleich je Basis/known stations mit Verweis auf Admin-SSOT. *(erledigt 2026-02-23)*
  - Evidenz: `novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md` (Abschnitt „Minimal-Abgleich Basis-/Known-Stationen (T0)“) mit Referenzen auf `Metrokarte-T0`, `Stationskontroll-Matrix`, `Warenueberblick-T0`.

Definition of Done (P0)
-----------------------

- [x] Jede bekannte Station ist in Karte + Kontrollmatrix mindestens einmal referenziert. *(erledigt 2026-02-23)*
  - Evidenz: `novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md` enthält jetzt alle in `novapolis-rp/database-rp/00-admin/Metrokarte-T0.md` geführten Stationscodes (Abdeckung 54/54).
- [x] [Jetzt] Jede Fraktion hat einen T0-Warenueberblick mit Herkunftslabeln.
  - Evidenz: `novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md` (Abschnitt `Fraktionsueberblick T0 (Herkunftslabel)`).
- [x] [Jetzt] D5/C6 sind konsistent als fruehe Aufbauphase modelliert; keine impliziten Handelsannahmen.
  - Evidenz: `novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md` (Abschnitt `D5/C6-Modell (fruehe Aufbauphase)`).
- [x] [Als naechstes] Danach erst Mengen-Backfill in Inventaren (D5/C6/Fraktionen) starten.
  - Startreihenfolge fuer den heutigen Pilot: `C6-inventar` -> `D5-inventar` -> `Novapolis-inventar`.
  - Arbeitsgrundlage: `novapolis-dev/docs/process/rp-inventory-backfill-pilot-2026-03-20.md`.
  - Verbindliche Gesamt-Reihenfolge fuer den naechsten Ausbau: `Metro-Rahmen` -> `Fraktionsbasis/known stations` -> `Stationsinventare` -> `Team/POI` -> `Charakter-/Rollenanker` -> `Fraktionsaggregation`.
  - Vor jeder Mengenpromotion muessen mindestens die betroffene Missions-/Logistikspur und die Ziel-Inventarebene existieren; fuer Aussenfluss zusaetzlich Handels- oder Relationslog.
  - Die vier Minimal-Deltas `Transfer`, `Verbrauch`, `Handel`, `Bilanz` sind ab jetzt der Pflichtwortschatz fuer neue Bestandsfortschreibung; ohne Quelle, Ziel oder Beleg bleibt der Eintrag `tbd`/`offen`.
  - Abschluss 2026-03-31: Der Pilot ist operativ durchgezogen. `D5-inventar.md`, `C6-inventar.md`, `Novapolis-inventar.md` und `Missionslog-Novapolis.md` fuehren jetzt denselben konservativen Warenlauf; fuer externe Fraktionen bleibt nur noch Rahmenpflege ohne Mengensetzung.

- [x] [Jetzt] Fehlende Transferkette `Entnahme -> Transport -> Ankunft -> Quittung` fuer `D5 -> C6` mit belastbaren RP-Belegzeilen schliessen.
  - Ziel: den aktuell nur generisch belegten Materiallauf so absichern, dass er fuer echte Bestandsfortschreibung taugt.
  - Akzeptanzkriterien:
    1) mindestens eine explizite Entnahmezeile im Quellkontext D5 ist belegt,
    2) mindestens eine Ankunfts- oder Zielbuchungszeile fuer C6 ist belegt,
    3) Verantwortliche oder Quittung sind im Missions-/Logistikpfad genannt,
    4) `Missionslog-Novapolis.md`, `D5-inventar.md`, `C6-inventar.md` und `Novapolis-inventar.md` fuehren dieselbe Transferkette ohne Widerspruch.
  - Evidenz: `novapolis-dev/docs/process/rp-inventory-backfill-pilot-2026-03-20.md`, `novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md`, `novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md`, `novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md`, `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Missionslog-Novapolis.md`.
  - Recheck 2026-03-27 08:14: Umfeld und RAW erneut geprueft. Hart belegt sind aktuell nur `AktiveFracht:D5->C6(Bauteile,Werkzeuge,Versorgungsgueter)` im RAW-Logistikcanvas `RAW-canvas-2025-10-16T13-05-00-000Z`, die Abmeldung `melden sich noch bei D5 ab` sowie die anschliessende `Ankunft` und `Bestandsaufnahme` in C6 im Chat-RAW. Nicht belegt bleiben explizite Entnahmezeilen, konkrete C6-Zielbuchungen in Schleuse/Lagerhalle und Quittungen/Verantwortliche; der Punkt bleibt daher bewusst offen.
  - Recheck 2026-03-27 08:25: D5-seitig ist der Quellkontext jetzt enger. `RAW-canvas-2025-10-20T12-05-00-000Z` belegt ein Materiallager unter dem Bahnsteig mit Lastenaufzug und Nutzung `Schwerlast, Rohstahl, Kabeltrommeln, Energiezellenpaletten`; `Draisine-Transportmodul.md` und Chat-RAW belegen parallel Werkstattbestand, Materiallauf-Unterstuetzung und die Freigabe/Fokussierung von Jonas, Pahl und Lumen auf das Transportmodul. Das reicht fuer eine belastbare Herkunftsannahme `D5-Materiallager und/oder Werkstattbestand`, aber weiter nicht fuer eine harte Inventarbuchung ohne explizite Entnahme- und Quittungszeile.
  - Recheck 2026-03-27 08:29: C6-seitig ist der Empfangspfad jetzt enger. Chat-RAW belegt nach der Abmeldung in D5 nicht nur `Ankunft` und `Bestandsaufnahme`, sondern auch den expliziten Satz `der Empfang der Ware muss bestaetigt werden`; anschliessend soll die Ware `zusammen mit der aus D5 an die Baustellen gebracht` werden. Das reicht fuer eine belastbare Zielannahme `Empfang in C6 mit nachgelagerter Baustellenverteilung`, aber weiter nicht fuer eine harte Inventarbuchung in `C6-Schleuse` oder `C6-Lagerhalle`, weil Einlagerungs-/Inventarlog-Zeilen fehlen.
  - Abschluss 2026-03-31: Der Punkt ist konservativ geschlossen. Der Chat-RAW liefert jetzt D5-seitig die explizite Entnahme-/Packzeile `Ronja wird das notwendige einpacken`, den Transport mit `Reflex`-Unterstuetzung, die `Abmeldung` in D5 sowie C6-seitig `Eintreffen`, `Bestandsaufnahme` und `Empfang der Ware muss bestaetigt werden`. `Missionslog-Novapolis.md`, `D5-inventar.md`, `C6-inventar.md` und `Novapolis-inventar.md` fuehren damit dieselbe Prozesskette widerspruchsfrei; offen bleiben nur Mengen, Charge und Primaer-/Sekundaerlager-Zuordnung.

- [x] [Jetzt] `Novapolis-inventar.md` von der generischen Fraktionslage auf ein belegtes Delta-/Bilanzformat umstellen.
  - Ziel: Das Fraktionsinventar soll nicht nur offene Hinweise sammeln, sondern die belegten Deltas `Transfer`, `Verbrauch`, `Handel`, `Bilanz` direkt in einer auswertbaren Struktur fuehren.
  - Akzeptanzkriterien:
    1) jeder aktuelle Fraktionsposten ist einem Delta-Typ zugeordnet,
    2) unbelegte Restmengen bleiben sichtbar `tbd`, aber ohne Mischformat aus Freitext und Halb-Buchung,
    3) die Struktur referenziert sauber auf D5/C6-Teilinventare und Missionslog,
    4) RP-Validator bleibt gruen.
  - Evidenz: Das Board fuehrt seit 2026-03-20 die vier Pflicht-Deltas; `Novapolis-inventar.md` enthaelt bislang zwar belegt/offen-Anker, aber noch keine eigenstaendige Delta-Struktur.
  - Abschluss 2026-03-31: `Novapolis-inventar.md` fuehrt jetzt getrennte Abschnitte fuer `Transfer`, `Verbrauch`, `Bilanz`, `Handel`, dazu einen kompakten Bedarfsblock und explizite `tbd`-Restmengen. Die Fraktionslage ist damit auswertbar, ohne Restbestaende zu erfinden.

- 24×1h-Runden (PC-zentriert) einführen
  - [x] Policy festhalten: Stunde spult leise weiter, bis ein PC-relevantes Ereignis eintritt (z. B. „Reflex weckt Ronja“). *(erledigt 2026-02-22)*
  - [x] Pro Stunde zwei Logs führen: `world_log` (Wahrheit) und `pc_log` (nur Sichtbares für den PC). *(erledigt 2026-02-22)*
  - [x] Sichtbarkeit umsetzen: scope `private|allies_only|pc|public`, plus `channel`, `source`, `confidence`, `freshness` (siehe Knowledge-Schema unten). *(erledigt 2026-02-22)*
  - [x] Referenz: `novapolis-dev/docs/specs/annotation-spec.md` vorhanden und weiterhin passend zum 24×1h-Vorgehen. *(validiert 2026-02-22)*

- Knowledge-Annotation schrittweise ergänzen (wichtige Charaktere/Missionen zuerst)
  - [x] Charaktere: Reflex, Ronja, Jonas - Knowledge-Einträge in dedizierten Dateien (z. B. `Reflex-Wissensstand-Trainingsstand.md`) und/oder Canvas-Frontmatter `knowledge:`. *(umgesetzt 2026-02-22)*
  - [x] Missionen/Ereignisse: je Kernereignis mind. ein Knowledge-Item mit `about`, `channel`, `source`, `scope`, `confidence`, `freshness`, `visibility_to`, `attachments`. *(umgesetzt 2026-02-22)*
  - [x] Rückblendenprozess: Items per Log/Funk von `allies_only/hidden` → `pc` heben (keine Retcons, nur Sichtbarkeit). *(umgesetzt 2026-02-22)*
  - [x] Referenz: `novapolis-dev/docs/specs/annotation-spec.md` vorhanden und weiterhin passend. *(validiert 2026-02-22)*

- Actions-Schema (für möglichen „Zug-um-Zug“-Wechsel) jetzt leicht mitpflegen
  - [x] In Missions-/Orts-Canvases `actions:` notieren: `verb`, `base_duration_min`, `effort`, `interruptible`, `locks`, `may_trigger_event`, `resources`. *(umgesetzt 2026-02-22)*
  - [x] Kernaktionen definieren (5-10): Reinigen, Reparatur, Reise, Wache, Funk, Erste Hilfe, Erkundung. *(umgesetzt 2026-02-22)*
  - [x] Naming-Konvention und kurze Beispiele dokumentieren. *(durch Spec vorhanden; validiert 2026-02-22)*
  - [x] Referenz: `novapolis-dev/docs/specs/annotation-spec.md` vorhanden und weiterhin passend. *(validiert 2026-02-22)*

- Skills aus Verhaltensmatrix ableiten (ohne zweites System)
  - Vorbereitung 2026-03-20: Start-Scope fuer `reparieren`, `wache` und `funk|wahrnehmung` auf Basis von `annotation-spec.md` und `AI-Behavior-Mapping.md` festgelegt.
  - [x] [Jetzt] Mapping-Gewichte je Skill (0-3) vorgeschlagen (Matrix-Dimensionen -> Skill), Ausgangswerte pro Rolle festgelegt. *(umgesetzt 2026-03-20; Referenz: `novapolis-dev/docs/specs/annotation-spec.md`, Abschnitt `Novapolis V1 (konservative Arbeitsfassung)`)*
  - [x] [Jetzt] Formel/Beispiele im Spec verlinkt; Ableitung bleibt on-demand, keine Duplikat-Wahrheit. *(umgesetzt 2026-03-20; Beispiele fuer Ronja, Jonas und Kora im Spec ergänzt)*
  - Ausbau 2026-03-20 07:08: zweite Referenzreihe fuer `Pahl`, `Reflex`, `Lumen` und `Echo` im Spec nachgezogen; Rollenfit bleibt konservativ auf `wartung_technik` bzw. `sicherung_monitoring` begrenzt.

- [x] [Als naechstes] Skill-Mapping-V1 an mindestens zwei aktiven Missions- oder Rollenpfaden gegen reale Szenen pruefen.
  - Ziel: Die dokumentierte V1 soll nicht nur als Spec existieren, sondern an echten RP-Faellen auf Plausibilitaet und Grenzfaelle gegengeprueft werden.
  - Akzeptanzkriterien:
    1) mindestens zwei konkrete Szenen/Missionen sind mit der V1 nachvollziehbar gegengelesen,
    2) auffaellige Ueber- oder Unterbewertungen sind als Guardrail oder Anpassung dokumentiert,
    3) keine zweite Wahrheit in Charakterdateien entsteht,
    4) Ergebnis landet im RP-Prozesslog oder Spec-Nachtrag.
  - Evidenz: `novapolis-dev/docs/specs/annotation-spec.md` enthaelt jetzt den Realabgleich fuer den Missionspfad `D5 -> C6` mit `Ronja`/`Reflex`, fuer `Pahl` als faktisches D5-Kommando sowie fuer `Kora`/`Echo` im C6-Schutz-/Logistikkontext.
  - Abschluss 2026-04-02: Der Realabgleich bestaetigt die konservativen Baselines fuer `Ronja`/`Reflex` und `Kora`/`Echo`. Nur `Pahl` bekommt keinen Rollenwechsel, sondern einen szenengebundenen Kontext-Lift `funk +1`, `wache +1`, wenn D5 explizit unter seinem Freigabe-/Sicherheitskommando laeuft.

- TTS (gemischt)
  - [x] [Spaeter] Vorproduzierte OGG-Summaries je Stunde (world/pc) - Kandidaten markieren.
    - Ziel: Der spaetere Build-Time-Export soll nicht blind jede Stunde vertonen, sondern zuerst die bereits kanonisierten Handover-, Kontakt- und Episodenkanten des Produktpfads markieren.
    - Akzeptanzkriterien:
      1) die Kandidaten bleiben an bestehende Slot-SSOTs und das vorhandene Audio-Namensschema gebunden,
      2) `world`- und `pc`-Kandidaten sind getrennt markiert,
      3) Build-Time-Kandidaten und spaetere Live-Dialoge werden nicht vermischt,
      4) der Punkt landet als nachvollziehbare SSOT im RP-Prozesspfad statt als lose Board-Notiz.
    - Ergebnis 2026-04-07: `novapolis-dev/docs/process/rp-ogg-summary-kandidaten-slot-00-30.ssot.md` markiert jetzt die erste belastbare Exportwelle ueber `slot 00-30`. Priorisiert sind die bestehenden Handover-, Kontakt- und Episodenkanten `01`, `04`, `07`, `08`, `09`, `10`, `15`, `20`, `25`, `26`, `28`, `29` und `30`; nicht priorisierte Slots bleiben bewusst ohne Audio-Pflicht.
    - Evidenz: `rp-folgekorridor-slot-00-05.ssot.md`, `rp-folgekorridor-slot-06-10.ssot.md`, `rp-folgekorridor-slot-11-15.ssot.md`, `rp-folgekorridor-slot-16-20.ssot.md`, `rp-folgekorridor-slot-21-25.ssot.md`, `rp-folgekorridor-slot-26-30.ssot.md`, `novapolis-dev/docs/specs/annotation-spec.md`, `novapolis-dev/docs/specs/scheduler-spec.md`, `novapolis-dev/docs/specs/tts-exporter-coqui.md`.
  - [x] [Spaeter] Live-Dialoge ueber produktiven Coqui-Runtime-Pfad mit Hash-Cache und sessionbezogener Artefaktkette fuehren.
    - Ziel: Der RP-Pfad soll Audio nicht nur fuer Build-Time-Summaries vormerken, sondern auch denselben Live-Dialogpfad nutzen koennen, der bereits Session, Kanal und Cache kontrolliert zusammenhaelt.
    - Akzeptanzkriterien:
      1) Live-Synthese bleibt an denselben Text-RPG-Sessionrahmen gebunden wie `world_log` und `pc_log`,
      2) Cache-Key und Artefaktpfad bleiben reproduzierbar und sessionbezogen,
      3) der Sim-Client kann dieselben Audioartefakte ueber `tts_manifest` konsumieren,
      4) weitere Provider bleiben explizite Ausnahme- oder Vergleichspfade statt impliziter Pflicht.
    - Ergebnis 2026-04-07: Der aktuelle Runtime-Iststand fuehrt Live-Dialoge bereits ueber den produktiven `coqui`-Provider. `novapolis_agent/app/main.py` und `app/tts/providers.py` fuehren denselben Session-/Slot-/Kanalrahmen in `/tts/synthesize`, Hash-Cache und Artefaktpfad `runtime/sessions/<session>/<channel>/...`; `novapolis_agent/docs/runbook.md` und `README.md` dokumentieren denselben Betriebsstand, und `novapolis-sim/scripts/Main.gd` konsumiert die sessionbezogenen Eintraege aus `tts_manifest` bereits fuer Live-Audio im Hub.
    - Evidenz: `novapolis_agent/docs/runbook.md`, `novapolis_agent/README.md`, `novapolis_agent/docs/DONELOG.txt`, `novapolis_agent/app/main.py`, `novapolis_agent/app/tts/providers.py`, `novapolis-sim/scripts/Main.gd`.






