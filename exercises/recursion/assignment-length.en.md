# Length of Linked Lists

You area given the following definition of `LinkedList`:

:::code{caption="Python"}

```python
class LinkedList:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
```

:::

::::TASK
Write a *recursive* function `length(lst)` that returns the length of a linked list.
::::

::::USAGE

```python
>>> lst = LinkedList(1, LinkedList(2, LinkedList(3, None)))
>>> length(lst)
3
```

::::HINT
The length of a list equals 1 plus the length of its tail.
::::
