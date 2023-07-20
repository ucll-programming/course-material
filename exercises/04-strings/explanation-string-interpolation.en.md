# String Interpolation

Programs often need to construct strings at runtime.
Python offers an easy way to do this.

:::code{caption="Python"}

```python
item_count = 5
day = 23
month = 5
message = f"Your order containing {item_count} items will be delivered on {day}/{month}"
```

:::

After executing this code, message will be set to

```text
Your order containing 5 items will be delivered 23/5
```

Building a string by "injecting" values is called [*string interpolation*](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals).
In order to activate string interpolation, you must prefix the string literal with `f`.
Without the `f`, no "injections" will take place and you will end up with literally `"Your order containing {item_count} items will be delivered on {day}/{month}"`.

You're not limited to putting variable names between the `{ }`: expressions will also work.
`f"{x} + {y} is equal to {x + y}"` will produce the expected result.

## Formatting Options

It is possible to tell Python how the injected values should be formatted using the `{expr:formatting}` syntax.
There are many options; you can find an overview [here](https://docs.python.org/3/library/string.html#formatspec).
We give a few examples below.

In practice, you should simply be aware that it is possible to specify a format.
When you need to format things a certain way, you should be aware you can check if there's a format specifier doing exactly what you need instead of trying to do the formatting manually.

::::EXAMPLE
A time of day is typically formatted `09:07:03` and not `9:7:3`, i.e., the numbers should always count two digits.
This can be achieved by adding `:02`:

* The `2` means the number should at least be 2 characters long.
* The preceding `0` indicates we want extra `0`'s to be added in case the number is too short.

:::code{caption="Python Shell"}

```python
>>> h = 1
>>> m = 2
>>> s = 3
>>> f'{h:02}:{m:02}:{s:02}'
"01:02:03"
```

:::
::::

::::EXAMPLE
It is possible to have floating point numbers show a specific number of decimals:

:::code{caption="Python Shell"}

```python
>>> pi = 3.141592
>>> f'{pi:.2f}'
"3.14"
```

:::
::::

::::EXAMPLE
You can left align, right align and center:

:::code{caption="Python Shell"}

```python
>>> text = 'abc'
>>> f"{text:<10}|{text:>10}|{text:^10}|"
'abc       |       abc|   abc    |'
```

:::
::::
