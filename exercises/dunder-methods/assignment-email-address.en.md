# Email Addresses

For this exercise, we will consider an email address to be valid if it contains exactly one `@` symbol.

Email addresses are case insensitive: `foo@gmail.com` and `FOO@GMAIL.COM` are the same address.

::::TASK
Write a class `EmailAddress`:

* Its constructor takes a string representing the email address.
  It throws a `ValueError` if this string is not a valid email address.
* The email address is stored in a private field.
* The email address can be queried using `str(email_address)`.
* Provide a sensible implementation for `repr(email_address)`.
* Implement equality.
::::

::::USAGE

```python
# Invalid email address, it is missing an @ symbol
>>> email_address = EmailAddress('test')
ValueError

>>> email_address = EmailAddress('bar@gmail.com')
>>> str(email_address)
bar@gmail.com

>>> repr(email_address)
EmailAddress('bar@gmail.com')

>>> EmailAddress('xyz@gmail.com') == EmailAddress('XYZ@gmail.com')
True

>>> EmailAddress('xyz@gmail.com') == EmailAddress('xyz@yahoo.com')
False
```

::::
