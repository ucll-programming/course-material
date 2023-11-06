---
layout: page
---

# Path Issues

## What's the PATH?

A shell (such as Bash, PowerShell, etc.) allows you to enter commands.
These commands are (in most cases) actual programs.
For example,

* `code filename` will open Visual Studio Code and have it show `filename`'s content.
* [`7-zip`](https://www.7-zip.org/), a popular file archiver (i.e., it can create zip files), has both a GUI and a command line interface.
* [`ffmpeg`](https://ffmpeg.org/) is a tool to deal with audio and video files.

Say you enter

```bash
$ 7z a package.zip *
```

This command invokes `7z` and asks it to create a new zip file named `package.zip` and add all files in the current directory.
Now, `7z` has to be installed somewhere.
On Windows, it is typically in the directory `C:\Program Files\7-Zip`.
But how does the shell know to look there?
It cannot possibly search your entire drive looking for `7z.exe`; that would take way too long.

The algorithm used by the shell goes as follows:

* It looks in the current directory of `7z`.
* If it cannot be found there, it goes through a list of other directories.
  This list is stored in the [`PATH` environment variable](https://en.wikipedia.org/wiki/PATH_(variable)).
