"""Parse frontend JS/HTML files to extract functions, fetch calls, and UI structure."""

import re
import os
import json
import sys
from pathlib import Path
from collections import defaultdict


SKIP_DIRS = {
    ".git",
    ".codex",
    "__pycache__",
    "venv",
    ".venv",
    "node_modules",
    "documentation",
    "Autodoc",
    "dist",
    "build",
    "original",
}


IDENTIFIER = r"[A-Za-z_$][\w$]*"
DTO_SUFFIXES = (
    "DTO",
    "Dto",
    "Request",
    "Response",
    "Payload",
    "Schema",
    "Model",
    "Props",
    "State",
    "Config",
    "Options",
    "Params",
)


def line_number(source, index):
    """Return a 1-based line number for an index into source."""
    return source[:index].count("\n") + 1


def normalize_signature(signature):
    """Collapse whitespace and remove trailing block openers from signatures."""
    signature = re.sub(r"\s+", " ", signature.strip())
    signature = signature.rstrip("{").strip()
    return signature.rstrip(";")


def is_dto_name(name):
    """Heuristic for frontend typed data shapes."""
    return bool(name) and name.endswith(DTO_SUFFIXES)


def add_unique(items, item):
    """Append item when another item with the same signature and line is not present."""
    key = (item.get("line"), item.get("signature"))
    if not any((existing.get("line"), existing.get("signature")) == key for existing in items):
        items.append(item)


def extract_imports(source):
    """Extract ES module imports and CommonJS require calls."""
    imports = []
    patterns = [
        r"(?m)^\s*import\s+[^;\n]+;?",
        r"(?m)^\s*(?:const|let|var)\s+[^=\n]+\s*=\s*require\s*\(\s*[\"'][^\"']+[\"']\s*\)\s*;?",
    ]
    for pattern in patterns:
        for match in re.finditer(pattern, source):
            add_unique(imports, {
                "line": line_number(source, match.start()),
                "statement": normalize_signature(match.group(0)),
            })
    return sorted(imports, key=lambda item: item["line"])


def extract_exports(source):
    """Extract explicit export statements."""
    exports = []
    patterns = [
        r"(?m)^\s*export\s+\{[^}]+\}\s*(?:from\s+[\"'][^\"']+[\"'])?\s*;?",
        r"(?m)^\s*export\s+default\s+[^;\n{]+;?",
        rf"(?m)^\s*export\s+(?:async\s+)?function\s+({IDENTIFIER})?[^\n{{;]*",
        rf"(?m)^\s*export\s+class\s+({IDENTIFIER})[^\n{{;]*",
        rf"(?m)^\s*export\s+interface\s+({IDENTIFIER})[^\n{{;]*",
        rf"(?m)^\s*export\s+type\s+({IDENTIFIER})[^\n;]*;?",
        rf"(?m)^\s*export\s+(?:const|let|var)\s+({IDENTIFIER})[^\n;]*;?",
    ]
    for pattern in patterns:
        for match in re.finditer(pattern, source):
            statement = normalize_signature(match.group(0))
            name = ""
            kind = "export"
            name_match = re.search(r"\b(function|class|interface|type|const|let|var)\s+(" + IDENTIFIER + r")", statement)
            if name_match:
                kind = name_match.group(1)
                if kind in ("const", "let", "var"):
                    kind = "value"
                name = name_match.group(2)
            elif statement.startswith("export default"):
                kind = "default"
                name = "default"
            elif statement.startswith("export {"):
                kind = "named"
                name = statement[len("export "):].strip()
            add_unique(exports, {
                "name": name,
                "kind": kind,
                "line": line_number(source, match.start()),
                "signature": statement,
            })
    return sorted(exports, key=lambda item: item["line"])


