# String Iteration

In our previous explanation, we claimed the `for` loop took the form

:::code{caption="Python"}

```python
for variable in range(start, stop):
    # body
```

:::

In reality, the `for` loop is a bit more flexible than this: `range` is just a specific case.
The actual general shape is

:::code{caption="Python"}

```python
for variable in iterable_object:
    # body
```

:::

`range` is just one function that returns an iterable object.
There are many iterable objects, strings being one of them:

:::code{caption="Python Shell"}

```python
>>> for char in "abcd":
...    print(char)
"a"
"b"
"c"
"d"
```

:::

::::INFO
Later you will see lists, tuples and dictionaries, all of which are also iterable.
::::
