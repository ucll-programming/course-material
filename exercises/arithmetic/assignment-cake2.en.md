# Cake 2

It turns out we need more than eggs to bake cake.
Each cake requires 5 eggs, but also 250g of flour.
We need to update our tool to take into account this second ingredient.

:::TASK
Write a function `cake2(eggs, flour)` that returns the amount of cakes one can make given `eggs` number of eggs and `flour` grams of flour.
:::

:::USAGE

```python
# Enough eggs, but not enough flour
>>> cake2(5, 0)
0

# Exactly enough for one cake
>>> cake2(5, 250)
1

# Enough eggs for 5 cakes, but only enough flour for 4
>>> cake(25, 1000)
4
```

:::
