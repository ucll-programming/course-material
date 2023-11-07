# Introduction

We can distinguish two uses for tuples:

* On the one hand, we can simply see them as a readonly list.
  Typically, the items all have the same type.
* On the other hand, tuples can be used to bundle data together.
  For example, a playing card has a value (integer) and a suit (string).

In this chapter, we focus on the latter usage.

Say we want to keep track of users.
We need the following data:

* The user's name.
  We want the user's first name and last name as two separate strings.
* The user's email address.
* The user's address, which is composed of
  * Street
  * House number
  * ZIP code
  * City
  * Country

We can represent this using tuples:

:::code{caption="Python"}

```python
user_data = (
    ("Sherlock", "Holmes"),
    "sherlock.holmes@aol.com",
    (
        "Baker Street",
        "221b",
        "NW1 6XE",
        "London",
        "United Kingdom"
    )
)
```

:::

In order to fetch specific information, we need to know the exact index, e.g., `user_data[2][4]` retrieves the user's country.
This approach, however, is extremely error prone.
Nothing about `user_data[2][4]` expresses that it fetches the country.
You can also imagine how messy things get if we need to add or removes fields and index updates are required across the entire code base.

A much more readable solution would have us assign *names* to the different parts of the tuple, so that we could write `user_data.address.country` instead of `user_data[4][2]`.
This is exactly what named tuples allow use to do:

:::code{caption="Python"}

```python
from collections import namedtuple


UserData = namedtuple("UserData", [
    "name",
    "email_address",
    "address"
])

Name = namedtuple("Name", [
    "first_name",
    "last_name"
])

Address = namedtuple("Address", [
    "street_name",
    "house_number",
    "zip_code",
    "city",
    "country"
])


user_data = UserData(
    Name("Sherlock", "Holmes"),
    "sherlock.holmes@aol.com",
    Address("Baker Street", "221b", "NW1 6XE", "London", "United Kingdom")
)

user_data.name.first_name   # Sherlock
user_data.address.country   # United Kingdom
```

:::

## Defining a Named Tuple

First, you need to define the structure of the new named tuple.
This includes the *name* (e.g., `Address`) and the fields (e.g., `street_name`, `house_number`, &hellip;)

:::code{caption="Python"}

```python
Name = namedtuple("Name", ["field1", "field2", "field3", ...])
```

:::

The name has to be repeated twice.
It is inconvenient but unavoidable.

::::IMPORTANT
The name of the tuple defines a new *type*: it becomes a "colleague" of `int`, `str`, `bool`, etc.
Custom types have their own [naming convention](https://peps.python.org/pep-0008/#class-names):
the words in the name are capitalized and joined together without separator.
For example, `UserData` is correct, `user_data`, `User_Data`, `User_Data` are wrong.
::::

## Creating Tuple Objects

Once you have defined the new type, you can create objects of that type.

:::code{caption="Python"}

```python
obj = Name(field1_value, field2_value, field3_value, ...)
```

:::

::::INFO
Getting the argument order right is still tricky when creating an large tuple such as `Address`.
Keyword arguments (discussed elsewhere) can help out:

:::code{caption="Python"}

```python
user_data = UserData(
    name=Name(
        first_name="Sherlock",
        last_name="Holmes"),
    email_address="sherlock.holmes@aol.com",
    Address(
        street_name="Baker Street",
        house_number="221b",
        zip_code="NW1 6XE",
        city="London",
        country="United Kingdom"
    )
)
```

:::
::::

## Accessing Fields

Once you have created a new tuple object, you can access its field with the `.` operator:

:::code{caption="Python"}

```python
obj.field1    # Evaluates to field1_value
obj.field2    # Evaluates to field2_value
obj.field3    # Evaluates to field3_value
...
```

:::
