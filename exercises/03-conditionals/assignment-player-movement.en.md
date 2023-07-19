# Player Movement

We're making a game and are dealing with user input.
The player has a certain position on the screen, let's call it `position`.

* Pressing the left arrow key will cause the player to move left, i.e., `position` decreases by `1`.
* Conversely, pressing the right key will cause a right player movement, incrementing `position` by 1.
* The player can also run by holding shift, in which case the amount `position` is increased/decreased is doubled.

::::TASK
Write a function `player_movement(position, left_arrow_pressed, right_arrow_pressed, shift_pressed)` that returns the updated `position` value.

`left_arrow_pressed`, `right_arrow_pressed` and `shift_pressed` are `True` when the corresponding key is pressed, `False` otherwise.
::::

::::USAGE

```python
# Player moves left
>>> player_movement(10, True, False, False)
9

# Player runs left
>>> player_movement(10, True, False, True)
8

# Player doesn't move
>>> player_movement(10, False, False, True)
10

# Player has both left and right arrow keys pressed, nothing happens
>>> player_movement(10, True, True, False)
10
```

::::
