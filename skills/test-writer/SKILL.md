---
name: test-writer
description: Write focused unit tests for a function or file — naming, edge cases, and what not to test. Use when the user asks for tests, or before refactoring code that has no test coverage.
---

# Test Writer

Write small, focused unit tests that catch real bugs. Tests should be easy to read and quick to run.

## How to work

1. **Read the code first.** Understand what the function does, what it takes in, and what it returns. If the code is unclear, say so before writing tests.
2. **Pick the cases that matter:**
   - The happy path — the normal input the function is written for.
   - Edge cases — empty input, zero, the biggest or smallest allowed value, a missing file.
   - Error cases — bad input, wrong types, things that should raise an error or return one.
3. **One behaviour per test.** A test that checks three things at once hides which one broke.
4. **Name tests after the behaviour**, not the function: `test_returns_empty_list_when_no_notes_found` beats `test_find_notes_3`.

## What NOT to test

- Don't test the language or the library (for example, that `sorted()` sorts).
- Don't test a private helper through the public function twice — test it once, directly.
- Don't write tests for code that is about to be deleted.

## Output format

- Use the project's existing test style. If there is no test file yet, use plain `assert` statements in a file named `test_<module>.py`.
- Group tests by the function they cover, with a short comment above each group.
- Keep setup tiny — build test data inside the test, not in a shared fixture, unless three or more tests need the same data.

## Rules

- Never change the code under test to make a test pass. If the code is wrong, say so.
- Every test must be able to fail. A test that always passes is not a test — read it once more after writing it and check.
- Keep tests fast. No network, no real files outside a temp folder, no sleeping.
