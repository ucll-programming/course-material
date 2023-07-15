import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("string", [
    "x",
    "xy",
    "abc",
    "1234",
    "some longer title"
])
def test_underline(string):
    actual = student.underline(string)

    lines = actual.split("\n")
    assert len(lines) == 2
    assert lines[0] == string
    assert len(lines[1]) == len(string)
    assert all(char == '-' for char in lines[1])
