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

You're going to perform a search, i.e., going through a list of possible GCDs and returning the one that satisfies the necessary conditions.

* `gcd(x, y)` can never be greater than either `x` or `y`.
  This should tell you what a good starting point.
  Let's call this starting point `r`.
* What is the lowest possible value for `gcd(x, y)`?
* The highest and lowest possible values define a range in which you're certain to find `gcd(x, y)`.
* Since you want the *greatest* common divisor, it makes sense to start with the highest value of the range and work your way down.
:::
