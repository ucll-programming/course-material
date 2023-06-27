# Internet Costs

Back in the not-so-good old days, you had to use your phone line to connect to the Internet.
Per initiated block of 6 minutes, you were billed a certain amount.
For example, if you were connected for just one second, you still had to pay for the full block of 6 minutes.

Write a function `internet_costs(duration_in_seconds, cost_per_block)` that computes the cost of an internet session that lasts `duration_in_seconds` seconds.

```python
# Zero seconds is free
>>> internet_costs(0, 0.15)
0

# One second gets counted as a full block
>>> internet_costs(1, 0.15)
0.15

# Exactly one block
>>> internet_costs(360, 0.5)
0.5

# 361 seconds = 1 block + 1 second. We get billed for 2 full blocks.
>>> internet_costs(361, 0.5)
1.0
```
