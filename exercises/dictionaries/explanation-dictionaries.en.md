# Dictionaries

Consider the following situations:

* You need to translate a text and would like having a dictionary that, given a word in English gives the corresponding word in Dutch.
  ::::div{.dictionary-table}
  :::center
  | English | Dutch |
  | ------- | ----- |
  | cat | kat |
  | dog | hond |
  :::
  ::::
* You have found a recipe for a delicious chocolate cake.
  It comes with a list of ingredients and the required quantities for each.
  ::::div{.dictionary-table}
  :::center
  | Ingredient | Quantity |
  | ---------- | -------- |
  | chocolate | 250g |
  | eggs | 5 |
  | sugar | 125g |
  | flour | 75g |
  | butter | 175g |
  :::
  ::::
* Given a student number, you wish to know the name of the student associated with that number.
  ::::div{.dictionary-table}
  :::center
  | Student Number | Student Name |
  | -------------- | ------------ |
  | r0123456 | Karen Eiffel |
  | r0654321 | Harold Crick |
  | r0121212 | Ana Pascal |
  | r0954321 | Jules Hilbert |
  :::
  ::::

In each cases, we can represent this data as a table.
Each row associated some data in the left column with some other data in the right column:

* `cat` is associated with `kat`.
* `chocolate` is associated with `250g`.
* `r0123465` is associated with `Karen Eiffel`.

We call the data in the left columns the *keys* and the corresponding data in the right column the *values*.

Python allows us to easily model such data using *dictionaries*, or `dict`s for short.
Here's what the translation dictionary would look like:

:::code{caption="Python"}

```python
translating_dictionary = {'cat': 'kat', 'dog': 'hond'}
```

Dictionaries are not limited to strings: both keys and values can have any type.
For example: `{1: True, 'a': [1, 2, 3]}` is a perfectly valid `dict`.

:::INFO
Actually, there *is* a limitation on the types of keys: the objects have to be *hashable* and comparable using `==`.
We'll delve further into this later.
For now, you can imagine there are no constraints on key types.
:::

* Literals
* Lookup, update
* `len`
* `in`
* `get`, `setdefault`
* `__hash__`, `__eq__`
* `del`
* `.keys()`, `.values()`, `.items()`
