# Debugging

Examine the code below.

:::code{caption="Python"}

```python
# A book has a title and a rating
class Book:
    def __init__(self, title, rating):
        if not 1 <= rating <= 5:
            raise ValueError('Rating must be integer between 1 and 5')
        self.title = title
        self.rating = rating


def group_by_rating(books):
    # Create a list containing 5 empty lists
    groups = [ [] ] * 5

    # Put every book in the correct list based on its rating
    for book in books:
        groups[book.rating].append(book.title)

    return groups
```

:::

Say we use this code as follows:

:::code{caption="Python Shell"}

```python
>>> book1 = Book('House of Leaves', 5)
>>> book2 = Book('The Hunger Games', 3)
>>> book3 = Book('The Room', 5)
>>> book4 = Book('Fifty Shades of Grey', 1)

>>> books = [book1, book2, book3, book4]
>>> group_by_rating(books)
# Expected output
[
    ['Fifty Shades of Grey'],
    [],
    ['The Hunger Games'],
    [],
    ['House of Leaves', 'The Room']
]
```

:::

::::TASK

Copy all code above (class definition, `group_by_rating` and the test code) to a file `books.py`.
Make sure `group_by_rating`'s output is actually `print`ed out to the screen.
Run the code from the shell:

:::code{caption="Shell"}

```bash
$ py books.py
```

:::

::::

You will be greeted by an `IndexError`.
Think for a moment what could be the cause.
You might spot the mistake quickly, or it might not be so obvious.

While it is possible to keep staring at the code looking for the bug, this is often an inefficient use of your time (especially during exams).
A better approach exists: a tool, known as a *debugger*_*, allows you to execute code step by step.
This allows you to see how the variables' values change as the program is running, making it much easier to identify the bug(s).
