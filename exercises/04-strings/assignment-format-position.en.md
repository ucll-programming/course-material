# Formatting Positions

You're programming an RTS game and are working on the save feature.
Each unit has a position (x, y) on the map and you wish to store this in a file as strings.
Note that the coordinates are floating point numbers.

:::TASK
Write a function `format_position(x, y)` that takes two `float`s `x` and `y` and returns a string `"(x, y)"` where `x` and `y` are displayed with 3 decimals.
:::

:::USAGE

```python
>>> format_position(3.21, 5.7852)
"(3.210, 5.785)"
```

:::
