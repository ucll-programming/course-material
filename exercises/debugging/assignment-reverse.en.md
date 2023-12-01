# Reverse

:::code{caption="Python"}

```python
def reverse(lst):
    for i in range(len(lst)):
        j = len(lst) - i - 1
        temp = lst[i]
        lst[i] = lst[j]
        lst[j] = temp
```

:::

This is a buggy implementation of a list-reversing algorithm.
Copy it to `student.py` and fix it so that the tests pass.

::::IMPORTANT
Make minimal changes, i.e., don't just implement it as `xs.reverse()`.
Pretend `lst.reverse()` and `reversed(lst)` don't exist and that the algorithm has to be implemented from scratch.
::::

::::TASK
Fix `reverse` so that the tests pass.
::::
