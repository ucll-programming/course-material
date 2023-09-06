# Append

::::TASK
Write a *recursive* function `append(linked_list, item)` that returns a new `LinkedList` equal to `linked_list` but with `item` added at the end.
::::

::::HINT{caption="Hint: General Approach"}
Say `linked_list` contains the elements `1, 2, 3, 4` and we need to append `5`.
We ask "someone else" to add `5` to `2, 3, 4` and then add `1` in front.
::::

::::HINT{caption="Hint: Base Case"}
Adding an item to the empty linked list is trivial.
::::

::::HINT{caption="Hint: Recursion"}
First append `value` to the tail of `linked_list`.
Then add `linked_list`'s value in front of the result.
::::
