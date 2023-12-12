# Bubblesort

The idea behind Bubble Sort is very simple: we look for consecutive elements that are in the wrong order and swap them around. We repeat this until all the elements are in the correct order.

For example, consider the list [2, 4, 1, 3]:

* The first two elements 2 and 4 are correct.
* The next two elements 4 and 1 are wrong. We swap them, the list is now [2, 1, 4, 3].
* We look at the next pair of consecutive elements, 4 and 3. These too must be swapped, giving rise to 2, 1, 3, 4.
* We start again at the beginning. The first two elements 2 and 1 are wrong → [1, 2, 3, 4].
* We find no more unordered pairs. Sorting is complete.

::::TASK
Write a function `bubblesort(ns)` that applies the above algorithm to the list `ns`. The function should modify the given list ns and return no result.
::::

::::USAGE

```python
>>> bubblesort([])
[]

>>> bubblesort([0])
[0]

>>> bubblesort([0,1])
[0,1]

>>> bubblesort([1,0])
[0,1]

>>> bubblesort([3,2,1])
[1,2,3]

>>> bubblesort([1,11,2])
[1,2,11]
```

::::

