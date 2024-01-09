# Constructor

The `__init__` method creates and initializes fields.
It is possible to pass it parameters so that you can choose what the field's values are set to.

:::code{caption="Python"}

```python
class Box:
    def __init__(self, initial_contents):
        self.contents = initial_contents
```

:::

Creating a `Box` object now requires a parameter:

:::code{caption="Python Shell"}

```python
>>> box = Box(5)
>>> box.contents
5
```

:::

::::INFO
It is often easier to have the parameter have the same name as the field:

:::code{caption="Python"}

```python
class Box:
    def __init__(self, contents):
        self.contents = contents
```

:::
::::
