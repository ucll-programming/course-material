# Removing Items

There are two ways to remove items from lists:

* Either you specify the *index* of the item to be removed, or
* You specify the value of the item to be removed.

## `pop`

`lst.pop(index)` removes the item at the given `index`.
You can omit `index` in which case the last element will be removed.

::::EXAMPLE

:::code{caption="Python Shell"}

```python
>>> xs = [1, 2, 3, 4, 5]
>>> xs.pop(1)
>>> xs
[1, 3, 4, 5]

>>> xs.pop()
>>> xs
[1, 3, 4]
```

:::
::::

## `del`

`del` is a keyword and has a syntax of its own.
Functionality-wise it is a more powerful version of `pop`.

`del lst[index]` does the same as `lst.pop(index)`: it removes the item with the given index.
However, `del` also works with slices: `del lst[start:stop]` removes all items from `start` to `stop`.

::::EXAMPLE

:::code{caption="Python Shell"}

```python
>>> xs = [1, 2, 3, 4, 5]
>>> del xs[-1]
>>> xs
[1, 2, 3, 4]

>>> del xs[:2]
>>> xs
[3, 4]
```

:::
::::

## `remove`

Lastly, we have `lst.remove(item)` which removes the *first* occurrence of `item`.

::::EXAMPLE

:::code{caption="Python Shell"}

```python
>>> xs = [6, 4, 2, 3, 4, 9, 4]
>>> xs.remove(2)
>>> xs
[6, 4, 3, 4, 9, 4]

>>> xs.remove(4)
>>> xs
[6, 3, 4, 9, 4]
```

:::
::::
