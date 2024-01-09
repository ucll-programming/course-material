import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("string, expected", [
    ("", None),
    ("a", "a"),
    ("abc", "c"),
    ("bcx", "x"),
    ("fjoifjoqfdpA", "A"),
])
def test_last_character(string, expected):
    actual = student.last_character(string)
    assert expected == actual
