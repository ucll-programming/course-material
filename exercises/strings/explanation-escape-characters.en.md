# Escape Characters

Imagine we need add in our code a string in which a `"` appears, for example `he said "hello"`.
Using double quotes will give us trouble:

:::code{caption="Python"}

```python
"he said "hello""
```

:::

Python gets very confused by this: it sees this as two strings `"he said "` and `""`, separated by `hello`, which is grammatically incorrect.
We got one unhappy Python on our hands.

But we hear you ask, why not single quotes then?

:::code{caption="Python"}

```python
'he said "hello"'
```

:::

Indeed, this works perfectly.
But, aha!, what if the string also contains apostrophes?

:::code{caption="Python"}

```python
'Jack's mother said "hello"'
```

:::

This again leads to a very grouchy Python.
Similar issues actually arise quite often.

::::EXAMPLE
HTML relies on tags to assign meaning to text: `<emph>some important text</emph>` emphasizes text.
But what if we want the text itself to contain a `<`?

`x < y` will be flagged down as an error, since it looks like you're starting a tag.
HTML's answer to this problem is to provide `&lt;` as an alternative to `<`.
::::

::::EXAMPLE
This document is written using [Markdown](https://en.wikipedia.org/wiki/Markdown).
Emphasizing text is done using `*emphasized text*`.
However, if we write `5*7 equals 7*5`, this results in "5*7 equals 7*5" instead of "5\*7 equals 7\*5".

In order to prevent the Markdown processor from interpreting the multiplication sign `*` as the start of an emphasized block, we need to *escape the `*` character* which we can do using a backslash: `5\*7 equals 7\*5`.
::::

Python allows you to *escape characters* using the backslash `\` in strings.
For example, `Jack's mother said "hello"` can be written

* `"Jack's mother said \"hello\""`, or
* `'Jack\'s mother said "Hello"'`.

In other word, `\"` and `\'` allow you to insert `"` and `'` characters in strings.

The backslash `\` is called an *escape character* because it changes the meaning of the next character.
`"` means "end of string" whereas `\"` means "a quote character".
There are [more combinations](https://docs.python.org/3/reference/lexical_analysis.html#literals) possible:

::::div{.formatted-table}
:::center

| Combination | Meaning |
| ------- | ------- |
| `\"` | `"` |
| `\'` | `'` |
| `\n` | Newline |
| `\r` | Carriage return |
| `\t` | Tab |
| `\b` | Backspace |
| `\\` | `\` |

:::
::::

## Raw Strings

Escape characters can sometimes be bothersome.
Say you want to add a file path in your code: `"C:\nodejs\training"` would be interpreted by Python as

:::code{caption="Text"}

```text
C:
nodejs    training
```

:::

This is due to `\n` being transformed to a newline and `\t` to a tab.
To prevent this from happening, you have to escape the `\`: `"C:\\nodejs\\training"`.
This quickly becomes bothersome.

Prefixing a string literal with an `r` turns it into a *raw string*.
Escape characters are ignored in such strings: `r"C:\nodejs\training"` works as intended.

::::INFO
Raw strings will come in handy later when you learn about regular expressions.
::::
