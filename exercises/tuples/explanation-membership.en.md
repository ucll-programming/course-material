# Membership

To determine whether a tuple contains an element, you can use the `in` operator.

:::code{caption="Python Shell"}

```python
>>> 3 in (1, 2, 3, 4, 5)
True

>>> 6 in (1, 2, 3, 4, 5)
False
```

:::

::::IMPORTANT
`x in t` does not work recursively, by which we mean that if `t` contains another tuple, `in` will not look inside that nested tuple.

:::code{caption="Python Shell"}

```python
>>> 3 in (1, (2, 3))
False
```

:::
::::

::::IMPORTANT
The `in` operator could check for substrings when applied on strings:

:::code{caption="Python"}

```python
>>> 'relax' in 'rancho relaxo'
True
```

:::

This will not work with tuples:

:::code{caption="Python"}

```python
>>> (2, 3) in (1, 2, 3, 4)
False
```

:::

The `in` operator is stricter when dealing with tuples: `x in t` only returns `True` if there's an item of `t` that equals `x`.
::::
