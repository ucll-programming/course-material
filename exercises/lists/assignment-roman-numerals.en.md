# Roman Numerals

If you're not familiar with Roman numerals, you should read this [Wikipedia article](https://en.wikipedia.org/wiki/Roman_numerals) first.

Roman numerals are not defined unambiguously.
The rules we follow here are:

* We use subtractive notation, meaning we represent 4 as IV, not as IIII.
* Not every subtraction is allowed.
  We only use IV (4), IX (9), XL (40), XC (90), CD (400) and CM (900).
  For example, representing 999 with IM is not allowed: I can only be subtracted from V and X.

As a quick reminder, here are the different letters in use:

| Letter | Value |
| ------ | ----- |
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

## Converting to Roman Numerals

::::TASK
Define a function `to_roman(n)` which takes that a positive integer `n` and returns the same value in Roman numerals.
::::

::::USAGE

```python
>>> to_roman(1)
'I'

>>> to_roman(2020)
'MMXX'
```

::::

## Converting from Roman Numerals

::::TASK
Define a function `from_roman(string)` which takes a Roman numeral as a string and converts it to an integer.
::::

::::USAGE

```python
>>> from_roman('MCMLXXXIV')
1984
```

::::
