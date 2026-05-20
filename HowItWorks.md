# How It Works

## Core Idea

Tvastr should meet users where they already work.

The PM or builder should not have to upload documents to a new web app as the primary workflow. Their PRD, notes, and design guidance may live locally, in a repo, in Notion, in Google Docs, or in exported Markdown. The product should be accessible from the tools they already use: Codex, Claude Code, Cursor, Copilot, a terminal, or eventually a VS Code/Cursor extension.

The key architecture:

```text
Local runner on user's machine -> reads local PRD/design files
Tvastr cloud service -> generates, stores, and publishes the mockup
Tvastr web editor -> humans review and edit the mockup
Tvastr agent endpoint -> coding agents read structured context and build from it
```

The web app should not directly read local files. A browser cannot and should not casually read arbitrary files from a user's machine.

Local files are read by a local tool that the user explicitly invokes:

- Tvastr CLI
- Tvastr local MCP server
- editor extension
- AI agent integration

The cloud product receives the document contents from the local runner, generates the mockup, and returns either a local `.mockup.html` file, a shareable link, or both.

## Product Surfaces

Tvastr needs three surfaces.

### 1. Local Generator

This is how PMs, builders, or developers create a mockup from documents that already exist on their machine.

Initial version:

```bash
npx tvastr mockup ./prd.md --design ./design-notes.md --publish
```

The CLI:

1. Reads the local files.
2. Sends their contents to the Tvastr backend.
3. Receives generated mockup data.
4. Writes a local `.mockup.html` file.
5. Optionally publishes a shareable link.

Example output:

```text
Created mockup:
./search-v2.mockup.html

Published:
https://tvastr.app/m/abc123
```

### 2. Shareable Mockup Editor

This is the human-facing browser experience.

PMs, designers, developers, and stakeholders can open the link and see the actual mockup immediately.

The editor supports:

- visual review
- manual edits
- copy changes
- layout changes
- adding/removing fields
- simple styling changes
- state edits
- annotations
- requirement notes
- design rationale
- feasibility notes
- version history

The designer should not need Cursor, Codex, Claude Code, or any AI subscription. Manual editing must be simple, obvious, and reliable.

If a designer wants AI-powered edits, they can bring their own API key or use a paid Tvastr workspace.

### 3. Agent-Readable Endpoint

This is how coding agents build from the mockup.

A developer should be able to give Codex, Claude Code, Cursor, Copilot, or another agent a Tvastr link:

```text
Read this mockup spec and implement it in this repo:
https://tvastr.app/m/abc123
```

The agent should not receive only a screenshot or static HTML. It should receive structured context:

- screens
- flows
- components
- requirement IDs
- annotations
- acceptance criteria
- design rationale
- design tokens
- states
- implementation hints
- unresolved questions
- component mappings

The mockup is both visual for humans and structured for agents.

## PM / Builder Flow

### Tools

The PM or builder may use:

- local Markdown files
- Notion or Google Docs exports
- PRD documents in a repo
- Cursor
- Claude Code
- Codex
- Copilot
- terminal
- Tvastr CLI
- Tvastr MCP server

### Actions

1. The PM keeps the PRD and design notes wherever they already are.
2. If needed, they export them to local files such as `prd.md` or `design-notes.md`.
3. From a terminal or AI coding tool, they invoke Tvastr.

CLI example:

```bash
npx tvastr mockup ./prd.md --design ./design-notes.md --publish
```

Agent example:

```text
Use Tvastr to create a mockup from ./prd.md and ./design-notes.md. Publish it and give me the link.
```

4. The local Tvastr runner reads the local files.
5. The runner sends the document contents to the Tvastr backend.
6. Tvastr generates a mockup with structured product context.
7. Tvastr returns a local `.mockup.html` file and/or a published link.
8. The PM opens the mockup in the browser.
9. The PM checks whether the generated flow matches product intent.
10. The PM edits copy, priorities, acceptance criteria, requirement labels, and comments.
11. The PM shares the mockup link with the designer and developer.

### What The PM Communicates

- This is the flow we want.
- This requirement is P0.
- This requirement is optional.
- This screen is wrong because the user goal is different.
- These are the edge cases.
- This version is ready for design review.
- This version is ready for dev review.

## Designer Flow

### Tools

The designer may use:

- Tvastr web editor
- Figma
- FigJam
- screenshots
- paper or pencil
- optional API key for AI edits

### Actions

1. The designer receives a Tvastr mockup link.
2. They open it in the browser.
3. They see the generated screens immediately.
4. They click Edit.
5. They manually adjust layout, hierarchy, spacing, text, fields, colors, and visual states.
6. They add missing states such as empty, loading, error, success, permission denied, and mobile.
7. They add annotations explaining design decisions.
8. If they prefer Figma, they can export to Figma or recreate/refine there.
9. If they prefer manual tools, they can sketch separately and reflect the decisions back into Tvastr.
10. If they want AI help, they can bring an API key and ask for targeted changes.
11. They mark screens or flows as design reviewed.

