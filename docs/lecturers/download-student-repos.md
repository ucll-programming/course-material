---
layout: page
---

# Downloading Student Repositories

## Installing GitHub CLI

GitHub offers a command line tool named `gh`.
[Install it](https://github.com/cli/cli#installation).
We suggest relying on Chocolatey, scoop or WinGet as it makes it easier to update `gh`.

## Installing the gh Classroom Extension

On the shell,

```bash
$ gh extension install github/gh-classroom
```

## Downloading Using gh classroom

**IMPORTANT** At the time of this writing, this leads to a server error.
At some point in the future we expect it will work.
In the meantime, see below for [manual download instructions](#downloading-using-gh).

```bash
$ gh classroom clone student-repos
# Select correct classroom/assignment from list
```

Alternatively, on the Github Classroom's Assignment page (for 22-23, [here](https://classroom.github.com/classrooms/145902458-p1-exercises/assignments/p1-exercises-2324)), you can find the command to download all repos.

```bash
# Specific for p1-exercises-2324
$ gh classroom clone student-repos -a 494018
```

## Downloading using gh

Create a file `download-student-repos.sh` and copy paste the following code into it:

```bash
#!/usr/bin/env bash

gh repo list UCLL-P1-2324 --limit 1000 --json url --template '{{'{{'}}range .}}{{'{{'}}.url}}{{'{{'}}"\n"}}{{'{{'}}end}}' > student-repo-urls.txt

for url in `cat student-repo-urls.txt`; do
    id=`basename $url`

    if [ -d $id ]; then
        echo Skipping $url
    else
        # Uncomment for SSH url
        # url=${url/https:\/\/github.com\//git@github.com:}

        git clone $url
    fi
done
```

Run the script:

```bash
$ ./download-student.repos.sh
```

If you get an error about a rename failing, tell it to try again.

This script will check if a repository has already been downloaded before, so it's safe to run it multiple times.

## More Information

[Official page](https://docs.github.com/en/education/manage-coursework-with-github-classroom/teach-with-github-classroom/using-github-classroom-with-github-cli)
