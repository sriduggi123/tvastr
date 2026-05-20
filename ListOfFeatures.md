# List Of Features

This document lists the PRDs that should be written to build Tvastr from the foundation document.

Source of truth: `TvastrPrimitivesFoundation.md` only.

## Priority Definitions

| Priority | Meaning |
| --- | --- |
| Foundational | Specification or decision work that must exist before multiple build PRDs can be implemented safely. These are not always user-facing features, but they define the product substrate. |
| P0 Make-Or-Break | Day-0 product proof. If this is weak, users will not believe the product, even if the surrounding platform works. |
| P0 Supporting | MVP-critical enabler for the make-or-break loop. Partial failure hurts, but does not singularly define whether Tvastr is a real product. |
| P1 | Near-term capability after the MVP spine works. Important, but not required for first useful launch. |
| Post MVP | Explicitly later, phase 2, not MVP, or only useful after the product has usage. |

## Recommended Build Order

1. Write the foundational PRDs that protect the two make-or-break capabilities: MVP architecture, context graph, HTML artifact protocol, lifecycle/status, contracts/errors, validation/versioning/audit, and trace/agent context.
2. Build and iterate the P0 make-or-break loop: generation engine and full HTML artifact editing capability. This is the product proof.
3. Build the P0 supporting creation and access loop: CLI local file ingestion, local `.mockup.html` output, publish, hosted artifact store, Google SSO/domain sharing, and hosted viewer.
4. Build the P0 supporting preservation loop: validation, save/version/audit, HTML export/local-only mode, agent context extraction, and lightweight approval markers.
5. Build the P0 supporting local sync loop: CLI pull, validate, sync, conflict prevention, and server acceptance.
6. Build P1 agent and collaboration depth: MCP server, structured edit tools, collaboration panels, direct agent APIs, diffs, implementation links, and CLI polish.
7. Build Post MVP surfaces only after the core loop proves useful: Figma, BYO keys, marketing, pricing, retention controls, and non-HTML exports.

## Product Risk Ranking

The product has two make-or-break capabilities:

1. **Generation Engine**: Tvastr must generate a coherent, useful, traceable mockup/spec artifact from product intent. It cannot merely produce attractive disconnected screens.
2. **HTML Artifact Editing Capability**: Tvastr must let humans and agents correct, extend, and preserve the generated artifact from day 0. There is no basic/advanced split here; the editing model must support the full conceptual surface immediately.

Everything else is supporting product infrastructure. Auth, hosting, CLI polish, approvals, MCP, integrations, and collaboration matter, but they do not singularly create belief in the product if generation and editing fail.

## Foundational PRDs

### FND-01: MVP Architecture And Primitive Boundaries

Priority: Foundational

Build order: 1

Requirement brief:
Define how the five primitives work together: CLI (P1), MCP Server (P2), Web Server (P3), HTML Mockup Artifact (P4), and Designer Edit Mode (P5). The PRD should preserve the operating model: created locally, reviewed visually, edited by humans, consumed by agents.

Acceptance criteria:

- Defines responsibilities and non-responsibilities for P1-P5.
- Makes CLI-first explicit and MCP later.
- States that the web app must not be the required starting point.
- States that the Web Server stores the canonical published HTML artifact.
- States that local-only mode remains first-class.
- Defines which features are MVP, P1, and Post MVP.

### FND-02: Core Context Graph And Data Model

Priority: Foundational

Build order: 1

Requirement brief:
Define the Tvastr context graph as the product data model: Workspace, Project, Source Document, Mockup Spec, Flow, Screen, Component, Requirement, State, Annotation, Decision, Design Token, Component Mapping, Version, Export, Agent Context, Implementation Link, Actor, Generation Run, and Trace Mapping.

Acceptance criteria:

- Covers entities E1-E20 from the foundation document.
- Treats Mockup Spec (E4) as the aggregate root embedded in the HTML artifact.
- Defines graph invariants for screens, components, states, annotations, decisions, exports, agent context, generation runs, and trace mappings.
- Defines stable IDs for DOM-to-context mapping.
- Avoids creating a hidden canonical graph that can drift from the HTML artifact.

### FND-03: HTML Artifact Protocol

Priority: Foundational

Build order: 1

