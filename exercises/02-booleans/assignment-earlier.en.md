# Earlier

:::TASK
Write a function `earlier(h1, m1, h2, m2)` that returns `True` if the time `h1`:`m1` is earlier in the day than `h2`:`m2`, `False` otherwise.
:::

:::USAGE

```python
# 01:02 is earlier than 03:04
>>> earlier(1, 2, 3, 4)
True

# 00:00 is earlier than 01:00
>>> earlier(0, 0, 1, 0)
True

# 10:30 is not earlier than 10:29
>>> earlier(10, 30, 10, 29)
False
```

:::

:::HINT
As always, there are multiple ways to go about it.
We give two possible approaches:

* You can first compare the hours.
  If `h1 < h2`, the first time must be earlier.
  If `h1 == h2`, then you'll also need to compare `m1` and `m2`.
* You can convert both times to total amount of minutes since midnight.
  For example, 03:30 becomes 3 * 60 + 30 == 210.
  Comparing total amount of minutes leads straight to the right result.
:::
