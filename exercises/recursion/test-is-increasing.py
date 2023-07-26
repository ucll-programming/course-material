import pytest
import student
from testlib import *


@pytest.mark.timeout(1)
@pytest.mark.parametrize("ns, expected", [
    (list_to_linked_list([]), True),
    (list_to_linked_list([1]), True),
    (list_to_linked_list([1, 1]), True),
    (list_to_linked_list([1, 2]), True),
    (list_to_linked_list([1, 2, 3]), True),
    (list_to_linked_list([4, 1]), False),
    (list_to_linked_list([1, 3, 5, 4]), False),
    (list_to_linked_list([1, 2, 3, 4, 5]), True),
    (list_to_linked_list([1, 0, 2, 3, 4, 5]), False),
    (list_to_linked_list([1, 2, 0, 3, 4, 5]), False),
    (list_to_linked_list([1, 2, 3, 1, 4, 5]), False),
    (list_to_linked_list([1, 2, 3, 4, 3, 5]), False),
])
def test_is_increasing(ns, expected):
    actual = student.is_increasing(ns)
    assert expected == actual