---
layout: page
title: Restore Files
---

# Restoring a File

Git allows you to restore a file to what it was in any previously made commit.

## Restoring to Last Commit

In order to undo all changes made since the last commit, use

```bash
$ git checkout FILENAME
```

> *WARNING* This operation cannot be undone.
> The file will be overwritten and there is no way to perform a "redo".

## Restoring to an Arbitrary Commit

You can view all the changes you made to a file using

```bash
$ git log FILENAME
commit HASH
Author: YOUR NAME <YOUR EMAIL ADDRESS>
Date:   SOME DATE

     DESCRIPTION
```

This will list all commits which contain modifications to this file.
A commit is uniquely identified by its hash: it's the long hexadecimal number following `commit`.
Find the commit that interests you.

If you wish to view the contents of the file according to a certain commit, use

```bash
$ git show HASH:./FILENAME
```

If you've found the version of the file you wish to revert to, use

```bash
$ git checkout HASH FILENAME
```

> *WARNING* This last operation will overwrite your file with an older version.
> All your more recent changes will be lost.
