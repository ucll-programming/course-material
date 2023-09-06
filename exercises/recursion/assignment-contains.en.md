# Contains

::::TASK
Write a *recursive* function `contains(linked_list, item)` that checks whether `item` is a member of the `linked_list`.
::::

::::HINT{caption="Hint: General Approach"}
Some value `x` is a member of a list if

* `x` is equal to the first item in the list.
* `x` is somewhere in the rest of the list.
::::

::::HINT{caption="Hint: Base Case"}
Given an empty linked list, we know for sure it cannot contain `item`.
::::

::::HINT{caption="Hint: Recursion"}
First, check if the head of `linked_list` is equal to `item`.
If so, you know that `linked_list` contains `item`.

Otherwise, have "someone else" check if `item` appears in the tail of the list.
::::
