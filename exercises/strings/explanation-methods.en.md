# Extra String Operations

Programs are instructions that apply operations on all kinds of objects (integers, booleans, strings, &hellip;).
As of yet, these operations have taken two forms:

* Operators like `a + b`, `a - b`, `a < b`,`a == b`, `a and b`, `not a`, etc.
* Functions like `len(a)`, `min(a, b)`, etc.
  Functions are more flexible than operators thanks to their ability to have any number of operands/parameters.

There's also a third form: *methods*.
Their syntax is `a.method(b, c, d, ...)`.
You can interpret this as "I ask object `a` to perform its operation `method` with arguments `b, c, d, ...`".
A method is in essence a function that is a part of an object, and the syntax `a.method` asks `a` for that part.
Don't worry if this does not make sense yet, right now we only need to focus on the syntax.

::::INFO
Why there is this third form of syntax will become apparent later.
The idea of functions being part of objects is central to the [object oriented paradigm](https://en.wikipedia.org/wiki/Object-oriented_programming#OOP_languages), a topic which will be discussed later.
::::

## String Methods

Strings come with a bunch of methods.
We give an overview of a selection of them.
A full list of string methods can be found [online](https://docs.python.org/3/library/stdtypes.html#string-methods).

::::div{.formatted-table}
:::center

| Method | Description |
| ------ | ----------- |
| `s.lower()` | Returns a lowercase copy of `s` |
| `s.upper()` | Returns an uppercase copy of `s` |
| `s.find(subs)` | Returns the index of `subs` in `s` |
| `s.startswith(prefix)` | Checks if `s` starts with `prefix` |
| `s.endswith(suffix)` | Checks if `s` ends on `suffix` |
| `s.strip()` | Returns a copy where whitespace at both ends have been removed |
| `s.lstrip()` | Returns a copy where whitespace at the start have been removed |
| `s.rstrip()` | Returns a copy where whitespace at the end have been removed |
| `s.ljust(width, fill)` | Returns a left justified copy of size `width` padded with `fill` |
| `s.rjust(width, fill)` | Returns a right justified copy of size `width` padded with `fill` |

:::
::::

::::EXAMPLE

`lower()` and `upper()` work as you would expect.

:::code{caption="Python Shell"}

```python
>>> "ABC".lower()
"abc"

>>> "Test".upper()
"TEST"
```

:::

::::

::::EXAMPLE

`string.find(s)` looks for `s` within `string`.
If `s` occurs somewhere inside `string`, the starting index is returned, otherwise `-1`.

:::code{caption="Python Shell"}

```python
>>> "some string".find("tri")
6

# -1 in case substring was not found
>>> "some string".find("abc")
-1
```

:::

::::

::::EXAMPLE
`ljust`, `rjust` and `center` help with formatting strings.

:::code{caption="Python Shell"}

```python
>>> 'abc'.rjust(10)
'       abc'

# We can choose the padding character
>>> 'abc'.rjust(10, '.')
'.......abc'

>>> ' title '.center(20, '=')
'====== title ======='
```

:::

::::
