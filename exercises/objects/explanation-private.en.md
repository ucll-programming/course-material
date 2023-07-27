# Private Members

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

This class definition tells us that a `Box` object has three members:

* a field `contents`;
* three methods named `is_empty`, and `put`.

All these members are publicly available, i.e., anyone with access to a `Box` object can make use of these members.
When we told you about abstraction, we explained how we should *hide* the internals and define a clean, easy-to-use public interface.
So, let's hide something, namely the field `contents`.

:::code{caption="Python"}

```python
class Box:
    def __init__(self, contents):
        self.__contents = contents

    def is_empty(self):
        return self.__contents is None

    def put(self, contents):
        self.__contents = contents
```

:::

The only change we needed to make is rename `contents` to `__contents`.
Python recognizes this naming pattern and understands that you mean to make that field private:

:::code{caption="Python Shell"}

```python
>>> box = Box(8)
>>> box.__contents
AttributeError: 'Box' object has no attribute '__contents'
```

:::

Our `Box` class has become even more useless than before!
We can't even access its contents anymore.
Let's make it available again by defining a method:

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

Let's put it to use:

:::code{caption="Python Shell"}

```python
>>> basket = Box("lotion")
>>> basket.contents()
"lotion"
```

:::

Let's summarize:

* `__contents` is a private field.
* There are three public methods: `is_empty`, `put` and `contents`.
  They give us access to `__contents` in an albeit indirect way.

We'll discuss the benefits of this in the next section.
