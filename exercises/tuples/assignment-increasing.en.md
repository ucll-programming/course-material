# Increasing

A sequence is *increasing* if every value is at least as great as the one preceding it.

:::TASK
Write a function `increasing(ns)` that returns `True` if `ns` is increasing and `False` otherwise.
:::

:::USAGE

```python
>>> increasing((1, 2, 4, 9))
True

>>> increasing((1, 2, 4, 3))
False

# Equal elements are allowed
>>> increasing((1, 1, 1))
True

# Empty sequence is considered increasing
>>> increasing(())
```

:::
