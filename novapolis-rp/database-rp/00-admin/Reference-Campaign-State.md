---
stand: 2026-02-04 21:17
update: Projekt-Link auf Fraktionspfad normalisiert.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-02-04 21:23); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp/database-rp/00-admin PASS (2026-02-04 21:23)
slug: reference-campaign-state
category: Admin
canvas: campaign-state
---

Reference: Campaign State (ausgelagert)
=====================================

Zweck: Sammelstelle für veränderliche Details (Inventar, Status, Timeline-Skizzen), die bewusst **nicht** im Canon-Core (`memory-bundle.md`) stehen.

Start here: [Current-State.md](./Current-State.md)

Mechanik (Reference): Symbiose-Energie (SE) - Pools (Reflex-System)
---------------------------------------------------------------

Ziel: Support-/Exo-Verbrauch als **temporäre Kapazität** modellieren, ohne Menschen mit Zahlen-Tracking zu belasten.

Grundsätze
----------

- SE ist eine **Reflex-interne Ressource** (Reflex + Instanzen). Menschen haben keinen eigenen SE-Pool.
- Pools sind **strikt getrennt**: keine direkte Übertragung/„Umladung“ zwischen Reflex, Lumen, Echo oder zukünftigen Instanzen.
- „Kompatibilität mit Entwicklung“: Wachstum/Training ist pro Entität getrennt (physisch: Pool/Regeneration; mental: Kontrolle/Trigger).

Poolgrößen (Startwerte, größenbasiert)
--------------------------------------

Diese Werte sind bewusst klein skaliert (spielbar, wenig Buchhaltung):

- Reflex (Primär, groß): `SE_max = 12`
- Echo (Instanz, mittel): `SE_max = 8`
- Lumen (Instanz, klein): `SE_max = 6`

Regel für zukünftige Instanzen:

- Bei Aktivierung wird ein `SE_max` vergeben, abhängig von physischer Größe/Trägervolumen:
  - klein: 5-7
  - mittel: 8-10
  - groß: 11-13
- Der Wert wird im jeweiligen Charakter-Canvas dokumentiert.

Verbrauch (Heuristik)
---------------------

SE-Kosten pro „Einsatz“ (ein klar abgegrenzter Schutz-/Support-Impuls) sind kategorisiert:

- leicht: 1 SE (Feinmotorik, kurzer Scan, leichte Dämpfung)
- mittel: 2 SE (stabiler Schutzschirm, merkliche Kraft-/Dämpfungsverstärkung)
- stark: 3 SE (Notfall-Kokon, starke Abschirmung, längere Hochleistung)

Überlastung & Bonus-Regeln
--------------------------

- Wenn `SE_aktuell` unter 25% von `SE_max` fällt: **Bonus/Verstärkungen entfallen**, es bleibt nur Grundschutz/Grundfunktion.
- Wenn `SE_aktuell` 0 erreicht: Entität geht in Schonmodus (Rückzug auf Grundschicht), bis Regeneration greift.

Regeneration (einfach)
----------------------

- Ruhig/ohne Einsatz: +1 SE pro 30 Minuten.
- „Reset“: nach einem echten Ruheblock (z. B. Schlaf-/Regenerationsfenster, SL-Entscheid) wieder auf `SE_max`.

Instanzen (Reference): Wissensstand & Persönlichkeit
---------------------------------------------------

Entscheidung (INSTANCES)
------------------------

- Bei der Entstehung einer Instanz wird ein **Wissensstand als Snapshot** übernommen: die Instanz startet mit dem Wissen des erzeugenden Trägers zum Zeitpunkt $t_0$ (Reflex, Lumen, Echo oder spätere Instanz).
- **Persönlichkeit wird nicht kopiert**: Die Instanz ist eine eigenständige Person/Entität. Sie teilt Grunddispositionen (z. B. "chaotisch gut", Verlustangst/Nähebedürfnis), aber die Entwicklung beginnt erst ab $t_0$.
- Danach gilt: Wissen/Erfahrung **divergieren**. Es gibt **keinen automatischen Wissensabgleich** zwischen Trägern.

