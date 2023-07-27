# Interval

For this exercise, you'll be making an `Interval` class with multiple methods.
We will implement it step by step.

## Initialization

::::TASK
Create a class `Interval`.

* It should have two fields: `lower` and `upper`.
* The constructor should allow the user to initialize these fields.

Note that if `lower` is greater than `upper`, the interval is considered empty.
::::

::::USAGE

```python
>>> interval = Interval(1, 9)
>>> interval.lower
1

>>> interval.upper
9
```

::::

## `contains`

::::TASK
Add a method `contains(value)` that checks if `value` falls in the interval.
::::

::::USAGE

```python
>>> interval = Interval(1, 5)
>>> interval.contains(1)
True

>>> interval.contains(2)
True

>>> interval.contains(5)
True

>>> interval.contains(0)
False

>>> interval.contains(6)
False
```

::::
