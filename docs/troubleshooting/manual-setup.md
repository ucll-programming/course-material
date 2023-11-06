---
layout: page
---

# Manual Setup

## Settings File

* Go to your home directory.
  * Windows: Open File Explorer and type `%HOMEPATH%` in the address bar.
* Create a subdirectory named `progtool`.
  If it already exists, you can leave it be.
* Go inside this newly created `progtool` directory.
* Create (or open if it already exists) the file named `progtool-settings.yaml`.
* If it is empty, copy paste the following data into it

```text
cache_delay: 5.0
html_path: HOME_DIRECTORY/progtool/index.html
judgment_cache: HOME_DIRECTORY/progtool/progtool-cache.json
language_priorities:
- en
- nl
repository_root: REPOSITORY_DIRECTORY
style_path: HOME_DIRECTORY/progtool/default.scss
```

* `HOME_DIRECTORY` should be an *absolute path* to your home directory, e.g. `C:/Users/myname` on Windows or `/usr/myname` on MacOS/Linux.
* `REPOSITORY_DIRECTORY` should be an *absolute path* to the directory in which all your course material has been stored.

Below is an example `progtool-settings.yaml`:

```text
cache_delay: 5.0
html_path: C:/Users/myname/progtool/index.html
judgment_cache: C:/Users/myname/progtool/progtool-cache.json
language_priorities:
- en
- nl
repository_root: C:/School/programming/course-material
style_path: C:/Users/myname/progtool/default.scss
```

## Downloading index.html

* Using a browser, go to this [webpage](https://github.com/ucll-programming/frontend/releases/latest).
* Under assets, you should find an entry `index.html`.
* Download this file and put this in the `HOME_DIRECTORY/progtool` directory you created in the previous step.

## Downloading default.scss

* Using a browser, go to this [webpage](https://raw.githubusercontent.com/ucll-programming/themes/master/default.scss).
* Download it (e.g., using right click -> Save as) to `HOME_DIRECTORY/progtool/default.scss`.
