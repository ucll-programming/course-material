# Compact

You get a list that contains all kinds of values, some of which `None`.
We wish you to remove all these `None` values from the list.
The order of the remaining elements should remain the same.

There are two ways to approach this.

* You could modify the given list.
* You could construct a new list that is equal to the given list but without the `None` values.

We ask of you to implement both variants.

:::TASK
Write a function `compact(xs)` that removes all `None` values from `xs` and returns the result as a new list.
The function must leave `xs` untouched.
:::

:::USAGE

```python
>>> compact([1, None, 2, None, 3])
[1, 2, 3]
```

:::

:::TASK
Write a function `compact_in_place(xs)` that removes all `None` values from `xs` by modifying `xs`.
:::

:::USAGE

```python
>>> xs = [True, None, 5, "Hello", None]
>>> compact_in_place(xs)
>>> xs
[True, 5, "Hello"]
```

:::
