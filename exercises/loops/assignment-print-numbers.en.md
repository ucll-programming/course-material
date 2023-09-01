# Printing Numbers

::::TASK
Write a function `print_numbers(start, stop, step)` that prints out numbers:

* The first number to be printed is `start`.
  Next comes `start + step`, then `start + 2 * step`, etc.
  Continue until `stop` is reached or exceeded.
  `stop` itself should not be printed out.
* You can assume `step` is positive.
::::

::::USAGE

```python
>>> print_numbers(1, 5, 1)
1
2
3
4

>>> print_numbers(5, 10, 2)
5
7
9
```

::::

::::HINT
You will need a variable, say `i`, that goes through the sequence of the numbers to be printed.

* `i` needs to have an initial value, i.e., the first value to be printed.
  Start your function by assigning this initial value to `i`.
* Next comes the loop.
  The condition of the loop should put an upper bound on `i`.
  What value should `i` not surpass?
* Inside the loop body, two things need to happen:
  * The value of `i` needs to be printed.
  * `i` has to get its next value assigned.
::::
