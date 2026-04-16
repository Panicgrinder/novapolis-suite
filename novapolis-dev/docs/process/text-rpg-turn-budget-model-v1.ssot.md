---
stand: 2026-04-17 01:04
update: Die Quellenbasis fuehrt den archivierten Sim-Redirect nicht mehr; aktive Referenzen zeigen nur noch auf verbleibende Zielquellen.
checks: snapshot-lock PASS (2026-04-17 01:04); markdownlint=PASS; frontmatter=PASS
---

Text-RPG Turn-Budget-Referenzmodell v1
======================================

Zweck
-----

Diese SSOT fuehrt den ausdifferenzierten Referenzrahmen fuer Turn-Budget, Zeitableitung, Verdichtung und harte Blockaden. Sie ergaenzt den kompakten Vertragskern aus dem Sessionvertrag, ohne ihn zu ersetzen.

Scope
-----

- Referenz-Grundwerte fuer typische Handlungsklassen
- Modifikator-Matrix fuer Zustand, Umgebung, Hilfsmittel, Unterstuetzung und Routine
- Schwellenlogik fuer Budgetklassen und Verdichtungswechsel
- mechanische Referenzfaelle fuer Fragmentierung, Verdichtung und aufloesbare Blockaden

Nicht-Ziele
-----------

- kein Ersatz fuer den Sessionvertrag v1 als kanonischen Feld- und Antwortvertrag
- keine direkte Runtime-Implementierung oder API-Festschreibung ueber den kompakten Vertragskern hinaus
- keine RP-Lore-, Start- oder Weltdefinition

Quellenbasis
------------

- `novapolis-dev/docs/specs/text-rpg-session-contract-v1.md`
- `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md`
- `novapolis-dev/docs/specs/scheduler-spec.md`

Einordnung im Wahrheitsrahmen
----------------------------

- Der Sessionvertrag v1 bleibt die kanonische Quelle fuer `plan_analysis`, `budget_decision`, `time_state`, `turn_feedback`, `carry_over` und den aeusseren Turn-Rahmen.
- Diese SSOT fuehrt die ausdifferenzierten Referenzwerte und Ableitungsregeln, die oberhalb des kompakten Vertragskerns gebraucht werden, aber noch nicht als Runtime-Pflicht materialisiert werden sollen.
- Das Product Gate prueft weiter nur Drift gegen den kompakten Vertragskern und seine expliziten Klassen; diese SSOT ist die aktive Detailquelle fuer spaetere Nachzuege, Tests und Produktentscheidungen.

Mapping auf den kompakten Vertragskern
--------------------------------------

### Schrittklassen

- `sehr kurz` mappt auf `very_short` und deckt `1 bis 3 Minuten` ab.
- `kurz` mappt auf `short` und deckt `3 bis 10 Minuten` ab.
- `mittel` mappt auf `medium` und deckt `10 bis 20 Minuten` ab.
- `lang` mappt auf `long` und deckt `20 bis 30 Minuten` ab.
- `mehrstufig` mappt auf `multi_stage` und deckt alles oberhalb eines sauber einzelnen `30`-Minuten-Turns ab.

### Modifikatortypen

- Figurenzustand mappt auf `condition`.
- Umgebung, Stoerung, Druck und Gefahr mappen auf `environment`.
- Werkzeug- und Materiallage mappt auf `tools`.
- Helfer- und Parallelunterstuetzung mappt auf `support`.
- Vertrautheit und Routine mappen auf `routine`.
- Sequenzverlust und Uebergangsaufschlag mappen auf `transition`.

### Budgetklassen

- `innerhalb des Rahmens` mappt auf `within_frame`.
- `knapp drueber` mappt auf `slightly_over`.
- `deutlich drueber` mappt auf `significantly_over`.
- `unspielbar` mappt auf `blocked`.

Zeitmodell v0.2
---------------

### Grundregel

- Jede Handlung kostet Zeit.
- Auch kleine Handlungen sind nicht kostenlos, sondern haben mindestens einen Basisaufwand.
- Die KI soll Zeit nicht dramaturgisch beliebig, sondern moeglichst konstant, wiederholbar und aus Grundwert plus Modifikatoren ableiten.

### Basislogik der Zeitschaetzung

