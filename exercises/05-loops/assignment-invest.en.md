# Investment

You have invested a certain amount `amount`.
This amount grows at a steady rate of `rate` percent each year.
You wish to know how many years you should wait until your investment reaches a certain goal `goal`.

:::TASK
Write a function `invest(amount, rate, goal)` that returns how long you need to wait for your investment to grow to at least `goal`.
The result should be an integer.

This exercise is not about finding a mathematical formula.
Simply simulate the passage of time using a loop.
:::

:::USAGE

```python
# Investment doubles every year
# 100 -> 200 -> 400
>>> invest(amount=100, rate=100, goal=400)
2

# 100 -> 200 -> 400 -> 800 -> 1600
>>> invest(amount=100, rate=100, goal=1000)
4
```

:::

:::HINT
You can use the following formula to calculate how much your investment grows in a year:

$$
\textrm{amount} * \frac{rate}{100}
$$
:::
