# Backend Index

*Auto-generated from source code. Do not edit the auto-generated sections.*

Each file section lists imports, exports/public symbols, DTO-like typed data, classes, methods, and functions with signatures.

## `scripts/`

### `generate_docs.py`
> Generate tiered documentation indexes from source code using AST parsing, regex, and ctags.

**Imports:**
- `import os` (line 4)
- `import sys` (line 5)
- `import re` (line 6)
- `import json` (line 7)
- `import argparse` (line 8)
- `from pathlib import Path` (line 9)
- `from collections import defaultdict` (line 10)
- `from parse_python import parse_directory as parse_python_dir, group_by_folder` (line 16)
- `from parse_frontend import parse_directory as parse_frontend_dir` (line 17)
- `from parse_other import parse_directory as parse_other_dir` (line 18)

**Public symbols:**
- `SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))` _constant_ (line 13)
- `DEFAULT_BACKEND_CANDIDATES = ['app', 'src', 'backend']` _constant_ (line 22)
- `DEFAULT_FRONTEND_CANDIDATES = ['static', 'frontend', 'client']` _constant_ (line 23)
- `DEFAULT_OUTPUT_DIR = 'Autodoc'` _constant_ (line 24)
- `DEFAULT_FETCH_PATTERNS = ['fetch']` _constant_ (line 25)
- `def load_config(project_root)` _function_ (line 28)
- `def resolve_paths(project_root, config)` _function_ (line 58)
- `def get_project_root()` _function_ (line 67)
- `PROJECT_ROOT = get_project_root()` _constant_ (line 75)
- `CONFIG = load_config(PROJECT_ROOT)` _constant_ (line 76)
- `DOC_DIR, BACKEND_PATHS, FRONTEND_PATHS = resolve_paths(PROJECT_ROOT, CONFIG)` _constant_ (line 77)
- `BACKEND_INDEX = os.path.join(DOC_DIR, 'backend', 'INDEX.md')` _constant_ (line 79)
- `FRONTEND_INDEX = os.path.join(DOC_DIR, 'frontend', 'INDEX.md')` _constant_ (line 80)
- `MASTER_INDEX = os.path.join(DOC_DIR, 'MASTER_INDEX.md')` _constant_ (line 81)
- `HAND_WRITTEN_START = '<!-- HAND-WRITTEN START -->'` _constant_ (line 84)
- `HAND_WRITTEN_END = '<!-- HAND-WRITTEN END -->'` _constant_ (line 85)
- `AUTODOC_INSTRUCTIONS_START = '<!-- AUTODOC HOOK START -->'` _constant_ (line 86)
- `AUTODOC_INSTRUCTIONS_END = '<!-- AUTODOC HOOK END -->'` _constant_ (line 87)
- `CORE_INSTRUCTION_TARGETS = {'AGENTS.md': '# Project Instructions', 'CLAUDE.md': '# Claude Instructions', 'HERMES.md': '# Hermes Instructions', '.claude/rules/autodoc.md': '# Aut...` _constant_ (line 89)
- `OPTIONAL_INSTRUCTION_FILES = ('GEMINI.md', 'rules.md', '.cursorrules', '.windsurfrules')` _constant_ (line 95)
- `def preserve_hand_written(filepath)` _function_ (line 103)
- `def unique_by(items, fields)` _function_ (line 120)
- `def append_signature_list(lines, title, items, empty_text=None)` _function_ (line 133)
- `def build_autodoc_instruction_block()` _function_ (line 149)
- `def upsert_marked_block(content, block)` _function_ (line 168)
- `def discover_instruction_targets()` _function_ (line 184)
- `def sync_instruction_files()` _function_ (line 202)
- `def generate_backend_index(python_data)` _function_ (line 220)
- `def generate_frontend_index(frontend_data)` _function_ (line 347)
- `def generate_api_contract(python_data, frontend_data)` _function_ (line 468)
- `def generate_other_index(other_data)` _function_ (line 534)
- `def generate_master_index(python_data, frontend_data, other_data)` _function_ (line 596)
- `def main()` _function_ (line 667)

