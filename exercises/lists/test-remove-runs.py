import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("ns, expected", [
    ([], []),
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([1, 1], [1]),
    ([1, 2, 2], [1, 2]),
    ([1, 2, 2, 2], [1, 2]),
    ([1, 2, 2, 2, 3], [1, 2, 3]),
    ([1, 2, 2, 2, 3, 2], [1, 2, 3, 2]),
    ([1, 2, 2, 2, 3, 2, 2], [1, 2, 3, 2]),
    ([5, 2, 3, 4], [5, 2, 3, 4]),
    ([5, 2, 3, 4, 2], [5, 2, 3, 4, 2]),
    ([5, 2, 2, 3, 3, 4, 4, 2, 2, 5, 5, 5, 2, 2, 2, 2], [5, 2, 3, 4, 2, 5, 2]),
])
def test_remove_runs(ns, expected):
    copy = ns[:]
    actual = student.remove_runs(ns)

    assert ns == copy
    assert expected == actual
