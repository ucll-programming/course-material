# Averager

::::TASK
Create a class `Averager` that assists in the computation of averages:

* The constructor takes no parameters.
* A method `add(value)` adds `value` to the list of values.
* A method `average()` returns the average of all values that have been previously `add`ed.
* A method `reset()` that lets the object forget about all previously `add`ed values.

Note that you don't need to keep a list of all values.
Instead, simply keep track of the sum and the number of added values.
::::

::::USAGE

```python
>>> averager = Averager()
>>> averager.add(10)
>>> averager.add(20)

# Returns average of [10, 20]
>>> averager.average()
15

>>> averager.add(30)

# Returns average of [10, 20, 30]
>>> averager.average()
20

>>> averager.reset()
```

::::
