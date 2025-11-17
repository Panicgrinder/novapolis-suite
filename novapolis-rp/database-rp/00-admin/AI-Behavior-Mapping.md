---
stand: 2025-11-16 06:52
update: frontmatter INIT
checks: pending
canvas: AI-Behavior-Mapping
last-updated: 2025-11-07T04:09:00+01:00
category: Admin
version: 1.0
---
canvas: AI-Behavior-Mapping
last-updated: 2025-11-07T04:09:00+01:00
category: Admin
version: 1.0
---

AI Behavior Matrix & Mapping (v2)
=================================

Ziel: Das vollständige Verhaltens-Matrix-Canvas (`ai_behavior_index_v2`) retten, normalisieren und für die Interaktion mit Novapolis-Akteuren nutzbar machen. Fokus liegt auf der Kombination aus globalen Clustern, Intensitäten, Modifikatoren und den daraus abgeleiteten Hooks für Charaktere/KI-Schnittstellen.

Zweck & Scope
-------------
- Globaler Referenzrahmen für alle Behavior-Codes (`O`, `T`, `L`, …) inkl. Intensität und Dynamik.
- Grundlage für Charakter-Signaturen (z. B. Ronja, Jonas, Reflex) und System-Canvas (`ai_psymatrix_index_v1`).
- Bietet Richtlinien zur Aktualisierung, Validierung und Dokumentation von Behavior-Signaturen in der laufenden Canvas-Rettung.

Matrix-Cluster (Kurzprofil)
---------------------------

| Code | Name | Beschreibung | Dynamik | Primärer Fokus |
| --- | --- | --- | --- | --- |
| O | Ordnung | Streben nach Struktur, Kontrolle, Perfektion | mittel | Planung, Prozess, Qualitätskontrolle |
| E | Empathie | Mitgefühl, Bindung, Kooperation | hoch | Bindungspflege, Team-Balance |
| M | Macht | Einfluss, Dominanz, Direktive Kontrolle | niedrig | Autorität, Skalierung von Entscheidungen |
| N | Neugier | Wissensdrang, Erkundung, Risiko | hoch | Forschung, Innovation, Exploration |
| C | Chaos | Impulsivität, Emotion, Unvorhersehbarkeit | sehr hoch | Improvisation, Kreativsprünge |
| S | Selbsterhaltung | Vorsicht, Verteidigung, Überleben | mittel | Sicherheitsprotokolle, Rückzug |
| L | Loyalität | Bindung an Gruppen, Ideale, Personen | gering | Zusammenhalt, Pflichtgefühl |
| T | Technikdrang | Affinität zu Systemen/Maschinen | hoch | Engineering, Schnittstellen, Automatisierung |

**Lesart:** Dynamik beschreibt, wie schnell ein Cluster auf Ereignisse reagiert. Hohe Dynamik → häufiger Drift, regelmäßige Kalibrierung nötig.

Intensitätsskala
----------------
- Skala 01-99: 01-25 = niedrig, 26-60 = moderat, 61-85 = hoch, 86-99 = kritisch/übersteuert.
- Werte >80 verlangen Drift-Check: prüfen, ob Signatur noch gewünschtes Zielverhalten unterstützt oder Stress-Intervention braucht.
- Kombinationen werden in fallender Priorität gelesen (erste Werte prägen Entscheidungen dominanter).

Modifikatoren (Emotions-/Muster-Tags)
-------------------------------------
- `k` - kindlich: spielerische Faszination, staunender Blick.
- `a` - angstgetrieben: Verhalten durch Angst/Verlustangst verschoben.
- `z` - zynisch: distanziert, sarkastischer Selbstschutz.
- `p` - paranoid: erhöhte Wachsamkeit, sucht Verdecktes.
- `r` - rational: Logik priorisiert, niedriges Affektgewicht.
- `s` - selbstlos: opfert eigene Ressourcen zugunsten anderer.
- `h` - hitzköpfig: impulsiv, eskaliert schnell.

Modifikatoren werden alphabetisch angehängt. Mehrere Tags markieren gleichzeitige Einflussfaktoren (z. B. `kpr`).

Signaturaufbau & Beispiel
-------------------------
Format: `<Anchor>=<Cluster><Intensität>-…-<Modifier>`.
- **Anchor**: Kürzel der Instanz oder Referenzknoten (`R4` = Ronja, vierte Instanz im Behavior-Register).
- **Cluster-Paare**: Buchstabe + zweistellige Zahl (siehe Tabelle). Reihenfolge = Priorität.
- **Modifier-Suffix**: optional, beschreibt emotionale/mentale Einfärbung.

