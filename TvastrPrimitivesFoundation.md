# Tvastr Primitives Foundation

## 1. Core Thesis

Tvastr is an AI-native mockup/spec system for turning product intent into implementation-ready structured context.

The product is not a general design canvas and should not try to become "AI Figma." Tvastr's core job is to preserve the product thinking that usually leaks between PRDs, mockups, design comments, engineering handoff, and AI-assisted implementation.

The central artifact is the **Mockup Spec (E4)**: a visual mockup that also carries structured product context. Humans can inspect and edit it visually. AI coding agents can read it as structured data.

Tvastr follows this operating model:

```text
Created locally.
Reviewed visually.
Edited by humans.
Consumed by agents.
```

The PM or builder should be able to start from files and tools they already use. The native creation path is not "upload everything into a new portal." Instead, a local runner such as the **CLI (P1)** or **MCP Server (P2)** reads local source documents with user intent, sends the relevant content to the **Web Server (P3)**, and receives a generated **HTML Mockup Artifact (P4)** and/or hosted mockup link.

The designer should be able to open the link and refine the mockup in **Designer Edit Mode (P5)** without needing Codex, Claude Code, Cursor, Copilot, or a separate AI subscription. Manual editing must remain first-class. At the same time, designers who do use an agent harness should be able to access the raw **HTML Mockup Artifact (P4)** locally through the same **MCP Server (P2)** path available to PMs and builders, make changes with their preferred agent, and push those changes back so the server artifact is updated.

PMs and builders should also be able to use the same HTML-level edit affordances available to designers. Tvastr should not treat visual editing as a designer-only capability. Anyone with permission to edit the mockup should be able to change copy, layout, fields, states, annotations, and structured context through the appropriate surface: browser edit mode, local HTML editing, CLI, MCP, or agent-assisted workflows.

The developer should be able to give the mockup link to a coding agent. The agent should consume structured context from Tvastr rather than infer everything from screenshots or static HTML. That context includes requirements, screens, flows, components, annotations, decisions, states, design rationale, acceptance criteria, implementation hints, and component mappings.

The product primitive stack exists to make one claim true:

> A Tvastr mockup is not merely a picture of a product. It is a living, structured agreement about what should be built.

### Core Commitments

- Tvastr meets users where they already work.
- Local files are read by explicitly invoked local tools, not silently by the browser.
- The hosted product stores and serves mockup specs, versions, share links, edits, annotations, exports, and agent-readable context.
- The HTML export remains portable and useful even when the hosted service is not present.
- Human review and manual editing are product-critical, not fallback behavior.
- AI generation is only one part of the system; traceability, context preservation, and agent handoff are the durable value.

## 2. Domain Boundary

Tvastr's domain is the creation, preservation, editing, publication, and agent consumption of structured mockup specs.

Tvastr is not the permanent home of every source document, design file, codebase, or conversation. It is the layer that turns those inputs into a shared product artifact and keeps the artifact usable across PM, design, development, and AI-agent workflows.

### In-Scope Ownership

Tvastr owns the following capabilities and objects:

| ID | Boundary Area | Tvastr Owns |
| --- | --- | --- |
| B1 | Source ingestion | Accepting source content from explicitly invoked local tools, web uploads, pasted text, or integrations |
| B2 | Mockup generation | Producing initial screens, flows, states, requirements mapping, and structured context |
| B3 | Mockup spec persistence | Storing the canonical hosted **HTML Mockup Artifact (P4)**, including embedded **Mockup Spec (E4)** context, versions, edits, annotations, and share state |
| B4 | Portable artifact export | Producing an **HTML Mockup Artifact (P4)** that remains human-readable and agent-readable outside the hosted app |
| B5 | Human edit surface | Supporting visual/manual edits through **Designer Edit Mode (P5)** for any authorized user |
| B6 | Agent edit surface | Supporting local and remote agent workflows through **CLI (P1)**, **MCP Server (P2)**, and agent-readable APIs |
| B7 | Context graph | Maintaining relationships between requirements, screens, flows, components, annotations, decisions, versions, and implementation hints |
| B8 | Handoff context | Exposing structured context that coding agents can use to implement the mockup in a codebase |
| B9 | Collaboration metadata | Tracking comments, decisions, approvals, feasibility notes, design notes, and unresolved questions |

### Out-Of-Scope Ownership

Tvastr does not own these systems as primary sources of truth:

| ID | External System | Boundary |
| --- | --- | --- |
| X1 | PRD/document authoring | PRDs may live in local files, Notion, Google Docs, Linear, Jira, GitHub, or another tool |
| X2 | Full design canvas | Figma or other design tools may remain the visual design source when teams prefer them |
| X3 | Code implementation | The application repo remains the source of truth for production code |
| X4 | Project management | Linear, Jira, GitHub Issues, or equivalent systems may remain task-management sources |
| X5 | AI coding harness | Codex, Claude Code, Cursor, Copilot, or another agent remains the coding execution environment |
| X6 | General file sync | Tvastr is not Dropbox, Google Drive, or a generic file collaboration system |

Tvastr may integrate with these systems, import from them, export to them, or link back to them, but it should not require teams to abandon them.

### Local Boundary

The browser-based Tvastr app does not read arbitrary local files directly.

Local file access belongs to user-invoked local tools:

- **CLI (P1)**
- **MCP Server (P2)**
- editor extension
- agent harness integration

Those tools may read local PRDs, design notes, screenshots, exported specs, or raw HTML artifacts when the user explicitly asks them to do so. The local tool then sends selected content or artifact updates to the **Web Server (P3)**.

This boundary matters because it keeps the product aligned with user expectations:

```text
User asks local tool -> local tool reads files -> Tvastr receives intentional content
```

Not:

```text
User opens website -> website silently scans local workspace
```

### Hosted Boundary

The hosted **Web Server (P3)** stores and serves the canonical **HTML Mockup Artifact (P4)** for published mockups. The artifact itself is the canonical representation, including its embedded **Mockup Spec (E4)** context.

It stores:

- current mockup spec
- version history
- share links
- permissions
- edits
- annotations
- decisions
- exported artifacts
- agent-readable context
- optional generated assets

For published mockups, the hosted artifact is canonical unless the user explicitly works from a local copy. Local edits made through **CLI (P1)**, **MCP Server (P2)**, or an agent harness must be pushed back to the server before collaborators see them on the shared link.

### Artifact Boundary

The **HTML Mockup Artifact (P4)** is both an export and a synchronization format.

It must be useful in three modes:

1. **Hosted mode**: rendered and edited through the Tvastr web app.
2. **Local mode**: opened or edited as a local HTML file.
3. **Agent mode**: parsed, modified, or regenerated by an AI agent through local tools or server APIs.

The artifact should carry enough structured context to remain meaningful outside the hosted product, but the hosted **Mockup Spec (E4)** remains the richer collaboration record when server features are used.

### Role Boundary

Tvastr roles describe typical use, not hard capability walls.

- PMs and builders usually create and validate product intent.
- Designers usually refine visual structure, interaction behavior, and states.
- Developers usually map feasibility and implementation details.
- AI agents usually generate, modify, analyze, or implement from structured context.

However, any authorized user may edit the mockup through the appropriate surface. A PM can use visual edit tools. A designer can use Claude Code through **MCP Server (P2)**. A developer can leave product questions. An AI agent can suggest design or implementation changes.

Permissions should control access. Job titles should not unnecessarily limit the product surface.

## 3. Core Context Graph

The core of Tvastr is a context graph. The graph connects the visual mockup to the product intent, design rationale, implementation constraints, and agent-readable structure behind it.

The context graph exists so that a human or AI agent can answer:

- What is this screen?
- Why does this component exist?
- Which requirement does it satisfy?
- What state or flow does it belong to?
- Who changed it, and why?
- What does a developer or coding agent need to know before implementing it?

### Entity Catalog

| ID | Entity | Definition |
| --- | --- | --- |
| E1 | Workspace | A billing, permission, and collaboration boundary for one team or organization |
| E2 | Project | A product area or feature initiative that groups related mockup specs, source documents, and implementation links |
| E3 | Source Document | A PRD, design note, screenshot, exported document, pasted text, or linked source used to generate or revise a mockup |
| E4 | Mockup Spec | The structured mockup context embedded inside the canonical **HTML Mockup Artifact (P4)**, containing visual layout references, context graph, versions, annotations, and export state |
| E5 | Flow | A user journey or task path represented by ordered screens and transitions |
| E6 | Screen | A single UI state or page within a mockup spec |
| E7 | Component | A meaningful UI element or component instance inside a screen |
| E8 | Requirement | A product requirement, user need, acceptance criterion, or constraint derived from source material or human input |
| E9 | State | A variant of a screen, flow, or component such as empty, loading, error, success, disabled, mobile, or permission-limited |
| E10 | Annotation | A human or AI note attached to a mockup, screen, component, requirement, state, or version |
| E11 | Decision | A resolved product, design, or technical choice that explains why the mockup is the way it is |
| E12 | Design Token | A named styling value or semantic visual rule used by screens and components |
| E13 | Component Mapping | A mapping from a Tvastr component to a design-system component, code component, or implementation pattern |
| E14 | Version | A snapshot of a mockup spec at a point in time |
| E15 | Export | A generated artifact derived from a mockup spec; for MVP, this is the HTML artifact only, with agent context embedded inside it |
| E16 | Agent Context | A structured representation of the mockup prepared for consumption by Codex, Claude Code, Cursor, Copilot, or another agent |
| E17 | Implementation Link | A link from the mockup spec to a code branch, commit, PR, issue, Linear ticket, or deployed preview |
| E18 | Actor | A PM, builder, designer, developer, stakeholder, or AI agent interacting with the mockup spec |
| E19 | Generation Run | A record of an AI generation or regeneration event, including source inputs, model/provider metadata, assumptions, warnings, and rationale summary |
| E20 | Trace Mapping | A coverage map connecting what the PRD requested, what the design spec required, what Tvastr generated/built in the mockup, and what implementation later delivered |

### Primary Relationships

```text
Workspace (E1)
  contains Projects (E2)

Project (E2)
  contains Source Documents (E3)
  contains Mockup Specs (E4)
  links to Implementation Links (E17)

Mockup Spec (E4)
  is generated from Source Documents (E3)
  has Generation Runs (E19)
  contains Flows (E5)
  contains Screens (E6)
  contains Requirements (E8)
  contains Annotations (E10)
  contains Decisions (E11)
  contains Trace Mappings (E20)
  contains Versions (E14)
  produces Exports (E15)
  produces Agent Context (E16)

Flow (E5)
  orders Screens (E6)
  references Requirements (E8)

Screen (E6)
  contains Components (E7)
  has States (E9)
  references Requirements (E8)

Component (E7)
  satisfies Requirements (E8)
  has States (E9)
  uses Design Tokens (E12)
  may have Component Mappings (E13)
  may have Annotations (E10)
  may have Decisions (E11)

Actor (E18)
  creates, edits, annotates, approves, or implements Mockup Specs (E4)

Generation Run (E19)
  reads Source Documents (E3)
  creates or revises Mockup Specs (E4)
  records assumptions, warnings, and rationale summary

Trace Mapping (E20)
  connects Source Documents (E3), Requirements (E8), Screens (E6), Components (E7), States (E9), Decisions (E11), Component Mappings (E13), Versions (E14), and Implementation Links (E17)
```

### Mockup Spec As Aggregate Root

The **Mockup Spec (E4)** is the main aggregate root.

Most domain objects are meaningful because they belong to a mockup spec. A **Screen (E6)**, **Component (E7)**, **Requirement (E8)**, **State (E9)**, **Annotation (E10)**, **Decision (E11)**, and **Version (E14)** should usually be read or written through the mockup spec boundary.

This does not mean every object must be physically stored in one database row or one HTML file. It means that product behavior should preserve the integrity of the mockup spec as a whole.

For example:

- A component should not reference a requirement that does not exist in the same mockup spec or an explicitly linked project source.
- A screen state should remain attached to the screen or flow it modifies.
- A design decision should point to the affected screen, component, requirement, or state.
- An export should record which mockup version it came from.
- Agent context should be generated from a known mockup version.

### Entity Responsibilities

#### Workspace (E1)

The workspace is the top-level collaboration and billing boundary.

It owns:

- users and roles
- billing plan
- workspace-level permissions
- shared integrations
- optional default design or product conventions

The workspace should not be required for local-only experimentation. In V1, workspace behavior should be auto-created and mostly hidden; it can remain an internal ownership record until visible workspace management is actually needed.

#### Project (E2)

The project groups related mockup specs and source material.

Examples:

- Search v2
- Admin settings redesign
- Patient onboarding
- Internal billing dashboard

A project can contain multiple mockup specs when the team explores alternatives or breaks a larger product area into smaller flows.

#### Source Document (E3)

A source document is any input used to generate or revise a mockup.

It may be:

- a local Markdown PRD
- a Notion or Google Docs export
- pasted text
- a screenshot
- a design note
- a Figma reference
- a repo file
- a previous HTML mockup artifact

Tvastr should track source document metadata and excerpts used for generation, but it does not need to become the permanent source of truth for the original document.

#### Mockup Spec (E4)

The mockup spec is the structured context inside the canonical Tvastr artifact.

It contains both:

- the visual representation of the product idea
- the structured context needed to understand and implement it

The mockup spec is what humans review and what agents consume.

#### Flow (E5)

A flow represents the path a user takes through one or more screens.

Flows are important because implementation agents need to understand behavior over time, not just isolated screens.

#### Screen (E6)

A screen is a single rendered UI state, page, route, modal, or meaningful view.

Screens may belong to one or more flows. They contain components and may have variants such as mobile, empty, loading, or error.

#### Component (E7)

A component is a meaningful UI element or group of elements.

Examples:

- search input
- filter chip group
- results table
- empty state panel
- save button
- onboarding stepper

Components are the main bridge between visual design, requirements, and implementation.

#### Requirement (E8)

A requirement captures product intent.

It may come from the original PRD, be inferred by AI, or be added by a human. Requirements should be linked to the screens, states, and components that satisfy them.

#### State (E9)

A state is a named variation of a screen, flow, or component.

Common states:

- default
- empty
- loading
- error
- success
- disabled
- permission denied
- mobile
- long content

States are first-class because missing states are one of the most common handoff failures.

#### Annotation (E10)

An annotation is a comment with structure.

It should include:

- author
- role or actor type
- target entity
- timestamp
- annotation type
- status, if resolvable
- text

Annotations are not throwaway comments. They are part of the handoff context.

#### Decision (E11)

A decision records a resolved choice.

Examples:

- Use table layout instead of cards for scanability.
- Do not include autosuggest in MVP.
- Reuse existing `SearchInput` component.
- Mobile view hides advanced filters by default.

