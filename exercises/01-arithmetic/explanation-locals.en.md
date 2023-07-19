# Local Variables

Consider the following code:

:::code{caption="Python"}

```python
def some_calculation(a, b, c):
    return min((-b-(b**2 - 4 * a * c)**0.5)/(2*a), (-b+(b**2 - 4 * a * c)**0.5)/(2*a))
```

:::

Such a monolithic mathematical expression is quite intimidating and hard to read.
We can improve the readability by storing intermediate results in *local variables* as follows:

:::code{caption="Python"}

```python
def some_calculation(a, b, c):
    d = b**2 - 4 * a * c
    sqrt_d = d ** 0.5
    x1 = (-b-sqrt_d)/(2*a)
    x2 = (-b+sqrt_d)/(2*a)
    return min(x1, x2)
```

:::

Here, `d`, `sqrt_d`, `x1` and `x2` are local variables.
They're called local because they only exist within the bounds of the function.
No one outside the function can access them.
The same holds true for parameters: these are also only accessibly from within the function.

The region of code in which some variable `x` is visible is called the *scope* of `x`.
Python is *function scoped*: functions form the boundaries of the scope of variables.

## Example

:::code{caption="Python"}

```python
def foo(a):
    b = 5
    return bar()


def bar():
    return a * b
```

:::

In the code above, we have a function `foo`.
It takes a parameter `a` and introduces a local variable `b`.
It also calls `bar`, which returns the product of `a` and `b`.
However, this code is invalid: `a` and `b` are variables that are only visible from within `foo`.

If you wish `bar` to have access to `a`'s and `b`'s value, you have to pass them as parameters:

:::code{caption="Python"}

```python
def foo(a):
    b = 5
    return bar(a, b)


def bar(a, b):
    return a * b
```

:::
