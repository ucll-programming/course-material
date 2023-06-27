# Candy Leftovers

Back to the candy problem.
Like before, we have `candy_count` candies and `child_count` ravenous children and we still need to distribute the candy evenly.
But now we are interested how much candy will be left for us.

Write a function `leftover_candy(candy_count, child_count)` that computes how much candy will be left over after having distributed them evenly over the children.

As always, there are multiple ways to solve this problem.
The purpose of this exercise is to find a solution that involves a single step.

```python
# Children get zero candy, we get 2
>>> leftover_candy(2, 10)
2

# Each child gets 5 pieces of candy, there's 6 left for us
>>> leftover_candy(56, 10)
6
```
