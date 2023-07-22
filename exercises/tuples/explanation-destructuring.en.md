# Destructuring

When using tuples to represent coordinates, colors, etc. you know exactly how many items a tuple will have.
Often you will need to get access to each item of the tuple:

:::code{caption="Python"}

```python
def process(color):
    r = color[0]
    g = color[1]
    b = color[2]
    # ...
```

:::

Such code can be simplified using destructuring:

:::code{caption="Python"}

```python
def process(color):
    r, g, b = color
    # ...
```

:::

Destructuring is also possible in `for` loops:

:::code{caption="Python"}

```python
colors = (
    (50, 128, 240),
    (0, 0, 0),
    (255, 200, 140),
    (142, 20, 185)
)

for r, g, b in colors:
    # ...
```

:::
