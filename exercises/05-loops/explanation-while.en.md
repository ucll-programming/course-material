# While Loop

Algorithms are built out of three kinds of building blocks.
You've already met two of them:

* Sequencing, i.e., having steps be executed one after the other, in order.
* Selection, i.e., being able to specify whether certain steps should be either executed or skipped based on a condition.
  In Python, selection takes the form of an `if`.

The last building block is *iteration*.
This construct allows us to *repeat* certain steps for as long as we want.

Here's an example:

```python
i = 1

while i < 4:
    print(i)
    i += i

print(f"i is now {i}")
```

Python has multiple ways to perform iteration.
In the code above, we are using a *while loop*.
The *body* of the while loop, which consists of the `print(i)` and `i += 1` statements, is repeated for as long as the condition `i < 5` is true.

Let's go through the code step by step:

* We initialize `i` to `1`.
* We arrive at the `while` loop.
  The condition `i < 4` is evaluated; this yields `True`.
  Because the condition is true, the loop's body gets evaluated.
  * The value of `i` (`1`) is printed.
  * `i` gets incremented by `1` and is now equal to `2`.
* Execution jumps back to the `while` line.
* The condition is re-evaluated: is `i` still less than `4`.
  The answer is yes, which causes the loop body to be executed a second time.
  * The value if `i` (`2`) is printed.
  * `i` gets incremented from `2` to `3`.
* We jump back to the `while` line.
* The condition is, once again, evaluated.
  It is still true, so the loop body gets executed a third time.
  `3` is printed and `i` becomes `4`.
* We jump back to the `while`.
* The condition is re-evaluated.
  This time, however, `i` is not less than `4`.
* Because the condition is not true anymore, the iteration ends, i.e., the loop body won't get executed again.
* We end up at the last `print`, which outputs `"i is now 4"`.
