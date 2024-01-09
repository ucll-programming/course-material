import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("xs, expected", [
    ([], True),
    ([1], True),
    ([1, 2], True),
    ([1, 1], False),
    (['a', 'b', 'c', 'd', 'e'], True),
    (['a', 'b', 1, 'd', 'e'], True),
    (['a', 'b', 1, 'd', 1, 'e'], False),
    (['a', 'b', 1, 'd', 'e', 'a'], False),
    ([1, 2, 3, 4, 5], True),
    ([1, 1, 2, 3, 4, 5], False),
    ([1, 2, 1, 3, 4, 5], False),
    ([1, 2, 3, 1, 4, 5], False),
    ([1, 2, 3, 4, 1, 5], False),
    ([1, 2, 3, 4, 5, 1], False),
    ([1, 2, 3, 4, 5, 2], False),
])
def test_all_different(xs, expected):
    actual = student.all_different(xs)
    assert expected == actual
