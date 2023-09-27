---
layout: page
---

# Python Installation (Linux)

How to install Python depends on your Linux distribution.
Look up how to install Python

{% include checking-python-installation.md %}

Open a shell in the `scripts` directory.

```bash
$ python check-python-installation.py

# In case this doesn't work, try

$ python3 check-python-installation.py
```

If the output ends on `SUCCESS`, you can proceed with the [next step](python-packages.md).

**IMPORTANT**

> Remember how you had to run a Python script (i.e., `python` vs `python3`).
> In all further instructions, we will just use `py`, but you will have to replace `py` by either `python` or `python3`.

## Next Step

[Install Python packages](packages.md).
