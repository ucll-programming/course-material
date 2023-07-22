# Identifiers

Functions and parameters need names, otherwise you wouldn't be able to refer to them.
These names are also called *identifiers*.

In this section, we discuss the rules about identifiers.

## Python Rules

Python, like all programming languages, imposes strict rules on what makes a valid identifier.
The [actual rules](https://docs.python.org/3/reference/lexical_analysis.html#identifiers) are a bit complicated;  we give you a simplified summary instead:

* There is no length limit on identifiers.
* An identifier can be any combination of letters (both upper and lowercase), digits and underscores, with the exception that the first character cannot be a digit.
* Identifiers are case sensitive: `abc` and `ABC` are completely unrelated identifiers as far as Python is concerned.

Not following these rules will cause Python to reject your code.

## Conventions

Besides to the Python rules there are also [naming conventions](https://peps.python.org/pep-0008/).
Python will not complain if you do not follow these, but programmers are expected to adhere to them nonetheless.

* Use descriptive names.
* All letters in an identifier should be lowercase.
* If an identifier consists of multiple words, these words should be separated using underscores (`_`).

::::INFO
Note that later we will see more Python concepts such as classes for which there will be a different naming convention.
::::

::::EXAMPLE

::::div{.formatted-table}
:::center

| Identifier | Description |
| ------- | ------- |
| `determine_fee` | Valid |
| `DetermineFee` | Violates naming conventions |
| `Determine-Fee` | Violates Python's syntax rules |

:::
::::

::::