from collections import namedtuple


def sum_range(a, b):
    if a == b:
        return a
    elif a > b:
        return sum_range(b, a)
    else:
        return sum_range(a, b - 1) + b


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


class LinkedList:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail


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


def contains(linked_list, item):
    if linked_list is None:
        return False
    else:
        return linked_list.value == item or contains(linked_list.next, item)


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


def tilings(width):
    if width <= 1:
        return 1
    else:
        return tilings(width - 1) + tilings(width - 2)


def coupon(menu, value):
    if value == 0:
        return []
    if value < 0:
        return None
    if len(menu) == 0:
        return None
    for price in menu:
        if (r := coupon(menu, value - price)) is not None:
            return [price, *r]
    return None
