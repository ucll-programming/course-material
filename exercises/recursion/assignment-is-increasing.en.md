# Is Increasing

::::TASK
Write a *recursive* function `is_increasing(linked_list)` that returns `True` if every element is less than or equal to the next one in the list.

An empty list is considered to be increasing.
::::

::::HINT{caption="General Approach"}
A linked list with items `a, b, c, d, e` is increasing if

* `a <= b`, and
* `b, c, d, e` is increasing.
::::

::::HINT{caption="Hint 1"}
You need to compare the first and second element.
Therefore, you should first check there exist a first and second element.
::::

::::HINT{caption="Hint 2"}
If `linked_list` is not `None`, there's a first element.
If the tail of `linked_list` is not `None`, there's a second element.
::::

::::HINT{caption="Hint 3"}
Start by checking that the first element is not greater than the second.
If that is the case, you already know the end result and no recursion is required.
Otherwise, let "someone else" check that the tail of the `linked_list` is increasing.
::::
