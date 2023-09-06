# Introduction

A computer is great to perform computations: if you tell it what to do, it can perform billions of instructions each second.
However, each of these instructions is deterministic: given the same inputs, they produce the same outputs.
This is in most cases a very desirable trait, but what to do if we need randomness?

We distinguish between two kinds of random number generators (RNGs).

* [True random number generators](https://en.wikipedia.org/wiki/Hardware_random_number_generator): these produce numbers that are impossible to predict.
  Such an RNG typically requires external inputs from which it draws randomness, such as the timing of certain hardware events (keyboard presses, mouse movements, &hellip;), temperature fluctuations, etc.
* [Pseudo random number generators](https://en.wikipedia.org/wiki/Pseudorandomness) (PRNGs) produce seemingly random numbers, but these are actually the result of deterministic computations.

Whenever you deal with cryptography, it is crucial that you rely on a true RNG.
A PRNG is hopelessly insecure.

## PRNGs

Python comes with the [`random` module](https://python.readthedocs.io/en/stable/library/random.html): it contains a number of functions that produce pseudorandom values.

:::code{caption="Python Shell"}

```python
>>> import random

# Generates a number between 1 and 5 (inclusive)
>>> random.randint(1, 5)
2

# Randomly picks one of the list's elements
>>> random.choice(['a', 'b', 'c'])
'c'

# Shuffles the list
>>> lst = [1, 2, 3, 4, 5]
>>> random.shuffle(lst)
>>> lst
[2, 4, 3, 5, 1]
```

:::

You can also *seed* the PRNG as follows:

:::code{caption="Python Shell"}

```python
>>> random.seed(15681)
>>> for _ in range(10):
...     print(random.randint(1, 6))
5
6
3
2
5
2
3
2
2
1

>>> random.seed(15681)
>>> for _ in range(10):
...     print(random.randint(1, 6))
5
6
3
2
5
2
3
2
2
1
```

:::

Notice how the same numbers are generated.
A seed determines which numbers the PRNG will generate.
Reuse the same seed and the PRNG will generate the exact same numbers.

## Advantages of PRNGs

You might wonder why PRNGs even exist.
Why not use true random number generators all the time?
Well, PRNGs have to major advantages:

* A PRNG is far more efficient.
* A PRNG allows you to "reset" it so that it produces the same random numbers again.

The repeatability is often used in games: consider a game where outcomes depends on chance.
For example, there's an 80% chance for you to hit your target.
Say you save your game just before taking a shot, and you miss, you can reload your game and try again, hoping that you'll hit the target this time.
To counter this, games can save the PRNGs internal state alongside other game data.
This guarantees that the reloading will still lead to the same outcomes, as the PRNG will be put back in the exact same state as it was during your first assassination attempt.
(Of course, you can work around this by performing actions in a different order. That's what I do anyway.)

Another advantage of the repeatability is how it simplifies debugging: if your code involves random numbers and the bug only occurs in specific circumstances, you do not want to wait around until those exact same circumstances take place again.
Instead, you'll want to setup the PRNG so that it produces the same numbers every time, allowing you to examine what went wrong.
