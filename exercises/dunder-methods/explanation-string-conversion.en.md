# String Conversion

Every object has a type: it can be an integer, a boolean, a string, etc.
In certain situations, it can be useful to be able to convert from one type to another:

* We've already discussed how strings can be converted to integers (e.g., `int("42")`) or floating point numbers (e.g., `float("3.14")`).
* `if`s and `while`s convert their condition using `bool(condition)`.
* When using string interpolation, objects are converted to strings.

It is possible to define such conversions for objects of your own classes by defining the corresponding dunder method: `__int__` for converting the object to an integer, `__float__`, `__bool__`, and so on.
In this section, we'll only discuss conversions to string in more detail.

There are actually two ways to convert to string:

* `str(obj)` returns an informal, user-readable string.
* `repr(obj)` returns an unambiguous string representation of the object.
  Ideally, the string should be actual Python code that can be used to recreate the object.

To specify what `str` and `repr` should do when applied to objects of your own classes, you can define `__str__` and `__repr__`, respectively.

::::EXAMPLE

We define a class `Position` that represents an (x, y)-position in 2D:

:::code{caption="Python"}

```python
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({x}, {y})'

    def __repr__(self):
        return f'Position({x}, {y})'
```

:::

This produces the following results:

:::code{caption="Python Shell"}

```python
>>> position = Position(1, 2)
>>> str(position)
(1, 2)

>>> repr(position)
Position(1, 2)
```

:::

The `str` version returns a string as how humans would typically write down a position.
Note that it is actually ambiguous: from `"(1, 2)"` alone, you cannot infer the object's type.
It could be a tuple `(1, 2)`, a `Position(1, 2)`, or any other type that choses to format its objects this way.

`repr` returns a more detailed string: it mentions the actual type `Position`, so there's no confusing it with tuples.
The result `Position(1, 2)` is actually also valid Python code.

Ideally, `repr(obj)` answers the question "How can I construct the object `object`?", but keep in mind that it's not necessarily possible.
::::
