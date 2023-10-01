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

## Why are we using Git?

Using a Version Control System (VCS), which Git is, is the most sensible way to deal with code, which includes distribution, storage and collaboration.
Alternative approaches like downloading/sending zips or relying on OneDrive/Google Drive/Dropbox is just asking for trouble.
We wish you to develop the attitude that using a VCS is the go-to solution whenever you work on code.
We also want you to become familiar with the typical `add`/`commit`/`push` commands.

Why Git specifically?
Git is at the moment by far the most widely used VCS.

Also, we rely on Git to be able to help you out more easily (since we have access to your code) and to track your progress.

## Why are we using the shell instead of a GUI?

While the shell can be trickier to use than a GUI, it also forces you to actually know what you're doing.
We've had too many students use a GUI and randomly click buttons in the hopes of finding a solution, but instead making things a lot worse and sometimes causing their work to be lost.

Being able to work using a shell is also a very important skill for anyone in IT, as it makes it *much* easier to automate tasks.
Some tools also offer more functionality through their command line interface.

# Installation Problems

## How do I create a new directory?

Follow these [instructions]({{ site.baseurl }}{% link troubleshooting/create-directory.md %})

## How do I open a shell?

Follow these [instructions]({{ site.baseurl }}{% link troubleshooting/open-shell.md %})

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

## I get an error when I try to clone my repository: Git says it does not exist

First check that the repository actually exists: copy the URL you're trying to clone in your browser's address bar.
If you get a 404 error (page not found), you didn't create your repository: you need to accept the GitHub Classroom Assignment, which is the step that creates your repository.

If, however, the webpage of your repository does exist, yet Git claims otherwise, this typically means you have multiple GitHub accounts and are using your account X to access the repository of your account Y.
You will need to [reset your credentials](troubleshooting/reset-credentials.md).

## When I do `progtool setup`, it shows many errors, the last one being `GitHubOrganizationNotFound`

When on campus, all students are connected to the internet using the same IP address.
GitHub detects a sudden surge in requests from that single address and doesn't like that, so it decides to cut us off for a short while.

We don't know exactly for how long GitHub cuts off access, but it should definitely be less than two hours.
In other words, if you encounter this error, you'll simply have to wait and try again later.

Or, if the problem persists, follow the [manual setup instructions]({{ site.baseurl }}{% link troubleshooting/manual-setup.md %}).

## When running `progtool setup`, I get many errors, something to do with certificates

At the moment of this writing, we're not entirely sure what causes this problem.
We do have a solution that we expect to work though.

* Go to your home directory.
  * Under Windows, you can use File Explorer and enter `%HOMEPATH%` in the address bar.
  * Under MacOS/Linux, go to `~`.
* There should be a subdirectory named `progtool`.
  If there isn't, you'll have to do a fully manual setup as described [here]({{ site.baseurl }}{% link troubleshooting/manual-setup.md %}).
* Go inside this `progtool` subdirectory.
* There should be a file named `progtool-settings.yaml`.
  If there isn't, we refer you to the [fully manual setup]({{ site.baseurl }}{% link troubleshooting/manual-setup.md %}).
* Open this file using an editor.
  We suggest you use Visual Studio Code.
* The settings file should contain a line starting with `html_path:`, followed by a path.
  This path should have the form `HOME_DIRECTORY/progtool/progtool-index.html`.
* If you look for a file at this location on your drive, we expect it's missing.
  If it's not missing, contact a lecturer.
* Using your browser, go to [this webpage](https://github.com/ucll-programming/frontend/releases/latest).
* Download `index.html` to your drive, to `HOME_DIRECTORY/progtool/progtool-index.html`.
  In other words, the settings file should point to this file.

Rerunning `progtool setup` should now work fine.

## How do I manually perform the setup of `progtool`?

Follow [these instructions]({{ site.baseurl }}{% link troubleshooting/manual-setup.md %})

## I have a technical problem and need help

Contact one of your lecturers.
Make sure to describe the problem in detail:

* Give context: what are you trying to achieve?
  What step are you at in the documentation?
* Tell us *exactly* what failed.
  What command did you type in?
  What directory are you in?
  (Find out using `pwd`.)
* Show us the actual error message you're getting.
* If the error involves progtool, run the same command again with diagnostics turned on.
  This is done by adding `-vv` just after `progtool`.
  For example, if `progtool setup` fails, try again with `progtool -vv setup`.
  It will still fail, but will give more information about what it's doing.
  Include this information in your message.
* Mention which OS (Windows, MacOS or Linux) you are using.
* Provide us with a link to your GitHub Classroom repository, i.e., the URL you receive when accepting the assignment.

Remark that the installation steps are interdependent: if you are at step 5, steps 1 through 4 must have succeeded.

# Progtool Issues

## I'm running `progtool server` for the first time and I'm just getting a spinning wheel

The first time, the assistant tool will run all tests of all exercises.
This can take some time on slower machines.
Just wait a little bit and the course's website should show up.

## When I'm running `progtool server` I get bombarded by errors mentioning `pytest`.

You probably didn't install `pytest` correctly.
Look for "Installing all necessary packages" in the [installation instructions]({{ site.baseurl }}{% link installation/index.md %}).

## How do I manually run the tests?

Open a shell in the chapter's directory (`course-material/exercises/CHAPTER`) and run

```bash
$ pytest test-EXERCISENAME.py
```

# Pytest Issues

## When I run pytest, it dumps a lot of information on me. Can I get a summary?

This [page]({{ site.baseurl }}{% link workflow/pytest.md %}) gives you some options.

## How do I interpret the pytest results?

This [page]({{ site.baseurl }}{% link workflow/pytest.md %}) provides a bit of explanation.

## I'm not satisfied with the provided tests. Can I perform test myself?

* You can write your own tests.
  We suggest you do not modify the given test files, as this may cause Git merge conflicts if we also choose to modify them.
  It is better to put your own tests in a separate file.
* You can use the Python shell.
  Say you have a function `foo` stored in `student.py` which you wish to test manually.
  * Go in the directory containing `student.py`.
  * Launch the Python shell: `$ py`.
  * Import your code: `from student import *`.
  * Now you can call your function from the shell: `foo(1, 2, 3)`.
