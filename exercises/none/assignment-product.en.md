# Product

:::TASK
Write a function `product(a, b, c)` that computes the product for the three given parameters.
However, some values might be missing, i.e., might have a `None` values.
These should be ignored while computing the product.

If all values are missing, return `1`.
:::

:::USAGE

```python
>>> product(2, 3, 4)
24

>>> product(None, 3, 5)
15
```

:::

:::HINT
Check each parameter in turn.
If it equals `None`, you can overwrite it with `1`.
:::
