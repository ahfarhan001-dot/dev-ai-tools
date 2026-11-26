# git-stats

Show simple stats for a git repository: total commits, commits per author, commits per month, the most-changed files, and an estimate of lines added and removed.

## Usage

```bash
# Stats for the current directory's repository
python3 git_stats.py

# Stats for another repository
python3 git_stats.py /path/to/your/repo
```

Requires Python 3.8 or newer, and `git` on your PATH. No extra packages.

## Example output

```
Repository: /home/user/myproject
Total commits: 42

Commits per author (top 10):
     30  AH Farhan
     12  Sara Lee

Commits per month (last 12):
  2026-09  5
  2026-10  20
  2026-11  17

Most changed files (top 10):
      8  README.md
      6  app.py
      4  utils.py

Lines added (estimate): 1204
Lines removed (estimate): 318
```

## Notes

- The path must be inside a git repository. Outside one, it prints an error and stops.
- A repository with no commits yet prints a short message instead of stats.
- Line counts come from `git log --numstat` and are estimates: binary files and renames are not counted as lines.
