---
layout: page
---

# Git Installation (MacOS)

## Checking For Pre-Existing Installation

First, check that Git is not already installed.
Open a terminal and enter

```bash
$ git --version
```

If you are shown a version number, Git is already installed and you can jump to the [Configuration section](#configuration).

## Checking For Pre-Existing Homebrew Installation

To install Git, you need [Homebrew](https://brew.sh/), a package manager for MacOS.
Let's first check if it's already installed:

```bash
$ brew --version
```

If this prints out a version number, jump to the [Git Installation section](#git-installation)

## Installing Homebrew

Enter the following command (if needed, you can watch this [video](https://www.youtube.com/watch?v=SOjSNB7F2m4)):

```bash
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow the instructions shown.

## Git Installation

To install Git, enter

```bash
$ brew install git
```

{% capture my_include %}{% include git-configuration.md %}{% endcapture %}
{{ my_include | markdownify }}

## Next Step

[Download the exercises](./github-classroom.md).
