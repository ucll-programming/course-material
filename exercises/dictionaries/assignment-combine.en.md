# Combine

Say we have a dictionary that translates English to Dutch, e.g., `{ 'cat': 'kat', 'dog': 'hond', ... }`.
We also have a dictionary that translates Dutch into French, e.g., `{ 'kat': 'chat', 'hond': 'chien' }`.
We now wish to build a English-French translating dictionary by combining the two above, e.g., `{ 'cat': 'chat', 'dog': 'chien', ... }`.

:::TASK
Write a function `combine(d1, d2)` that returns a new dictionary:

* Looking up `key` in the resulting dictionary must be the same as looking up `key` in `d1` and then looking up the corresponding value in `d2`.
  In short: `result[key] == d2[d1[key]]`.
* It is possible that `d1[key]` does not appear in `d2`.
  For example, say `d1` equals `{ 'elephant': 'olifant' }` and `d2` equals { `zeehond', 'phoque' }`.
  The Dutch-French dictionary does not contain a translation for `olifant`, so neither should the combined dictionary.
:::

:::USAGE

```python
>>> d1 = {
        'cat': 'kat',
        'dog': 'hond',
        'elephant': 'olifant'
    }
>>> d2 = {
        'kat': 'chat',
        'hond': 'chien',
        'zeehond': 'phoque'
    }
>>> combine(d1, d2)
{
    'cat': 'chat',
    'dog': 'chien'
    # Note: no elephant because d2 does not contain the right translation
}
```

:::
