# Dominos

A [domino](https://en.wikipedia.org/wiki/Dominoes) is a rectangular tile divided into two parts, each of which contains a number ranging from 0 to 6.
We represent a domino using a pair, e.g., `(2, 4)`.

We can arrange dominos in a chain, for example, `((2, 4), (4, 3), (3, 0), (0, 0), (0, 5), (5, 4))`.
As you can see, their values on touching ends match: the second value of a domino is equal to the first value of its neighbor on the right.
Your task will be to check if a given series of dominos satisfies this condition.

:::TASK
Write a function `domino_chain(dominos)` that returns `True` if the dominos form a valid chain, `False` otherwise.

A series of zero dominos is considered a valid chain.
:::

:::USAGE

```python
>>> domino_chain(((1, 2), (2, 5), (5, 3), (3, 3), (3, 0)))
True

>>> domino_chain(((4, 1), (2, 5)))
False
```

:::
