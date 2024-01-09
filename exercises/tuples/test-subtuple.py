import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("xs, ys, expected", [
    ((), (), True),
    ((1, 2, 3), (), True),
    ((1, 2, 3), (1,), True),
    ((1, 2, 3), (2,), True),
    ((1, 2, 3), (3,), True),
    ((1, 2, 3), (1, 2), True),
    ((1, 2, 3), (2, 3), True),
    ((1, 2, 3), (1, 2, 3), True),
    ((1, 2, 3), (1, 3), False),
    ((), (1,), False),
    (('a', 'b', 'c', 'd', 'e'), ('b', 'c', 'd'), True),
    (('a', 'b', 'c', 'd', 'e'), ('c', 'd', 'e'), True),
])
def test_subtuple(xs, ys, expected):
    actual = student.subtuple(xs, ys)
    assert expected == actual, f'subtuple({xs!r}, {ys!r}) should return {expected}'
