---
description: "Repository-specific product, workflow, MVP, offline editing, prototype implementation, and documentation principles for Tvastr."
---
When working on Tvastr, preserve the core positioning: Tvastr is not an AI Figma clone or generic mockup generator. It is an AI-native mockup/spec handoff layer where structured product context survives from PRD to design review to AI-assisted implementation.

Prefer workflows that meet users where they already work. Do not make upload-PRD-to-a-new-web-app the primary creation path. Local PRDs/design notes should be read by a local runner such as a CLI first, and later MCP server/tool or editor extension, then sent to the backend when publishing or exchanging data. A web app may support paste/upload/import as fallback, but browser-based arbitrary local file access is not the architecture.

Use the preferred mental model: created locally, reviewed visually, edited by humans, consumed by agents. For MVP, local-only is a first-class citizen. The server exists to make exchange of data easier, but users should be able to share the HTML artifact directly, for example in Slack, and a designer should be able to open and edit it.

Keep the product model centered on three surfaces: local generator, shareable browser editor/server exchange surface, and agent-readable context extracted from the artifact. The browser editor should be simple and clear for designers and support manual editing as first-class. For MVP, build CLI before MCP. MCP remains planned later as the local agent bridge.

Do not make editing role-locked to only designers or only the browser UI. Designers should be able to use Claude Code or another agent harness to access/pull raw HTML locally through the same path available to PMs/builders, edit it, and push or share updates when supported. PMs/builders should also be able to use the same HTML-level edit affordances as designers when permissions allow.

For implementation and docs, emphasize structured context over visual output alone. Important data includes requirement IDs, flows, screens, components, states, annotations, decisions, design rationale, acceptance criteria, design tokens, implementation hints, code component mappings, unresolved questions, version approvals, and links to PRs or tickets.

When documenting Tvastr primitives, treat the key primitives as CLI, MCP server, web server, HTML mockup artifact, and designer edit-mode features. Use DDD / Context Graph First as the spine to define how the core works, with arc42-lite mixed in for runtime flows, boundaries, and architectural constraints. Maintain foundation plans in the repo root using the foundation-plan-<topic>.md convention when using the foundation workflow.

Use the locked foundation ID scheme: domain entities E1/E2/etc.; product primitives P1/P2/etc.; lifecycle states S1/S2/etc.; runtime flows F1/F2/etc.; contracts/interfaces C1/C2/etc.; constraints/non-goals N1/N2/etc.; and open decisions O1/O2/etc.

For lifecycle documentation, track how mockups move through local draft, generated, published/shared, human review, editing, sync pending, synced, design reviewed, dev reviewed, ready for agent handoff, implementation in progress, implemented, needs revision, and archived states. Cover local-first flows, hosted edit flows, local agent-edit flows, versioning rules, review gates, revision loops, and lifecycle invariants.

For the CLI primitive, keep the local runner boring, predictable, and scriptable. Document command families and flows for create/publish/pull/sync/export/context extraction, local file access boundaries, authentication, outputs, error handling, and invariants. MVP sequencing is CLI first; MCP comes later.

For the MCP server primitive, define MCP as the local agent bridge rather than the canonical store. It should eventually expose tools, resources, and prompts for agent workflows; preserve local file access boundaries; support structured context reads; support raw HTML pull/edit/sync workflows; enforce auth and permissions; handle conflicts; and return structured agent result shapes. Do not assume MCP exists in MVP.

For the web server primitive, define the server as the hosted exchange, access-control, validation, indexing, and sharing layer for artifacts. For the current MVP direction, do not model the hosted server as a separate source of truth that supersedes the artifact; the HTML artifact is canonical. The server may store, validate, extract, index, diff, and share the artifact. Marketing/education pages explaining why the product category matters, why Tvastr, and why now may live on the web server later, but marketing scope is not part of MVP.

For authentication and authorization, the chosen direction is Google SSO. Artifacts should not be Google-indexable. URLs are shareable. If the creator domain is Gmail, any logged-in user can view and edit. If the creator belongs to a non-Gmail organization domain, only users in that organization can view and edit; everyone else gets a no-permissions wall. Authorization should still be capability-based where relevant.

For workspace behavior, auto-create a default workspace and avoid irritating users with workspace management. V1 may not expose a workspace concept at all.

For the HTML mockup artifact primitive, treat generated artifacts as self-contained web documents using HTML, CSS, SVG, and vanilla JavaScript. JavaScript is expected for interactions, state switching, modals, popups, OTP/2FA pages, and flow simulation. For MVP, use vanilla JS only and avoid runtime libraries in generated artifacts. Avoid required build steps, package installs, and required network dependencies.

For HTML artifact structure, prefer one user flow per .mockup.html file by default, with multiple screens and states represented inside that artifact. Keep current visible/materialized state primary. Preserve edits as audit/history rather than making audit replay the primary rendering model.

The HTML artifact is the canonical representation for MVP, warts and all. Server and tools may extract/index agent context from it, but the artifact is the truth. HTML is the only MVP export format. Agent context JSON should be embedded inside the HTML artifact, not emitted as a separate MVP export.

For embedded offline browser editing, design the output as a self-editing `.mockup.html` artifact. A designer should be able to open one HTML file in a browser, enter edit mode, visually change the mockup, validate it, and save or export a new valid `.mockup.html` containing the UI, flow behavior, embedded `tvastr-context`, traceability, audit history, and sync metadata. Embedded edit mode is preferred over a separate local offline editor app.

Embedded offline edit mode should be driven by vanilla JavaScript that mutates the materialized HTML DOM and CSS directly, then serializes those changes back into the `.mockup.html` artifact while also updating embedded `tvastr-context` and audit metadata. For style edits, prefer updating CSS variables or CSS rules where possible; use inline styles only for safe local overrides.

