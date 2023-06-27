# A Tale of Two Numbers

Your computer has two ways of representing numbers: integers and floating point numbers.

* [Integers](https://en.wikipedia.org/wiki/Integer_(computer_science)) can represent arbitrarily large *whole* numbers such as `0`, `1`, `803980` and `-34890840`, but not decimal numbers like `1.5`.
  However, integers are quite efficient.
* [Floating point numbers](https://en.wikipedia.org/wiki/Floating-point_arithmetic) are also able to represent whole numbers, but also support decimal numbers such as `0.1`, `1.5`, `3.1415`.
  While it may seem floating point numbers can represent any number, they have their limitations.
  The rules are too complicated to go into detail here.
  Working with floating point numbers is typically also less efficient.

So, when it comes to whole numbers, such as `5`, you can choose between two internal representations:

* The integer representation is simply written `5`.
* The floating point representation is written `5.0`.

For example, you can ask Python which type of number you are dealing with:

```python
>>> type(5)
<class 'int'>

>>> type(5.0)
<class 'float'>
```

From now on, we'll use the Python names `int` and `float` to refer to the different representations.

## How To Choose

If you're wondering which type of number (`int` of `float`) to use, here's a rule of thumb: use `int` whenever you can, and only `float` when you actually need decimal numbers.

An example of the limitations of floating point numbers:

```python
# Everything okay here
>>> 2 * 0.1 == 0.2
True

# Uhh?
>>> 3 * 0.1 == 0.3
False

# Okay, things make sense again
>>> 4 * 0.1 == 0.4
True

#
>>> 5 * 0.1 == 0.5
True

>>> 6 * 0.1 == 0.6
False

>>> 7 * 0.1 == 0.7
False
```

There are plenty of sources that explain this behavior.
For your convenience, here's [one](https://docs.python.org/3/tutorial/floatingpoint.html).
