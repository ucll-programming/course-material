# Total Cost

Your favorite webshop has the following rules:

* If your order costs less than &eur;100, you need to pay a delivery fee of &eur;10.
* If your order costs at least &eur;200, you get 5% discount.

:::TASK
Write a function `total_cost(amount)` that computes the total cost after taking into account the delivery fee and the discount.

Use two `if` statements:

* The first should deal with the delivery fee and increase `amount` if necessary.
* The second should deal with the discount and decrease `amount` if necessary.
:::

:::USAGE

```python
# Order costs less than 50, so add delivery fee
>>> total_cost(50)
60

# Order costs more than 50 but less than 200
# No delivery fee but no discount either
>>> total_cost(150)
150

# Order costs more than 200
# No delivery fee and discount
>>> total_cost(500)
475
```

:::
