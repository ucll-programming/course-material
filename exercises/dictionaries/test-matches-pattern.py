import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("pattern, string, expected", [
    ('A', 'A', True),
    ('AB', 'AB', True),
    ('AB', 'BA', True),
    ('ABC', 'ABC', True),
    ('ABC', 'BAC', True),
    ('ABC', 'CBA', True),
    ('AA', 'XX', True),
    ('AA', 'XY', False),
    ('AB', 'XX', False),
    ('A', '', False),
    ('ABC', 'XYZW', False),
    ('', 'X', False),
    ('ABCD', 'ABCDE', False),
    ('ABCABC', 'TOKTOK', True),
    ('AAAAAA', 'TTTTTT', True),
    ('AAAAAA', 'TTTTXT', False),
    ('XXXYYY', 'AAACCC', True),
    ('XXXYYY', 'AAAAAA', False),
])
def test_matches_pattern(pattern, string, expected):
    actual = student.matches_pattern(pattern=pattern, string=string)
    assert expected == actual, f'{pattern} should {"" if expected else "not "} match {string}'
