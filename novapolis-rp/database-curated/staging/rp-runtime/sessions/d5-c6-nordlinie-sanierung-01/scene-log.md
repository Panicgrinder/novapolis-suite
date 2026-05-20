---
stand: 2026-05-20 17:42
update: Turn 15 spielt Reflex' Wahrnehmung zwischen bestaetigter Naehe und kantigem Weltendruck aus, ohne technischen Fortschritt.
checks: snapshot-lock PASS (2026-05-20 17:42); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-05-20 17:42); .\.venv\Scripts\python.exe scripts\check_frontmatter.py changed-md PASS (EXITCODE=0, 2026-05-20 17:42); .\.venv\Scripts\python.exe scripts\check_todo_index_sync.py PASS (2026-05-20 17:42); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-05-20 17:42); git diff --check PASS (CRLF warnings only, 2026-05-20 17:42).
---

Scene Log - D5 C6 Nordlinie Sanierung 01
========================================

Meta
----

- session_id: d5-c6-nordlinie-sanierung-01
- status: active
- canon_state: Probe
- review_state: working
- perspective: Ronja im Tunnelarbeitskorridor zwischen D5 und C6
- location: Verbindungstunnel D5-C6, D5-seitiger Sanierungsabschnitt
- tone: nuechtern, handwerklich, angespannt
- mood: kontrollierte Konzentration unter Infrastruktur- und Materialdruck

Scene Log
---------

Turn 1
------

- input: Ronja beendet zuerst gewissenhaft den laufenden Abschnitt, gibt danach den bearbeiteten Stand und den Materialbedarf nach D5 durch und geht anschliessend den naechsten Tunnelabschnitt an.
- inworld_result: Ronja sichert den aktuellen Abschnitt fertig, markiert tragfaehige und nachzuarbeitende Stellen sauber nach und meldet D5 anschliessend knapp den Stand durch. Die Meldung nennt den Abschnitt als gelesen, gesichert und fuer Folgearbeit vorbereitet sowie den Bedarf an Schweißgeraet, DN60-Adaptern und Stuetzelementen. Aus Richtung D5 kommt wieder Werkstattlaerm zurueck, was Jonas und Pahl weiter an der Draisine bindet. Danach geht Ronja ohne theatrale Pause an den naechsten Meter der Strecke und bleibt im Arbeitsfluss.
- new_signals:
  - Probe: Ronja priorisiert saubere Sicherung und dokumentierte Nacharbeit vor spontaner Reaktion auf Tunnelunruhe.
  - Probe: Der aktuelle Abschnitt gilt nicht als repariert, aber als geprueft, markiert und fuer Folgearbeit vorbereitet.
  - Probe: D5 fuehrt fuer Nordlinie weiter eine Material- und Werkstattrolle, waehrend Ronja und Reflex praktisch im Tunnel arbeiten.
  - Review required: Der konkrete Materialfluss aus D5 ist noch nicht erfolgt und bleibt Runtime-Bedarf statt belegter Lieferung.
- follow_up: Naechsten Abschnitt pruefen, D5-Bedarfsliste getrennt nachziehen und den Runtime-Projektstatus fuer Nordlinie-01 knapp aktualisieren.

Turn 2
------

- input: Ronja wartet auf die Antwort aus D5, hoert sie an und bleibt danach im Tunnelarbeitsfluss.
- inworld_result: Aus D5 kommt eine knappe Rueckmeldung zurueck. Die Werkstatt meldet den Bedarf verstanden, bestaetigt aber keinen sofortigen Materiallauf. Schweißgeraet und DN60-Adapter bleiben weiter ein offener Engpass; Jonas und Pahl priorisieren die Anfrage in ihrer laufenden Werkstattarbeit, ohne Ronja eine schnelle Loesung vorzutäuschen. Ronja nimmt die Antwort ohne Diskussion an, verbucht sie innerlich als das, was sie ist, und geht dann direkt den naechsten Abschnitt an. Sie setzt neu Licht, liest Wand, Schotter und Trasse und arbeitet weiter im Modus Sicherung vor Tempo.
- new_signals:
  - Probe: D5 reagiert knapp, belastbar und ohne falsche Entwarnung auf Ronjas Bedarfsmeldung.
  - Probe: Der Materialmangel bleibt aktiv; es gibt keine sofortige Ausgabe oder Lieferung.
  - Probe: Ronja laesst sich durch die knappe Antwort nicht aus dem Arbeitsmodus ziehen und setzt die Tunnelsanierung ohne Szenensprung fort.
  - Review required: Welche Teile von D5 spaeter als behelfmaessige Stuetzelemente oder Werkstattloesung taugen, bleibt offen bis zu einem spaeteren Folgezug.
- follow_up: Naechsten Tunnelabschnitt auf konkrete Folgeblocker pruefen und D5 nur dann erneut ziehen, wenn der Arbeitszug ohne Material nicht mehr sauber vorbereitend weitergeht.

Turn 3
------

- input: Ronja markiert am neuen Problemabschnitt weiter und erkundigt sich zwischendurch bei C6 nach dem Stand ihrer Seite.
- inworld_result: Ronja bleibt zunaechst bei ihrer Arbeit, zieht weitere Warn- und Nacharbeitsmarken an Wand und Trasse und oeffnet nur so viel vom weichen Schienenbett, wie ohne Folgebruch vertretbar ist. Zwischen zwei Handgriffen zieht sie das Funkgeraet hoch und fragt C6 knapp nach deren Seite. Die Antwort bleibt ebenso knapp: Von C6 aus wird ebenfalls vorbereitet, markiert und vorsichtig freigelegt, aber ohne Durchbruch oder falsche Erfolgsmeldung. Die Gegenseite meldet keinen sauberen Materialueberschuss und keine schnelle Entspannung, nur belastbare kleine Arbeitsschritte und denselben Respekt vor dem Tunnel. Ronja nimmt das als bestaetigten Gesamtzustand, haengt das Geraet wieder tiefer und arbeitet weiter an ihrer eigenen Markierungslinie.
- new_signals:
  - Probe: Nordlinie 01 wird auf beiden Seiten weiter bearbeitet, aber beidseitig vorsichtig und ohne falsche Fortschrittsbehauptung.
  - Probe: C6 meldet Arbeitsfortsetzung statt Loesung; es gibt keinen beidseitigen Durchbruch und keinen freien Materialpuffer.
  - Probe: Ronja nutzt den Funk nur als kurzen Lageabgleich und bleibt danach konsequent im Tunnelarbeitsmodus.
  - Review required: Konkrete Personen- und Materialrollen auf C6-Seite bleiben im Runtime-Zug bewusst unscharf, bis eine spaetere Szene sie belastbar ausspielt.
- follow_up: Problemabschnitt weiter vorbereitend lesen und pruefen, ob sich aus dem bilateralen Stand ein klarer naechster Engpass oder ein koordinierter Arbeitskorridor ergibt.

Turn 4
------

- input: Die laufenden Markierungsarbeiten und die erste Materialerfassung sollen in der naechsten Szene zusammenfassbar vorgespult werden; zusaetzlich wird ausgewuerfelt, ob ein Ereignis diesen Vorspulzug unterbricht.
- inworld_result: Der Vorspulwurf wird nicht unterbrochen. Weder aus D5, noch aus C6, noch aus dem Tunnel selbst tritt ein eigenes Vorkommnis auf, das eine Zwischenszene erzwingt. Ronja, Reflex und die Gegenseite bleiben im selben vorsichtigen Arbeitsmodus: markieren, lesbar machen, erste Bedarfe sauber fassen, nichts beschoenigen. Damit kann die naechste Szene die Markierungsarbeiten und die erste Materialerfassung als gebuendelten Arbeitsblock fortschreiben.
- new_signals:
  - Probe: Kein Unterbrechungsereignis stoppt den Vorspulzug.
  - Probe: Die Nordlinie bleibt beidseitig im vorbereitenden Sanierungsmodus.
  - Probe: Die naechste Szene darf die Markierungsarbeiten und erste Materialerfassung als Zusammenfassung ziehen, ohne eine fehlende Zwischenkrise nachreichen zu muessen.
  - Review required: Konkrete Materialmengen und abschnittsscharfe Erfassung bleiben fuer den Folgezug offen.
- follow_up: Naechste Szene als gebuendelte Fortschrittssequenz fuer Markierungsarbeiten und erste Materialerfassung schreiben; dabei auf SSOT-/Lore-Fortschreibung achten.

Turn 5
------