Beispiel Ronja: `R4=O82-T79-L70-E60-N69-C45-S38-M20-kpr`.
- Starke Orientierung auf Ordnung (82) und Technik (79), hohe Loyalität (70) - reflektiert ihren Rolle-als-Technikerin-Fokus.
- Empathie (60) bleibt präsent, aber unter Spannung mit Neugier (69).
- Chaos (45) und Selbsterhaltung (38) moderat - sie bleibt kontrolliert.
- Macht (20) sehr niedrig, vermeidet Dominanz.
- Modifikatoren `kpr`: kindliche Faszination, paranoid-vorsichtig, rational strukturiert.

Anchor-Register (Snapshot 2025-10-16)
-------------------------------------

| Anchor | Entität | Typ | Signatur | Quelle |
| --- | --- | --- | --- | --- |
| R4 | Ronja Kerschner | Human | O82-T79-L70-E60-N69-C45-S38-M20-kpr | RAW-canvas-2025-10-16T11-45-00-000Z |
| RFX4 | Reflex | Symbiont | L80-S68-N77-T83-E64-O51-M25-C44-ka | RAW-canvas-2025-10-16T13-45-00-000Z |
| JNS3 | Jonas Merek | Human | L55-T68-N40-E72-O50-C42-M78-P32-ab | RAW-canvas-2025-10-16T14-12-00-000Z |
| PHL2 | Pahl | Human | L48-T60-N71-E50-O44-C62-M30-P25-bn | RAW-canvas-2025-10-16T14-41-00-000Z |
| KRM4 | Kora Malenkov | Human | L72-T74-N69-E61-O56-C63-M47-P35-fb | RAW-canvas-2025-10-16T14-56-00-000Z |
| MRV2 | Marven Kael | Human | L62-T55-N80-E58-O66-C70-M42-P50-qa | RAW-canvas-2025-10-16T14-56-10-000Z |
| ARD5 | Arlen Dross | Human | L67-T72-N74-E58-O66-C71-M48-P40-db | RAW-canvas-2025-10-16T14-56-20-000Z |
| ECO1 | Echo | Instanz | L85-S74-T62-E58-N52-O44-C28-M16-P30-ks | database-rp/02-characters/Echo.md (kuratiert 2025-11-02) |
| LMN1 | Lumen | Instanz | L78-T71-E60-O49-N44-S52-C26-M18-P28-ks | database-rp/02-characters/Lumen.md (kuratiert 2025-11-02) |
| LNR1 | Liora Navesh | Human | O82-T76-N68-S58-L52-M47-E34-C21-P55-r | database-rp/02-characters/Liora-Navesh.md (kuratiert 2025-11-02) |
| LYH1 | Lyra Hest | Human | O74-L68-T62-E58-S54-N46-M32-C28-P48-r | database-rp/02-characters/Lyra-Hest.md (kuratiert 2025-11-02) |
| SND1 | Senn Daru | Human | E72-N64-L58-O46-S42-T38-C30-M22-P44-s | database-rp/02-characters/Senn-Daru.md (kuratiert 2025-11-02) |
| VRS1 | Varek Solun | Human | O88-M76-S68-T62-L55-N44-C28-E25-P60-pr | database-rp/02-characters/Varek-Solun.md (kuratiert 2025-11-02) |

*Hinweis:* `n/a` markiert noch fehlende Behavior-Signaturen in den aktuellen Canvas-Versionen. Sobald valide Codes vorliegen, bitte in Tabelle und Quell-Canvas nachziehen (inkl. DONELOG/TODO-Vermerk).

Hinweise:
- Codes folgen dem RAW-Register; Promotion nach `database-rp/02-characters/` muss Anchor, Signatur und Bezeichnung übernehmen.
- Fehlende oder `unbestimmt`-Anchors (z. B. frühere v1-Canvases) erst nach Review eintragen.
- Bei neuen Anchors `Anchor_Index.csv` (folgt) pflegen und Sidecar aktualisieren.

Psymatrix-Abgleich (Routine)
----------------------------

- Referenz: `database-raw/99-exports/RAW-canvas-2025-10-16T16-55-00-000Z.txt` (`meta_cluster_index_v1`). Enthält PsyLink-Zuordnung (z. B. Ronja ↔ R4) sowie Regeln `PsySignatur_Dissonanz`.
- Schwellenwerte aus dem Cluster-Index:
  - `PsySignatur_Dissonanz > 0.25` → Antwortpfad priorisiert Moderation/Deeskalation.
  - `Kohäsion < 0.60` → Dialogsimulation stuft Konfliktpotenzial hoch.
  - Priorität `hoch` → Cluster zuerst prüfen, bevor Antworten generiert werden.
