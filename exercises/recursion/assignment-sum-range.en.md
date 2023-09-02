# Sum of Range

::::TASK
Write a *recursive* function `sum_range(a, b)` that computes the sum of all numbers between `a` and `b`, including `a` and `b` themselves.

Do not rely on the built-in function `sum`, but rely on recursion.
::::

::::USAGE

```python
# 2 + 3 + 4
>>> sum_range(2, 4)
9

# 1 + 2 + 3 + 4 + 5
>>> sum(5, 1)
15
```

::::

::::HINT{caption="Recursion Hint 1"}
`sum_range(a, b)` has to compute the sum of all numbers in the range `a` to `b`.
In order to find a recursive implementation, you need to find a way to shrink this range.
::::

::::HINT{caption="Recursion Hint 2"}
A sum from `a` to `b` can be shrunk in multiple ways:

* From the left side: `sum_range(a, b) == a + sumrange(a + 1, b)`.
* From the right side: `sum_range(a, b) == sum_range(a, b - 1) + b`.
::::

::::HINT{caption="Base Case Hint"}
The range over which to take the sum shrinks with every recursive call.
Ultimately, you'll end up having to deal with the sum for the range `a` to `a`.
Intercept this case (`a == b`) and return the answer directly.
::::

::::HINT{caption="Hint: Dealing with a > b"}
The possibility that `a > b` makes it a bit harder.
However, it actually is very to get rid of: add a test that checks if `a > b`, and if so, add a recursive call `sum_range(b, a)`:

:::code{caption="Python"}

```python
def sum_range(a, b):
    if a > b:
        return sum_range(b, a)
    else:
        # ...
```

:::
::::
