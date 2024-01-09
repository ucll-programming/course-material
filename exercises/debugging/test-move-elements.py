import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("xs, new_positions, expected", [
    (
        ['a', 'b'],
        [0, 1],
        ['a', 'b'],
    ),
    (
        ['a', 'b'],
        [1, 0],
        ['b', 'a'],
    ),
    (
        ['a', 'b', 'c'],
        [0, 1, 2],
        ['a', 'b', 'c'],
    ),
    (
        ['a', 'b', 'c'],
        [1, 2, 0],
        ['c', 'a', 'b'],
    ),
    (
        ['a', 'b', 'c'],
        [2, 0, 1],
        ['b', 'c', 'a'],
    ),
    (
        ['a', 'b', 'c'],
        [1, 0, 2],
        ['b', 'a', 'c'],
    ),
])
def test_move_elements(xs, new_positions, expected):
    actual = xs[:]
    student.move_elements(actual, new_positions)

    assert expected == actual, f"move_elements({xs!r}, {new_positions!r}) should return {expected!r} but got {actual!r} instead"
