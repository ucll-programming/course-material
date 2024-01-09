# Counts

:::TASK
Write a function `counts(xs)` that returns the frequencies of the elements of `xs` as a `dict`:

* All elements in `xs` must appear as key in the resulting `dict`.
* `result[x]` must equal the number of times `x` occurs in `xs`.
:::

:::USAGE

```python
>>> counts(['a', 'b', 'b', 'c', 'c', 'c'])
{
    'a': 1,
    'b': 2,
    'c': 3
}
```

:::

:::INFO
This functionality [already exists](https://docs.python.org/3/library/collections.html#counter-objects) in Python's standard library.
Don't rely on it though for solving this exercise.
:::
