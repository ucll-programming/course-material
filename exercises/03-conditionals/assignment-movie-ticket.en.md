# Movie Ticket

Let's go to the movies!
But let's first see how much the tickets cost&hellip;

The ticket cost depends on multiple factors.
First, the duration determines the base cost.

::::div{.formatted-table}
:::center

| Duration | Base Price |
| -------- | ---------- |
| up to 90  | &euro;10 |
| 90 - 120  | &euro;11 |
| 120 - 150  | &euro;12 |
| longer than 150  | &euro;15 |

:::
::::

Next, if it's the IMAX version, add 20% and round up.

Students get a &euro;3 discount.

::::TASK
Write a function `movie_ticket(duration, imax, student, ticket_count)` that computes the total cost of movie tickets.

* `duration` is an `int`.
* `imax` and `student` are boolean values.
* `ticket_count` is an `int`.
::::

::::USAGE

```python
>>> movie_ticket(70, False, False, 1)
10

>>> movie_ticket(70, False, True, 1)
7

>>> movie_ticket(70, False, True, 3)
21

>>> movie_ticket(180, True, False, 2)
36
```

::::
