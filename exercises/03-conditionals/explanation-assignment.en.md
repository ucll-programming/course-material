# Assignment

In a previous section, you were shown how you could introduce local variables to store intermediate results:

```python
def my_function():
    y = 2
    print(y)
```

Calling `my_function()` will print out `2`.

You can also overwrite a variable's value using the same syntax:

```python
def my_function():
    y = 2
    print(y)    # Prints 2
    y = 3
    print(y)    # Prints 3
```

## Sequential Evaluation

Some students misinterpret how assignment works.
Consider the following code:

```python
def my_function():
    x = 1
    y = 2 * x
    print(x, y)
    x = 10
    print(x, y)
```

Take a good look at the code and predict what ´my_function()` will print before continuing reading.

&vellip;

* The first line is straightforward: it introduces a new local variable `x` and sets it to `1`.
* The second line is where confusion can arise.
  The exact interpretation is "Evaluate `2 * x` and store the result in `y`".
  At this point in time, `x` equals `1`, so `2 * x` evaluates to `2`, which is stored in `y`.
* The `print` on the third line writes `1 2` to the console.
* `x = 10` assigns a new value to `x`.
  Here, it is crucial to understand that `y` is left unchanged.
* The second `print` writes `10 2` to the console.

Some people, possibly inspired by Microsoft Excel, think that `y = 2 * x` introduces a "relationship" so that `y` is to be equal to `2 * x` at all times.
In their minds, `x = 10` causes `y` to magically be updated to `20` as a way to preserve this relationship.
While this is certainly a valid interpretation of how things *could* work, in Python this is *not* how it works!

:::IMPORTANT
If you are confused by this section, make sure to ask the lecturer for more explanations.
:::

## Augmented Assignment

Take a look at this line of code:

```python
x = 4
x = x + 1
print(x)
```

Mathematical minds might be confused by the second assignment: how can `x` be equal to `x + 1`?
That looks like circular reasoning!

However, as a programmer, you should know how to interpret this assignment:

* First, evaluate the right hand side: take the current value of `x` and add `1` to it, which yields `5`.
* Next, assign this result to `x`.

In other words, executing these two lines of code will cause `5` to be printed out.

This pattern of reading and writing to the same variable (e.g., `x = x + 1`, `y = y * 2`, etc.) occurs quite often in code.
For this reason, a shorthand notation has been introduced:

```python
x = x + 1
# can also be written as
x += 1

y = y * 2
# can also be written as
y *= 2
```

For most operators, this shorthand `x op= y` notation exists.

:::INFO
In case you're already familiar with certain other programming languages, know that Python does not support the `i++` notation.
You'll have to write `i += 1`.
:::
