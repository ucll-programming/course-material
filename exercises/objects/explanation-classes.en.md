# Classes

::::IMPORTANT
We gave you a long explanation about the virtues of abstraction.
However, just telling you straight away how to achieve it will probably leave you utterly confused, as there are multiple concepts involved.

Instead, we will explain the new concepts one by one.
So, if at first it is not clear to you how these concepts aid in achieving abstraction, no need to worry, we'll get there eventually.
::::

## `Box`

Let's start very simple, with a rather silly example.

:::code{caption="Python"}

```python
class Box:
    def __init__(self):
        self.contents = 0
```

:::

Here, we defined a *class* named `Box`.
Note that the class itself is not an box, it merely *describes* what boxes look like.
Let's create a box:

:::code{caption="Python"}

```python
box = Box()
```

:::

As you can see, `Box` is callable as if it were a function.
`Box()` creates and returns an actual `Box` object.

A class contains functions, but because they're inside a class, they are called *methods* instead.
`Box` defines just one ~function~ method, namely `__init__`.
The name has a special meaning: it tells Python it is the *constructor*.
A constructor's responsibility is to initialize newly made `Box` objects.
When you create a new `Box`, Python creates an empty object in memory and passes it to `__init__`, i.e., the `self` parameters refers to the fresh object.
`__init__` then performs `self.content = 0` which means "let this new object have a field named `content` and set it to `0`".

After execution `box = Box()`, the variable `box` references this initialized object.
We can use our new `Box` as follows:

:::code{caption="Python"}

```python
print(box.contents)
```

:::

`box.contents` asks the `box` for the value of its `contents` field.
This field has been set to `0` by the constructor, so `box.contents` will evaluate to `0`.

You can update this field as you see fit:

:::code{caption="Python"}

```python
box.contents = "Hello"
```

:::

::::IMPORTANT
A class is merely a description of what objects will look like.
Once you have defined a class, you can *instantiate* it, i.e., creating objects that conform to what the class describes.

In the example above, the `Box` class states that all `Box` objects shall have a `contents` field that's initially set to `0`.
You can then proceed to make as many `Box` objects as you wish:

:::code{caption="Python"}

```python
box1 = Box()
box2 = Box()
box3 = Box()
```

:::
Each of these boxes will have their own `contents`.

:::code{caption="Python"}

```python
box1.contents = 1
box2.contents = "Hello"
box3.contents = True
```

:::

::::
