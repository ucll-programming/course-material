## Configuration

After you have finished installing Git, you still need to configure it.
In a shell, write the following commands where you substitute `YOUR-NAME` your name (not your GitHub login) and `YOUR-EMAIL-ADDRESS` by your UCLL email address.

**IMPORTANT**

> A `$` in the beginning of a line means that you should input that line in a shell.
> Do not write the `$` itself though, only what follows.
> For example, `$ ls` means you should type `ls` followed by enter.

```bash
$ git config --global user.name "YOUR-NAME"

$ git config --global user.email "YOUR-EMAIL-ADDRESS"
```

For example, for a student named John Smith, the commands would be

```bash
$ git config --global user.name "John Smith"

$ git config --global user.email "john.smith@student.ucll.be"
```

**You won't receive any output from these commands.**
That's fine.