- Jede Handlung bekommt einen `Grundwert` in Minuten.
- Dieser Grundwert wird anschliessend durch reale Einflussfaktoren modifiziert.
- Fuer wiederkehrende Taetigkeiten wird spaeter derselbe Grundwert wiederverwendet und nur durch aktuelle Umstaende angepasst.
- Bei mehrteiligen Plaenen wird die Gesamtzeit zusaetzlich um einen `Uebergangsaufschlag` erhoeht.

### Vorlaeufige Einflussfaktoren

- Faehigkeiten und Eigenschaften der Spielfigur.
- Unterstuetzung durch andere beteiligte Personen.
- Werkzeuge, Materiallage und Vorbereitung.
- Entfernung, Wegzeit und Zugangsbedingungen.
- Umgebungszustand, Stoerungen, Gefahr und Druck.
- Vertrautheit mit der Taetigkeit.
- Erschoepfung, Verletzung oder sonstige Einschraenkungen.

### Referenz-Grundwerte fuer Standardhandlungen v0.1

- `kurzer Blick oder kurze verbale Reaktion`: `1 bis 2 Minuten`
- `einfache direkte Interaktion`: `3 bis 5 Minuten`
- `Bewegung innerhalb eines vertrauten Teilbereichs`: `5 bis 10 Minuten`
- `Werkzeug oder Material im Nahbereich organisieren`: `5 bis 10 Minuten`
- `kurze Sichtpruefung oder einfache Analyse`: `5 bis 10 Minuten`
- `gezielte Untersuchung mit mehreren Pruefschritten`: `10 bis 15 Minuten`
- `einfache manuelle Arbeit ohne Stoerung`: `10 bis 15 Minuten`
- `technische Standardarbeit mit Werkzeug`: `15 bis 25 Minuten`
- `komplexe Reparatur oder mehrgliedriger Eingriff`: `25 bis 30 Minuten`
- `mehrstufige Arbeit mit Vorbereitung, Eingriff und Test`: `ueber 30 Minuten`

### Leitregeln fuer die Nutzung der Referenzwerte

- Die Referenzwerte sind keine Spielerinformation, sondern interne Systemwerte fuer konsistente Ableitungen.
- Die KI darf einen Wert nur dann stark absenken oder anheben, wenn ein konkreter Modifikator dies traegt.
- Derselbe Handlungstyp soll unter vergleichbaren Umstaenden wieder auf denselben Grundwert zurueckfallen.
- Wenn eine Handlung aus mehreren verschiedenen Handlungstypen besteht, wird sie nicht als ein Gesamtblock gewertet, sondern in Einzelschritte zerlegt.

Modifikator-Matrix fuer die Zeitableitung v0.1
----------------------------------------------

### Zustand der Figur (`condition`)

- `ausgeruht und handlungssicher`: `-2 Minuten`, mindestens jedoch nicht unter `1 Minute` fuer den jeweiligen Schritt
- `leicht erschoepft oder leicht angeschlagen`: `+2 Minuten`
- `deutlich erschoepft oder verletzt`: `+5 Minuten`
- `stark eingeschraenkt`: `+10 Minuten` oder harte Blockade, wenn die Handlung real nicht mehr plausibel ist

### Umgebung und Druck (`environment`)

- `ruhig, hell, geordnet`: `0 Minuten`
- `dunkel, eng oder unaufgeraeumt`: `+2 Minuten`
- `chaotisch, laut oder unsicher`: `+5 Minuten`
- `akute Gefahr, Beschuss, Panik oder massiver Zeitdruck`: `+10 Minuten` oder Wechsel in Verdichtung, wenn unmittelbare Reaktionslogik wichtiger wird als Planlogik

### Hilfsmittel und Materiallage (`tools`)

- `passendes Werkzeug und Material voll verfuegbar`: `0 Minuten`
- `Werkzeug muss erst geholt oder vorbereitet werden`: `+3 Minuten`
- `behelfsmessig oder improvisiert`: `+5 Minuten`
- `notwendiges Werkzeug oder Material fehlt`: harte Blockade oder Plan muss umformuliert werden

### Unterstuetzung (`support`)

- `allein`: `0 Minuten`
- `gezielte Hilfe durch eine geeignete Person`: `-3 Minuten`
- `mehrere koordinierte Helfer`: `-5 Minuten`, sofern die Arbeit parallelisierbar ist
- `ungeeignete oder stoerende Hilfe`: `+3 Minuten`

### Vertrautheit und Routine (`routine`)