Requirement brief:
Specify the portable `.mockup.html` artifact format. It must be a self-contained HTML/CSS/SVG/vanilla JavaScript document with embedded structured context, sync metadata, artifact protocol, and audit log.

Acceptance criteria:

- Defines the required file shape, including `tvastr-context`.
- Allows HTML, CSS, SVG, vanilla JavaScript, and embedded JSON context.
- Disallows required network dependencies, package installs, build steps, minified/obfuscated output, remote scripts for core behavior, canvas-only rendering, and bundled UI/helper libraries for MVP.
- Defines one flow per artifact by default.
- Defines the artifact protocol rules for local agent edits.
- Defines local mode, hosted mode, and agent mode.

### FND-04: Validation, Versioning, Audit, And Diff Rules

Priority: Foundational

Build order: 1

Requirement brief:
Define the shared rules used by CLI, Web Server, Designer Edit Mode, and later MCP to validate artifacts, create versions, preserve audit history, and produce agent-oriented diffs.

Acceptance criteria:

- Blocks broken context JSON, missing required IDs, invalid sync metadata, and graph invariant violations.
- Treats missing audit entries and some trace gaps as warnings at first.
- Creates versions for meaningful saves, syncs, generation runs, approval changes, and major context edits.
- Preserves audit logs generously.
- Defines HTML/context/trace/audit diffs for agents.
- Excludes screenshot diffs from MVP.

### FND-05: Trace Mapping And Agent Context Contract

Priority: Foundational

Build order: 1

Requirement brief:
Define how Tvastr records traceability and handoff context. Trace Mapping (E20) must connect source requirements and design guidance to screens, components, states, decisions, versions, component mappings, and later implementation links. Agent Context (E16) must be embedded in the HTML artifact and extracted for tools.

Acceptance criteria:

- Defines trace mapping statuses: covered, partial, missing, deferred, not applicable.
- Defines the agent context shape for flows, screens, components, requirements, states, annotations, decisions, component mappings, trace mappings, open questions, and implementation hints.
- Requires agent context to reference a specific Version (E14).
- Makes clear that agent context is not a separate MVP export format.
- Makes clear that implementation execution is outside Tvastr's guaranteed runtime boundary.

### FND-06: Lifecycle And Status Model

Priority: Foundational

Build order: 1

Requirement brief:
Define lifecycle states and transitions for local drafts, generation, publication, review, editing, sync, handoff, revision, approval, implementation reference, and archive. The lifecycle should clarify status without becoming a rigid project-management workflow.

Acceptance criteria:

- Covers lifecycle states S1-S15 from the foundation document.
- Defines expected transitions for CLI create/publish, hosted browser edit, local edit/sync, agent handoff, approval/finalization, revision/regeneration, and export.
- Allows teams to skip steps, loop backward, branch versions, or keep a mockup local.
- Defines which lifecycle changes require a Version (E14).
- Defines what status must be exposed through CLI, web, and later MCP.
- Keeps implementation execution outside Tvastr's guaranteed runtime boundary.

### FND-07: Cross-Primitive Contracts And Error Model

Priority: Foundational

Build order: 1

Requirement brief:
Define stable contracts across CLI, MCP, Web API, artifact context, edit events, sync changes, validation results, agent context, trace mappings, versions, approvals, and errors.

Acceptance criteria:

- Covers contracts C1-C12 from the foundation document.
- Defines format/API versioning expectations where appropriate.
- Defines edit event and sync change payloads with actor, base version, source primitive, change summary, and affected entities.
- Defines structured error categories for auth/permission, missing file, invalid source, generation failure, validation failure, sync conflict, unsupported artifact format, broken trace mapping, and server unavailable.
- Ensures agent-facing contracts are structured, not prose-only.
- Ensures error contracts are clear enough for humans and agents to decide the next step.

## P0 PRDs

P0 is not flat. `P0-01` and `P0-02` are the make-or-break product proof. The remaining P0 PRDs support that proof by making it accessible, persistent, shareable, validatable, and handoff-ready.

### P0-01: Make-Or-Break Generation Engine

Priority: P0 Make-Or-Break

Build order: 2

Requirement brief:
Build the generation engine that turns source product intent into a coherent Tvastr mockup/spec artifact. This is the first product proof. The engine must generate a usable flow, not a set of disconnected pretty screens, and must preserve the product context that makes the artifact useful to humans and agents.

