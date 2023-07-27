# Benefits of Hiding Data

We repeat the code of the `Box` class for your benefit:

:::code{caption="Python"}

```python
class Box:
    def __init__(self, contents):
        self.__contents = contents

    def is_empty(self):
        return self.__contents is None

    def put(self, contents):
        self.__contents = contents

    def contents():
        return self.__contents
```

:::

We made the field (= data) private and replaced it with public methods (= code).
The idea of replacement of data by code is fundamental in the world of software engineering: it shows up time and again if you pay attention to it.
But why is this such a powerful concept?

Data is *dumb*.
If `contents` were simply a public field, anyone can do whatever they want with it: anyone can read it or overwrite it with arbitrary values.
Code, however, is smart: it allows you to specify any behavior you want.

Say for example you want to restrict what kind of values are allowed in the box, e.g., only numbers.
The only way to update the `Box`'s contents is through `put`.
If we add a check there, we can control what goes in the box:

:::code{caption="Python"}

```python
class Box:
    def __init__(self, contents):
        self.__contents = contents

    def is_empty(self):
        return self.__contents is None

    def put(self, contents):
        # Checks whether parameter is an integer
        if isinstance(contents, int):
            self.__contents = contents
        else:
            raise ValueError()

    def contents():
        return self.__contents
```

:::

A bit of explanation is in order:

* `isinstance(value, type)` checks whether `value` has type `type`.
  Examples of types are `int`, `str`, `bool`, `list`, `tuple`, `dict`, any class name, ...
* `raise ValueError()` raises an *exception*.
  We'll discuss these in another chapter.
  Suffice it to say, raising an exception is a way for a function or method to say "I refuse to do this".

:::code{caption="Python Shell"}

```python
>>> box = Box(5)
>>> box.put("invalid value")
ValueError

>>> box.contents()
5
```

:::

## Loophole

There is still a loophole though: the constructor does not check its parameter.
Let's fix this:

:::code{caption="Python"}

```python
class Box:
    def __init__(self, contents):
        if isinstance(contents, int):
            self.__contents = contents
        else:
            raise ValueError()

    def is_empty(self):
        return self.__contents is None

    def put(self, contents):
        if isinstance(contents, int):
            self.__contents = contents
        else:
            raise ValueError()

    def contents():
        return self.__contents
```

:::

## Getting Rid of Redundancy

The same checking code is repeated twice, which is generally a bad idea.
We rewrite our code a bit:

:::code{caption="Python"}

```python
class Box:
    def __init__(self, contents):
        self.put(contents)

    def is_empty(self):
        return self.__contents is None

    def put(self, contents):
        if isinstance(contents, int):
            self.__contents = contents
        else:
            raise ValueError()

    def contents():
        return self.__contents
```

:::

As you can see, the constructor simply delegates to `put`.
Remark that fields can be created by any method, not just the constructor.

## Finishing Touches

We can improve on `Box` a little bit more:

:::code{caption="Python"}

```python
class Box:
    def __init__(self, contents):
        self.put(contents)

    def is_empty(self):
        return self.__contents is None

    def put(self, contents):
        if self.valid_contents(contents):
            self.__contents = contents
        else:
            raise ValueError()

    def contents():
        return self.__contents

    def valid_contents(self, contents):
        return isinstance(contents, int)
```

:::

The validation is now moved to a separate method named `valid_contents`.
This change is in accordance with [Curly's Law](https://workat.tech/machine-coding/tutorial/software-design-principles-dry-yagni-eytrxfhz1fla#curlys-law) that states that everything should have exactly one purpose.
In our experience, it is a good rule to live by and can avoid many a headache.
