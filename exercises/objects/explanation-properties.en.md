# Properties

Say you have the following class:

:::code{caption="Python"}

```python
class Box:
    def __init__(self, contents):
        self.contents = contents
```

:::

As you can see, the `contents` field is public.
Say you rely on this `Box` class all over your code base, so that it is riddled with stuff like

:::code{caption="Python"}

```python
print(box.contents)
box.contents = "800"
box.contents *= 2
```

:::

Now it turns out that you need to make `contents` a bit more intelligent, like maybe you need all changes to the contents to be logged somewhere.
In order to accomplish this, you need to upgrade `contents` from dumb data to smart code:

:::code{caption="Python"}

```python
class Box:
    def __init__(self, contents):
        self.put(contents)

    def put(self, contents):
        log_change()
        self.__contents = contents

    def contents(self):
        return self.__contents
```

:::

However, this change makes it necessary to update all other code that relies on `Box`:

:::code{caption="Python"}

```python
print(box.contents())
box.contents.put("800")
box.contents.put(box.contents() * 2)
```

:::

This is a *serious* problem: a small change in one class ripples throughout the entire code base.
One of the highest priorities in software engineering is that changes can remain localized, i.e., that one component can be modified locally without it having any impact on other components.

One could claim we could have avoided this problem by showing some foresight: we should've known better than to directly expose `contents` and go straight for the method-approach, even though at the time we didn't need to.
This is a dangerous mentality, however: one could easily foresee all kinds of potential changes and start designing their classes to try to take into account all possible future needs.
This inevitably leeds to an overengineered mess.

Luckily, Python provides solutions that allow you to start with a [simple solution first](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it) and, if need be, gracefully improve it without needing to break other code.
Python's properties is one such solution.
Here's what a `Box` relying on properties would look like:

:::code{caption="Python"}

```python
class Box:
    def __init__(self, contents):
        self.contents = contents

    # This is the getter
    @property
    def contents(self):
        return self.__contents

    # This is the setter
    @contents.setter
    def contents(self, value):
        log_change()
        self.__contents = value
```

:::

And this is how you would use it:

:::code{caption="Python Shell"}

```python
>>> box = Box(5)
>>> print(box.contents)
>>> box.contents *= 2
```

:::

As you can see from the usage, interacting with a property has the [exact same syntax](https://en.wikipedia.org/wiki/Uniform_access_principle) as interacting with a field.
This aspect is very important: it means that you can upgrade a field to a property without the outside world noticing.

`box.contents` causes the *getter* to be called.
In other words, you can define yourself what actually happens when the property is read.

Writing to `box.contents`, e.g., `box.contents = 10`, will call the *setter*.
Similarly, you can fully customize what happens when writing to a property: you can perform validation, logging, notify others of the change, etc.

Defining a setter is optional: if you leave it out, the property will be considered readonly, i.e., attempts to write to it will result in an error.

::::IMPORTANT
A property only consists a getter and optional setter.
In general, you'll still need a separate (private) field to actually have some memory to store the value in.
::::

::::EXAMPLE
:::code{caption="Python"}

Using `print`s, we can demonstrate when the getter and setter are being called.

```python
class Box:
    def __init__(self, contents):
        self.contents = contents

    # This is the getter
    @property
    def contents(self):
        print('Reading')
        return self.__contents

    # This is the setter
    @contents.setter
    def contents(self, value):
        print('Writing')
        self.__contents = value
```

:::

:::code{caption="Python Shell"}

```python
>>> box = Box(5)
Writing      # Because constructor sets property

>>> box.contents
Reading      # Because property's getter was called
5            # Property returned 5

>>> box.contents = 10
Writing      # Because property's setter was called

>>> box.contents *= 2
Reading      # Because the property's value needs to be read first
Writing      # Writing the property's value after it has been doubled
```

:::

::::
