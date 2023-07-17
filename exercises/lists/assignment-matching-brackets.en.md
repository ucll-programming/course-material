# Matching Brackets

In a previous exercise, you had to check if a string contained balanced parentheses.
This exercise is the same, except that you'll be dealing with multiple kinds of brackets:

* `(` needs a matching `)`
* `{` needs a matching `}`
* `[` needs a matching `]`

:::TASK
Write a function `balanced_brackets(string)` that checks if `string` contains only balanced brackets.
:::

:::USAGE

```python
>>> balanced_brackets('')
True

>>> balanced_brackets('()')
True

>>> balanced_brackets('(}')
False

>>> balanced_brackets('({)}')
False
```

:::
