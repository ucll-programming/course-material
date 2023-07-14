# Selling Shoes +

Our little sneaker store isn't doing too well.
It turns out we forgot to take into account shoe sizes.
We need to update the way we represent our stock.
Per model, we need to keep track of how many pairs are available *in each size*.
For this, we need *nested dictionaries*, i.e., dictionaries in dictionaries.

:::code{caption="Python"}

```python
stock = {
    'New Balance 530': {44: 2, 45: 3, 47: 1},
    'Converse Chuck Taylor All Star 70 Hi': {39: 2, 40: 1, 43: 4, 44: 2},
    'Air Jordan 1 Retro': {46: 1},
    'Nike Air Max Tuned 1': {44: 2, 45: 1},
    'Adidas Superstar': {41: 2, 43: 2, 45: 1, 47: 3},
    'Vans Classic Slip-on Checkered': {43: 1}
}
```

:::

:::TASK
Write a function `sell2(stock, model, size)` that works as follows:

* If the shoe is not available in the right size, the function must return `False` and leave `stock` untouched.
* If the shoe is available in the requested size:
  * The function must return `True`.
  * The stock number must be decremented by one.
  * If no more shoes of a particular size are available, that key/value pair must be removed.
    In other words, `{42: 1, 43: 0}` must be simplified to `{42: 1}`.
  * If a shoe is not available in any size, it must be removed from `stock`.
    In other words, `{'Reebok Fury Pump': {}}` must be simplified to `{}`.
:::
