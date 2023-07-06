import pytest
import student


@pytest.mark.parametrize("actual, guess, expected_judgement", [
    ("A", "A", "C"),
    ("A", "B", "X"),
    ("AA", "AA", "CC"),
    ("AB", "AB", "CC"),
    ("AB", "BA", "MM"),
    ("AB", "BX", "MX"),
    ("ABCDE", "ABCDE", "CCCCC"),
    ("ABCDE", "BCDEA", "MMMMM"),
    ("ABCDE", "BXDEA", "MXMMM"),
    ("AABCD", "ABCAA", "CMMMX"),
    ("AABCD", "BCDAA", "MMMMM"),
    ("ABABA", "BABAB", "MMMMX"),
])
def test_judge(actual, guess, expected_judgement):
    actual_judgement = student.judge(actual, guess)
    assert expected_judgement == actual_judgement
