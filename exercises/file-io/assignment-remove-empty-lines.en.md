# Remove Empty Lines

:::TASK
Write a function `remove_empty_lines(source, destination)` that removes the empty lines from the file named `source` and writes the result to a new file named `destination`.
If a line has spaces in it, it does not count as an empty line.
:::

:::USAGE

```python
# Say input.txt contains the following lines:
#     a
#
#
#     b
#     c
#
#     d

>>> remove_empty_lines("input.txt", "output.txt")

# output.txt now contains
#     a
#     b
#     c
#     d
```

:::
