# Introduction

Python has a special value called `None` which is meant to represent "a missing value".
For example, if a function requires the handle to your Twitter account as a parameter, but you have no account there, `None` can be used to indicate this.

:::code{caption="Python"}

```python
def register_user(name, email_address, twitter_handle):
    # ...


# John has no Twitter account
register_user("John Jackson", "john.jackson@gmail.com", None)
```

:::

`None` is quite a boring value.
The only useful operation you can use on it is comparison:

:::code{caption="Python"}

```python
if variable == None:
    # ...
```

:::

::::INFO
Technically, if you want to check if a variable contains `None`, it is better to use the `is` operator:

:::code{caption="Python"}

```python
if variable is None:
    # ...
```

:::

What `is` does exactly will be discussed later.
Using `==` will also work, but it is less efficient.
::::

