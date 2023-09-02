# Quicksort

There are many algorithms to sort a list.
Here, we will explain [Quicksort](https://en.wikipedia.org/wiki/Quicksort), an efficient sorting algorithm.
There are more efficient ones such as [Timsort](https://en.wikipedia.org/wiki/Timsort), but they are much more complicated.

Quicksort operates as follows:

* Take a random element from the list, for example, the first.
  Let's call this element `pivot` and all remaining elements `rest`.
* Divide `rest` in two sublists:
  * All elements from `rest` that are `<= pivot`; let's call this list `left`.
  * All elements from `rest` that are `> pivot`; let's call this `right`.
* Sort these two sublists recursively, yielding `sorted_left` and `sorted_right`.
* Now you have a sorted list of items `<= pivot`, a sorted lists of items `> pivot`, and a pivot.
  Put them back together to construct a single sorted list.

::::EXAMPLE
We apply the algorithm on `ns = [5, 7, 5, 4, 3, 8, 7]`.

* We pick `5` as `pivot` (can be any element, but the first one is easiest.)
  The remaining elements `rest` is now `[7, 5, 4, 3, 8, 7]`.
* Selecting the items `<= pivots` gives us `left = [5, 4, 3]`.
* Selecting the items `> pivots` gives us `right = [7, 8, 7]`.
* We sort both these lists recursively.
  We can assume this "magically" works.
  We get `sorted_left = [3, 4, 5]` and `sorted_right = [7, 8, 8]`.
* Putting everything back together gives us `[3, 4, 5, 5, 7, 8, 8]`.
::::

::::TASK
Write a *recursive* function `quicksort(ns)` that sorts `ns`.
Do not modify `ns` in any way, instead return the sorted version as a new list.

Don't forget about the base case.
Which lists are trivially sorted?
::::
