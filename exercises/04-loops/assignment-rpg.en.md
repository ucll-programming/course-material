# RPG

A typical die has six sides, numbered 1 to 6.
However, other dice also exist: four-sided dice, 10 sided, 20 sided, 100 sided, ...
Regardless of the size, each face has a value ranging between 1 and `N`, where `N` is the number of sides.

We're playing a game that involves two dice with `n_sides` sides.
We roll both dice and in order to win, the sum of the sides must be at least `goal`.
We want to know how probable it is that we win.

In order to compute this probability, we go through all possible values each die can have.
For example, for four-sided dice, we must consider 16 combinations (&#x2680;&#x2680;, &#x2680;&#x2681;, &#x2680;&#x2682;, &#x2680;&#x2683;, &#x2681;&#x2680;, &#x2681;&#x2681;, &#x2681;&#x2682;, &#x2681;&#x2683;, etc.)
For each of these combinations, we count how many of then sums up at least `goal`.
At the end, we divide this count by the total number of combinations.

:::TASK
Write a function `rpg2(n_sides, goal)` that returns the probability that we get at least `goal` using two dice with `n_sides` sides.
:::

:::HINT

* You'll need nested loops (a `for` inside a `for`).
* Each loop will represent one die: each must iterate from `1` to `n_sides`.
* Inside the inner loop, take the sum and use an `if` to check if the sum is greater than `goal`.
* We need to count how many times this is the case: introduce a local variable initialized to `0` for this purpose.

:::

:::TASK
Write a function `rpg3(n_sides, goal)` that returns the probability that we get at least `goal` using **three** dice with `n_sides` sides.
:::
