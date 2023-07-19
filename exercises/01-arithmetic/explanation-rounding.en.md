# Rounding

You can turn a floating point number into an integer by rounding it.
There are three ways to perform rounding:

::::div{.formatted-table}
:::center

| Math | Python | Description |
| ---- | ------ | ----------- |
| $\lfloor x \rfloor$ | `floor(x)` | Rounding down |
| $\lceil x \rceil$ | `ceil(x)` | Rounding up |
| | `round(x)` | Rounding to nearest integer |

:::
::::

::::IMPORTANT
`floor` and `ceil` are not available by default: you first need to *import* them using the following code:

:::code{caption="Python"}

```python
from math import floor, ceil
```

:::

Imports are generally put at the top of the `.py` file.

::::

Let's see the three functions in action:

:::code{caption="Python Shell"}

```python
>>> from math import floor, ceil
>>> floor(4.9)
4

>>> ceil(2.4)
3

>>> round(8.49)
8

>>> round(8.51)
9
```

:::
