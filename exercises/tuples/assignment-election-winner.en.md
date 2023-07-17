# An Election's Winner

An election is held and it's your job to determine who the winner is.
You get a sequence of votes.
Find out which vote occurs most often.

:::TASK
Write a function `election_winner(votes)` that returns the most common element of `votes`.

* If there's a tie between winners, you are free to return any winner.
* If no votes have been cast, return `None`.
* Try to make it as efficient as possible with the knowledge you currently have.
  We'll revisit this exercise later when you have tools to make it optimally efficient.
:::

:::USAGE

```python
# Two votes for Kang, only one for Kodos. Kang wins.
>>> election_winner(('Kang', 'Kodos', 'Kang'))
'Kang'
```

:::

:::HINT
Sorting the lists brings equal votes together.
It then becomes a matter of finding the longest run.
:::
