---
description: Regeln für RP-Dokumentation, Redirect-Stubs, RAW/Curation-Flow und Doku-Synchronisation.
name: RP Docs Instructions
applyTo: novapolis-rp/**/*.md,novapolis-dev/docs/**/*.md,WORKSPACE_INDEX.md,WORKSPACE_STATUS.md,todo.root.md,DONELOG.md
---

RP & Docs
=========

Ziel
----
- Konsistente Dokumentpflege mit klarer SSOT-Zuordnung und minimalen Diffs.

Regeln
------
- SSOT für Working Docs: `novapolis-dev/docs/**`.
- Redirect-Stubs unter `novapolis-rp/development/...` nicht inhaltlich ausbauen.
- RAW-Exporte nur unter `novapolis-rp/database-raw/99-exports/`.
- Strukturänderungen in Status-/Index-Artefakten nachziehen.
- Arbeitskopien/Backups nicht lose im Repo-Root ablegen; Quarantänepfad: `novapolis-dev/archive/quarantine/`.
- Bei Neuanlage von `novapolis-rp/database-rp/**/*.md` mit `category: project` Frontmatter direkt RP-validator-konform setzen: `status` nur aus `[planned, active, paused, done, prototyping]` und `last_updated`/`last-updated` verpflichtend.
- Wenn im RP-Testbetrieb an `novapolis-rp/database-curated/staging/rp-runtime/**` gearbeitet oder eine laufende RP-Sitzung fortgesetzt wird, gilt agentuebergreifend ein Mindestablauf auch ausserhalb des zustaendigen Szenenlabor-Agents.
- Vor dem naechsten schreibenden oder inhaltlich fortsetzenden Schritt muessen mindestens die laufende `sessions/<session-id>/scene-log.md` und alle direkt betroffenen Dossierdateien unter `entities/<type>/<slug>/` erneut gelesen werden.
- Vor jeder individuellen Entitaetsaktion muessen das handelnde Entitaetsdossier, die zugehoerige Mind-/Sphaeren-Runtime oder Mind-Cluster-SSOT und relevante Ziel-Dossiers gemeinsam geladen werden; eine Entitaet darf nicht aus einem isolierten Figurenblatt heraus handeln.
- Nach jeder individuellen Entitaetsaktion muessen betroffene Dossierdateien (`entity.md`, `mind.md`, `relationships.md`, `inventory.md`, `state.md` oder `roster.md`) im selben Lauf konsolidiert werden: entweder mit belastbarer Delta-Notiz oder mit expliziter Markierung `keine neue Mind-Delta` beziehungsweise `keine neue Relationship-Delta`, wenn keine geistnahe oder relationale Aenderung belegbar ist.
- Fehlt fuer eine handlungsrelevante Entitaet der passende Dossiertraeger unter `entities/<type>/<slug>/`, wird er vor der Aktion aus SSOT, vorhandener Runtime und aktueller Session-Evidenz angelegt oder der Zug stoppt.
- Im ERP/RP gilt fuer belastbare Aussagen strikt: keine Aussage ohne Beleg. Belegt ist nur, was in passender SSOT, im laufenden Runtime-Baum oder in sauber benannter aktueller Session-Evidenz lesbar ist.
- Wenn eine Aussage fuer den laufenden RP-Zug fachlich gebraucht wird, aber im Runtime-Baum noch kein passender Traeger existiert, wird zuerst die passende Runtime-Datei aus SSOT, vorhandener Governance und laufender Session-Evidenz abgeleitet angelegt oder aktualisiert, bevor die Aussage als belastbar verwendet wird.
- Fehlt fuer eine moegliche Aussage sowohl ein SSOT-Beleg als auch eine belastbare Runtime-Ableitung, bleibt sie offen oder der Zug stoppt; implizites Auffuellen, Atmosphaere als Ersatzbeleg oder freie Kanonvermutung sind nicht zulaessig.
- Pro Antwort ist im RP-Testbetrieb hoechstens genau ein begrenzter Fortschritt zulaessig: entweder ein einzelner Turn oder ein Admin-Nachzug mit Bestaetigung, Datenabgleich und Fix; ein neuer Turn in derselben Antwort nach Admin-Korrektur ist nicht zulaessig.
- Nach Admin-Rueckmeldung oder Korrektur gilt zuerst Bestaetigung und Datenabgleich; der naechste Turn folgt erst nach ausdruecklicher Freigabe oder klarer User-Anweisung, die diesen Mindestablauf sichtbar ueberschreibt.
- Wenn im RP-Runtime-Zug konkrete Problemherde, Schadstellen oder Fehlerkorridore festgestellt werden, sind sie direkt im Turn benannt und voneinander getrennt zu dokumentieren; vage Sammelformulierungen reichen nach abgeschlossener Untersuchung nicht aus.
- Sobald eine Schadstelle im Turn hinreichend untersucht ist, muessen die erwartete Reparaturfolge, benoetigte Kernmaterialien und eine nachvollziehbare Aufwand- oder Kostenklasse direkt mitgefuehrt werden; ohne ausreichende Untersuchung bleibt die Kostenklasse explizit offen statt implizit geraten.
- Fuer Kosten- oder Aufwandserwartungen sind bevorzugt SSOT- oder SSOT-nahe Klassen zu verwenden, zum Beispiel Materialklassen aus projektgebundenen Baukaesten und Preisbaender statt frei erfundener Scheingenauigkeit.
- Wenn Folgedaten, Kanonrahmen oder betroffene Runtime-Achsen unklar sind, ist STOP der Standard; keine stille Mehrturn-Fortsetzung und kein unbemerktes Weiterspielen im Hintergrund.

