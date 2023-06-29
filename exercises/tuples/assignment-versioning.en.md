# Versions

Software often gets improved as time goes on.
To make the distinction between different versions, *version number* are often used.

A popular version scheme is [semantic versioning](https://en.wikipedia.org/wiki/Software_versioning#Semantic_versioning).
A version number consists of three parts, for example `3.9.5`.

* The first part (`3`) is called the *major* number.
* The middle part (`9`) is called the *minor* number.
* The last part (`5`) is called the *patch* number.

Whenever a new version comes out, one of these three parts must be incremented.
Semantic versioning means these rules are followed:

* We increase the major number (`3.9.5` &rarr; `4.0.0`) if the new version introduced *breaking changes*.
* We increase the minor number (`3.9.5` &rarr; `3.10.0`) if we added more features, but everything else remained the same.
* We increase the patch number (`3.9.5` &rarr; `3.9.6`) if we made small changes (e.g., optimizations, bug fixes).

:::EXAMPLE
Say we were to apply semantic versioning on a single function.

* Adding an extra parameter would be a *breaking change*: all code that calls this function will fail after this change due to a missing parameter.
  This must be signaled by increasing the major number.
* Adding an extra parameter with a default value does not break existing code but adds new functionality.
  Here, we increment the minor number.
:::

In Python, we will represent a version using a tuple of three integers.
For example, the version `3.9.5` will be represented by the triple `(3, 9, 5)`.

## Increasing Version

:::TASK
Write a function `increase_version(version, breaking_change, new_features)` takes takes

* `version`: a triple reprenting a version.
* `breaking_change`: a boolean indicating whether or not a breaking change is involved.
* `new_features`: a boolean indicating whether or not new features have been added.
:::

:::USAGE

```python
>>> increase_version((1, 2, 3), breaking_change=True, new_features=True)
(2, 0, 0)

>>> increase_version((1, 2, 3), breaking_change=False, new_features=True)
(1, 3, 3)

>>> increase_version((1, 2, 3), breaking_change=False, new_features=False)
(1, 2, 4)
```

:::

## Comparing Versions

We want to be able to compare semantic versions.
This works as you would expect.
Given two versions `v1 = a.b.c` and `v2 = x.y.z`:

* First compare the major numbers, `a` and `x`.
  If `a` is less than `x`, clearly `v1` is the older one.
  If `a` is greater than `x`, `v1` is the more recent one.
* If the major versions are equal, look at the minor versions `b` and `y`.
  If `b` is less than `y`, `v1` is older.
  If `b` is greater than `y`, `v1` is more recent.
* If the minor versions are also equal, we compare the patch numbers.
  The version with the highest patch number is the more recent.

:::TASK
Write a function `is_more_recent(v1, v2)` where `v1` and `v2` are both triples representing versions.
The function must return `True` if `v1` is more recent than `v2`, `False` otherwise.
:::

:::TASK
Write a function `is_older(v1, v2)` where `v1` and `v2` are both triples representing versions.
The function must return `True` if `v1` designates and older version than `v2`, `False` otherwise.

Solve this one using a single line of code.
:::

:::INFO
We have a confession to make: Python has this functionality built-in.

Whenever you compare tuples (e.g., `(2, 4) < (5, 1)`), it will perform the same operation as described above:
first checking the first elements, and if they are equal, moving on to the next, etc.
This is called [Lexicographic order](https://en.wikipedia.org/wiki/Lexicographic_order).

Thus, a valid solution for `is_more_recent(v1, v2)` would be

```python
def is_more_recent(v1, v2):
  return v1 > v2
```

:::