Acceptance criteria:

- Accepts explicit source content and metadata from local tools.
- Produces a coherent product flow with screens, states, components, and transitions.
- Represents common flow complexity such as modals, popups, OTP, 2FA, error states, loading states, empty states, success states, and permission states when implied by source material.
- Produces a self-contained HTML/CSS/SVG/vanilla JS artifact.
- Embeds structured `tvastr-context` with flows, screens, components, requirements, states, annotations, decisions, design tokens, component mappings, trace mappings, generation run metadata, audit log, sync metadata, artifact protocol, open questions, and implementation hints where available.
- Creates Generation Run (E19), Trace Mapping (E20), Agent Context (E16), and Version (E14) data inside the artifact context.
- Records source documents used, timestamp, requesting actor, generation parameters where appropriate, warnings, assumptions, and rationale summary.
- Does not store hidden chain-of-thought as product data.
- Treats generated output as a strong editable starting point, not final truth.
- Quality bar: a PM/builder can open the generated artifact and recognize whether the product intent survived.
- Quality bar: a developer or coding agent can inspect the embedded context and understand what should be built.

### P0-02: Make-Or-Break HTML Artifact Editing Capability

Priority: P0 Make-Or-Break

Build order: 2

Requirement brief:
Build the day-0 editing system for the HTML mockup artifact. Editing must support the full conceptual surface immediately: screens, flows, states, components, copy, style, requirements, annotations, decisions, trace mappings, design rationale, component mappings, implementation hints, audit history, and embedded context. The UI can be rough; the capability cannot be partial.

Acceptance criteria:

- Authorized users can edit screens and flows: rename, reorder, duplicate, remove, add, mark optional/deferred, and define transitions.
- Authorized users can edit components: select, edit copy/labels, change visibility, add/remove common components, group or ungroup where supported, reorder within document flow, and attach requirement IDs or annotations.
- Authorized users can edit styles: color, typography, spacing, alignment, size, border, radius, shadow, visibility, and responsive behavior hints.
- Authorized users can add and modify states: default, empty, loading, error, success, disabled, permission denied, mobile, long-content, modal open/closed, OTP, 2FA, validation, account locked, and related flow states.
- Authorized users can edit context: requirement labels, priorities, acceptance criteria, design rationale, annotations, decisions, open questions, component mappings, trace mappings, and implementation hints.
- Edits update materialized HTML/CSS/SVG/JS and embedded `tvastr-context` together.
- Edits preserve stable Component (E7), Screen (E6), State (E9), Requirement (E8), and Trace Mapping (E20) IDs where possible.
- Edits append audit entries for meaningful changes.
- Edits keep current visible/materialized state primary; audit log remains history, not the rendering mechanism.
- Editing works in hosted browser mode.
- Editing works on local `.mockup.html` files in a text editor or agent harness, with validation before sync.
- Editing works without AI and without designers needing Codex, Claude Code, Cursor, Copilot, or BYO API keys.
- Quality bar: a designer/PM can fix a wrong generated flow without regenerating from scratch.
- Quality bar: a local agent can modify raw HTML/context and the artifact can still validate.

### P0-03: Google SSO And Domain Share-Link Access

Priority: P0 Supporting

Build order: 3

Requirement brief:
Implement hosted access through Google SSO and URL sharing. Artifacts must not be Google-indexable. Logged-in access depends on the creator domain.

Acceptance criteria:

- Users can sign in with Google.
- Hosted mockup URLs require login to view.
- If the creator domain is `gmail.com`, any logged-in user with the URL can view and edit.
- If the creator uses an organization domain, only logged-in users from that same domain can view and edit.
- Users outside the allowed domain see a no-permissions wall.
- Workspaces or ownership records are auto-created and hidden from the V1 user flow.
- API tokens or equivalent auth support exists for CLI-hosted operations.

### P0-04: Web Server Canonical Artifact Store

Priority: P0 Supporting

Build order: 3

Requirement brief:
Build the hosted system of record for published mockups. The server stores the canonical HTML Mockup Artifact (P4), its embedded Mockup Spec (E4), versions, permissions, share links, validation state, and indexed operational metadata.