- `Routinehandlung im vertrauten Umfeld`: `-2 Minuten`
- `bekannt, aber nicht eingespielt`: `0 Minuten`
- `ungewohnt oder selten`: `+3 Minuten`
- `erstmals oder nur theoretisch bekannt`: `+6 Minuten`

### Leitregeln fuer die Modifikatoren

- Die Modifikatoren werden pro atomarem Schritt und nicht nur auf den Gesamtplan angewendet.
- Gleichartige Modifikatoren duerfen sich addieren, solange die Begruendung pro Schritt sichtbar bleibt.
- Wenn ein Modifikator eine Handlung praktisch unmoeglich macht, ersetzt die harte Blockade jede weitere Minutenrechnung.
- Negative Modifikatoren duerfen einen Schritt beschleunigen, aber nie auf `0 Minuten` senken.

Prioritaetslogik fuer Modifikatoren v0.1
----------------------------------------

1. Harte Blockade pruefen: Wenn Koerperlichkeit, Werkzeug, Zugang, Wissen oder soziale Position die Handlung real unmoeglich machen, endet die Auswertung ohne weitere Minutenrechnung.
2. Verdichtungsbedarf pruefen: Wenn unmittelbare Gegenreaktionen, akute Gefahr oder parallele Akteure die Lage bestimmen, wechselt die Auswertung von Planlogik auf Tick-Logik.
3. Zeitmodifikatoren anwenden: Nur wenn die Handlung weiter planbar bleibt, werden Minutenmodifikatoren auf den atomaren Schritt gerechnet.
4. Sequenzverlust addieren: Erst nach Schrittbewertung wird der Uebergangsaufschlag fuer Mehrschrittplaene addiert.

Eskalationsregeln fuer Verdichtung v0.1
--------------------------------------

- Ein Modifikator `akute Gefahr, Beschuss, Panik oder massiver Zeitdruck` zwingt nicht automatisch in Verdichtung, sondern nur dann, wenn dadurch unmittelbare Reaktionsfolgen im Minutentakt relevant werden.
- Ein sozialer oder physischer Konflikt mit moeglicher direkter Gegenreaktion hat Vorrang vor normaler Minutenrechnung und wird in Verdichtung ueberfuehrt.
- Reine Schwierigkeit ohne unmittelbare Gegenreaktion bleibt im normalen Turn und erzeugt nur Minutenaufschlaege.
- Eine Lage kann waehrend der Ausspielung von normaler Turn-Logik in Verdichtung kippen, wenn aus dem Resultat heraus ploetzlich unmittelbare Reaktionen entstehen.

Harte Blockade-Regeln v0.1
--------------------------

- `koerperlich unmoeglich`: Die Figur kann die Handlung in ihrem aktuellen Zustand real nicht ausfuehren.
- `werkzeugseitig unmoeglich`: Ein zwingend notwendiges Werkzeug oder Material fehlt vollstaendig.
- `zugangsseitig unmoeglich`: Der Zielort oder das Zielobjekt ist ohne vorherige Zusatzhandlung nicht erreichbar.
- `wissensseitig unmoeglich`: Die Figur kann die Handlung mangels Wissen, Kontext oder Bedienkenntnis nicht plausibel beginnen.
- `sozial unmoeglich`: Die Handlung scheitert bereits an Autoritaet, Rolle oder fehlender sozialer Zugriffsebene.

### Leitregeln fuer harte Blockaden

- Eine harte Blockade beendet die aktuelle Planbewertung fuer den betroffenen Schritt sofort.
- Harte Blockaden sollen konkret benannt werden und nicht nur als abstraktes `geht nicht` erscheinen.
- Wenn eine Blockade durch vorbereitende Teilhandlungen aufloesbar ist, soll die KI diese Teilhandlungen statt der blockierten Zielhandlung anbieten.
- Wenn die gesamte Handlungskette auf einem blockierten Kernschritt beruht, gilt der Gesamtplan als `unspielbar`.

Turn-Feedback-Mindestset v0.1
-----------------------------

- Jeder abgeschlossene Turn muss mindestens sichtbar machen, was erledigt wurde.
- Jeder abgeschlossene Turn muss sichtbar machen, was offen oder begonnen bleibt.
- Jeder abgeschlossene Turn muss mindestens ein unmittelbares Rueckmeldesignal enthalten: Zustandsaenderung, Reaktion, Risiko oder neuer Anschluss.
- Wenn keine direkte Weltreaktion sichtbar ist, muss stattdessen klar benannt werden, welche spaetere Folge angestossen wurde.
- Der Spieler soll nach jedem Turn wissen, was jetzt anders ist, was noch laeuft und worauf der naechste Schritt aufsetzt.

