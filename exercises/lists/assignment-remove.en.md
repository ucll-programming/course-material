# Removing Elements

:::TASK
Write a function `remove(xs, item_to_remove)` that removes all occurrences of `item_to_remove` in `xs`.
It has to modify `xs` in place.

Make sure your algorithm works efficiently.
We added a special test case that will time out if your code is too slow.
:::

:::USAGE

```python
>>> xs = [1, 2, 3, 2, 1]
>>> remove(xs, 2)
>>> xs
[1, 3, 1]
```

:::

:::HINT
Be careful if you process the list from left to right: you don't want to accidentally jump over elements.
:::
