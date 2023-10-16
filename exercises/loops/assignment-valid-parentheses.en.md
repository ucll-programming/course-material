# Valid Parentheses

You are given a string that contains only parentheses, for example `"()(())"`.
We say the string is *valid* if

* Every opening parenthesis has a matching closing parenthesis.
  This closing parenthesis must come after the opening parentheses.
  For example, `)(` is not considered valid.
* Similarly, every closing parenthesis must have a matching opening parenthesis.
  In other words, we cannot have too many closing parentheses.

:::TASK
Write a function `valid_parentheses(string)` that returns `True` if `string` satisfies the rules above or `False` otherwise.
:::

:::USAGE

```python
# Empty string is valid
>>> valid_parentheses("")
True

>>> valid_parentheses("(")
False

>>> valid_parentheses(")")
False

>>> valid_parentheses("()")
True

>>> valid_parentheses(")(")
False

>>> valid_parentheses("()()(()())")
True
```

:::