- input: Die naechste Szene zieht die laufenden Markierungsarbeiten und eine erste Materialerfassung als gebuendelten Arbeitsblock weiter.
- inworld_result: Die naechsten Stunden laufen im selben kontrollierten Takt ab. Ronja arbeitet sich mit Reflex Meter fuer Meter weiter durch den D5-seitigen Abschnitt, zieht Warn- und Nacharbeitsmarken enger, legt lose Kanten frei und liest den Tunnel nicht auf Hoffnung, sondern auf Belastbarkeit. Aus der reinen Vorsicht wird dabei eine erste saubere Materialerfassung: Ohne Schweißgeraet bleibt jede tragende Reparatur weiter auf Vorarbeit begrenzt, ohne Adapter DN60 bleibt der uebergaengige Leitungs- und Trassenzug an einer kritischen Stelle offen, und Stuetzelemente werden nicht mehr nur allgemein, sondern fuer klar markierte Schwachzonen gebraucht. Ronja fasst das knapp, sachlich und ohne Theater zu einer belastbaren Bedarfsskizze zusammen, gibt sie Richtung D5 weiter und markiert den Abschnitt so nach, dass der naechste Arbeitszug nicht von vorn lesen muss. Als sie am Ende einen Schritt zuruecktritt, ist der Tunnel nicht geheilt und nicht freigegeben, aber er ist lesbarer, sauberer gefasst und materiell ehrlicher als zu Beginn des Blocks.
- new_signals:
  - Probe: Die Markierungsarbeiten werden als gebuendelter Folgeblock fortgeschrieben, ohne den vorbereitenden Charakter der Sanierung zu verlieren.
  - Probe: Eine erste Materialerfassung trennt jetzt harte Blocker von allgemeinem Folgebedarf.
  - Probe: Schweißgeraet und Adapter DN60 bleiben die klaren Sofortblocker fuer tragende und uebergaengige Reparaturarbeit.
  - Probe: Stuetzelemente sind nicht nur abstrakter Bedarf, sondern an markierte Schwachzonen im Abschnitt gebunden.
  - Review required: Konkrete Mengen, Werkstattzusagen und eine eventuelle Teilbereitstellung aus D5 bleiben fuer den naechsten Folgezug offen.
- follow_up: D5-Werkstattstand gegen die jetzt gegliederte Bedarfsskizze pruefen und den naechsten Arbeitszug entweder ueber Teilbereitstellung oder ueber den naechsten harten Materialstopp weiterfuehren.

Turn 6
------

- input: Ronja zieht die konkrete Werkstattantwort aus D5 auf ihre gegliederte Bedarfsskizze und richtet den naechsten Arbeitszug daran aus.
- inworld_result: Aus D5 kommt diesmal kein freier Hoffnungston, sondern eine engere, brauchbare Werkstattantwort. Jonas und Pahl bestaetigen, dass weder Schweißgeraet noch Adapter DN60 kurzfristig aus dem Nichts auftauchen; genau diese beiden Punkte bleiben die harten Stopper. Gleichzeitig ziehen sie aber einen schmalen Behelfssatz fuer den Tunnel zurecht: einfache Stuetzelemente und das noetige Kleinzeug, um markierte Schwachzonen nicht nur zu lesen, sondern im naechsten Schritt gezielt zu sichern. Der Zug bleibt klein, vorsichtig und ohne falsches Lieferversprechen. Es geht nicht um einen geloesten Materiallauf, sondern um eine enge Teilbereitstellung fuer genau die Stellen, die Ronja bereits sauber markiert hat. Ronja nimmt diese Antwort entsprechend nuechtern an. Sie trennt den Abschnitt jetzt noch klarer in zwei Arten von Arbeit: Bereiche, die mit dem angekuendigten Behelfssatz vorbereitet und abgestuetzt werden koennen, und Punkte, die ohne Schweißgeraet oder DN60 weiter echte Stopmarken bleiben. Damit bleibt der Tunnel unfertig, aber der naechste Arbeitszug bekommt eine scharfere Richtung.
- new_signals:
  - Probe: D5 beantwortet die Bedarfsskizze jetzt nicht nur mit Priorisierung, sondern mit einer schmalen, konkreten Werkstattvorbereitung fuer Stuetzelemente.
  - Probe: Schweißgeraet und Adapter DN60 bleiben weiterhin die harten Hauptblocker des Nordlinie-Zugs.
  - Probe: Der Folgeabschnitt ist jetzt in abgestuetzte Schwachzonen und echte Materialstopps getrennt lesbar.
  - Review required: Ob und wann der vorbereitete Behelfssatz tatsaechlich aus D5 in den Tunnelzug uebergeht, bleibt fuer den naechsten Folgezug offen.
- follow_up: Den naechsten Abschnitt ueber die angekuendigte Teilbereitstellung konkretisieren und pruefen, ob der Behelfssatz die ersten markierten Schwachzonen wirklich abstuetzen kann, ohne den Bedarf an Schweißgeraet und DN60 zu verdecken.

Turn 7
------

- input: Ronja laesst die angekuendigte kleine Teilbereitstellung aus D5 an den markierten Schwachzonen konkret werden und prueft sofort, was sich damit im Tunnel wirklich stabilisieren laesst.
- inworld_result: Der naechste Zug bleibt klein und ehrlich. Aus D5 kommt kein grosser Materiallauf, sondern nur das, was Jonas und Pahl in der Werkstatt kurzfristig tatsaechlich loseisen konnten: ein schmaler Satz einfacher Stuetzelemente, Klemmen und improvisierter Versteifungen fuer genau die markierten Schwachzonen, die Ronja im letzten Block sauber vorbereitet hat. Reflex uebernimmt den schwierigen Teil des Tragens und Einsetzens nicht als geloeste Zweitfigur, sondern eng an Ronja gebunden als ihr Exoskelett; die Kraft- und Stabilisierungshilfe bleibt damit koerpernah in Ronjas Arbeitszug eingebettet. Ronja arbeitet die Punkte nicht der Reihe nach, sondern nach echtem Risiko ab. Zwei Stellen lassen sich damit sichtbar ruhiger bekommen: lose Kanten stehen nicht mehr sofort auf Druck, ein kurzer Abschnitt wirkt beim Nachsetzen weniger fragil, und der Arbeitsraum wird fuer die naechsten Meter lesbarer. Gleichzeitig zeigt der Zug auch seine Grenze. Wo die Trasse selbst oder der Leitungsuebergang wirklich auf Verbindung und Halt angewiesen waeren, helfen weder die kleinen Stuetzelemente noch saubere Improvisation; dort bleiben Schweißgeraet und DN60 die unverschoebbaren Stopmarken. Ronja meldet genau das knapp zurueck: Der Behelfssatz war nuetzlich, aber nur fuer Sicherung und Vorbereitung, nicht fuer eigentliche Reparatur. Danach bleibt sie im Tunnel, nutzt den gewonnenen Spielraum sofort aus und zieht den Blick auf den naechsten Meter, der jetzt bearbeitbar ist, solange niemand aus dem kleinen Zugewinn einen falschen Fortschritt macht.
- new_signals:
  - Probe: D5 hat erstmals eine kleine, reale Teilbereitstellung fuer markierte Schwachzonen in den Nordlinie-Zug gebracht.
  - Probe: Reflex stuetzt den Tunnelzug beim Tragen und Setzen der improvisierten Sicherungen weiterhin koerpernah als Ronjas Exoskelett, nicht als frei geloeste Traegerinstanz.
  - Probe: Der Behelfssatz verbessert Sicherung und Lesbarkeit einzelner Stellen, ersetzt aber keine eigentliche Reparatur.
  - Probe: Schweißgeraet und Adapter DN60 bleiben trotz erster Teilbereitstellung die unverschoebbaren Hauptblocker.
  - Review required: Konkrete Mengen, Haltbarkeit des Behelfssatzes und die genaue Reichweite des gesicherten Folgeabschnitts bleiben fuer den naechsten Zug offen.
