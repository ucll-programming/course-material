# Linked Lists

We have discussed tuples and lists as ways of representing ordered sequences of values.
Internally, these are blocks of contiguous memory: all items are placed one after the other in RAM.

## Insertion in Front

Say we insert a new item at the beginning of a list:

:::code{caption="Python Shell"}

```python
>>> ns = [1, 2, 3]
>>> ns.insert(0, 0)
>>> ns
[0, 1, 2, 3]
```

:::

What happens internally is that all elements have to be shifted one position to the right:

:::code{caption="Python"}

```python
for i in range(len(ns), 0, -1):
    ns[i] = ns[i-1]

ns[0] = 0
```

:::

This can get quite slow if the lists contains many elements.
This is due inherently to the way the lists are represented internally.

## Alternative Representation

We can change how lists are represented internally.
Consider the following code:

:::code{caption="Python"}

```python
class LinkedList:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
```

:::

A `LinkedList` is an object with two fields:

* `head` contains the first element of the list.
* `tail` refers to another linked list containing the remaining elements.

Let's create a linked list that contains the elements `[1, 2, 3]`.

:::code{caption="Python Shell"}

```python
# Represents [3]
>>> lst_3 = LinkedList(3, None)

# Represents [2, 3]
>>> lst_23 = LinkedList(2, lst_3)

# Represents [1, 2, 3]
>>> lst_123 = LinkedList(1, lst_23)

>>> lst.head
1

>>> lst.tail.head
2

>>> lst.tail.tail.had
3
```

:::

A visualization might help:

:::center
![Linked List](image-linked-lists.svg)
:::

A chain of objects representing a list is called a *linked list*.
One of the advantages of linked lists is that insertion in front is very cheap:

:::code{caption="Python"}

```python
# Adding 0 in front
>>> ns = LinkedList(0, ns)
```

:::

As you can see, adding a new item in front is merely a matter of creating a new `LinkedList` object.
No values need to be moved around.

::::INFO
Linked lists are certainly not strictly better than lists: they can be fast where regular lists are slow, but they can also be slow where regular lists are fast.

The reason we introduce them is that they are great to practice recursion on.
::::
