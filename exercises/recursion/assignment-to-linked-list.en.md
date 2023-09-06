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

::::HINT{caption="Hint: General Approach"}
Say `xs = [1, 2, 3, 4]`.
First, let "someone else" convert `[2, 3, 4]`.
Then, add the missing `1` yourself.
::::

::::HINT{caption="Hint: Destructuring"}
You can use `first, *rest = xs` to get the parts of `xs` you need.
Alternatively, you can of course also use slicing: `rest = xs[1:]`.
::::

::::HINT{caption="Hint: Detailed Approach"}
First deal with the base case: if `xs` is empty, return `None`.

If `xs` contains at least one element, name the first element `first` and the remaining elements `rest`.
Perform a recursive call on `rest`.
Then, create an extra `LinkedList` object to add `first` to the linked list.
::::
