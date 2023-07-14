# Desktop

Say we have a computer component catalog, which is a `dict` associating item names with item prices:

:::code{caption="Python"}

```python
catalog = {
    'Intel Core i7 13700K': 439,
    'Intel Core i5 13600K': 331,
    'Gigabyte Z790 AORUS ELITE AX': 261,
    'MSI MAG Z790 TOMAHAWK WIFI': 279,
    'Corsair DDR5 Vengeance 2x16GB 5600': 95,
    'Corsair DDR5 Vengeance 2x32GB 5600': 165,
    'MSI GeForce RTX 4070 VENTUS 3X 12G OC GPU': 659,
    'Gigabyte GeForce RTX 4090 GAMING OC 24G GPU': 1849,
    ...
}
```

:::

Given a list of components of a desktop PC, we wish to know the total cost of this PC.

:::TASK
Write a function `desktop(catalog, components)` that looks up the price of each component and returns the total.
:::

:::USAGE

```python
>>> desktop(catalog, ['Intel Core i7 13700K', 'Gigabyte Z790 AORUS ELITE AX'])
700   # == 439 + 261
```

:::
