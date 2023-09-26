---
layout: page
show_in_header: true
title: FAQ
---

**Table of Contents**

* Table of Contents
{:toc}

# General Questions

## I found a small mistake in the course material. Who do I tell about it?

Create an issue [here](https://github.com/ucll-programming/course-material/issues).
You only need to copy the sentence in which the mistake occurs, we can easily search through the entire material for that sentence.
You should preferably also indicate what the mistake is.

After we fix it, we will close your issue.
You can then download the updated version of the course material following [these instructions](workflow/update-course-material.md).

## I don't like the location where I stored my course material. How do I move it elsewhere?

You can freely move the course material around on your drive.
[This page](troubleshooting/relocating.md) explains how.

## I work with multiple machines. How do I set up the course material so that it's always synchronized across all machines?

Follow [these steps](workflow/two-machines.md).

## I've switched machines. How do I transfer all my solutions to the new machine?

Start by making sure that all your work has been [committed and pushed](workflow/commit-all-files.md) on your old machine.
Next, if you follow all [installation instructions](installation/index.md) on your new machine, you should end up with an up-to-date version of the course material, including your solutions.

# Troubleshooting

## I get an error when I try to clone my repository: Git says it does not exist

First check that the repository actually exists: copy the URL you're trying to clone in your browser's address bar.
If you get a 404 error (page not found), you didn't create your repository: you need to accept the GitHub Classroom Assignment, which is the step that creates your repository.

If, however, the webpage of your repository does exist, yet Git claims otherwise, this typically means you have multiple GitHub accounts and are using your account X to access the repository of your account Y.
You will need to [reset your credentials](troubleshooting/reset-credentials.md).

## I cannot download the course material as explained in the instructions

If performing the `git pull upstream` step fails, you probably have entered the wrong `upstream` URL in a previous step.

You can check if it's correct:

```bash
$ git remote -v
```

Copy the URL to the right of `upstream` and paste in the address bar of your browser.
If it doesn't lead you to the course material webpage, the URL is wrong and you'll need to update it:

```bash
$ git remote set-url upstream CORRECTURL
```

If the URL is correct and `git pull upstream` still doesn't work, you have encountered a new kind of error.
Contact a lecturer.
