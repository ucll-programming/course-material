---
layout: page
---

- [Headings](#headings)
- [Formatting](#formatting)
- [Ordered Lists](#ordered-lists)
- [Code Blocks](#code-blocks)
- [Table](#table)
- [Links](#links)
- [Images](#images)
- [Extensions](#extensions)
  - [Centering](#centering)
  - [Blocks](#blocks)
  - [Hints](#hints)
  - [Usage Block](#usage-block)
  - [Code Blocks](#code-blocks-1)
- [Official Documentation](#official-documentation)

# Headings

```text
# Heading Level 1
## Heading Level 2
### Heading Level 3
#### Heading Level 4
```

# Formatting

| Syntax | Effect |
| ------: | ------ |
| `*italic*` | *italic* |
| `**bold**` | **bold** |
| `` `code` `` | `code` |
| `~~strikethrough~~` | ~~strikethrough~~ |

# Ordered Lists

```markdown
1. First
   1. Subitem 1
   2. Subitem 2
2. Second
3. Third```

The numbering is unimportant: the compiler will automatically renumber them from 1 to N.

# Unordered Lists

```markdown
* First
  * Subitem 1
  * Subitem 2
* Second
* Third
```

# Code Blocks

````markdown
```python
def example_function():
    print('Hello')
```
````

# Table

```markdown
| Header 1 | Header 2 | Header 3 |
| -------- | -------- | -------- |
| Some text | Some text | Some text |
| Some text | Some text | Some text |
| Some text | Some text | Some text |
```

# Links

```markdown
[Visible text](url)
```

# Images

```markdown
![Alternative text](filename.svg)
```

# Extensions

Markdown is extensible.
Below are extensions developed specifically for the course, so no information online will be found about it.

## Centering

```markdown
:::center
Centered content
:::
```

Code snippet shortcut: `center`.

## Blocks

```markdown
::::WARNING
Contents
::::

::::EXAMPLE
Contents
::::

::::INFO
Contents
::::

::::QUESTION
Contents
::::

::::TASK
Contents
::::

::::IMPORTANT
Contents
::::
```

Each has their own code snippet (e.g., `warning`, `example`, `info`, etc.)

## Hints

```markdown
::::HINT
Content
::::

::::HINT{caption="Hint 1"}
Content
::::
```

Code snippet: `hint` (default header) or `hinth` (custom header).

## Usage Block

```markdown
::::USAGE
Contents
::::
```

Code snippet: `usage`.

## Code Blocks

````markdown
::::code{caption="Python Shell"}

```python
>>> 5
5
```

:::
::::
````

Code snippet: `ccode`.

# Official Documentation

[Official Documentation](https://www.markdownguide.org/basic-syntax/)
