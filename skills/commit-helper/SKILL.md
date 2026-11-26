---
name: commit-helper
description: Write a clear conventional commit message from staged changes. Use when the user asks for a commit message, or before committing.
---

# Commit Helper

Turn staged changes into one good commit message. Follow Conventional Commits.

## How to work

1. Look at the staged diff (`git diff --cached`). If nothing is staged, say so and stop.
2. Work out the single main purpose of the change. If the diff does two unrelated things, say that and suggest splitting the commit.
3. Pick the type from this list:
   - `feat` — a new feature
   - `fix` — a bug fix
   - `docs` — documentation only
   - `style` — formatting, no code change
   - `refactor` — code change that is neither a feature nor a fix
   - `test` — adding or fixing tests
   - `chore` — build, tooling, or dependency changes
4. Write the message:
   - Subject line: `type(scope): short summary`, 50 characters or fewer, lowercase, no full stop at the end.
   - Body (only if it adds real information): 1–3 short lines saying what changed and why. Wrap at 72 characters.
   - No filler like "updated files" or "minor changes".

## Example

```
feat(auth): add password reset via emailed link

Users can now request a reset link from the login page.
The link expires after one hour.
```

## Rules

- Never commit anything yourself — only write the message and show it to the user.
- If the diff is huge or unclear, ask what the change is for instead of guessing.
- Keep the subject honest: it must describe what the change actually does.
