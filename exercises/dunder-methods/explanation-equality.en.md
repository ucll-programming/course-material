# Equality

In a previous chapter, we explained the difference between equal objects and same objects.
A quick reminder:

* `x is y` answers the question "is `x` the same object as `y`?".
  The answer is `True` if there is actually just one object in memory and both `x` and `y` refer to this object.
* `x == y` answers "is `x` equal to `y`?" which is `True` when the objects have the same contents.

For example, two lists `[1, 2, 3]` and `[1, 2, 3]` are equal (because they have the same items) but not necessarily the same (because the list could appear twice in memory).

## Operations Relying on Equality

When we check for list membership, e.g., `x in [1, 2, 3]`, what are we actually asking?
Are we asking if the list contains an object that is the *same* as `x`, or one that is *equal* to `x`?
In other words, which of the two implementations below returns the same result as `x in lst`?

:::code{caption="Python"}

```python
def membership_same(x, lst):
    for item in lst:
        if x is item:
            return True
    return False


def membership_equal(x, lst):
    for item in lst:
        if x == item:
            return True
    return False
```

:::

Both implementations have their merit, but which one does `in` use?
The answer: `membership_equal`.

The same is true for all other operations that require some form of equality:

* `lst.remove(x)` removes the first element *equal* (`==`) to `x`.
* `lst.index(x)` returns the index of the first element *equal* (`==`) to `x`.
* Set operations all rely on `==`.
  For example, `{x, y}` becomes `{x}` when `x == y`.

## Defining Equality

Sameness works exactly the same for all objects of all types.
Equality, however, is trickier: when you define your own class, Python cannot guess how equality has to be determined.
Take, for example, a class representing fractions:

:::code{caption="Python"}

```python
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
```

:::

We know that $\frac{1}{2}$ and $\frac{2}{4}$ are equal, but Python cannot know that.
You have to specify what rules to follow by defining an `__eq__` method:

:::code{caption="Python"}

```python
import math


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other):
        # a / b == c / d    if    a * d == b * c
        return self.numerator * other.denominator == self.denominator * other.numerator
```

:::

## `isinstance`

This `__eq__` implementation has a flaw: it assumes that `other` is a `Fraction`.
`__eq__` is expected to be able to deal (i.e., not crash) with any combination of object types.
We need to add code that first checks if `other` is a `Fraction`, and only if that's the case, perform the math.
If `other` does not have the right type, `__eq__` should return the predefined object `NotImplemented`.

:::code{caption="Python"}

```python
import math


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator == self.denominator * other.numerator
        else:
            return NotImplemented
```

:::

::::IMPORTANT
If you do not define an `__eq__` method, Python will define it for you and implement it using `is`.

Technically speaking, this default implementation is actually *inherited* from `object`.
This will make more sense to you after you've learned about inheritance.
::::

::::INFO
For the sake of completeness: `x == y` actually performs the steps shown below.

:::code{caption="Python"}

```python
if (result := x.__eq__(y)) is not NotImplemented:
    return result
elif (result := y.__eq__(x)) is not NotImplemented:
    return result
else:
    return False
```

:::
::::

## Inequality

We now know what `==` does, but what about `!=`?

Simple: you can define a method `__ne__` that teaches Python when your objects are _not_ equal.
Fortunately, you do not need to define this method manually, as every class comes with an excellent default implementation:

:::code{caption="Python"}

```python
def __neq__(self, other):
    return not self == other
```

:::