def extract_functions(source, filename):
    """Extract function and method declarations from JavaScript/TypeScript source."""
    functions = []

    # Match: export async function name<T>(params): Return
    function_pattern = rf"(?m)^\s*((?:export\s+)?(?:default\s+)?(?:async\s+)?function\s*({IDENTIFIER})?\s*(?:<[^>\n]+>)?\s*\([^)]*\)\s*(?::\s*[^\n{{]+)?)"
    for match in re.finditer(function_pattern, source):
        signature = normalize_signature(match.group(1))
        params_match = re.search(r"\((.*)\)", signature)
        add_unique(functions, {
            "name": match.group(2) or "default",
            "params": params_match.group(1).strip() if params_match else "",
            "line": line_number(source, match.start()),
            "is_async": "async function" in signature,
            "kind": "function",
            "signature": signature,
            "is_exported": signature.startswith("export "),
        })

    # Match: export const name: Type = async (params): Return =>
    arrow_pattern = rf"(?m)^\s*((?:export\s+)?(?:const|let|var)\s+({IDENTIFIER})\s*(?::\s*[^=\n]+)?=\s*(?:async\s*)?(?:\([^)]*\)|{IDENTIFIER})\s*(?::\s*[^=\n]+)?=>)"
    for match in re.finditer(arrow_pattern, source):
        signature = normalize_signature(match.group(1))
        params_match = re.search(r"=>|=\s*(?:async\s*)?(\([^)]*\)|" + IDENTIFIER + r")", signature)
        params = params_match.group(1).strip("() ") if params_match and params_match.group(1) else ""
        add_unique(functions, {
            "name": match.group(2),
            "params": params,
            "line": line_number(source, match.start()),
            "is_async": "async" in signature,
            "kind": "function",
            "signature": signature,
            "is_exported": signature.startswith("export "),
        })

    # Match: const name = async function optionalName(params)
    function_expr_pattern = rf"(?m)^\s*((?:export\s+)?(?:const|let|var)\s+({IDENTIFIER})\s*(?::\s*[^=\n]+)?=\s*(?:async\s+)?function\s*(?:{IDENTIFIER})?\s*\([^)]*\)\s*(?::\s*[^\n{{]+)?)"
    for match in re.finditer(function_expr_pattern, source):
        signature = normalize_signature(match.group(1))
        params_match = re.search(r"\((.*)\)", signature)
        add_unique(functions, {
            "name": match.group(2),
            "params": params_match.group(1).strip() if params_match else "",
            "line": line_number(source, match.start()),
            "is_async": "async function" in signature,
            "kind": "function",
            "signature": signature,
            "is_exported": signature.startswith("export "),
        })

    # Match class/object methods: async method(params): Return {
    method_pattern = rf"(?m)^\s{{2,}}((?:async\s+)?({IDENTIFIER})\s*\([^)]*\)\s*(?::\s*[^\n{{]+)?)\s*\{{"
    excluded = {"if", "for", "while", "switch", "catch", "function"}
    for match in re.finditer(method_pattern, source):
        name = match.group(2)
        if name in excluded or "=>" in match.group(0):
            continue
        signature = normalize_signature(match.group(1))
        params_match = re.search(r"\((.*)\)", signature)
        add_unique(functions, {
            "name": name,
            "params": params_match.group(1).strip() if params_match else "",
            "line": line_number(source, match.start()),
            "is_async": signature.startswith("async "),
            "kind": "method",
            "signature": signature,
            "is_exported": False,
        })

    return sorted(functions, key=lambda item: item["line"])


def extract_classes(source):
    """Extract class declarations."""
    classes = []
    class_pattern = rf"(?m)^\s*((?:export\s+)?(?:default\s+)?class\s+({IDENTIFIER})?(?:<[^>\n]+>)?(?:\s+extends\s+[^\n{{]+)?(?:\s+implements\s+[^\n{{]+)?)\s*\{{"
    for match in re.finditer(class_pattern, source):
        name = match.group(2) or "default"
        signature = normalize_signature(match.group(1))
        add_unique(classes, {
            "name": name,
            "line": line_number(source, match.start()),
            "kind": "dto" if is_dto_name(name) else "class",
            "signature": signature,
            "is_exported": signature.startswith("export "),
        })
    return sorted(classes, key=lambda item: item["line"])


def extract_types_and_interfaces(source):
    """Extract TypeScript type aliases and interfaces."""
    items = []
    interface_pattern = rf"(?m)^\s*((?:export\s+)?interface\s+({IDENTIFIER})(?:<[^>\n]+>)?(?:\s+extends\s+[^\n{{]+)?)\s*\{{"
    type_pattern = rf"(?m)^\s*((?:export\s+)?type\s+({IDENTIFIER})(?:<[^>\n]+>)?\s*=\s*[^\n;]*;?)"

    for match in re.finditer(interface_pattern, source):
        name = match.group(2)
        signature = normalize_signature(match.group(1))
        add_unique(items, {
            "name": name,
            "line": line_number(source, match.start()),
            "kind": "dto" if is_dto_name(name) else "interface",
            "signature": signature,
            "is_exported": signature.startswith("export "),
        })

    for match in re.finditer(type_pattern, source):
        name = match.group(2)
        signature = normalize_signature(match.group(1))
        add_unique(items, {
            "name": name,
            "line": line_number(source, match.start()),
            "kind": "dto" if is_dto_name(name) else "type",
            "signature": signature,
            "is_exported": signature.startswith("export "),
        })

    return sorted(items, key=lambda item: item["line"])