Budgetschwellen und Auslegung v0.1
----------------------------------

- `within_frame`: geplanter Gesamtaufwand `<= 30 Minuten`
- `slightly_over`: geplanter Gesamtaufwand `31 bis 40 Minuten`
- `significantly_over`: geplanter Gesamtaufwand `41 bis 60 Minuten`
- `blocked`: geplanter Gesamtaufwand `> 60 Minuten` oder logisch unmoeglich
- Wenn eine Einzeltaetigkeit fuer sich bereits ueber `30 Minuten` liegt, wird sie als `multi_stage` behandelt.
- Wiederkehrende Taetigkeiten sollen mit dokumentiertem Grundwert gespeichert werden; modifiziert wird dann nur noch die konkrete Situation.

### Schwellenlogik fuer die Budgetpruefung

- `within_frame` wird ohne Sonderdialog ausgespielt.
- `slightly_over` wird nur mit sichtbarer Fragmentierung ausgespielt: letzte Schritte fallen weg oder bleiben begonnen und offen.
- `significantly_over` fuehrt zu einem klaren Hinweis, dass der Plan nicht sauber in den Turn passt; der Spieler muss kuerzen oder die Fragmentierung bewusst bestaetigen.
- `blocked` bedeutet entweder zeitlich unspielbar oder logisch unmoeglich; in beiden Faellen greift eine harte Blockade.

### Realitaetsgruende fuer harte Blockaden

- fehlende Mittel
- falsche Annahmen ueber die Lage
- physikalische oder soziale Unmoeglichkeit

Referenzfaelle
--------------

- Die folgenden Referenzdurchlaeufe dienen als aktive Detailreferenz fuer Fragmentierung, Verdichtung und aufloesbare Blockaden.
- Sie sind kein Lore-Kanon, sondern mechanische Belegfaelle fuer Ablauf, Bewertung, Ausspielung und Rueckmeldung.

### Referenzfall A - Normaler 30-Minuten-Turn ohne Verdichtung

#### Ausgangslage Referenzfall A

- Die Figur befindet sich in einem vertrauten Wartungsbereich.
- Ein Ventil in Abschnitt C6 zeigt Druckverlust, aber keine akute Gefahr.
- Werkzeug ist in der Naehe verfuegbar, die Umgebung ist eng und leicht unaufgeraeumt.

#### KI-Lagebild Referenzfall A

- `Im Wartungsgang C6 hoerst du weiter das unruhige Zischen aus dem linken Leitungsstrang. Das Ventil verliert Druck, aber noch haelt das System. Dein Werkzeugschrank steht am Ende des Gangs, der Zugang zur Leitung ist frei.`

#### Spielerplan Referenzfall A

- `Ich hole das passende Werkzeug, oeffne die Wartungsklappe, pruefe das Ventil, ziehe die lockere Verbindung nach und teste danach kurz, ob der Druck stabil bleibt.`

#### Zerlegte Handlungsschritte

1. Werkzeug holen
2. Wartungsklappe oeffnen
3. Ventil sichten und Schaden pruefen
4. Verbindung nachziehen
5. kurze Druckprobe

#### Abgeleitete Bewertung

- `Werkzeug holen`: `8 Minuten`; Modifikator Umgebung leicht unaufgeraeumt `+2`; Ergebnis `10 Minuten`
- `Wartungsklappe oeffnen`: `3 Minuten`
- `Ventil pruefen`: `8 Minuten`; Modifikator vertrautes Umfeld `-2`; Ergebnis `6 Minuten`
- `Verbindung nachziehen`: `10 Minuten`
- `Druckprobe`: `4 Minuten`
- `Uebergangsaufschlag`: `3 Minuten`
- Gesamtwert: `36 Minuten`

#### Budgetentscheidung

- Klasse: `slightly_over`
- Systemausgabe: `Das ist etwas mehr, als in diesen Turn sauber hineinpasst. Ich kann den Plan anspielen, aber die letzten Schritte bleiben wahrscheinlich begonnen oder offen.`

#### Spielerentscheidung

- Der Spieler bestaetigt die fragmentierte Ausspielung.

#### Ausspielung

