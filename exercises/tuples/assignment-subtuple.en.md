# Subtuple

A subtuple of a tuple `xs` is a tuple that contains a contiguous part of `xs`.
For example, `(2, 3, 4)` is a subtuple of `(1, 2, 3, 4, 5)`.

::::TASK
Write a function `subtuple(xs, ys)` that checks if `ys` is a subtuple of `xs`.
::::

::::USAGE

```python
>>> subtuple((1, 2, 3, 4, 5), (2, 3, 4))
True

# Must be contiguous
>>> subtuple((1, 2, 3, 4, 5), (1, 3, 4))
False

>>> subtuple((1, 2, 3, 4, 5), (1, 2, 3, 4, 5))
True

>>> subtuple((1, 2, 3, 4, 5), ())
True
```

::::
