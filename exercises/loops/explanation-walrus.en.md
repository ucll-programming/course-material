# Walrus Operator

The [walrus operator](https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions) is an operator that can help write more readable code.
It is a slightly more advanced topic and we don't expect you to use it, but for those students who are willing to go the extra mile, it's good to know it exists.

:::code{caption="Python"}

```python
value = int(input("Enter an integer: "))
while value != 0:
    print(value)
    value = int(input("Enter an integer: "))
```

:::

The code above reads integers from the keyboard and prints them out.
It stops as soon as the user inputs `0`.

The code above contains some duplication: `int(input("Enter an integer: "))` occurs twice.
We should get rid of this, as duplication can easily lead to bugs.

## Using Helper Function

One solution consists of introducing a helper function:

:::code{caption="Python"}

```python
def input_integer():
    return int(input("Enter an integer: "))


value = input_integer()
while value != 0:
    print(value)
    value = input_integer()
```

:::

We expect you to be able do perform this kind of code cleanup.

## Using Walrus Operator

Another approach would be to rely on the walrus operator.

`a = b` and `a := b` do exactly the same thing: they evaluate `b` and assign the result to `a`.
The difference between both lies in *where* you are allowed to use them.

`a = b` is a *statement*, which means you cannot but it inside something else.
For example `print(a = b)` is invalid.
An assignment always belongs on a line of its own.

`a := b` is an *expression* and belongs "inside" something else.
Writing `a := b` on a separate line will cause an error.
However, `print(a := b)` is okay.
But this raises the question, what would `print(a := b)` output?

All expressions evaluate to a value.
For example, `3 + 5` is also an expression and it evaluates to `8`.
So what does `a := b` evaluate to?
Simple: it evaluates to the value of `b`.

::::EXAMPLE

:::code{caption="Python"}

```python
print(a := 2 * 5)
```

:::

* Before we can call `print`, we need to evaluate its argument `a := 2 * 5`.
* `a := 2 * 5` first evaluates its right hand side.
* `2 * 5` yields `10` as result.
* This result is then assigned to `a`.
* `a := 2 * 5` as a whole evaluates to `10`.
* This is used as argument for `print`.
* Ultimately, `10` is written to the screen.

::::

Let's apply the walrus operator to our loop.

:::code{caption="Python"}

```python

while (value := int(input("Enter an integer: "))) != 0:
    print(value)
```

:::

Here, we made the `input` functionality part of the condition.
Whenever the condition of the `while` is evaluated, the user will be asked for an integer.
This integer will be assigned to `value` and then be compared to `0`.

In the end, the walrus operator is never needed: it did not even exist prior to Python 3.8 and was purely added for convenience.

::::INFO
Very few languages make the distinction between `=` and `:=`.
`a = b` is generally considered an expression and can be used anywhere.
Why does Python make it so complicated?

A common mistake is to confuse `=` with `==`:

:::code{caption="Python"}

```python
if a = b:    # Should be a == b
    # ...
```

:::

To catch this mistake, Python made it an error to use `=` in an expression, i.e., `=` must be used on its own line.
This constraint, in turn, caused some need for duplication (see example at the top.)
To counter this, `:=` was added to the language.
::::
