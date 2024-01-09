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

::::HINT{caption="Hint 1"}
While there are [special math tricks](https://en.wikipedia.org/wiki/Euclidean_algorithm) to quickly find the gcd, we can also do it in a less sophisticated way.

You know that `gcd(a, b)` must divide both `a` and `b`.
Perform a search until you find a number that satisfies that constraint.
::::

::::HINT{caption="Hint 2"}
There's a range in which `gcd(a, b)` must lie.

* What's the lowest value `gcd(a, b)` can take?
  Is there a low number that is guaranteed to always divide both `a` and `b`?
* What's the highest value `gcd(a, b)` can be?
  Can it be higher than `a`?
  Can it be higher than `b`?
::::

::::HINT{caption="Hint 3"}
`gcd(a, b)` must evaluate to the *greatest* common divisor.
If you know that `min <= gcd(a, b) <= max`, in which order should you look for a common divisor?

* Should you start from the lowest possible value and work your way up, or
* Should you start from the highest possible value and work your way down?
::::
