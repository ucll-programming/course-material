# Mastermind

Mastermind consists in finding a secret code. This code consists of an indefinite number of digits. For this, you are allowed to make multiple guesses. For each guess you get feedback in the form of two numbers :

* The first number indicates how many digits you guessed correctly.
* The second number is the number of digits that appear in the code, but in a different place.

Suppose the code is 1 2 3 4 and you guess 1 5 3 2. The feedback you get on this is 1 2 :

* The first digit 1 is correct and is in the correct position.
* The digits 2 and 3 occur in the code, but in your guess they are in the fourth and third positions, respectively, whereas they belong in the second and third positions.

::::TASK
Write a function `mastermind(code, guess)` that, given two lists of numbers code and guess, returns the feedback as a list of two numbers.
::::

::::USAGE

```python
>>> mastermind([],[])
[0,0]

>>> mastermind([1],[1])
[1,0]

>>> mastermind([1],[2])
[0,0]

>>> mastermind([1,2],[2,1])
[0,2]

>>> mastermind([1,2],[1,1])
[1,0]

>>> mastermind([1,1,1],[1,1,2])
[2,0]

>>> mastermind([1,2,3,4],[1,3,2,4])
[2,2]
```

::::


