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
# The empty list is represented by None and has length 0
>>> length(None)

# List having items 1, 2, 3
>>> lst = LinkedList(1, LinkedList(2, LinkedList(3, None)))
>>> length(lst)
3
```

::::

::::HINT
The length of a list equals 1 plus the length of its tail.
::::

::::QUESTION
Why do you think we have you implement `length` as a function and not as a method part of `LinkedList`?
::::