- follow_up: Den neu stabilisierten Abschnitt sauber nachziehen und pruefen, ob der gewonnene Spielraum fuer weitere Vorbereitung reicht oder der naechste echte Materialstopp sofort wieder greift.

  Turn 8
  ------

  - input: Ronja geht mit Reflex den durch Turn 7 gewonnenen Korridor erneut auf Basis des jetzt volleren Runtime-Slices ab. D5 bleibt im Hintergrund auf demselben knappen Werkstattstand; fuer den Zug gibt es keine neue Freigabe und nur noch den realen Tunnelrest aus `metallprofil-kurz`, `ausgleichsplatte` und `schraubensatz-mittel`.
  - inworld_result: Ronja bleibt im gleichen Arbeitsrhythmus und liest den kleinen Zugewinn bewusst nicht als Durchbruch, sondern als eng begrenztes Arbeitsfenster. Die bekannte D5-Kante bleibt dabei unveraendert im Hintergrund: Jonas und Pahl haben keine neue Lieferung nachgeschoben, sondern nur den schon belegten kleinen Satz in den Tunnel gebracht; mehr Rueckenwind als diese belastbar knappe Werkstattlage steht Ronja nicht zur Verfuegung. Zusammen mit Reflex geht sie deshalb den freier gewordenen Meter noch einmal sauberer ab, leuchtet Fugen, Lagerpunkte und die naechste Trassenkante neu aus und trennt den Fehlerkorridor jetzt nicht nur technisch, sondern auch arbeitspraktisch scharf. Drei Problemherde stehen danach nicht mehr als diffuse Tunnelstimmung, sondern als belastbarer Befund im Abschnitt: Erstens die `Schottertasche Nordkante`, bei der unter einer seitlichen Kante Material ausgespuelt ist und der Unterbau lokal nachgibt. Zweitens das `Haltepunktpaar Leitungszug`, zwei noch sitzende, aber nur vorlaeufig tragende Haltepunkte am seitlichen Leitungsstrang. Drittens der `Uebergang Engbogen`, ein kurz vor dem engeren Bogen verzogener Uebergang, der ohne Schweißgeraet und DN60 nicht in belastbare Reparatur kippt. Weil aus D5 seit Turn 7 nichts Neues angekommen ist, arbeiten Ronja und Reflex exakt mit dem Rest, der tatsaechlich noch im Tunnel liegt. Reflex haelt Ronjas Koerper weiter exoskelettnah im Druck, waehrend Ronja das letzte kurze Metallprofil zusammen mit der letzten Ausgleichsplatte und dem letzten mittleren Schraubensatz an die vibrierende Nordkante setzt, damit die `Schottertasche Nordkante` fuer den naechsten Leseschritt nicht sofort wieder aufreisst. Mehr wird daraus bewusst nicht gemacht: keine neue Freigabe, kein nacherfundenes Material, keine Reparaturbehauptung ueber den Rest hinaus. Der Gewinn von Turn 8 liegt damit weiterhin nicht in Loesung, sondern im saubereren Fehlerbild und in der engeren Trennung zwischen dem, was der Tunnelrest noch sichern konnte, und dem, was nur ein realer neuer D5-Zug mit Schweißgeraet und DN60 weiterbewegen kann.
  - problem_clusters:
    - name: `Schottertasche Nordkante`
      status: hinreichend untersucht
      befund: Seitliche Kante mit ausgespueltem Unterbau und vibrierender Auflage; provisorisch beruhigt, aber nicht tragend saniert.
      reparaturfolge: Freiraeumen, Unterfuetterung stabilisieren, Auflage neu verspannen und die lokale Kante mit Baukastenmaterial erneut setzen.
      kernmaterialien: `metallprofil-kurz`, `ausgleichsplatte`, `schraubensatz-mittel`, zusaetzliche Unterfuetterung / Schotterarbeit
      kostenklasse: `Band M`
    - name: `Haltepunktpaar Leitungszug`
      status: teilweise untersucht
      befund: Zwei Haltepunkte sitzen noch, tragen aber nur unter Vorbehalt; Langzeitlast und Anschlussqualitaet sind im Zug noch nicht voll geprueft.
      reparaturfolge: Anschlussstellen freilegen, Haltepunkte einzeln pruefen und erst danach Ersatz oder Neuverspannung festziehen.
      kernmaterialien: offen nach Freilegung; wahrscheinlich `klemme` und Verbindungsteile aus dem Baukasten
      kostenklasse: offen bis zur vollstaendigen Untersuchung
    - name: `Uebergang Engbogen`
      status: hinreichend untersucht
      befund: Verzogener Uebergang vor dem engeren Bogen; ohne thermische Arbeit und DN60-Anschluss keine belastbare Rueckfuehrung in den Trassen- und Leitungsverbund.
      reparaturfolge: Uebergang freilegen, Geometrie neu ausrichten, mit Schweißgeraet nacharbeiten, DN60-Adapter sauber einpassen und den Bereich anschliessend mechanisch sichern.
      kernmaterialien: `Schweißgeraet`, `Adapter DN60`, zusaetzliche Verbindungssicherung
      kostenklasse: `Band H`
  - new_signals:
    - Probe: Turn 8 verbraucht nur den realen Tunnelrest des kleinen Turn-7-Satzes; eine weitere D5-Lieferung findet in diesem Zug nicht statt.
    - Probe: Die D5-Werkstattkante bleibt im Hintergrund belastbar knapp und unveraendert; Jonas und Pahl oeffnen in Turn 8 keine neue Freigabe ueber den bereits belegten Turn-7-Satz hinaus.
    - Probe: Der naechste Fehlerkorridor ist jetzt nicht nur enger lesbar, sondern direkt in `Schottertasche Nordkante`, `Haltepunktpaar Leitungszug` und `Uebergang Engbogen` getrennt.
    - Probe: Reflex bleibt auch im Folgezug koerpernah als Ronjas Exoskelett eingebunden; es gibt keine abgeloeste Material- oder Traegerfigur.
    - Probe: Fuer `Schottertasche Nordkante` ist die Reparaturfolge jetzt mit `Band M` belastbar eingegrenzt; fuer den `Uebergang Engbogen` liegt mit `Band H` ein klar technischer Hauptblocker vor.
    - Review required: Der naechste materielle Fortschritt muss als reale Lieferung aus D5 belegt werden; aus dem ausgeschopften Tunnelrest und dem unveraenderten D5-Hintergrund laesst sich kein weiterer Behelfssatz mehr ableiten.
  - follow_up: Die benannten Problemherde im Runtime-State mit Reparaturklasse nachziehen und den naechsten Materialzug erst dann als Fortschritt buchen, wenn D5 die fuer `Uebergang Engbogen` benoetigten Kernmaterialien explizit und real in den Tunnel bringt.

Turn 9
------

- input: Turn 9 bleibt ein offener Weltzug des aktuellen Nordlinie-Hauptpfads, wird aber per Admin-Auswertung auf den festgeschriebenen Arbeitsstand gezogen: `D5` bleibt korrekt, `C6` arbeitet seinerseits ebenfalls am Tunnel, `Kora` bleibt in der Stationsverwaltung, die nicht im Tunnel eingesetzten Gefluechteten tragen den Innenbetrieb von `C6`, `Mara Quell` bleibt in `C6` beim Aufbau des H-47-Aussenpostens und `G7` erhaelt mangels Meldung keinen frischen Novapolis-Stand.
- inworld_result: Im Tunnel selbst bleibt Ronja bei derselben klaren Nuechternheit. Sie und Reflex machen aus dem enger gelesenen Korridor keinen neuen Vorstoss, sondern ziehen fuer den naechsten echten Arbeitsschritt eine saubere Prioritaetenlinie: `Schottertasche Nordkante` bleibt die lokal bearbeitbare Schwachstelle, `Haltepunktpaar Leitungszug` der offene Pruefpunkt und `Uebergang Engbogen` der harte technische Blocker, der ohne Schweißgeraet und `DN60` nicht kippt. Von der Gegenseite arbeitet `C6` in derselben Vorsicht weiter in den Tunnel hinein; der Vorspulzug hat die beiden Trupps inzwischen so weit zusammengezogen, dass sie sich im Restkorridor unter Licht, Staub und vorsichtiger Rufdistanz gegenseitig wahrnehmen koennen. Es ist noch kein sauberer Durchgang und kein entspannter Treffpunkt, aber die Arbeit laeuft jetzt nicht mehr nur auf Vermutung der anderen Seite, sondern auf vorsichtige gegenseitige Sicht und Bestaetigung. In `D5` verlaesst der Druck gleichzeitig den improvisierten Soforthilfemodus und geht in technische Verdichtung ueber. Jonas und Pahl setzen keinen neuen Satz frei, sondern ziehen die bislang nur praktisch gefuehlte Bedarfslage in eine belastbar knappe Werkstattanforderung zusammen: Wenn der naechste Zug ueber reine Sicherung hinausgehen soll, muss die Anforderung an Schweißgeraet, `DN60`, Anschlusssicherung und vorgelagerte Freiraeumung jetzt sauber und ohne Theater formulierbar werden. Lumen bleibt dabei im D5-Arbeitsfenster eng an Jonas gekoppelt; nichts an der Werkstattlage liest sich nach Entspannung oder nach stiller Zusatzreserve. In `C6` selbst bleibt `Kora` gerade deshalb aus dem Tunnel heraus. Sie fuehrt Station, Empfang, Schichtordnung und Sicherung weiter, waehrend `Echo` lokal an ihr bleibt und die innere Arbeitsdisziplin stuetzt. Die Gefluechteten, die nicht im Tunnel arbeiten, fuellen keine Leerstelle, sondern den noetigen Restbetrieb des Aussenpostens: Wasser und Rationen werden verteilt, Filter und Lagergut gesichtet, Schlaf- und Quarantaeneflaechen in Ordnung gehalten, einfache Werkzeuge sortiert, Wege freigehalten, Verletzte oder Erschoepfte mitgetragen und Wache, Kueche und Materiallauf unter Anleitung mitbesetzt. `C6` bleibt damit nicht passiv, sondern arbeitet auf zwei Ebenen zugleich: Tunnelkante draussen, Stationslast drinnen. `Mara Quell` bleibt waehrenddessen in `C6` und nicht in `G7`. Ihre Rolle in diesem Zug ist nicht die einer fernen Leitstelle, sondern die des vorsichtigen Aufbaus eines H-47-Aussenpostens unter enger Beobachtung derselben knappen Lage. Sie zieht deshalb auch kein grosses Handelsfenster auf, sondern bleibt vor Ort bei kleinster bestaetigter Handlungslogik. `G7` selbst bekommt in diesem Zug keinen neuen Novapolis-Stand, weil Mara nichts nach draussen gespiegelt hat. Der Weltzug bewegt damit die Lage spuerbar, aber nicht spektakulaer: Die Trupps im Tunnel sehen einander jetzt vorsichtig, `C6` bleibt innen arbeitsfaehig, `D5` verdichtet die technische Forderung, und weder `Mara` noch `G7` behaupten mehr Wissen oder Reichweite, als dieser Stand traegt.
- new_signals:
  - Probe: Turn 9 liest sich weiter als Weltzug, aber nur ueber die direkt belegten und nun admin-korrigierten Achsen `Tunnel`, `D5`, `C6` und `Mara in C6`.
  - Probe: Die Trupps aus `D5` und `C6` arbeiten im Vorspulstand inzwischen so weit aufeinander zu, dass sie sich vorsichtig gegenseitig wahrnehmen koennen; ein voller Durchgang folgt daraus noch nicht.
  - Probe: `Kora` bleibt in Turn 9 an der Stationsverwaltung von `C6` und nicht als eigene Tunnelakteurin.
  - Probe: Die nicht im Tunnel eingesetzten Gefluechteten tragen in `C6` jetzt sichtbar Wasser-, Lager-, Hygiene-, Kuechen-, Wache- und Entlastungsarbeit des laufenden Aussenpostens.
  - Probe: `Mara Quell` bleibt lore-konform in `C6` beim Aufbau des H-47-Aussenpostens; `G7` erhaelt in diesem Zug keinen neuen Wissensstand zu Novapolis.
  - Review required: Wie aus der verdichteten D5-Anforderung, dem vorsichtigen Tunnelkontakt und dem laufenden C6-Innenbetrieb der naechste konkrete Material- oder Durchgangsschritt wird, bleibt offen, bis derselbe Schritt runtime-seitig real belegt ist.