### Optional AI Edit Examples

```text
Make this screen feel more like a serious B2B SaaS settings page.
```

```text
Add a mobile version of this flow.
```

```text
Create an empty state for no search results.
```

```text
Make the hierarchy clearer without changing the underlying requirements.
```

### What The Designer Communicates

- I changed this layout because it better supports the user goal.
- This interaction pattern should be used here.
- This state was missing.
- This component should behave like this.
- This is ready for development.
- I edited this in Tvastr.
- I exported this to Figma.
- I kept Figma as the visual source, but Tvastr has the structured handoff context.

## Developer Flow

### Tools

The developer may use:

- Tvastr mockup link
- GitHub or GitLab
- local repo
- Cursor
- Claude Code
- Codex
- Copilot
- Storybook
- existing design system or component library
- Tvastr MCP/API endpoint

### Actions

1. The developer receives the Tvastr mockup link.
2. They open it in the browser to understand the product flow.
3. They review requirements, states, annotations, acceptance criteria, and design rationale.
4. They add feasibility notes when needed.
5. They identify missing backend/API dependencies.
6. They map mockup components to existing code components where possible.
7. They give the link to their AI coding agent.

Example:

```text
Read this Tvastr mockup spec and implement it in this repo:
https://tvastr.app/m/abc123
```

8. The agent reads structured Tvastr context.
9. The agent proposes or creates an implementation.
10. The developer reviews the code.
11. The developer opens a PR.
12. The PR links back to the Tvastr mockup.
13. Implementation notes, deviations, or blockers are reflected back into Tvastr.

### What The Developer Communicates

- This needs a new API.
- This component already exists.
- This component needs to be created.
- This design is expensive because of this technical constraint.
- This requirement is blocked.
- This was implemented in PR #123.
- The shipped implementation differs from the mockup here and here.

## AI Coding Agent Flow

### Tools

The AI coding agent may be:

- Codex
- Claude Code
- Cursor
- Copilot
- another MCP-compatible agent

### Actions

1. The developer gives the agent a Tvastr link.
2. The agent calls the Tvastr agent-readable endpoint.
3. The endpoint returns structured context.
4. The agent reads the local repo.
5. The agent maps mockup concepts to existing code patterns.
6. The agent generates an implementation plan.
7. The agent writes code.
8. The agent reports requirement coverage.

Example agent output:

```text
Implemented:
- REQ-1: Search input
- REQ-2: Search results table
- REQ-4: Empty state

Blocked:
- REQ-3: Suggestions API. No backend endpoint exists yet.
```

### What The Agent Needs From Tvastr

The agent needs more than pixels.

It needs:

- what screens exist
- how screens connect
- what each component represents
- which requirement each component satisfies
- why important design decisions were made
- what states must be implemented
- what acceptance criteria apply
- what annotations exist
- what is unresolved
- which implementation hints are available
- which design tokens and component mappings exist

## Communication Model

Tvastr should not replace everyone's tools. It should connect them.

```text
PM local PRD
  -> Tvastr local runner
  -> Tvastr mockup link
  -> Designer edits in browser or Figma
  -> Developer reviews and maps feasibility
  -> AI coding agent builds from structured context
  -> PR links back to mockup
```

The central communication object is the mockup spec.

It contains:

- requirements
- screens
- flows
- components
- comments
- decisions
- open questions
- acceptance criteria
- design states
- code mappings
- version approvals

The goal is that nobody has to ask:

> Where was that decided?

The answer should always be:

> In the Tvastr mockup spec, attached to the exact requirement, screen, or component.

## Local File Access Model

The browser app does not read local files directly.

Local files are read only by a user-invoked local runner.

Supported local runners:

1. CLI
2. MCP server
3. editor extension
4. agent tool integration

### CLI Flow

```bash
npx tvastr mockup ./prd.md --design ./design-notes.md --publish
```

```text
Local file -> CLI reads file -> backend generates mockup -> browser link returned
```

### MCP Flow

The user asks their agent:

```text
Use Tvastr to create a mockup from ./prd.md and publish it.
```

The agent calls a local tool:

```json
{
  "tool": "tvastr.create_mockup",
  "prdPaths": ["./prd.md"],
  "designPaths": ["./design-notes.md"],
  "publish": true
}
```

The tool:

1. Reads the files locally.
2. Sends the content to Tvastr.
3. Receives mockup data.
4. Writes a local artifact if requested.
5. Returns the published link.

### Web Fallbacks

The web app can still support secondary input methods:

- drag and drop PRD
- paste PRD text
- connect Google Docs
- connect Notion
- import from GitHub

But these should be fallback options, not the native wedge.

The native wedge is:

> Run Tvastr where your PRD already lives.

## Strategic Principle

Tvastr should feel like infrastructure around the user's existing workflow, not another place where work has to start.

The cleanest mental model:

```text
Created locally.
Reviewed visually.
Edited by humans.
Consumed by agents.
```

The mockup is not merely a screen. It is a living, structured product agreement that humans can inspect and agents can implement.
