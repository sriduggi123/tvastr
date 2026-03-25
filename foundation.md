# Foundation Document

## What Is This?

A skill (invoked as `/mockup`) that generates self-contained HTML files from a PM's PRD and design guide. These HTML files are simultaneously:

1. **A visual mockup** of the screen/flow
2. **A structured data store** carrying design rationale, PRD traceability, and component mapping
3. **A lightweight visual editor** that non-technical users can use to modify the design
4. **An annotation layer** for cross-team communication
5. **A machine-readable artifact** that AI agents can parse and act on

One file. No server. No build step. No dependencies.

---

## The Problem

Today, the journey from idea to code looks like this:

```
PRD (doc) → Design (Figma) → Handoff (meetings, comments) → Code
```

Context leaks at every handoff. The developer doesn't know *why* the designer chose that layout. The designer doesn't know *which* PRD requirement drove that field. The AI coding agent gets a ticket with half the context missing.

**This tool collapses the entire chain into a single artifact** — an HTML file that carries the what, the why, and the how, readable by both humans and machines.

---

## Who Uses It and Why

### PM (Product Manager)
- **Creates** mockups by running `/mockup` with a PRD and design guide as input
- **Annotates** with priorities, requirement clarifications, acceptance criteria
- **Iterates** by asking the AI to update the mockup based on feedback
- **Does not use git.** Shares files via Slack, email, or shared drives.

### Designer
- **Visually edits** the mockup directly in the browser — changes colors, adds fields, adjusts spacing, replaces text
- **Annotates** with design rationale, accessibility notes, responsive behavior guidance
- **Does not use git.** Shares files via Slack, email, or shared drives.

### Developer
- **Reads** the mockup to understand what to build and why
- **Annotates** with feasibility notes, technical constraints, questions
- **Commits** the file to the repo
- **Uses git** as the sharing layer

### AI Agent (Claude Code / Codex / Cowork)
- **Reads** the HTML file and parses the embedded structured data
- **Modifies** the mockup based on user instructions
- **Generates code** from the mockup's structured context
- **Reads/writes** directly to the file via CLI

---

## The HTML File

Every generated mockup is a single `.mockup.html` file. When opened in a Chromium-based browser, it renders the visual mockup. When read as a file, it contains structured data that AI agents can parse.

### Structure

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="generator" content="mockup-skill">
  <title>[Feature Name] Mockup</title>
  <style>
    /* All styles inline — no external dependencies */
    /* Mockup styles */
    /* Editor panel styles */
    /* Annotation styles */
  </style>
</head>
<body>

  <!-- ============ MOCKUP ============ -->
  <div id="mockup">
    <!-- The visual mockup lives here -->
    <!-- Every significant element has a data-component attribute -->
    <!-- linking it to the structured context below -->
  </div>

  <!-- ============ EDITOR PANEL ============ -->
  <div id="editor-panel" hidden>
    <!-- Built-in visual editor (toggle with Edit button) -->
    <!-- Properties: text, color, font, spacing, visibility -->
    <!-- Add/remove element controls -->
    <!-- Save button (File System Access API) -->
  </div>

  <!-- ============ ANNOTATIONS PANEL ============ -->
  <div id="annotations-panel" hidden>
    <!-- Annotation viewer/creator -->
    <!-- Click element → add note -->
    <!-- Filter by author role (PM/Designer/Developer/AI) -->
  </div>

  <!-- ============ STRUCTURED CONTEXT ============ -->
  <script type="application/json" id="mockup-context">
  {
    "meta": {
      "version": "1.0",
      "created": "2025-01-15T10:30:00Z",
      "lastModified": "2025-01-16T14:22:00Z",
      "prdSource": "features/search-v2.md",
      "designGuide": "design-system/guide.md"
    },
    "components": [
      {
        "id": "search-bar",
        "element": "[data-component='search-bar']",
        "prdRequirement": "REQ-42: Users must be able to search by keyword",
        "designRationale": "Full-width search bar for discoverability, auto-suggest enabled",
        "acceptanceCriteria": [
          "Debounced input (300ms)",
          "Shows top 5 suggestions",
          "Keyboard navigable"
        ],
        "designTokens": {
          "height": "48px",
          "borderRadius": "8px",
          "fontSize": "16px"
        }
      }
    ],
    "annotations": [
      {
        "id": "ann-1",
        "targetComponent": "search-bar",
        "author": "PM",
        "timestamp": "2025-01-15T11:00:00Z",
        "text": "This is P0 for launch. Must support mobile.",
        "type": "requirement"
      },
      {
        "id": "ann-2",
        "targetComponent": "search-bar",
        "author": "Designer",
        "timestamp": "2025-01-15T15:30:00Z",
        "text": "Changed border-radius from 4px to 8px to match new design system.",
        "type": "design-change"
      },
      {
        "id": "ann-3",
        "targetComponent": "search-bar",
        "author": "Developer",
        "timestamp": "2025-01-16T09:00:00Z",
        "text": "Auto-suggest requires a new API endpoint. ~2 day effort.",
        "type": "feasibility"
      }
    ],
    "changelog": [
      {
        "timestamp": "2025-01-15T10:30:00Z",
        "author": "AI",
        "action": "Generated initial mockup from PRD"
      },
      {
        "timestamp": "2025-01-15T15:30:00Z",
        "author": "Designer",
        "action": "Updated search bar styling, added filter chips"
      }
    ]
  }
  </script>

  <!-- ============ EDITOR + ANNOTATION LOGIC ============ -->
  <script>
    /* All JS inline — no external dependencies */

    // === EDIT MODE ===
    // - Toggle with Edit button or keyboard shortcut
    // - Click any element to select it (blue outline)
    // - Properties panel shows: text, bg color, font size,
    //   padding, margin, border-radius, visibility
    // - "Add Element" menu: button, input, text, image, divider
    // - "Delete Selected" button
    // - Changes update the DOM live

    // === ANNOTATION MODE ===
    // - Toggle with Annotate button
    // - Click any element to attach a note
    // - Select your role (PM/Designer/Developer)
    // - Notes stored in the JSON context block
    // - Visual indicators on annotated elements

    // === SAVE ===
    // - Uses File System Access API (Chromium only)
    // - window.showSaveFilePicker() to write back to the same file
    // - Serializes current DOM state + updated JSON context
    // - One click. No download dialog. File updates in place.

    // === AI INTEROP ===
    // - AI reads/writes the <script type="application/json"> block
    // - AI can also modify the HTML/CSS directly
    // - The structured context is the contract between humans and AI
  </script>