Acceptance criteria:

- Stores the published `.mockup.html` artifact as canonical.
- Stores at least one Version (E14) for every hosted mockup.
- Stores server-side operational metadata for auth, share links, ownership, validation, previews, search, and performance without making it the product source of truth.
- Serves hosted mockup links.
- Exposes raw HTML artifact retrieval to authorized clients.
- Rejects hosted writes that break artifact/context invariants.

### P0-05: CLI Create, Publish, And Local Output

Priority: P0 Supporting

Build order: 3

Requirement brief:
Build the first CLI path so a PM or builder can run a local command against explicit source files, generate a mockup, write a local `.mockup.html`, and optionally publish a hosted link.

Acceptance criteria:

- Supports the common path: `tvastr mockup ./prd.md --design ./design.md --publish`.
- Reads only explicit user-provided paths.
- Does not silently scan the workspace, repository, home folder, or synced drive.
- Shows what it reads and writes.
- Writes a local `.mockup.html` artifact by default unless disabled.
- Publishes a hosted link when requested.
- Prints local path, hosted link, status, and version.
- Provides machine-readable JSON output when requested.
- Handles missing files, unreadable files, auth missing, network failure, generation failure, and invalid artifact errors clearly.

### P0-06: Hosted Mockup Viewer

Priority: P0 Supporting

Build order: 4

Requirement brief:
Serve hosted mockup links so PMs, designers, developers, and stakeholders can view the artifact quickly, inspect screens and flows, switch states, and read structured context without understanding the full data model.

Acceptance criteria:

- Opens a hosted mockup URL after permission checks.
- Renders the canonical HTML artifact.
- Supports screen and flow navigation.
- Supports state switching for represented states.
- Shows annotations, decisions, requirements, and traceability when present.
- Allows authorized users to enter Designer Edit Mode.
- Allows authorized users or tools to extract agent handoff context from the embedded artifact context.

### P0-07: HTML Export And Local-Only Mode

Priority: P0 Supporting

Build order: 4

Requirement brief:
Make the artifact useful without hosted state. Users should be able to receive, open, inspect, and share a `.mockup.html` file directly in Slack, email, or a drive.

Acceptance criteria:

- Exports HTML only for MVP.
- The exported artifact includes embedded agent context JSON.
- The artifact opens in a modern browser without package install, build step, or required network access.
- The artifact remains readable in a text editor.
- The artifact includes source/version references where available.
- The artifact can be shared as a file and still communicate the product flow, screens, states, and context.
- No Markdown, screenshots, Figma packages, image exports, or standalone agent context JSON exports are built for MVP.

### P0-08: Artifact Validation Engine

Priority: P0 Supporting

Build order: 4

Requirement brief:
Build a validator shared by CLI and Web Server. It must verify artifact integrity before publish, export, sync, and hosted acceptance.

Acceptance criteria:

- Validates HTML parse where practical.
- Requires a `tvastr-context` block.
- Validates parseable context JSON.
- Validates known artifact format version.
- Validates unique DOM component IDs.
- Validates that referenced screens, components, states, annotations, decisions, generation runs, and trace mappings point to valid targets.
- Validates sync metadata for published or pulled artifacts.
- Validates no disallowed generated dependencies are present.
- Validates JavaScript syntax where practical.
- Produces structured validation results with info, warning, error, and blocking severities.

### P0-09: Save, Version, Audit, And Rollback Basics

Priority: P0 Supporting

Build order: 5

Requirement brief:
Persist meaningful browser and server changes with versions and audit history. The current materialized state remains primary; audit explains how it changed.

Acceptance criteria:

- Meaningful saves create or update Version (E14).
- Save captures actor, timestamp, affected entities, source primitive, base version, resulting version, and change summary.
- Audit log entries are preserved.
- Version history is visible or inspectable.
- Rollback is supported for server-stored versions at an initial MVP level.
- Approval, export, and agent context reference a specific version.

### P0-10: CLI Pull, Validate, Sync, And Conflict Prevention

Priority: P0 Supporting

Build order: 6

Requirement brief:
Support local artifact editing and sync back to hosted state through CLI. This makes local-only and local-agent editing first-class even before MCP exists.

Acceptance criteria:

