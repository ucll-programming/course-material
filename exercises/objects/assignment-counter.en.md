# Counter

::::TASK
Define a class `Counter`:

* Internally, it keeps track of a count, i.e., an integer.
* The constructor initializes this count to `0`.
* A method `increment()` adds `1` to this count.
* You can retrieve the count using a readonly property named `count`.
* You can reset the count to `0` using a method `reset()`.
::::

::::USAGE

```python
>>> counter = Counter()

# Counter is initially set to 0
>>> counter.count
0

>>> counter.increment()
>>> counter.count
1

>>> counter.increment()
>>> counter.count
2

>>> counter.reset()
>>> counter.count
0
```

::::
