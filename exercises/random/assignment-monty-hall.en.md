# Monty Hall Problem

The [Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem) is a well known brainteaser with a solution that is apparently so counterintuitive that it has caused many vitriolic discussions online.
The proble goes as follows:

> You're on a game show.
> In front of you are three doors.
> Behind one door there's a car (which you are desperate to win), behind the other two doors are goats.
> You're asked to pick one of the three doors.
> The game host then opens one of the other two doors that has a goat behind it.
> You are now allowed to again pick a door.
> Whatever's behind it, you win.

The question is now: what strategy should you adopt in order to maximize your chances of winning the car?
Does it actually make a difference?

* Either you stick to your original choice.
* Or, you switch to the other unopened door.

Feel free to think about this for a while.
The answer is hidden below.

::::HINT{caption="Answer to the brainteaser"}
You should switch.
Sticking to your original choice gives you 33.3% only chance to win the car, whereas switching gives you 66.6% chance.
::::

Many people, however, refuse to believe this answer.
Let's convince those skeptics with an actual simulation:

* First, randomly pick the door (1 to 3) with the car behind it.
* Next, you simulate your own first choice: randomly pick a door.
  For simplicity's sake, you can actually pretend you always pick door 1, it will make no difference in the outcome.
* Now simulate the host's behavior: he must pick a door with a goat behind it.
* Finally, pretend you've chosen the other door and see if it has the car behind it.
  If so, count it as a win.

Repeat this a large number of times and determine in how many percent of the simulations you've won.

::::TASK
Write a function `monty_hall(simulation_count)` that performs the simulation described above `simulation_count` times and returns the win percentage.
::::