Decisions should be distinct from annotations because decisions represent settled context that future users and agents should treat as authoritative unless reopened.

#### Design Token (E12)

A design token is a reusable styling value or semantic rule.

Examples:

- `color.background.surface`
- `space.3`
- `radius.medium`
- `font.body.md`

Tvastr may generate starter tokens when no design system exists, import tokens from a design system, or map tokens to code/design systems later.

#### Component Mapping (E13)

A component mapping connects a Tvastr component to an external implementation or design-system equivalent.

Examples:

- Tvastr `primary-button` maps to code `Button variant="primary"`.
- Tvastr `results-table` maps to `DataTable`.
- Tvastr `search-input` maps to Figma component `Inputs/Search`.

This is critical for coding agents because it reduces guesswork.

#### Version (E14)

A version is a snapshot of the mockup spec.

Versions support:

- review history
- diffing
- rollback
- export traceability
- implementation traceability

#### Export (E15)

An export is any generated artifact derived from a mockup spec.

Examples:

- `.mockup.html`
- HTML artifact
- image snapshots
- Figma handoff package
- agent context bundle

Every export should know which mockup spec version produced it.

#### Agent Context (E16)

Agent context is the machine-readable representation prepared for coding agents.

It should be structured, compact enough to consume, and explicit about relationships between requirements, screens, components, states, annotations, and implementation hints.

#### Implementation Link (E17)

An implementation link connects the mockup spec to downstream work.

Examples:

- GitHub PR
- branch
- commit
- Linear ticket
- Jira issue
- deployed preview

This closes the loop between mockup and code.

#### Actor (E18)

An actor is anyone or anything that interacts with Tvastr.

Actors include:

- PM
- builder
- designer
- developer
- stakeholder
- AI agent

Actor roles should inform defaults and labels, but permissions decide actual capabilities.

#### Generation Run (E19)

A generation run records an AI generation or regeneration event.

It should include:

- source documents used
- source excerpts or references
- model/provider metadata where appropriate
- prompt/template version
- generation timestamp
- requesting actor
- assumptions
- warnings
- rationale summary
- produced mockup version

Generation runs should store useful explainable reasoning, not hidden model scratchpad or private chain-of-thought. The goal is to explain why the generated mockup looks the way it does and what source material influenced it.

#### Trace Mapping (E20)

A trace mapping records coverage across product intent, design guidance, generated mockup output, and implementation.

It should answer:

```text
What did the PRD request?
What did the design spec require?
What did Tvastr generate or build in the mockup?
What did the final implementation deliver?
```

Trace mappings are must-have handoff data. They should connect requirements to screens, components, states, design decisions, component mappings, versions, and implementation links.

### Graph Invariants

The context graph should preserve these invariants:

- Every **Mockup Spec (E4)** belongs to a **Project (E2)** or a local/unassigned workspace context.
- Every **Screen (E6)** belongs to a **Mockup Spec (E4)**.
- Every **Component (E7)** belongs to a **Screen (E6)**.
- Every **State (E9)** is attached to a flow, screen, or component.
- Every **Annotation (E10)** has a target entity.
- Every **Decision (E11)** has a target entity or mockup-wide scope.
- Every **Export (E15)** references the **Version (E14)** it was generated from.
- Every **Agent Context (E16)** references the **Mockup Spec (E4)** and **Version (E14)** it summarizes.
- Component-to-code mappings should be explicit through **Component Mapping (E13)**, not inferred only from visual similarity.
- Every **Generation Run (E19)** should reference source inputs and the produced or revised **Version (E14)**.
- Every finalized **Trace Mapping (E20)** should reference at least one source requirement/design input and at least one mockup output target.

## 4. Primitive Map

Tvastr has five primary product primitives.

Each primitive is a distinct surface or execution environment, but all of them operate on the same core context graph. The primitives should feel different to users because they appear in different workflows, but they should not create separate meanings for the same underlying concepts.

| ID | Primitive | Primary User | Primary Job |
| --- | --- | --- | --- |
| P1 | CLI | PM, builder, developer, local power user | Create, export, publish, sync, and inspect mockups from the terminal |
| P2 | MCP Server | AI agent harnesses and agent-assisted users | Let Codex, Claude Code, Cursor, Copilot, and similar tools read local files, create mockups, fetch artifacts, edit artifacts, and sync changes |
| P3 | Web Server | All users and integrations | Generate, persist, publish, version, serve, and expose mockup specs and agent context |
| P4 | HTML Mockup Artifact | Humans, agents, local workflows, export workflows | Provide a portable visual and structured representation of a mockup spec |
| P5 | Designer Edit Mode | Designers, PMs, builders, developers with edit permission | Provide browser-based visual/manual editing and annotation of the mockup spec |

### Primitive Relationship Model

```text
Local files / existing docs
  -> CLI (P1) or MCP Server (P2)
  -> Web Server (P3)
  -> Mockup Spec (E4)
  -> HTML Mockup Artifact (P4)
  -> Designer Edit Mode (P5)
  -> Agent Context (E16)
  -> coding agent / implementation workflow
```

The direction is not strictly linear. A user or agent may also start from a hosted mockup, pull the **HTML Mockup Artifact (P4)** locally through **MCP Server (P2)**, edit it, and push changes back to **Web Server (P3)**.

### Primitive Responsibilities

#### CLI (P1)

The CLI is the local command-line surface.

It is responsible for:

- reading local source files when explicitly invoked
- sending source content to **Web Server (P3)** for generation
- writing local **HTML Mockup Artifact (P4)** files
- publishing mockups to hosted links
- pulling hosted artifacts locally
- pushing local artifact changes back to the server
- exporting mockups into supported formats
- inspecting mockup metadata and status

It is not responsible for:

- silently scanning workspaces
- becoming a full visual editor
- replacing the web editor
- directly implementing application code

The CLI should be boring, predictable, and scriptable.

#### MCP Server (P2)

The MCP server is the local agent bridge.

It is responsible for:

- exposing Tvastr operations to agent harnesses
- reading local files only when requested by the agent/user
- creating mockups from local PRDs and design notes
- fetching hosted mockup specs and artifacts
- exposing raw HTML and structured context to agents
- accepting agent-produced edits
- syncing artifact changes back to **Web Server (P3)**
- returning links, statuses, and structured operation results

It is not responsible for:

- deciding product intent without user or source context
- granting broader local filesystem access than the user/harness allows
- replacing the coding agent's own repository analysis

The MCP server makes Tvastr available inside Codex, Claude Code, Cursor, Copilot, and similar tools.

#### Web Server (P3)

The web server is the hosted system of record for published mockups.

It is responsible for:

- receiving source content from trusted clients
- generating mockup specs
- storing **Mockup Spec (E4)** records
- managing versions, permissions, share links, comments, and approvals
- serving the visual mockup experience
- serving **Designer Edit Mode (P5)**
- producing and storing exports
- exposing agent-readable endpoints
- receiving synced edits from CLI, MCP, browser, or integrations

It is not responsible for:

- directly reading arbitrary local files
- replacing the user's PRD, design, project management, or code tools
- forcing every workflow to start from a web upload

The web server coordinates collaboration and persistence.

#### HTML Mockup Artifact (P4)

The HTML mockup artifact is the portable representation.

It is responsible for:

- rendering the mockup visually in a browser
- carrying embedded structured context
- preserving enough information for AI agents to inspect and modify it
- supporting local review and local editing workflows
- acting as an export/sync format between local tools and hosted state

It is not responsible for:

- holding every collaboration feature when disconnected from the server
- replacing hosted version history
- becoming disconnected from the canonical hosted artifact once a mockup is published

The artifact should remain useful even if the user never opens the hosted web app again.

#### Designer Edit Mode (P5)

Designer Edit Mode is the browser-based visual edit surface.

Despite the name, it is not only for designers. Any authorized editor should be able to use it.

It is responsible for:

- selecting and editing screens and components
- changing copy, layout, fields, styling, and visibility
- adding, removing, or reordering components within supported constraints
- adding and editing states
- adding annotations and design rationale
- reviewing requirement/component traceability
- marking review status where permissions allow
- optionally invoking AI edits when configured

It is not responsible for:

- becoming a full professional design canvas
- requiring AI for normal editing
- requiring designers to leave Figma if they prefer Figma for high-fidelity design
- hiding raw HTML or structured context from users who prefer agent/local workflows

Designer Edit Mode should be simple, direct, and forgiving.

### Primitive Inputs And Outputs

| Primitive | Inputs | Outputs |
| --- | --- | --- |
| CLI (P1) | local file paths, mockup IDs, publish flags, export flags, auth token | local HTML files, hosted links, status output, exported artifacts |
| MCP Server (P2) | agent tool calls, local paths, mockup IDs, edit instructions, artifact diffs | tool results, local files, hosted links, synced updates, structured context |
| Web Server (P3) | source content, edit events, artifact syncs, browser requests, API requests | hosted mockups, generated specs, versions, exports, agent context, rendered app |
| HTML Mockup Artifact (P4) | generated mockup spec, embedded context, edits, sync metadata | visual mockup, local editable file, parseable structured context |
| Designer Edit Mode (P5) | hosted mockup spec, user actions, optional AI instructions, permissions | edit events, annotations, state changes, updated mockup spec, new versions |

### Primitive-To-Entity Mapping

| Primitive | Reads | Writes |
| --- | --- | --- |
| CLI (P1) | Source Document (E3), Mockup Spec (E4), Export (E15) | Source Document metadata (E3), Mockup Spec (E4), Export (E15), Version (E14) |
| MCP Server (P2) | Source Document (E3), Mockup Spec (E4), HTML Artifact export (E15), Agent Context (E16), Generation Run (E19), Trace Mapping (E20) | Mockup Spec (E4), Component (E7), Requirement (E8), State (E9), Annotation (E10), Decision (E11), Version (E14), Trace Mapping (E20) |
| Web Server (P3) | canonical hosted HTML artifacts and embedded context entities | canonical hosted HTML artifacts and embedded context entities |
| HTML Mockup Artifact (P4) | Mockup Spec (E4), Screen (E6), Component (E7), Requirement (E8), State (E9), Annotation (E10), Decision (E11), Design Token (E12), Component Mapping (E13), Generation Run (E19), Trace Mapping (E20) | local representation of same; synced writes must go through CLI (P1), MCP Server (P2), or Web Server (P3) |
| Designer Edit Mode (P5) | Mockup Spec (E4), Flow (E5), Screen (E6), Component (E7), Requirement (E8), State (E9), Annotation (E10), Decision (E11), Version (E14), Trace Mapping (E20) | Screen (E6), Component (E7), Requirement (E8), State (E9), Annotation (E10), Decision (E11), Version (E14), Trace Mapping (E20) |

### Primitive Rules

- **P1 CLI** and **P2 MCP Server** are local trust-boundary tools. They may read local files only after explicit user/agent invocation.
- **P3 Web Server** is the canonical host for published HTML artifacts and their embedded collaboration context.
- **P4 HTML Mockup Artifact** is portable and syncable, but not a replacement for hosted collaboration state when a mockup is published.
- **P5 Designer Edit Mode** is permission-based, not role-locked.
- All primitives must preserve the **Mockup Spec (E4)** as the coherent aggregate root.
- Any primitive that changes a mockup should create or update a **Version (E14)** according to the versioning rules.
- Any primitive exposing data to an AI agent should prefer **Agent Context (E16)** over raw visual inference.

## 5. Lifecycle

The lifecycle describes how a **Mockup Spec (E4)** moves from source material to implementation context.

The lifecycle is not a rigid project-management workflow. Teams may skip steps, loop backward, branch versions, or keep a mockup local. The purpose of lifecycle states is to make status, ownership, and safe transitions explicit.

### Lifecycle State Catalog

| ID | State | Meaning |
| --- | --- | --- |
| S1 | Local Draft | Source documents or a local artifact exist, but no hosted artifact has been created |
| S2 | Generation Requested | A user or agent has asked Tvastr to generate or regenerate a mockup |
| S3 | Generated | Tvastr has produced an initial mockup spec and context graph |
| S4 | Published | The mockup has a hosted link and server-stored canonical HTML artifact |
| S5 | Human Review | PMs, designers, developers, or stakeholders are reviewing the mockup |
| S6 | Editing | An authorized user or agent is modifying visual layout, structured context, annotations, or states |
| S7 | Sync Pending | Local or agent-made edits exist and need to be pushed to the hosted mockup |
| S8 | Synced | Local, browser, or agent edits have been accepted into the hosted canonical artifact |
| S9 | Design Reviewed | Visual structure, interaction behavior, and required states have been reviewed |
| S10 | Dev Reviewed | Feasibility, component mapping, implementation hints, and technical questions have been reviewed |
| S11 | Ready For Agent Handoff | The mockup has enough structured context for a coding agent to implement from it |
| S12 | Implementation In Progress | A developer or coding agent is building from the mockup |
| S13 | Implemented | The mockup is linked to implementation output such as a PR, commit, branch, issue, or deployed preview |
| S14 | Needs Revision | New information requires changes to the mockup or its context graph |
| S15 | Archived | The mockup is no longer active but remains available for reference |

### Typical Lifecycle

```text
S1 Local Draft
  -> S2 Generation Requested
  -> S3 Generated
  -> S4 Published
  -> S5 Human Review
  -> S6 Editing
  -> S8 Synced
  -> S9 Design Reviewed
  -> S10 Dev Reviewed
  -> S11 Ready For Agent Handoff
  -> S12 Implementation In Progress
  -> S13 Implemented
```

At almost any review or implementation point, the mockup may move to **Needs Revision (S14)**, then return to generation, editing, sync, or review.

### State Transitions

