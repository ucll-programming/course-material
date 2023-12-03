import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("words, expected", [
    (
        "",
        ""
    ),
    (
        "a",
        "A"
    ),
    (
        "the great gatsby",
        "The Great Gatsby"
    ),
    (
        "the midnight coterie of SINISTER intruders",
        "The Midnight Coterie Of Sinister Intruders"
    )
])
def test_capitalize_words(words, expected):
    actual = student.capitalize_words(words)
    assert expected == actual, f"capitalize_words({words!r}) should return {expected!r} but got {actual!r} instead"