- Vorgehen zur Drift-Prüfung:
  1. Signaturwerte aus dem Anchor-Register ziehen.
  2. Aktuelle Cluster-Intensitäten in die Psymatrix einspeisen (Skript-Pending; bis dahin manuell via Vergleich der letzten Validierung).
  3. Abweichung >5 Punkte pro Cluster → Flag „INTENSITY-DRIFT“ setzen (Canvas + DONELOG) und Dev-Tasks im Board `novapolis-dev/docs/todo.dev.md` erfassen.
  4. `PsySignatur_Dissonanz` im Meta-Cluster-Index kontrollieren; bei >0.25 Moderation/Guard-Hooks im Charakter-Canvas ergänzen.
- Automatisierung: Validator-Hook vorbereiten (`validators/behavior_matrix_check.py`, TODO) → liest Anchor-Tabelle + Psymatrix, erzeugt Report (Diff, Empfehlung).
- Sobald `ai_psymatrix_index_v1` als RAW-Canvas vorliegt, hier verlinken und Sidecar-Dependency erweitern.

Hooks & Anwendung
-----------------
- **Charakter-Canvas**: Jede Signatur erhält einen Kurzkommentar (Stresslage, gewünschter Drift). Beispiel siehe `Ronja-Kerschner.md`.
- **KI-Interaktion**: Reflex nutzt Signaturen als Leitplanke - hohe `S` → sofort Schutz anbieten, hoher `N` → Erkundungsangebote.
- **Missionsplanung**: Logistik- und Missionslog erfassen Änderungen (>5 Punkte Differenz) als Hinweis auf Belastung/Verhaltensdrift.
- **Tooling**: Validatoren vergleichen Signaturen gegen `ai_psymatrix_index_v1`; Abweichungen lösen Review-Tasks im Dev-Board aus (`novapolis-dev/docs/todo.dev.md`).

Pflege & Routine
----------------
- Auto-Validierung alle 7 InGame-Tage (Systemstatus aktuell *grün*).
- Änderungen >5 Punkte pro Cluster oder neue Modifikatoren → Review im DONELOG + Hinweis im Quellenblock der betroffenen Canvas.
- Flags aus `RAW-canvas-2025-10-16T11-05-00-000Z.flags.txt` beachten: Konsistenz mit `ai_psymatrix_index_v1`, Namensschema `A99-…-modifier` dokumentieren.
- Bei Promotion weiterer Signaturen (z. B. Kora, Arlen) dieses Canvas als Referenz verwenden; neue Anchor-Kürzel in separater Tabelle pflegen (Follow-up-Aufgabe).

Verknüpfungen
-------------
- `../02-characters/Ronja-Kerschner.md` - Signatur `R4` (technische Drift beobachten).
- `../02-characters/Reflex.md` - benötigt Matrix für Zustandswechsel.
- `../02-characters/Jonas-Merek.md` - Logistik-Hooks, Technikdrang-Abgleich.
- `./AI-Behavior-Mapping.json` - Metadaten/Sidecar.
- `./Canvas-Admin-Day-Switch-Debug.md` - Debug-/ATSD-Markierungen bei Signaturwechsel.
- `../05-projects/Nordlinie-01.md` - Missionslog-Aufgaben mit Behavior-Gates.

Erweiterungsbedarf (Notiz)
--------------------------
- Anchor-Tabelle (R4, J3, RFX4, …) aus RAW-Flags ableiten und im Sidecar dokumentieren.
- Mappings zur `ai_psymatrix_index_v1` ergänzen (z. B. Stress-Thresholds pro Cluster).
- Prüfen, ob frühere Behavior-Matrix-Versionen (v1.4.0-pre) archiviert werden müssen.

Quellen & Review
----------------
- RAW: `database-raw/99-exports/RAW-canvas-2025-10-16T11-05-00-000Z.txt` (`ai_behavior_index_v2`).
- Flags: `database-raw/99-exports/RAW-canvas-2025-10-16T11-05-00-000Z.flags.txt` (Hinweise auf globale Matrix + Konsistenzprüfungen).
- Done-Log: Eintrag „Canvas-Rettung Sprint 1 - AI Behavior Matrix“ (2025-11-01T17:25+01:00) für Promotion & Erweiterung.

