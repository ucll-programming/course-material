# Contains Equal Neighbors

:::code{caption="Python"}

```python
def contains_equal_neighbors(xs):
    for i in range(len(xs)):
        if xs[i] != xs[i+1]:
            return False
    return True
```

:::

::::TASK
`contains_equal_neighbors(xs)` should check if the list `xs` contains two consecutive elements that are equal.
::::

::::USAGE

```python
>>> contains_equal_neighbors([])
False

>>> contains_equal_neighbors([5])
False

>>> contains_equal_neighbors([1, 1])
True

>>> contains_equal_neighbors([1, 2])
False

>>> contains_equal_neighbors([1, 2, 3, 4, 4, 5])
True
```

::::
