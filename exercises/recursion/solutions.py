from collections import namedtuple


def sum_range(a, b):
    if a == b:
        return a
    elif a > b:
        return sum_range(b, a)
    else:
        return sum_range(a, b - 1) + b


LinkedList = namedtuple('LinkedList', ['value', 'next'])


def length(linked_list):
    if linked_list is None:
        return 0
    else:
        return 1 + length(linked_list.next)


def to_linked_list(xs):
    if len(xs) == 0:
        return None
    else:
        return LinkedList(xs[0], to_linked_list(xs[1:]))


def contains(linked_list, value):
    if linked_list is None:
        return False
    else:
        return linked_list.value == value or contains(linked_list.next, value)


def append(linked_list, value):
    if linked_list is None:
        return LinkedList(value, None)
    else:
        return LinkedList(linked_list.value, append(linked_list.next, value))


def count(linked_list, value):
    if linked_list is None:
        return 0
    else:
        if linked_list.value == value:
            extra = 1
        else:
            extra = 0
        return extra + count(linked_list.next, value)


def is_increasing(linked_list):
    if linked_list is not None and linked_list.next is not None:
        return linked_list.value <= linked_list.next.value and is_increasing(linked_list.next)
    else:
        return True


def quicksort(ns):
    if len(ns) <= 1:
        return ns
    else:
        pivot, *rest = ns
        left = [n for n in rest if n <= pivot]
        right = [n for n in rest if n > pivot]
        sorted_left = quicksort(left)
        sorted_right = quicksort(right)
        return [*sorted_left, pivot, *sorted_right]
