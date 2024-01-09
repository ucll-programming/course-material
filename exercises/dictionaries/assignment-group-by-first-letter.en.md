# Group By

:::TASK
Write a function `group_by_first_letter(strings)` that groups strings by their first letter and returns the results as a `dict`:

* The keys must be *uppercase* letters.
* The values must be the sublist of `strings` that start with the corresponding key.
  The strings must appear in the same order as in `strings`.
* Only those letters that actually occur as first letter in `strings` should be included as keys.
  In other words, all values should be nonempty lists.
* `strings` will only contain nonempty strings that start with letters.
:::

:::USAGE

```python
>>> group_by_first_letter(['Anne', 'Albert', 'aardvark', 'Boris', 'Chris'])
{
    'A': ['Anne', 'Albert', 'aardvark'],  # Appear in same order as in argument
    'B': ['Boris'],
    'C': ['Chris']
    # Note: no D, E, F, ...
}
```

:::
