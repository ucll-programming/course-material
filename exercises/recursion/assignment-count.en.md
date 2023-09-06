# Count

::::TASK
Write a *recursive* function `count(linked_list, value)` that counts how often `value` occurs in `linked_list`.
::::

::::HINT{caption="Base Case"}
Whatever the `value`, an empty list contains `0` occurrences of it.
::::

::::HINT{caption="Recursion"}
First count how often `value` occurs in the tail.
Then add one to this result if necessary.
::::
