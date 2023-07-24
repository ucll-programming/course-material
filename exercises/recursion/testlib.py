from collections import namedtuple


LinkedList = namedtuple('LinkedList', ['value', 'next'])


def list_to_linked_list(ns):
    result = None
    for n in reversed(ns):
        result = LinkedList(n, result)
    return result
