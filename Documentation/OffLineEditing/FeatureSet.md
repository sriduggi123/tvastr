# Offline Embedded Editing FeatureSet

Draft date: 2026-05-20

Source context: `TvastrPrimitivesFoundation.md`

## 1. Feature Promise

Offline Embedded Editing lets a designer open a generated `.mockup.html` artifact directly in a browser, enter edit mode inside that same file, refine the mockup UI, and leave with an updated `.mockup.html` artifact that is still portable, readable, valid, and sync-ready.

The designer should feel like they are editing the mockup itself, not maintaining HTML. The artifact should still remain honest HTML/CSS/SVG/vanilla JavaScript with embedded `tvastr-context`, stable IDs, variant metadata, audit history, and validation signals.

## 2. End Result Output

The output of this feature is one self-editing `.mockup.html` artifact.

The artifact should:

- open in a modern browser without a build step, package install, login, or required network access
- render the current mockup in review mode by default
- include an embedded edit mode that can be toggled on by the user
- allow visual, copy, layout, state, variant, annotation, and context edits
- preserve all screens, states, variants, interactions, and traceability inside the same file
- show only one active screen/state/variant combination at a time
- save or export a new `.mockup.html` file after edits
- keep `tvastr-context` parseable and aligned with the visible DOM
- preserve sync metadata when the artifact came from a hosted mockup
- remain useful as a local-only artifact even when it is never synced

## 3. Primary Designer Outcome

A designer should be able to receive a generated artifact, open it, and confidently fix the things designers normally catch after generation:

- copy that feels wrong
- hierarchy that needs adjustment
- missing loading, empty, error, success, OTP, 2FA, disabled, or permission states
- color or token choices that do not match the product feel
- layout spacing and alignment issues
- missing annotations or implementation notes
- unclear interactions between screens, modals, and states
- broken or incomplete requirement coverage

The feature succeeds when a designer can correct the artifact without needing Figma, an AI agent, a hosted Tvastr session, or raw-code editing.

## 4. Designer Capabilities

### 4.1 Open and Review

The designer can open the `.mockup.html` file and immediately see the active mockup view. Review mode should be clean and not expose editor controls until the user enters edit mode.

### 4.2 Enter Embedded Edit Mode

The artifact includes its own edit controls. Entering edit mode should not require server state. If the artifact has permission metadata from a hosted source, that metadata can inform warnings or sync behavior, but offline edit mode should still be locally usable.

### 4.3 Select Meaningful Elements

The designer can click meaningful UI elements and see what they are editing:

- screen
- state
- component
- group
- modal
- field
- button
- table
- card
- annotation
- requirement mapping

Selection should prefer stable `data-*` IDs that map visible DOM elements to `tvastr-context`.

### 4.4 Edit Copy

The designer can edit headings, labels, body copy, helper text, placeholder text, button text, error text, empty-state text, modal text, toast text, and review annotations.

Copy editing should support both inline editing and property-panel editing.

### 4.5 Edit Layout

The designer can make practical mockup-level layout changes:

- reorder components within a screen or group
- duplicate a component
- remove or hide a component
- resize supported components
- adjust alignment
- adjust spacing
- group or ungroup simple component clusters
- move a component between supported containers

This is not intended to become a freeform infinite canvas. The purpose is to refine structured product mockups and handoff context.

### 4.6 Edit Style

The designer can adjust:

- color
- typography
- spacing
- alignment
- size
- border
- radius
- shadow
- visibility
- responsive hints
- presentation variants such as theme, density, or color treatment

When named design tokens exist, the editor should prefer token-aware editing. When tokens do not exist, local overrides are allowed.

### 4.7 Manage Screens

The designer can:

- switch screens
- rename screens
- reorder screens in a flow
- duplicate screens
- add a screen from a starter template
- remove or mark a screen as deferred
- define simple transitions between screens

### 4.8 Manage States and Variants

States and variants are first-class editing objects, not hidden DOM tricks.

