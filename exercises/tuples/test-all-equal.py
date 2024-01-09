import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("xs, expected", [
    ([], True),
    ([1], True),
    ([1, 1], True),
    ([1, 2], False),
    ([1, 1, 1, 1], True),
    (['a', 'a', 'a'], True),
    ([1, 'a'], False),
    ([1, 1, 1, 1, 2, 1, 1, 1], False),
    ([5, 5, 5, 5, 5, 6], False),
    ([1, 2, 3], False),
])
def test_all_equal(xs, expected):
    actual = student.all_equal(xs)
    assert expected == actual