**Module constants / assignments:**
- `SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))` (line 13)
- `DEFAULT_BACKEND_CANDIDATES = ['app', 'src', 'backend']` (line 22)
- `DEFAULT_FRONTEND_CANDIDATES = ['static', 'frontend', 'client']` (line 23)
- `DEFAULT_OUTPUT_DIR = 'Autodoc'` (line 24)
- `DEFAULT_FETCH_PATTERNS = ['fetch']` (line 25)
- `PROJECT_ROOT = get_project_root()` (line 75)
- `CONFIG = load_config(PROJECT_ROOT)` (line 76)
- `DOC_DIR, BACKEND_PATHS, FRONTEND_PATHS = resolve_paths(PROJECT_ROOT, CONFIG)` (line 77)
- `BACKEND_INDEX = os.path.join(DOC_DIR, 'backend', 'INDEX.md')` (line 79)
- `FRONTEND_INDEX = os.path.join(DOC_DIR, 'frontend', 'INDEX.md')` (line 80)
- `MASTER_INDEX = os.path.join(DOC_DIR, 'MASTER_INDEX.md')` (line 81)
- `HAND_WRITTEN_START = '<!-- HAND-WRITTEN START -->'` (line 84)
- `HAND_WRITTEN_END = '<!-- HAND-WRITTEN END -->'` (line 85)
- `AUTODOC_INSTRUCTIONS_START = '<!-- AUTODOC HOOK START -->'` (line 86)
- `AUTODOC_INSTRUCTIONS_END = '<!-- AUTODOC HOOK END -->'` (line 87)
- `CORE_INSTRUCTION_TARGETS = {'AGENTS.md': '# Project Instructions', 'CLAUDE.md': '# Claude Instructions', 'HERMES.md': '# Hermes Instructions', '.claude/rules/autodoc.md': '# Aut...` (line 89)
- `OPTIONAL_INSTRUCTION_FILES = ('GEMINI.md', 'rules.md', '.cursorrules', '.windsurfrules')` (line 95)

**Functions:**
- `def load_config(project_root)` (line 28)
  > Load autodoc.json from project root, falling back to auto-detection.
- `def resolve_paths(project_root, config)` (line 58)
  > Resolve config values to paths.
- `def get_project_root()` (line 67)
- `def preserve_hand_written(filepath)` (line 103)
  > Read existing file and extract hand-written sections to preserve.
- `def unique_by(items, fields)` (line 120)
  > Return items with duplicate field tuples removed while preserving order.
- `def append_signature_list(lines, title, items, empty_text=None)` (line 133)
  > Append a Markdown section for items with signature and line fields.
- `def build_autodoc_instruction_block()` (line 149)
  > Generate the instruction block shared by Codex, Claude, and other agents.
- `def upsert_marked_block(content, block)` (line 168)
  > Insert or replace the generated autodoc instruction block in a file.
- `def discover_instruction_targets()` (line 184)
  > Find instruction files that should mention the autodoc hook.
- `def sync_instruction_files()` (line 202)
  > Ensure app instruction files include the autodoc hook guidance.
- `def generate_backend_index(python_data)` (line 220)
  > Generate backend/INDEX.md from parsed Python data.
- `def generate_frontend_index(frontend_data)` (line 347)
  > Generate frontend/INDEX.md from parsed frontend data.
- `def _normalize_api_path(path)` (line 457)
  > Normalize an API path for matching: strip prefixes, replace params with *.
- `def generate_api_contract(python_data, frontend_data)` (line 468)
  > Generate the API contract mapping between backend routes and frontend calls.
- `def generate_other_index(other_data)` (line 534)
  > Generate a section for config and other files.
- `def generate_master_index(python_data, frontend_data, other_data)` (line 596)
  > Generate MASTER_INDEX.md combining all sources.
- `def main()` (line 667)
  > Run all parsers and generate documentation indexes.

