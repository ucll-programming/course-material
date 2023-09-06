---
layout: page
title: Updating the Course Material
---

# Updating the Course Material

First, you should make sure that all your changes have been committed.

```bash
$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

shows you a list of files you modified since your last commit.
Ideally, there shouldn't be any such files.
If there are, consider [committing the changes](#saving-your-work).

Next, pull in the updates:

```bash
$ git pull upstream master
```
