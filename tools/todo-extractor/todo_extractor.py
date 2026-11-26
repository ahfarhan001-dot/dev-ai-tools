#!/usr/bin/env python3
"""Find TODO, FIXME, and HACK comments in a codebase and print one tidy report.

Usage:
    python3 todo_extractor.py [PATH] [--tags TODO,FIXME,HACK]

PATH defaults to the current directory. Only common code and text files are
scanned; hidden folders (.git, node_modules, __pycache__, .venv) are skipped.
"""

import argparse
import re
import sys
from pathlib import Path

DEFAULT_TAGS = ("TODO", "FIXME", "HACK")

EXTENSIONS = {
    ".py", ".js", ".ts", ".jsx", ".tsx", ".java", ".c", ".h", ".cpp",
    ".hpp", ".go", ".rs", ".rb", ".php", ".swift", ".kt", ".css",
    ".html", ".md", ".txt", ".sh", ".sql",
}

SKIP_DIRS = {
    ".git", "node_modules", "__pycache__", ".venv", "venv",
    "dist", "build", ".idea", ".vscode",
}


def find_notes(root, tags):
    """Walk root and return a list of (file, line_no, tag, text) notes."""
    pattern = re.compile(
        r"\b(" + "|".join(re.escape(t) for t in tags) + r")\b[:\s-]*(.*)"
    )
    notes = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() not in EXTENSIONS:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for i, line in enumerate(text.splitlines(), start=1):
            match = pattern.search(line)
            if match:
                notes.append((str(path), i, match.group(1), match.group(2).strip()))
    return notes


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default=".",
                        help="directory to scan (default: current directory)")
    parser.add_argument("--tags", default=",".join(DEFAULT_TAGS),
                        help="comma-separated tags to look for")
    args = parser.parse_args(argv)

    root = Path(args.path)
    if not root.is_dir():
        print(f"Error: {args.path} is not a directory.", file=sys.stderr)
        return 1

    tags = tuple(t.strip() for t in args.tags.split(",") if t.strip()) or DEFAULT_TAGS
    notes = find_notes(root, tags)

    if not notes:
        print(f"No {', '.join(tags)} found under {root}.")
        return 0

    print(f"Found {len(notes)} note(s) under {root}:\n")
    current_file = None
    for file, line_no, tag, text in notes:
        if file != current_file:
            current_file = file
            print(f"{file}")
        print(f"  line {line_no}: [{tag}] {text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
