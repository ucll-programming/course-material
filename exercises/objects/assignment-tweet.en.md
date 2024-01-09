# Tweet

You got yourself a job at Twitter!
Or X.
Or whatever Elon has set his mind to by the time you read this.

A Tweet has a maximum length.
But what this exact length is tends to change rather arbitrarily.
You decide to make your code flexible enough to deal with this variable length.

::::TASK
Create a class `Tweet`:

* It has two private fields: message and max_length.
* Its constructor takes two parameters allowing you to initialize these fields.
* It has a public property `message` (get &amp; set) which gives you access to the tweet's message.
  The setter must guard against oversized tweets: if the new value exceeds the maximum length, it gets truncated.
* It also has a public property `max_length` (get &amp; set).
  * If `max_length` is set to a new value, it has to make sure that the current message doesn't exceed it.
    If it does, the message gets truncated.
  * `max_length` must at least be `1`.
    If the user sets it to a lower value, raise a `ValueError`.

Note: you can make private methods too.
You can use these to prevent having to duplicate code inside your class.
To make a method private, simply have their name start with two underscores.
::::

:::code{caption="Python"}

```python
>>> tweet = Tweet("1234567", 10)
>>> tweet.message
"1234567"

# Max length exceeded, message gets truncated
>>> tweet = Tweet("1234567", 5)
>>> tweet.message
"12345"

>>> tweet.max_length = 20
>>> tweet.message
"12345"

# Setting max length will automatically truncate message if it is too long
>>> tweet.max_length = 3
>>> tweet.message
"123"

# Setting invalid length raises ValueError
>>> tweet.max_length = 0
ValueError
```

:::
