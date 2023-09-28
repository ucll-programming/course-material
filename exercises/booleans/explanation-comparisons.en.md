# Comparisons

In the previous section, you were introduced to all kinds of operators and functions: `+`, `-`, `*`, `min`, `max`, etc.
These all have one thing is common: they all operate on numbers and yield numbers as result.

Let's take a look at a series of other operators, which should be very familiar to you:

::::div{.formatted-table}
:::center

| Python Syntax | Mathematical Notation | Description |
| :-----------: | :-------------------: | :---------- |
| `==` | $=$ | equal to |
| `!=` | $\neq$ | not equal to |
| `<`  | $<$ | less than |
| `>`  | $>$ | greater than |
| `<=` | $\leq$ | less than or equal to |
| `>=` | $\geq$ | greater than or equal to |

:::
::::

What would the result be of such a comparison?
If you were to open a Python shell and enter a comparison, you would get

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

:::WARNING
Make sure to notice the difference between `=` and `==`:

* `a = b` takes the value of `b` and *assigns* it to `a`.
* `a == b` compares the values of `a` and `b`, leaving both variables unchanged.

It is a common error to confuse the two operators.
:::

:::INFO
Confusingly, Python actually allows you to apply `+`, `-`, `*`, ... on boolean values.
But we beg you, please resist the temptation to, for the following reasons:

* Python happens to be one of the few languages (e.g., JavaScript, C, C++) that allow this, but most others (e.g., C#, Java, Ruby, Go, Rust, Kotlin, Scala, Racket, ...) will consider it an error.
  We prefer you to learn to write code that doesn't rely on tricks that only work in very limited cases.
* To others, using `+`, `-`, etc. will automatically create the impression that you're working on numbers, thus confusing them.
  Writing readable code is your number two priority (your number one priority being that your code should behave correctly.)

So, in summary: we ask you to just assume `+`, `-`, `*`, etc. are not usable on boolean values.
:::
