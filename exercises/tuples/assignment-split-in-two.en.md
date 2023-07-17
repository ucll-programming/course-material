# Splitting in Two

We wish two split tuples in two equal sizes.
If the tuple contains an odd number of elements, the left half should contain one more element.

:::TASK
Write a function `split_in_two(xs)` that returns the left and right halves of `xs` in a tuple.
:::

:::USAGE

```python
>>> split_in_two((1, 2, 3, 4))
((1, 2), (3, 4))

# In case of odd size, put the extra element in left half
>>> split_in_two((1, 2, 3, 4, 5))
((1, 2, 3), (4, 5))
```

:::
