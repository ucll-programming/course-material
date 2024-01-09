# Date Checking

For this exercise, you'll write a series of date-related functions.
You can run the tests after each separate task.

Here's a few tidbits of information you might need to solve the exercises.

:::div{.centered.horizontal-table.inner-borders}

| | | | | | | | | | | | | |
| -: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Month | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| Day count | 31 | 28/29 | 31 | 30 | 31 | 30 | 31 | 31 | 30 | 31 | 30 | 31 |

:::

A year is a leap year if it is divisible by 4.
However, if the year is divisible by 100, it is *not* a leap year, except if it is divisible by 400, then it *is* a leap year.
(Hey, we didn't make up these rules ourselves.)

::::IMPORTANT
This exercise involves writing more than one function.
All tests are grouped in a single file named `test-dates.py`.
::::

:::TASK
Write a function `is_valid_month(month)` that checks if `month` is valid, i.e., is a number between `1` and `12`.
:::

:::TASK
Write a function `is_leap_year(year)` that returns `True` if `year` is a leap year and `False` if it is not.
:::

:::TASK
Write a function `has_30_days(month)` that returns `True` if the given month (`1` = January, `2` = February, etc.) counts 30 days in total, `False` otherwise.

Note: `has_30_days(month)` should return `False` of months with more than `30` days.
:::

:::TASK
Write a function `has_31_days(month)` that returns `True` if the given month counts 31 days in total, `False` otherwise.
:::

:::TASK
Write a function `has_28_days(month, year)` that returns `True` if the given month counts 28 days in total, `False` otherwise.

Note the extra parameter: `year` is needed because the result will depend on whether it's a leap year.
:::

:::TASK
Write a function `has_29_days(month, year)` that returns `True` if the given month counts 28 days in total, `False` otherwise.
:::

## `is_valid_date`

Now comes the tricky part.
We want to know if a given date is valid or not.
In order to implement this, you will have to rely on all the functions you defined above.

:::TASK
Write a function `is_valid_date(day, month, year)` that checks returns `True` if the given date is valid, `False` otherwise.
:::

:::HINT
The solution will be a relatively long expression, but it should exhibit a very clean structure.

The `year` is always valid, so that leaves us with the `month` and the `day` to be checked.
Checking the `month` should be trivial: we already have a function for that.
The `day` is more complex, so here's some help.
The day is valid if...

* The `month` has 31 days **and** the `day` is between `1` and `31`,
* **or**, the `month` has 30 days **and** the `day` is between `1` and `30`,
* **or**, ...

You should rely on parentheses to ensure the subexpressions are grouped together correctly.
For example, don't write `a and b or c and d`, but write `(a and b) or (c and d)`.
:::