- `tvastr pull <mockup-url>` writes a local `.mockup.html` with sync metadata.
- `tvastr validate <artifact-path>` runs the shared artifact validator.
- `tvastr sync <artifact-path>` pushes local changes to hosted state.
- Sync identifies target mockup, base version, and hosted latest version.
- Sync detects conflicts when hosted state changed since local base version.
- Sync avoids destructive overwrite by default.
- Accepted syncs create a new hosted version.
- Sync returns updated hosted link, version ID, validation warnings, or conflict details.

### P0-11: Agent Context Extraction And Developer Handoff

Priority: P0 Supporting

Build order: 6

Requirement brief:
Let developers and coding agents consume structured context from a Tvastr link or artifact instead of inferring intent from screenshots or raw visuals.

Acceptance criteria:

- CLI can extract agent context from a hosted link or local artifact.
- Web Server can provide an agent-readable context response derived from the canonical HTML artifact and embedded context.
- Agent context includes version identity, lifecycle state, flow summary, screens, components, requirements, states, annotations, decisions, design tokens, component mappings, implementation hints, unresolved questions, and trace mappings.
- Agent context is versioned.
- The handoff clearly states that production code implementation is outside Tvastr's guaranteed boundary.
- Developers can give a Tvastr link to a coding agent and get implementation-ready structured context.

### P0-12: Lightweight Approval And Finalization

Priority: P0 Supporting

Build order: 6

Requirement brief:
Support simple approval markers without building a heavy workflow engine. Approval happens within the team; Tvastr records useful metadata on versions.

Acceptance criteria:

- Supports `approved_by_product` and `approved_by_design`.
- Approval applies to a specific version.
- Approval records actor, timestamp, approval type, note, and deferred items where present.
- If a later diff/change invalidates an approved version, approval can be undone or marked stale.
- Approval does not block ordinary edits unless a later PRD explicitly changes that policy.

## P1 PRDs

### P1-01: MCP Server Base

Priority: P1

Build order: 7

Requirement brief:
Build the local MCP server after the CLI path works. It should expose Tvastr workflows inside Codex, Claude Code, Cursor, Copilot, and similar agent harnesses.

Acceptance criteria:

- Exposes tools for create, publish, get mockup, get context, pull artifact, sync artifact, validate artifact, list versions, and approve version.
- Reads local files only through explicit tool calls and allowed roots.
- Respects Tvastr auth, link permissions, and host filesystem permissions.
- Returns structured results with `ok`, IDs, version identity, warnings, errors, and suggested next actions.
- Does not become the canonical store.

### P1-02: Structured MCP Edit Tools

Priority: P1

Build order: 7

Requirement brief:
Add safer structured edit operations for agents so important changes do not require unconstrained raw HTML editing.

Acceptance criteria:

- Provides targeted tools for operations such as add state, rename screen, update trace mapping, update component copy, add annotation, and update decision.
- Updates DOM and embedded context together.
- Appends audit entries for meaningful edits.
- Validates changes before sync.
- Preserves stable IDs and graph invariants.
- Falls back to raw HTML workflow only when structured tools are insufficient.

### P1-03: Editing UX Polish And Usability Hardening

Priority: P1

Build order: 7

Requirement brief:
Improve the ergonomics, speed, resilience, and polish of the day-0 editing system after the full conceptual editing surface exists. This PRD should not move core editing capabilities out of P0; it exists to make editing feel better, faster, and easier to learn.

Acceptance criteria:

- Improves selection, inline editing, property panels, screen/flow navigation, state switching, and traceability panels.
- Improves undo/redo reliability and edit-session recovery.
- Improves component insertion ergonomics without changing the P0 requirement that insertion capability exists from day 0.
- Improves validation guidance so users can repair context issues without feeling punished.
- Improves performance on larger single-flow artifacts.
- Does not defer screens, flows, states, components, style, context, trace mapping, or audit editing from P0.

### P1-04: Collaboration Objects And Review Panels

Priority: P1

Build order: 7

Requirement brief:
Make annotations, decisions, unresolved questions, implementation blockers, and review status first-class browser objects attached to context graph targets.

Acceptance criteria:

- Users can create and resolve annotations.
- Users can record and reopen decisions.
- Users can mark requirements, screens, states, and component mappings as reviewed, missing, covered, deferred, or needing revision.
- Collaboration objects attach to valid graph targets.
- Collaboration changes appear in audit and version history.
- Collaboration data appears in agent context.

