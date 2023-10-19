# Runnable Scripts

As of yet, you've been writing function after function and storing them in a `.py` file.
But how does one make an actual application, like a game?
Surely, launching a game can't involve having to open a Python shell and calling some function?
There has to be a better way.
Can we run a Python program just like we can start Chrome, Visual Studio Code, Netflix, etc.?

Good news, everyone: the answer to this question is yes.

## Top Level Statement

First, you need to know about top level statements.
These are pieces of code you put outside functions, like this:

:::code{caption="script.py"}

```python
# This is a top level statement
print('Hello from the top')

def foo():
    # This is NOT a top level statement as it is inside a function
    print('Hello from inside foo')
```

:::

If you store this within a file (e.g., `script.py`), you can run its contents from the shell.
Python will then execute all top level statements:

:::code{caption="Bash"}

```bash
$ py script.py
Hello from the top
```

:::

While it is technically possible to put all your code at the top level, there are serious disadvantages to do so:

* It quickly becomes an unreadable mess.
  Functions add structure, improve readability and maintainability, etc.
* You want to be able to test targeted pieces of your code.
  Functions are nice little testable packages.
  Code on the top level is monolithic and much harder to test.

A typical approach is to define a `main` function:

:::code{caption="script.py"}

```python
def main():
    print('Hello!')


main()
```

:::

`main` is a clear starting point, from which other functions will be called, that will call other functions, etc.

## `__name__`

Top level statements are quite a hassle when it comes to testing.
If you look at the tests we provide, they generally look like this:

:::code{caption="Some test file"}

```python
import pytest
import student


def test_some_function():
    # ...
```

:::

The second line, `import student`, tells Python we will be referencing the code written in `student.py`.
However, importing will also cause the top level statements to be executed.
This is problematic: first your application will run, and only when it finishes will the tests run.

We need a way to distinguish between these two scenarios:

* A Python file is being executed from the shell and we want the top level statements to be executed.
* A Python file is being imported from another Python file in which case we *don't* want the top level statements to be executed.

This can be achieved using the following trick:

:::code{caption="script.py"}

```python
def main():
    print('Hello!')


if __name__ == '__main__':
    main()
```

:::

How it works exactly is not important, what matters is its effect: `main` will only be called if the script is directly ran from the shell, which is exactly what we need.

:::INFO
We refer those interested in what `__name__` does to [this page](https://docs.python.org/3/library/__main__.html).
:::

## Shebang

Running our script still requires going to the shell and entering

:::code{caption="Bash"}

```bash
$ py app.py
```

:::

You have to remember that the OS does not know anything about Python.
As far as the OS knows, `app.py` is just a text file like any other, and `py` is just some executable.
*We* know that `py` is actually the Python interpreter and `app.py` contains Python code, so we know to tell the OS to combine both: "launch `py` and have it run `app.py`".

There is another way to tell the OS that `app.py` should be fed to `py`: if the first line of a file contains a [shebang (`#!`)](https://en.wikipedia.org/wiki/Shebang_(Unix)), the OS will take this as a hint about how to run that file:

:::code{caption="app.py"}

```python
#!/usr/bin/env py

def main():
    print('Hello!')


if __name__ == '__main__':
    main()
```

:::

Here, the first line informs the OS that if the user wishes to launch `app.py`, it should actually launch `py` instead and feed it `app.py`.

::::INFO
Those using Linux or MacOS need to tell the OS that it's okay to execute `app.py`.
This is achieved as follows:

:::code{caption="Bash"}

```bash
$ chmod +x app.py
```

:::

This marks the file as executable and needs only to be done once.

::::

After adding a shebang (and making the file executable on OSses that require it), you should be able to run your script by simply writing `./app.py` instead of `py app.py`.

::::INFO
On MacOS and Linux, you should also be able to double click it from a graphical user manager.

Windows works differently: if you want to be able to run your Python application from File Explorer or using a shortcut, you'll have to [associate `.py` files with `python.exe`](https://support.microsoft.com/en-us/windows/change-default-programs-in-windows-e5d82cad-17d1-c53b-3505-f10a32e1894d).
Normally, this association should already have been established for you by the Python installer.
::::

## Summary

If you'd like your script to be runnable, use the following pattern:

:::code{caption="app.py"}

```python
#!/usr/bin/env py

def main():
    # Startup code

if __name__ == '__main__':
    main()
```

:::
