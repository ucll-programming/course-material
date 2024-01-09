# Pad Right

::::TASK
Write the function `pad_right(xs, length, padding)` that takes as parameters

* a list `xs`;
* a desired length `length`;
* a padding value `padding`.

`pad_right(xs, length, padding)` adds `padding` values to the end of the list such that `xs` ends up with `length` items.
If `xs` already contains `length` items (or more), nothing needs to be done.
::::

::::USAGE

```python
>>> xs = [1, 2, 3, 4]
>>> pad_right(xs, 8, 'x')
>>> xs
[1, 2, 3, 4, 'x', 'x', 'x', 'x']

>>> xs = [1, 2, 3, 4]
>>> pad_right(xs, 6, 0)
>>> xs
[1, 2, 3, 4, 0, 0]

>>> xs = [1, 2, 3, 4, 5, 6, 7, 8]
>>> pad_right(xs, 6, 0)
>>> xs
[1, 2, 3, 4, 5, 6, 7, 8]
```

::::
