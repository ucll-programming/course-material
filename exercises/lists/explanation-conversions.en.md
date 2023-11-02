# Conversions

Strings, tuples and lists are all very similar:

* They represent a sequence of items.
* They can be indexed: `xs[index]`.
* They have a length: `len(xs)`.
* Many operations (`min`, `max`, etc.) can be applied on them.

::::INFO
You might wonder why Python bothers having all three.
Why not just lists?

* Strings are in essence tuples that contain characters.
  They exist as a separate type for efficiency reasons: they have a very specialized, optimized implementation.
* Tuples are useful because they're immutable.
  This may seem like a drawback, but in reality, this property can simplify things *a lot*.
::::

Using `str(x)`, `tuple(x)` and `list(x)` you can convert `x` to a string, tuple or list, respectively.

## `str`

We already discussed `str`.
It can be applied on (as good as) any value `x` to build a string representation of `x`.

::::EXAMPLE

:::code{caption="Python Shell"}

```python
>>> str([1, 2, 3])
"[1, 2, 3]"

>>> str((1, 2, 3))
'(1, 2, 3)'
```

:::

::::

## `tuple`

`tuple(x)` requires `x` to be *iterable*.
What this means exactly will be discussed later, but for now you can imagine it refers to any kind of value that contains multiple values, which includes strings, tuples and lists.

Given an iterable value `x`, `tuple(x)` will take all values stored in `x` and put them in a tuple.

::::EXAMPLE

:::code{caption="Python Shell"}

```python
# Converts string to tuple
>>> tuple("abcd")
("a", "b", "c", "d")

# Converts tuple to tuple, not very useful
>>> tuple((1, 2, 3, 4))
(1, 2, 3, 4)

# Converts list to tuple
>>> tuple([1, 2, 3, 4])
(1, 2, 3, 4)
```

:::

::::

## `list`

Just like `tuple`, `list(x)` needs `x` to be iterable.
It works like you would expect: it takes all items in `x` and puts them in a list.

::::EXAMPLE

:::code{caption="Python Shell"}

```python
# Converts string to list
>>> tuple("abcd")
["a", "b", "c", "d"]

# Converts tuple to list
>>> list((1, 2, 3, 4))
[1, 2, 3, 4]

# Converts list to list, can be used to make a copy
>>> list([1, 2, 3, 4])
[1, 2, 3, 4]
```

:::

::::
