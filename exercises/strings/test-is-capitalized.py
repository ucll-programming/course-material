import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("string, expected", [
    ("", False),
    ("A", True),
    ("Ab", True),
    ("Ab def", True),
    ("ab def", False),
    ("AbcdeF", False),
])
def test_is_capitalized(string, expected):
    actual = student.is_capitalized(string)
    assert expected == actual
