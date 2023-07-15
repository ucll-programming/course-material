# Greet Script

You should be incredibly proud of your `interactive_greet`.
So proud, in fact, that you can't wait to show it to your parents.

However, right now, `interactive_greet` is a Python function.
In order to call it, you'd have to start up a Python shell, load your code and call `interactive_greet`.
You would like to turn `interactive_greet` into a standalone application, i.e., a script we can call from Bash (or any other OS shell, such as PowerShell) like this:

:::code{caption="Bash"}

```bash
$ py greet.py
What is your name? Dexter Morgan
Hello, Dexter Morgan!
```

:::

To achieve this, we can rely on *top level statements*.
These are statements in your Python file that appear at the top level, i.e., outside functions.

:::code{caption="script.py"}

```python
# This is a top level statement
print("Hello!")

def hello():
    # This is not a top level statement because it's contained within a function
    print("Hello!")
```

:::

Running a Python script from the shell (e.g. `$ py script.py`) will cause all top level statements to be executed.
If your script contains only function definitions and no top level statements, running the script will do nothing.

:::TASK

* Create a new file `greet.py`.
* Add all relevant code.
* At the bottom, add a top level statement that calls `interactive_greet`.
* In Bash, run `$ py greet.py` and check that your script works as intended.

:::
