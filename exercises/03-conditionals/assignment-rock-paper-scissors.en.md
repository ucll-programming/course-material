# Rock Paper Scissors

We want to play a quick game of Rock, Paper, Scissors.
To those who are unfamiliar with the rules: two players simultaneously choose one of three options: rock, paper or scissors.
The outcome is determined by the following rules:

* If both players picked the same option, it's a tie.
* Rock beats scissors.
* Paper beats rock.
* Scissors beat paper.

We need a way to represent the three options.
Let's use numbers (later we'll see there are better ways):

::::div{.formatted-table}
:::center

| Option | Representation |
| ------ | -------------- |
| Rock | 0 |
| Paper | 1 |
| Scissors | 2 |

:::
::::

There are three possible outcomes.
Again, we need a way to represent these:

::::div{.formatted-table}
:::center

| Option | Representation |
| ------ | -------------- |
| Tie | 0 |
| Player 1 wins | 1 |
| Player 2 wins | 2 |

:::
::::

:::TASK
Write a function `rock_paper_scissors(player1_choice, player2_choice)` that returns `0`, `1` or `2`, depending on who won.

Make use of a `if-elif-else` chain.
:::

:::USAGE

```python
# Both players picked rock, so it's a tie
>>> rock_paper_scissors(0, 0)
0

# Paper vs scissors, scissors wins
>>> rock_paper_scissors(1, 2)
2

# Rock vs scissors, rock wins
>>> rock_paper_scissors(0, 2)
1
```

:::
