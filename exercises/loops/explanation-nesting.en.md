# Nesting

It is possible to nest your conditionals and loops as deeply as you want:

:::code{caption="Python"}

```python
# Very complex code (understanding it is not necessary)
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
* As you may have experienced yourself, lots of nesting makes the code makes the code very difficult to understand.

Sometimes, performing such complex logic is unavoidable.
It is strongly recommended to split the code into separate functions with descriptive names which then serve as guide in understanding what is actually going on.

::::EXAMPLE

Below we rearranged the code so as to make it more manageable:

:::code{caption="Python"}

```python
# Outer loop
for y in range(height):
    process_row(y)


def process_row(y):
    for x in range(width):
        process_square_neighborhood(x, y)


def process_square_neighborhood(x, y):
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            count += process_single_square(x + dx, y + dy)
    register(x, y, count)


def process_single_square(x, y):
    if check(x, y):
        return 1
    else:
        return 0
```

:::

Take your time to find how this code is related to the deeply nested original version.
It is important that you understand how that parameters and return values are used to split up a monolithic code block.
On exams, many students write code that looks like the original version, and unfortunately for them, it typically contains hard to find bugs.
Making it a habit to spread code over multiple functions makes a big difference: a good coding discipline has literally helped certain students go from 0 to 20.
::::
