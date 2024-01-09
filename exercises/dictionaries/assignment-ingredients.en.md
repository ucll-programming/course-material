# Ingredients

These were the ingredients for the chocolate cake in table form.

::::div{.formatted-table}
:::center
| Ingredient | Quantity |
| ---------- | -------- |
| chocolate | 250g |
| eggs | 5 |
| sugar | 125g |
| flour | 75g |
| butter | 175g |
:::
::::

:::TASK
Write a function `ingredients()` that returns a `dict` containing the information above.

All keys and values should be strings.
In other words, represent the 5 in the eggs rows with `"5"`.
:::

::::HINT
The function will have the form

:::code{caption="Python"}

```python
def ingredients():
    return {
        key1: value1,
        key2: value2,
        ...
    }
```

:::

where `key1`, `key2`, &hellip; are the ingredient names and `value1`, `value2`, &hellip; the corresponding quantities.

::::