- follow_up: Den naechsten Zug erst auf dem jetzt geklaerten Stand fortsetzen: vorsichtiger bilateraler Tunnelkontakt, verdichtete D5-Anforderung, C6-Innenbetrieb unter Kora und Mara weiter in `C6`, waehrend `G7` ohne Meldung ignorant bleibt.

Turn 10
-------

- input: Auf dem jetzt freigegebenen Stand fuehrt Ronja den Zug nicht als Sprung oder Durchbruch weiter, sondern dokumentiert in aller Ruhe den Rest der Strecke bis zum C6-Tunneltrupp, spricht dort kurz die beidseitigen Beobachtungen ab und zieht mit ihnen eine gemeinsame Befundliste plus Bedarfskalkulation fuer den naechsten echten Arbeitsschritt. Entscheidend ist dabei die Trennung: Der `C6-Tunneltrupp` bringt seine eigene Tunnelhaelfte als Reparaturflaeche ein; die `C6-Station` unter `Kora` bleibt der getrennte Ruecklauf- und Innenbetriebsort dieser Meldung.
- inworld_result: Ronja bleibt auch in diesem Zug bei derselben sauberen Nuechternheit. Zusammen mit Reflex arbeitet sie den verbleibenden Abschnitt zwischen ihrer D5-Seite und dem C6-Tunneltrupp meterweise ab, notiert dabei nicht nur die schon benannten Problemherde, sondern auch, wo der Kontaktkorridor selbst tragfaehig genug fuer eine vorsichtige Begegnung ist und wo er es ausdruecklich nicht ist. Sie kommt nicht durch einen freigewordenen Tunnelspalt geschossen, sondern an einen schmalen, staubigen, behelfshaft sicheren Kontaktpunkt, an dem die C6-Seite bereits auf dieselbe Vorsicht heruntergebremst hat. Das kurze Gespraech bleibt entsprechend funktional: keine grosse Erleichterung, kein Pathos, kein Streit um Deutungshoheit. Ronja gleicht mit dem C6-Tunneltrupp zuerst ab, was ihre Seite traegt: Die `Schottertasche Nordkante` bleibt als lokal beruhigte, aber noch nicht belastbar geschlossene Schwachstelle bestaetigt. Das `Haltepunktpaar Leitungszug` wird als nur vorlaeufig tragend gefuehrt und fuer den naechsten Schritt ausdruecklich auf Freilegung und Einzelpruefung gesetzt. Der `Uebergang Engbogen` bleibt unstrittig der technische Hauptblocker, den sie ohne Schweißgeraet und `DN60` nicht sauber in den Verbund zurueckholen. Dann kommt sichtbar die Gegenseite dazu. Der C6-Tunneltrupp meldet fuer seine eigene Haelfte keinen leeren Spiegel von Ronjas Befunden, sondern drei eigene Arbeitsstellen: den `Schuttkeil Kontaktseite`, an dem lose Masse aus der C6-Richtung nachdrueckt und vor jedem staerkeren Lastwechsel erst geraeumt werden muss; die `Randauflage Suedlauf`, eine seitliche Auflageflaeche, die noch haelt, aber unter Wechselbelastung nachgesetzt und unterfuettert werden muss; und die `Leitungsaufnahme C6-Vorlauf`, eine deformierte Leitungsfuehrung kurz vor ihrer Seite, die ohne Verbindungsmaterial und saubere Freilegung keine belastbare Weiterarbeit traegt. Aus der kurzen Begegnung wird damit kein freier Austauschzug, sondern ein echter Arbeitsabgleich zweier beschaedigter Tunnelhaelften: Beide Seiten halten fest, dass der Restkorridor zwar fuer vorsichtige Personenbewegung an genau diesem Kontaktpunkt reicht, aber weder fuer entspannte Passage noch fuer echten Materialdurchsatz taugt. Darauf bauen sie gemeinsam die erste belastbare Befundliste mit Bedarfskalkulation fuer den Folgezug. Mindestbedarf bleibt ein echtes `Schweißgeraet` mit passendem `DN60`-Adapter; dazu kommen Anschlusssicherung, weiteres Verbindungsmaterial fuer die Leitungsseite, ein kleiner bis mittlerer Satz Baukastenmaterial fuer Nachsicherung und Unterfuetterung, gezielte Raeumkapazitaet fuer den `Schuttkeil Kontaktseite` sowie vorgelagerte Freiraeumung, damit weder D5- noch C6-Haelfte am Kontaktpunkt wieder sofort kollabiert oder beim ersten Lastwechsel den Engbogen ueberfordert. Ronja haelt den Ton dabei bewusst knapp und technisch. Der C6-Tunneltrupp nimmt die gemeinsame Liste mitsamt seinem eigenen Zusatzbefund in den Ruecklauf zur `C6-Station` mit und spiegelt, dass dieselbe Bedarfskalkulation nach innen zu `Kora` geht. Der Zug gewinnt damit keinen grossen Durchbruch, aber etwas Wertvolleres fuer den naechsten Schritt: eine beidseitig bestaetigte Arbeitsgrundlage statt zwei parallel gefuehrter Vermutungen oder einer still als sauber gelesenen C6-Haelfte.
- new_signals:
  - Probe: Ronja erreicht den C6-Tunneltrupp jetzt an einem schmalen, behelfshaft sicheren Kontaktpunkt, ohne dass daraus bereits ein freier Tunnel- oder Materialdurchgang wird.
  - Probe: Der C6-Tunneltrupp bringt jetzt einen eigenen Reparaturbefund seiner Haelfte mit: `Schuttkeil Kontaktseite`, `Randauflage Suedlauf` und `Leitungsaufnahme C6-Vorlauf`.
  - Probe: Die drei bekannten D5-seitigen Problemherde `Schottertasche Nordkante`, `Haltepunktpaar Leitungszug` und `Uebergang Engbogen` stehen jetzt neben einem eigenen C6-seitigen Befundblock statt als alleinige Tunnelliste.
  - Probe: Aus dem ersten direkten Austausch entsteht eine gemeinsame Befundliste plus Bedarfskalkulation fuer den Folgezug, ausdruecklich mit D5- und C6-Anteil.
  - Probe: Mindestbedarf bleibt ein echtes `Schweißgeraet` mit `DN60`-Adapter; hinzu kommen Anschlusssicherung, Verbindungsmaterial, Baukastenmaterial fuer Nachsicherung und Unterfuetterung, Raeumkapazitaet fuer den `Schuttkeil Kontaktseite` sowie vorgelagerte Freiraeumung.
  - Probe: Der C6-Tunneltrupp traegt dieselbe Liste mit eigenem Zusatzbefund zurueck in die `C6-Station`, sodass `Kora` den naechsten Schritt nicht nur als Ronja-Ruecklauf, sondern als beidseitige Tunnelmeldung lesen kann.
  - Review required: Ob und wann die gemeinsame Bedarfskalkulation real in D5- und C6-seitige Material- oder Freigabebewegung kippt, bleibt offen, bis ein Folgezug denselben Uebergang explizit traegt.
