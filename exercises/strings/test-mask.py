import pytest
import student
import re


@pytest.mark.timeout(1)
@pytest.mark.parametrize("password", [
    '',
    'x',
    'xy',
    'abc',
    '1234',
    'ababa',
    'xyzabc',
    'unguessable password',
])
def test_mask(password):
    actual = student.mask(password)

    assert len(password) == len(actual)
    assert all(char == '*' for char in actual)
