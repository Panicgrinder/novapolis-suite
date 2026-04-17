---
stand: 2026-04-18 00:55
update: Die UI-IA fuehrt jetzt auch die kanonische Warnsignal-Matrix fuer stille Hintergrundlage, Knappheit, Warnung und Ueberzug.
checks: snapshot-lock PASS (2026-04-18 00:55); markdownlint=PASS; frontmatter=PASS
---

Sim UI- und Menue-IA (SSOT)
===========================

Zweck
-----

Diese SSOT beschreibt die fachliche Informationsarchitektur fuer Hub, eigentliches Spiel, Replay-/Resume-Pfad und operative Module, damit weitere UI-Arbeit nicht nur auf Node-Layoutnamen basiert.

Scope
-----

- Screen- und Menuebaum fuer Sim-Hub, eigentliches Spiel und modulare Betriebsmodi
- Zustandsbesitz fuer Session, Slot, Replay-Anker und aktive Ansicht
- Rueckwege zwischen Hub, Spielsicht und operativen Modulen
- kanonische User-Hinweise fuer den Zustand, in dem RP noch nicht aktiv oder noch nicht ueber denselben Sessionpfad angeschlossen ist

Produktlesart des ersten Vertikalslice
-------------------------------------

- Der erste suiteweite Vertikalslice lautet auch in der UI verbindlich `Hub -> Spielhauptmenue -> Charakterstart -> erster Vollturn -> turn_resume_ready`.
- Der kleinste stabile Save-Punkt ist das erste `turn_resume_ready` nach einem voll ausgespielten ersten Turn; davor darf die UI keinen versprochenen Resume-Anker anzeigen.
- Replay-Zweck bleibt Nachvollzug und Wiedereinstiegshilfe fuer denselben Lauf und nicht ein paralleler Fortschrittspfad.
- Pflichtkern fuer die erste sichtbare UI: KI-gestuetzter Charakterstart, lesbarer erster Vollturn mit unmittelbarem Anschlusssignal, Save-/Resume-/Replay-Bruecke ab `turn_resume_ready`.
- Die UI verwendet fuer planbezogene Rueckmeldungen ohne Parallelformel dieselben drei Recovery-Begriffe wie der restliche Produktpfad: `teilmoeglich`, `verschoben`, `blockiert`.
- Bewusst spaeter bleiben breitere Startauswahl, aktive RP-Integration hinter `slot 30` und Komfort-/Atmosphaereausbau.
- Kanonischer CLI-Smoke fuer genau diesen UI-Pfad bleibt `Checks: sim headless verify` bzw. `& .\.venv\Scripts\python.exe scripts\run_sim_headless_verify.py`.

Recovery-Lesart im UI-Pfad
--------------------------

- `teilmoeglich`: Die Spielsicht zeigt sichtbaren Fortschritt, markiert aber denselben Planrest als begonnen oder offen und gibt einen direkten Folgeschritt aus derselben Linie.
- `verschoben`: Die Spielsicht zeigt, dass der Zielplan in diesem Turn nicht sauber passt, und lenkt auf Vorarbeit, engeren Teilschritt oder bestaetigte Aufteilung um, statt still zu kuerzen.
- `blockiert`: Die Spielsicht nennt die konkrete Sperre und zeigt unmittelbar einen vorbereitenden Alternativschritt oder einen anderen plausiblen Zugang an.
- Diese drei Begriffe sind fuer den ersten Vertikalslice die kanonische Lesart in Hub-Chat, Resume-Hinweisen und spaeteren UI-Statusmeldungen.

Warnsignal-Matrix im UI-Pfad
----------------------------

- `stille Hintergrundlage` bleibt dauerhaft lesbar, aber unaufdringlich. Sie gehoert in Topband und Telemetrieband und fuehrt Grundton, wirtschaftliche Lage oder langsamen Systemdruck, ohne den laufenden Turn zur Hauptsache zu machen.
- `Knappheit` gehoert sichtbar ins Topband und in die aktive Spielsicht, sobald eine Ressource oder ein Spielraum knapp wird. Der Spieler soll auf einen Blick erkennen koennen, was enger wird und welcher stabile naechste Schritt die Lage entschärft.
- `Warnung` gehoert sichtbar in Stage und Ops-Spalte, sobald eine unmittelbare negative Folge fuer Sicherheit, Lage oder Anschluss droht. Sie braucht eine kurze Handlungslesart statt nur ein abstraktes Gefahrenschild.
- `Ueberzug` gehoert direkt an Turn-Feedback, Hub-Chat und Resume-Hinweise. Er markiert keine allgemeine Weltgefahr, sondern dass der aktuelle Plan den Turn-Rahmen ueberzieht und deshalb in `teilmoeglich` oder `verschoben` uebergeht.
- Dieselbe Viererlesart bleibt ueber alle Hub-Zonen stabil: ruhige Lage in Topband/Telemetrie, knappe Mittel in Topband/Spielsicht, akute Warnung in Stage/Ops, turnbezogener Ueberzug am Antwort- und Resume-Pfad.
- Die UI soll fuer den ersten Slice lieber einen dominanten Druckhinweis pro Kategorie zeigen als mehrere konkurrierende Marker zugleich.

Screen- und Menuebaum
---------------------

### Ebene 0 - Sim-Hub

- Einstiegspunkt des Projekts.
- Zonen: Topband, Stage, Ops-Spalte, Telemetrieband.
- Der Hub ist Operator-Oberflaeche und nicht selbst die eigentliche Ingame-Figurensicht.

### Ebene 1 - Hauptmenue des eigentlichen Spiels

