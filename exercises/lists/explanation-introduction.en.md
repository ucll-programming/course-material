# Introduction

Tuples are *immutable*: once created, they cannot be changed: we cannot remove, add or overwrite elements.
This immutability can be a strength, but in other cases it can be quite an impediment.

*Lists* are very much like tuples, except they can be modified.

## Literals

A list literal has the following syntax:

:::code{caption="Python Shell"}

```python
>>> lst = [1, 2, 3, 4]
```

:::

As you can see, the only difference lies in the brackets: square brackets for lists, round brackets for tuples.
The list with one item also requires no trickery: `[1]` works just fine.

## Tuple Functionality

All functionality available on tuples also works on lists: `len`, indexing, slicing, `sum`, `min`, `max`, iteration, destructuring, etc. all work without change.
Actually, all code you write that interacts with tuples will behave the same if given lists.
Tuples have a *subset* of the functionality of lists.
