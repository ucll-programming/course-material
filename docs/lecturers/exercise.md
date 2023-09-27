---
layout: page
---

- [Write Assignment](#write-assignment)
- [Write Tests](#write-tests)
- [Update YAML File](#update-yaml-file)

# Write Assignment

- Create a file with extension `.md`.
  While the name can be chosen arbitrarily, the convention is to use `assignment-TITLE.en.md`.
- Add contents to this file.
  See [markdown overview](markdown.md) for help.

# Write Tests

Write tests inside a file `test-title.py`, e.g. `test-is-prime.py`.
Rely on [pytest](https://docs.pytest.org/en/7.4.x/).

Useful code snippets:

- `testprelude` that adds the most commonly used `import`s.
- `testparam` generates a skeleton for a parametrized test.

# Update YAML File

- Open `metadata.yaml`.
- Under `contents`, add an extra exercise entry.
  Suggestion: put your cursor at the right insertion position (slightly indented) and use code snippet `exercise`.

General form of an exercise entry is:

```yaml
  - name: NAME
    type: exercise
    id: UNIQUE-IDENTIFIER
    documentation:
      en: assignment-NAME.en.md
    difficulty: DIFFICULTY
    judge:
      type: pytest
      file: test-NAME.py
```

Optionally, you can also add a `topics` entry (use `topics` code snippet):

```yaml
  - name: NAME
    type: exercise
    id: UNIQUE-IDENTIFIER
    documentation:
      en: assignment-NAME.en.md
    difficulty: DIFFICULTY
    judge:
      type: pytest
      file: test-NAME.py
    topics:
      introduces:
        - ID1
        - ID2
      must_come_before:
        - ID3
      must_come_after:
        - ID4
        - ID5
        - ID6
```

Each of the three subentries of `topics` is optional.

- `introduces` states which topics are discussed in that exercise.
  This should be empty as exercises should not introduce new concepts, only explanations.
- `must_come_before` should be seldomly used.
  It lists topics that should *not* yet have been discussed.
- `must_come_after` are topics that the exercise relies on.

Use `progtool check topics` to make sure the constraints are satisfied.
