import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("argument, expected", [
    (0, 0),
    (1, 3),
    (2, 6),
    (1111, 3333),
])
def test_triple(argument, expected):
    assert student.triple(argument) == expected
