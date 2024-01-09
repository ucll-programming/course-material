# Colors

In this exercise, we'll create a new `Color` type and define a few operations on them.

## Color Type

::::TASK
Create a named tuple `Color` and fields `r`, `g` and `b`.
::::

::::USAGE

```python
>>> color = Color(50, 90, 150)
>>> color.r
50

>>> color.g
90

>>> color.b
150
```

::::

## Valid Colors

A `Color` object is valid if each component has a value between `0` and `255` (inclusive).

::::TASK
Create a function `valid_color(color)` that returns `True` if the color is valid, `False` otherwise.
::::

::::USAGE

```python
>>> valid_color(Color(0, 0, 0))
True

>>> valid_color(Color(100, 300, 200))
False
```

::::

## Clamp Colors

Clamping a color means bringing each of the components back into a valid range.
All components lower than `0` become `0` and all components higher than `255` become `255`.

::::TASK
Write a function `clamp_color(color)` that returns a clamped copy of `color`.
::::

::::USAGE

```python
>>> clamp_color(Color(50, -50, 300))
Color(r=50, g=0, b=255)
```

::::
