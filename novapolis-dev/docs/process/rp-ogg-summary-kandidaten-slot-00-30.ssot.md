---
stand: 2026-04-07 21:38
update: Die RP-SSOT markiert jetzt die ersten belastbaren OGG-Summary-Kandidaten fuer den Text-RPG-Pfad ueber slot 00-30.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260407_213201.md
---

RP OGG Summary Kandidaten: Slot 00-30
=====================================

Zweck
-----

Diese SSOT markiert die ersten belastbaren Build-Time-Kandidaten fuer vorproduzierte Stunden-Summaries aus demselben Text-RPG-Produktpfad. Sie fuehrt keine neuen Ereignisse ein, sondern leitet nur aus den bestehenden Slot-SSOTs ab, an welchen Uebergaben, Entscheidungsfenstern und Abschlusskanten ein spaeterer OGG-Export fuer `world` und `pc` den hoechsten Nutzen hat.

Quellenbasis
------------

- novapolis-dev/docs/process/rp-folgekorridor-slot-00-05.ssot.md
- novapolis-dev/docs/process/rp-folgekorridor-slot-06-10.ssot.md
- novapolis-dev/docs/process/rp-folgekorridor-slot-11-15.ssot.md
- novapolis-dev/docs/process/rp-folgekorridor-slot-16-20.ssot.md
- novapolis-dev/docs/process/rp-folgekorridor-slot-21-25.ssot.md
- novapolis-dev/docs/process/rp-folgekorridor-slot-26-30.ssot.md
- novapolis-dev/docs/specs/annotation-spec.md
- novapolis-dev/docs/specs/scheduler-spec.md
- novapolis-dev/docs/specs/tts-exporter-coqui.md

Ableitungsregeln
----------------

- Kein Vollabzug aller Stunden: Kandidaten werden nur dort markiert, wo der bestehende Produktpfad einen klaren Handover, eine Schwerpunktwahl, einen Kontaktwechsel oder einen Episodenanker fuehrt.
- `pc`-Kandidaten priorisieren Stunden, in denen fuer den Spieler ein zusammenhaengender Rueckblick, eine Lageeinschaetzung oder eine sichtbare Wahlkante entsteht.
- `world`-Kandidaten priorisieren Stunden, in denen derselbe Slot aus Welt- oder Operator-Sicht einen konsolidierten Zustandswechsel, Drucksprung oder Abschlussbericht traegt.
- Das Audio-Namensschema bleibt unveraendert: `epoch{dd}_slot{hh}_{channel}.ogg`.

Kandidatenmatrix
----------------

| Slot | world | pc | Anlass |
| --- | --- | --- | --- |
| `01` | ja | ja | `D5 Terminal, Port und System-Link` markiert den ersten klaren System- und Sichtbarkeitswechsel nach dem Einstieg. |
| `04` | ja | ja | `C6 Abschluss, Uebergabe und Echo-Moment` ist die erste belastbare Uebergabekante zwischen Parallelfaden und Rueckmeldung. |
| `07` | ja | nein | `Materiallauf D5 -> C6 vorbereiten und fahren` eignet sich vor allem als Welt- oder Operator-Zusammenfassung des aktiven Transfers. |
| `08` | ja | ja | `C6 Empfang, Bestandsaufnahme und Baustellenverteilung` liefert denselben Transfer als sichtbaren Abschluss- und Rueckmeldepunkt. |
| `09` | ja | ja | `G7-Kontaktfenster und Aussenkontakt` fuehrt den ersten externen Kontakt als zusammenfassbare Kontaktlage. |
| `10` | nein | ja | `Schwerpunktwahl nach innen oder aussen` ist primaer eine spielerseitige Entscheidungszusammenfassung. |
| `15` | ja | ja | `Langzeitprioritaet festziehen` markiert den ersten groesseren Strategie- und Schwerpunktabschluss. |
| `20` | ja | ja | `Ersten Kampagnenmodus fixieren` eignet sich als kompakter Kampagnenzwischenstand fuer beide Kanaele. |
| `25` | ja | ja | `Episodischen Uebergabeanker festziehen` ist der erste explizite Save-/Replay-/Handover-Anker. |
| `26` | nein | ja | `Wiedereinstieg nach dem Uebergabeanker ordnen` priorisiert eine pc-seitige Reorientierung statt eines neuen Weltberichts. |
| `28` | ja | ja | `G7 als Reservekontakt, Tauschfenster oder bewusstes Auslassen` verdichtet Aussenpfad und Kontaktkosten auf eine klare Stundenkante. |
| `29` | ja | ja | `E2/F1 als schmale Schleife oder Abschlusskante lesen` fuehrt denselben Randpfad mit hoher Verdichtungs- und Begrenzungsfunktion. |
| `30` | ja | ja | `Modulanker fuer die naechste Episode festschreiben` ist der zentrale Abschluss- und Wiederanlaufpunkt dieser Stufe. |

Nicht priorisierte Slots dieser Welle
-------------------------------------

- `00`, `02`, `03`, `05`, `06`, `11`, `12`, `13`, `14`, `16`, `17`, `18`, `19`, `21`, `22`, `23`, `24`, `27` bleiben in dieser ersten Welle bewusst ohne OGG-Prioritaet. Diese Stunden tragen weiter den Produktpfad, liefern aber noch keinen gleich starken Summary-Nutzen wie die markierten Handover-, Kontakt- oder Abschlusskanten.

Operative Lesart
----------------

- Die Matrix markiert nur Kandidaten; sie schreibt keine Texte vor.
- Fuer jede spaetere Exportwelle bleiben `world_log` und `pc_log` die Textquelle; es entsteht keine zweite Inhaltswahrheit in RP-Dateien.
- Die Reihenfolge fuer eine erste Offline-Welle lautet: `25`, `30`, `04`, `08`, `09`, `15`, `20`, danach die restlichen markierten Slots.

Offen ausserhalb dieser SSOT
----------------------------

- Die Live-Dialog-Synthese bleibt ein separater Runtime-Punkt und wird hier bewusst nicht mit dem Build-Time-Kandidatenpfad vermischt.
- Die konkrete Sprecherzuordnung und Voice-Map bleiben im TTS-Exporter- und Runtime-Vertrag des Agent-Moduls verankert.
