# Insertion

`dict`s are *mutable*, i.e., they can be modified.
For example, we can add new key/value pairs to an existing `dict` as follows:

:::code{caption="Python"}

```python
# We start with empty dict
my_dict = {}

my_dict['a'] = 1
my_dict['b'] = 2
my_dict['c'] = 3
```

:::

After executing this code, `my_dict` equals `{'a': 1, 'b': 2, 'c': 3}`.

It is also possible to overwrite existing associations:

:::code{caption="Python"}

```python
my_dict['a'] = 5
my_dict['b'] *= 2
```

:::

Now `my_dict` equals `{'a': 5, 'b': 4, 'c': 3}`.
