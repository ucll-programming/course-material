# Adding Items

Lists provide two ways to add items to them.
We discuss each in turn.

## `append`

`lst.append(x)` adds an extra element to the end of the list.

::::EXAMPLE

:::code{caption="Python Shell"}

```python
>>> xs = [1, 2, 3]
>>> xs.append(4)
>>> xs
[1, 2, 3, 4]
```

:::
::::

## `insert`

If you need to add an element somewhere else than at the end, you can rely on the `insert` method.
`lst.insert(index, x)` adds an element `x` so that its index equals `index`.
All subsequent elements are shifted one position.

::::EXAMPLE

:::code{caption="Python"}

```python
>>> xs = [1, 2, 3, 4]
>>> xs.insert(0, 9)
>>> xs
[9, 1, 2, 3, 4]
```

:::
::::
