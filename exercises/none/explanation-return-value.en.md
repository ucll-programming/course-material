# Return Value

Consider the following function:

:::code{caption="Python"}

```python
def say_hello():
    print("Hello")
```

:::

There is no `return` statement, which is perfectly valid.
However, functions *always* return a value in Python.
In this case, because no return value was specified in the code, the function simply returns `None`.
In other words, the code above is equivalent to

:::code{caption="Python"}

```python
def say_hello():
    print("Hello")
    return None
```

:::
