# Monte Carlo Simulations

Let's consider a statistics problem.
In a lottery, we have to pick $k$ numbers out of $N$ possible numbers.
At some later point in time, $k$ winning numbers are drawn.
If these winning numbers coincide with the numbers we picked, we win the jackpot.
We would like to find out how much chance we've got to win the lottery.

While there are statistical formulae that allow us to determine exactly what the odds of winning are, we'd rather use an easier (but less accurate) method: a *Monte Carlo simulation*.
The idea is very simple: we simply simulate the entire playing process many times:

* Randomly pick $k$ random numbers out of $N$.
* Determine $k$ winning numbers at random.
* Check if we've won.

If we perform this a million times, and it turns out we won a 1000 times, we can infer from this that the odds of winning the lottery is 1 in 1000, or 0.1%.
The more often we repeat the simulation, the more accurate our estimate of the winning percentage will be.
