# Move Elements

:::code{caption="Python"}

```python
def move_elements(xs, new_positions):
    for i in range(len(new_positions)):
        j = new_positions[i]
        xs[j] = xs[i]
```

:::

The function `move_elements(xs, new_positions)` moves the elements of `xs` around as described by `new_positions`.

* `xs` is a list.
* `new_positions` is a list containing the numbers `0` to `len(xs) - 1` and represents the new positions for the elements in `xs`.

Say `new_positions[0]` contains the value `1`.
This means that the value in `xs[0]` should be moved to `xs[1]`.
Put more generally, if `new_positions[i]` contains `j`, then `xs[i]` should be moved to `xs[j]`.
See below for more examples.

::::TASK
Fix the given implementation to make the tests pass.
::::

::::USAGE

```python
>>> xs = ['a', 'b']
# Move 0 -> 0
#      1 -> 1
>>> move_elements(xs, [0, 1])
>>> xs
['a', 'b']

# Move 0 -> 1
#      1 -> 0
>>> move_elements(xs, [1, 0])
>>> xs
['b', 'a']

>>> xs = ['a', 'b', 'c']
# Move 0 -> 2
#      1 -> 1
#      2 -> 1
>>> move_elements(xs, [2, 1, 0])
>>> xs
['c', 'b', 'a']

>>> xs = ['a', 'b', 'c', 'd', 'e']
# Move 0 -> 3
#      1 -> 1
#      2 -> 2
#      3 -> 4
#      4 -> 0
>>> move_elements(xs, [3, 1, 2, 4, 0])
>>> xs
['e', 'b', 'c', 'a', 'd']
```

::::
