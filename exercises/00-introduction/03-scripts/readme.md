# Scripts

While it is technically possible to develop your Python projects using the shell, it would be a rather awkward experience.
Instead, Python code is typically written in a file (typically called a *Python script*) after which you tell Python to execute all commands written in that script.

Using VSCode, create a file named `my-script.py` and add the following code to it:

```python
1 + 2
```

## Running your Script

Now that you've written a Python script, you'll want to tell Python to run it.
How this is done is OS specific.

TODO Better explanations

Open a terminal in the same directory as `my-script.py` and enter the following commands

```bash
# If you're on Windows
$ py my-script.py

# If you're on MacOS
$ python3 my-script.py

# If you're on Linux
$ python my-script.py
```

Hmm, it does not appear to do anything.
We kind of hoped it would output `3`...

When using the Python shell, Python will always print out the result of the last evaluation.
This is not true for a script.
This is also makes perfect sense: imagine playing a game while having Python print out the results of all millions of calculations performed.

So, when using scripts, you have to explicitly ask Python to print out the result.

Change the contents of `my-script.py` to

```python
print(1 + 2)
```

Now run it again.

```bash
# Use the right command for your OS
$ py my-script.py
3
```
