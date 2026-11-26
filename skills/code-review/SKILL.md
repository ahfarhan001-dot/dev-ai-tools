---
name: code-review
description: Review a code change for bugs, security issues, performance problems, and readability. Use when the user asks for a code review, or before a commit or pull request.
---

# Code Review

Review the given code or diff like a careful senior teammate. Be useful, not noisy.

## How to review

1. **Understand first.** Read the whole change before judging any line. Say what the change is trying to do, in one or two sentences.
2. **Check in this order:**
   - **Correctness** — wrong logic, off-by-one errors, missed edge cases, broken error handling.
   - **Security** — injection, leaked secrets, unsafe input handling, missing auth checks.
   - **Performance** — needless loops, N+1 queries, loading more data than needed.
   - **Readability** — confusing names, duplicated logic, functions doing too much.
3. **Only flag real problems.** Skip style nits unless they genuinely hurt readability. No praise for its own sake.

## Output format

- Start with a one-line verdict: `Looks good`, `Needs changes`, or `Needs discussion`.
- Then a short list of findings, most serious first. Each finding has:
  - Where it is (file and line, or function name)
  - What's wrong and why it matters
  - A concrete fix — show the corrected code, don't just describe it
- End with anything worth a quick follow-up, if there is any. If there is nothing, say so.

## Rules

- Never invent bugs that aren't there. If you are unsure about something, say you are unsure and explain the risk.
- Keep every suggestion actionable. If the user can't act on it, don't write it.
- Match the project's existing style instead of imposing your own.