| From | To | Trigger | Typical Primitive |
| --- | --- | --- | --- |
| S1 | S2 | User asks Tvastr to generate from local files or pasted/uploaded content | CLI (P1), MCP Server (P2), Web Server (P3) |
| S2 | S3 | Tvastr completes generation | Web Server (P3) |
| S3 | S4 | User publishes or generation request included publish flag | CLI (P1), MCP Server (P2), Web Server (P3) |
| S3/S4 | S5 | User opens or shares mockup for review | Web Server (P3), Designer Edit Mode (P5) |
| S5 | S6 | Authorized user starts editing | Designer Edit Mode (P5), MCP Server (P2), CLI (P1) |
| S6 | S7 | Edits are made locally or by an agent but not yet pushed | CLI (P1), MCP Server (P2), HTML Mockup Artifact (P4) |
| S7 | S8 | Local or agent edits are pushed and accepted by hosted state | CLI (P1), MCP Server (P2), Web Server (P3) |
| S6 | S8 | Browser edits are saved directly to hosted state | Designer Edit Mode (P5), Web Server (P3) |
| S8 | S9 | Designer or authorized reviewer marks design reviewed | Designer Edit Mode (P5), Web Server (P3) |
| S8/S9 | S10 | Developer adds feasibility notes, mappings, or review status | Designer Edit Mode (P5), Web Server (P3), MCP Server (P2) |
| S9/S10 | S11 | Required review gates and context completeness checks pass | Web Server (P3), MCP Server (P2) |
| S11 | S12 | Developer or agent begins implementation from Tvastr context | MCP Server (P2), agent-readable API |
| S12 | S13 | Implementation link is attached | Web Server (P3), CLI (P1), MCP Server (P2) |
| S5/S6/S9/S10/S11/S12/S13 | S14 | New requirement, design change, feasibility blocker, or implementation deviation is discovered | any primitive |
| S14 | S2 | Regeneration is requested | CLI (P1), MCP Server (P2), Web Server (P3) |
| S14 | S6 | Manual or agent edit begins | Designer Edit Mode (P5), MCP Server (P2), CLI (P1) |
| any active state | S15 | User archives mockup | Web Server (P3), CLI (P1), MCP Server (P2) |

### Local And Hosted Lifecycle

Tvastr must support both local-first and hosted collaboration paths.

#### Local-first path

```text
User has local PRD/design notes
  -> CLI (P1) or MCP Server (P2) reads them
  -> Web Server (P3) generates Mockup Spec (E4)
  -> local HTML Mockup Artifact (P4) is written
  -> optional hosted link is published
```

In this path, a mockup may exist as a local artifact before or without being published. If the user later publishes it, the hosted **Mockup Spec (E4)** becomes the collaboration record.

#### Hosted path

```text
User opens hosted mockup
  -> edits through Designer Edit Mode (P5)
  -> Web Server (P3) writes changes directly
  -> new Version (E14) is created
```

In this path, edits are immediately written into the hosted canonical artifact.

#### Local agent-edit path

```text
User or designer asks agent to edit mockup
  -> MCP Server (P2) fetches artifact/context
  -> agent modifies raw HTML or structured context
  -> MCP Server (P2) validates and pushes changes
  -> Web Server (P3) creates new Version (E14)
```

In this path, **Sync Pending (S7)** is important because collaborators should not assume local agent edits are visible until they are pushed and accepted.

### Versioning Rules

The lifecycle depends on **Version (E14)** snapshots. The default posture should be verbose: preserve more history rather than less until usage patterns prove what can be safely compressed.

Create a new version when:

- initial generation completes
- a hosted edit session is saved
- local or MCP edits are synced
- a major annotation/decision set is accepted
- design review status changes
- dev review status changes
- agent context is regenerated for handoff
- implementation links or deviations are recorded

Minor transient UI operations do not need to create separate named versions until saved, but draft revisions and audit entries can still be verbose.

Each version should record:

- version ID
- timestamp
- actor
- source primitive
- change summary
- parent version
- affected entities
- export IDs generated from it

### Review Gates

Review gates are optional but useful for teams that want stronger handoff.

#### Design Reviewed (S9)

Design review means:

- key screens are visually coherent
- core interaction flow is represented
- required states are present or explicitly deferred
- design rationale is captured for important decisions
- major components are named and traceable

It does not mean:

- the mockup is pixel-perfect
- Figma has been replaced
- implementation is guaranteed easy

#### Dev Reviewed (S10)

Dev review means:

- feasibility notes have been added where needed
- obvious backend/API dependencies are identified
- reusable code components are mapped where known
- implementation blockers or questions are recorded
- acceptance criteria are sufficiently clear for coding work

It does not mean:

- code has been written
- estimates are final
- every edge case has been solved

#### Ready For Agent Handoff (S11)

Ready for agent handoff means:

- screens and flows are understandable
- requirements are linked to relevant screens/components/states
- important states are defined
- annotations and decisions are available
- component mappings or implementation hints exist where possible
- unresolved questions are either closed or clearly marked

This state is the threshold where Tvastr should be comfortable exposing **Agent Context (E16)** as implementation input.

### Revision Loops

Tvastr should expect loops, not perfect linear progress.

Common revision triggers:

- PM discovers missing requirement
- designer adds or changes a state
- developer flags an implementation constraint
- AI agent reports missing context
- implementation differs from the mockup
- stakeholder requests a product change

When a mockup enters **Needs Revision (S14)**, Tvastr should preserve the previous version and make the reason for revision explicit through an **Annotation (E10)**, **Decision (E11)**, or change summary.

### Lifecycle Invariants

- A published mockup must have a hosted **Mockup Spec (E4)** and at least one **Version (E14)**.
- A local edit is not visible to collaborators until it reaches **Synced (S8)**.
- **Ready For Agent Handoff (S11)** should reference a specific **Version (E14)**.
- **Implemented (S13)** should include at least one **Implementation Link (E17)**.
- **Needs Revision (S14)** should include a reason.
- Archiving a mockup should not destroy its versions, exports, or implementation links by default.

## 6. CLI Primitive

The **CLI (P1)** is the local command-line interface for creating, publishing, pulling, syncing, exporting, and inspecting Tvastr mockups.

It is the simplest way for PMs, builders, and developers to use Tvastr where their PRDs and project files already live.

The CLI should feel like a normal developer/productivity tool:

```bash
npx tvastr mockup ./prd.md --design ./design-notes.md --publish
```

It should not feel like adopting a new workspace before any value is created.

### CLI Jobs

| Job | Description |
| --- | --- |
| Create | Generate a mockup from local source files |
| Publish | Create or update a hosted mockup link |
| Pull | Fetch a hosted mockup or HTML artifact locally |
| Sync | Push local artifact changes back to hosted state |
| Export | Produce the HTML artifact export; other formats are post-MVP |
| Inspect | Show metadata, status, versions, links, and validation results |
| Auth | Authenticate the local user with Tvastr |

### Command Shape

The first version should optimize for the common path:

```bash
npx tvastr mockup ./prd.md --design ./design-notes.md --publish
```

Expected result:

```text
Created:
./feature.mockup.html

Published:
https://tvastr.app/m/abc123
```

The CLI command family should eventually include:

```bash
tvastr login
tvastr mockup ./prd.md --design ./design.md
tvastr mockup ./prd.md --publish
tvastr publish ./feature.mockup.html
tvastr pull https://tvastr.app/m/abc123
tvastr sync ./feature.mockup.html
tvastr export https://tvastr.app/m/abc123 --format html
tvastr context https://tvastr.app/m/abc123 --for codex
tvastr status ./feature.mockup.html
tvastr versions https://tvastr.app/m/abc123
```

The names can change later, but the jobs should remain stable.

### Local File Access

The CLI may read local files only when the user explicitly provides paths or command options.

Allowed:

```bash
tvastr mockup ./prd.md --design ./design.md
```

Not allowed:

```text
CLI scans the entire repo or home folder without explicit request.
```

The CLI may support explicit globbing if the user provides it:

```bash
tvastr mockup "docs/prd/*.md" --design ./design-system.md
```

In that case, the CLI should show what it will read before sending content if the set is large or potentially surprising.

### Create Flow

When creating a mockup, the CLI should:

1. Resolve user-provided file paths.
2. Validate that files exist and are readable.
3. Classify source files as **Source Document (E3)** inputs.
4. Read the files locally.
5. Package source content and metadata.
6. Send the request to **Web Server (P3)**.
7. Receive a generated **Mockup Spec (E4)** and export payload.
8. Write a local **HTML Mockup Artifact (P4)** unless disabled.
9. Publish a hosted link if requested.
10. Print concise output with local path, hosted link, and status.

The CLI should preserve a local record that links the artifact to the hosted mockup when published. This sync metadata may be embedded in the HTML artifact, written to a sidecar file, or both.

### Publish Flow

Publishing turns a local artifact or generated result into a hosted collaboration record.

```bash
tvastr publish ./feature.mockup.html
```

Publishing should:

1. Parse the local **HTML Mockup Artifact (P4)**.
2. Validate embedded structured context.
3. Create or update a hosted **Mockup Spec (E4)**.
4. Create a **Version (E14)**.
5. Return a shareable link.
6. Store sync metadata locally.

Publishing should not require the user to manually copy/paste content into the web app.

### Pull Flow

Pulling brings hosted mockup state local.

```bash
tvastr pull https://tvastr.app/m/abc123
```

Pulling should:

1. Authenticate or validate access to the mockup.
2. Fetch the requested **Mockup Spec (E4)** or **Export (E15)**.
3. Write a local **HTML Mockup Artifact (P4)**.
4. Include sync metadata so later `sync` knows the source mockup and version.
5. Avoid overwriting local files without confirmation or an explicit force flag.

This supports designers, PMs, or developers who want to edit the artifact locally with an editor or agent harness.

### Sync Flow

Syncing pushes local artifact changes back to the server.

```bash
tvastr sync ./feature.mockup.html
```

Syncing should:

1. Parse local artifact sync metadata.
2. Identify the target hosted **Mockup Spec (E4)** and base **Version (E14)**.
3. Validate local structured context and HTML integrity.
4. Compute or submit a change set.
5. Detect conflicts if the hosted mockup changed since the local base version.
6. Create a new hosted **Version (E14)** if accepted.
7. Return the updated hosted link and version ID.

If conflicts exist, the CLI should explain them clearly and avoid destructive overwrite by default.

### Export Flow

For MVP, the CLI exports mockups as the portable HTML artifact. Other downstream formats are post-MVP.

For MVP:

```bash
tvastr export https://tvastr.app/m/abc123 --format html
```

The HTML export includes embedded agent context JSON. Exports should reference a specific **Version (E14)** by default. If the user exports latest, the output should still record which version was used.

### Agent Context Extraction Flow

The CLI may expose agent-ready context to a local agent without making agent context a separate export format:

```bash
tvastr context https://tvastr.app/m/abc123 --for codex
```

This should read or fetch the canonical **HTML Mockup Artifact (P4)**, extract its embedded agent context JSON, and return or write a temporary **Agent Context (E16)** view for the requesting agent, including:

- flow summary
- screens
- components
- requirements
- states
- annotations
- decisions
- component mappings
- implementation hints
- open questions
- source version

This command is useful when a coding agent cannot call the Tvastr MCP server directly but can read local files.

For MVP, this is an extraction/view operation over the HTML artifact, not a standalone export format.

### Authentication

The CLI needs authentication for hosted operations:

- publishing
- pulling private mockups
- syncing
- exporting private artifacts
- reading private agent context

Unauthenticated usage may be allowed for local-only generation if product policy supports it, but any server-side persistence should have an actor identity or anonymous-link policy.

The CLI should support:

- `tvastr login`
- browser-based auth flow
- token storage in the user's standard credential store where possible
- explicit logout
- clear workspace/project selection when needed

### Output Principles

CLI output should be:

- concise by default
- scriptable with JSON flags
- explicit about files read and written
- explicit about hosted links created or updated
- explicit about version IDs when relevant
- careful around destructive operations

Examples:

```text
Read:
- ./prd.md
- ./design-notes.md

Created:
- ./search-v2.mockup.html

Published:
- https://tvastr.app/m/abc123

Version:
- v1
```

For automation:

```bash
tvastr mockup ./prd.md --publish --json
```

Should produce machine-readable output.

### Error Handling

The CLI should make common failures understandable.

| Failure | Expected Behavior |
| --- | --- |
| File missing | Show path and command correction hint |
| File unreadable | Explain permission/read issue |
| Unsupported file | Explain accepted formats or fallback |
| Auth missing | Ask user to run `tvastr login` |
| Network failure | Preserve local state and suggest retry |
| Generation failure | Show a stable error ID and avoid losing input |
| Sync conflict | Explain local base version and hosted latest version |
| Invalid artifact | Identify malformed HTML/context region if possible |

The CLI should never silently discard local work.

### CLI Invariants

- The CLI reads local files only when explicitly instructed.
- The CLI should never silently scan a workspace.
- The CLI should not overwrite local files without confirmation or explicit force.
- Hosted writes should create a **Version (E14)**.
- Published artifacts should carry enough sync metadata to support later pull/sync flows.
- CLI-generated exports should record their source **Mockup Spec (E4)** and **Version (E14)** when available.
- CLI behavior should be deterministic enough for scripts and agent harnesses to rely on.

## 7. MCP Server Primitive

The **MCP Server (P2)** is Tvastr's local agent bridge.

Its job is to make Tvastr available inside agent harnesses such as Codex, Claude Code, Cursor, Copilot, and future MCP-compatible tools. It lets a user ask an agent to create, inspect, pull, edit, or sync a mockup without leaving the tool where they are already working.

The MCP server is not the same as the **Web Server (P3)**. It runs locally or in the user's agent environment. It can access local files only through the permissions and roots available to that environment. It talks to **Web Server (P3)** for generation, hosted persistence, publication, and sync.

### MCP Jobs

| Job | Description |
| --- | --- |
| Create mockup | Read user-specified local source files and ask Tvastr to generate a mockup |
| Publish mockup | Publish a generated or local artifact to a hosted link |
| Fetch mockup | Retrieve hosted mockup metadata, structured context, or HTML artifact |
| Pull artifact | Write a hosted **HTML Mockup Artifact (P4)** into the local workspace |
| Edit artifact | Allow an agent to modify raw HTML or structured context locally |
| Sync edits | Push validated local/agent edits back to the hosted canonical artifact |
| Expose context | Provide **Agent Context (E16)** optimized for coding, design, or product review |
| Attach implementation | Link PRs, branches, commits, tickets, or previews to a mockup |
| Inspect status | Return lifecycle state, versions, review status, and open questions |

### MCP Users

The MCP server is used by agents on behalf of humans.

Typical users:

- PM asks Codex or Claude Code to generate a mockup from local PRD files.
- Designer asks Claude Code or another agent to pull the raw HTML, make design changes, and sync them back.
- Developer asks Cursor or Codex to read a Tvastr link and implement from the structured context.
- Agent asks Tvastr for missing context, version metadata, component mappings, or unresolved questions.

### Tool Catalog

The first MCP server should expose a small, stable tool surface.

| Tool | Purpose |
| --- | --- |
| `tvastr_create_mockup` | Create a mockup from local source paths or provided text |
| `tvastr_publish_mockup` | Publish a local artifact or generated mockup to a hosted link |
| `tvastr_get_mockup` | Fetch mockup metadata and lifecycle status |
| `tvastr_get_context` | Fetch **Agent Context (E16)** for a target harness or task |
| `tvastr_pull_artifact` | Fetch hosted mockup HTML and write it locally |
| `tvastr_sync_artifact` | Push local HTML/context changes back to hosted state |
| `tvastr_validate_artifact` | Validate local HTML artifact structure and embedded context |
| `tvastr_list_versions` | List versions for a hosted mockup |
| `tvastr_attach_implementation` | Attach PR, branch, commit, ticket, or deployed preview |

