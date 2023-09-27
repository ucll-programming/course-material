---
layout: page
---

# Python Installation (Windows)

The most recent Python version can be found [on the Python website](https://www.python.org/downloads/).
Download and install it.
While installing, **check the checkbox to Add Python to PATH**.
Then select Install Now.

{% include checking-python-installation.md %}

Open Git Bash in the `scripts` directory inside the repository and enter:

```bash
$ py check-python-installation.py
```

If the output ends on `SUCCESS`, you can proceed with the [next step](packages.md).

## Next Step

[Install Python packages](packages.md).
