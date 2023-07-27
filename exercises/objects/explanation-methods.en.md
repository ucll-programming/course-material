# Methods

## `is_empty`

Let's add a method to our `Box` class.

:::code{caption="Python"}

```python
class Box:
    def __init__(self, contents):
        self.contents = contents

    def is_empty(self):
        return self.contents is None
```

:::

`box.is_empty()` can now be used to check if our box is empty, i.e., contains `None`.

:::code{caption="Python Shell"}

```python
>>> box = Box(5)
>>> box.is_empty()
False

>>> box.contents = None
>>> box.is_empty()
True
```

:::

Notice that although `is_empty` has a parameter `self`, the call to `is_empty` does not provide an argument.
This is a peculiarity of object-oriented syntax: the `self` parameter is actually set to the `Box` object that receives the method call.
In a way, you can think of `box.is_empty()` being the same as `is_empty(box)`.

::::IMPORTANT
The `self` parameter must appear as the first parameter of *all* methods of *all* classes.

Due to this ubiquity, many other programming languages made the `self` parameter (or its equivalent) implicit, i.e., you don't need to mention it every time because it is added automatically for you behind the scenes.
::::


## `put`

We add another methods to `Box`.

:::code{caption="Python"}

```python
class Box:
    def __init__(self, contents):
        self.contents = contents

    def is_empty(self):
        return self.contents is None

    def put(self, contents):
        self.contents = contents
```

:::

We can use these methods as follows:

:::code{caption="Python Shell"}

```python
>>> box = Box(5)
>>> box.put("Gwyneth")
>>> box.contents
"Gwyneth"
```

:::

Make sure to notice the call to `put`: the method expects two parameters, but the call only mentions one argument.
As explained before, the first parameter is the `Box` object on which the method is called, so you can see `box.put("data")` is actually being `put(box, "data")`, which fits better with the definition.

::::INFO
At this point, the methods we defined offer absolutely no added value: they don't contain any nontrivial logic and don't do anything that we couldn't do ourselves.
This is due to the fact that `contents` is publicly available: the methods are nothing more than useless middle men.

However, things are about to change.
::::
