# Entrance Exam

An entrance exam consists of five tests, each one being graded on 20.
The rules for passing are

* It is allowed to skip at most one test.
* The average of the tests that were taken must be at least 12.

:::TASK
Write a function `entrance_exam(grade1, grade2, grade3, grade4, grade5)` that returns `True` if the given grades are good enough to pass, `False` otherwise.

A skipped test will be represented by the value `None`.
:::

:::USAGE

```python
# Took all tests, average 12 good enough
>>> entrance_exam(12, 12, 12, 12, 12)
True

# Took four tests, average 12 good enough
>>> entrance_exam(12, 12, 12, None, 12)
True

# Took four tests, average 10 not good enough
>>> entrance_exam(12, 12, 12, 2, 12)
False

# Skipped too many tests
>>> entrance_exam(20, 20, 20, None, None)
False
```

:::

:::HINT
This exercise will require some repeated code.

Keep three local variables:

* One variable to count the number of skipped tests.
* One variable to count the number of taken tests.
* One variable to take the total grade.

Go through all give grades one by one and update the variables.
Next, check that the number of skipped tests is low enough.
Finally, compute the average and check that it is high enough.
:::