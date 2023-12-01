import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("xs", [
    *(list(range(k)) for k in range(20)),
    [5, 1, 3, 7, 5, 3, 7, 5],
    [5, 1, 3, 7, 5, 3, 7, 5, 9],
    list('The Assassination of Jesse James by the Coward Robert Ford')
])
def test_reverse(xs):
    actual = list(xs[:])
    student.reverse(actual)
    expected = list(reversed(xs))
    assert expected == actual, f"Reversing {xs!r} gave {actual!r} instead of {expected!r}"
