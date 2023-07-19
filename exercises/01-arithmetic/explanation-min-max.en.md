# Built-In Functions

Python comes with a number of [built-in functions](https://docs.python.org/3/library/functions.html).
We focus here on two of them: [`min`](https://docs.python.org/3/library/functions.html#min) and [`max`](https://docs.python.org/3/library/functions.html#max).

`min` and `max` are functions that compute the minimum and maximum of their parameters, respectively.
Most functions expect a specific number of arguments, but `min` and `max` are known as [*variadic functions*](https://en.wikipedia.org/wiki/Variadic_function), meaning they can take any number of parameters.
We'll see later how to define your own variadic functions.

:::code{caption="Python Shell"}

```python
>>> min(4, 9)
4

>>> max(2, 6, 4, 7, 5, 4)
7
```

:::
