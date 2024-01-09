---
layout: page
title: Shell
---

* Table of Contents
{:toc}

# Opening a Shell

## Windows: From File Explorer

On Windows, open File Explorer and go to the directory you wish to open a terminal in.
Right click on the directory and `Open in Windows Terminal` (or `Git Bash Here`).

There are multiple different shells: `cmd.exe`, Powershell, Git Bash, and so on.
For the purposes of this course, it's best to use Git Bash.
You can select the shell by pressing the little down arrow button.

> You can make Git Bash the default shell in the settings.

## Inside Visual Studio Code

You can open a shell inside Visual Studio Code by opening the `Terminal` menu and selecting `New Terminal`.

# Current Directory

If you're not sure in which directory you currently reside, you can use the "print working directory" command:

```bash
$ pwd
/g/repos/ucll/programming/course-material/exercises/arithmetic
```

# Changing Directory

## Going Back Up

```bash
$ cd ..
```

## Entering a Subdirectory

```bash
$ cd SUBDIRECTORY
```

where `SUBDIRECTORY` has been replaced by the name of the subdirectory you wish to enter.
