---
layout: page
---

# Python Installation on Linux

How to install Python depends on your Linux distro.
Look up how to install Python

{% include python-installation-shared.md %}

Open a terminal in the `scripts` directory.

```bash
$ python check-python-installation.py

# In case this doesn't work, try

$ python3 check-python-installation.py
```

If the output ends on `SUCCESS`, you can proceed with the [next step](python-packages.md).

**IMPORTANT**

> Remember how you had to run a Python script (i.e., `python` vs `python3`).
> In all further instructions, we will just use `py`, but you will have to replace `py` by either `python` or `python3`.

Next: [Install Python packages](packages.md)
