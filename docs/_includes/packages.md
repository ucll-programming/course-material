In a shell (the directory is unimportant here), write

```bash
$ pip install pytest pytest-timeout mypy pipx
```

If you're running MacOS and encounter problems with this command, you can also try:

```bash
$ python3 -m pip install pytest pytest-timeout mypy pipx
```

## Checking the Installation

Open a shell in **the `scripts` directory** and enter (only the first line! The subsequent lines are expected output)

```bash
# Inside the course-material/scripts directory
$ pytest
..                               [100%]
2 passed in 0.01s
```

If you get the same output, you have successfully installed the Python packages.
Otherwise, ask a lecturer for help.