- follow_up: Den naechsten Zug auf der gemeinsamen Befundliste aufbauen: D5- und C6-Haelfte getrennt, aber gekoppelt sichern, Bedarf nach innen und nach D5 sauber spiegeln und erst dann entscheiden, ob zuerst Raeumung auf der C6-Seite, Leitungsfreilegung oder der Engbogen mit Schweißgeraet und `DN60` angegangen wird.

Turn 11
-------

- input: Nach dem beidseitigen Tunnelabgleich geht Ronja mit Reflex wieder zurueck nach `D5`. Dort sucht sie Jonas und Pahl nicht in einem stillen Werkstattraum, sondern an der Draisine auf den Gleisen am Bahnsteig, fragt zuerst ihren Bau- und Materialstand ab und klaert erst danach mit ihnen den Reparaturbedarf aus dem Tunnel. Parallel verteilt `Kora` in `C6` weiter die Gefluechteten und liest anschliessend den Bericht des Tunneltrupps.
- inworld_result: Der Rueckweg nach `D5` bleibt fuer Ronja Arbeit und nicht Heimkehr. Sie und Reflex ziehen denselben vorsichtigen Korridor wieder zurueck, bis der Tunnelmund auf die Bahnsteigkante von `D5` aufmacht. Dort sitzt der Arbeitsdruck nicht in einem abgeschlossenen Werkstattkaemmerchen, sondern offen an den Gleisen: Jonas und Pahl stehen bei der Draisine, die genau dort auf den Schienen am Bahnsteig aufgebaut wird, weil sie nach Fertigstellung nicht erst aus irgendeinem Innenraum auf die Strecke gezaubert werden kann. Lumen bleibt bei Jonas in derselben Naharbeit. Ronja geht nicht sofort mit ihrer Tunnelliste dazwischen, sondern fragt zuerst den Stand ab. Jonas gibt die technische Seite knapp und ohne Theater: Der Rahmen steht weiter nur im Prototypzustand, die laufende Arbeit sitzt an Radaufnahme, Sicherung und den belastbaren Fixpunkten fuer die Schiene; Pahl haelt die Freigabe- und Sicherheitskante dazu eng. Auf Ronjas Frage nach dem Verbrauch kommt keine weiche Sammelantwort, sondern ein kleiner, ehrlicher Zwischenstand: Schmieroel, Lagerfett, ein Sicherungssatz und eine Dichtungsmanschette sind fuer den aktuellen Bauzustand bereits gebunden; weitere groessere Abgaenge sind gerade nicht belegt. Auf die wichtigere Frage, ob ihnen fuer den Draisine-Bau selbst noch etwas fehlt, bleibt die Antwort ebenfalls eng: Fuer den naechsten kleinen Bauschritt haben sie den Kernsatz vor Ort, aber die Reserve ist knapp und nichts daran liest sich nach "alles da" fuer jede Folgeidee. Erst danach legt Ronja den Tunnelbedarf auf den Tisch. Sie trennt sauber zwischen Kontaktpunkt, D5-Haelfte und C6-Haelfte, statt alles in einen diffusen Gesamtmangel zu rutschen. Jonas und Pahl lesen den Bericht nicht als Fremdtext, sondern als Arbeitsauftrag gegen ihren aktuellen Gleisbau. Schweißgeraet und `DN60` bleiben sofort die harten Blocker; dazu kommen Anschlusssicherung, Verbindungsmaterial, Material fuer Nachsicherung und Unterfuetterung sowie Raeumbedarf fuer die C6-Seite. Wichtig bleibt dabei der Schnitt: Die Draisine auf den Gleisen ist kein dekoratives Nebenprojekt, sondern derselbe Logistikkoerper, an dem Materiallauf und Tunnelbedarf spaeter haengen koennen, wenn der Korridor ueberhaupt weit genug freigezogen wird. In `C6` laeuft waehrenddessen kein stilles Warten. `Kora` verteilt weiter die Gefluechteten auf Wasser-, Lager-, Hygiene-, Kuechen-, Wache- und Entlastungsarbeit, zieht danach den Bericht des Tunneltrupps heran und liest ihn ausdruecklich als Meldung aus `C6-Tunneltrupp` und nicht als Fernnotiz von Ronja. Damit bleiben die Ebenen sauber getrennt: Ronja spricht in `D5` mit Jonas und Pahl ueber Bau- und Materialstand der Draisine sowie den Tunnelbedarf, waehrend `Kora` denselben Tunnelbericht in `C6` als Stations- und Verteilungsaufgabe verarbeitet.
- new_signals:
  - Probe: Ronja kehrt in Turn 11 mit Reflex nach `D5` zurueck und trifft Jonas und Pahl an der Draisine auf den Gleisen am Bahnsteig, nicht in einer stillen Werkstatt.
  - Probe: Vor der Reparaturfrage klaert Ronja zuerst Baufortschritt, Materialverbrauch und Fehlstellen der Draisine mit Jonas und Pahl.
  - Probe: Fuer den aktuellen Draisine-Bau sind Schmieroel, Lagerfett, ein Sicherungssatz und eine Dichtungsmanschette bereits gebunden; groessere weitere Abgaenge sind in diesem Zug nicht belegt.
  - Probe: Schweißgeraet und `DN60` bleiben fuer den Tunnelbedarf die harten Blocker; weitere Bedarfe sind Anschlusssicherung, Verbindungsmaterial, Nachsicherung, Unterfuetterung und C6-seitige Raeumung.
  - Probe: `Kora` verteilt in `C6` weiter Gefluechtete und liest den Bericht des `C6-Tunneltrupps` anschliessend als eigene Stationsaufgabe statt als mit Ronjas D5-Ebene vermischte Perspektive.
  - Review required: Ob D5 aus Draisine-Bau, bestehendem Materialstand und Tunnelbedarf bereits eine echte Priorisierungsentscheidung oder nur einen weiteren Engpassbericht zieht, bleibt offen, bis der Folgezug denselben Schnitt explizit fortfuehrt.
- follow_up: Den naechsten Zug erst auf dem jetzt geklaerten Dreischnitt fortsetzen: `Ronja/Reflex` in `D5`, `Jonas/Pahl/Lumen` an der Draisine auf den Bahnsteiggleisen und `Kora` in `C6` mit getrennter Stationsverarbeitung des Tunnelberichts.

Turn 12
-------

- input: Admin-Korrektur zum Replay: Die Formulierung, dass die Draisine heute nur Pruefstand und kein Versprechen bleibe, wird nicht als Szene uebernommen. Stattdessen ueberlegt Ronja eine Weile, funkt `C6` an und fragt, ob der `Schuttkeil Kontaktseite` so zerschlagen werden kann, dass brauchbare Bruchstuecke die `Schottertasche Nordkante` stabilisieren. Danach fragt sie Jonas und Pahl an der Draisine, wie diese eigentlich angetrieben wird.
- inworld_result: Ronja bleibt an der D5-Bahnsteigkante stehen, ohne die Draisine vorschnell einzuordnen. Sie laesst den Blick zwischen dem offenen Fahrgestell, Jonas' Arbeitsstelle und der Tunnelliste hin und her gehen. Dann greift sie wieder zum Funkgeraet. "C6, kommen. Koennt ihr den Schuttkeil so zerschlagen, dass man mit den Bruchstuecken die Schottertasche stabilisieren kann? Das wuerde zwei Fliegen mit einer Klappe schlagen." Die Frage geht nicht als Auftrag oder bestaetigte Loesung hinaus, sondern als technische Pruefung: C6 muss erst melden, ob der Schuttkeil Material hergibt, ob die Bruchstuecke tragfaehig genug sind und ob das Zerschlagen den Kontaktpunkt nicht gefaehrdet. Erst danach dreht Ronja sich wieder zu Jonas und Pahl an der Draisine. Sie zeigt nicht auf den Rahmen, sondern auf die offene technische Frage dahinter. "Wie wird die eigentlich angetrieben?" Damit verschiebt sie den D5-Teil des Zuges nicht in einen Testlauf, sondern auf die Grundlagenklaerung: Ohne belegten Antrieb, Bremslogik und Lastgrenze bleibt die Draisine ein offener Prototyp auf den Bahnsteiggleisen. Jonas und Pahl haben die Frage jetzt auf dem Tisch; eine Antwort ist in diesem Zug noch nicht belegt.
- new_signals:
  - Probe: Die verworfene Replay-Formulierung zur Draisine wird nicht als Runtime-Stand uebernommen.
  - Probe: Ronja oeffnet fuer C6 eine konkrete Prueffrage: Ob Bruchstuecke aus dem `Schuttkeil Kontaktseite` als Stabilisierungsmaterial fuer die `Schottertasche Nordkante` taugen, ist jetzt angefragt, aber noch nicht bestaetigt.
  - Probe: Aus dem Schuttkeil entsteht noch keine Materialbuchung; Tragfaehigkeit, Groesse, Gewinnung und Risiko am Kontaktpunkt bleiben offen bis zur C6-Antwort.
  - Probe: Die Draisine-Antriebsfrage ist jetzt explizit offen. Der Runtime-Stand belegt noch keinen konkreten Antrieb, keine Lastfreigabe und keinen Testlauf.
  - Probe: Ronja handelt weiter als technische Leitungsfigur: Sie sucht zuerst Wiederverwendung und Grundlagenklaerung, bevor sie Materiallauf oder Draisine-Einsatz behauptet.
  - keine neue Mind-Delta / keine neue Relationship-Delta: Die Szene erzeugt technische Prueffragen, aber noch keine belegte relationale Verschiebung zwischen Ronja, C6, Jonas oder Pahl.
  - Review required: C6-Antwort zur Eignung der Schuttbruchstuecke und Jonas/Pahl-Antwort zum Draisine-Antrieb muessen im Folgezug ausgespielt oder dokumentiert werden.
