# Pad Right

::::TASK
Write the function `pad_right(xs, length, padding)` that given a list `xs`, a desired length `length`, and a padding value `padding`, modifies the list in place, with the `padding` value added to the right, as many times as necessary to make its length equal to `length`.
::::

::::USAGE

```python
>>> xs = [1, 2, 3, 4]
>>> pad_right(xs, 8, 'x')
>>> xs
[1, 2, 3, 4, 'x', 'x', 'x', 'x']
```

```python
>>> xs = [1, 2, 3, 4]
>>> pad_right(xs, 8, 0)
>>> xs
[1, 2, 3, 4, 0, 0, 0, 0]
```

::::