**Calls to other modules:**
- `load_config` -> `json.json.load`
- `load_config` -> `os.os.path.abspath`
- `load_config` -> `os.os.path.basename`
- `load_config` -> `os.os.path.exists`
- `load_config` -> `os.os.path.isdir`
- `load_config` -> `os.os.path.join`
- `resolve_paths` -> `os.os.path.join`
- `get_project_root` -> `argparse.argparse.ArgumentParser`
- `get_project_root` -> `os.os.path.abspath`
- `get_project_root` -> `os.os.path.dirname`
- `preserve_hand_written` -> `os.os.path.exists`
- `preserve_hand_written` -> `re.re.escape`
- `preserve_hand_written` -> `re.re.search`
- `upsert_marked_block` -> `re.re.escape`
- `upsert_marked_block` -> `re.re.search`
- `upsert_marked_block` -> `re.re.sub`
- `discover_instruction_targets` -> `pathlib.Path`
- `discover_instruction_targets` -> `os.os.path.exists`
- `discover_instruction_targets` -> `os.os.path.isdir`
- `discover_instruction_targets` -> `os.os.path.join`
- `sync_instruction_files` -> `pathlib.Path`
- `generate_backend_index` -> `parse_python.group_by_folder`
- `generate_backend_index` -> `os.os.path.basename`
- `generate_frontend_index` -> `collections.defaultdict`
- `_normalize_api_path` -> `re.re.sub`
- `generate_master_index` -> `parse_python.group_by_folder`
- `generate_master_index` -> `os.os.path.basename`
- `main` -> `os.os.makedirs`
- `main` -> `os.os.path.isdir`
- `main` -> `os.os.path.join`
- `main` -> `parse_frontend.parse_frontend_dir`
- `main` -> `parse_other.parse_other_dir`
- `main` -> `parse_python.parse_python_dir`

### `parse_frontend.py`
> Parse frontend JS/HTML files to extract functions, fetch calls, and UI structure.

**Imports:**
- `import re` (line 3)
- `import os` (line 4)
- `import json` (line 5)
- `import sys` (line 6)
- `from pathlib import Path` (line 7)
- `from collections import defaultdict` (line 8)

**Public symbols:**
- `SKIP_DIRS = {'.git', '.codex', '__pycache__', 'venv', '.venv', 'node_modules', 'documentation', 'Autodoc', 'dist', 'build', 'original'}` _constant_ (line 11)
- `IDENTIFIER = '[A-Za-z_$][\\w$]*'` _constant_ (line 26)
- `DTO_SUFFIXES = ('DTO', 'Dto', 'Request', 'Response', 'Payload', 'Schema', 'Model', 'Props', 'State', 'Config', 'Options', 'Params')` _constant_ (line 27)
- `def line_number(source, index)` _function_ (line 43)
- `def normalize_signature(signature)` _function_ (line 48)
- `def is_dto_name(name)` _function_ (line 55)
- `def add_unique(items, item)` _function_ (line 60)
- `def extract_imports(source)` _function_ (line 67)
- `def extract_exports(source)` _function_ (line 83)
- `def extract_functions(source, filename)` _function_ (line 121)
- `def extract_classes(source)` _function_ (line 193)
- `def extract_types_and_interfaces(source)` _function_ (line 210)
- `def extract_fetch_calls(source, fetch_patterns=None)` _function_ (line 241)
- `def extract_websocket_connections(source)` _function_ (line 276)
- `def extract_event_listeners(source)` _function_ (line 287)
- `def extract_js_from_html(filepath)` _function_ (line 297)
- `def parse_file(filepath, base_dir, fetch_patterns=None)` _function_ (line 309)
- `def parse_directory(root_dir, base_dir=None, fetch_patterns=None)` _function_ (line 342)

**Module constants / assignments:**
- `SKIP_DIRS = {'.git', '.codex', '__pycache__', 'venv', '.venv', 'node_modules', 'documentation', 'Autodoc', 'dist', 'build', 'original'}` (line 11)
- `IDENTIFIER = '[A-Za-z_$][\\w$]*'` (line 26)
- `DTO_SUFFIXES = ('DTO', 'Dto', 'Request', 'Response', 'Payload', 'Schema', 'Model', 'Props', 'State', 'Config', 'Options', 'Params')` (line 27)

**Functions:**
- `def line_number(source, index)` (line 43)
  > Return a 1-based line number for an index into source.
