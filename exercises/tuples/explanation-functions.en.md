# Functions

## `min` and `max`

Both `min` and `max` know how to handle tuples.
When you pass either function a single argument, they expect it to be an iterable.
They then proceed to find the lowest/highest value.

::::EXAMPLE
:::code{caption="Python Shell"}

```python
>>> min((5, 2, 3, 9))
2

>>> max((5, 2, 3, 9))
9
```

:::
::::

## `sum`

The built-in function `sum` allows you to compute the sum of all items in an iterable collection, such as a tuple.
(Later we will also discuss lists, sets and generators; `sum` will also work on them.)

::::EXAMPLE
:::code{caption="Python Shell"}

```python
>>> sum((5, 2, 3, 9))
19
```

:::
::::

## `sorted`

The function `sorted(t)` returns a sorted copy of `t`.

::::EXAMPLE

:::code{caption="Python Shell"}

```python
>>> sorted((4, 2, 9, 1, 3))
(1, 2, 3, 4, 9)
```

:::
::::

There's a caveat though: the values in `t` must be comparable to each other.
If you mix different types of values, the sorting will lead to an error.
When sorting, it is best to stick to tuples where all elements have the same type,

::::EXAMPLE

:::code{caption="Python Shell"}

```python
>>> sorted((4, "5", 9, 1, 3))
TypeError: '<' not supported between instances of 'str' and 'int'
```

:::
::::
