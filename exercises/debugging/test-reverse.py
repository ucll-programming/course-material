import pytest
import itertools
import reverse


@pytest.mark.timeout(1)
@pytest.mark.parametrize("xs", [
    list(xs)
    for k in range(6)
    for xs in itertools.permutations(range(k))
])
def test_reverse(xs):
    actual = list(xs[:])
    reverse.reverse(actual)
    expected = list(reversed(xs))
    assert expected == actual, f"Reversing {xs!r} gave {actual!r} instead of {expected!r}"
