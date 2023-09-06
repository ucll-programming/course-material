---
layout: page
title: Committing Single File
---

# Committing All Files at Once

First, make sure you know exactly which files are about to be committed.
In the repository's root directory, type

```bash
$ git status
```

Make sure you didn't actually modify files you didn't mean to.
Follow [these instructions](restore-files.md) if you wish to undo changes.

Only proceed if you're certain you wish to commit all changes listed by `git status`.

```bash
# In the repository's root directory
$ git add .

# Writes the changes to the repository
# Replace MESSAGE by something more descriptive
$ git commit -m "MESSAGE"

# Uploads updates to GitHub
$ git push
```
