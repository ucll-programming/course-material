# Pattern Matching

We are given a coded message where each letter has been replaced by a symbol.
For example, the word "example" could be represented by "&#x2299;&#x2663;&#x26C7;&#x22C8;&#x265E;&#x212C;&#x2299;".
However, for compatibility's sake, instead of weird symbols, we'll simply use boring letters.
So, "example" could be represented by "qjairnq".

The rules are simple:

* Every symbol stands for a unique letter.
* No two symbols stand for the same letter.

Our goal is to determine given a code pattern (e.g., "qjairnq") could describe a given word (e.g., "example").

::::TASK
Write a function `matches_pattern(pattern, string)` that returns `True` if `string` matches the given `pattern`, and `False` otherwise.
::::

::::USAGE

```python
# P->C, F->A, R->T works
>>> matches_pattern("PFR", "CAT")
True

# Pattern shorter than word
>>> matches_pattern("PR", "CAT")
False

# X cannot represent both C and T
>>> matches_pattern("XYX", "CAT")
False

# C and D both represent P, which is forbidden
>>> matches_pattern("ABCDE", "HIPPO")
False
```

::::
