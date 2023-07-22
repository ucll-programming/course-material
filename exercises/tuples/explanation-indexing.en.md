# Indexing

When we were discussing strings, we explained how you could determine the string's length using `len` and how to get access to individual characters.
Tuples are very much like strings, except more flexible: a string can only contain characters, whereas a tuple can contain any kind of data.
They also offer very similar functionality.

::::div{.formatted-table}
:::center

| Syntax | Meaning |
| ------- | ------- |
| `len(t)` | Length of the tuple `t` |
| `t[0]` | First item in the tuple `t` |
| `t[-1]` | Last item in the tuple `t` |
| `t[1:4]` | Slicing the tuple |

:::
::::

::::INFO
If you're wondering whether you can modify a tuple, the answer is no.
We'll discuss lists soon, and these are in essence modifiable tuples.
::::
