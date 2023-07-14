# Cake

Remember the cake exercises?
Well, they're back!
But now we can make them so much better.

We have a stock of ingredients, represented as a `dict`.
We also have a recipe that requires specific amounts of specific ingredients.

:::code{caption="Python"}

```python
stock = {
    "sugar": 1500,
    "eggs": 20,
    "flour": 2000,
    "butter": 1000,
    "chocolate": 2500,
    "salt": 250
}

cake_ingredients = {
    "butter": 250,
    "eggs": 4,
    "flour": 250,
    "sugar": 250
}
```

:::

We now want to determine how many cakes we can bake with the stock we have.
To determine this, we need to look at every ingredient in turn:

* We need 250g butter per cake and we have 1000g available, which allows us to make 4 cakes.
* We need 4 eggs per cake and have 20, so we can make 5 cakes.
* We have enough flour for 8 cakes.
* We have enough sugar for 6 cakes.

The butter is the most limiting ingredient: in the end, we can only make 4 cakes.

:::TASK
Write a function `cake(stock, recipe_ingredients)` that returns how many cake you can bake, where a single cake requires `recipe_ingredients`.

Note that it is possible that the stock does not contain all necessary ingredients.
:::