The designer can add, edit, rename, duplicate, remove, or mark as deferred:

- default
- loading
- empty
- error
- disabled
- permission denied
- OTP
- 2FA
- locked account
- success
- validation
- modal open or closed
- long-content
- mobile or responsive
- color/theme
- density
- representation variants

The editor must make these variants accessible without showing all of them at once.

### 4.9 Edit Interactions

The designer can define simple prototype behavior:

- click opens a modal
- click closes a modal
- click navigates to another screen
- click switches to another state
- submit shows loading
- submit shows error
- submit shows success
- OTP failure shows validation state
- account issue shows locked-account or permission-denied state

These interactions should be represented in embedded vanilla JavaScript and in structured context.

### 4.10 Annotate and Explain

The designer can add or edit:

- design notes
- implementation notes
- requirements notes
- decision records
- open questions
- component mapping hints
- traceability notes

Annotations should attach to stable entities such as screens, states, components, requirements, or versions.

## 5. State and Variant Model

### 5.1 Core Rule: One Active Surface

The artifact may contain many screens, states, and presentation variants, but the canvas should show exactly one active combination at a time.

The active view is:

```text
Flow -> Screen -> State/Variant -> Viewport
```

Example:

```text
Flow: Login
Screen: Sign In
State/Variant: Error
Viewport: Desktop
```

The designer should feel:

```text
I am editing the login screen in its error state.
Now I switch to OTP.
Now I switch to locked account.
Now I switch the color variant.
```

They should not see twelve duplicated screens stacked on one page unless a later compare mode is explicitly added.

### 5.2 Variant Categories

The editor should group variants so designers can find them quickly:

| Category | Examples |
| --- | --- |
| Content states | default, empty, long-content |
| System states | loading, error, success, validation |
| Access states | disabled, permission denied, locked account |
| Auth states | OTP, 2FA |
| Presentation variants | color, theme, density, representation |
| Responsive variants | desktop, tablet, mobile |

These groups are for navigation and editing clarity. They should still resolve to one active visible view.

### 5.3 Materialized Variants for MVP

For MVP, prefer materialized variants.

Each important state or variant should exist as readable HTML in the artifact, with inactive variants hidden or stored as templates. This is less compact than a patch-based renderer, but it is much better for designers, agents, validation, and direct local editing.

Example shape:

```html
<section data-screen-id="screen_login" data-variant-id="state_default"></section>
<section data-screen-id="screen_login" data-variant-id="state_error" hidden></section>
<section data-screen-id="screen_login" data-variant-id="state_otp" hidden></section>
```

The embedded runtime should ensure only the active variant is visible.

### 5.4 Variant Registry in Context

The `tvastr-context` block should include a registry of available screens, states, and variants.

Example:

```json
{
  "screens": [
    {
      "id": "screen_login",
      "name": "Login",
      "variants": [
        { "id": "state_default", "type": "state", "name": "Default" },
        { "id": "state_loading", "type": "state", "name": "Loading" },
        { "id": "state_error", "type": "state", "name": "Error" },
        { "id": "state_otp", "type": "state", "name": "OTP" }
      ]
    }
  ],
  "activeView": {
    "flowId": "flow_login",
    "screenId": "screen_login",
    "variantId": "state_default",
    "viewport": "desktop"
  }
}
```

The visible DOM and the context registry must stay aligned.

### 5.5 Variant Switcher

Edit mode should include a clear switcher for:

- flow
- screen
- state or variant
- viewport
- theme or presentation variant where present

The switcher changes the active view. It should not cause every state to render at once.

### 5.6 Edit Scope Control

When a designer edits a variant, the editor must make scope clear.

Common scopes:

- this variant only
- all variants of this screen
- all screens in this flow
- all components using this token
- all matching components

This is critical. Designers need to know whether changing an error-state button affects only the error state or every submit button in the flow.

### 5.7 Apply Across Variants

The editor should support intentional propagation:

- apply this style to all states of this screen
- apply this copy to all variants where the same component exists
- apply this token change globally
- clone current screen into a new state
- create missing state from current state

