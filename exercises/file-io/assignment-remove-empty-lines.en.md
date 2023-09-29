# Remove Empty Lines

:::TASK
Write a function `remove_empty_lines(source, destination)` that removes the empty lines from the path `source` and writes the result to the path `destination`.
If a line has spaces in it, it does not count as an empty line.
:::

:::USAGE

```python
>>> source = 'example.txt'
>>> destination = 'output.txt'
>>> with open(source, 'w') as f:
...     f.write('\nLine 1\nLine 2\n\nLine 2\n  \n')

>>> remove_empty_lines(source, destination)

>>> with open(destination, 'r') as f:
...     f.read()
'Line 1\nLine 2\nLine 2\n  \n'
```

:::
