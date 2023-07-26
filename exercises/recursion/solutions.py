from collections import namedtuple


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
