# Capitalize Words

:::code{caption="Python"}

```python
def capitalize_words(string):
    words = string.split()
    for word in words:
        word.capitalize()
    return " ".join(words)
```

:::

`capitalize_words(string)` should return a new string in which every word in `string` is capitalized.

::::TASK
Fix the given implementation.
::::

::::USAGE

```python
>>> capitalize_words('abc def')
'Abc Def'

>>> capitalize_words('A SENTENCE WITH FIVE WORDS')
"A Sentence With Five Words"
```

::::
