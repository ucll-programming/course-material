# Types of Division

Python provides two division operators:

* True division, written `/`.
* Floor division (also called integer division), written `//`.

## True Division

True division is the one you're familiar with from mathematics:

```python
>>> 4 / 2
2

>>> 5 / 2
2.5
```

As you can see, the result is an `int` if it can accurately represent the result, which is the case in the first example.
If the result is not a whole number, Python will switch over to `float`s, as shown in the second example.

## Floor Division

When using floor division, you will always end up with a whole number:

```python
>>> 4 // 2
2

>>> 5 // 2
2
```

Whenever the division's "real result" is not a whole number, it is rounded down: in the case of `5 // 2`, the "real" result `2.5` is being rounded down to `2`.

You can interpret `a // b` as the answer to the question "how many times does `b` fit in `a`?".
You'll find that floor division comes in handy more often than you might think.
