# Split Name

We are given a string containing a first name and a last name, separated by a space.
We now wish to have the first and last name as separate strings.

::::TASK
Write a function `split_name(full_name)` that extracts the first and last name from `full_name` and returns them as a tuple.
::::

::::USAGE

```python
>>> split_name("Walter White")
("Walter", "White")
```

::::

::::HINT
Start by looking for the space in the string.
Once you know where it is located, use slicing to extract the first and last name.
::::
