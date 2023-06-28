# Thanos

Thanos wants to buy a sandwich at 't Smullerke.
But of course, since it's around noon, there's a long queue.
Hungry as he is, he decides to snap his fingers a few times.
As you know, with every snap, half of the population of the universe disappears, thus halving the queue size with it.

Note that if the queue contains an odd number of people, you have to round down.
For example, a queue of `21` gets snapped to `10`, not `11`.

:::TASK
Write a function `thanos(queue_size, target_size)` that computes how many snaps are necessary to reduce the queue's size from `queue_size` to at most `target_size`.

Thanos, being the reasonable guy that he is, only snaps his fingers the minimal amount required to reduce the queue down to his preferred size.
:::

:::USAGE

```python
# 8 -> 4
>>> thanos(8, 4)
1

# 8 -> 4 -> 2 (leftover queue must be at most 3)
>>> thanos(8, 3)
2

# 100 -> 50 -> 25 -> 12 -> 6
>>> thanos(100, 10)
4
```

:::
