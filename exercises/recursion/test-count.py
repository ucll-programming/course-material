import pytest
import student
from testlib import *


@pytest.mark.timeout(1)
@pytest.mark.parametrize("linked_list, value, expected", [
    (list_to_linked_list(xs), x, xs.count(x))
    for xs in [
        [],
        [1],
        [1, 2, 3],
        [1, 1, 2, 2, 3, 3],
        [1, 2, 3, 1, 2, 3],
        [1, 3, 5, 4, 2],
        [1, 1, 1, 2, 3, 2, 3, 4, 4, 4, 5]
    ]
    for x in [0, 1, 2, 3, 4, 5]
])
def test_count(linked_list, value, expected):
    actual = student.count(linked_list, value)
    assert expected == actual
