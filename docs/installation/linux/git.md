---
layout: page
---

# Git Installation (Linux)

## Checking For Pre-Existing Installation

In a shell, write

```bash
$ git --version
```

If you are shown a version number, Git is already installed and you can jump to the [Configuration section](#configuration).

## Git Installation

The installation depends on which Linux distribution you're running.
We refer you to this [page](https://git-scm.com/download/linux).

{% capture my_include %}{% include git-configuration.md %}{% endcapture %}
{{ my_include | markdownify }}

## Next Step

[Download the exercises](./github-classroom.md).
