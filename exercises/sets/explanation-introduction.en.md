# Introduction

## Benchmarking List Operations

Let's have fun with a little benchmarking.
The file `benchmark-lists.py` measures the time of several list-related operations.
You can run it on your own machine if you'd like.
These are the results when we run it:

::::div{.formatted-table}
:::center

| Operation | Time |
| ------- | ------- |
| Add element at beginning of list | 2.38s |
| Add element at end of list | 0.004s |
| Remove element at beginning of list | 0.59s |
| Remove element at end of list | 0.007s |

:::
::::

::::INFO
Note that the absolute times do not mean much: each operation is repeated thousands of times.
What matters is how the times relate to each other.
::::

As you can see, operations at the beginning of the list are dramatically slower compared to those taking place at the end of the list.
What could be the reason behind this phenomenon?

It's actually very simple: when adding/removing an item at the beginning of a list, all subsequent elements have to be shifted right or left.
This overhead does not exist when adding/removing at the end of the list.

## Data Structures

A list is a kind of [*data structure*](https://en.wikipedia.org/wiki/Data_structure).
A data structure provides a number of *operations*.
For example, a list allows indexing, adding and removing elements, looking for elements, etc.

As shown above, these operations can differ in speed.
The [*time complexity*](https://en.wikipedia.org/wiki/Time_complexity) of an operation describes how much time each operation takes.
This is actually quite a complicated subject; we won't go into the details here.
Instead, we'll simply make the distinction between *slow* operations and *fast* operations.
For example, insertion and deletion are *slow* when done at the front of the list, but *fast* when done at the end.

## Membership Testing

Let's examine the operation `x in lst`, i.e., checking whether `x` occurs in `lst`.
Is this a slow or a fast operation?

There is no magic or special trickery involved in the operation.
In essence, it performs the following algorithm:

:::code{caption="Python"}

```python
for item in lst:
    if item == x:
        return True
return False
```

:::

In other words, it goes through the list, compares `x` with each item, and if some item turns out to be equal to `x`, `x in lst` returns `True` and `False` otherwise.
This is a slow operation: think of having to find a term in an encyclopedia that isn't alphabetically sorted.
Sadly, we cannot do better than this: lists are inherently slow when it comes to membership checking.

## Sorted Lists

Looking up something in an encyclopedia is efficient because it is alphabetically sorted, which allows us to perform a [binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm).
Maybe we can apply a similar trick to lists?

There is nothing that keeps us from doing exactly that.
If it is *guaranteed* that the list is sorted, then `x in lst` can rely on the binary search algorithm, making it a fast operation.
However, in order to provide that guarantee, we have to make sure that every other operation keeps the list sorted.
This means we have to make some sacrifices.

For example, `append(x)` has to be dropped, as it adds an item to the *end* of the list, which could jeopardize the sorted nature of the list.
We can replace it with an `add(x)` operation that adds `x` to the list, but at the "right" position.

In short, in order to have a sorted list, we'll have to give up the ability to choose the actual location of items in the list.
We cannot make `[3, 1, 2]` anymore, only `[1, 2, 3]`.
In return, we get a fast `in` operation.

This sorted list is a separate kind of data structure, as it provides a different set of operations, with different time complexities.
The `in` on regular lists is *slow*, but `in` on sorted lists is *fast*.

## Sets

A *set* is yet another data structure.
It is very similar to a sorted list, except it's even faster.
But, just like with sorted lists, it comes at a price.

The good news about sets is that the basic operations are very fast.
`benchmark-sets.py` contains some benchmarking code:

::::div{.formatted-table}
:::center

| Operation | Set Time |
| ------- | ------- |
| Adding an item | 0.006s |
| Removing an item | 0.009s |
| Membership | 0.007s |

:::
::::

The bad news:

* No more indexing: you have no control over the order of the items.
* No duplicates allowed: every item can appear only once in a set.

Choosing to use a set is typically done for purposes of efficiency: a list can do everything a set can do, just more slowly.

## Python Sets

Sets are deemed important enough for Python to have them [built-in](https://docs.python.org/3/tutorial/datastructures.html#sets).
Here is a quick overview:

::::div{.formatted-table}
:::center

| Syntax | Description |
| ------- | ------- |
| `{1, 2, 3}` | Set literal |
| `len(s)` | Number of items in set |
| `s.add(x)` | Add `x` to set `s` |
| `s.remove(x)` | Remove `x` from set `s` |
| `x in s` | Check if `x` is an element of `s` |

:::
::::

::::IMPORTANT
Note that the empty set cannot be written `{}`, you have to use `set()`.

The reason for this is that dictionaries use the same curly braces.
If there's at least one element, the syntax gives away if the literal is meant to denote a set or a dictionary:

* `{value}` is a set.
* `{key: value}` is a dictionary.

However, when no items are listed, both set and dictionary syntax reduce to `{}`.
To resolve this ambiguity, Python chooses to see `{}` as a dictionary and lets you use `set()` for an empty set.
::::
