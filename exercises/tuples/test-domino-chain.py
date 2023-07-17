import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("dominos, expected", [
    (
        (),
        True
    ),
    (
        ((1, 2),),
        True
    ),
    (
        ((1, 2), (2, 3)),
        True
    ),
    (
        ((1, 2), (2, 3), (3, 4)),
        True
    ),
    (
        ((1, 2), (2, 3), (3, 4), (4, 2), (2, 6), (6, 0), (0, 3)),
        True
    ),
    (
        ((1, 2), (3, 1)),
        False
    ),
    (
        ((1, 2), (2, 1), (1, 5), (4, 5)),
        False
    ),
    (
        ((1, 2), (1, 2)),
        False
    ),
])
def test_domino_chain(dominos, expected):
    actual = student.domino_chain(dominos)
    assert expected == actual
