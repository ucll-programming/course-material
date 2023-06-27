# Cake

We want to bake cake.
Each cake requires 5 eggs.
We want to write a tool that helps us determine how many cakes we can bake given a certain amount of eggs.

Write a function `cake(eggs)` that returns the amount of cakes one can make given `eggs` number of eggs.

```python
# Without any eggs, we can't bake any cakes
>>> cake(0)
0

# One egg short of a cake
>>> cake(4)
0

# Five eggs make one cake
>>> cake(5)
1

# 15 eggs make three cakes
>>> cake(15)

# 16 eggs still make only three cakes
>>> cake(16)
3
```
