# Enumerating

As of yet, we've seen two ways to retrieve information from a dictionary:

* `d[key]` looks up the value associated with `key`.
* `key in d` tells you whether `d` contains a certain `key`.

Remark how you always need a key to start with.
If you have no key handy, you can't do much with the `dict`, apart from trying to guess which keys it contains.

## `keys()`

Luckily, `dict`s allow you to ask for a list of keys:

:::code{caption="Python Shell"}

```python
>>> d = {'a': 1, 'b': 2}
>>> d.keys()
dict_keys(['a', 'b'])
```

:::

While `keys()` does not really return a `list`, you can think of the result as one.

::::INFO
Why does `keys()` not simply return a `list`?
Consider the following code:

:::code{caption="Python Shell"}

```python
>>> d = {'a': 1, 'b': 2}
>>> keys = d.keys()
>>> keys
dict_keys(['a', 'b'])

>>> d['c'] = 3
>>> keys
dict_keys(['a', 'b', 'c'])
```

:::

If `keys()` were to return `list`, it would contain a copy of the keys that are present at the moment you call `keys()`.
Adding new keys to the `dict` later would not affect the `list`.
The `list` is "dumb": it is not aware that its contents come from a `dict`.

A `dict_keys` object is very much *like* a list, but it is "smarter": it *knows* its items are keys of a `dict` and will keep itself synchronized.
In other words, if you were to add or remove keys after calling `keys()`, this change would be reflected in the `dict_keys` object.

::::

## `values()`

`dict`s also provide you with a `values()` method, which returns a "list" of values:

:::code{caption="Python Shell"}

```python
>>> d = {'a': 1, 'b': 2}
>>> d.values()
dict_values([1, 2])
```

:::

## `items()`

Say you want to iterate over all key/value pairs.
You can achieve this using

:::code{caption="Python"}

```python
for key in d.keys():
    value = d[key]
    # ...
```

:::

However, you achieve the same more efficiently using `items()`:

:::code{caption="Python"}

```python
for key, value in d.items():
    # ...
```

:::

This way, you don't have to manually look up every key.

::::INFO
In essence, `items()` returns a list of pairs, i.e., tuples of size 2.
The loop above relies on automatic destructuring.
It is equivalent with

:::code{caption="Python"}

```python
for pair in d.items():
    key = pair[0]
    value = pair[1]
    # ...
```

:::

::::