Wissensabgleich (optional, bewusst)
----------------------------------

- Spätere Wissensübertragung ist nur als **bewusster Austausch** möglich (Kommunikation/Training/Protokolle), nicht als Hintergrund-Sync.
- Wenn ein formaler Abgleich benötigt wird, wird er als eigener Schritt dokumentiert (z. B. im Trainingsstand/Log), inklusive "was wurde geteilt".

Training/Achsen (langfristig kompatibel)
----------------------------------------

- Physisch: SE-Pool/Regeneration bleibt strikt getrennt pro Entität.
- Mental/Verhalten: Kontrolle/Trigger/Consent werden pro Instanz trainiert (Einfluss der Bezugsperson ist zentral).
- Spezialisierung: Jede Instanz hat eine Hauptfähigkeit/Scope, der nicht automatisch auf andere Träger übergeht.

Mechanik (Reference): Nähe-Kopplung (PROXIMITY)
----------------------------------------------

Ziel: Eine spielbare Proximity-Regel für die Bezugspaare **Reflex↔Ronja**, **Lumen↔Jonas**, **Echo↔Kora**.

Grundannahmen (REFLEX-SPEECH)
-----------------------------

- Proximity ist **tatsächliche Nähe** (Distanz, optional Kontakt). Sie wirkt als Stabilitätsanker.
- Proximity hat zwei Treiber: **Zuneigung/Bindung** (Affektion) und **Schutz/Bedrohung** (Guard).
- Proximity ist **situativ** (Zustand wechselt je nach Lage); Intensität und Verhalten unterscheiden sich zwischen Reflex und Instanzen.

Zustände (Heuristik)
--------------------

- `CALM`: Affektionsnähe dominiert. Nähe wird aktiv gesucht, um Bindung/Regulation zu stabilisieren.
- `ALERT`: Unbekanntes/Risiko. Distanzfenster wird enger; Schutzpositionierung nimmt zu.
- `CRISIS`: Akute Selbst-/Fremdgefährdung. Schutzhandlungen dürfen kurzfristig übergriffig werden, bis die unmittelbare Gefahr gebrochen ist; danach Deeskalation.

Distanzfenster (Startwerte)
---------------------------

Diese Werte sind Startwerte, nicht „hart“; Anpassung über Training.

- Lumen↔Jonas: bevorzugt <= 20 m (Werkstatt-/Arbeitsfenster). > 20 m: Unruhe/Schonmodus-Trigger.
- Echo↔Kora: bevorzugt <= 10 m (C6/Alarmfenster). > 20 m: Schonmodus-Trigger.
- Reflex↔Ronja: bevorzugt sehr eng (Körperkontakt/unter ~3 m), insbesondere in `ALERT/CRISIS`.

Distanzfolgen (spielbar)
------------------------

- Wenn das bevorzugte Fenster länger überschritten wird: steigende Unruhe, Fokusverlust, Rückzug/Schonmodus.
- Schonmodus bedeutet: Minimalfunktionen (Grundschutz, Beobachten), weniger Initiative und weniger „Feinsteuerung“.

Training (Ziele)
----------------

- Instanzen: Stabilität bei Distanz verbessern (z. B. auf 30-50 m mit Sicht/Funkkontakt), ohne Arbeitsfähigkeit zu verlieren.
- Reflex: Deeskalation/Stop-Reaktion verbessern und Eskalationen kürzer halten.

Scope-Unterschiede
------------------

- Reflex (Primär): stärkster Affektions- und Schutztreiber; in `CRISIS` darf er kurzfristig blockieren/abschirmen (z. B. Bewegung unterbinden, Kokon/Abschirmung), um Leben zu sichern.
- Instanzen (Lumen/Echo): Nähe wird gesucht (Affektion), Schutzhandlungen bleiben **lokal und kurz** (z. B. Hand stoppen, Sichtlinie schützen), um Arbeitsfähigkeit und Alltag zu ermöglichen.

