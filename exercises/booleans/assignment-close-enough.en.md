# Assignment

:::TASK
Write a function `close_enough(x, y)` that checks whether the two numbers `x` and `y` are "almost equal".
We say they are almost equal if they differ at most `0.1`.
:::

:::USAGE

```python
>>> close_enough(0, 0)
True

>>> close_enough(0, 0.05)
True

>>> close_enough(0, 0.1)
True

>>> close_enough(0, -0.1)
True

>>> close_enough(0, 0.2)
False

>>> close_enough(18.5, 18.6)
True
```

:::

:::HINT
Contrary to many other programming languages, it is possible to combine multiple comparisons.
For example, `a < b < c` is the same as `a < b and b < c`.
:::
