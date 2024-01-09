# Duration

:::INFO
This exercise is a bit longer than usual.
As of yet, the only reason you wrote functions is, well, because we asked you to.
However, when writing more complex code, functions help you split it up in manageable parts.

In this exercise, we will ask you to write functions that build on top of each other.
That is how software is also build, as large pyramids of functions: lots of little functions at the bottom which are relied upon by the layer of functions just above, etc.
:::

Say you receive a duration expressed in seconds.
You would like to see this duration expressed in hours, minutes and seconds.
For example, 10000 seconds can be written as 2 hours, 46 minutes and 40 seconds.
We will implement this logic as three different functions: `hours`, `minutes` and `seconds`.

## `hours`

Let's start with `hours(duration)`.
Here, the parameter `duration` is a number representing a total number of seconds.
`hours(duration)` must return the number of *complete* hours that fit in this duration.
Remember that an hour equals 3600 seconds.

:::USAGE

```python
# 2000 seconds is less than an hour, so 0 hours fit
>>> hours(2000)
0

>>> hours(3600)
1

>>> hours(7200)
2

>>> hours(7201)
2
```

:::

:::TASK
Write a function `hours(duration)` that returns the number of hours that fit in `duration` seconds.
:::

:::HINT
A simple integer division (`//`) should do.
:::

## `minutes`

We now focus on the minutes.
We only want to count the minutes left over after having taken care of the hours.
For example, `minutes(3600)` should return `0` and not `60`.
In other words, `minutes(duration)` should only return values between `0` and `59` (inclusive).

:::USAGE

```python
# Not enough seconds for one full minute
>>> minutes(59)
0

# Exactly one minute
>>> minutes(60)
1

# Just shy of 2 minutes
>>> minutes(119)
1

# One hour and one minute
>>> minutes(3660)
1
```

:::

Our suggested approach to implement `minutes` is:

* First rely on `hours` to determine the number of hours `h`.
  To call your own function `hours` and store its result in a local variable `h`, you can write `h = hours(duration)`.
* Subtract `3600 * h` from `duration`.
* Find the number of minutes in this new version of `duration`.
  Again, a simple integer division will suffice.

:::TASK
Write a function `minutes(duration)` that counts the number of minutes in `duration`.
Use the algorithm described above.

The result should be an integer between `0` and `59` (inclusive).
:::

## `seconds`

Lastly we arrive at seconds.
To implement this, we use the same trick as with `minutes`:

* Rely on `hours` to determine the amount of hours `h`.
* Subtract `h * 3600` from `duration`.
* Use `minutes` to get the number of minutes `m`.
* Subtract `m * 60` from `duration`.
* What's left over is the number of seconds.

:::TASK
Write a function `seconds(duration)` that computes the remaining number of seconds.

The result should be an integer between `0` and `59` (inclusive).
:::

:::INFO
Later on we will learn how you can write a single function that returns multiple values.

Also, the calculations can be simplified using the modulo operator `%` as will be shown later.
:::
