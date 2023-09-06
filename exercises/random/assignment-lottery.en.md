# Lottery

Let's solve the lottery problem introduced previously.

In a lottery, we have to pick $k$ numbers out of $N$ possible numbers.
At some later point in time, $k$ winning numbers are drawn.
We win the lottery it the numbers we picked all coincide with the winning numbers.

::::TASK
Write a function `lottery(k, n, simulation_count)` that determines the winning percentage for a lottery where `k` numbers out of `n` have to be guessed correctly.
Simulate it `simulation_count` times.
::::

::::USAGE

```python
# Easy lottery
>>> lottery(5, 5, 1000)
100

>>> lottery(1, 10, 100000)
10     # or at least a value close to 10
```

::::

::::WARNING
Due to the inherent inaccuracy of our approach, it could be that the tests fail undeservedly.
Feel free to rerun the tests if you think you've been judged unfairly.
::::

::::HINT
Take a look at the [documentation](https://python.readthedocs.io/en/stable/library/random.html) for `random`.
It contains a function that does a lot of the work for you.
::::
