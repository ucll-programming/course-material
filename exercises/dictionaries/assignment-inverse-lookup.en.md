# Inverse Lookup

Dictionaries are data structures optimized for finding a value associated with a given key.
Finding which key leads to a specific value, however, is much slower and needs to be done manually.

While a key can only occur once in a dictionary, the same is not true for values.
Consider for example `{'a': 1, 'b': 1}`: here the value `1` appears twice.
This makes inverse lookup a bit trickier: multiple solutions are possible.

:::TASK
Write a function `inverse_lookup(dictionary, value)` that returns a list of keys for which `dictionary[key] == value`.
The order in which you return the keys is not important.

If `value` does not occur in `dictionary` as a value, return the empty list.
:::

:::USAGE

```python
>>> inverse_lookup({'a': 1, 'b': 1, 'c': 2}, 1)
['a', 'b']

>>> inverse_lookup({'a': 1, 'b': 1, 'c': 2}, 2)
['c']

>>> inverse_lookup({'a': 1, 'b': 1, 'c': 2}, 3)
[]
```

:::