- follow_up: Naechsten Zug mit zwei Antworten beginnen: `C6` prueft Schuttbruch-Eignung fuer die `Schottertasche Nordkante`; Jonas und Pahl erklaeren den belegbaren Antrieb, die Brems-/Stopplogik und die aktuelle Lastgrenze der Draisine, ohne einen Testlauf vorwegzunehmen.

Turn 13
-------

- input: Nach deiner Freigabe bestaetigt Kora aus dem C6-Funkraum, dass sie die Schuttkeil-Frage verstanden hat und sich die Stelle selbst ansehen wird. Anschliessend geht Ronja zu Jonas und Pahl, streichelt Reflex kurz und spricht mit den beiden ruhig ueber konservative Antriebsvarianten fuer die Draisine wie Hebelbetrieb oder schlichtes Schieben auf der Schiene.
- inworld_result: Im D5-seitigen Funk- und Kontrollkern kommt die Rueckmeldung aus `C6` diesmal nicht nur als weitergereichte Tunnelnotiz an, sondern direkt ueber Kora selbst. Ihre Antwort bleibt knapp und sauber: Sie hat verstanden, dass es nicht um blindes Herausschlagen geht, sondern um die Frage, ob der `Schuttkeil Kontaktseite` an der richtigen Stelle kontrolliert genug Material fuer die `Schottertasche Nordkante` hergeben kann. Sie will das nicht aus zweiter Hand entscheiden. Kora bestaetigt deshalb, dass sie sich vom Funkraum aus selbst an die Kante bewegt, den Keil mit eigener Sicht liest und sich danach noch einmal direkt bei Ronja meldet. Mehr Zusage als diese pruefende Eigenbewegung macht sie nicht.
- inworld_result: Ronja nimmt genau diese knappe Bestaetigung an und bleibt bei ihrer Arbeitsruhe. Bevor sie sich wieder den Gleisen zuwendet, legt sie Reflex einen kurzen Moment die Hand an die Seite. Es ist kein grosses Zeichen und keine ausformulierte Geste, eher ein stiller Kontakt, der zwischen Arbeit und Warten passt und dessen Bedeutung im Zug offen bleibt. Danach geht sie zu Jonas und Pahl an die Draisine auf den Bahnsteiggleisen.
- inworld_result: Das Gespraech mit den beiden bleibt ebenso nuechtern. Ronja zieht keine freie Maschinenidee auf, sondern legt einen konservativen Gedanken vor: Wenn weder `D5` noch `C6` ueber einen Motor verfuegen, muesse die erste brauchbare Bewegung vielleicht mechanischer und kleiner gedacht werden, etwa ueber eine einfache Hebelvorrichtung wie bei einer Handdraisine oder notfalls schlicht ueber kontrolliertes Schieben auf der Schiene. Jonas nimmt das ernst, aber nicht euphorisch. Fuer ihn bleibt Schieben auf freier, gesicherter Strecke die ehrlichste Anfangslesart, solange nichts ueber Kraftuebertragung, Verschleiss und Ruecklauf hinaus versprochen wird. Eine Hebelvariante verwirft er nicht, aber sie oeffnet sofort neue Baustellen bei Lagerpunkten, Gestaenge und gleichmaessigem Lauf. Pahl setzt die Sicherheitskante eng dahinter: Weder Hebelbetrieb noch Schubvariante werden zur Freigabe, solange `Brems-/Stopplogik`, `Not-Aus` und ein klarer Rueckzugspfad nicht fuer denselben konservativen Rahmen mitgedacht sind. Damit bleibt der Antrieb offen, aber die Diskussion kippt von der leeren Motorfrage in eine belastbarere, nichtmotorische Arbeitsrichtung.
- new_signals:
  - Probe: Kora bestaetigt die Schuttkeil-Frage selbst aus dem C6-Funkraum und geht anschliessend eigenhaendig zur Pruefung an den Kontaktpunkt.
  - Probe: Die naechste belastbare C6-Antwort soll nicht nur Tunneltrupp-Ruecklauf, sondern Koras eigene Sichtpruefung des `Schuttkeil Kontaktseite` tragen.
  - Probe: Ronja fuehrt mit Jonas und Pahl jetzt erstmals eine konservative Debatte ueber nichtmotorische Draisine-Varianten statt weiter auf einen unbelegten Motor zu warten.
  - Probe: Schieben auf gesicherter Strecke und eine einfache Hebel-/Handdraisine bleiben pruefbare Arbeitsrichtungen, aber keine freigegebenen Bau- oder Einsatzentscheidungen.
  - Probe: Der kurze koerperliche Kontakt zwischen Ronja und Reflex ist jetzt belegt, wird aber bewusst noch nicht in eine feste Bedeutungsbehauptung oder neue Delta-Wertung gezogen.
  - keine neue Mind-Delta / keine neue Relationship-Delta: Turn 13 bestaetigt Arbeitsnaehe, Disziplin und Prueflogik, aber noch keine belastbare Verschiebung in Vertrauen, Bindung oder Konflikt.
- follow_up: Auf Koras Eigenpruefung des `Schuttkeil Kontaktseite` warten und die konservative Hand-/Schubdebatte fuer die Draisine erst danach gegen reale Tunnel- und Stopplogik enger ziehen.

Turn 14
-------

- input: Admin-/Spielervorgabe: Fuer Ronja hatte die kurze Geste an Reflex die Bedeutung, dass sie ihm zeigen wollte, dass sie weiss, dass er da ist, ihn nicht vergessen hat und froh ist, dass er da ist.
- inworld_result: Der kurze Kontakt aus dem vorigen Zug bleibt damit nicht laenger nur eine offene Bewegung zwischen Arbeit und Warten. Fuer Ronja ist er kein technisches Kommando, keine Freigabe fuer mehr Kontrolle und kein Versuch, die laufende Lage weichzuzeichnen. Er bedeutet schlicht, dass Reflex nicht nur als Werkzeug oder Schutzschicht mitlaeuft: Sie weiss, dass er da ist, sie hat ihn nicht vergessen, und sie ist froh ueber seine Naehe. Reflex nimmt das nicht als Anlass, groesser zu werden oder die Situation an sich zu ziehen. Die Reaktion bleibt klein und koerpernah: ein ruhigeres Anliegen, ein kurzer Abfall von unnoetigem Druck, dann wieder dieselbe wachsame Stabilitaet an Ronjas Seite. Am D5-Bahnsteig aendert sich dadurch technisch nichts. Koras Antwort vom `Schuttkeil Kontaktseite` steht weiter aus, und die Draisine bleibt bei den konservativen Hand-/Schubvarianten ohne Freigabe. Aber zwischen Ronja und Reflex ist der kurze Kontakt jetzt nicht mehr leer: Er ist als bestaetigendes Naehesignal belegt, ohne daraus eine neue Symbiose-Stufe, eine Kontrollfreigabe oder einen geloesten Konflikt zu machen.
- new_signals:
  - Probe: Turn 14 klaert die Bedeutung der Geste aus Turn 13 ueber explizite Spielervorgabe: Ronja zeigt Reflex Wahrnehmung, Erinnerung und Freude ueber seine Anwesenheit.
  - Probe: Reflex nimmt das Signal als Beruhigung und Bestaetigung auf, bleibt aber klein, koerpernah und ohne Kontroll- oder Detachment-Claim.
  - Probe: Der Zug erzeugt ein Relationship-Delta zwischen Ronja und Reflex, aber keinen technischen Fortschritt an Draisine, Schuttkeil, Materiallage oder Tunnel-Freigabe.
  - Mind-Delta: Ronjas innerer Sinn der Geste ist jetzt belastbar dokumentiert; Reflex' Reaktion bleibt als ruhige Stabilisierung und bestaetigte Naehe lesbar.
  - Relationship-Delta: `Ronja -> Reflex` und `Reflex -> Ronja` werden als reaffirmed/contact-signal gefuehrt; kein harter Score, keine neue Symbiose-Stufe.
  - keine technische Delta: Kora, Jonas, Pahl, Lumen, Draisine und Nordlinie bleiben auf dem Vorbereitungsstand von Turn 13.
