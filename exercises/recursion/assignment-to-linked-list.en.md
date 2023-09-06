# Conversion to Linked List

::::TASK
Write a *recursive* function `to_linked_list(xs)` that given a regular Python lists returns a linked list containing the same elements in the same order.
::::

::::USAGE

```python
>>> to_linked_list([])
None

>>> to_linked_list([1, 2])
LinkedList(head=1, tail=LinkedList(head=2, tail=None))
```

::::
