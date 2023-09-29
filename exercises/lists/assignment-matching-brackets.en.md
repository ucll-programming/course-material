# Matching Brackets

In a previous exercise, you had to check if a string contained balanced parentheses.
This exercise is the same, except that you'll be dealing with multiple kinds of brackets:

* `(` needs a matching `)`
* `{` needs a matching `}`
* `[` needs a matching `]`

:::TASK
Write a function `matching_brackets(string)` that checks if `string` contains only matched brackets.
:::

:::USAGE

```python
>>> matching_brackets('')
True

>>> matching_brackets('()')
True

>>> matching_brackets('(}')
False

>>> matching_brackets('({)}')
False
```

:::