- follow_up: Naechster Zug soll zuerst die konservative Draisine-Frage mit Jonas/Pahl/Lumen enger ziehen, ohne Koras noch offene Eigenpruefung des `Schuttkeil Kontaktseite` still zu ersetzen.

Turn 15
-------

- input: Freigegebener Reflex-Wahrnehmungszug: Nach der geklaerten Naehesignal-Geste soll zuerst Reflex' Wahrnehmung zwischen Ronja-Bindung, D5-/C6-Druck, Tunnelgefahr und belegter CRISIS-Kokon-Kante ausgespielt werden. Kein neuer technischer Fortschritt, keine neue Ronja-Entscheidung und keine freie Symbiose- oder Kontrollfreigabe.
- inworld_result: Reflex bleibt an Ronja, aber das ruhige Signal aus Turn 14 macht die Welt nicht weicher. Es sortiert nur den ersten Wert in seinem inneren Raster: Ronja ist da, Ronja weiss von ihm, Ronja will ihn in ihrer Naehe. Danach kommen sofort die anderen Werte, hart und kantig. Der Bahnsteig von `D5` vibriert unter Werkstattlaerm, die offene Draisine riecht nach Schmieroel, Lagerfett und unfertigem Metall, aus dem Tunnel haengt noch Staub in den Luftschichten, und hinter der Funklinie nach `C6` steht der `Schuttkeil Kontaktseite` als ungelesene Masse. Fuer Reflex ist das kein Hintergrund. Es ist Druck, Richtung, Risiko. Er liest kleinste Lastwechsel in Ronjas Haltung, die Entfernung zum Tunnelmund, die offenen Raender des Fahrgestells, Jonas' und Pahls Bewegungen an den Gleisen, das noch unbeantwortete C6-Fenster. Die bestaetigte Naehe senkt seinen Grunddruck, aber nicht seine Schutzbereitschaft. Unter der ruhigen, anliegenden Schicht bleibt ein zweiter Zustand wach: Wenn der Tunnel nachgibt, wenn eine Last kippt, wenn Ronja ploetzlich zu hart aus dem sicheren Arbeitsfenster faellt, waere Reflex nicht erst hoeflich, sondern sofort Huelle, Gegendruck, Dunkelung, Koerper um Koerper. In diesem Moment passiert das nicht. Kein Kokon bildet sich, keine Bewegung wird blockiert, keine Kontrolle wird genommen. Aber der Impuls ist da, sauber unter der Oberflaeche gehalten. Reflex bleibt klein, weil Ronjas Zeichen ihn haelt; er bleibt kantig, weil Novapolis nichts daran verspricht, sicher zu sein.
- new_signals:
  - Probe: Turn 15 klaert Reflex' Wahrnehmung nicht als geglaettete Beruhigung, sondern als zweischichtige Regulation: Naehe stabilisiert, Weltendruck haelt den Schutzmodus scharf.
  - Probe: Der belegte `CRISIS`-Kokon/Vollschutz bleibt als Notfallimpuls lesbar, wird in diesem Zug aber nicht ausgeloest.
  - Probe: Reflex registriert D5-Bahnsteig, Draisine, Tunnelstaub, C6-Funkfenster und Schuttkeil-Frage als Risiko-/Druckfeld, ohne daraus technische Fakten, Materialbewegung oder neue Freigabe abzuleiten.
  - keine PC-Delta: Ronja erhaelt keine neue Handlung, Entscheidung, innere Reaktion oder Zustimmung; Turn 15 spielt nur Reflex' Wahrnehmung auf Basis der bereits belegten Lage.
  - keine technische Delta: Kora, Jonas, Pahl, Lumen, Draisine, Schuttkeil und Nordlinie bleiben auf dem Vorbereitungsstand von Turn 14.
- follow_up: Naechster Zug kann weiter bei der konservativen Draisine-Frage und Koras offener Schuttkeil-Eigenpruefung ansetzen; Reflex' Wahrnehmung bleibt dabei als kantiger Schutzfilter aktiv, ohne technische Antworten zu ersetzen.

Vorbereitungsanker fuer den naechsten Zug
----------------------------------------

- status: vorbereitet nach Turn 15; Ronja/Reflex-Geste geklaert und Reflex' Wahrnehmung als kantiger Schutzfilter ausgespielt, technische Antworten weiter nicht ausgespielt
- startreihenfolge:
  - Jonas und Pahl ziehen als naechste technische Achse die konservativen Hand-/Schubvarianten der Draisine enger gegen `Brems-/Stopplogik`, `Not-Aus`, Rueckzugspfad und Lastfenster.
  - Kora bleibt mit ihrer eigenen Sichtpruefung aus `C6` als Folgeantwort offen: ob der `Schuttkeil Kontaktseite` kontrolliert genug Material hergibt, welche Bruchstueckgroesse fuer die `Schottertasche Nordkante` taugt und welches Risiko dabei fuer den Kontaktpunkt bleibt, ist noch nicht entschieden.
  - Erst danach wird entschieden, ob `Schottertasche Nordkante`, `Schuttkeil Kontaktseite` und der weitere Logistikpfad praktisch zusammengefuehrt werden koennen.
- harte grenzen:
  - Die Bedeutung der Ronja/Reflex-Geste ist jetzt als Naehesignal geklaert, aber nicht als technische Freigabe, Kontrollfreigabe oder Symbiose-Stufe-II-Claim zu lesen.
  - kein Schuttbruch wird als Materialbuchung, Einsatz oder Transfer gefuehrt, solange Kora die Eignung, Gewinnung und das Kontaktpunktrisiko nicht ausdruecklich selbst bestaetigt hat.
  - weder Hebelbetrieb noch Schubvariante werden als fertiger Antrieb, Lastfreigabe oder Logistikclaim ausgespielt, solange `Brems-/Stopplogik`, `Not-Aus`, Rueckzugspfad und Lastfenster nicht belastbar mitgezogen sind.
  - keine neue D5- oder C6-Freigabe wird still aus der Vorbereitung abgeleitet; der naechste Zug darf Antworten und Priorisierung liefern, aber keine freie Erfolgsmeldung.
- geladene achsen:
  - `Ronja/Reflex`
  - `Jonas/Pahl/Lumen`
  - `C6-Tunneltrupp` und `Kora` als getrennter Stationsruecklauf
  - `D5`, `C6`, `Nordlinie 01` und `Draisine-Transportmodul`
- zielbild:
  - Der naechste Zug ist vorbereitet, wenn Koras Eigenpruefung und die konservative Draisine-Debatte denselben engen Arbeitsrahmen tragen, ohne daraus schon Material- oder Fahransprueche zu machen.

Admin Handover
-------------

- agent_switch: vollzogen
- target_mode: SSOT, Story, Weltgeschichte, Lore
- handover_basis: Turn 1-15 bilden jetzt den Runtime-Arbeitsstand; die Folgeszene schliesst an die geklaerte Ronja/Reflex-Geste, Reflex' kantige Wahrnehmung des D5-/C6-Druckfelds, Koras angekuendigte Eigenpruefung des `Schuttkeil Kontaktseite`, die konservative Hand-/Schubdebatte zur Draisine, den enger gelesenen Fehlerkorridor, den schmalen Kontaktpunkt mit dem C6-Trupp, die gemeinsame Befundliste plus Bedarfskalkulation sowie den weiter offenen Materialblocker bei `Schweißgeraet` und `DN60` an.
- interruption_roll: `1W6 = 4`, kein Unterbrechungsereignis

Kurzauswertung
--------------

- Ton: konzentriert, sachlich und klar auf Ronjas Arbeitsmodus gezogen.
- Stimmung: kein Alarm, aber spuerbarer Druck durch Materialmangel und Tunnelzustand.
- Kanonlage: vorsichtig bis belegt; Tunnelarbeit und Draisine sind SSOT, der konkrete Zug ist Runtime-Arbeitsstand.
- Reuse-Wert: hoch fuer Fortsetzung von Nordlinie-01 mit sauberem Status- und Bedarfsfokus.

Neue belastbare Signale
-----------------------

