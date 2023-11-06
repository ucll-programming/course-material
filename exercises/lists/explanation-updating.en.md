# Updating

Accessing the items of a list is done the same way as with tuples, i.e., by indexing.

::::EXAMPLE

:::code{caption="Python Shell"}

```python
>>> lst = ["a", "b", "c", "d"]

# Fetch first item, which has index 0
>>> lst[0]
"a"

# Fetch last item, which has index -1
>>> lst[-1]
"d"
```

:::
::::

Using the syntax `lst[index] = x` you can *overwrite* the item at the given index.

::::EXAMPLE

:::code{caption="Python Shell"}

```python
>>> lst = [7, 4, 1, 9, 3]

# Overwrite first item
>>> lst[0] = 100
>>> lst
[100, 4, 1, 9, 3]

# Double the last item
>>> lst[-1] *= 2
>>> lst
[100, 4, 1, 9, 6]
```

:::
::::
