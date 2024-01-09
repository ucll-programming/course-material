# Is Prime

:::code{caption="Python"}

```python
def is_prime(n):
    k = 2
    while k * k < n:
        if n % k == 0:
            return False
        k += 1

    return k >= 2
```

:::

The function `is_prime(n)` should check whether `n` is prime or not.
However, the tests fail.

::::TASK
Fix it so that the tests work correctly.
::::
