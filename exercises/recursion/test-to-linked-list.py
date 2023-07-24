import pytest
import student
from testlib import *


@pytest.mark.timeout(1)
@pytest.mark.parametrize("lst, expected", [
    (
        lst, list_to_linked_list(lst)
    )
    for lst in [
        [],
        [1],
        [5],
        [1, 2, 3, 4, 5],
        ['d', 'c', 'b', 'a']
    ]
])
def test_to_linked_list(lst, expected):
    actual = student.to_linked_list(lst)
    assert expected == actual