Names can evolve, but the capabilities should remain clear and few. A small tool surface makes the MCP server easier for agents to choose correctly.

### Tool Behavior

#### `tvastr_create_mockup`

Creates a mockup from local files or provided text.

Example tool input:

```json
{
  "prdPaths": ["./prd.md"],
  "designPaths": ["./design-notes.md"],
  "publish": true,
  "writeLocalArtifact": true
}
```

Expected behavior:

1. Resolve paths within allowed local roots.
2. Read only the requested files.
3. Send source content and metadata to **Web Server (P3)**.
4. Receive generated **Mockup Spec (E4)** and optional hosted link.
5. Write local **HTML Mockup Artifact (P4)** if requested.
6. Return structured result with artifact path, hosted link, version ID, and warnings.

#### `tvastr_get_context`

Returns agent-optimized structured context.

Example tool input:

```json
{
  "mockup": "https://tvastr.app/m/abc123",
  "for": "codex",
  "task": "implementation"
}
```

Expected behavior:

1. Authenticate or validate access.
2. Fetch a specific or latest **Version (E14)**.
3. Return **Agent Context (E16)** with requirements, flows, screens, components, states, annotations, decisions, mappings, and implementation hints.
4. Include unresolved questions and known blockers.

This tool should be preferred when an agent is building code. It is more reliable than asking the agent to infer intent from the visual HTML alone.

#### `tvastr_pull_artifact`

Writes a hosted mockup artifact into the local workspace.

Example tool input:

```json
{
  "mockup": "https://tvastr.app/m/abc123",
  "outputPath": "./search-v2.mockup.html"
}
```

Expected behavior:

1. Fetch the requested mockup/version.
2. Write the **HTML Mockup Artifact (P4)** locally.
3. Include sync metadata.
4. Avoid overwriting existing files unless explicitly allowed.

This enables designers and PMs to use agent harnesses for raw HTML editing.

#### `tvastr_sync_artifact`

Pushes local artifact changes back to hosted state.

Example tool input:

```json
{
  "path": "./search-v2.mockup.html",
  "changeSummary": "Adjusted spacing, added empty state, clarified filter copy"
}
```

Expected behavior:

1. Read the local artifact.
2. Validate embedded context.
3. Compare against the base hosted version.
4. Detect conflicts.
5. Submit changes to **Web Server (P3)**.
6. Create a new **Version (E14)** if accepted.
7. Return updated link, version ID, and validation warnings.

### Resource Catalog

The MCP server should expose read-only resources where useful.

Potential resources:

| Resource | Purpose |
| --- | --- |
| `tvastr://mockups/{id}` | Hosted mockup metadata |
| `tvastr://mockups/{id}/context` | Agent context |
| `tvastr://mockups/{id}/html` | HTML artifact content |
| `tvastr://mockups/{id}/versions` | Version list |
| `tvastr://mockups/{id}/requirements` | Requirement summary |
| `tvastr://mockups/{id}/open-questions` | Unresolved questions |

Resources should be used for safe reads. Tools should be used for actions that create, edit, publish, sync, or attach implementation links.

### Prompt Catalog

The MCP server may expose prompts that help agents use Tvastr correctly.

Potential prompts:

| Prompt | Purpose |
| --- | --- |
| `create_mockup_from_prd` | Guide agent to ask for source paths and invoke `tvastr_create_mockup` |
| `review_mockup_for_design` | Guide agent to inspect states, hierarchy, design rationale, and missing UI cases |
| `prepare_for_implementation` | Guide agent to check requirements, mappings, states, and unresolved questions |
| `implement_from_mockup` | Guide coding agent to fetch context, inspect repo, plan, implement, and report coverage |
| `sync_html_edits` | Guide agent through pull/edit/validate/sync flow |

Prompts should not hide the underlying tools. They should make common workflows smoother.

### Local File Boundary

The MCP server must follow the same local file principle as the CLI:

> It reads local files only when the user or agent explicitly asks it to read specific paths.

The MCP server may be more powerful than the CLI because it operates inside an agent harness, but it must not become vague about file access.

Allowed:

```json
{
  "prdPaths": ["./prd.md"],
  "designPaths": ["./design.md"]
}
```

Not allowed:

```text
MCP server silently scans the repo for all product docs without user request.
```

If an agent proposes broad file access, the MCP server should either reject it or require explicit confirmation depending on the host environment's capabilities.

### Raw HTML Editing Boundary

The MCP server should support raw HTML workflows because designers, PMs, and agents may want to edit the **HTML Mockup Artifact (P4)** directly.

Supported flow:

```text
pull hosted mockup -> write local HTML -> agent edits file -> validate -> sync to server
```

The MCP server should not treat raw HTML edits as second-class. They are part of the product thesis: the artifact is both human-editable and agent-editable.

However, syncing raw HTML must validate:

- required structured context exists
- component IDs remain stable where possible
- embedded context is parseable
- sync metadata is present
- base version is known
- changes do not break graph invariants

### Authentication And Permissions

The MCP server performs actions on behalf of a user.

It must respect:

- Tvastr auth
- workspace/project permissions
- mockup link permissions
- local agent host permissions
- allowed filesystem roots

The MCP server should not give an agent more authority than the user has.

Permission-sensitive operations:

- publishing mockups
- pulling private mockups
- syncing changes
- reading private agent context
- attaching implementation links
- changing review state

### Conflict Handling

Conflicts can happen when an agent edits a local artifact while collaborators edit the hosted mockup.

The MCP server should detect:

- local base version differs from hosted latest version
- same component changed in both places
- structured context changed incompatibly
- target entity no longer exists
- local artifact lacks sync metadata

Default behavior should be conservative:

- do not overwrite hosted changes silently
- return conflict details to the agent
- let the agent explain options to the user
- support explicit force/merge only when intentionally requested and permitted

### Agent Result Shape

Tool results should be structured and agent-friendly.

Example result:

```json
{
  "ok": true,
  "mockupId": "mock_abc123",
  "url": "https://tvastr.app/m/abc123",
  "localArtifactPath": "./search-v2.mockup.html",
  "version": "v3",
  "state": "Synced",
  "warnings": []
}
```

Errors should also be structured:

```json
{
  "ok": false,
  "errorCode": "SYNC_CONFLICT",
  "message": "The hosted mockup changed since this artifact was pulled.",
  "localBaseVersion": "v2",
  "hostedLatestVersion": "v4",
  "conflicts": ["component:filters-panel", "state:empty-results"]
}
```

This helps agents decide whether to continue, ask the user, or fetch newer context.

### MCP Invariants

- The MCP server is an agent bridge, not the canonical store.
- The MCP server reads local files only through explicit tool calls and allowed roots.
- The MCP server should prefer **Agent Context (E16)** for implementation tasks.
- The MCP server should expose raw **HTML Mockup Artifact (P4)** for local edit workflows.
- Sync operations must preserve **Mockup Spec (E4)** graph invariants.
- Hosted writes through MCP should create a **Version (E14)**.
- Tool results must be structured enough for agents to reason about success, failure, warnings, conflicts, versions, and next steps.
- The MCP server must not grant agents broader permissions than the user or host environment allows.

## 8. Web Server Primitive

The **Web Server (P3)** is the hosted system of record for published Tvastr mockups.

It coordinates generation, persistence, sharing, permissions, collaboration, versions, exports, and agent-readable context. It is the place where the **Mockup Spec (E4)** becomes a durable collaboration object rather than only a local file.

The web server should not force users to start in the web app. Its job is to receive intentional input from local tools, web forms, integrations, or browser edits, and store/serve the canonical HTML artifact once a mockup is published.

### Web Server Jobs

| Job | Description |
| --- | --- |
| Generate | Convert source content into a structured **Mockup Spec (E4)** |
| Persist | Store canonical HTML artifacts, embedded context, versions, annotations, and decisions |
| Publish | Create shareable hosted links and optional public/private access modes |
| Serve | Render the mockup and edit experience in the browser |
| Collaborate | Support comments, annotations, decisions, review gates, and permissions |
| Version | Snapshot meaningful changes and support history, diffing, and rollback |
| Sync | Accept validated changes from CLI, MCP, browser, and integrations |
| Export | Produce HTML artifacts; other export formats are post-MVP |
| Expose context | Serve structured **Agent Context (E16)** to coding agents and local tools |
| Integrate later | Link to external systems such as GitHub, Linear, Jira, Figma, or docs tools after the core product is stable |
| Market and educate later | Serve public pages that explain why this product category exists, why Tvastr, and why now; not MVP |

### Hosted Canonical State

For published mockups, the web server owns the canonical **HTML Mockup Artifact (P4)**. The **Mockup Spec (E4)** lives inside that artifact as embedded structured context.

The canonical artifact includes product/mockup truth:

- mockup metadata
- source document metadata and excerpts
- flows
- screens
- components
- requirements
- states
- annotations
- decisions
- design tokens
- component mappings
- versions
- exports
- generation runs
- trace mappings
- implementation links
- agent context snapshots

The web server should store the HTML artifact as the canonical representation, warts and all. It may maintain server-side operational metadata for authentication, share links, ownership, permissions, validation, previews, search, and performance, but product/mockup truth should remain inside the artifact.

### Input Channels

The web server receives input from several channels.

| Channel | Example | Notes |
| --- | --- | --- |
| CLI (P1) | `tvastr mockup ./prd.md --publish` | Local files are read by CLI, not by server |
| MCP Server (P2) | `tvastr_create_mockup` tool call | Agent invokes local bridge, server receives intentional content |
| Browser UI | Paste PRD, upload file, manual edit | Web upload/paste is supported but not the primary wedge |
| Designer Edit Mode (P5) | User changes copy/layout/state | Browser edits write directly to hosted state |
| Artifact sync | Local HTML changes pushed back | Server validates and versions changes |
| Integrations | GitHub, Figma, Linear, docs tools | Optional; should not be required for core use |

### Generation Service

Generation is the process of creating or revising a **Mockup Spec (E4)** from source context.

Generation should produce:

- flows
- screens
- components
- requirements
- states
- annotations or assumptions where appropriate
- initial design tokens
- rationale or decision candidates
- agent-readable structure
- an initial **HTML Mockup Artifact (P4)**
- a **Generation Run (E19)** record
- initial **Trace Mapping (E20)** entries

Generation should not be treated as final truth. It creates a starting point for human and agent refinement.

When generation completes, the server should create a **Version (E14)** and **Generation Run (E19)**, then record:

- source documents used
- generation parameters
- model/provider metadata where appropriate
- prompt/template version where appropriate
- timestamp
- requesting actor
- warnings or assumptions
- rationale summary

### Persistence Model

The web server should persist the HTML artifact and enough indexed metadata to support collaboration and agent handoff.

At minimum, it should persist:

- **HTML Mockup Artifact (P4)** as the canonical representation
- embedded **Mockup Spec (E4)** context
- **Version (E14)** snapshots
- edit events or change summaries
- artifact content
- selected indexed context graph entities
- generation runs and trace mappings
- permissions and share state

Implementation may still use indexes, tables, or sidecar metadata for performance and access control. The foundation requirement is that the HTML artifact remains the canonical representation.

### Share Links

Share links are the primary way humans enter the hosted experience.

Example:

```text
https://tvastr.app/m/abc123
```

Share links should support modes such as:

- private authenticated access
- logged-in URL access for `gmail.com` creators
- same-domain URL access for organization creators
- no-permissions wall for users outside the creator's organization domain
- future invited-editor or expiring-link modes if the access model expands

The MVP access model is defined in **O1**. Future capability-based authorization may separate:

- view permission
- comment/annotation permission
- edit permission
- publish/sync permission
- admin/manage permission

### Browser Rendering

The web server serves the human-facing mockup experience.

The browser view should support:

- viewing screens and flows
- inspecting requirements and context
- switching states
- reading annotations and decisions
- entering **Designer Edit Mode (P5)** if authorized
- extracting or copying agent handoff context from the artifact if authorized

The default shared-link experience should show the mockup quickly. Users should not have to understand Tvastr's full data model to review a screen.

### Edit Acceptance

The web server receives edits from:

- browser edit mode
- CLI sync
- MCP sync
- future integrations

Every edit should be normalized into changes against the **Mockup Spec (E4)** context graph.

Edit acceptance should:

1. Authenticate actor or validate link permission.
2. Validate target mockup and base version.
3. Validate changed entities.
4. Preserve graph invariants.
5. Detect conflicts where needed.
6. Create or update **Version (E14)** of the artifact.
7. Return updated state, warnings, or conflicts.

The server should not accept changes that produce broken references, orphaned components, invalid embedded context, or unknown base versions without explicit recovery behavior.

### Versioning And Diffing

The web server owns version history for published mockups.

Versions should support:

- change history
- review of who changed what
- rollback
- structured diff where possible
- export traceability
- agent context traceability

Useful diff types:

- screen/component tree diff
- requirement mapping diff
- annotation/decision diff
- state diff
- HTML artifact diff
- agent context diff

For MVP, diffs are primarily for agents and should focus on HTML/context/trace/audit changes. Screenshot diffs are not part of MVP.

### Agent-Readable Endpoints

The web server should expose agent-readable context through APIs used by **CLI (P1)**, **MCP Server (P2)**, and possibly direct agent integrations.

The endpoint may return **Agent Context (E16)** for agent ergonomics, but that response should be derived from the canonical hosted **HTML Mockup Artifact (P4)** and its embedded context. It is not a second canonical store and not a separate MVP export format.

Agent context should include:

- mockup identity
- version identity
- lifecycle state
- flow summary
- screens
- components
- requirements
- states
- annotations
- decisions
- design tokens
- component mappings
- implementation hints
- unresolved questions
- trace mappings
- implementation links, if present

The web server may also serve raw **HTML Mockup Artifact (P4)**, but implementation agents should be guided toward structured context first.

### Export Service

The web server should produce **Export (E15)** artifacts.

MVP export format:

- HTML mockup

The HTML mockup includes embedded agent context JSON. Markdown, screenshots/images, and Figma-oriented packages are post-MVP unless this decision is reopened.

Every export should reference:

- mockup ID
- version ID
- export type
- timestamp
- actor
- generation options

Exports should be reproducible where possible.

### Authentication And Authorization

The web server controls hosted access through Google SSO and URL-based sharing.

It should support:

- Google-authenticated user accounts
- auto-created default ownership/workspace records, mostly hidden in V1
- link-based access
- creator-domain access rules
- API tokens for CLI/MCP
- audit trail for meaningful changes

MVP access policy:

