# Deletion

Apart from adding and overwriting key/value pairs, it is also possible to delete them:

:::code{caption="Python"}

```python
del dictionary[key]
```

:::

After this `del` statement, `dictionary` will no longer associate `key` with a value.
If `key` did not appear in `dictionary` at the moment of the `del` operation, you will get an error.
