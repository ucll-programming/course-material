# Membership Testing

Given a dictionary `d`, you can look up the value associated with some `key` using `d[key]`.
However, it is an error to look up a `key` that is not included in the dictionary:

:::code{caption="Python Shell"}

```python
>>> d = {'a': 1, 'b': 2}
>>> d['c']
KeyError: 'c'
```

:::

In order to prevent this error from occurring, we might want to first check if the dictionary does indeed contain an entry with `key`.
You can do this with the `in` operator:

:::code{caption="Python Shell"}

```python
>>> d = {'a': 1, 'b': 2}
>>> 'a' in d
True

>>> 'b' in d
True

>>> 'c' in d
False
```

:::

Note that `in` only works on keys.
You cannot look for values.

:::code{caption="Python Shell"}

```python
>>> d = {'a': 1, 'b': 2}
>>> 1 in d
False
```

:::
