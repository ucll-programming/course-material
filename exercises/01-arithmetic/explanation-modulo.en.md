# Modulo

The [modulo operator `%`](https://en.wikipedia.org/wiki/Modulo) is probably new to you.
In short, `a % b` computes the *remainder* when you divide `a` by `b`.
We give an example to make the concept clearer.

:::EXAMPLE
An web store shows 20 items per page.
In total, there are 114 items.
How many items are on the last page?

`114 // 20` computes the number of times `20` fits in `114`, i.e., the number of pages that are full.
We need an extra page for the leftover items.
`114 % 20` yields this number: `14`.
:::