Mechanik (Reference): Reflex Sprache/Audio (REFLEX-SPEECH)
--------------------------------------------------------

Ziel: Eine klare, spielbare Sprach-/Audio-Regel für Reflex, ohne Widerspruch zu Symbiose-Stufe I.

Grundannahmen
-------------

- Reflex kann Informationen als "Stimme" übermitteln, ohne akustisch im Raum zu sprechen.
- Es gibt zwei Kanäle: **Privatkanal (Ronja-only)** und **Broadcast (über Technik)**.

Kanal A: Privatkanal (Ronja-only, Tympanon-Kopplung)
----------------------------------------------------

- Reflex koppelt sich an Ronjas Hörsystem ("Tympanon") und erzeugt einen internen Schall-/Signalreiz, den **nur Ronja** als Stimme wahrnimmt.
- Das ist **kein Raumklang**: Außenstehende hören nichts.
- Default-Regel: Aktivierung nur mit Ronjas Freigabe (Signal/Consent). Ronja kann jederzeit abbrechen ("Stop" / "Signal aus").

Kanal B: Broadcast (über Geräte)
-------------------------------

- Reflex kann sich an ein technisches Gerät koppeln (z. B. Ohrhörer/Headset/Funkgerät/Intercom/Telefon) und darüber Audio ausgeben.
- Wer das Gerät nutzt bzw. es hören kann, hört Reflex ("Broadcast").

Dauer & Erschöpfung (Heuristik)
-------------------------------

- "Ping" (Sekunden, Warnung/Signal): jederzeit möglich, sehr geringe Belastung.
- "Satz" (kurz, <= 1 Minute): geringe Belastung.
- "Gespräch" (mehrere Minuten): merkliche Belastung → Pausen einplanen.
- "Dauerkanal" (lange Kopplung): nicht als Default; nutzt sich ab (kognitiv/sensorisch) und erhöht Dysregulationsrisiko.

Kosten/Limitierung (kompatibel mit SE)
--------------------------------------

- Privatkanal und Broadcast zählen als **leichte bis mittlere** Aktivität (je nach Dauer/Intensität).
- Bei niedriger SE (nahe Schonmodus) wird Kommunikation **kurz, selten, priorisiert** (Warnungen/Essentials vor Smalltalk).

Consent & Notfall-Override
--------------------------

- Im Normalfall gilt: Privatkanal nur mit Consent; Abbruchwunsch wird respektiert.
- In `CRISIS` (akute Selbst-/Fremdgefährdung) darf Reflex **kurz** ("Notfall-Ping") auch ohne vorherige Freigabe warnen, wenn dies unmittelbar lebensrettend ist.
- Nach Ende der Akutlage gilt sofort wieder: Consent + Deeskalation + Pause.

Mechanik (Reference): Schutz-Übernahme (REFLEX-CONTROL)
------------------------------------------------------

Ziel: Eine klare, spielbare Regel für Schutz-Übernahme und Rückgabe, die Reflex' Überreaktionsrisiko begrenzt.

Grundsatz (Decision, REFLEX-CONTROL)
-----------------------------------

- **Rückgabe/Entkopplung erfolgt erst, wenn die Situation als "Sicher" eingeschätzt wird (nicht früher).**

Definition "Sicher" (Heuristik)
-------------------------------

"Sicher" bedeutet als Mindeststandard:

- keine akute Bedrohung mehr (kein unmittelbarer Angriff/Absturz/Erstickung/Brand),
- Ronja ist wieder handlungs- und entscheidungsfähig (Atmung/Orientierung stabil),
- Umgebung ist stabil genug, dass ein Loslassen nicht sofort wieder in `CRISIS` kippt.

Stop / Deeskalation
-------------------

- Ronjas "Stop" ist ein **Deeskalationssignal**: Reflex reduziert Druck/Blockaden auf das notwendige Minimum.
- **Volle Entkopplung** erfolgt trotzdem erst bei "Sicher".

