# Parameters

Functions are everywhere:

* Google is in essence a function that returns a list of web pages.
* A satnav is a function that returns the shortest path to a certain destination.
* An chess AI is a function that returns the best move.
* And so on.

As of yet, we've been focusing on the *output* of functions, i.e., on their return value.
Functions often also require *inputs*:

* Google needs a series of keywords.
* A satnav needs starting location and a destination.
* A chess AI needs the current state of the chess board and who it's playing as.

A function takes inputs in the form of *parameters*.
This is what it looks like in Python form:

:::code{caption="Python"}

```python
def function_name(parameter1, parameter2, ...):
    instruction1
    instruction2
    ...
    return return_value
```

:::

If we were to translate our examples above into Python functions, we'd get

:::code{caption="Python"}

```python
def google_search(keyword_list):
    ...
    return pages


def satnav(departure, arrival):
    ...
    return shortest_path


def chess_ai(chessboard, ai_color):
    ...
    return best_move
```

:::