- Werkzeug wird geholt.
- Wartungsklappe wird geoeffnet.
- Das Ventil wird geprueft und die lockere Verbindung identifiziert.
- Die Verbindung wird nachgezogen.
- Fuer die vollstaendige Druckprobe reicht die Restzeit nicht mehr; sie wird begonnen, aber nicht sauber abgeschlossen.

#### Turn-Ergebnis Referenzfall A

- `completed`: Werkzeug holen, Wartungsklappe oeffnen, Ventil pruefen, Verbindung nachziehen
- `started`: Druckprobe
- `open`: keine weiteren Schritte

#### Carry-Over Referenzfall A

- `Druckprobe C6`: begonnen, Leitung offen, Werkzeug liegt bereit, Wiederaufnahme verkuerzt

#### Mindestfeedback Referenzfall A

- sichtbar geschafft: Verbindung stabilisiert
- sichtbar offen: Druckprobe nicht abgeschlossen
- unmittelbare Weltreaktion: Zischen nimmt ab, aber die Stabilitaet ist noch nicht bestaetigt
- naechster Anschluss: Druckprobe im Folgeturn sauber zu Ende bringen

### Referenzfall B - Turn mit Verdichtungswechsel

#### Ausgangslage Referenzfall B

- Die Figur spricht in einem engen Gang mit einem angespannten NPC ueber knappe Vorratsausgabe.
- Die Lage ist sozial aufgeladen, aber zunaechst noch planbar.

#### KI-Lagebild Referenzfall B

- `Der Versorgungshelfer vor dir wirkt uebernaechtigt und gereizt. Hinter ihm warten zwei weitere Personen, und du merkst, dass jede falsche Formulierung die Stimmung kippen lassen kann.`

#### Spielerplan Referenzfall B

- `Ich spreche ihn ruhig an, erklaere die Lage, versuche ihn zu beruhigen und will danach mit ihm die Ausgabe kurz neu ordnen.`

#### Erste Budgetbewertung

- Der Plan ist zunaechst als sozialer Mehrschrittplan lesbar.
- Bevor die volle Minutenrechnung abgeschlossen wird, kippt die Lage durch unmittelbare Gegenreaktion in Verdichtung.

#### Verdichtungsstart

- Systemausgabe: `Die Lage kippt in unmittelbare Reaktion. Ab jetzt zaehlt jede Minute einzeln.`

#### Tick-Folge

- Tick 1: Wahrnehmung `Der NPC hebt die Stimme und tritt einen halben Schritt naeher.`; Spieleraktion `beschwichtigen`; Reaktion `Er zoegert, bleibt aber angespannt.`
- Tick 2: Wahrnehmung `Eine wartende Person mischt sich ein.`; Spieleraktion `klare Prioritaet setzen`; Reaktion `Die zweite Person weicht verbal zurueck, der NPC bleibt fokusiert.`
- Tick 3: Wahrnehmung `Der unmittelbare Druck sinkt leicht.`; Spieleraktion `konkrete Neuordnung der Ausgabe vorschlagen`; Reaktion `Der NPC nickt knapp und laesst dich ausreden.`
- Tick 4: Wahrnehmung `Keine direkte Eskalation mehr, Lage stabilisiert sich.`; Reaktion `Verdichtungsende wird moeglich.`

#### Verdichtungsende

- Systemausgabe: `Die akute Lage beruhigt sich. Fuer diesen Turn bleiben noch 26 Minuten planbare Zeit.`

#### Restliche Ausspielung

- Die Figur ordnet die Ausgabe fuer die naechsten Minuten neu.
- Die wartende Gruppe beruhigt sich vorlaeufig.

#### Turn-Ergebnis

- `completed`: erste Deeskalation, Ausgabe kurz neu geordnet
- `interrupted`: keine technische Unterbrechung, aber soziale Spannung bleibt als Folgezustand bestehen
- `open`: laengerfristige Versorgungsklaerung

#### Carry-Over

- `Versorgungskonflikt Gang Nord`: offen, soziale Spannung reduziert, Vertrauen des Helfers fragil, weitere Klaerung noetig

#### Mindestfeedback

- sichtbar geschafft: akute Eskalation verhindert
- sichtbar offen: Versorgungslage bleibt instabil
- unmittelbare Weltreaktion: Gruppe beruhigt sich, NPC bleibt angespannt
- naechster Anschluss: Konflikt kann im naechsten Turn wieder als normaler Plan oder erneut verdichtet weiterlaufen

