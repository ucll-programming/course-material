# Parsing Positions

We revisit our RTS game.
In a previous exercise, you implemented a function that turned an (x, y) position in a string.
Now it's time to implement the inverse operation: given a string, extract the values for x and y from it.

This is slightly more complicated to implement than `parse_date`, as these strings have a less rigid structure.

:::TASK
Write two functions `parse_position_x(string)` and `parse_position_y(string)` that take a string and return the x-coordinate and y-coordinate, respectively.
Examples are shown below.
:::

:::USAGE

```python
>>> string = "(12.453, 9.120)"
>>> parse_position_x(string)
12.453

>>> parse_position_y(string)
9.12
```

:::

:::HINT{caption="Hint 1"}
Many algorithms consists of multiple steps.
Don't try to find a final solution in one go.
Find little steps that allow you to chip away the complexity in tiny bits.
:::

:::HINT{caption="Hint 2"}
A possible first step would be to get rid of the enclosing parentheses.
These are always at fixed positions, so this should be easy.
This way, you have reduced the problem from parsing `(x, y)` to parsing `x, y`.
:::

:::HINT{caption="Hint 3"}
You need to know where both `x` and `y` start and end.
There's a special character separating the two.
Find its position in the string.
:::

:::HINT{caption="Hint 4"}
Once you have the index of the separator, you can partition the string in a left part (where `x` is stored) and a right part (where `y` is stored).
:::
