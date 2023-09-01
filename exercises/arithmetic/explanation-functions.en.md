# Functions

An *algorithm* is a series of instructions that, when followed, achieve a certain goal.
Cooking recipes are an example of algorithms: follow the recipe's steps and you'll end up with a (hopefully) delicious dish.
A programming language, such as Python, allows you to write down instructions in a way that your computer can understand them.

Recipes are given names: chili con carne, cacio e pepe, larb kai, etc.
The same can be done for algorithms in programming languages: we bundle the instructions together and give them a name.
Such a named group of instructions is called a *function*.

::::EXAMPLE

:::code{caption="Python"}

```python
def my_function():
    instruction1
    instruction2
    instruction3
    ...
```

:::
The code shown above defines a function named `my_function`.
::::

## Return Values

When following a recipe, you end up with some dish.
Similarly, functions can also produce a result.
This result is called the *return value* of the function.

::::EXAMPLE
:::code{caption="Python"}

```python
def zero():
    return 0
```

:::
Here we have defined a very simple function that produces `0` as return value.
::::

## Calling a Function

Once you have defined a function, you can *call* it.
This means that you want all instructions contained within the function to be executed.
Calling a function is done with `function_name()`.

::::EXAMPLE
You can test this out in the Python shell:

:::code{caption="Python Shell"}

```python
>>> def zero():
...     return 0

>>> zero()
0
```

:::
::::