- `def normalize_signature(signature)` (line 48)
  > Collapse whitespace and remove trailing block openers from signatures.
- `def is_dto_name(name)` (line 55)
  > Heuristic for frontend typed data shapes.
- `def add_unique(items, item)` (line 60)
  > Append item when another item with the same signature and line is not present.
- `def extract_imports(source)` (line 67)
  > Extract ES module imports and CommonJS require calls.
- `def extract_exports(source)` (line 83)
  > Extract explicit export statements.
- `def extract_functions(source, filename)` (line 121)
  > Extract function and method declarations from JavaScript/TypeScript source.
- `def extract_classes(source)` (line 193)
  > Extract class declarations.
- `def extract_types_and_interfaces(source)` (line 210)
  > Extract TypeScript type aliases and interfaces.
- `def extract_fetch_calls(source, fetch_patterns=None)` (line 241)
  > Extract fetch/XHR API calls with URL patterns.
- `def extract_websocket_connections(source)` (line 276)
  > Extract WebSocket connection URLs.
- `def extract_event_listeners(source)` (line 287)
  > Extract DOM event listener registrations.
- `def extract_js_from_html(filepath)` (line 297)
  > Extract JavaScript code blocks from an HTML file.
- `def parse_file(filepath, base_dir, fetch_patterns=None)` (line 309)
  > Parse a single frontend file and return its structure.
- `def parse_directory(root_dir, base_dir=None, fetch_patterns=None)` (line 342)
  > Parse all frontend files in a directory tree.

**Calls to other modules:**
- `normalize_signature` -> `re.re.sub`
- `extract_imports` -> `re.re.finditer`
- `extract_exports` -> `re.re.finditer`
- `extract_exports` -> `re.re.search`
- `extract_functions` -> `re.re.finditer`
- `extract_functions` -> `re.re.search`
- `extract_classes` -> `re.re.finditer`
- `extract_types_and_interfaces` -> `re.re.finditer`
- `extract_fetch_calls` -> `re.re.finditer`
- `extract_fetch_calls` -> `re.re.search`
- `extract_fetch_calls` -> `re.re.sub`
- `extract_websocket_connections` -> `re.re.finditer`
- `extract_websocket_connections` -> `re.re.sub`
- `extract_event_listeners` -> `re.re.finditer`
- `extract_js_from_html` -> `re.re.finditer`
- `parse_file` -> `os.os.path.relpath`
- `parse_file` -> `os.os.path.splitext`
- `parse_file` -> `os.os.path.splitext(filepath)[1].lower`
- `parse_directory` -> `os.os.path.join`
- `parse_directory` -> `os.os.path.relpath`
- `parse_directory` -> `os.os.path.splitext`
- `parse_directory` -> `os.os.path.splitext(filename)[1].lower`
- `parse_directory` -> `os.os.walk`

### `parse_other.py`
> Parse non-Python, non-JS files using universal-ctags for symbol extraction.

**Imports:**
- `import subprocess` (line 3)
- `import json` (line 4)
- `import os` (line 5)
- `import sys` (line 6)
- `from collections import defaultdict` (line 7)
- `import tempfile` (line 75)

**Public symbols:**
- `HANDLED_EXTENSIONS = {'.py', '.js', '.jsx', '.ts', '.tsx', '.html', '.htm'}` _constant_ (line 11)
- `SKIP_EXTENSIONS = {'.pyc', '.pyo', '.so', '.dylib', '.dll', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.woff', '.woff2', '.ttf', '.eot', '.zip', '.tar', '.gz', '.bz2', '....` _constant_ (line 16)
- `SKIP_DIRS = {'__pycache__', 'venv', '.venv', 'node_modules', '.git', '.codex', '.pytest_cache', '.mypy_cache', '.tox', 'dist', 'build', 'documentation', 'Autodoc', 'original'}` _constant_ (line 26)
- `RELEVANT_KINDS = {'function', 'class', 'method', 'variable', 'constant', 'interface', 'type', 'enum', 'struct', 'module', 'target', 'service', 'key', 'anchor'}` _constant_ (line 33)
- `def find_ctags()` _function_ (line 40)
- `def run_ctags(directory, base_dir)` _function_ (line 54)
- `def parse_config_files(directory, base_dir)` _function_ (line 124)
- `def parse_directory(root_dir, base_dir=None)` _function_ (line 294)

