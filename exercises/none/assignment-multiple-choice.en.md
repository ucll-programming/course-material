# Multiple Choice Grading

You have set up a multiple choice test.
The possible answers are numbered 1 to 5.
The grading follows these rules:

* A correct answer adds 1 point to your total.
* An incorrect answer removes 0.2 points from your total.
* A missing answer does not affect your total.

:::TASK
Write a function `multiple_choice(right_answer, given_answer)` that returns how much points the answer is worth.

* `right_answer` represents the expected answer.
* `given_answer` is the answer given by the student.
  If the student left that question unanswered, this parameter will receive `None`.
:::

:::USAGE

```python
# Right answer is worth 1 point
>>> multiple_choice(3, 3)
1

# Wrong answer loses 0.2 points
>>> multiple_choice(2, 5)
-0.2

# No answer leads to 0 points
>>> multiple_choice(4, None)
0
```

:::