### P1-05: Agent-Oriented Diff And Conflict Review

Priority: P1

Build order: 7

Requirement brief:
Improve version comparison and sync conflict review for humans and agents. Diff remains HTML/context/trace/audit first, not screenshot-based.

Acceptance criteria:

- Shows or returns screen/component tree diffs.
- Shows requirement mapping diffs.
- Shows annotation/decision diffs.
- Shows state diffs.
- Shows HTML artifact diffs.
- Shows agent context diffs.
- Explains sync conflicts with local base version, hosted latest version, and affected entities.
- Does not implement screenshot diffs for MVP/P1 unless the decision is reopened.

### P1-06: Optional Web Paste Or Upload Creation

Priority: P1

Build order: 7

Requirement brief:
Add a fallback web creation path for users who want to paste or upload source material, while preserving the foundation rule that users should not have to start in a web upload portal.

Acceptance criteria:

- Users can paste source text into the web app.
- Users can upload explicit files through the browser.
- The web path creates the same Source Document, Generation Run, Trace Mapping, Version, and HTML artifact structures as CLI creation.
- The UI presents this as optional, not the primary wedge.
- Browser upload does not imply arbitrary local file scanning.

### P1-07: Component Mapping And Design Token Refinement

Priority: P1

Build order: 7

Requirement brief:
Improve how generated and edited mockups represent design tokens and component mappings when teams do not have a formal design-system document.

Acceptance criteria:

- Users can view and edit Design Token (E12) values.
- Users can map a Tvastr component to a code or design-system component.
- Component mappings appear in trace mappings and agent context.
- Missing or uncertain mappings can be marked as open questions.
- The feature does not become full design-system management.

### P1-08: Implementation Link Attachment

Priority: P1

Build order: 7

Requirement brief:
Allow users or agents to attach downstream implementation references such as PRs, branches, commits, issues, tickets, or deployed previews without making Tvastr own implementation execution.

Acceptance criteria:

- Users can attach implementation links to a mockup, version, requirement, screen, component, or trace mapping.
- Links appear in agent context and trace mapping where relevant.
- Links do not imply Tvastr controls the code implementation workflow.
- Links can be added manually before external integrations exist.

### P1-09: CLI Polish And Automation Commands

Priority: P1

Build order: 7

Requirement brief:
Expand CLI ergonomics after the core create/publish/pull/sync loop exists.

Acceptance criteria:

- Supports `tvastr status`.
- Supports `tvastr versions`.
- Supports `tvastr context --for <agent|task>`.
- Supports `--json`, `--dry-run`, `--force`, and clear machine-readable errors where appropriate.
- Avoids overwriting local files without confirmation or explicit force.
- Remains scriptable and deterministic.

### P1-10: Direct Agent-Readable Web API

Priority: P1

Build order: 7

Requirement brief:
Expose stable web APIs for authorized tools and agents to retrieve artifact-derived context without going through the browser.

Acceptance criteria:

- Provides versioned endpoints or payload versions before external dependencies form.
- Returns agent context derived from the canonical HTML artifact.
- Returns raw HTML artifact when authorized.
- Includes version identity and lifecycle state.
- Uses structured error contracts.
- Applies permission checks consistently with browser, CLI, and MCP.

## Post MVP PRDs

### PMVP-01: Figma Import, Export, And Mapping

Priority: Post MVP

Build order: 8

Requirement brief:
Add Figma support only after the core product works. Figma is not part of MVP and Tvastr should not become a Figma replacement.

Acceptance criteria:

- Supports optional import or reference of Figma components.
- Supports optional export or handoff package for Figma.
- Supports mapping Tvastr components to Figma components.
- Does not require Figma for Tvastr use.
- Does not attempt to become an infinite-canvas design tool.

### PMVP-02: BYO API Key And AI-Assisted Designer Edits

Priority: Post MVP

Build order: 8

Requirement brief:
Add optional AI-assisted browser editing and BYO API keys in Phase 2. Manual editing must remain first-class.

Acceptance criteria:

