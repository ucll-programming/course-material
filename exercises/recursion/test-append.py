import pytest
import student
from testlib import *


@pytest.mark.timeout(1)
@pytest.mark.parametrize("linked_list, value, expected", [
    (list_to_linked_list(xs), x, list_to_linked_list([*xs, x]))
    for xs in [
        [],
        [1],
        [1, 2],
        [5, 4, 3, 2, 1]
    ]
    for x in [1, 'x']
])
def test_append(linked_list, value, expected):
    actual = student.append(linked_list, value)
    assert expected == actual
