---
layout: page
---

# Python Installation

The most recent Python version can be found [on the Python website](https://www.python.org/downloads/).
Download and install it.

## Checking Your Python Installation

It’s important to check that your Python installation actually works.
This can be slightly tricky, since the details depend on your OS.
There are two kinds of problems that can arise:

* Python cannot be found
* The wrong version of Python is found

Below are instructions that verify both at the same time.
The goal is that you get Python to tell you which version it is, and that this version is 3.8 or higher.
If you encounter problems, inform a lecturer.

**IMPORTANT**

> A `$` in the beginning of a line means that you should input that line in a shell.
> Do not write the `$` itself though, only what follows.
> For example, `$ ls` means you should type `ls` followed by enter.

### Windows Instructions

Open Git Bash in the `scripts` directory and enter.

```bash
$ py check-python-installation.py
```

If the output ends on `SUCCESS`, you can proceed with the [next step](python-packages.md).

Next: [Install Python packages](packages.md)

### MacOS/Linux Instructions

Open a terminal in the `scripts` directory.

```bash
$ python3 check-python-installation.py

# or, if this doesn't work, try

$ python check-python-installation.py
```

Remember which one you used; it will come in handy later.

If the output ends on `SUCCESS`, you can proceed with the [next step](python-packages.md).

Next: [Install Python packages](packages.md)