Scope & Kosten (kompatibel)
---------------------------

- Schutz-Übernahme ist `CRISIS`-verknüpft (akute Selbst-/Fremdgefährdung) und soll zeitlich kurz bleiben.
- Bei niedriger SE (nahe Schonmodus) wird Kontrolle grober und kürzer; Rückgabe-Check bleibt Pflicht.


Mechanik (Reference): Detachment & Beweglichkeit (REFLEX-DETACH)
---------------------------------------------------------------

Ziel: Widerspruchsfrei festlegen, was "Trennung" bedeutet (Primärinstanz vs Instanzen) und welche kurzen Sonderfälle spielbar sind.

Grundsatz (Decision)
--------------------

- **Reflex (Primärinstanz) bleibt immer mit Ronjas Körper verbunden.** Keine vollständige Trennung.
- **Instanzen (z. B. Lumen/Echo) sind an ihre Bezugsperson gekoppelt**, dürfen aber in sicheren Kontexten kurzzeitig ohne permanenten Körperkontakt im Nahbereich agieren.

Reflex (Primärinstanz, Ronja)
-----------------------------

- "Strecken/Seestern" ist erlaubt als **Umpositionierung ohne Entkopplung** (Ausbreiten, Umgreifen, Abstützen, Abschirmen), aber Reflex bleibt durchgehend Teil der anliegenden Symbiose.
- Reflex erzeugt dabei **keine frei laufende, eigenständige Teil-Instanz** außerhalb Ronjas.
- Wenn ein Vorgang eine echte Abtrennung erfordern würde, gilt: **nicht möglich** (stattdessen: Werkzeug/Person anfordern, oder Instanzen nutzen, falls vorhanden).

Instanzen (Lumen/Echo): lokales Agieren ohne Dauer-Körperkontakt
--------------------------------------------------------------

- Default: Nähe/Regulation über Kontakt bzw. sehr kurze Distanz (siehe PROXIMITY-Startwerte). "Trennung" im Sinn dieser Regel meint: **kein dauerhafter Körperkontakt**, nicht "weit weg".
- Erlaubt: kurzzeitig im Nahbereich bewegen (z. B. Werkstatt-/Verwaltungsaufgabe, Material reichen, Sensorcheck), solange der Kontext **sicher** ist.

Kosten/Limitierung (SE-kompatibel, Heuristik)
---------------------------------------------

- Ohne externe Energiequelle steigt der Aufwand deutlich: lokales Agieren ohne Kontakt zählt als **zusätzliche Belastung** (SE-Verbrauch steigt schneller; Schonmodus wird wahrscheinlicher).
- Mit externer Energiequelle/Anker (z. B. Werkbank/Station-Power/geladenes Modul) ist lokales Agieren **länger und stabiler**, ohne dass SE-Pools zwischen Entitäten übertragen werden.
- Wenn die Instanz Unruhe/Stress zeigt oder "Stop" kommt: **sofort zurück in Nähe/Kontakt**; bei Überschreiten des eigenen Distanzfensters kippt sie in Schonmodus.


Mechanik (Reference): Kontakt-Guard / Eifersuchts-Guard (JEALOUSY-GLOVES)
------------------------------------------------------------------------

Ziel: Eine spielbare, "süße" Jealousy-Detailregel, die **körperlichen Kontakt** konsensbasiert behandelt und unangenehme Dynamiken vermeidet.

Grundsatz (Decision, JEALOUSY-GLOVES)
------------------------------------

- Reflex (und Instanzen bei ihrer Bezugsperson) darf als Reaktion auf unerwünschten Körperkontakt einen **Kontakt-Guard** bilden: Er legt sich **nicht nur als Handschuh über die Haut**, sondern kann die **konkret betroffene Körperstelle** (z. B. Schulter, Arm, Hand, Rücken) mit einer dünnen Schicht **bedecken/abschirmen**, sodass der Kontakt nicht direkt zustande kommt.
- Der Kontakt-Guard ist **Blockade/Barriere**, keine Bestrafung: kein Schmerz, keine Luft-/Sichtblockade, kein "Festhalten" als Default.