- Artifacts should not be Google-indexable.
- A URL is shareable.
- A user must be logged in to view.
- If the creator's domain is `gmail.com`, any logged-in user with the URL can view and edit.
- If the creator's domain is an organization domain, only users from the same domain can view and edit.
- Users outside the allowed domain see a no-permissions wall.

Future authorization may become more capability-based, but MVP should avoid permission-management complexity unless required.

### Marketing And Education Surface

The web server may later own Tvastr's public marketing and education surface. This is not part of MVP.

This matters because Tvastr is creating a new product category, not merely offering another design editor. The public website and unauthenticated product pages should explain:

- why AI-generated mockups need structured product context
- why existing PRD/design/code handoff loses intent
- why visual mockups alone are insufficient for AI coding agents
- why Tvastr is different from design canvases, prototyping tools, and app builders
- why now: coding agents, local agent harnesses, MCP, and AI-assisted development are changing handoff requirements
- how PMs, designers, developers, and agents each participate
- what a Tvastr mockup/spec looks like in practice

These pages may eventually live on the same web server as the application, but they are a different surface from authenticated collaboration. Marketing pages should not require login, while workspace/mockup operations should still respect authorization.

The marketing surface should make the product legible before a user ever runs the CLI, installs the MCP server, or opens a hosted mockup link.

### Collaboration Objects

The web server should treat collaboration metadata as first-class data.

Important objects:

- **Annotation (E10)**
- **Decision (E11)**
- review status
- unresolved question
- implementation blocker
- approval marker
- change summary

These objects should be attached to targets in the context graph, not stored as disconnected comments.

### Integration Boundary

The web server may integrate with external systems, but integrations are not the core primitive.

Useful post-MVP integrations:

- GitHub/GitLab for implementation links
- Linear/Jira for tickets
- Figma for design import/export
- Notion/Google Docs for document import
- Slack/email for sharing
- model providers for generation

Integrations should preserve the central rule:

> Tvastr is the mockup/spec context layer, not the permanent replacement for every external tool.

### Web Server Invariants

- The web server stores the canonical published **HTML Mockup Artifact (P4)**.
- The web server must not directly read arbitrary local files.
- Every hosted mockup should have at least one **Version (E14)**.
- Meaningful hosted edits should be attributable to a Google-authenticated **Actor (E18)**.
- Agent-readable endpoints should include version identity.
- Exports should reference the source **Mockup Spec (E4)** and **Version (E14)**.
- Public marketing pages, when built, should be accessible without requiring workspace membership.
- Permission checks must apply consistently across browser, CLI, MCP, and API access.
- Server-accepted changes must preserve context graph invariants.

## 9. HTML Mockup Artifact

The **HTML Mockup Artifact (P4)** is the portable representation of a Tvastr mockup.

It is a single HTML file that can be opened by humans, parsed by agents, edited locally, synced back to the server, or stored as an export. It is the bridge between local workflows, browser review, and AI-agent modification.

### Artifact Technology Model

The artifact should be a self-contained web document.

It may use:

- HTML
- CSS
- SVG
- JavaScript

JavaScript is allowed and expected for flows, state switching, modal behavior, tabs, popups, OTP screens, 2FA screens, interactive annotations, and local artifact behavior. The restriction is not "no JavaScript." The restriction is:

> No build step, no package install, and no required network dependency for the core artifact.

The generated artifact may include runtime JavaScript if that script is embedded in the file. For MVP, the artifact runtime should use vanilla JavaScript only. No bundled UI libraries, framework helpers, or CSS utility libraries should be included unless this decision is explicitly reopened.

### Artifact Jobs

| Job | Description |
| --- | --- |
| Render | Show the visual mockup in a browser without a build step |
| Preserve | Carry structured context alongside the visual markup |
| Transport | Move mockup state between server, local files, and agents |
| Inspect | Let humans and agents read the artifact directly |
| Edit | Allow local/manual/agent edits to visual markup and embedded context |
| Sync | Provide enough metadata for CLI/MCP to push changes back to hosted state |
| Export | Serve as a durable output format for teams that want a file |

### File Shape

The artifact should be a single `.mockup.html` file.

Recommended high-level structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="generator" content="tvastr">
  <meta name="tvastr-mockup-id" content="mock_abc123">
  <meta name="tvastr-version" content="v3">
  <title>Search v2 Mockup</title>
  <style>
    /* Generated CSS */
  </style>
</head>
<body>
  <main id="tvastr-mockup">
    <!-- HTML + CSS + SVG + JS-driven mockup flow -->
  </main>

  <script type="application/json" id="tvastr-context">
    {}
  </script>

  <script>
    /* Embedded artifact runtime */
  </script>
</body>
</html>
```

The JSON script tag stores structured context as data. Runtime JavaScript should read that context but keep it distinct from the data block.

### Allowed Content

The artifact may contain:

- semantic HTML
- CSS in `<style>` tags
- inline styles when useful
- inline SVG
- executable JavaScript in embedded `<script>` tags
- JSON data inside `<script type="application/json">`
- data attributes linking DOM elements to context graph entities
- metadata tags
- comments used as stable section markers
- embedded audit log and edit protocol data

The artifact should prefer semantic HTML where possible because semantic structure helps both accessibility and agent parsing.

### Disallowed Content

The generated artifact should not contain:

- remote script tags required for core behavior
- unbundled npm/browser framework dependencies
- bundled UI/helper libraries for MVP
- external CSS dependency links required for core behavior
- canvas-only rendering
- required remote images
- base64-encoded bitmap assets as core UI structure
- build-tool output that is unreadable to humans and agents
- minified unreadable markup
- obfuscated class names as the only structural signal

JavaScript is allowed, but it should remain readable, local to the artifact, and organized around the artifact protocol. SVG is allowed because it remains text-based, portable, inspectable, and easy for agents to modify.

If a future workflow requires richer assets, those assets should be represented as optional references or separate exports, not as required content for the core generated mockup artifact.

### Visual Representation

The visual mockup should be represented through:

- HTML structure
- CSS layout
- CSS tokens/variables
- inline SVG for icons, charts, diagrams, and illustrative UI elements
- JavaScript for screen navigation, state switching, dialogs, simulated interactions, annotations, and local artifact behavior

Opening the file in a browser should show a usable mockup without installing anything. JavaScript may control which screen/state is active, but the file should still be understandable if read as text.

The artifact may represent multiple screens or states in one file. Common approaches:

- separate `<section data-screen-id="...">` blocks
- state containers with `data-state-id`
- CSS classes for active/default state
- visible screen index/navigation represented as plain HTML
- JavaScript-controlled flow navigation
- JavaScript-controlled modal/popover visibility

### One Flow, One Artifact

The default rule should be:

> One product flow equals one HTML mockup artifact.

For example, a login flow should normally live in one `.mockup.html` file even if it contains:

- login page
- forgot-password modal
- OTP screen
- 2FA screen
- backup-code screen
- error states
- success state
- account-locked state

Those should be represented as multiple **Screen (E6)** and **State (E9)** entries inside one **Mockup Spec (E4)** and one **HTML Mockup Artifact (P4)**.

This is better for dev handoff because the agent receives the entire flow, its state machine, and its traceability in one artifact. Splitting every page into separate HTML files would make local transport harder and would force agents to reconstruct relationships across files.

Multiple HTML files are allowed only when:

- flows are genuinely separate
- a mockup is too large for one practical artifact
- a team explicitly exports per-screen files
- a downstream tool requires split files

When multiple files exist, there must still be one parent manifest or hosted **Mockup Spec (E4)** that connects them.

### Structured Context

The artifact must carry structured context for agents and sync tools.

The context should include:

- mockup ID
- project/workspace metadata where available
- version ID
- source document metadata
- generation run metadata
- trace mappings
- flows
- screens
- components
- requirements
- states
- annotations
- decisions
- design tokens
- component mappings
- implementation hints
- open questions
- sync metadata
- artifact edit protocol
- audit log

The structured context should be parseable without rendering the page.

The preferred location is:

```html
<script type="application/json" id="tvastr-context">
{
  "mockupId": "mock_abc123",
  "version": "v3",
  "generationRuns": [],
  "traceMappings": [],
  "screens": [],
  "components": [],
  "requirements": [],
  "artifactProtocol": {
    "formatVersion": "1.0",
    "rules": [
      "Preserve stable IDs",
      "Update DOM and context together",
      "Append audit events for meaningful edits",
      "Do not delete source traceability"
    ]
  },
  "auditLog": []
}
</script>
```

Because the script type is `application/json`, the content is data, not executable JavaScript.

### Metadata Layers

The artifact should distinguish the different kinds of metadata.

#### Incoming source metadata

Incoming PRD and design-spec information belongs to **Source Document (E3)** records on the server. The artifact should carry source references, filenames, hashes, excerpts, and requirement/design IDs where useful. It should not be required to embed full source documents by default because PRDs and design specs may be large or sensitive.

#### Generation metadata

AI generation metadata belongs to **Generation Run (E19)**.

The artifact may include a summary of:

- source documents used
- generated version
- model/provider metadata where appropriate
- prompt/template version where appropriate
- assumptions
- warnings
- rationale summary

This should be useful explainable reasoning, not hidden chain-of-thought.

#### Final trace mapping

The finalized mapping belongs to **Trace Mapping (E20)**.

This is the must-have coverage record:

```text
PRD requested -> design spec required -> Tvastr mockup contains -> implementation delivered
```

Trace mappings should connect requirements and design guidance to screens, components, states, decisions, component mappings, versions, and implementation links.

### DOM-To-Context Mapping

Every meaningful visual element should map to context graph entities.

Example:

```html
<button
  class="tv-button tv-button-primary"
  data-component-id="cmp_search_submit"
  data-requirement-ids="req_keyword_search"
>
  Search