**Module constants / assignments:**
- `HANDLED_EXTENSIONS = {'.py', '.js', '.jsx', '.ts', '.tsx', '.html', '.htm'}` (line 11)
- `SKIP_EXTENSIONS = {'.pyc', '.pyo', '.so', '.dylib', '.dll', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.woff', '.woff2', '.ttf', '.eot', '.zip', '.tar', '.gz', '.bz2', '....` (line 16)
- `SKIP_DIRS = {'__pycache__', 'venv', '.venv', 'node_modules', '.git', '.codex', '.pytest_cache', '.mypy_cache', '.tox', 'dist', 'build', 'documentation', 'Autodoc', 'original'}` (line 26)
- `RELEVANT_KINDS = {'function', 'class', 'method', 'variable', 'constant', 'interface', 'type', 'enum', 'struct', 'module', 'target', 'service', 'key', 'anchor'}` (line 33)

**Functions:**
- `def find_ctags()` (line 40)
  > Find the universal-ctags binary.
- `def run_ctags(directory, base_dir)` (line 54)
  > Run universal-ctags on a directory and return parsed JSON output.
- `def parse_config_files(directory, base_dir)` (line 124)
  > Parse known config file formats for structure.
- `def _parse_env_file(filepath)` (line 172)
  > Extract variable names from a .env file (not values).
- `def _parse_requirements(filepath)` (line 184)
  > Extract package names from requirements.txt.
- `def _parse_dockerfile(filepath)` (line 197)
  > Extract key directives from a Dockerfile.
- `def _parse_docker_compose(filepath)` (line 210)
  > Extract service names from docker-compose.yml.
- `def _parse_yaml_keys(filepath)` (line 227)
  > Extract top-level keys from a YAML file.
- `def _parse_toml_keys(filepath)` (line 241)
  > Extract section headers from a TOML file.
- `def _parse_gitignore(filepath)` (line 252)
  > Extract patterns from .gitignore.
- `def _parse_markdown_headings(filepath)` (line 263)
  > Extract headings from a Markdown file.
- `def _parse_ini_sections(filepath)` (line 283)
  > Extract sections from an INI/CFG file.
- `def parse_directory(root_dir, base_dir=None)` (line 294)
  > Parse all non-Python, non-JS files in a directory tree.

**Calls to other modules:**
- `find_ctags` -> `os.os.path.exists`
- `find_ctags` -> `subprocess.subprocess.run`
- `run_ctags` -> `json.json.loads`
- `run_ctags` -> `os.os.path.join`
- `run_ctags` -> `os.os.path.relpath`
- `run_ctags` -> `os.os.path.splitext`
- `run_ctags` -> `os.os.path.splitext(filename)[1].lower`
- `run_ctags` -> `os.os.unlink`
- `run_ctags` -> `os.os.walk`
- `run_ctags` -> `subprocess.subprocess.run`
- `run_ctags` -> `tempfile.tempfile.NamedTemporaryFile`
- `parse_config_files` -> `os.os.path.join`
- `parse_config_files` -> `os.os.path.relpath`
- `parse_config_files` -> `os.os.path.splitext`
- `parse_config_files` -> `os.os.path.splitext(filename)[1].lower`
- `parse_config_files` -> `os.os.walk`

### `parse_python.py`
> Parse Python files using the ast module to extract structure, docstrings, and call relationships.

**Imports:**
- `import ast` (line 3)
- `import os` (line 4)
- `import json` (line 5)
- `import sys` (line 6)
- `from pathlib import Path` (line 7)
- `from collections import defaultdict` (line 8)