Consent, Stop, Freigabe
-----------------------

- **Consent-first:** Kontakt-Guard ist im Normalfall nur aktiv, wenn die Bezugsperson das möchte (oder es als "süßes" Verhalten akzeptiert).
- **"Stop" beendet sofort** den Kontakt-Guard (Deeskalation auf 0), sofern keine akute Gefahr vorliegt.
- **"Freigabe"** (oder eine von der Bezugsperson definierte Freigabe-Phrase) erlaubt den Kontakt: Reflex/Instanz zieht sich an der Stelle zurück.

Eskalation (Heuristik)
----------------------

- Default ist erst Signal/Warnung (Kribbeln/Kälte), dann erst Bedecken der Stelle.
- Wenn wiederholt versucht wird, die Grenze zu übergehen, wird die Barriere dichter und Reflex/Instanz fordert explizit Freigabe oder Abstand.
- Wenn es **keine Jealousy-Situation**, sondern eine **Bedrohung/Übergriff** ist, greifen die Schutzregeln aus `REFLEX-CONTROL` (CRISIS) statt JEALOUSY-GLOVES.


Admin/Canon-Policy (Reference): Neue Entitäten / "Lebewesen"
------------------------------------------------------------

Grundsatz
---------

- Es gibt ohne Adminfreigabe **kein** weiteres neues/undefiniertes Lebewesen außer **Reflex** (inkl. Instanzen wie Lumen/Echo).
- Hinweise wie "Lebewesen unter dem Boden" (C6) sind bis zur Adminfreigabe als **Artefakt/Noise/Gerücht** zu behandeln und werden nicht als Canon-Entität etabliert.

Praxis
------

- Wenn so ein Hinweis im Spiel auftaucht: maximal als Signalrauschen in Narrative/Logs notieren (ohne neue Spezies/Entität zu definieren).
- Erst nach expliziter Adminfreigabe darf daraus eine neue Entität werden.

Externe Handschuhe / Kleidung
-----------------------------

- Externe Handschuhe sind als **Arbeits-/Witterungsschutz** grundsätzlich ok.
- Wenn Kontakt-Guard aktiv ist, hat die Schutzschicht Priorität: Reflex/Instanz legt sich an der **betroffenen Stelle** so, dass der unerwünschte Kontakt zuverlässig blockiert wird (auch über Stoff/Handschuh möglich).


Währung (Reference): "Kugeln" (neu vs gebraucht)
-------------------------------------------

Ziel: Eine klare, spielbare Regel für Munition als Währung, ohne harte Buchhaltung.

Grundsatz (Decision, KUGELN)
---------------------------

- "Kugeln" ist die **Standard-Währungseinheit** im Feld, weil Munition universell gebraucht wird.
- Es gibt zwei Wertstufen:
  - **Kugeln (neu)**: neuwertig/zuverlässig (z. B. original verpackt, sauber gelagert, geprüft) → **hochwertige Währung**.
  - **Kugeln (gebraucht)**: wiederaufbereitet/alt/uneinheitlich (z. B. nachgegossen, nachgeladen, gemischte Herkunft) → **Alltags-Währung**.

Umrechnung (Faustregel)
-----------------------

- **1 Kugel (neu) äquivalent zu ~10 Kugeln (gebraucht)**.
- Die Quote kann je nach Lage/Vertrauen/Charge schwanken (z. B. 1:8 bis 1:12), aber **1:10** ist der Default.

Qualität & Risiko (gebraucht)
-------------------------------

- Gebrauchte Kugeln sind **die häufigste Hauptmunition** im Alltag.
- Qualität schwankt: Aussetzer/Misfire/ungleiches Pulver sind möglich. Im Zweifel wird bei wichtigen Einsätzen **neu** bevorzugt.
- Bei Handel kann "gebraucht" je nach sichtbarer Qualität (sauberer Sitz, identische Hülsen, geprüft) auf- oder abgewertet werden.

