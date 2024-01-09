# Removing Backspaces

Internally, letters and symbols are represented by numbers, because numbers is really all a computers knows about.
While any mapping between symbols and numbers will do, it's always nice if people agreed on one specific mapping.
So, in 1991, some brave people set out to define the Unicode standard which defines a number (called a *codepoint*) for every character of any writing system in existence.

::::EXAMPLE
A few examples of codepoints:

::::div{.formatted-table}
:::center

| Codepoint | Character |
| ------- | ------- |
| 65 | A |
| 66 | B |
| 952 | &#952; |
| 995 | &#992; |
| 3091 | &#3091; |
| 129428 | 🦔 |
:::

At the moment of this writing, Unicode supports 149,186 different characters.
::::

It also defines encodings for what some weirder "symbols", such as the bell signal (codepoint 7) and backspace (codepoint 8).
In Python, we can insert a backspace in our strings using `\b`.

For this exercise, you receive a string containing backspace characters.
Your task would be to process them so that they actually remove the preceding character.
For example, `"abc\b"` should be simplified to `"ab"`.

A backspace in the beginning of a string has no effect: `"a\b\b\b"` becomes the empty string.

::::TASK
Write a function `remove_backspaces(string)` that processes all backspaces.
::::

::::USAGE

```python
>>> remove_backspaces("abc")
"abc"

>>> remove_backspaces("abc\b")
"ab"

>>> remove_backspaces("abc\b\b")
"a"

>>> remove_backspaces("abc\b\bxyz")
"axyz"
```

::::
