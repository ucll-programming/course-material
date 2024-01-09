# Removing Runs

We define a *run* as a contiguous series of equal elements.
For example, `[1, 2, 2, 2, 4, 7, 9, 9, 9, 9]` contains two runs: one containing `2`s, the other `9`'s.

We want you to get rid of such runs by deleting the repeated elements.
In case of the example above, we want to get `[1, 2, 4, 7, 9]`.

:::TASK
Write a function `remove_runs(ns)` that returns a new list equal to `ns` but with runs removed.
:::
