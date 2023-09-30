# Remove Duplicate Lines

:::TASK
Write a function `remove_duplicate_lines(source, destination)` that removes adjacent duplicate lines from a file named `source` and writes the result to a new file named `destination`.
:::

:::USAGE

```python
# Say input.txt contains the following lines:
#    a
#    a
#    b
#    b
#    b
#    a
#    c
#    c

>>> remove_duplicate_lines("input.txt", "output.txt")

# output.txt now contains
#    a
#    b
#    a
#    c
```

:::
