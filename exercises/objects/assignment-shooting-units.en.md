# Unit Damage

We're making a game where units can shoot at each other.
Units are characterized by

* The amount of health left.
* Their armor.
* Their firing power.

A unit A can shoot at another unit B.
The damage done to B depends on A's firepower and B's armor, which absorbs part of the damage.
The formula used is

$$
    \textrm{B's health lost} = \textrm{A's firepower} - \textrm{B's armor}
$$

Of course, being shot can never cause a unit to be healed.

::::TASK
Create a class `Unit`.

* It has three private fields: `health`, `firepower` and `armor`.
* The constructor allows to initialize all three.
  It checks that all three are positive (`>= 0`), otherwise it throws a `ValueError`.
* Readonly properties `health`, `firepower` and `armor` give public access to the unit's information.
* A method `shot_by(other)` computes what happens if `self` is being shot by some other unit `other`.
  This method decreases `self.health` by the correct amount.
  The `health` cannot go below `0`.

As a reminder: exceptions are thrown using

:::code{caption="Python"}

```python
raise ValueError()
```

:::

::::