</body>
</html>
```

---

## The Built-In Editor

When the designer (or anyone) clicks "Edit", a panel appears with visual controls. This is NOT a developer tool — it's a simplified property editor.

### What the designer can do:

| Action | How |
|--------|-----|
| Change text | Click the element, type directly (contenteditable) |
| Change colors | Select element → color picker in panel |
| Change spacing | Select element → padding/margin sliders |
| Change font size | Select element → font size dropdown |
| Add a new element | "Add" menu → select type → click where to place it |
| Delete an element | Select → press Delete or click "Remove" |
| Reorder elements | Drag and drop within the mockup |
| Hide/show elements | Select → toggle visibility |
| Save changes | Click "Save" → file updates on disk |

### What it does NOT do:

- No layers panel. This is not Figma.
- No pixel-perfect positioning. Elements follow document flow.
- No responsive design tools. The mockup targets one viewport.
- No asset management. Images are placeholders or data URIs.

The goal is **just enough editing power** for a designer to refine a mockup, not to replace their design tool.

---

## The Annotation System

Annotations are first-class data, not throwaway comments.

### Annotation structure:

```json
{
  "id": "ann-1",
  "targetComponent": "search-bar",
  "author": "Designer",
  "timestamp": "2025-01-15T15:30:00Z",
  "text": "Changed border-radius from 4px to 8px to match new design system.",
  "type": "design-change"
}
```

### Annotation types:

| Type | Used by | Purpose |
|------|---------|--------|
| `requirement` | PM | Links to PRD requirement, sets priority |
| `design-change` | Designer | Explains why a visual change was made |
| `design-rationale` | Designer | Explains the thinking behind a design choice |
| `feasibility` | Developer | Flags technical constraints or effort estimates |
| `question` | Anyone | Asks for clarification |
| `ai-suggestion` | AI | Proposes alternatives or flags inconsistencies |

### Visual representation:

- Annotated elements show a small colored dot (role-coded: blue for PM, purple for Designer, green for Developer, orange for AI)
- Hovering the dot shows the annotation
- The annotations panel lists all annotations, filterable by role and type

---

## Sharing Model

There is no single sharing mechanism. The system meets users where they are.

### Non-technical users (PM, Designer):

```
Edit in browser → Save to disk → Share via Slack / email / Google Drive
```

They never touch git. The file is just a file. They share it like they share any other file.

### Technical users (Developer):

```
Receive file → Commit to repo → AI reads from repo
```

The developer is the bridge between the non-git world and git.

### AI Agent:

```
Read file from repo (or from local path) → Parse JSON context → Modify HTML/JSON → Write back
```

The AI can read and write the file directly. The structured JSON context is its API.

### Full collaboration flow:

```
1. PM runs /mockup with PRD + design guide
   → AI generates feature.mockup.html
   → PM shares on Slack

2. Designer opens file in Chrome
   → Clicks Edit → modifies colors, adds fields, adjusts layout
   → Clicks Save → file updates on disk
   → Adds annotations explaining design decisions
   → Shares updated file on Slack

3. Developer downloads file from Slack
   → Opens in browser to review
   → Adds feasibility annotations
   → Commits to repo

4. AI reads file from repo
   → Parses structured context (requirements, design tokens, annotations)
   → Generates implementation code
   → Or: updates the mockup based on new instructions
```

---

## The `/mockup` Skill

### Invocation:

```
/mockup <prd-path> <design-guide-path>
```

### What it does:

1. Reads the PRD document
2. Reads the design guide / design system document
3. Generates a complete `.mockup.html` file containing:
   - Visual mockup matching the PRD requirements and design guide
   - Structured JSON context with component mapping, PRD traceability, and design tokens
   - Built-in editor (JS/CSS, all inline)
   - Annotation system (JS/CSS, all inline)
4. Writes the file to the current directory

### What it needs:

- A PRD document (markdown, text, or any readable format)
- A design guide or design system document (optional but recommended)
- That's it. No config, no setup, no dependencies.

---

## Principles

1. **One file.** Everything lives in a single HTML file. No external CSS, no JS libraries, no server, no build step.

2. **Context is data.** Design rationale, PRD requirements, and annotations are structured JSON — not scattered across Figma comments, Jira tickets, and Slack threads.

3. **The browser is the UI.** No custom app to install. Open the HTML file in Chrome. That's it.

4. **AI-native.** The structured JSON context is designed for AI consumption. An AI agent can read a mockup file and understand not just what the UI looks like, but why it looks that way and what requirements it satisfies.

5. **Meet users where they are.** PMs and designers don't use git. Developers do. The system works with both workflows, not against them.

6. **Just enough editing.** The built-in editor enables refinement, not creation from scratch. The AI generates the mockup. Humans refine it. The AI reads the refinements and generates code.

7. **No lock-in.** It's an HTML file. You can open it in any browser, read it in any editor, parse it with any tool. If this skill disappears tomorrow, your mockups still work.
