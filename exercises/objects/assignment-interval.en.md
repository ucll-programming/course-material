# Interval

For this exercise, you'll be making an `Interval` class with multiple methods.
We will implement it step by step.

## Initialization

::::TASK
Create a class `Interval`.

* It should have two fields: `lower` and `upper`.
* The constructor should allow the user to initialize these fields.
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

## `is_empty`

::::TASK
Add a method `is_empty()` that returns `True` if the interval is empty, `False` otherwise.

An interval is empty if `lower` is greater than `upper`.
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

## `overlaps_with`

::::TASK
Add a method `overlaps_with(other)` that checks if the current interval (`self`) overlaps with the given interval (`other`).
Intervals overlap when they have at least one element in common.

Make sure you get all corner cases right, and keep it efficient.
::::

::::USAGE

```python
>>> Interval(1, 5).overlaps_with(Interval(6, 10))
False

>>> Interval(1, 5).overlaps_with(Interval(4, 8))
True

>>> Interval(1, 2).overlaps_with(Interval(2, 3))
True

>>> Interval(1, 5).overlaps_with(Interval(2, 3))
True
```

::::

::::HINT{caption="Hint 1"}
First deal with the cases where one of the intervals is empty.
You know that nothing can overlap with an empty interval.
::::

::::HINT{caption="Hint 2"}
Check if the endpoints of one interval are contained in the other interval.
::::
