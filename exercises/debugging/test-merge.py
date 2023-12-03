import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("xs, ys", [
    (xs, ys)
    for xs in [[], [1], [2], [1, 2], [5, 6], [1, 3, 5, 7, 9], [2, 4, 6, 8]]
    for ys in [[], [1], [2], [1, 2], [5, 6], [1, 3, 5, 7, 9], [2, 4, 6, 8]]
])
def test_merge(xs, ys):
    actual = student.merge(xs, ys)
    expected = sorted([*xs, *ys])
    assert expected == actual
