# dev-ai-tools

Open-source AI tools and reusable development skills for developers. Small, practical things that help with everyday coding work — built in the open, free for everyone to use.

## What's inside

### Skills (`skills/`)

Reusable skill packs you can drop into your AI coding setup. Each skill is a single folder with a `SKILL.md` that tells the AI exactly how to do one job well.

| Skill | What it does |
| --- | --- |
| [code-review](skills/code-review/) | Reviews a code change for bugs, security issues, performance problems, and readability — and gives fixes, not just complaints. |
| [commit-helper](skills/commit-helper/) | Writes clear, conventional commit messages from your staged changes. |

### Tools (`tools/`)

Small command-line tools you can run right away. No setup, no dependencies beyond Python 3.

| Tool | What it does |
| --- | --- |
| [todo-extractor](tools/todo-extractor/) | Scans your code for `TODO`, `FIXME`, and `HACK` comments and prints one tidy report. |

## Quick start

```bash
git clone https://github.com/ahfarhan001-dot/dev-ai-tools.git
cd dev-ai-tools

# Find every TODO in a project
python3 tools/todo-extractor/todo_extractor.py /path/to/your/project
```

Skills are plain Markdown — copy a skill folder into your AI tool's skills directory and it just works.

## Roadmap

- More skills: refactor-helper
- More tools: duplicate-code finder, import cleaner, changelog generator
- Every addition stays small, documented, and dependency-free where possible

## Contributing

Found a bug or want to add a skill or tool? See [CONTRIBUTING.md](CONTRIBUTING.md). Keep it small, keep it documented, keep it working.

## License

MIT — see [LICENSE](LICENSE).
