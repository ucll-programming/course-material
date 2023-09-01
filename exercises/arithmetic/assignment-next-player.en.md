# Next Player

We're playing a game with `player_count` players.
The players are numbered 0, 1, 2, ..., `n-1`.

The players take turns.
For example, if `n=3`, they play in order 0, 1, 2, 0, 1, 2, 0, 1, 2, etc.

:::TASK
Write a function `next_player(player, player_count)` that computes who should play next.
:::

:::USAGE

```python
# 5 players are involved. After player 1 it's player 2's turn.
>>> next_player(1, 5)
2

# 10 player game. Player 5 follows player 4.
>>> next_player(4, 10)
5

# 10 player game. After player 9 it's back to player 0.
>>> next_player(9, 10)
0
```

:::
