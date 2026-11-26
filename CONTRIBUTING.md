# Contributing to dev-ai-tools

Thanks for helping! Keep it simple:

## Adding a skill

1. Create `skills/<skill-name>/SKILL.md` with frontmatter (`name` + `description`) and clear instructions.
2. The skill should do **one job well**. If it does two jobs, split it.
3. Include a short example of good output.

## Adding a tool

1. Create `tools/<tool-name>/` with the code and a `README.md`.
2. The tool must run with as few dependencies as possible — standard library only, unless there is a strong reason.
3. The README must show how to run it and what the output looks like.
4. Test it before opening a pull request.

## General rules

- Small changes beat big ones. One skill or one tool per pull request.
- Write in plain, simple English.
- Don't break what already works.