Propagation should always be explicit.

### 5.8 Active View Persistence

The artifact should remember the last active view:

- active flow
- active screen
- active state or variant
- active viewport
- active theme or representation variant

Reopening the artifact should show the most recently saved active view.

## 6. Embedded Editor Surfaces

The embedded editor should include:

- mode toggle: review/edit
- canvas or mockup viewport
- selection outline
- element breadcrumb
- property panel
- screen and flow navigator
- state and variant switcher
- interaction editor
- annotation panel
- requirement/traceability panel
- validation panel
- save/export controls
- undo/redo within the current session

The UI should be powerful but not visually dominant. The mockup remains the main object.

## 7. First Build Slice: Embedded Mode and Core Editing

The embedded mode should be built first. The first useful editing slice should include:

- embedded edit mode shell
- select meaningful elements
- edit copy
- edit layout
- edit style

This first slice should make a generated artifact feel genuinely correctable by a designer. It does not need to solve every future editing workflow, but it must prove the central product promise: open one `.mockup.html` file, enter edit mode, select something, change it, export/save it, reopen it, and see the change preserved with context.

### 7.1 First Slice Scope

The first slice must include enough infrastructure for edits to be real:

- review/edit mode toggle
- editor chrome embedded in the artifact
- selection outline and selected-element inspector
- property controls for copy, layout, and style
- active screen/state/variant awareness
- session undo/redo
- dirty-state indicator
- export or save updated `.mockup.html`
- basic validation before export
- DOM and `tvastr-context` updates for meaningful edits
- audit entry creation for meaningful edits

State creation, deep interaction authoring, traceability editing, advanced annotation workflows, and hosted sync can follow. However, the first slice must not break or ignore existing states and variants. It must edit the currently active variant clearly.

### 7.2 Embedded Edit Mode Shell

Embedded edit mode is the editing container inside the artifact itself.

The artifact should open in review mode. The designer can turn on edit mode from a visible but quiet control. When edit mode is active, the artifact adds editor UI around or above the mockup without changing the mockup layout.

Required shell behavior:

- review mode shows the mockup without editor panels
- edit mode shows toolbar, selection outline, and property panel
- editor UI is visually distinct from the mockup UI
- editor UI does not become selectable mockup content
- editor UI can be collapsed enough to inspect the design
- active flow, screen, state/variant, and viewport are visible
- unsaved changes are clearly indicated
- Escape clears selection or exits inline editing before leaving edit mode

The editor runtime should keep a strict boundary between:

- mockup DOM
- editor chrome
- embedded `tvastr-context`
- audit/session state

Acceptance criteria:

- A designer can open the artifact offline and toggle edit mode on and off.
- Toggling edit mode does not move or resize the mockup.
- Editor controls are not confused with generated product UI.
- The active screen/state/variant is visible in the editor shell.
- The artifact can be exported after an edit and reopened with the edit preserved.

### 7.3 Select Meaningful Elements

Selection is the foundation of all visual editing.

The designer should be able to click a meaningful visible element and understand what they selected. The selected object may be a screen, section, component, text block, field, button, card, modal, table, group, or visible state container.

Selection rules:

- click selects the nearest meaningful `data-component-id` or `data-screen-id` element
- hover shows a lightweight outline without changing layout
- selected state shows a stronger outline and property panel
- nested elements use a breadcrumb so the designer can move from child to parent
- inactive variants are not selectable until the designer switches to them
- editor chrome is excluded from selection
- unmapped meaningful elements can be selected, but the editor should mark them as unmapped

The property panel for a selected element should show:

- display name
- entity type
- stable ID if present
- active screen/state/variant
- edit scope
- linked requirement IDs where present
- available edit groups: copy, layout, style

First-slice selection should support single selection. Multi-select can come later. Parent selection through breadcrumbs is enough for the first build.

Acceptance criteria:

