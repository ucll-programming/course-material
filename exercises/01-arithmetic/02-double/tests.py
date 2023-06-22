import pytest
from student import *


@pytest.mark.parametrize("argument, expected", [
    (0, 0),
    (1, 2),
    (2, 4),
    (1111, 2222),
])
def test_double(argument, expected):
    assert double(argument) == expected
