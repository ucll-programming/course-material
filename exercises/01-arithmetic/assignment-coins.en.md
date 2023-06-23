# Coins

We have three types of coins at our disposition with denominations [€5](https://www.coin-database.com/series/germany-5-euro-coins.html), €2 and €1.
We want to know how many coins we minimally need to form a certain goal amount.

:::TASK
Write a function `coins(amount)` that returns the minimal amount of coins necessary to make `amount`.
:::

:::USAGE

```python
# To make €5, we only need one coin
>>> coins(5)
1

# To make €6, we need at least 2 coins (€5 + €1).
>>> coins(6)
2

# To make €9, we need at least 3 coins (5€ + 2€ + 2€).
>>> coins(9)
3
```

:::