</button>
```

This mapping lets agents and sync tools answer:

- which DOM element represents which component
- which requirement the element satisfies
- which annotations or decisions apply
- which component mapping may be relevant for implementation

DOM IDs and context IDs should be stable across edits when possible.

### Agent Edit Protocol

The artifact should tell local agents how to edit it safely.

The `artifactProtocol` block should define rules such as:

- preserve stable IDs
- update DOM and context together
- append an audit event for meaningful edits
- preserve source references and trace mappings
- keep current visible state materialized
- validate before syncing
- avoid deleting requirements, states, decisions, or mappings unless explicitly requested

This matters when a designer or PM uses Claude Code, Codex, Cursor, or another harness to edit the local artifact. The agent should not have to infer the rules from prose alone.

### Current State And Audit Log

The artifact should be materialized.

That means the visible HTML/CSS/SVG/JS represents the current mockup state. Opening the artifact should show what is currently true.

Edits should also be preserved, but as audit/history:

- who or what changed it
- when it changed
- source primitive
- summary
- affected entity IDs
- base version
- resulting version, if synced

The audit log should not be the primary rendering mechanism. Tvastr should not require replaying every edit event to understand the current artifact.

### Sync Metadata

A published or pulled artifact should contain sync metadata.

The metadata should identify:

- hosted mockup ID
- hosted URL
- base version ID
- export ID
- generated timestamp
- checksum or integrity marker, if used
- artifact format version

This allows **CLI (P1)** and **MCP Server (P2)** to detect whether local edits are based on the latest hosted version.

### Artifact Modes

The same artifact format should support three modes.

#### Hosted mode

The web server renders the artifact or an equivalent representation inside the Tvastr web app.

Hosted mode may add surrounding app UI, permissions, comments, edit controls, and navigation. These hosted controls are not part of the generated artifact requirement.

#### Local mode

The user opens the artifact as a local file.

The mockup should be visible without installing anything. The file should remain understandable in a text editor.

#### Agent mode

An agent reads or edits the artifact through **MCP Server (P2)**, **CLI (P1)**, or local file access granted by the harness.

Agent mode depends on:

- stable DOM structure
- embedded JSON context
- clear IDs
- non-minified text
- embedded/local runtime code when runtime behavior is needed
- artifact protocol and audit log that tell the agent how changes should be made

### Editing Rules

The artifact should be editable by humans and agents.

Valid edits include:

- changing copy
- changing layout-related CSS
- changing colors, spacing, typography, and visibility
- adding/removing supported components
- adding states
- updating annotations
- updating structured context
- adding design rationale
- updating component mappings
- updating trace mappings
- appending audit events

Edits should preserve:

- required context block
- sync metadata when present
- stable entity IDs where possible
- parseable JSON
- valid HTML
- graph invariants
- readable runtime JavaScript
- materialized current state

If an agent changes the DOM, it should update corresponding context entries when needed. If an agent changes context, it should update DOM mappings when needed.

### Validation

The artifact validator should check:

- valid HTML parse
- required `tvastr-context` block exists
- context JSON is parseable
- artifact format version is known
- screens/components referenced in JSON exist in DOM where required
- DOM component IDs are unique
- annotations and decisions target valid entities
- generation runs and trace mappings reference valid entities where present
- audit log is append-only or change-preserving according to policy
- artifact protocol exists for synced/published artifacts
- sync metadata is complete for published artifacts
- no disallowed generated dependencies are present
- JavaScript parses without syntax errors where practical
- no runtime dependencies beyond the artifact's own vanilla JavaScript

Validation should be available through:

- **CLI (P1)**
- **MCP Server (P2)**
- **Web Server (P3)**

### Portability Rules

The artifact should be useful outside Tvastr.

Portability requirements:

- single file by default
- opens in a modern browser
- readable in a text editor
- no build step
- no package install
- no required network access
- self-contained HTML/CSS/SVG/JavaScript by default
- structured context embedded in the file
- stable format version
- one flow per artifact by default

If optional remote links exist, the mockup should still communicate the product structure without them.

### Artifact Invariants

- Generated artifacts may use HTML, CSS, SVG, and JavaScript.
- The artifact must not require a build step, package install, or required network dependency for core behavior.
- The artifact must contain parseable structured context.
- Meaningful visual elements should map to context graph IDs.
- One flow should usually be represented by one artifact, with multiple screens/states inside it.
- The artifact should include source metadata references, generation run summaries, and trace mappings where available.
- The artifact should include an agent edit protocol for local agent workflows.
- The current visible/materialized state is primary; edit history is audit data.
- Published/pulled artifacts should contain sync metadata.
- Artifact exports should reference their source **Mockup Spec (E4)** and **Version (E14)**.
- The artifact should remain legible and non-minified by default.
- Local artifact edits are not visible to collaborators until synced through **CLI (P1)**, **MCP Server (P2)**, or **Web Server (P3)**.

## 10. Designer Edit Mode

**Designer Edit Mode (P5)** is the browser-based visual/manual editing surface for a hosted Tvastr mockup.

The name reflects a common user, not an exclusive role. Any authorized editor should be able to use it: designer, PM, builder, developer, stakeholder, or AI-assisted reviewer. Permissions control access, not job title.

Designer Edit Mode exists because Tvastr cannot be only an AI generator. The generated mockup must be easy for humans to correct, refine, annotate, and approve.

### Edit Mode Jobs

| Job | Description |
| --- | --- |
| Visual edit | Change layout, copy, spacing, style, fields, and visibility directly in the browser |
| Flow edit | Add, remove, reorder, or rename screens and flow steps |
| State edit | Add and modify states such as empty, loading, error, OTP, 2FA, success, and permission-limited |
| Component edit | Select, edit, add, remove, group, or remap meaningful components |
| Context edit | Update requirements, annotations, decisions, rationale, and trace mappings |
| Review | Mark design, PM, or dev review status when permitted |
| Handoff check | Inspect whether the mockup has enough context for coding-agent handoff |
| Export/sync | Trigger exports or update hosted state |
| Optional AI edit | Use Tvastr AI or BYO API key when configured in a later phase |

### Design Principles

Designer Edit Mode should be:

- simple enough for non-technical users
- precise enough to fix real handoff issues
- structured enough that edits update the context graph
- forgiving enough to experiment
- clear about what changed and what is currently true
- useful without any AI subscription

It should not try to become a full professional design canvas.

Tvastr should avoid competing with Figma on high-fidelity canvas depth. Instead, edit mode should focus on the mockup/spec layer: flows, screens, states, components, copy, annotations, decisions, requirement mapping, and implementation handoff context.

### Editing Capabilities

#### Screen and flow editing

Authorized editors should be able to:

- rename screens
- reorder screens in a flow
- add a new screen from a template or blank state
- duplicate a screen
- remove a screen
- define transitions between screens
- mark a screen as optional/deferred
- switch viewport presets where supported

For a login flow, this means the editor can represent login, OTP, 2FA, account locked, error, and success states within the same flow artifact.

#### Component editing

Authorized editors should be able to:

- select meaningful components
- edit text and labels
- edit component visibility
- add common components such as button, input, select, table, card, modal, tab, alert, toast, divider, image placeholder, and icon
- remove components
- group or ungroup components where supported
- reorder components within document flow
- map a component to a design-system or code component
- attach requirement IDs and annotations

Component editing should preserve stable **Component (E7)** IDs where possible.

#### Style editing

Authorized editors should be able to adjust:

- color
- typography
- spacing
- alignment
- size
- border
- radius
- shadow
- visibility
- responsive behavior hints

Style editing should prefer named **Design Token (E12)** values when available, but allow local overrides when no design system exists.

#### State editing

States are first-class.

Authorized editors should be able to add or modify:

- default state
- empty state
- loading state
- error state
- success state
- disabled state
- permission denied state
- mobile state
- long-content state
- modal open/closed state
- OTP state
- 2FA state
- validation state

State editing should update **State (E9)** entries in the context graph, not only hide/show DOM elements.

#### Context editing

Authorized editors should be able to update:

- requirement labels
- priorities
- acceptance criteria
- design rationale
- annotations
- decisions
- open questions
- component mappings
- trace mappings
- implementation hints

Context editing is as important as visual editing. The product value comes from preserving why the mockup looks and behaves the way it does.

### Interaction Model

The default edit interaction should be direct:

```text
Click element -> select component -> edit in side panel or inline
```

Common controls:

- inline text editing
- property side panel
- screen/flow navigator
- state switcher
- component insert menu
- annotations panel
- requirements/traceability panel
- version/change summary modal
- review status controls

The UI should make the structured nature of the mockup visible without overwhelming the user. A designer should be able to edit visually; a PM should be able to edit copy and requirements; a developer should be able to inspect mappings and feasibility notes.

### Save And Version Behavior

Browser edits write to hosted state through **Web Server (P3)**.

The edit mode should support:

- autosave for safe incremental changes, if product policy chooses it
- explicit save with change summary
- draft edit sessions
- undo/redo within a session
- version creation for meaningful saved changes
- audit log entries for meaningful edits

The current visible state should remain primary. The audit log records how it got there.

When saving, Tvastr should capture:

- actor
- timestamp
- affected entities
- change summary
- source primitive: Designer Edit Mode (P5)
- base version
- resulting version

### AI-Assisted Editing

AI-assisted editing is optional.

Designer Edit Mode should work without AI. If AI is available, users may ask for targeted changes such as:

```text
Add an empty state for no search results.
```

```text
Make this flow include OTP and account lockout states.
```

```text
Tighten this layout for a B2B SaaS admin screen.
```

AI edits should follow the same rules as human edits:

- update current materialized state
- update structured context
- preserve stable IDs where possible
- append audit events
- create versions when saved
- expose assumptions or warnings

AI can later be provided by Tvastr, by a workspace configuration, or by user-supplied API keys. BYO API keys are Phase 2, not MVP. The product should not require designers to buy or know Codex, Claude Code, Cursor, or Copilot.

### Local And Agent Editing Coexistence

Designer Edit Mode is not the only edit path.

A user may also:

```text
pull hosted mockup -> edit raw HTML locally with Claude Code/Codex/Cursor -> validate -> sync back
```

The browser edit mode and local artifact edit mode must converge on the same hosted **Mockup Spec (E4)**.

This means:

- browser edits and local syncs must share version/conflict rules
- both should update the same context graph entities
- both should append audit information
- both should preserve trace mappings
- both should respect permissions

### Figma Boundary

Figma may remain part of a team's workflow outside Tvastr.

For MVP, Figma is not part of the product. Post-MVP, Designer Edit Mode may allow teams to:

- keep edits in Tvastr only
- use Figma as a visual refinement tool
- export a handoff package for Figma
- import or reference Figma components where supported
- map Tvastr components to Figma components

Tvastr should not require Figma, and it should not become a worse Figma. The core Tvastr edit surface is the structured mockup/spec, not infinite-canvas visual design.

### Traceability In Edit Mode

Edit Mode should keep traceability visible.

When an editor selects a component or screen, Tvastr should be able to show:

- related requirements
- source document references
- design-spec references
- generation assumptions
- annotations
- decisions
- states
- component mappings
- implementation hints
- trace mapping coverage

Editors should be able to fix broken or missing traceability directly.

Example:

```text
This button exists because REQ-4 requires account recovery.
Design spec says destructive actions must use danger styling.
Current mockup uses Button variant="secondary".
Developer later mapped it to app/components/Button.
```

### Review Actions

Edit Mode should support review markers.

Useful review actions:

- mark screen as PM reviewed
- mark screen as design reviewed
- mark flow as dev reviewed
- mark requirement as covered
- mark state as missing
- mark component mapping as confirmed
- reopen a decision
- request revision

Review actions should create audit entries and may create **Version (E14)** snapshots depending on product policy.

### Edit Mode Validation

Before saving or publishing meaningful edits, Tvastr should validate:

- selected components still exist
- required context remains parseable
- screen and component IDs are unique
- states are attached to valid targets
- annotations and decisions target valid entities
- trace mappings are not broken
- required screens/states for review gates are present or explicitly deferred
- generated/exported artifact remains valid

Validation should be helpful, not punitive. The editor should guide users to fix broken context.

### Edit Mode Non-Goals

Designer Edit Mode is not:

- a full Figma replacement
- a freeform infinite canvas
- a vector illustration tool
- a production code editor
- a replacement for local agent editing
- a requirement that designers use AI

It is the browser surface for refining the structured mockup/spec.

### Designer Edit Mode Invariants

- Editing is permission-based, not role-locked.
- Manual editing must work without AI.
- Visual edits should update structured context when relevant.
- Context edits should remain connected to visible mockup entities.
- Meaningful edits should produce audit history.
- Current visible/materialized state is primary.
- Browser edits and local MCP/CLI syncs must converge on the same **Mockup Spec (E4)**.
- Edit Mode should preserve or repair trace mappings rather than silently dropping them.

## 11. Runtime Flows

Runtime flows describe how the primitives work together during real user journeys.

These flows are not UI wireframes or PRDs. They are choreography: which primitive acts, what it reads, what it writes, what state changes, and what must be preserved.

### Flow Catalog

| ID | Flow | Purpose |
| --- | --- | --- |
| F1 | CLI Create And Publish | PM/builder creates a mockup from local docs and gets a hosted link |
| F2 | MCP Create And Publish | User asks an agent to create a mockup from local docs |
| F3 | Hosted Browser Edit | Authorized user edits the mockup in Designer Edit Mode |
| F4 | Local Agent HTML Edit And Sync | User pulls HTML locally, edits with an agent, and syncs back |
| F5 | Developer Agent Handoff | Developer gives a Tvastr link to a coding agent for implementation |
| F6 | Approval And Finalization | Reviewers approve a version as the finalized handoff artifact |
| F7 | Revision And Regeneration | New requirements or blockers trigger a revised mockup |
| F8 | Export And Portable Handoff | User exports the self-contained HTML artifact |

### F1: CLI Create And Publish

Purpose: a PM or builder creates a mockup without starting in the web app.

```text
Local PRD/design files
  -> CLI (P1)
  -> Web Server (P3)
  -> Mockup Spec (E4)
  -> HTML Mockup Artifact (P4)
  -> Hosted link
```

Steps:

1. User runs:

   ```bash
   tvastr mockup ./prd.md --design ./design.md --publish
   ```

2. **CLI (P1)** resolves and reads only the requested local files.
3. CLI sends source content and metadata to **Web Server (P3)**.
4. Web server creates **Source Document (E3)** records or references.
5. Web server runs generation.
6. Web server creates **Generation Run (E19)**.
7. Web server creates **Mockup Spec (E4)** with flows, screens, components, requirements, states, initial decisions, and trace mappings.
8. Web server creates **Version (E14)**.
9. Web server creates hosted share link.
10. Web server returns generated artifact payload and link.
11. CLI writes local **HTML Mockup Artifact (P4)** with sync metadata.
12. CLI prints local file path, hosted link, and version.

State transitions:

```text
S1 Local Draft -> S2 Generation Requested -> S3 Generated -> S4 Published
```

Must preserve:

- explicit local file access
- source document references
- generation run metadata
- trace mappings
- artifact sync metadata

### F2: MCP Create And Publish

Purpose: a user asks Codex, Claude Code, Cursor, Copilot, or another agent harness to create a Tvastr mockup.

```text
User instruction in agent
  -> MCP Server (P2)
  -> local files
  -> Web Server (P3)
  -> hosted mockup + local artifact
```

Steps:

1. User tells agent:

   ```text
   Use Tvastr to create a mockup from ./prd.md and ./design.md. Publish it.
   ```

2. Agent calls `tvastr_create_mockup`.
3. **MCP Server (P2)** resolves paths within allowed roots.
4. MCP server reads only requested files.
5. MCP server sends source content and metadata to **Web Server (P3)**.
6. Web server performs the same generation/publish work as **F1**.
7. MCP server optionally writes local **HTML Mockup Artifact (P4)**.
8. MCP server returns structured result to the agent.
9. Agent reports hosted link, local file path, and warnings to the user.

State transitions:

```text
S1 Local Draft -> S2 Generation Requested -> S3 Generated -> S4 Published
```

Must preserve:

- host filesystem permissions
- explicit file paths
- structured result shape
- version identity
- warnings and assumptions

### F3: Hosted Browser Edit

Purpose: an authorized user refines the mockup in the browser.

```text
Hosted link
  -> Web Server (P3)
  -> Designer Edit Mode (P5)
  -> edit events
  -> Web Server (P3)
  -> new Version (E14)
```

Steps:

1. User opens hosted mockup link.
2. Web server checks permissions.
3. User enters **Designer Edit Mode (P5)** if authorized.
4. User edits screens, components, states, copy, styles, annotations, decisions, or trace mappings.
5. Edit mode validates changed targets.
6. User saves or autosave policy triggers save.
7. Web server normalizes edit events into context graph changes.
8. Web server updates materialized current mockup state.
9. Web server appends audit entries.
10. Web server creates **Version (E14)** when changes are meaningful.
11. Web server updates hosted rendering and agent context.

State transitions:

```text
S5 Human Review -> S6 Editing -> S8 Synced
```

May continue to:

```text
S8 Synced -> S9 Design Reviewed
S8 Synced -> S10 Dev Reviewed
```

Must preserve:

- stable entity IDs where possible
- current materialized state
- audit trail
- trace mappings
- graph invariants

### F4: Local Agent HTML Edit And Sync

Purpose: a designer, PM, or developer edits the raw HTML artifact locally with an agent and pushes changes back.

```text
Hosted mockup
  -> MCP Server (P2) pull
  -> local HTML Mockup Artifact (P4)
  -> agent edits HTML/context
  -> MCP validate
  -> MCP sync
  -> Web Server (P3)
  -> new Version (E14)
```

Steps:

1. User asks agent to pull a mockup locally.
2. Agent calls `tvastr_pull_artifact`.
3. MCP server fetches artifact and writes local `.mockup.html`.
4. Artifact includes sync metadata, `artifactProtocol`, structured context, and audit log.
5. User asks agent to modify the mockup.
6. Agent edits current materialized HTML/CSS/SVG/JS and updates `tvastr-context`.
7. Agent appends audit events according to artifact protocol.
8. Agent or user calls `tvastr_validate_artifact`.
9. MCP server validates HTML, context, trace mappings, and runtime dependency rules.
10. Agent calls `tvastr_sync_artifact`.
11. MCP server compares local base version with hosted latest version.
12. If no conflict, MCP server submits changes to web server.
13. Web server accepts changes, updates the canonical hosted **HTML Mockup Artifact (P4)**, and creates **Version (E14)**.
14. MCP server returns updated link/version to the agent.

State transitions:

```text
S4 Published -> S6 Editing -> S7 Sync Pending -> S8 Synced
```

Conflict path:

```text
S7 Sync Pending -> conflict detected -> user/agent chooses merge, pull latest, or abort
```

Must preserve:

- artifact protocol
- audit log
- current materialized state
- base version
- sync metadata
- graph invariants
- explicit conflict handling

#### Assurance model

Tvastr cannot fully assure that an arbitrary local agent will follow instructions just because the artifact contains an `artifactProtocol`. The protocol tells the agent what to do; assurance comes from the surrounding tools.

Assurance should come from:

- **Structured edit tools where possible**: MCP should prefer targeted operations such as "add state", "rename screen", or "update trace mapping" over unconstrained raw text edits when the agent can use them.
- **Artifact validation before sync**: CLI/MCP validators check HTML, JavaScript syntax where practical, context JSON, IDs, trace mappings, audit log, and runtime dependency rules.
- **Server-side acceptance rules**: **Web Server (P3)** revalidates every synced change before accepting it into the canonical hosted **HTML Mockup Artifact (P4)**.
- **Base-version checks**: sync metadata records the local base **Version (E14)** so the server can detect stale edits and conflicts.
- **Audit requirements**: meaningful local edits must include audit entries; missing audit entries can be rejected or accepted with server-generated audit warnings depending on policy.
- **Graph invariant checks**: changed DOM/context must not create orphan components, broken requirement links, invalid state targets, or malformed trace mappings.
- **Canonical normalization**: after accepting changes, the server should be able to normalize the current hosted artifact and ensure its embedded context remains parseable and coherent.

The raw HTML path is powerful, but it should not be the only safe edit path. For important operations, the MCP server should expose structured edit tools that make correct changes easier than freeform changes.

### F5: Developer Agent Handoff

Purpose: a developer gives a mockup link to a coding agent so the agent can implement with structured context.

```text
Developer prompt
  -> coding agent
  -> MCP Server (P2) or Web API
  -> Agent Context (E16)
  -> downstream implementation workflow
