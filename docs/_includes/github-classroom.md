
* Table of Contents
{:toc}

## Accepting the Assignment

On Toledo, under "Cursus Materiaal", you'll find a link to the GitHub Classroom Assignment.
Click on it.
You will be led to a page inviting you to "Accept this assignment".
Press the button to accept it.

You are then shown a page informing you that your repository is being prepared.
Refresh the page every few seconds until a new page appears telling you you're ready to go.
A URL should be shown: it should look something like `https://github.com/UCLL-P1-2324/p1-exercises-2324-yourusername`.
You will need this URL, so don't lose it.

> **IMPORTANT** If you go to your repository's website, GitHub tries to be helpful by showing you instructions of how to set up things, such as creating a `README.md` file.
> Do NOT follow these instructions.
> Simply follow the instructions shown on this page.

> If you happen to lose the URL, simply visit the GitHub Classroom link on Toledo again.
> You'll be brought straight to the page showing the URL.

## Cloning the Repository

On your machine, create a directory where you would like to store the exercises.

> Do _not_ place this directory under OneDrive/DropBox/Google Drive/...
> We will be working with GitHub, which is a better alternative for storing code in the cloud.
> Storing a Git repository on OneDrive/... could corrupt it.

Open a terminal in this directory and enter the following command:

> As always, you only need to enter in commands following a `$`.
> All other lines are either comments or expected responses.

```bash
# Download the repository
# !!! Replace YOUR-FORK-URL by the URL you were given earlier by GitHub Classroom !!!
$ git clone YOUR-FORK-URL course-material
```

This should create a directory named `course-material` and download the course material into that directory.

## Setting Up Remote Repositories

Enter the following commands:

```bash
# Go into course material directory
$ cd course-material

# Tell Git about the lecturer's repository and call it upstream
$ git remote add upstream https://github.com/ucll-programming/course-material.git
```

Let's check if everything worked:

```bash
# Ask for a list of remote repositories
$ git remote -v
origin    https://github.com/UCLL-P1-2324/p1-exercises-2324-youraccountname (fetch)
origin    https://github.com/UCLL-P1-2324/p1-exercises-2324-youraccountname (push)
upstream  https://github.com/ucll-programming/course-material.git (fetch)
upstream  https://github.com/ucll-programming/course-material.git (push)
```

Here, `origin` refers to your very own repository, which you have write access to.
`upstream` refers to our repository, to which you only have readonly access.

## Getting the Course Material

Visit your remote repository's webpage.
You can do this by using a browser and going to your repository URL.
GitHub should claim it's empty.
Let's fill it up by sending your locally stored data to GitHub:

```bash
# Download from lecturer's repository
$ git pull upstream master

# Upload to your remote repository
$ git push -u origin master
```

After the push is finished, refresh your repository's webpage in the browser.
It should now contain all the exercises.

From now on, you should make sure to always push your solutions to GitHub.
Instructions for how to do this can be found [here](../../workflow).
