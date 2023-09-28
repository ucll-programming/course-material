# For Loop

A very common loop pattern is

:::code{caption="Python"}

```python
i = 0
while i < i_max:
    # ...
    i += 1
```

:::

In other words, the loop body is executed for every value from `0` to `i_max`.
Such loops occur so often that many programming language provide a separate looping construct for it.
Python is no exception:

:::code{caption="Python"}

```python
for i in range(0, i_max):
    # ...
```

:::

Meet the `for` loop.
The loop shown above makes `i` go through all values of the `range(0, i_max)`, i.e., `0`, `1`, `2`, &hellip; `i_max - 1`.
Note: the variable name `i` can be freely chosen.

::::IMPORTANT
Note that `range(start, stop)` does not include `stop` itself.
::::

::::EXAMPLE

:::code{caption="Python Shell"}

```python
>>> for i in range(0, 3):
...    print(i)
0
1
2
```

:::

::::

## `range`

`range` exhibits a lot of similarities with slicing.

* `range(start, stop)` represents all integers from `start` to `stop` (exluding `stop` itself).
* `range(start, stop, step)` goes from `start` to `stop` with increments of `step`.
* `range(stop)` is the same as `range(0, stop)`.
* Negative `step` allows you to count backwards.
