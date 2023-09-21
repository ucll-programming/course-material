# Higher Cards

Playing cards have one of thirteen different values.
We represent each by a number, as shown below:

::::div{.formatted-table}
:::center

| Card Value | Number |
| ---------- | ------ |
| Ace | 1 |
| Two | 2 |
| Three | 3 |
| Four | 4 |
| Five | 5 |
| Six | 6 |
| Seven | 7 |
| Eight | 8 |
| Nine | 9 |
| Ten | 10 |
| Jack | 11 |
| Queen | 12 |
| King | 13 |

:::
::::

The number can be seen as the "value" of a card.
For example, an eight is more valuable than a two, and a king is more valuable than a jack.

The ace is a tricky one: in some games, it is worth little, but in others games, it is the most valuable card.
We happen to be playing a game where the ace is the most valuable card.

:::TASK
Write a function `higher_card(card1, card2)` that returns `True` if `card1` is worth more than `card2`.
:::

:::USAGE

```python
# Five is worth more than two
>>> higher_card(5, 2)
True

# Two is not worth more than five
>>> higher_card(2, 5)
False

# King is worth more than jack
>>> higher_card(13, 11)
True

# Ace is worth more than king
>>> higher_card(1, 13)
True


# We want strictly higher
>>> higher_card(8, 8)
False
```

:::

:::HINT
This exercise is trickier than it might look.
Let's break it down in smaller pieces and then glue them together.

We need to find a boolean expression that expresses that `card1` is worth more than `card2`.
We know that if `card2 == 1` (i.e., an ace) the function can never return `True`.
We can therefore exclude all cases where `card2 == 1`, which gives us

```python
card2 != 1 and ???
```

To determine what `???` needs to be, we can assume `card2 != 1`.
So, given that assumption, when is `card1` the more valuable one?

* When `card1`'s numeric value is higher; *or*
* When `card1` is an ace.
:::
