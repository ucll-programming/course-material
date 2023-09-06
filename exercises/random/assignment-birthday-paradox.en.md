# Birthday Paradox

In a classroom of 23 students, what are the odds that two students share a birthday?
The answer is 50.7%, which to many people comes off as very unintuitive and for this reason known as the [birthday paradox](https://en.wikipedia.org/wiki/Birthday_problem).

Let's write some code that verifies this.
We proceed as follows:

* We represent birthdays by the numbers 1 to 365 (apologies to those born on 29th February).
* We pick 23 random numbers between 1 and 365.
* We check if two of these numbers are equal.

We repeat this many times and count in how many cases there are shared birthdays.

::::TASK
Write a function `birthday_paradox(n, simulation_count)` that determines how likely it is that a room with `n` people share a birthday.
::::

::::USAGE

```python
>>> birthday_paradox(1, 100)
0

>>> birthday_paradox(23, 10000)
50.7   # approximately
```

::::
