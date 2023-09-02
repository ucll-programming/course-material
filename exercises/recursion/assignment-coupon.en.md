# Coupon

You have a &euro;100 coupon for your favorite restaurant!
There's one catch: when you order, you have to spend *exactly* that amount.

::::TASK
Write a function `coupon(menu, value)`:

* `menu` is a list of prices.
* `value` contains how much the coupon is worth.

`coupon(menu, value)` must returns a list of prices that sum up to `value`.
Each of these prices must be listed in the menu.
The same price can be reused multiple times.

If there are multiple solutions, any solution will do.
The order in which you return the prices does not matter.

If no solutions can be found, return `None`.
::::

::::USAGE

```python
# It's easy if there's an item with price 1
>>> coupon([1], 3)
[1, 1, 1]

# Impossible to make 3.
>>> coupon([2], 3)
None

# 5 + 12 + 12 == 29
>>> coupon([5, 31, 12], 29)
[5, 12, 12]
```

::::