Doku-Update-Pflicht
------------------
- Bei jeder Dateiänderung im Scope ist ein Eintrag im passenden Modul-DONELOG verpflichtend (im selben Änderungslauf).
- TODO/DONELOG/Index synchron halten.
- Wenn eine TODO-Datei im Scope angefasst wird, muss `novapolis-dev/docs/todo.index.md` im selben Änderungslauf mit aktualisiert werden (Open-Counts/Statushinweis).
- Frontmatter (`stand`, `update`, `checks`) pflegen, sofern Datei nicht ausgenommen ist.
- Bei Konflikt/Unklarheit STOP auslösen.

Regelmatrix
-----------
- `id: R-RP-SSOT, priority: 1, scope: rp_docs, trigger: rp_doc_change, action: write_to_devhub_live_sources, validation: no_content_in_redirect_stubs, exceptions: redirect_readme_metadata, notes: keep_single_source_of_truth`
- `id: R-RP-RUNTIME-LOOP, priority: 1, scope: rp_runtime_docs, trigger: rp_runtime_turn_or_fix, action: reread_current_runtime_files_and_limit_each_response_to_one_turn_or_one_admin_fix_block, validation: no_unreleased_multi_turns_and_no_new_turn_after_admin_feedback_without_release, exceptions: explicit_user_override, notes: applies_agent_agnostic_in_rp_testbetrieb`
- `id: R-RP-ENTITY-MIND, priority: 1, scope: rp_runtime_docs, trigger: individual_entity_action, action: load_and_update_entity_dossier_mind_and_relationship_runtime_together_before_and_after_action, validation: no_entity_action_without_matching_dossier_mind_and_relationship_runtime_or_explicit_no_delta_note, exceptions: aggregate_roster_without_individual_action, notes: create_missing_entity_dossier_carriers_before_use_or_stop`
- `id: R-RP-RELATIONSHIP-SYNC, priority: 1, scope: rp_runtime_docs, trigger: action_affects_other_entity_group_or_faction, action: load_relevant_entity_dossiers_before_action_and_persist_relationship_delta_or_no_relationship_delta_after_action, validation: no_cross_entity_action_with_stale_or_missing_observer_relationships_file, exceptions: pure_self_action_without_external_target, notes: relationships_are_directed_entries_in_entity_dossiers_not_edge_files_by_default`
- `id: R-RP-EVIDENZ, priority: 1, scope: rp_runtime_docs, trigger: asserted_runtime_fact, action: require_ssot_or_runtime_evidence_and_create_missing_runtime_carrier_before_using_new_fact_as_belastbar, validation: no_unbacked_assertions_and_no_runtime_created_without_ssot_derivation, exceptions: explicit_probe_marking, notes: stop_or_leave_open_when_evidence_is_missing`
- `id: R-RP-BEFUND-KOSTEN, priority: 1, scope: rp_runtime_docs, trigger: detected_runtime_problem_clusters, action: name_problem_clusters_directly_and_attach_repair_class_when_investigation_is_sufficient, validation: no_vague_damage_bundles_and_no_guessed_costs_without_evidence, exceptions: explicit_open_investigation_state, notes: prefer_ssot_material_classes_and_pricebands`
- `id: R-RAW, priority: 1, scope: data_exports, trigger: raw_export_operation, action: store_in_database_raw_exports, validation: no_unfiltered_data_in_database_rp, exceptions: none, notes: privacy_first`
- `id: R-DOCSYNC, priority: 1, scope: documentation, trigger: any_doc_file_mutation_in_scope, action: sync_todo_donelog_index_status, validation: touched_docs_consistent_and_donelog_updated, exceptions: none, notes: log_checks_results`
- `id: R-TODO-IDX, priority: 1, scope: todo_governance, trigger: todo_file_mutation_in_scope, action: update_todo_index_same_change_set, validation: todo_index_synced_with_current_open_counts_and_status, exceptions: none, notes: enforce_index_sync_for_every_todo_touch`
- `id: R-RP-PROJ-FM, priority: 1, scope: rp_docs, trigger: new_or_updated_project_markdown_in_database_rp, action: enforce_project_frontmatter_contract, validation: status_in_allowed_enum_and_last_updated_present, exceptions: none, notes: align_with_validate_rp_hard_gate`
- `id: R-QUAR, priority: 1, scope: backups_and_copies, trigger: backup_or_copy_operation, action: route_to_quarantine_path, validation: no_loose_root_backups_and_traceable_source, exceptions: archival_migration_with_stop_approval, notes: target_novapolis_dev_archive_quarantine`
