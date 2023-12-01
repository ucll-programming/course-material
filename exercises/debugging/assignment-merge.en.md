# Merge

:::code{caption="Python"}

```python
def merge(xs, ys):
    result = []
    i = 0
    j = 0
    while i < len(xs) or j < len(ys):
        if xs[i] < ys[j]:
            result.append(xs[i])
            i += 1
        else:
            result.append(ys[j])
            j += 1
    result.extend(xs[i:])
    result.extend(ys[i:])
    return result
```

:::

::::TASK
`merge(xs, ys)` takes two *sorted* lists and should return a new list that contains all elements from `xs` and `ys` in sorted order.
Fix the given implementation.
::::

::::USAGE

```python
>>> merge([1, 3, 5], [2, 4, 6])
[1, 2, 3, 4, 5, 6]
```

::::
