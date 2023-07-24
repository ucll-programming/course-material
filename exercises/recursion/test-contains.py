import pytest
import student
from testlib import *


@pytest.mark.timeout(1)
@pytest.mark.parametrize("linked_list, value, expected", [
    (list_to_linked_list(xs), value, value in xs)
    for xs in [
        [],
        [1],
        [1, 2, 3],
        [*"sdfgh"],
        [5, 2, 3, 1, 3],
    ]
    for value in [1, 2, 3, 5, 's', 'f', 'h']
])
def test_contains(linked_list, value, expected):
    actual = student.contains(linked_list, value)
    assert expected == actual
