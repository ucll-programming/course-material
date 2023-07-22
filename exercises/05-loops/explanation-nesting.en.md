# Nesting

It is possible to nest your conditionals and loops as deeply as you want:

:::code{caption="Python"}

```python
for y in range(height):
    for x in range(width):
        count = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if check(x + dx, y + dy):
                    count += 1
        register(x, y, count)
```

:::

Having the ability to do so does not necessarily mean it's a good idea:

* Nesting loops can lead to very inefficient code.
* If the nested looping is actually necessary, consider extracting part of the code into a separate function.

::::EXAMPLE

Below we rearranged the code so as to make it more manageable:

:::code{caption="Python"}

```python
for y in range(height):
    process_row(y)


def process_row(y):
    for x in range(width):
        process_square(x, y)


def process_square(x, y):
    count = 0
    for dy in range(-1, 2):
        count += process_neighbors(x, y + dy)
    register(x, y, count)


def process_neighbors(x, y):
    count = 0
    for dx in range(-1, 2):
        if check(x + dx, y):
            count += 1
    return count
```

:::
::::
