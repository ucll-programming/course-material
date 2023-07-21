# Input

`print` allows you to output data to the terminal.
You can also *receive* data using `input`, making it possible to interact with the user.

::::EXAMPLE

:::code{caption="Python"}

```python
name = input("Enter your name: ")
```

:::

::::

::::IMPORTANT
`input` will always return a string.
If the user enters `15`, your program will receive `"15"`.
Soon we will see how to convert this string to an actual integer `15`.
::::