```

Steps:

1. Developer receives or opens hosted mockup link.
2. Developer asks agent:

   ```text
   Read this Tvastr mockup spec and implement it in this repo:
   https://tvastr.app/m/abc123
   ```

3. Agent calls `tvastr_get_context` through MCP or a web API.
4. Tvastr returns **Agent Context (E16)** for a specific **Version (E14)**.
5. Tvastr's core responsibility ends at delivering versioned, structured handoff context.
6. The coding agent then enters the downstream implementation workflow.

Recommended downstream behavior, outside Tvastr's guaranteed runtime boundary:

- agent reads local repository conventions and available components
- agent maps Tvastr components to code components using **Component Mapping (E13)** where available
- agent identifies missing APIs, components, states, or requirements
- agent proposes an implementation plan
- developer approves or asks for changes
- agent implements in repo
- agent reports coverage and blockers

State transitions:

```text
S10 Dev Reviewed -> S11 Ready For Agent Handoff
```

Must preserve:

- version identity
- requirement coverage
- state coverage
- component mappings
- unresolved questions
- explicit handoff boundary
 
After this point, Tvastr may be referenced by the coding agent, but it does not control implementation execution.

### F6: Approval And Finalization

Purpose: reviewers mark a mockup version as approved by product and/or design.

```text
Review comments and edits
  -> resolved decisions
  -> optional trace mapping check
  -> approval marker
  -> approved version
```

Steps:

1. PM, designer, developer, or authorized reviewer reviews the current mockup version.
2. Feedback is captured through comments, annotations, decisions, direct edits, or trace mapping changes.
3. Required comments/questions are resolved or explicitly deferred according to team preference.
4. **Trace Mapping (E20)** may be checked for coverage:

   ```text
   PRD requested -> design spec required -> Tvastr mockup contains
   ```

5. Reviewer marks the version as approved by product and/or approved by design.
6. Web server records approval actor, timestamp, version, approval type, and optional approval note.
7. If the artifact changes after approval, Tvastr should make it possible to undo or invalidate approval on the changed diff.
8. Agent handoff context and exports can reference the latest approved version when available.

State transitions:

```text
S8 Synced -> S9 Design Reviewed
S8/S9 -> S10 Dev Reviewed
S9/S10 -> S11 Ready For Agent Handoff, if the team chooses to use that marker
```

Must preserve:

- approval actor
- approval timestamp
- approved version and approval type
- unresolved-but-deferred items
- comments and decisions
- trace mappings

### F7: Revision And Regeneration

Purpose: new information changes the mockup.

Common triggers:

- PM adds a requirement
- designer changes flow or state
- developer finds a technical blocker
- coding agent reports missing context
- stakeholder changes scope
- approved version is later found to be wrong or incomplete

Steps:

1. Actor records the reason for revision.
2. Tvastr moves mockup to **Needs Revision (S14)**.
3. Actor chooses revision method:
   - manual browser edit
   - local agent HTML edit
   - CLI/MCP regeneration
   - web AI-assisted regeneration
4. Tvastr preserves previous **Version (E14)**.
5. Tvastr creates new **Generation Run (E19)** if AI regeneration occurs.
6. Tvastr updates **Trace Mapping (E20)**.
7. Tvastr creates new version.
8. Review gates may need to be repeated.

State transitions:

```text
S14 Needs Revision -> S6 Editing
S14 Needs Revision -> S2 Generation Requested -> S3 Generated
```

Must preserve:

- revision reason
- previous version
- changed source references
- assumptions
- trace mapping changes
- audit trail

### F8: Export And Portable Handoff

Purpose: users create portable artifacts for sharing, review, archive, or agent input.

```text
Mockup Spec (E4)
  -> Export Service
  -> Export (E15)
  -> HTML artifact with embedded agent context
```

Steps:

1. User requests export from web, CLI, or MCP.
2. Tvastr resolves target **Mockup Spec (E4)** and **Version (E14)**.
3. Tvastr validates current state.
4. Tvastr generates requested **Export (E15)**.
5. Export records source mockup/version.
6. User receives file, link, or structured output.

Supported MVP export:

- self-contained `.mockup.html`

The agent context JSON is embedded inside the HTML artifact. Markdown, screenshots/images, Figma packages, and standalone agent context JSON are post-MVP.

State transition:

```text
no lifecycle state change required unless export is recorded as meaningful
```

Must preserve:

- version identity
- source references
- trace mappings
- artifact protocol for HTML exports
- no build/network dependency for portable HTML core behavior

### Cross-Flow Invariants

- Local file reads happen only in local primitives: **CLI (P1)** and **MCP Server (P2)**.
- Published mockups use the server-stored **HTML Mockup Artifact (P4)** as canonical state.
- Every meaningful hosted change creates or updates **Version (E14)**.
- Current materialized state is primary; audit logs explain how it changed.
- **Trace Mapping (E20)** should be preserved across generation, editing, sync, handoff, approval, and revision.
- **Agent Context (E16)** should reference a specific mockup version.
- Browser edits and local artifact edits must converge on the same **Mockup Spec (E4)**.
- Runtime flows should avoid forcing users to start in the web app.

## 12. Contracts

Contracts define the shapes that let Tvastr primitives interoperate.

This section is not a final OpenAPI document or JSON Schema package. It is a foundation-level contract map: what must exist, what must be stable, and which primitive consumes or produces each contract.

### Contract Catalog

| ID | Contract | Producer | Consumer |
| --- | --- | --- | --- |
| C1 | CLI Command Contract | CLI (P1) | PMs, builders, developers, scripts, agents |
| C2 | MCP Tool Contract | MCP Server (P2) | Codex, Claude Code, Cursor, Copilot, agent harnesses |
| C3 | Web API Contract | Web Server (P3) | CLI, MCP, browser, integrations |
| C4 | Artifact Context Contract | HTML Mockup Artifact (P4), Web Server (P3) | CLI, MCP, Web Server, agents |
| C5 | Edit Event Contract | Designer Edit Mode (P5), MCP, CLI | Web Server |
| C6 | Sync Change Contract | CLI, MCP | Web Server |
| C7 | Validation Result Contract | CLI, MCP, Web Server | humans, agents, automation |
| C8 | Agent Context Contract | Web Server, MCP | coding agents and agent harnesses |
| C9 | Trace Mapping Contract | Web Server, artifact, edit mode | humans, agents, exports |
| C10 | Version Contract | Web Server | all primitives |
| C11 | Approval Contract | Designer Edit Mode, Web Server | exports, agent context, humans |
| C12 | Error Contract | all primitives | humans, agents, automation |

### C1: CLI Command Contract

The CLI command contract defines stable command jobs, not necessarily final command names.

Required command families:

```bash
tvastr login
tvastr mockup <source-path...> [--design <path...>] [--publish]
tvastr publish <artifact-path>
tvastr pull <mockup-url-or-id>
tvastr sync <artifact-path>
tvastr validate <artifact-path>
tvastr export <mockup-url-or-id> --format html
tvastr context <mockup-url-or-id> [--for <agent|task>]
tvastr status <mockup-url-or-id|artifact-path>
tvastr versions <mockup-url-or-id>
```

Common options:

- `--publish`
- `--output <path>`
- `--format <html>`
- `--version <version-id>`
- `--workspace <workspace-id>`
- `--project <project-id>`
- `--json`
- `--force`
- `--dry-run`

CLI commands should return human-readable output by default and machine-readable JSON when `--json` is provided.

### C2: MCP Tool Contract

MCP tools should be small, explicit, and structured.

Required tools:

| Tool | Purpose |
| --- | --- |
| `tvastr_create_mockup` | Create mockup from local source paths or provided text |
| `tvastr_get_mockup` | Read mockup metadata and lifecycle state |
| `tvastr_get_context` | Extract **Agent Context (E16)** from the canonical artifact for a specific version |
| `tvastr_pull_artifact` | Write hosted HTML artifact locally |
| `tvastr_validate_artifact` | Validate local artifact |
| `tvastr_sync_artifact` | Push local artifact changes to hosted state |
| `tvastr_list_versions` | List versions |
| `tvastr_export_mockup` | Export the self-contained HTML artifact |
| `tvastr_approve_version` | Approve/finalize a version when permitted |

MCP tool results should always include:

- `ok`
- stable IDs where applicable
- version identity where applicable
- warnings
- error object when failed
- suggested next action when useful

Example result:

```json
{
  "ok": true,
  "mockupId": "mock_abc123",
  "url": "https://tvastr.app/m/abc123",
  "versionId": "v3",
  "artifactPath": "./search-v2.mockup.html",
  "warnings": []
}
```

### C3: Web API Contract

The web API is consumed by CLI, MCP, browser edit mode, and future integrations.

Required API capabilities:

- create generation request
- create/publish mockup
- get mockup metadata
- get mockup version
- get artifact export
- get agent context
- submit edit events
- submit artifact sync changes
- validate artifact/context
- list versions
- create export
- create approval/finalization marker
- manage share permissions

The API should use versioned endpoints or versioned payloads before external integrations depend on it.

### C4: Artifact Context Contract

The artifact context contract is the JSON stored in:

```html
<script type="application/json" id="tvastr-context">
  {}
