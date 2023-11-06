---
layout: page
---

# Receiving Course Material Updates

During the semester, the course material can be updated by the lecturers: typos could be fixed, exercises added, explanations can be improved, etc.
If a lecturer informs you about updates made to the course material, use these instructions to receive these updates.

## Steps

First, you should make sure that all your changes have been committed.
`git status` shows you a list of files you modified since your last commit.
Ideally, there shouldn't be any such files:

```bash
$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

If there are, consider [committing the changes](#saving-your-work).

Next, pull in the updates:

```bash
$ git pull upstream master
```

The updates are now on your machine.
Let's also upload them into the cloud, to Github's servers:

```bash
$ git push
```
