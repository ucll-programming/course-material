import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("string, expected", [
    ("r0123456", True),
    ("R0123456", True),
    ("s0123456", True),
    ("S0123456", True),
    ("r9999999", True),
    ("q9999999", False),
    ("r123456", False),
    ("r12345678", False),
    ("rx123456", False),
    ("r0x23456", False),
    ("r01x3456", False),
    ("r012x456", False),
    ("r0123x56", False),
    ("r01234x6", False),
    ("r012345x", False),
])
def test_is_student_id(string, expected):
    actual = student.is_student_id(string)
    assert expected == actual, f'is_student_id({string!r}) should return {expected}'