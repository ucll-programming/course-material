# Is Student Id?

We want to be able to check whether a string forms a valid student id.
The rules are as follows:

* A student id must count exactly eight characters.
* The first character must be an `r` or an `s`.
  Both upper and lowercase are acceptable.
* The remaining seven characters must all be digits.

:::TASK
Write a function `is_student_id(string)` that returns `True` if `string` is a valid student id, `False` otherwise.
:::

:::USAGE

```python
>>> is_student_id('r0123456')
True

>>> is_student_id('R0123456')
True

>>> is_student_id('s0123456')
True

# Too short
>>> is_student_id('r012345')
False

# Missing first letter
>>> is_student_id('01234567')
False

# Wrong first letter
>>> is_student_id('u0123456')
False

# Second character should be digit
>>> is_student_id('us123456')
False
```

:::

:::HINT
We strongly suggest to write a separate `is_digit(char)` function.
While it is possible to implement this as a long series of equality checks, don't forget you can also rely on `<=`.
Using `in` can also lead to a succinct solution.
:::

:::INFO
It requires a lot of repetitive code to check all eight characters in the string.
Soon you will learn how *loops* will allow you to do this with much less code.
:::
