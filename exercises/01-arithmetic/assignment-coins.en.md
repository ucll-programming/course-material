# Coins

We have three types of coins at our disposition with denominations [&euro;5](https://www.coin-database.com/series/germany-5-euro-coins.html), &euro;2 and &euro;1.
We want to know how many coins we minimally need to form a certain goal amount.

:::TASK
Write a function `coins(amount)` that returns the minimal amount of coins necessary to make `amount`.

* Start with determining how many 5-coins fit in `amount`.
* Subtract the total value made by the 5-coins from `amount`.
* Determine how many 2-coins fit in `amount`.
* Subtract the value made by the 2-coins from `amount`.
* What remains in `amount` is equal to the number of 1-coins.
* Add all the coin counts together and return this sum.
:::

:::USAGE

```python
# To make 5 euros, we only need one coin
>>> coins(5)
1

# To make 6 euros, we need at least 2 coins (5 + 1).
>>> coins(6)
2

# To make 9 euros, we need at least 3 coins (5 + 2 + 2).
>>> coins(9)
3
```

:::
