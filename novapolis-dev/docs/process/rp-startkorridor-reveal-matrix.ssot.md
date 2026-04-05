---
stand: 2026-04-05 19:43
update: Reveal-, Geheimhaltungs- und Wissensgrenzen fuer den ersten Novapolis-Startkorridor sind jetzt als eigene SSOT-Matrix festgezogen.
checks: snapshot-lock PASS (2026-04-05 08:10); markdownlint PASS; frontmatter PASS
---

RP Startkorridor Reveal Matrix SSOT
===================================

Zweck
-----

Diese SSOT fixiert fuer den ersten Novapolis-Startkorridor, welche Informationen direkt an den PC duerfen, was nur im Verbund sichtbar ist und was reine Spielleiter- oder Geruechtebene bleibt.

Quellenbasis
------------

- `novapolis-dev/docs/process/rp-startbogen-novapolis-d5.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-novapolis-c6.ssot.md`
- `novapolis-dev/docs/process/rp-text-rpg-startpaket-slot-00-05-2026-04-05.md`
- `novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md`
- `novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md`
- `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Missionslog-Novapolis.md`
- `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md`
- `novapolis-rp/database-rp/01-factions/novapolis/07-mind-clusters/ronja-kerschner-mind-cluster.md`
- `novapolis-rp/database-rp/01-factions/novapolis/07-mind-clusters/reflex-mind-cluster.md`
- `novapolis-rp/database-rp/01-factions/novapolis/07-mind-clusters/jonas-merek-mind-cluster.md`
- `novapolis-rp/database-rp/01-factions/novapolis/07-mind-clusters/pahl-brenner-mind-cluster.md`
- `novapolis-rp/database-rp/01-factions/novapolis/07-mind-clusters/kora-malenkov-mind-cluster.md`
- `novapolis-rp/database-rp/01-factions/novapolis/07-mind-clusters/echo-mind-cluster.md`

Regelkerne
----------

1. `world_only` bleibt Spielleiterwissen und wird nie ungefiltert in PC-Text oder Optionslisten gespiegelt.
2. `npc_only` deckt interne Motivlagen und lokale Einzelentscheide ab, die nicht automatisch im Gruppenkanal landen.
3. `allies_only` darf ueber Funk, Log, bestaetigte Uebergabe oder freigegebenen Reflex-Link verbreitet werden.
4. `pc_visible` ist unmittelbare Beobachtung, eigener Auftrag oder explizit freigegebener Verbundoutput.
5. `rumor` bleibt unsicher, bis eine bestaetigte Quelle denselben Inhalt auf `allies_only` oder `pc_visible` hebt.
6. `log/reflex` ist kein eigener Wahrheitsraum, sondern der definierte Transportpfad fuer kontrollierten Reveal.

Reveal-Klassen
--------------

| Klasse | Bedeutung | Zulaessige Ausspielung |
| --- | --- | --- |
| `pc_visible` | direkter Wahrnehmungs- oder Auftragskontext | PC-Text, Optionen, `pc_log` |
| `allies_only` | bestaetigtes Gruppenwissen | Funk, Arbeitslog, freigegebene Besprechung |
| `npc_only` | lokale Einzelabsicht oder situative Innenlage | NPC-Reaktion, nie ungefiltert im PC-Text |
| `world_only` | Weltwahrheit, verdeckte Lage, rohe Sphaerenwerte | nur SL, Debug, `world_log` |
| `rumor` | ungesichertes Rauschen, Geruecht, schwaches Signal | als Geruecht markieren, nie als Fakt |
| `log/reflex` | kontrollierter Transportkanal fuer Reveal | hebt Inhalte nur mit Quelle und Freigabe |

Matrix
------

| Objekt | Startlage | Klasse | Reveal-Pfad | Guardrail |
| --- | --- | --- | --- | --- |
| D5-Wartungsauftrag | unmittelbarer Startauftrag in D5 | `pc_visible` | direkte Beobachtung, Arbeitslog | keine freien Auftragdetails erfinden |
| Werkzeugtasche/Fundkontext D5 | lokaler Unsicherheitsanker | `pc_visible` | Beobachtung, spaeter Log | Inhalt bleibt offen bis belegter Befund |
| D5-System-Link Rohsignal | technisch belastbarer, aber unscharfer Signalanker | `log/reflex` | Reflex-Link, Terminal, spaeter PC-Freigabe | kein harter Lore-Reveal ohne Folgebeleg |
| Pahls Hausregeln/Freigaben | interne Betriebsordnung | `allies_only` | Ansage, Log, Freigabeprotokoll | nicht als Weltgesetz ausspielen |
| Nordlinie E/S/B-Stand | Projektstatus des Startkorridors | `allies_only` | Projektlog, Lagebriefing | keine freie Prozentfortschreibung |
| C6-Sicherung C6-N3 / Marker `7A` | lokaler C6-Arbeitsanker | `world_only` | nur via bestaetigten Kora-/Log-/Reflex-Pfad hebbar | keine Rohdaten direkt an den PC |
| C6-Abschluss-/Uebergabefenster | bestaetigter lokaler Abschlussmoment | `allies_only` | Log, Funk, freigegebene Meldung | keine freie Folgeninterpretation |
| C6-Funk/Scan-Suche | aktiver Auftrag mit offenem Output | `log/reflex` | Funkbericht, Scanprotokoll | Output erst nach belegtem Ergebnis |
| Geruechte ueber Lebenszeichen im C6-Nordbereich | schwaches Monitoring-Rauschen | `rumor` | Geruecht, vorsichtige Warnung | nie als bestaetigte Entitaet ausgeben |
| E3-Risikosignal | bestaetigter, aber begrenzter Gefahrmarker | `pc_visible` fuer Ronja, sonst `allies_only` | Missionslog, Reflex-Warnung | Quelle und Sichtbarkeit trennen |
| Mind-Cluster-Werte und relationale Innenlage | verdeckte Zustandsdaten | `world_only` / `npc_only` | nur indirekt ueber Verhalten, Ton, Optionen | keine Rohwerte im PC-Text |

Reveal-Pfade
------------

### Direkte Beobachtung

- D5-Auftragslage, Wartungsgang, offene Arbeitsmittel, lokale Teamreaktionen.

### Funk

- Bestaetigte Statusmeldungen D5 <-> C6.
- Keine unvalidierten Rohsignale ohne Marker als Fakt ausspielen.

### Log

- Missionslog, Projektstatus Nordlinie, Freigabe- und Uebergabeprotokolle.
- Logeintraege heben Sichtbarkeit, veraendern aber nicht rueckwirkend den Inhalt.

### Reflex-Link

- Erlaubter Schnellkanal fuer Gefahr, Schutz und technische Verdichtung.
- Nur explizit freigegebene oder bereits bestaetigte Inhalte gehen von `log/reflex` nach `pc_visible`.

### Geruecht

- Unsichere Stimmen, schwache Scans, unklare Tunnelhinweise.
- Muss im Wording unsicher bleiben.

Verbotene Kurzschluesse
-----------------------

- Kein Mind-Cluster-Rohwert wird direkt als Erklaerungstext fuer den PC ausgespielt.
- Kein `rumor` wird ohne Bestaetigung zu `pc_visible` promoted.
- Kein C6-N3-Detail wird allein wegen eines vorhandenen Logs automatisch PC-Wissen.
- Kein Funk- oder Reflexkanal ersetzt Quellen- und Sichtbarkeitsmarkierung.