**Public symbols:**
- `def get_module_docstring(tree)` _function_ (line 11)
- `def get_imports(tree)` _function_ (line 16)
- `def unparse(node)` _function_ (line 48)
- `def truncate(text, limit=180)` _function_ (line 56)
- `def format_function_signature(node)` _function_ (line 64)
- `def format_class_signature(node)` _function_ (line 71)
- `def is_public_name(name)` _function_ (line 78)
- `def extract_literal_string_list(node)` _function_ (line 83)
- `def get_assignment_targets(node)` _function_ (line 94)
- `def format_assignment_signature(node)` _function_ (line 108)
- `def is_dto_class(name, bases, decorators)` _function_ (line 113)
- `def extract_class_fields(node)` _function_ (line 135)
- `def get_decorators(node)` _function_ (line 150)
- `def get_function_calls(node)` _function_ (line 171)
- `def get_parameters(node)` _function_ (line 183)
- `def extract_router_prefixes(tree)` _function_ (line 191)
- `def parse_file(filepath)` _function_ (line 213)
- `def resolve_call_targets(file_data, all_files_data)` _function_ (line 318)
- `def extract_routes(file_data)` _function_ (line 351)
- `def parse_directory(root_dir, base_dir=None)` _function_ (line 376)
- `def group_by_folder(all_data, base_dir)` _function_ (line 402)

**Functions:**
- `def get_module_docstring(tree)` (line 11)
  > Extract the module-level docstring from an AST tree.
- `def get_imports(tree)` (line 16)
  > Extract import statements from an AST tree.
- `def unparse(node)` (line 48)
  > Safely turn an AST node back into compact source text.
- `def truncate(text, limit=180)` (line 56)
  > Keep generated signatures readable in Markdown.
- `def format_function_signature(node)` (line 64)
  > Return a Python function signature with args and return annotations.
- `def format_class_signature(node)` (line 71)
  > Return a Python class signature with bases when present.
- `def is_public_name(name)` (line 78)
  > Python convention: names without a leading underscore are public.
- `def extract_literal_string_list(node)` (line 83)
  > Extract a simple list/tuple/set of strings, such as __all__.
- `def get_assignment_targets(node)` (line 94)
  > Extract top-level assignment target names.
- `def format_assignment_signature(node)` (line 108)
  > Return a compact top-level assignment signature.
- `def is_dto_class(name, bases, decorators)` (line 113)
  > Heuristic for classes that represent typed request/response/data shapes.
- `def extract_class_fields(node)` (line 135)
  > Extract class-level fields from typed data classes and DTO-like classes.
- `def get_decorators(node)` (line 150)
  > Extract decorator names from a function or class node.
- `def get_function_calls(node)` (line 171)
  > Extract function call names from within a function body.
- `def get_parameters(node)` (line 183)
  > Extract parameter names from a function definition.
- `def extract_router_prefixes(tree)` (line 191)
  > Extract APIRouter/FastAPI router variable names and their prefix arguments.
- `def parse_file(filepath)` (line 213)
  > Parse a single Python file and return its structure.
- `def resolve_call_targets(file_data, all_files_data)` (line 318)
  > Resolve function calls to their source modules using import information.
- `def extract_routes(file_data)` (line 351)
  > Extract API route definitions from decorators, resolving router prefixes.
- `def parse_directory(root_dir, base_dir=None)` (line 376)
  > Parse all Python files in a directory tree.
- `def group_by_folder(all_data, base_dir)` (line 402)
  > Group parsed file data by their parent folder.

**Calls to other modules:**
- `get_module_docstring` -> `ast.ast.get_docstring`
- `get_imports` -> `ast.ast.walk`
- `unparse` -> `ast.ast.unparse`
- `unparse` -> `ast.ast.unparse(node).strip`
- `get_decorators` -> `ast.ast.unparse`
- `get_function_calls` -> `ast.ast.unparse`
- `get_function_calls` -> `ast.ast.walk`
- `extract_router_prefixes` -> `ast.ast.walk`
- `parse_file` -> `ast.ast.get_docstring`
- `parse_file` -> `ast.ast.iter_child_nodes`
- `parse_file` -> `ast.ast.parse`
- `parse_directory` -> `os.os.path.join`
- `parse_directory` -> `os.os.path.relpath`
- `parse_directory` -> `os.os.walk`
- `group_by_folder` -> `collections.defaultdict`
- `group_by_folder` -> `os.os.path.dirname`
