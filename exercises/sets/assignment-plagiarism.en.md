# Plagiarism

We have two exam submissions but suspect plagiarism.
Each submission is a string containing possibly multiple lines: for example, `"a\nb\nc"`` contains three lines.
We wish to count how many unique lines they have in common.
If they have the same line in common multiple times, it only contains as one shared line.

::::TASK
Write a function `plagiarism(s1, s2)` that returns the number of unique lines `s1` and `s2` have in common.
::::

::::USAGE

```python
# Line 'a' in common
>>> plagiarism("a", "a")
1

# Three lines each, but nothing in common
>>> plagiarism("a\nb\nc", "x\ny\nz")
0

# Line 'a' is shared, but is only counted once
>>> plagiarism("a\na\na", "a\na")
1

# 'a', 'b' and 'c'
>>> plagiarism("a\nb\nc", "c\nb\na\nx\ny")
3
```

::::
