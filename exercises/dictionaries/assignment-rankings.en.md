# Ranking

The [Dodentocht](https://en.wikipedia.org/wiki/Dodentocht) is over.
It was a great success: thousands have participated.
The organization has published a list of participants ordered by time of arrival:

```text
Raymond Garraty
Stebbins
Peter McVries
Arthur Baker
Abraham
Collie Parker
```

Here, Raymond Garraty arrived first, followed by Stebbins, etc.
Given this list, we want to be able to quickly determine the rank of each of the participants: Garraty is ranked first, Stebbins rank second, etc.
However, determining the rank takes time: we have to go through the list looking for a particular name.
We wish to speed this up by creating a `dict` that associates each name with a rank:

:::code{caption="Python"}

```python
rankings = {
    'Raymond Garraty': 1,
    'Stebbins': 2,
    'Peter McVries': 3,
    'Arthur Baker': 4,
    'Abraham': 5,
    'Collie Parker': 6
}
```

:::

This way, we can just write `rankings[participant]` to efficiently determine `participant`'s rank.

:::TASK
Write a function `rankings(participants)` that returns a `dict` as described above.
:::
