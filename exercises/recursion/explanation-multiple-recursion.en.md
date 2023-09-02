# Multiple Recursion

Back to our genie story.
When asked to compute
$$
0 + 1 + 2 + \dots + (N-1) + N
$$
it took off the last value and asked another genie to calculate
$$
0 + 1 + 2 + \dots + (N-1)
$$
and then added the final $N$ itself.
Written in code, this givesn

:::code{caption="Python"}

```python
def sum_up_to(n):
    if n == 0:
        return 0
    else:
        return sum_up_to(n - 1) + n
```

:::

Nothing prevents the genie from summoning *multiple* helper genies though.
The genie could split the list of numbers in two sublists and assign each to a different genie.
For example, a genie tasked with the sum of 0 to 100 could divide ask one helper genie to compute the sum from 0 to 50 and another genie the sum from 51 to 100.

```python
def sum_range(a, b):
    if a == b:
        return a
    else:
        middle = (a + b) // 2
        left_sum = sum_range(a, middle)
        right_sum = sum_range(middle + 1, b)
        return left_sum + right_sum
```

When a genie calls upon two or more helpers, this is called *multiple recursion*.

::::INFO
Note that this alternative way of computing the sum is not faster!
While the two assistant genies might do the work in parallel and therefore producing results much quicker, in Python, the two recursive calls are done one after the other.

It is possible though to have the two recursive calls perform their work in parallel, granting us a performance boost, but this is not the default.
This topic is too advanced to delve into during this course.
::::
