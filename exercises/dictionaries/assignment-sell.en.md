# Selling Shoes

We own a sneaker store and keep track of our stock using a `dict`:

:::code{caption="Python"}

```python
stock = {
    'New Balance 530': 5,
    'Converse Chuck Taylor All Star 70 Hi': 2,
    'Air Jordan 1 Retro': 8,
    'Nike Air Max Tuned 1': 1,
    'Adidas Superstar': 4,
    'Vans Classic Slip-on Checkered': 15
}
```

:::

Whenever we sell a pair, we wish to decrease the number of pairs left by one.
For example,

:::code{caption="Python Shell"}

```python
>>> remove_from_stock(stock, 'New Balance 530')
>>> stock
{
    'New Balance 530': 4,
    'Converse Chuck Taylor All Star 70 Hi': 2,
    'Air Jordan 1 Retro': 8,
    'Nike Air Max Tuned 1': 1,
    'Adidas Superstar': 4,
    'Vans Classic Slip-on Checkered': 15
}
```

:::

However, when none are left in stock, you should remove it from `stock`:

:::code{caption="Python Shell"}

```python
>>> remove_from_stock(stock, 'Nike Air Max Tuned 1')
>>> stock
{
    'New Balance 530': 4,
    'Converse Chuck Taylor All Star 70 Hi': 2,
    'Air Jordan 1 Retro': 8,
    'Adidas Superstar': 4,
    'Vans Classic Slip-on Checkered': 15
}
```

:::

:::TASK
Write a function `sell(stock, model)` that implements the logic described above.

You can assume that `stock` always contains at least one of `model`.
:::
