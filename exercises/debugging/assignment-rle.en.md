# RLE

[Run Length Encoding](https://en.wikipedia.org/wiki/Run-length_encoding) (RLE) is a simple way to compress data.
The compression algorithm assumes that the data contains long runs of the same character, e.g., `"aaaaaaaabbbbbccc"`.
If a character, say `x`, appears 5 times in a row, taking up 5 bytes, we can just store it as `"5x"`.
The example above would thus become `"8a5b3c"`.

There's a snag, however.
Consider the data `"555555555577777777777"`, i.e., ten `5`s followed by eleven `7`s.
This would be encoded as `"105117"`.
But how to decode it?

* Maybe it's one `0`, followed by five `1`'s, and one `7`.
* Maybe it's ten `5`s and eleven `7`s.
* Maybe it's 10511 `7`s.

In order to make the encoding unambiguous, we must introduce a strict structure: we will always have exactly one digit (1-9) followed by one character.

::::EXAMPLE
Let's encode `aaaabcccccccccccc` (four `a`s, one `b` and twelve `c`s).
This gets encoded to `4a1b9c3c`.

Note the following details:

* `b` appears only once and thus we must encode it as `1b`, not as `b`.
  In other words, RLE will double the size of the file if there are no runs.
  RLE only causes a reduction in file size if there are enough runs.
* `c` appears twelve times, but we're only allowed to use one digit.
  We therefore split it in two separate runs: `9c3c`. `6c6c`, `4c8c`, etc. would also work.
::::

We provide a buggy implementation below.
In works in two steps:

* First, it identifies the runs.
* Second, it translates these runs to string-form, splitting long (with length > 9) runs into smaller (with length <= 9) runs.

:::code{caption="Python"}

```python
def rle(string):
    groups = []
    i = 0
    while i < len(string):
        j = i + 1
        while j < len(string) and string[i] == string[j]:
            j += 1
        groups.append((string[i], j - i))
    result = ''
    for char, count in groups:
        while count > 0:
            k = max(9, count)
            result += f"{k}{char}"
            count -= k
    return result
```

:::

::::TASK
Fix the given implementation so that the tests work.
::::
