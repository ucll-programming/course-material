# Conversion

Before discussing conversions, it is crucial that you understand there is a difference between the integer `15` and the string `"15"`.
It is the same difference as a painting of a pipe and an actual pipe.
Internally, the computer represents both in very different ways.
Mathematical operations can only be done if the value is stored as an actual `int`.

Fortunately, it is possible to switch between representations.

::::div{.formatted-table}
:::center

| Syntax | Description |
| ------ | ----------- |
| `int(x)` | Converts to `int` |
| `float(x)` | Converts to `float` |
| `bool(x)` | Converts to `bool` |
| `str(x)` | Converts to `bool` |

:::
::::

::::EXAMPLE

:::code{caption="Python Shell"}

```python
>>> int("15")
15

>>> str(845)
"845"
```

:::

::::

::::IMPORTANT
Watch out with `bool`:

:::code{caption="Python Shell"}

```python
>>> bool('True')
True

>>> bool('False')
True                # !!!
```

:::

The reason for this surprising result has to do with truthy vs falsey values.
Any nonempty string is considered truthy, so `bool(nonempty_string)` will always return `True`, regardless of the contents of the string.
Only `bool("")` will give you `False`.
::::