- Users can configure a supported API key when the policy allows it.
- AI edits update materialized state and embedded context together.
- AI edits append audit entries and expose assumptions or warnings.
- Designers can still use manual edit mode without AI.
- The feature does not require designers to buy or know Codex, Claude Code, Cursor, or Copilot.

### PMVP-03: Public Marketing And Education Site

Priority: Post MVP

Build order: 8

Requirement brief:
Create the public surface that explains the category, why Tvastr exists, why now, and why visual mockups alone are insufficient for AI coding agents.

Acceptance criteria:

- Public pages do not require login.
- Pages are separate from private mockup/workspace authorization.
- Explains AI-native mockup/spec artifacts.
- Explains why PRD/design/code handoff loses intent.
- Explains how PMs, designers, developers, and agents participate.
- Shows what a Tvastr mockup/spec looks like in practice.

### PMVP-04: Pricing, Billing, And Visible Workspace Management

Priority: Post MVP

Build order: 8

Requirement brief:
Define pricing, limits, billing, and visible workspace management after usage shape is known. V1 should avoid interrupting first use with workspace setup.

Acceptance criteria:

- Defines pricing tiers and limits.
- Defines billing ownership.
- Defines when workspace management becomes visible.
- Preserves default auto-created workspaces for low-friction first use.
- Does not force pricing assumptions into MVP architecture prematurely.

### PMVP-05: Data Retention, Deletion, And Enterprise Privacy

Priority: Post MVP

Build order: 8

Requirement brief:
Add retention, deletion, and privacy controls before broad external or enterprise launch. The current MVP decision is to store server data forever for now.

Acceptance criteria:

- Defines deletion behavior for mockups, artifacts, versions, audit logs, and source metadata.
- Defines retention periods or forever-retain exceptions.
- Defines admin controls where needed.
- Defines export-before-delete or recovery behavior if supported.
- Defines privacy expectations for source excerpts, generation metadata, and embedded context.

### PMVP-06: Additional Export Formats

Priority: Post MVP

Build order: 8

Requirement brief:
Add non-HTML exports only after HTML-only export proves useful.

Acceptance criteria:

- Evaluates Markdown, image snapshots, screenshots, Figma packages, and standalone agent context JSON as separate decisions.
- Every export references source mockup ID and Version (E14).
- Exports are reproducible where possible.
- HTML remains the canonical portable format unless the foundation decision is reopened.

### PMVP-07: External Tool Integrations

Priority: Post MVP

Build order: 8

Requirement brief:
Integrate with external systems after the core mockup/spec layer is stable.

Acceptance criteria:

- Candidate integrations include GitHub/GitLab, Linear/Jira, Notion/Google Docs, Slack/email, model providers, and other document tools.
- Integrations preserve Tvastr as the mockup/spec context layer.
- Integrations do not make Tvastr a replacement for project management, source documents, code repos, or file sync.
- Integrations respect the same auth and permission model as core access.

### PMVP-08: Advanced Permissions And Sharing

Priority: Post MVP

Build order: 8

Requirement brief:
Move beyond MVP domain-based access when the product needs invited members, expiring links, role/capability controls, or enterprise permission models.

Acceptance criteria:

- Supports capability-based permissions such as view, comment, edit, sync, publish, approve/finalize, export, read agent context, and manage permissions.
- Supports invited users or groups if required.
- Supports temporary or expiring links if required.
- Preserves the MVP simplicity until permission complexity is justified.

### PMVP-09: Screenshot Or Visual Diff Exploration

Priority: Post MVP

Build order: 8

Requirement brief:
Explore screenshot or visual diff only if the decision is reopened. The foundation currently says no screenshot diffs for MVP and diff is primarily for agents.

Acceptance criteria:

- Starts with a decision review before implementation.
- Does not replace HTML/context/trace/audit diffs.
- Does not make screenshots the source of truth.
- Defines how visual diff output helps humans without weakening agent-readable context.

### PMVP-10: Rich Design-System Management

Priority: Post MVP

Build order: 8

Requirement brief:
Consider richer design-system management only after initial tokens and component mappings are useful. Tvastr should not become a full design-system suite.

Acceptance criteria:

- Supports richer token and component conventions if needed.
- Keeps mapping to design/code systems explicit.
- Does not expand into full professional design canvas or design-system replacement.
- Preserves artifact portability and agent readability.
