# Next Player Renumbered

Some people complained that numbering players starting at zero is weird.
Okay then, let's number `n` players starting by one.
In other words, the players are numbered `1`, `2`, `3`, ..., `n`.

Write a function `next_player2(player, player_count)` that returns who comes after player `player` taking into account the new numbering system.

```python
# Simple case
>>> next_player2(4, 10)
5

# After player 10, it's back to player 1
>>> next_player2(10, 10)
1
```
