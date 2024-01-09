import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("string, expected", [
    (
        "a",
        "1a"
    ),
    (
        "aa",
        "2a"
    ),
    (
        "aaaaaaaaaa",
        "9a1a"
    ),
    (
        "bbbbbbbbbbbbbbbbbbbb",
        "9b9b2b"
    ),
    (
        "aaabbc",
        "3a2b1c",
    ),
    (
        "11111222233444455555",
        "5142234455"
    ),
    (
        "aaabbbaaabbbaaa",
        "3a3b3a3b3a"
    ),
    (
        "abc",
        "1a1b1c"
    )
])
def test_rle(string, expected):
    actual = student.rle(string)
    assert expected == actual, f"rle({string}) should return {expected!r} but got {actual!r} instead"
