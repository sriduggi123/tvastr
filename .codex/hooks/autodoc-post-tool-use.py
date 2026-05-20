#!/usr/bin/env python3
"""Regenerate deterministic autodoc indexes after Codex edits."""

from __future__ import annotations

import json
import os
import hashlib
import subprocess
import sys
from pathlib import Path


STATE_PATH = Path(".codex") / "autodoc-state.json"
GENERATED_PREFIXES = (
    "Autodoc/",
    ".codex/memory/",
)
GENERATED_EXACT = {
    "Autodoc/MASTER_INDEX.md",
    "Autodoc/backend/INDEX.md",
    "Autodoc/frontend/INDEX.md",
}
TEXT_EXTENSIONS = {
    ".cfg",
    ".env",
    ".htm",
    ".html",
    ".ini",
    ".js",
    ".json",
    ".jsx",
    ".md",
    ".py",
    ".toml",
    ".ts",
    ".tsx",
    ".txt",
    ".yaml",
    ".yml",
}
SPECIAL_TEXT_FILES = {
    ".gitignore",
    "Dockerfile",
    "requirements.txt",
}
SKIP_DIRS = {
    ".git",
    ".codex",
    "Autodoc",
    "node_modules",
    "venv",
    ".venv",
    "__pycache__",
    "dist",
    "build",
    "original",
}


def git_root(cwd: str) -> Path | None:
    try:
        result = subprocess.run(
            ["git", "-C", cwd, "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            timeout=5,
        )
    except Exception:
        return None
    if result.returncode != 0:
        return None
    root = result.stdout.strip()
    return Path(root).resolve() if root else None


def is_relevant_file(path: Path) -> bool:
    if path.name in SPECIAL_TEXT_FILES:
        return True
    return path.suffix.lower() in TEXT_EXTENSIONS


def iter_relevant_files(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        current = Path(dirpath)
        for filename in sorted(filenames):
            path = current / filename
            rel = path.relative_to(root).as_posix()
            if rel in GENERATED_EXACT:
                continue
            if any(rel.startswith(prefix) for prefix in GENERATED_PREFIXES):
                continue
            if is_relevant_file(path):
                yield path, rel


def input_digest(root: Path) -> str:
    digest = hashlib.sha256()
    for path, rel in iter_relevant_files(root):
        digest.update(rel.encode("utf-8"))
        digest.update(b"\0")
        try:
            digest.update(path.read_bytes())
        except OSError:
            continue
        digest.update(b"\0")
    return digest.hexdigest()


def indexes_exist(root: Path) -> bool:
    return all((root / path).exists() for path in GENERATED_EXACT)


def should_run(root: Path) -> tuple[bool, str]:
    current_digest = input_digest(root)
    state_path = root / STATE_PATH
    try:
        previous = json.loads(state_path.read_text(encoding="utf-8")).get("input_digest")
    except Exception:
        previous = None
    return current_digest != previous or not indexes_exist(root), current_digest


def save_state(root: Path, digest: str) -> None:
    state_path = root / STATE_PATH
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps({"input_digest": digest}, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    if os.environ.get("TVASTR_AUTODOC_RUNNING") == "1":
        print("{}")
        return 0

    try:
        payload = json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError:
        payload = {}

    root = git_root(payload.get("cwd") or os.getcwd())
    if root is None:
        print("{}")
        return 0

    generator = root / "scripts" / "generate_docs.py"
    run_needed, digest = should_run(root)
    if not generator.exists() or not run_needed:
        print("{}")
        return 0

    env = os.environ.copy()
    env["TVASTR_AUTODOC_RUNNING"] = "1"
    result = subprocess.run(
        [sys.executable, str(generator), str(root)],
        cwd=str(root),
        env=env,
        capture_output=True,
        text=True,
        timeout=30,
    )
    if result.returncode != 0:
        message = (result.stderr or result.stdout or "autodoc failed").strip()[-1000:]
        print(json.dumps({"systemMessage": f"autodoc failed: {message}"}))
        return 0

    final_digest = input_digest(root)
    save_state(root, final_digest)
    summary = "Autodoc regenerated `Autodoc/MASTER_INDEX.md`, `Autodoc/backend/INDEX.md`, and `Autodoc/frontend/INDEX.md`."
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": summary,
        }
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
