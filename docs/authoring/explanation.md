---
layout: page
---

---
layout: page
---

- [Write Explanation](#write-explanation)
- [Update YAML File](#update-yaml-file)

# Write Explanation

- Create a file with extension `.md`.
  While the name can be chosen arbitrarily, the convention is to use `explanation-TITLE.en.md`.
- Add contents to this file.
  See [markdown overview](markdown.md) for help.

# Update YAML File

- Open `metadata.yaml`.
- Under `contents`, add an extra explanation entry.
  Suggestion: put your cursor at the right insertion position (slightly indented) and use code snippet `explanation`.

General form of an exercise entry is:

```yaml
  - name: TITLE
    type: explanation
    id: UNIQUE-IDENTIFIER
    documentation:
      en: explanation-NAME.en.md
```

Optionally, you can also add a `topics` entry (use `topics` code snippet):

```yaml
  - name: TITLE
    type: explanation
    id: UNIQUE-IDENTIFIER
    documentation:
      en: explanation-NAME.en.md
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
