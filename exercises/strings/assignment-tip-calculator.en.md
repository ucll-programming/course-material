# Tip Calculator

You're about to make a trip to the US.
Being aware of the tipping culture, you decide to make a little script that helps you determine how much to pay when you go out to eat.

::::TASK
Write a function `tip_calculator()` that behaves as shown below.

:::USAGE

```python
>>> tip_calculator()
Enter total price: 100
Enter tip percentage (default=20): 10
You have to pay 110

>>> tip_calculator()
Enter total price: 200
Enter tip percentage (default=20):
You have to pay 240
```

:::

* Remark how in the second calculation no input was given as tip percentage.
  Empty input should be interpreted as 20%.
* The final amount should be rounded to the closest integer using `round`.
* Make an executable script `tip-calculator.py`.

::::
