# Spellcheck

We are given a document that needs to be proofread: every word appearing in this document must appear in the English dictionary.
Luckily, you are given this English dictionary in the form of a (long) list of valid English words.

The document itself is a single string from which you will need to extract the words.
For the sake of simplicity, we left out all punctuation.
You can assume the document is a line containing lines that contain space-separated words.

::::TASK
Write a function `spellcheck(document, valid_words)` that returns a *set* of words from `document` that do not appear in `valid_words`.
The words in this result set must be in lowercase.

* `document` is a string containing lines of space-separated words.
* `valid_words` is a list of (lowercase) strings.
::::

::::USAGE

```python
>>> valid_words = [ 'cat', 'mat', 'sat', 'the' ]
>>> document = """
The cat
sat on
the mat
"""

>>> spellcheck(document, valid_words)
{'on'}
```

::::