- Session-Arbeitslesart: Ronja meldet nicht erst bei Krise, sondern nach sauber abgeschlossenem Teilabschnitt.
- Session-Arbeitslesart: Materialbedarf wird frueh und knapp an D5 rueckgekoppelt.
- Session-Arbeitslesart: Der naechste Arbeitszug beginnt unmittelbar nach der Meldung, ohne Szenensprung.
- Session-Arbeitslesart: D5 antwortet ohne falsche Zusage; der Engpass bleibt offen und steuerbar statt wegfiktionalisiert.
- Session-Arbeitslesart: C6 fuehrt denselben vorsichtigen Sanierungsmodus; der Tunnel wird beidseitig bearbeitet, aber nicht beschoenigt.
- Session-Arbeitslesart: Ein Vorspulzug ueber die laufenden Markierungsarbeiten wird durch kein Ereignis unterbrochen.
- Session-Arbeitslesart: Die erste Materialerfassung liegt jetzt als gegliederte Bedarfsskizze fuer einen konkreten Folgeabschnitt vor.
- Session-Arbeitslesart: D5 zieht auf die Bedarfsskizze eine kleine, konkrete Werkstattvorbereitung fuer Stuetzelemente nach, ohne die Hauptblocker kleinzureden.
- Session-Arbeitslesart: Der erste kleine Behelfssatz aus D5 schafft reale Sicherung an markierten Schwachzonen, aber keinen Reparaturdurchbruch.
- Session-Arbeitslesart: Reflex bleibt auch bei praktischer Trage- und Setzhilfe koerpernah an Ronja gebunden; der Turn liest die Assistenz explizit als Exoskelett und nicht als abgeloeste Begleitfigur.
- Session-Arbeitslesart: Turn 8 arbeitet ohne neue Lieferung nur mit dem realen Tunnelrest weiter; weiterer Materialfortschritt muss ab jetzt wieder als explizite D5-Lieferung belegt werden.
- Session-Arbeitslesart: Der Fehlerkorridor ist jetzt direkt als `Schottertasche Nordkante`, `Haltepunktpaar Leitungszug` und `Uebergang Engbogen` benannt.
- Session-Arbeitslesart: Fuer die hinreichend untersuchten Problemherde liegen jetzt Reparaturfolge und Aufwandsklasse vor: `Schottertasche Nordkante` auf `Band M`, `Uebergang Engbogen` auf `Band H`.
- Session-Arbeitslesart: Turn 9 spielt denselben Hauptpfad jetzt offen als Weltzug ueber `D5`, `C6` und den laufenden Tunnelkontakt, ohne den Materialblocker frei zu ueberspringen.
- Session-Arbeitslesart: Die Tunneltrupps aus `D5` und `C6` haben sich im Vorspulstand jetzt vorsichtig gegenseitig wahrgenommen; das ersetzt noch keinen freien Durchgang.
- Session-Arbeitslesart: `Kora` bleibt in `C6` auf Stationsverwaltung und Innenbetrieb, waehrend die nicht eingesetzten Gefluechteten den laufenden Vorposten praktisch mittragen.
- Session-Arbeitslesart: `Mara Quell` bleibt in `C6`; `G7` bekommt ohne Meldung keinen neuen Novapolis-Stand.
- Session-Arbeitslesart: Turn 10 fuehrt Ronja jetzt bis an den C6-Tunneltrupp und macht aus der bisherigen Sicht-/Rufdistanz einen vorsichtigen direkten Arbeitskontakt.
- Session-Arbeitslesart: Der C6-Tunneltrupp bringt fuer seine Haelfte jetzt eigene melderelevante Befunde mit und steht nicht nur als bestaetigende Gegenstimme von Ronjas Arbeit im Raum.
- Session-Arbeitslesart: Die D5-seitigen Problemherde stehen jetzt neben dem C6-seitigen Befundblock `Schuttkeil Kontaktseite`, `Randauflage Suedlauf` und `Leitungsaufnahme C6-Vorlauf`.
- Session-Arbeitslesart: Fuer den Folgezug liegt jetzt eine gemeinsame Bedarfskalkulation mit `Schweißgeraet`, `DN60`, Anschlusssicherung, Verbindungsmaterial, Baukasten-Nachsicherung, C6-seitiger Raeumung und Freiraeumung vor.
- Session-Arbeitslesart: Turn 11 fuehrt Ronja wieder zurueck nach `D5` und setzt Jonas/Pahl/Lumen sichtbar an die Draisine auf den Bahnsteiggleisen statt in einen stillen Werkstattinnenraum.
- Session-Arbeitslesart: Ronja klaert zuerst Baufortschritt, Materialverbrauch und Fehlstellen der Draisine und erst danach den Tunnelbedarf.
- Session-Arbeitslesart: `Kora` verarbeitet denselben Tunnelbericht in `C6` als eigene Stations- und Verteilungsaufgabe; die Ebenen `Ronja`, `D5` und `C6` bleiben dabei getrennt.
- Session-Arbeitslesart: Turn 12 setzt die C6-Schuttkeil-Idee nur als Prueffrage, nicht als bestaetigte Materialgewinnung oder Reparaturloesung.
- Session-Arbeitslesart: Die Draisine-Antriebsfrage ist jetzt explizit offen und muss von Jonas/Pahl beantwortet werden, bevor Lastgrenze, Testlauf oder Materiallogistik daraus abgeleitet werden.
- Session-Arbeitslesart: Turn 13 zieht Kora selbst in den C6-Funkraum und von dort an die Eigenpruefung des `Schuttkeil Kontaktseite`; die naechste belastbare Antwort soll damit aus ihrer eigenen Sicht kommen.
- Session-Arbeitslesart: Turn 13 zieht die Draisine-Debatte von der freien Motorfrage auf konservative Hand-/Schubvarianten, ohne daraus schon eine Bau- oder Freigabeentscheidung zu machen.
- Session-Arbeitslesart: Turn 14 klaert die Ronja/Reflex-Geste als bestaetigendes Naehesignal ueber Wahrnehmung, Erinnerung und Freude an Reflex' Anwesenheit.
- Session-Arbeitslesart: Turn 14 erzeugt ein enges Relationship-Delta zwischen Ronja und Reflex, aber keinen technischen Fortschritt und keine neue Freigabe.
- Session-Arbeitslesart: Der kurze Kontakt zwischen Ronja und Reflex ist jetzt belegt, bleibt aber bewusst ohne vorschnelle Deutung oder neue Bindungsbehauptung.
- Session-Arbeitslesart: Turn 15 spielt Reflex' Wahrnehmung als kantigen Schutzfilter aus: Naehe stabilisiert, aber Weltendruck, Tunnelgefahr und `CRISIS`-Kokon-Impuls bleiben aktiv lesbar.

Open Threads
------------

- naechsten Tunnelabschnitt zwischen `Schottertasche Nordkante`, `Haltepunktpaar Leitungszug` und `Uebergang Engbogen` priorisieren
- D5-Priorisierung gegen die jetzt gegliederte Bedarfsskizze erneut pruefen
- pruefen, ob D5 aus Draisine-Bau und Tunnelbedarf zuerst Material, Freiraeumung oder Logistikpfad priorisiert
- C6-Seite spaeter konkreter ziehen, falls aus dem bilateralen Sanierungsstand eine koordinierte Aktion entsteht
- Reichweite und Haltbarkeit der ersten Teilbereitstellung gegen den naechsten Abschnitt pruefen
- konkrete Folgelieferung aus D5 nur dann fortschreiben, wenn sie im Runtime-Zug explizit real ankommt
- pruefen, ob der enger gelesene Uebergang vor dem Bogen erst mit Schweißgeraet und DN60 oder schon mit vorgelagerter Freiraeumung sinnvoll weitergezogen werden kann
- pruefen, wie aus dem jetzt vorsichtigen Sichtkontakt der Trupps ein belastbarer Arbeits- oder Durchgangsschritt wird
- pruefen, wie der schmale Kontaktpunkt gegen Erschuetterung, Lastwechsel und Materialbewegung gesichert werden kann
- C6-seitigen `Schuttkeil Kontaktseite`, die `Randauflage Suedlauf` und die `Leitungsaufnahme C6-Vorlauf` im Folgezug getrennt priorisieren statt als still saubere Gegenhaelfte mitzuschleppen
- C6-Innenbetrieb unter Kora, Echo und den nicht eingesetzten Gefluechteten weiter lesbar halten, solange kein neuer Materialimpuls ankommt
- gemeinsame Bedarfskalkulation sauber nach D5 und in den C6-Innenlauf spiegeln, ohne daraus schon eine reale Freigabe zu behaupten
- Mara nur dann ueber `C6` hinaus in neue Handels- oder Meldelogik ziehen, wenn sie dieselbe Lage wirklich nach aussen spiegelt
- Folgeszene im SSOT-/Lore-Agenten auf genau diesem Handover-Stand fortsetzen
- pruefen, ob aus der laufenden Runtime-Session spaeter ein belastbarer Nordlinie-Status fuer RP-SSOT promotable wird
- C6-Antwort einholen, ob der `Schuttkeil Kontaktseite` kontrolliert zerschlagen werden kann und ob die Bruchstuecke fuer die `Schottertasche Nordkante` tragfaehig genug sind
- Jonas/Pahl-Antwort zum konkreten Draisine-Antrieb, zur Brems-/Stopplogik und zur belastbaren Lastgrenze einholen
- Reflex' kantigen Schutzfilter bei Folgeantworten mitfuehren, ohne ihn als technische Loesung, PC-Steuerung oder freie Kontrollfreigabe zu verwenden

Promotion Notes
---------------

- nothing promoted yet
