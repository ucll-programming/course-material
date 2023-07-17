import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("xs, item_to_remove, expected", [
    ([], 0, []),
    ([0], 0, []),
    ([1], 0, [1]),
    ([1, 1], 1, []),
    ([1, 1], 0, [1, 1]),
    ([*'abcd'], 'a', [*'bcd']),
    ([*'abcd'], 'b', [*'acd']),
    ([*'abcd'], 'c', [*'abd']),
    ([*'abcd'], 'd', [*'abc']),
    ([1, 2, 3, 2, 1], 2, [1, 3, 1]),
    ([1, 2, 3, 2, 1], 3, [1, 2, 2, 1]),
    ([2, 1, 2, 2, 3, 2, 3, 4, 2, 2, 2, 5], 2, [1, 3, 3, 4, 5]),
])
def test_remove(xs, item_to_remove, expected):
    return_value = student.remove(xs, item_to_remove)

    assert return_value is None, 'remove should return None'
    assert expected == xs
