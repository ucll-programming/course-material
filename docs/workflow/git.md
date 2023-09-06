---
layout: page
title: Git
---

* Table of Contents
{:toc}

# Saving Your Work

```bash
# First select the files to be saved
$ git add MODIFIED-FILES

# Writes the changes to the repository
$ git commit -m "SOME MESSAGE"

# Uploads updates to GitHub
$ git push
```

# Working on Two Machines

Let's call your two machines A and B.
First, make sure that you have performed the [installation instructions](../installation/) on both machines, with one exception: on the second machine, skip the `git pull upstream master` step.

Say you have made updates on machine A and you wish to see them appear on machine B.

* On machine A: make sure you have [saved your work](#saving-your-work): `add`, `commit` and `push`.
* On machine B: enter `$ git pull`.

## Merge Conflicts

If you made changes on both A and B before synchronizing, you might run into a merge conflict.
This means that Git does not know how to combine the changes made on both machines.

There are multiple ways to resolve merge conflicts.

### Resolving Conflicts: Blunt Approach

First, determine which files are conflicted:

```bash
$ git status
```

Say `student.py` is the problem: you have made incompatible changes to this file on both machines.

```bash
# Tell Git to keep the version stored on the current machine
$ git checkout --ours student.py

# OR

# Tell Git to keep the version from the other machine
$ git checkout --ours student.py
```

After you have made your choice,

```bash
$ git add student.py
$ git commit
# VSCode should pop up and show you a commit message, simply save and close
$ git push
```

### Resolving Conflicts: Precise Approach

Determine which files are conflicted:

```bash
$ git status
```

Open these files in Visual Studio Code.
Git will have added extra lines to indicate which parts of the file contain incompatible changes.
These will look like this:

```python
...

<<<<<<<<<<<<<<<<<<<<
VERSION 1
====================
VERSION 2
>>>>>>>>>>>>>>>>>>>>

...
```

You'll have to remove the `<<<<<`, `=====` and `>>>>>` lines, as well as merge both versions of the code.
Save.

```bash
$ git add FILE
$ git commit
# VSCode will appear and present a commit message, simply save and close
$ git push
```
