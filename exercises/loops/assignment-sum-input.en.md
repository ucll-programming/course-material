# Sum of Inputs

We want a function that assists us with computing the sum of a series of numbers.
The function should repeatedly ask us for numbers using `input` until we enter `0`, after which the script prints out the sum, as shown below.

::::TASK
Write a function `sum_input()` that performs the task described above.

* To make the tests happy, use `input(prompt)` to show the `"Enter integer: "` prompt, i.e., do not use `print` for this.
* The function should not return the sum, but print it out as shown below.
::::

::::USAGE

```python
>>> sum_input()
Enter integer: 1
Enter integer: 2
Enter integer: 3
Enter integer: 4
Enter integer: 0
The sum equals 10.
```

::::
