# GCD

The greatest common divisor of two integers `x` and `y` is the greatest integer that divides both `x` and `y`.
The signs of `x` and `y` do not matter: `gcd(x, y) == gcd(-x, y) == gcd(x, -y) == gcd(-x, -y)`.

:::TASK
Write a function `gcd(x, y)` that computes the greatest common divisor of the given integers `x` and `y`.

* Take into account the possibility that `x` and `y` can be negative.
* Some tests test for the efficiency of your algorithm.
  No smart math tricks will be necessary to make it run within the time limits.
:::

:::USAGE

```python
>>> gcd(5, 7)
1

>>> gcd(15, 10)
5

>>> gcd(10, -15)
5
```

:::

:::HINT

* Start with some "high" value `r`.
  See if it divides both `x` and `y`.
  If it does, it is the greatest common divisor, provided you started with a high enough `r`.
  If it does not, decrement `r` by one and try again.
  Ultimately, you're bound to find a value for `r` that divides both `x` and `y`.
* `gcd(x, y)` can never be greater than either `x` or `y`.
  This should tell you what a good starting value for `r` would be.

:::
