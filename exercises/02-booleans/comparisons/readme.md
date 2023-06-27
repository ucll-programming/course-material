# Comparisons

In the previous section, you were introduced to all kinds of operators and functions: `+`, `-`, `*`, `min`, `max`, etc.
These all have one thing is common: they all operate on numbers and yield numbers as result.

Let's take a look at a series of other operators, which should be very familiar to you:

| Python Syntax | Mathematical Notation | Description |
| :-----------: | :-------------------: | :---------- |
| `==` | $=$ | equal to |
| `!=` | $\neq$ | not equal to |
| `<`  | $<$ | less than |
| `>`  | $>$ | greater than |
| `<=` | $\leq$ | less than or equal to |
| `>=` | $\geq$ | greater than or equal to |

What would the result be of such a comparison?
If you were to open a terminal and enter a comparison, you would get

```python
>>> 1 == 1
True

>>> 1 == 2
False
```

`True` and `False` are a new type of value called *booleans*.
As with integers, you can store them in variables, pass them as parameters and return them from functions.

Numbers have all kinds of operations defined on them, such as addition, subtraction, multiplication, etc.
Booleans have their very own set of operators: `and`, `or` and `not`.
We will discuss them in detail later.

Make sure to notice the difference between `=` and `==`:

* `a = b` takes the value of `b` and *assigns* it to `a`.
* `a == b` compares the values of `a` and `b`, leaving both variables unchanged.

It is a common error to confuse the two operators.
