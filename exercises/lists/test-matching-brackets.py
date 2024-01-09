import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("string, expected", [
    ('', True),
    ('()', True),
    ('{}', True),
    ('[]', True),
    ('[]', True),
    ('()[]', True),
    ('(){}[]', True),
    ('(())', True),
    ('([{}])', True),
    ('(([]){}){([][])}', True),
    ('(}', False),
    ('(', False),
    ('())', False),
    (')(', False),
    (')()', False),
    ('([)]', False),
    ('(([{}]{))', False),
    ('[]()}{', False),
])
def test_matching_brackets(string, expected):
    actual = student.matching_brackets(string)
    assert expected == actual