- A designer can select common elements: heading, paragraph, button, input, card, container, and visible modal.
- Selection uses stable IDs from the artifact when available.
- The selected element is visually obvious without shifting layout.
- The property panel updates when selection changes.
- If an element has no context mapping, the editor surfaces that fact instead of pretending it is fully mapped.

### 7.4 Edit Copy

Copy editing should feel direct and forgiving.

The designer should be able to edit:

- headings
- paragraph text
- labels
- button text
- helper text
- placeholder text
- error text
- empty-state text
- modal text
- toast or alert text
- field descriptions

Editing modes:

- inline edit for visible text
- property-panel edit for text properties such as placeholder, label, helper, and error copy

Default scope:

- copy edits apply to the selected component in the active screen/state/variant only

The editor may offer explicit propagation later, such as "apply to all variants where this component appears." The first slice should avoid silent propagation.

Data behavior:

- update the visible DOM
- update the matching `tvastr-context` component copy where a mapping exists
- preserve the component ID
- add an audit entry for meaningful saved copy changes
- mark unmapped copy edits as requiring mapping review if context cannot be updated safely

Designer interaction details:

- Enter or blur commits inline text edits
- Escape cancels the active inline edit
- undo restores the previous copy
- empty copy is allowed only where the component type supports it
- copy editing should preserve simple inline formatting where practical

Acceptance criteria:

- A designer can edit a heading inline.
- A designer can edit button text inline.
- A designer can edit an input placeholder from the property panel.
- The exported artifact reopens with edited copy intact.
- The edited copy is reflected in `tvastr-context` when the element is mapped.

### 7.5 Edit Layout

Layout editing should be structured, not freeform canvas editing.

The first slice should let designers correct common mockup layout problems without pretending to be Figma. The designer should be able to adjust hierarchy, spacing, alignment, ordering, visibility, and practical sizing inside the current screen/state/variant.

Supported first-slice layout actions:

- move component up or down within its parent
- drag reorder within a supported container or reorder list
- duplicate a selected component
- hide or show a selected component
- remove a selected component with undo support
- adjust width, max width, min height, and fit behavior where supported
- adjust margin, padding, and gap
- adjust horizontal and vertical alignment
- switch simple layout direction where safe: row, column
- align a component within parent: start, center, end, stretch

Layout editing should prefer controls over arbitrary x/y dragging. Freeform drag can create fragile HTML and surprising responsive behavior. If drag exists in the first slice, it should reorder within a known parent container rather than position anywhere on the page.

Data behavior:

- update DOM order or style for the active variant
- update context ordering and component visibility where mapped
- preserve stable IDs on moved or restyled components
- create new IDs only for duplicated components
- record audit entries for meaningful saved layout changes

Default scope:

- layout edits apply to the active screen/state/variant only

Acceptance criteria:

- A designer can reorder two components in a form or card.
- A designer can hide a component and undo it.
- A designer can duplicate a button or card with a new stable ID.
- A designer can adjust spacing between visible components.
- A designer can center or align selected content.
- The exported artifact reopens with the layout changes intact.
- Context ordering or visibility is updated when mappings exist.

### 7.6 Edit Style

Style editing should let designers correct visual feel without requiring raw CSS.

The designer should be able to adjust:

- text color
- background color
- border color
- font size
- font weight
- line height
- border width
- radius
- shadow
- opacity
- spacing values exposed as style controls
- theme or token references when available

Style controls should support:

- color picker
- token picker where tokens exist
- numeric input for spacing and size
- stepper controls for common values
- reset to inherited or generated value
- clear indication of whether the edit is local override or token edit

Default scope:

- style edits apply to the selected component in the active screen/state/variant only

Token editing must be explicit. If the designer changes a global token, the editor should make clear that the change may affect multiple components, screens, or variants.

Data behavior:

- prefer CSS custom properties or structured style blocks where available
- use inline styles only when that is the safest local override
- update `tvastr-context` design token or component style metadata when mapped
- preserve readable CSS
- avoid creating minified or opaque style output
- record audit entries for meaningful saved style changes

