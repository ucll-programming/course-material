import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("string, expected", [
    ("", True),
    ("a", True),
    ("aa", True),
    ("ab", False),
    ("abcba", True),
    ("abccba", True),
    ("abcdcba", True),
    ("abcb", False),
    ("xy", False),
    ("racecars", False),
])
def test_palindrome(string, expected):
    actual = student.palindrome(string)
    assert expected == actual
