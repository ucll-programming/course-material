# Parsing Dates

We have strings representing dates and wish to extract the day, month and year from them as `int` values.

Ideally, we'd implement a single function that returns all three components, but that will have to wait until we see tuples.
Instead, we will implement three functions: `parse_day(string)`, `parse_month(string)`, and `parse_year(string)`.

The strings we wish to parse always have the same exact structure: `dd/mm/yyyy`.
In other words, there's always two digits for the day, two digits for the month and four for the year.

:::TASK
Write the functions

* `parse_day(string)`
* `parse_month(string)`
* `parse_year(string)`
:::

:::USAGE

```python
>>> string = '01/02/2000'
>>> parse_day(string)
1

>>> parse_month(string)
2

>>> parse_year(string)
2000
```

:::
