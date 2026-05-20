# Hermes Instructions

<!-- AUTODOC HOOK START -->
## Autodoc Hook

The project-local Codex hook at `.codex/hooks/autodoc-post-tool-use.py` regenerates deterministic documentation after Codex `Edit`, `Write`, and `Bash` events when relevant source files change.

Read these generated indexes before changing code:

- `Autodoc/MASTER_INDEX.md` - project overview, API contract, config, and Markdown headings
- `Autodoc/backend/INDEX.md` - Python imports, exports/public symbols, constants, DTO-like classes, class/function signatures, methods, routes, and cross-module calls
- `Autodoc/frontend/INDEX.md` - frontend imports, exports, classes, functions, TypeScript types/interfaces/DTO-like shapes, API calls, WebSockets, and event listeners

Do not hand-edit `Autodoc/**`; change source files or run `python3 scripts/generate_docs.py <project-root>` to refresh the generated docs.

When adding code, keep function, class, type, interface, DTO, import, and export signatures clear enough for the autodoc parser to capture them.
<!-- AUTODOC HOOK END -->
