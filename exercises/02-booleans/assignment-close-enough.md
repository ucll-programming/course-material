# Assignment

:::TASK
Write a function `close_enough(x, y)` that checks whether the two numbers `x` and `y` are "almost equal".
We say they are almost equal if they differ at most 5.
:::

:::USAGE

```python
>>> close_enough(0, 0)
True

>>> close_enough(1, 0)
True

>>> close_enough(5, 0)
True

>>> close_enough(6, 0)
False

>>> close_enough(54, 60)
False

>>> close_enough(100, 98)
True
```

:::