Acceptance criteria:

- A designer can change a button background color.
- A designer can change heading size or weight.
- A designer can adjust card radius or border.
- A designer can reset a style override.
- The editor clearly distinguishes local override from token-level edit.
- The exported artifact reopens with style changes intact.

### 7.7 First-Slice State and Variant Handling

The first slice does not need full state authoring, but it must be state-aware.

Minimum behavior:

- show the current active flow, screen, state/variant, and viewport
- allow switching between variants that already exist in the artifact
- edit only the active variant by default
- preserve inactive variants when exporting
- keep `activeView` updated in `tvastr-context`
- avoid applying copy, layout, or style edits across variants unless the designer explicitly chooses that scope

This protects the earlier product decision: variants must be accessible, but only one thing should show up on the canvas.

### 7.8 First-Slice Non-Goals

The first build slice does not need to include:

- full state creation and deletion
- full interaction editor
- multi-select editing
- complex grouping logic
- traceability authoring
- approval workflows
- hosted collaboration
- CLI/MCP sync
- AI-assisted editing
- freeform absolute positioning

These should not be blocked conceptually, but they should not slow down proving the embedded editing loop.

### 7.9 First-Slice Success Test

A designer should be able to complete this loop:

1. Open a `.mockup.html` artifact offline.
2. Turn on embedded edit mode.
3. Switch to the desired existing screen/state/variant.
4. Select a heading, button, input, card, or container.
5. Edit copy.
6. Adjust layout.
7. Adjust style.
8. Undo one change.
9. Export or save the updated artifact.
10. Reopen the artifact and see the changes preserved.
11. Inspect `tvastr-context` and see mapped edits reflected there.

If this loop works, the feature has crossed from prototype to product capability.

## 8. Save, Export, and Sync Readiness

Offline embedded editing should support:

- session undo/redo
- local save where browser APIs allow it
- download/export updated `.mockup.html` where direct save is unavailable
- audit events for meaningful edits
- validation before export
- preservation of sync metadata when present
- base-version preservation for later CLI/MCP sync

The server is not required for this feature to produce value.

## 9. Validation Expectations

Before export, the artifact should validate:

- required `tvastr-context` block exists
- context JSON parses
- active view points to valid flow, screen, variant, and viewport entries
- DOM screen and variant IDs are unique
- meaningful components have stable IDs
- annotations target valid entities
- requirements and trace mappings target valid entities
- embedded JavaScript parses where practical
- no required remote dependencies were introduced
- audit log records meaningful edits

Validation should be helpful. It should guide the designer to repair broken parts instead of turning the editor into a punitive gate.

## 10. Non-Goals for This Feature

This feature is not:

- a full Figma replacement
- an infinite canvas
- a vector illustration suite
- a production code editor
- a hosted collaboration system
- a file sync product
- an AI-required workflow
- a requirement that designers use Claude Code, Codex, Cursor, Copilot, or any agent

## 11. Initial Product Decisions

- Embedded edit mode is the target direction.
- Embedded edit mode should be built before broader hosted collaboration or MCP-driven editing polish.
- The first build slice should include selection, copy editing, layout editing, and style editing.
- Offline editing should work inside the generated artifact itself.
- The artifact should show only one active screen/state/variant combination at a time.
- Variants must be accessible, navigable, editable, and preserved inside the same file.
- MVP should prefer materialized variants over patch-only variant rendering.
- Edit scope must be explicit whenever changes may affect more than the active variant.
- The artifact remains a single `.mockup.html` file by default.
- Vanilla JavaScript only for embedded runtime behavior.

## 12. Sections to Build Next

We should expand this document section by section in this order:

1. Designer workflow walkthrough for the first build slice
2. Variant and state UX details
3. Selection and property editing model
4. Layout editing model
5. Style and token editing model
6. Save/export behavior
7. Validation behavior
8. Interaction editing model
9. Annotation and traceability model
10. MVP cutline and later enhancements
