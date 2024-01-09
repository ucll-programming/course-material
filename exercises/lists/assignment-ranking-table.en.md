# Ranking Table

You receive the results of [speedcubing](https://en.wikipedia.org/wiki/Speedcubing) competitions as a sorted list of pairs, for example:

```python
[
    ('Max Park', 3.13),
    ('Yusheng Du', 3.47),
    ('Tymon Kolasiński', 3.85),
    ('Jode Brewster', 3.88),
    ('Asher Kim-Magierek', 3.89),
    ('Yiheng Wang', 3.90),
    ('Luke Garrett', 3.95),
    ('Max Siauw', 4.03),
    ('Ruihang Xu', 4.06),
    ('Sean Patrick Villanueva', 4.11)
]
```

We wish to see this nicely formatted:

```text
 1 Max Park                3.13
 2 Yusheng Du              3.47
 3 Tymon Kolasiński        3.85
 4 Jode Brewster           3.88
 5 Asher Kim-Magierek      3.89
 6 Yiheng Wang             3.90
 7 Luke Garrett            3.95
 8 Max Siauw               4.03
 9 Ruihang Xu              4.06
10 Sean Patrick Villanueva 4.11
```

Note the following details:

* We distinguish three columns: the rank, the name and the timing.
* Each column is as just wide enough to accommodate its longest item.
* The columns are separated by one space.
* The ranks are aligned to the right.
* The names and timings are aligned to the left.
* The timings show two decimals.
  For example, 3.9 is shown as `3.90`.

:::TASK
Write a function `ranking_table(ranking)` that returns a string containing the table as described above.
:::

:::HINT
Some helpful functionality:

* `string.ljust(n)` to left align text.
* `string.rjust(n)` to right align text.
* [Format specifiers for interpolated strings](https://docs.python.org/3/library/string.html#format-specification-mini-language) allow you to format the timings.
:::
