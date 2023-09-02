# Introduction

Being able to repeat certain instructions a specified number of times (i.e., iteration) is an important building block in programs.
We've discussed how we can achieve iteration in Python, namely with loops.
In this chapter, we'll see another approach: recursion.

## Recursive Functions

Let's start with a definition: a *recursive* function is a function that calls itself.
The simplest recursive function is

:::code{caption="Python"}

```python
def recursive_function():
    recursive_function()
```

:::

This function doesn't do any useful, however.
Calling it would lead to *infinite recursion*: execution would get stuck calling the same function over and over again.

A more useful recursive function would be

:::code{caption="Python"}

```python
def another_recursive_function(n):
    if n == 0:
        return 0
    else:
        return n + another_recursive_function(n - 1)
```

:::

Feel free to examine this code and try to find out what `another_recursive_function(5)` would evaluate to.
It's okay if you draw a blank: recursion is not the most intuitive concept for beginning programmers.
To help you understand how recursion works, we'll tell you how you can imagine recursion works in the real world.

## Ricky and Mort (we don't want to get sued)

::::INFO
Any resemblance to [episode 5 of season 1](https://www.imdb.com/title/tt3333832/?ref_=ttep_ep5) of a certain show is purely coincidental.
::::

Imagine you have a magic box with a button on it.
Whenever you press the button, a blueish genie appears, ready to do your bidding.
You can give it one task, which it will do its very best to accomplish, after which it disappears again.
For example, we could ask the genie to compute the sum of the numbers up to 5, and it would answer 15 and vanish.

In Python, the equivalent would be calling a function.
Calling a function can be seen as invoking the genie, asking it to perform the instructions inside the function, and returning the result.

Now it turns out the genie is quite lazy and would rather do a minimal amount of work.
The genie can also press the magic box's button and make a *second* genie appear, which it can give orders to.
This second genie is an exact clone of the first, so it will act in exactly the same way.

Let's imagine that upon being asked to compute the sum of 0 to 5, the genie is so lazy that it goes straight to the box and asks the second genie the same question.
Since the second genie behaves in exactly the same way, it too will press the button, summoning a third genie, who in turns will summon a fourth one, and so on.
Ultimately, we would end up with an infinite amount of genies, but no answer.

The genie may be lazy, but it also takes pride in being able to actually finish the task at hand.
It will need to take the necessary precautions to prevent a pointless unending outbreak of genies to take place.
The genie will therefore perform a minimal amount of work and then delegate the rest of the work to another genie.

So this is what our genie will do:

* It knows it has to compute the sum 0 + 1 + 2 + 3 + 4 + 5.
* It calls upon another genie and tasks it with computing the sum 0 + 1 + 2 + 3 + 4.
* The second genie computes this sum.
  The first genie does not care about how this is done, it only cares about the result.
  Once the second genie has finished the calculation, it tells the original genie that 0 + 1 + 2 + 3 + 4 equals 10 and vanishes.
* The first genie now knows that 0 + 1 + 2 + 3 + 4 equals 10. It only has to add an extra 5 to this result which gives 15.
  It proudly tells us that 0 + 1 + 2 + 3 + 4 + 5 equals 15 and promptly disappears.

We can now wonder how the second genie performed its job of computing 0 + 1 + 2 + 3 + 4.
Simple: it uses the exact same tactic as the first genie:

* The second genie has to compute 0 + 1 + 2 + 3 + 4.
* It summons a third genie and tells it to compute 0 + 1 + 2 + 3.
  It gets 6 as answer.
* The second genie adds 4 to this result, giving 10.
  It tells the first genie that 0 + 1 + 2 + 3 + 4 equals 10.
  Having fulfilled its task, it goes poof.

The important thing to understand here is that every genie delegates a slightly simpler version of the task to another genie.
If a genie has to compute

$$
0 + 1 + 2 + \dots + (N - 1) + N
$$

it will have another compute

$$
0 + 1 + 2 + \dots + (N - 1)
$$

and add the final $N$ itself.

Written in Python, we can write this as

:::code{caption="Python"}

```python
def sum_up_to(n):
    return sum_up_to(n - 1) + n
```

:::

However, this will not work as is: this code states that every genie summons another genie, leading to infinite recursion.
We need a way to prevent this from happening.

A genie, if it realizes it doesn't really have much work to do, will agree to do the entirety of the job itself.
Let's make an overview of the genies involved in computing 0 + 1 + 2 + 3 + 4 + 5.

::::div{.formatted-table}
:::center

| Genie | Task |
| -----: | ---- |
| First   | 0 + 1 + 2 + 3 + 4 + 5 |
| Second  | 0 + 1 + 2 + 3 + 4 |
| Third   | 0 + 1 + 2 + 3 |
| Fourth  | 0 + 1 + 2 |
| Fifth   | 0 + 1 |
| Sixth   | 0 |

:::
::::

The genie chain should end at the sixth: computing 0 is trivial, i.e., it's simply 0.
We update our Python function to mirror this:

:::code{caption="Python"}

```python
def sum_up_to(n):
    if n == 0:
        return 0
    else:
        return sum_up_to(n - 1) + n
```

:::

## Conclusion

In order to better understand recursion, view a function call as the summoning of a worker that performs a task.
A recursive function is then nothing more than a worker that summons an assistant worker to perform part of the work.

There always has to be a special case (typically called the *base case*) where no recursion is done.
A lack of base case will lead to infinite recursion.

A recursive function often has the form

:::code{caption="Python"}

```python
def recursive_function(inputs):
    if is base case:
        return simple answer
    else:
        subresult = recursive_function(smaller inputs)
        return upgraded subresult
```

:::
