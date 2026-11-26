#!/usr/bin/env python3
"""Show simple stats for a git repository: commits, authors, months, files.

Usage:
    python3 git_stats.py [PATH]

PATH defaults to the current directory. It must be inside a git repository.
"""

import argparse
import subprocess
import sys
from collections import Counter
from pathlib import Path


def run_git(repo, args):
    """Run a git command in repo; return (returncode, stdout)."""
    result = subprocess.run(
        ["git", "-C", str(repo)] + args,
        capture_output=True, text=True,
    )
    return result.returncode, result.stdout


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default=".",
                        help="path inside a git repository (default: current directory)")
    args = parser.parse_args(argv)

    repo = Path(args.path)
    if not repo.is_dir():
        print(f"Error: {args.path} is not a directory.", file=sys.stderr)
        return 1

    code, out = run_git(repo, ["rev-parse", "--is-inside-work-tree"])
    if code != 0 or out.strip() != "true":
        print(f"Error: {args.path} is not inside a git repository.", file=sys.stderr)
        return 1

    code, out = run_git(repo, ["rev-list", "--count", "HEAD"])
    if code != 0:
        print("This repository has no commits yet.")
        return 0
    total = int(out.strip())

    code, out = run_git(repo, ["log", "--format=RECORD:%an|%ad",
                               "--date=short", "--numstat"])
    authors = Counter()
    months = Counter()
    files = Counter()
    added = 0
    removed = 0
    for line in out.splitlines():
        if line.startswith("RECORD:"):
            author, date = line[len("RECORD:"):].split("|")
            authors[author] += 1
            months[date[:7]] += 1
            continue
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) == 3:
            ins, dele, fname = parts
            files[fname] += 1
            if ins != "-":
                added += int(ins)
            if dele != "-":
                removed += int(dele)

    print(f"Repository: {repo.resolve()}")
    print(f"Total commits: {total}")

    print("\nCommits per author (top 10):")
    for author, count in authors.most_common(10):
        print(f"  {count:>5}  {author}")

    print("\nCommits per month (last 12):")
    for month in sorted(months)[-12:]:
        print(f"  {month}  {months[month]}")

    print("\nMost changed files (top 10):")
    for fname, count in files.most_common(10):
        print(f"  {count:>5}  {fname}")

    print(f"\nLines added (estimate): {added}")
    print(f"Lines removed (estimate): {removed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
