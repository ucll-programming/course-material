# Empty Seats

You receive an ordered sequence of used seat numbers, for example, `(4, 5, 9, 10, 12, 19)`
You wish to know how many seats are still empty, but you are only interested in empty seats between two used seats.
For the example above, the empty seats are `6`, `7`, `8`, `11`, `13`, `14`, `15`, `16`, `17` and `18`.

:::TASK
Write a function `empty_seats(used_seats)` that returns the number of unused seats.
:::

:::USAGE

```python
>>> empty_seats((1, 2, 3))
0

>>> empty_seats((1, 3))
1

>>> empty_seats((1, 3, 5))
2

>>> empty_seats((1, 10, 12))
9
```

:::
