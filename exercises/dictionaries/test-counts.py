import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize('xs, expected', [
    (
        [],
        {}
    ),
    (
        ['a'],
        {
            'a': 1,
        }
    ),
    (
        ['a', 'a'],
        {
            'a': 2,
        }
    ),
    (
        ['a', 'b'],
        {
            'a': 1,
            'b': 1,
        }
    ),
    (
        "a",
        {
            'a': 1,
        }
    ),
    (
        "aaa",
        {
            'a': 3,
        }
    ),
    (
        "abbccc",
        {
            'a': 1,
            'b': 2,
            'c': 3,
        }
    ),
    (
        "abcbcc",
        {
            'a': 1,
            'b': 2,
            'c': 3,
        }
    ),
])
def test_group_by_first_letter(xs, expected):
    actual = student.counts(xs)
    assert expected == actual