### Referenzfall C - Harte Blockade mit vorbereitender Teilhandlung

#### Ausgangslage

- Die Figur will ein verriegeltes Technikdepot hinter einer Sicherheitstuer oeffnen, um dort einen Spannungsregler auszutauschen.
- Der Zugang ist nicht frei; die Figur hat weder Autorisierung noch das passende Override-Werkzeug.
- In unmittelbarer Naehe befindet sich jedoch ein Aufsichtsposten, an dem ein temporaerer Wartungsschluessel ausgegeben werden koennte.

#### KI-Lagebild

- `Vor dir sitzt die verriegelte Sicherheitstuer zum Technikdepot. Ohne Freigabe oder passenden Override kommst du an den Regler dahinter nicht heran. Zwei Gaenge weiter ist noch der Aufsichtsposten besetzt.`

#### Spielerplan

- `Ich gehe direkt an die Tuer, oeffne das Depot und tausche sofort den Spannungsregler aus.`

#### Blockadebewertung

- Kernschritt `Depot oeffnen` scheitert an `zugangsseitig unmoeglich`.
- Der Folgeeingriff `Spannungsregler austauschen` ist ohne diesen Zugang ebenfalls nicht spielbar.
- `budget_decision.class`: `blocked`
- `hard_block`: `true`

#### Systemausgabe bei Blockade

- `So kommst du hier im Moment nicht hinein: Die Sicherheitstuer blockiert den Zugang zum Depot, und dir fehlt die noetige Freigabe oder ein passendes Override-Werkzeug. Du koenntest stattdessen zuerst am Aufsichtsposten einen Wartungsschluessel besorgen oder eine Freigabe erbitten.`

#### Alternativpfad des Spielers

- `Dann gehe ich zuerst zum Aufsichtsposten und versuche, fuer die Reparatur einen temporaeren Wartungsschluessel zu bekommen.`

#### Neubewertung des Alternativpfads

- `zum Aufsichtsposten gehen`: `6 Minuten`
- `Lage erklaeren und Freigabe erbitten`: `5 Minuten`
- `Wartungsschluessel uebernehmen und Rueckweg antreten`: `7 Minuten`
- `Uebergangsaufschlag`: `2 Minuten`
- Gesamtwert: `20 Minuten`

#### Budgetentscheidung Referenzfall C

- Klasse: `within_frame`
- Systemausgabe: `Das passt in den aktuellen Turn. Ich spiele zuerst die vorbereitende Freigabe aus; der eigentliche Reglertausch kann danach sauber geplant werden.`

#### Ausspielung Referenzfall C

- Die Figur erreicht den Aufsichtsposten.
- Nach kurzer Begruendung erhaelt sie einen temporaeren Wartungsschluessel.
- Der Schluessel wird fuer den naechsten Zugriff bereitgehalten; der Reglertausch selbst beginnt in diesem Turn noch nicht.

#### Turn-Ergebnis Referenzfall C

- `completed`: Aufsichtsposten erreicht, Freigabe erbeten, Wartungsschluessel erhalten
- `started`: keine
- `open`: Spannungsregler im Technikdepot austauschen

#### Carry-Over Referenzfall C

- `Depotzugang Techniksektor`: offen, Wartungsschluessel fuer den Folgeturn vorhanden, Zugang jetzt prinzipiell vorbereitet
- `Spannungsregler austauschen`: offen, Blockade aufgeloest, eigentliche Reparatur noch nicht begonnen

#### Mindestfeedback Referenzfall C

- sichtbar geschafft: Die urspruengliche Zugangsblockade ist praktisch aufgeloest.
- sichtbar offen: Der eigentliche Reglertausch steht noch aus.
- unmittelbare Weltreaktion: Der Aufsichtsposten erkennt die Wartung als plausibel an und gibt begrenzte Freigabe.
- naechster Anschluss: Der Folgeturn kann mit vorbereitetem Zugang direkt in die Reparaturplanung gehen.

Definition of Done
------------------

- Die ausdifferenzierte Zeit-, Budget- und Verdichtungslogik liegt nicht mehr nur als Rest in der Sim-Planungs-SSOT, sondern als eigene aktive Prozessquelle.
- Mapping auf `step_class`, Modifikatortypen und Budgetklassen des Sessionvertrags ist explizit benannt.
- Referenzfaelle fuer Fragmentierung, Verdichtung und harte Blockaden sind als aktive Detailbelege dokumentiert.