# Dunder Methods

We previously discussed the `__init__` method and how it had a special meaning.
There are other method names that Python assigns special meaning to.
They all have in common that their names are enclosed by two underscores: `__len__`, `__getitem__`, etc.
For this reason, they are sometimes referred to as *dunder methods*, where "dunder" is a shortened version of "double underscore".

Dunder methods allow your new type to fit in with the existing Python ecosphere.
We'll give a few examples to clarify what we mean by this.

## Custom Comparison

The `max` function returns the largest element of a sequence of elements.
But how does `max` know how to compare those elements?
It works on integers, floats, strings, etc.
Does it have specialized code for all of these types?

`max` actually relies on the `<` operator.
A possible implementation would be

:::code{caption="Python"}

```python
def max(items):
    if len(items) == 0:
        raise TypeError()
    result = items[0]
    for index in range(1, len(items)):
        current = items[index]
        if result < current:
            result = current
    return result
```

:::

So, as long as you present `max` with a list of objects that can be compared using `<`, it will be able to do its job.
But then this simply raises the question, how does `<` work?
How does it know how to compare objects?

The answer is simple: `x < y` is actually translated to `x.__lt__(y)`.
Implementing this method lets everyone know how to compare your custom objects.
`min`, `max`, `sort` and all other functionality relying on order will then be able to work with your own type.

## Other Examples

Python recognizes [many dunder methods](https://docs.python.org/3/reference/datamodel.html).
We give an incomplete list:

::::div{.formatted-table}
:::center

| Dunder Method | Computes |
| ------- | ------- |
| `x.__add__(y)` |`x + y` |
| `x.__sub__(y)` | `x - y` |
| `x.__neg__()` | `-x` |
| `x.__mul__(y)` | `x * y` |
| `x.__truediv__(y)` | `x / y` |
| `x.__floordiv__(y)` | `x // y` |
| `x.__mod__(y)` | `x % y` |
| `x.__pow__(y)` | `x ** y` |
| `x.__eq__(y)` | `x == y` |
| `x.__abs__()` | `abs(x)` |
| `x.__round__()` | `round(x)` |
| `x.__floor__()` | `floor(x)` |
| `x.__ceil__()` | `ceil(x)` |
| `x.__getitem__(key)` | `x[key]` |
| `x.__setitem__(key, value)` | `x[key] = value` |
| `x.__len__()` | `len(x)` |
| `x.__iter__()` | Used by `for` loops |

:::
::::
