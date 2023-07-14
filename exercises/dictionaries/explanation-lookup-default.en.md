# Lookup With Defaults

Say you have a `dict` that represents the contents of your pantry:

:::code{caption="Python"}

```python
pantry = {
    'sugar': 200,
    'eggs': 5,
    'flour': 750
}
```

:::

You intend to bake some dessert and need to know if you have enough eggs.
The dessert requires four eggs, so you perform the following check:

:::code{caption="Python"}

```python
if pantry['eggs'] >= 4:
    # Enough eggs
```

:::

But what if you check for vanilla beans?

:::code{caption="Python"}

```python
if pantry['vanilla beans'] >= 1:
    # ...
```

:::

This will lead to a crash: you can only look up using an existing key.
To prevent a crash, you would need to write

:::code{caption="Python"}

```python
if 'vanilla beans' in pantry and pantry['vanilla beans'] >= 1:
    # ...
```

:::

That's a lot of typing for something relatively trivial.
Luckily, there exist better solutions.

## `get`

`dict`s have a method named [`get`](https://docs.python.org/3/library/stdtypes.html#dict.get).
`d.get(key)` behaves exactly the same as `d[key]`, but it takes an optional second parameter: a default value in case `key` does not appear in `d`.

:::code{caption="Python Shell"}

```python
>>> pantry = {
    'sugar': 200,
    'eggs': 5,
    'flour': 750
}

>>> pantry['vanilla beans']
KeyError: 'vanilla beans'

>>> pantry.get('vanilla beans')
KeyError: 'vanilla beans'

>>> pantry.get('vanilla beans', 0)
0
```

:::

As you can see, `get` allows you to succinctly express that a missing ingredient in the ingredient is the same as having 0 of that item.
Therefore, the check above can be rewritten as

:::code{caption="Python"}

```python
if pantry.get('vanilla beans', 0) >= 1:
    # ...
```

:::

## `setdefault`

A very similar method to `get` is [`setdefault`](https://docs.python.org/3/library/stdtypes.html#dict.setdefault).
Contrary to what its name may lead you to believe, `d.setdefault(key, if_missing)` actually performs a lookup, just like `d.get(key, if_missing)`.
The difference is in what happens if `key` is missing: while `get` simply returns the `if_missing` value, `setdefault` will actually add it to the `dict`:

:::code{caption="Python Shell"}

```python
>>> pantry = {
    'sugar': 200,
    'eggs': 5,
    'flour': 750
}

>>> pantry.get('vanilla beans', 0)
0

# As you can see, pantry is still unchanged
>>> pantry
{
    'sugar': 200,
    'eggs': 5,
    'flour': 750
}

# setdefault also returns the default in case the key is absent
>>> pantry.setdefault('vanilla beans', 0)
0

# setdefault added an extra key/value pair to the dict
>>> pantry
{
    'sugar': 200,
    'eggs': 5,
    'flour': 750,
    'vanilla beans': 0
}

```

:::

:::INFO
More advanced students might like to know about [`defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict).
This is a special kind of `dict` that allows you to define an `if_missing` value at creation.
Every lookup `d[key]` is then equivalent to `d.get(key, if_missing)`.
The main advantage is that you only need to define the `if_missing` value once (i.e., at creation) instead at every lookup.
:::
