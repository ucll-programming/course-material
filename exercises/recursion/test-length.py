import pytest
import student
from testlib import *


@pytest.mark.timeout(1)
@pytest.mark.parametrize("linked_list, expected", [
    (list_to_linked_list(xs), len(xs))
    for xs in [
        [],
        [1],
        ['a'],
        [1, 2],
        [1, 2, 3, 4, 5]
    ]
])
def test_length(linked_list, expected):
    actual = student.length(linked_list)
    assert expected == actual
