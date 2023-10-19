# Operators

Just like integers and booleans, strings have all kinds of operations defined on them.
We'll discuss a number of them here.
We start with an overview, after which we shortly discuss them in turn.

::::div{.formatted-table}
:::center

| Syntax | Result | Description |
| ------ | ----------- | ------- |
| `"ab" + "cd"` | `"abcd"` | Concatenation |
| `"ab" * 3` | `"ababab"` | Repetition |
| `"a" in "abc"` | `True` | Membership |
| `"a" == "a"` | `True` | Equality |
| `"a" != "a"` | `False` | Inequality |
| `"a" < "b"` | `True` | Lexicographic comparison |
| `"a" <= "b"` | `True` | Lexicographic comparison |
| `"a" > "b"` | `False` | Lexicographic comparison |
| `"a" >= "b"` | `False` | Lexicographic comparison |
| `len("abc")` | `3` | Length |

:::
::::

## String Concatenation

Concatenation is a fancy name for joining strings together.

:::code{caption="Python Shell"}

```python
>>> "Hello" + "World"
"HelloWorld"
```

:::

As you can see, you can add strings together using the `+` operator.

::::EXAMPLE
Some code that exemplifies the difference between integers and strings:

:::code{caption="Python Shell"}

```python
>>> 1 + 2
3

>>> "1" + "2"
"12"
```

:::

::::

::::INFO
The operator `+` is reused in many places:

* You can add integers: `5 + 8`.
* You can add floats: `1.2 + 3.4`.
* You can add strings: `"abc" + "def"`.

Assigning multiple meanings to the same thing is called *overloading*, or, in our case, more specifically, [operator overloading](https://en.wikipedia.org/wiki/Operator_overloading).
At a later point, we will discuss how you can overload operators yourself.
::::

## Repetition

The `*` operator allows you to repeat a string an arbitrary number of times:

:::code{caption="Python Shell"}

```python
>>> "x" * 10
'xxxxxxxxxx'
```

:::

## Membership Checking

The `in` (and its negation `not in`) can be used to see if a string contains another.

:::code{caption="Python Shell"}

```python
# Can't spell slaughter without laughter
>>> "laughter" in "slaughter"
True

# There's no I in team
>>> "i" not in "team"
True
```

:::

## Lexicographic Comparison

Lexicographic comparison actually does what you intuitively would expect `s1 < s2` would do: it checks whether `s1` would come before `s2` in a dictionary.

:::code{caption="Python Shell"}

```python
>>> "Aaronson" < "Zukowski"
True
```

:::

Remark, however, the following details:

* Comparison is *case sensitive*: `"B" < "a"` evaluates to `True`, because uppercase letters are considered "smaller" than lowercase letters.
* Every character (`5`, `@`, space, &hellip;) has a specific place in the "alphabet".
  For example, `' ' < 'A'`.
  The actual order is determined by [The Unicode Standard](https://en.wikipedia.org/wiki/List_of_Unicode_characters).

## String Length

Admittedly, `len` is not an operator but just a function.
But do you really want a separate page just for `len`?

`len` hides no surprises: it returns the length of the string.

:::code{caption="Python Shell"}

```python
>>> len('schnackenpfefferhausen')
22
```

:::
