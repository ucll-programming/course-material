from collections import namedtuple


LinkedList = namedtuple('LinkedList', ['value', 'next'])


def list_to_linked_list(xs):
    result = None
    for n in reversed(xs):
        result = LinkedList(n, result)
    return result
