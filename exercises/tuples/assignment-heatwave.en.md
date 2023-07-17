# Heatwaves

A [heatwave](https://en.wikipedia.org/wiki/Heat_wave) is a period of abnormally hot weather.
What constitutes "abnormally hot" depends on the region.
In Belgium, a heatwave is defined as follows:

* The heatwave period must be at least five consecutive days long.
* During these days, the temperature must be at least 25&deg;C.
* During at least three days the temperature must reach 30&deg;C or more.

:::TASK
Write a function `heat_wave(temperatures)` that checks whether a heatwave occurred and returns `True` if that's the case, `False` if not.

* `temperatures` is a tuple containing daily temperature measurements.
* Note that a heatwave does not need to encompass the entire period represented by `temperatures`.
  Finding a subsequence that satisfies the heatwave conditions is sufficient.
:::

:::USAGE

```python
>>> heatwave([25, 30, 31, 30, 28])
True

# Heatwave starting on second day
>>> heatwave([24, 28, 31, 35, 36, 32, 20])
True

>>> heatwave([24, 26, 28, 31, 29, 27, 32, 25, 27, 26, 30, 23])
True

# Not long enough for a heatwave
>>> heatwave([40, 40, 40, 40])
False

# Hot period is not contiguous
>>> heatwave([40, 20, 40, 40, 40, 40])
False
```

:::

:::HINT

* Process the `temperatures` from left to right.
* Introduce two local variables.
  * One keeps the count of temperatures greater than 25.
  * The other keeps the count of temperatures greater than 30.
* Increment these variables as you go through the list.
* When you encounter a temperature lower than 25, reset both variables to 0.
* If at one point, the 25-count is greater than 5 and the 30-count is greater than 30, you've got a heatwave.

:::
