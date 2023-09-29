# Remove Duplicate Lines

:::TASK
Write a function `remove_duplicate_lines(source, destination)` that removes duplicate lines that are adjacent from the path `source` and writes the result to the path `destination`.
:::

:::USAGE

```python
>>> source = 'example.txt'
>>> destination = 'output.txt'
>>> with open(source, 'w') as f:
...     f.write('Line 1\nLine 1\nLine 2\nLine 3\nLine 2\n')

>>> remove_duplicate_lines(source, destination)

>>> with open(destination, 'r') as f:
...     f.read()
'Line 1\nLine 2\nLine 3\nLine 2\n'
```

:::