</script>
```

Required top-level fields:

```json
{
  "formatVersion": "1.0",
  "mockupId": "mock_abc123",
  "versionId": "v3",
  "project": {},
  "sources": [],
  "generationRuns": [],
  "flows": [],
  "screens": [],
  "components": [],
  "requirements": [],
  "states": [],
  "annotations": [],
  "decisions": [],
  "designTokens": [],
  "componentMappings": [],
  "traceMappings": [],
  "sync": {},
  "artifactProtocol": {},
  "auditLog": []
}
```

Rules:

- IDs must be stable where possible.
- DOM elements must reference context IDs through data attributes.
- Context must be parseable without running artifact JavaScript.
- Full PRDs/design docs are not required in the artifact; references, hashes, excerpts, and IDs are preferred.
- Current materialized state is primary; `auditLog` is history.

### C5: Edit Event Contract

Edit events describe browser or structured-agent changes before they become canonical state.

Example:

```json
{
  "eventId": "evt_123",
  "mockupId": "mock_abc123",
  "baseVersionId": "v3",
  "actor": {
    "type": "user",
    "id": "user_123",
    "roleLabel": "designer"
  },
  "sourcePrimitive": "P5",
  "operation": "component.updateText",
  "target": {
    "entityType": "component",
    "id": "cmp_submit"
  },
  "patch": {
    "text": "Send code"
  },
  "summary": "Updated submit button copy",
  "timestamp": "2026-05-19T14:30:00Z"
}
```

Edit events should be normalized by **Web Server (P3)** into changes to the canonical artifact and embedded context.

### C6: Sync Change Contract

Sync changes are submitted by **CLI (P1)** or **MCP Server (P2)** when local artifact edits are pushed to hosted state.

Required fields:

```json
{
  "mockupId": "mock_abc123",
  "baseVersionId": "v3",
  "artifactFormatVersion": "1.0",
  "changeSummary": "Added OTP state and clarified error copy",
  "artifactHtml": "<!DOCTYPE html>...",
  "context": {},
  "auditLogDelta": [],
  "client": {
    "primitive": "P2",
    "name": "tvastr-mcp",
    "version": "0.1.0"
  }
}
```

Server acceptance must validate:

- base version
- artifact format
- context parseability
- graph invariants
- audit requirements
- trace mapping integrity
- dependency/runtime rules

### C7: Validation Result Contract

Validation results should be consistent across CLI, MCP, and web server.

Example:

```json
{
  "ok": false,
  "artifactPath": "./login.mockup.html",
  "mockupId": "mock_login",
  "baseVersionId": "v2",
  "errors": [
    {
      "code": "BROKEN_TRACE_MAPPING",
      "message": "Trace mapping tm_4 references missing component cmp_otp_submit.",
      "severity": "error",
      "target": "traceMapping:tm_4"
    }
  ],
  "warnings": [
    {
      "code": "MISSING_AUDIT_EVENT",
      "message": "A component changed without a matching audit event.",
      "severity": "warning",
      "target": "component:cmp_title"
    }
  ]
}
```

Validation severity levels:

- `info`
- `warning`
- `error`
- `blocking`

Only valid or explicitly override-approved changes should reach the hosted canonical artifact.

### C8: Agent Context Contract

Agent context is the implementation-facing structured summary.

In MVP, agent context lives embedded inside the **HTML Mockup Artifact (P4)**. This contract describes the structured view extracted for tools and agents; it should not become a separate canonical export format unless that decision is reopened.

Required fields:

```json
{
  "mockupId": "mock_abc123",
  "versionId": "v5",
  "approvalState": "approved_by_product",
  "summary": "",
  "flows": [],
  "screens": [],
  "components": [],
  "requirements": [],
  "states": [],
  "annotations": [],
  "decisions": [],
  "componentMappings": [],
  "traceMappings": [],
  "openQuestions": [],
  "implementationHints": []
}
```

Agent context should be:

- versioned
- compact enough to consume
- explicit about unresolved questions
- explicit about lightweight approval state, if any
- clear that downstream implementation execution is outside Tvastr's guaranteed boundary

### C9: Trace Mapping Contract

Trace mappings connect source intent to mockup output.

Example:

```json
{
  "id": "tm_login_otp",
  "requirementRefs": ["req_auth_otp"],
  "designRefs": ["design_auth_modal_pattern"],
  "mockupRefs": [
    {"type": "screen", "id": "scr_otp"},
    {"type": "component", "id": "cmp_otp_input"},
    {"type": "state", "id": "state_otp_error"}
  ],
  "status": "covered",
  "notes": "OTP screen and invalid-code state are represented in the login flow."
}
```

Allowed statuses:

- `covered`
- `partial`
- `missing`
- `deferred`
- `not_applicable`

Implementation delivery may be added later, but approval/finalization does not require Tvastr to own implementation feedback.

### C10: Version Contract

Every meaningful hosted state change should reference a version.

Required fields:

```json
{
  "versionId": "v5",
  "mockupId": "mock_abc123",
  "parentVersionId": "v4",
  "createdAt": "2026-05-19T14:30:00Z",
  "actor": {},
  "sourcePrimitive": "P5",
  "summary": "Added 2FA and OTP states",
  "affectedEntities": [],
  "approvalState": "draft"
}
```

Versions are the stable anchor for exports, agent context, approvals, sync, and rollback.

### C11: Approval Contract

Approval records lightweight team approval.

Example:

```json
{
  "approvalId": "appr_123",
  "mockupId": "mock_abc123",
  "versionId": "v5",
  "approvedBy": {
    "type": "user",
    "id": "user_123",
    "roleLabel": "pm"
  },
  "approvalType": "approved_by_product",
  "approvedAt": "2026-05-19T14:45:00Z",
  "deferredItems": ["traceMapping:tm_password_reset_mobile"],
  "note": "Approved for first implementation pass."
}
```

Approval should approve a specific version, but it should not become a heavy workflow engine in MVP. Required approval types for MVP are `approved_by_product` and `approved_by_design`. If a later diff changes the approved version, Tvastr should allow approval to be undone or marked stale.

### C12: Error Contract

Errors should be structured for both humans and agents.

Example:

```json
{
  "ok": false,
  "error": {
    "code": "SYNC_CONFLICT",
    "message": "The hosted mockup changed since this artifact was pulled.",
    "severity": "blocking",
    "retryable": false,
    "details": {
      "localBaseVersion": "v3",
      "hostedLatestVersion": "v5",
      "conflicts": ["component:cmp_otp_input"]
    },
    "suggestedNextAction": "Pull the latest version or resolve conflicts manually."
  }
}
```

Common error categories:

- auth/permission
- missing file
- invalid source
- generation failure
- validation failure
- sync conflict
- unsupported artifact format
- broken trace mapping
- server unavailable

### Contract Invariants

- Contracts should include format or API version where appropriate.
- Hosted writes should include actor, base version, source primitive, and change summary.
- Agent-facing contracts should be structured, not prose-only.
- Artifact context must be parseable without executing JavaScript.
- Approval, export, and agent context should reference a specific **Version (E14)**.
- Validation contracts should be shared across CLI, MCP, and web.
- Error contracts should be clear enough for both users and agents to decide the next step.

## 13. Constraints And Non-Goals

This section defines boundaries that future PRDs should preserve.

Tvastr is a new kind of product, so constraints matter. Without them, the product can easily drift into being a generic design tool, a portal-first document uploader, a code generator, or a project-management system.

### Hard Constraints

| ID | Constraint | Meaning |
| --- | --- | --- |
| N1 | Local file reads require local tools | The web app must not directly read arbitrary local files |
| N2 | No portal-first requirement | Users should not need to start by uploading PRDs into a Tvastr web portal |
| N3 | Published artifact is canonical | Once published, **Web Server (P3)** stores the canonical **HTML Mockup Artifact (P4)** |
| N4 | Artifact is self-contained | **HTML Mockup Artifact (P4)** should not require build steps, package installs, or required network dependencies |
| N5 | Context is first-class | Requirements, states, annotations, decisions, trace mappings, and agent context are product data, not comments sprinkled around a UI |
| N6 | Current state is primary | The visible/materialized mockup is primary; audit logs explain history |
| N7 | Validation is required for sync | Local/agent artifact edits must be validated before hosted acceptance |
| N8 | Editing is permission-based | Capabilities are controlled by permissions, not job titles |
| N9 | AI is optional for human editing | Manual browser editing must work without an AI subscription |
| N10 | Tvastr does not own implementation execution | Agent coding and repo changes are downstream behavior, not Tvastr's guaranteed runtime boundary |
| N11 | One flow per artifact by default | A flow with screens, modals, OTP, 2FA, and states should usually live in one artifact |
| N12 | Agent context must be versioned | Handoff context must reference a specific **Version (E14)** |
| N13 | Local-only is first-class | The HTML artifact must be useful even when shared directly outside the server |

### Local File Boundary

The browser app must not directly read arbitrary local files.

Local files may be read only by:

- **CLI (P1)**
- **MCP Server (P2)**
- future editor extensions
- agent harness integrations with user-granted file access

Users must explicitly provide paths, commands, or tool calls. Tvastr should not silently scan a workspace, repository, home directory, or synced drive.

### Workflow Constraint

Tvastr must meet users where they already work.

The primary creation path should be:

```text
local docs / existing tools -> CLI or MCP -> generated mockup/link
```

Not:

```text
go to Tvastr website -> upload everything -> start over
```

The web app may support upload, paste, and integrations, but those are fallback or optional paths.

### Artifact Constraint

The **HTML Mockup Artifact (P4)** should be self-contained by default.

Allowed:

- HTML
- CSS
- SVG
- JavaScript
- embedded structured JSON context

Not allowed for core artifact behavior:

- build step
- package install
- required network dependency
- unbundled runtime framework dependency
- bundled UI/helper library dependency for MVP
- remote script required for rendering
- remote CSS required for rendering
- canvas-only representation
- minified/obfuscated output as the primary artifact

The artifact may use JavaScript extensively for flow behavior, state switching, modals, popups, OTP, 2FA, annotations, and local artifact runtime behavior. The constraint is portability and inspectability, not absence of JavaScript.

For MVP, artifact JavaScript should be vanilla JavaScript only.

### Design Tool Non-Goal

Tvastr is not trying to replace Figma.

Non-goals:

- full infinite-canvas design environment
- vector illustration suite
- advanced prototyping timeline tool
- full design-system management suite
- pixel-perfect high-fidelity design replacement

Tvastr may import from, export to, or reference Figma, but the core product is the structured mockup/spec and its handoff context.

### Implementation Non-Goal

Tvastr does not own production code implementation.

Tvastr should provide:

- versioned agent context
- requirements
- flows
- screens
- states
- decisions
- component mappings
- trace mappings
- approval state

After that, Codex, Claude Code, Cursor, Copilot, or another coding agent may implement in the local repo. That downstream implementation is outside Tvastr's guaranteed runtime boundary.

Tvastr may later integrate with PRs, branches, commits, or tickets, but that is not required for the core handoff product.

### Feedback Non-Goal

Tvastr does not need a separate implementation feedback loop as a core primitive.

Feedback before finalization should happen through:

- comments
- annotations
- decisions
- direct edits
- trace mapping changes
- review markers

The clean product boundary is approval/finalization of a version for handoff.

### Local-Only Constraint

Local-only mode is first-class.

Users should be able to:

- generate or receive a `.mockup.html` artifact
- share it directly in Slack, email, or a drive
- open it in a browser
- inspect and edit it locally
- preserve embedded context and audit history

The server makes exchange, hosting, and access easier. It should not be required for the artifact to be meaningful.

### AI Non-Goals

Tvastr should not assume every stakeholder has an AI subscription or wants to use an agent.

Non-goals:

- requiring designers to use Claude Code, Codex, Cursor, or Copilot
- requiring PMs to use an agent harness
- making manual editing second-class
- treating generated output as final truth
- storing hidden model chain-of-thought as product data

Tvastr should store useful generation metadata, assumptions, warnings, and rationale summaries through **Generation Run (E19)**.

### Assurance Boundary

Tvastr cannot guarantee that arbitrary local agents will edit raw HTML correctly.

Tvastr can provide assurance through:

- artifact protocol
- structured MCP edit tools
- validation
- base-version conflict checks
- server-side acceptance/rejection
- graph invariant checks
- audit requirements
- canonical artifact normalization

Raw HTML editing is allowed because it is powerful and agent-friendly, but hosted acceptance must remain guarded.

### Permission Constraint

Roles are labels, not hard product walls.

PM, designer, developer, stakeholder, and AI agent roles may influence defaults. MVP access is domain-based as described in **O1**. Future capability-based permissions may include:

- can view
- can comment
- can edit
- can sync
- can publish
- can approve/finalize
- can export
- can read agent context
- can manage permissions

A PM may edit layout. A designer may use MCP. A developer may comment on product intent. An AI agent may suggest changes. The system should allow this when the access model permits it.

### Marketing Constraint

The web server may later include a public marketing and education surface. This is not part of MVP.

This is eventually necessary because Tvastr is not an obvious existing category. The public site should explain:

- why AI-native mockup/spec artifacts matter
- why visual mockups alone are insufficient
- why structured traceability matters for coding agents
- why the product exists now
- why Tvastr is not just another design tool

This marketing surface should be publicly accessible and separate from private mockup/workspace authorization.

### Non-Goal Summary

Tvastr is not:

- AI Figma
- a generic design canvas
- a production code generator
- a project-management tool
- a replacement for PRD/document tools
- a replacement for GitHub/GitLab
- a replacement for Linear/Jira
- a generic file sync tool
- a requirement that all users start in a web app
- a system that silently reads local workspaces

Tvastr is:

- a local-first mockup generation and handoff system
- a hosted structured mockup/spec collaboration layer
- a portable HTML artifact format
- a human-editable and agent-readable product context graph
- a bridge between product intent, design refinement, and AI-assisted implementation

## 14. Open Decisions

This section records decisions, current defaults, and remaining open items.

### Decision Catalog

| ID | Decision | Status |
| --- | --- | --- |
| O1 | Auth and share-link model | Decided for MVP |
| O2 | Workspace/project requirement for first use | Decided for MVP |
| O3 | Artifact runtime library policy | Decided for MVP |
| O4 | Artifact storage strategy | Decided for MVP |
| O5 | Versioning granularity | Default chosen, may tune later |
| O6 | Diff strategy | Decided for MVP |
| O7 | Validation strictness | Default chosen |
| O8 | MCP structured edit tools | Later; CLI first |
| O9 | Approval model | Lightweight for MVP |
| O10 | Figma integration depth | Not MVP |
| O11 | BYO API key policy | Phase 2 |
| O12 | Local-only mode | First-class |
| O13 | Marketing site scope | Not MVP |
| O14 | Export formats for MVP | HTML only |
| O15 | Pricing and limits | Later |
| O16 | Data retention and privacy | Store forever for now; later problem |

### O1: Auth And Share-Link Model

Decision:

- Use Google SSO.
- Artifacts should not be Google-indexable.
- Mockups are shareable by URL.
- A user must be logged in to view.
- If the creator's domain is `gmail.com`, any logged-in user with the URL can view and edit.
- If the creator uses an organization domain, only users from the same organization domain can view and edit.
- Users outside the allowed domain see a no-permissions wall.

Implication:

MVP does not need complex invited-member permissions. Domain-based access plus URL sharing is the starting model.

### O2: Workspace/Project Requirement For First Use

Decision:

- Workspaces are auto-created by default.
- V1 should avoid exposing workspace management unless absolutely necessary.
- Users should not be interrupted by workspace setup before getting value.

Implication:

Workspace (E1) may exist internally for ownership and future billing, but it should not be a visible V1 concept unless needed.

### O3: Artifact Runtime Library Policy

Decision:

- Use vanilla JavaScript only for MVP.
- Do not use Lit, htmx, Tailwind, DOM helper libraries, or other bundled UI libraries in the generated artifact unless this decision is reopened.

Implication:

The artifact should be easy for humans and agents to understand. Avoid clever runtime abstractions.

### O4: Artifact Storage Strategy

Decision:

- Everything important lives in the **HTML Mockup Artifact (P4)**.
- The HTML artifact is the canonical representation, warts and all.
- The server stores the artifact.
- The server may index metadata for access, validation, previews, search, and performance, but the HTML artifact remains the source of truth.

Implication:

The product should resist splitting the canonical truth into a separate hidden graph database that can drift from the artifact.

### O5: Versioning Granularity

Decision:

- Default to verbose versioning.
- Create versions for meaningful saves, syncs, generation runs, approval changes, and major context edits.
- Preserve audit logs generously.

Suggested default:

- Autosave may create draft revisions.
- Explicit save/sync/finalize creates named versions.
- Approval changes should be reversible and traceable.

### O6: Diff Strategy

Decision:

- No screenshot diffs for MVP.
- The product lives as the artifact itself.
- Diff is primarily for agents.

Implication:

Prioritize HTML/context/trace/audit diffs over visual screenshot comparison.

### O7: Validation Strictness

Decision:

Accept the earlier recommendation:

- Block broken context JSON.
- Block missing required IDs.
- Block invalid sync metadata.
- Block graph invariant violations.
- Treat missing audit entries and some trace gaps as warnings at first.

### O8: MCP Structured Edit Tools

Decision:

- MCP will come later.
- Build CLI first.

Implication:

MVP should not depend on MCP availability. MCP contracts remain useful, but implementation sequencing should prioritize CLI and artifact workflows.

### O9: Approval Model

Decision:

- Approval flows are second-class in MVP.
- Approval happens within the team.
- Do not over-restrict workflows around approval.
- Support lightweight markers:
  - approved by design
  - approved by product
  - undo approval when a diff/change invalidates it

Implication:

Approval should be useful metadata, not a blocking workflow engine.

### O10: Figma Integration Depth

Decision:

- Figma is not part of MVP.

Implication:

Do not build Figma import/export/mapping for V1. Keep architecture open for later integration.

### O11: BYO API Key Policy

Decision:

- Not part of MVP.
- Move to Phase 2.

### O12: Local-Only Mode

Decision:

- Local-only mode is a first-class citizen.
- Server exists to make exchange of data easier.
- Users should be able to share the HTML file directly in Slack.
- A designer should be able to open that HTML file and edit it without needing hosted server state.

Implication:

The artifact must remain useful as a standalone product surface, not merely an export from the server.

### O13: Marketing Site Scope

Decision:

- Not part of MVP.

Implication:

The web server can later own public marketing/education pages, but V1 implementation should focus on the product primitives.

### O14: Export Formats For MVP

Decision:

- HTML is the only export format for MVP.
- Agent context JSON is embedded inside the HTML artifact.

Implication:

Do not build Markdown, screenshots, Figma packages, image exports, or standalone agent context JSON exports for MVP unless this decision is reopened.

### O15: Pricing And Limits

Decision:

- Later.

Implication:

Do not overfit MVP architecture to pricing before usage shape is known.

### O16: Data Retention And Privacy

Decision:

- Everything stored on the server is stored forever for now.
- Retention/deletion/privacy controls are a later problem.

Implication:

This is acceptable for early development but must be revisited before broad external or enterprise launch.

### Remaining Decision Invariants

- Decisions that change entities, primitives, or lifecycle states should update this foundation document.
- Decisions with engineering consequences should become ADRs.
- Decisions with product/user behavior consequences should become PRDs.
- Security, privacy, and billing decisions should be revisited before broad external launch.