def extract_fetch_calls(source, fetch_patterns=None):
    """Extract fetch/XHR API calls with URL patterns."""
    calls = []
    if fetch_patterns:
        fetch_func = r'(?:' + '|'.join(fetch_patterns) + r')'
    else:
        fetch_func = r'(?:auth|api)?[Ff]etch'

    # Match string literals (single/double quotes only)
    for match in re.finditer(fetch_func + r'\s*\(\s*([\'"])([^\'"]+)\1', source):
        url = match.group(2)
        line_num = source[:match.start()].count('\n') + 1
        method = "GET"
        context = source[match.start():match.start()+300]
        method_match = re.search(r'method\s*:\s*[\'"](\w+)[\'"]', context)
        if method_match:
            method = method_match.group(1).upper()
        calls.append({"url": url, "method": method, "line": line_num})

    # Match template literals (backticks) — normalize ${expressions} to *
    for match in re.finditer(fetch_func + r'\s*\(\s*`([^`]+)`', source):
        url = match.group(1)
        line_num = source[:match.start()].count('\n') + 1
        # Replace all template expressions with *
        normalized = re.sub(r'\$\{[^}]+\}', '*', url)
        method = "GET"
        context = source[match.start():match.start()+300]
        method_match = re.search(r'method\s*:\s*[\'"](\w+)[\'"]', context)
        if method_match:
            method = method_match.group(1).upper()
        calls.append({"url": normalized, "method": method, "line": line_num})

    return calls


def extract_websocket_connections(source):
    """Extract WebSocket connection URLs."""
    connections = []
    for match in re.finditer(r'new\s+WebSocket\s*\(\s*[`\'"]([^`\'"]+)[`\'"]', source):
        url = match.group(1)
        line_num = source[:match.start()].count('\n') + 1
        normalized = re.sub(r'\$\{[^}]+\}', '*', url)
        connections.append({"url": normalized, "line": line_num})
    return connections


def extract_event_listeners(source):
    """Extract DOM event listener registrations."""
    listeners = []
    for match in re.finditer(r'addEventListener\s*\(\s*[\'"](\w+)[\'"]', source):
        event_type = match.group(1)
        line_num = source[:match.start()].count('\n') + 1
        listeners.append({"event": event_type, "line": line_num})
    return listeners


def extract_js_from_html(filepath):
    """Extract JavaScript code blocks from an HTML file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    js_blocks = []
    for match in re.finditer(r'<script[^>]*>(.*?)</script>', content, re.DOTALL):
        js_blocks.append(match.group(1))

    return "\n".join(js_blocks), content


def parse_file(filepath, base_dir, fetch_patterns=None):
    """Parse a single frontend file and return its structure."""
    rel_path = os.path.relpath(filepath, base_dir)
    ext = os.path.splitext(filepath)[1].lower()

    if ext in ('.html', '.htm'):
        js_source, full_content = extract_js_from_html(filepath)
        file_type = "html"
    elif ext in ('.js', '.jsx', '.ts', '.tsx'):
        with open(filepath, "r", encoding="utf-8") as f:
            js_source = f.read()
            full_content = js_source
        file_type = "javascript"
    else:
        return None

    result = {
        "file": filepath,
        "rel_path": rel_path,
        "type": file_type,
        "imports": extract_imports(js_source),
        "exports": extract_exports(js_source),
        "classes": extract_classes(js_source),
        "types": extract_types_and_interfaces(js_source),
        "functions": extract_functions(js_source, filepath),
        "fetch_calls": extract_fetch_calls(js_source, fetch_patterns),
        "websocket_connections": extract_websocket_connections(js_source),
        "event_listeners": extract_event_listeners(js_source),
    }

    return result


def parse_directory(root_dir, base_dir=None, fetch_patterns=None):
    """Parse all frontend files in a directory tree."""
    if base_dir is None:
        base_dir = root_dir

    frontend_extensions = {'.html', '.htm', '.js', '.jsx', '.ts', '.tsx'}
    all_data = {}

    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for filename in sorted(filenames):
            ext = os.path.splitext(filename)[1].lower()
            if ext in frontend_extensions:
                filepath = os.path.join(dirpath, filename)
                rel_path = os.path.relpath(filepath, base_dir)
                data = parse_file(filepath, base_dir, fetch_patterns)
                if data:
                    all_data[rel_path] = data

    return all_data


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parse_frontend.py <directory>")
        sys.exit(1)

    target_dir = sys.argv[1]
    base_dir = os.path.dirname(target_dir.rstrip("/"))
    result = parse_directory(target_dir, base_dir)
    print(json.dumps(result, indent=2, default=str))