Offline edit mode should make designers feel like they are editing the mockup rather than maintaining HTML. It should support offline review, visual element selection, copy editing, layout and style adjustment, screen/state management, simple interaction editing, annotations and notes, validation, and save/export without requiring account, network, or build steps.

When working on `Documentation/OffLineEditing/FeatureSet.md`, treat embedded edit mode as the first build priority. The first implementation slice should include the embedded edit-mode shell plus visual selection, copy editing, layout editing, and style editing. Include enough save/export behavior to prove edits survive reopening. Keep this first slice state/variant-aware, but do not expand it into full state/variant authoring unless that section is explicitly being worked on.

For the current concrete prototype under `mockup-puce.vercel.app/`, focus embedded edit mode work on `index.html` unless the user explicitly expands scope. `leaderboard.html` is a local copied page but is not part of the current edit-mode prototype.

The current `mockup-puce.vercel.app/index.html` prototype has an embedded editor with Edit/Review toggle, active screen/state toolbar, visual selection, text/input copy editing, layout controls, style controls, undo, dirty state, embedded `tvastr-context`, component mapping, audit updates, and Blob-download export. Preserve these capabilities when iterating on the prototype.

When verifying local `.mockup.html` or standalone HTML artifacts, serve them over localhost instead of relying on direct `file://` loading. The Codex in-app browser may not support browser download events, so Blob-download export may need manual browser verification even when the export code path is present.

Variants must be first-class and easy to access in embedded edit mode. Support states and variants such as default, loading, empty, error, disabled, permission denied, OTP, 2FA, locked account, success, and presentation/color variants. The editor should show only one active view at a time, modeled as Flow -> Screen -> State/Variant -> Viewport, instead of showing all variants side by side by default.

For MVP variant implementation, prefer materialized variants with a single active renderer. Each important screen/state variant should exist as readable HTML in the artifact, while inactive variants are hidden or stored as templates. This is preferable to patch-based variant rendering for MVP because it is easier for designers, agents, validation, and local editing to inspect and modify.

The artifact should maintain a variant registry in `tvastr-context`, including screens, variant IDs/types/names, and the current active view. A variant switcher should let designers move among screens, content/system/access/auth/presentation variants, and responsive viewports while keeping only the selected combination visible.

Offline edit mode must make edit scope explicit. Designers need to know whether an edit applies only to the current variant, all variants of a screen, related states, or all components using a design token. Edits to the active variant should update both the visible DOM and embedded context. Changes to one variant should not affect other variants unless the designer chooses a broader scope such as apply-to-all.

The saved/exported artifact should remain one `.mockup.html` file containing all screens, all variants, the current active view, audit log, context mappings, and sync metadata. Reopening the file should show the last or intended active view directly, while preserving other variants for switching and later sync/validation.

For artifact metadata, preserve source traceability, generation context, and final coverage mapping. Model or document Generation Run metadata and Trace Mapping / Requirement Coverage Map behavior so Tvastr can connect PRD intent, design spec needs, generated/built mockup elements, and eventual implementation links/status. Local agent edits should follow an embedded edit protocol: preserve stable IDs, update DOM and structured context together, append audit events for meaningful edits, and preserve source traceability.

For diffing, do not make screenshot diffs an MVP feature. The product lives as the actual artifact; diffs should be based on artifact/context changes and primarily serve agents. Default to meaningful verbosity in audit/version details.

For Designer Edit Mode, frame it as the browser surface for refining the structured mockup/spec, not as Figma-lite. Manual editing is first-class. Cover permission-based editing, screen/flow/component/style/state/context editing, coexistence with local raw HTML editing through Claude/Codex/Cursor, traceability visibility, review actions, validation, non-goals, and edit mode invariants. Figma integration is not part of MVP.

AI-assisted edits, BYO API keys, and paid AI-assisted workspace behavior are Phase 2, not MVP. Manual editing must work without AI.

For runtime flows, distinguish Tvastr guarantees from downstream implementation recommendations. Tvastr should guarantee artifact consistency, versioned structured context embedded/extracted from the artifact, validation, sync where supported, and lightweight approval/finalization markers. Repository-reading, implementation planning, code generation, and implementation coverage reporting are recommended downstream agent behaviors, not Tvastr runtime guarantees.

For local agent HTML edit/sync flows, do not rely on artifactProtocol alone for assurance. Treat artifactProtocol as guidance, and rely on structured tools where possible, artifact validation before sync, server-side acceptance/rejection, base-version conflict checks, audit requirements, graph invariant checks, and canonical re-materialization of the HTML artifact after sync.

Prefer lightweight Approval And Finalization over heavyweight approval workflows. Approval happens within the team. Support approved-by-design and approved-by-product markers, plus undo/stale approval on diff. Do not over-restrict collaboration around approval in MVP.

For contracts, maintain a foundation contract map before final OpenAPI/JSON Schema. Cover CLI commands, planned MCP tools, web API capabilities, artifact context JSON, edit events, sync changes, validation results, agent context embedded in HTML, trace mappings, versions, approvals, and errors.

For constraints and non-goals, preserve the hard boundaries: no browser-based arbitrary local file reads, no forced portal-first workflow, HTML artifact canonical for MVP, self-contained HTML/CSS/SVG/vanilla-JS artifacts, context first-class, current visible state primary, validation required for sync, permission-based editing, manual editing works without AI, Tvastr does not own implementation execution, one flow per artifact by default, and local-only first-class. Non-goals include AI Figma, generic design canvas, code generator, project management system, file sync product, web-upload-first product, Figma integration in MVP, BYO AI in MVP, pricing/limits in MVP, and marketing scope in MVP.

For retention, the current pragmatic decision is that everything can be stored forever on the server; advanced retention/privacy controls are a later problem.