- Fachlich die erste Spielschwelle hinter dem Hub.
- Trennfunktion: Wechsel von Operator-Kontext zu Spieler-Kontext.
- Bei neuem Lauf fuehrt dieser Pfad in Charakterstart bzw. Startbriefing.
- Bei laufender Session fuehrt derselbe Pfad in die aktuelle Spielsituation oder einen Resume-Anker.

### Ebene 2 - Laufende Spielsicht

- Kernloop `Input -> Antwort -> State-Update -> UI-Refresh`.
- Sichtbar im aktuellen Sim-Hub ueber Stage und `Hub-Chat`, spaeter weiterhin an denselben Session-Vertrag gebunden.
- Zeigt aktive Szene, Konsequenz, Optionen, Patch-Hinweise und Session-Kontext.

### Ebene 3 - Ingame-Menues

- Pause/Optionen, Rueckspruenge, Restart-/Resume-Entscheidungen.
- Diese Menues duerfen den Session-Vertrag nicht brechen, sondern nur bestehende Session-, Replay- oder Einstellungsdaten sichtbar machen oder bestaetigen.

### Ebene 4 - Operative Module

- Agent-Studio
- Checks-Studio
- RP-Studio
- Diese Modi bleiben bewusst getrennt vom eigentlichen Spielpfad und sind Operator-Oberflaechen, keine Ingame-Menues.

Zustandsbesitz
--------------

### Hub-Zustand

- Besitzer: lokaler Godot-Client
- Daten: Karten-Sichtbarkeit, Default-Panel, Refresh-Profil, aktive Modulansicht
- Persistenz: `user://hub_prefs.cfg`

### Live-Session-Zustand

- Besitzer: Sim-API-Sessionvertrag
- Daten: `session_id`, `campaign_id`, `scene_id`, `slot_id`, `slot_index`, `turn_id`, `world_log`, `pc_log`, `state_patches`
- Persistenz: API-Artefakte unter `novapolis_agent/tmp/sim_sessions/<session_id>/`

### Replay-/Resume-Zustand

- Besitzer: Sim-API plus lokaler Auswahlzustand
- Daten: `resume_checkpoint_id`, `checkpoints`, `replay_manifest`, lokal gewaehlter Checkpoint
- Persistenz: Resume- und Replay-Basis in den Session-Artefakten; zuletzt gewaehlter Checkpoint zusaetzlich in `user://hub_prefs.cfg`
- Fachliche Lesart: Resume setzt nur den kleinsten stabilen Save-Punkt auf `turn_resume_ready` fort; Replay dient demselben Lauf als Nachvollzug und Wiedereinstiegshilfe.

### Aktive Ansicht

- Besitzer: Godot-UI
- Daten: Hub vs. Agent vs. Checks vs. RP, plus Sichtbarkeit von Config- und Replay-Panels
- Persistenz: nur lokale Hub-Prefs, keine Session-Artefakte

Rueckwege und Wechsel
---------------------

- Hub -> Hauptmenue des eigentlichen Spiels: Rollenwechsel von Operator zu Spieler.
- Hauptmenue -> laufende Spielsicht: neuer Start oder Resume einer bestehenden Session.
- Laufende Spielsicht -> Hub: Rueckweg auf Operator-Ebene ohne Verlust des Session-Vertrags.
- Hub -> Agent/Checks/RP: modulare Operator-Wechsel; kein direkter Ingame-Sprung.
- Replay/Resume bleibt querliegender Bedienpfad im Hub und darf keinen zweiten Sessionkanal eroeffnen.

User-Fuehrung vor aktiver RP-Integration
----------------------------------------

- Solange RP nicht ueber denselben Session- und Handover-Pfad aktiv angeschlossen ist, bleibt `Hub-Chat` der einzige kanonische Live-Spielpfad fuer den Spieler.
- `RP-Studio` und `RP-Chat` muessen in diesem Zustand sichtbar als Operator- oder Modulkontext lesbar bleiben und duerfen keine produktive Ingame-Fortsetzung versprechen.
- Wenn ein RP-Pfad noch nicht aktiv ist, braucht die UI einen klaren Statushinweis `RP noch nicht aktiv ueber diesen Lauf`, statt stiller Leere oder einer impliziten Fehlfunktion.
- Der Einstieg ueber `Hub -> Hauptmenue -> Spiel/Resume` bleibt auch dann der kanonische Spielerpfad; RP-spezifische Panels duerfen dafuer keinen konkurrierenden Startbutton oder Schnellpfad anbieten.
- Unterschiede zwischen Live-Zustand, Resume-Anker und Replay-Zustand muessen im Hub sichtbar lesbar bleiben: Live ist die aktuelle Session, Resume setzt den letzten stabilen Anker fort, Replay bleibt Nachvollzug und nicht der primaere Fortschrittspfad.
- Wenn RP spaeter aktiv wird, darf derselbe UI-Bereich von Statushinweis auf echten Anschluss umschalten, aber nur entlang derselben Begriffe `Hub-Chat`, `RP-Chat`, `Resume-Anker` und `Replay`.

Kontextgrenzen
--------------

- `Hub-Chat` ist der Live-Spielclient im Hub-Kontext.
- `RP-Chat` bleibt Modulkontext im RP-Studio.
- Beide Kontexte duerfen nicht ueber dieselbe UI-Beschriftung oder impliziten Zustandsbesitz vermischt werden.

Kanonische Verweise
-------------------

- `novapolis-sim/README.md`
- `novapolis-dev/docs/todo.sim.md`
- `novapolis-dev/docs/process/sim-export-release-path.ssot.md`
- `novapolis-dev/docs/process/text-rpg-pre-rp-product-model-v1.ssot.md`
- `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md`
- `novapolis-sim/scripts/Main.gd`