Praxis (SL/Spielbarkeit)
------------------------

- Kleine Einkäufe/Service laufen meist in **gebraucht**.
- Größere Deals, kritische Ressourcen oder Vertrauenshandel laufen eher in **neu** (oder in gemischten Paketen).


Projekt (Reference): Draisine-/Transportmodul (D5 Prototyp)
----------------------------------------------------------

Kontext
-------

- Vor RP-Abbruch wurde in D5 ein kleiner Draisine-/Transportmodul-Prototyp begonnen.
- Träger/Owner: Jonas (Bau/Integration), mit Sicherheits-/Systemreview durch Pahl.

Status (Reference)
------------------

- Status: **prototyping** (noch kein abgesicherter Feldtest).
- Ziel: Ein **konservativer Material-/Transport-Usecase** für Nordlinie (D5↔C6), nicht "schnell" und nicht als Dauerdienst.

Gates (erster Testlauf)
-----------------------

- Tunnel-Abschnitt ist freigegeben (Sicherung/Belüftung/Statik ok) → `Nordlinie-01`.
- Not-Aus/Stop-Protokoll definiert (Stopp-Punkte, Rückzug, Rollen).
- Lastgrenzen konservativ (Erstlauf ohne Personentransport, außer explizit freigegeben).
- Logpflicht: Missionslog + Logistik (Materialverbrauch, Schäden, Lessons Learned).

Link
----

- Projekt-Canvas: [Draisine-Transportmodul](../01-factions/novapolis/05-projects/Draisine-Transportmodul.md)


Inventar / Ressourcen (Arbeitsstand)
------------------------------------

- D5-Inventar gepflegt.
- C6-Funde verbucht (Filter, Energiezellen, Werkzeuge); Versorgungsschwerpunkte mit Marei abgestimmt.
- Fehlend/Offen: Schweißausrüstung, Adapter DN60. Hydrofilter-Behälter als Reserve.

Fortschritt (Reporting-Detail)
------------------------------

- Nordlinie 01 berichtet getrennt: Erkundung / Sicherung / Betrieb (0-100%).

Timeline-Skizze (aus ehem. Core-Block)
--------------------------------------

Hinweis: Diese Sequenz ist eine **Skizze** und muss an das finale T+0-Fenster in [Canvas-T+0-Timeline](./Canvas-T+0-Timeline.md) angepasst werden.

1. Erwachen D5 → Selbstcheck → Wartungsauftrag.
2. Erstkontakt Reflex, Dämpfungs-Test, Regeln.
3. C6: Funk/Scan, Reaktorstabilisierung, Suche/Leichenfund; Evakuierungsaufnahme (20 Personen) gemeinsam mit Marei.
4. D5: Wiederaufbau; Jonas eingebunden; Pahl in Pflege.
5. Projektstart „Nordlinie 01“; Vorratsläufe; Überwachung an C6.

Offene Fäden (Detail)
---------------------

- Nordlinie 01: Schweißgerät, DN60-Adapter, Statikprüfung.
- C6: Überwachungssplitter auswerten; eventuelle Überlebende.
- E3: Anomalie „E3-Gefahr“ untersuchen; Reaktivierungsplan abstimmen.
- Reflex-Forschung: Sensorik, Trägerarchitektur („Wirbelsäule“), Exo-Prototyp.
- Fraktionen: Signale/Beobachtungen sammeln.
- Jonas: Vertrauen festigen; Werkstatt einrichten.
- Hydrofilter: Aufbereitung/Tests.

Links
-----
- Canon-Core → ./memory-bundle.md
- Timeline (T+0) → ./Canvas-T+0-Timeline.md
- Szene (T+0 Status-Ping) → ../06-scenes/scene-2025-10-27-a.md
- Nordlinie 01 → ../05-projects/Nordlinie-01.md
- Inventar (Fraktion) → ../04-inventory/Novapolis-inventar.md
