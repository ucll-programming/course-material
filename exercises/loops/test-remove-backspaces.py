import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("string, expected", [
    ("", ""),
    ("a", "a"),
    ("\b", ""),
    ("a\b", ""),
    ("abc", "abc"),
    ("abc\b", "ab"),
    ("a\bb\bc\b", ""),
    ("aa\bb\bc\b", "a"),
    ("a\bb\bc\bc", "c"),
    ("aa\bb\bc\bc", "ac"),
    ("aa\bb\bc\bbc", "abc"),
    ("13\b2356\b\b45677\b8990\b\b0", "1234567890"),
])
def test_remove_backspaces(string, expected):
    actual = student.remove_backspaces(string)
    assert expected == actual
