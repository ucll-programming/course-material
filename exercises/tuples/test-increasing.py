import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("ns, expected", [
    (
        (),
        True
    ),
    (
        (1,),
        True
    ),
    (
        (1, 2),
        True
    ),
    (
        (1, 1),
        True
    ),
    (
        (1, 3, 4, 9),
        True
    ),
    (
        (1, 3, 2, 4, 9),
        False
    ),
    (
        (1, 3, 4, 4, 9, 9),
        True
    ),
    (
        (1, 3, 4, 4, 9, 9, 8),
        False
    ),
])
def test_increasing(ns, expected):
    actual = student.increasing(ns)
    assert expected == actual, f'increasing({ns!r}) should return {expected}'
