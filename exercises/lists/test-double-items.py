import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("ns, expected", [
    (ns, [2 * n for n in ns])
    for ns in [
        [],
        [0],
        [1],
        [0, 1, 2, 3],
        [9, 4, 5, 8, 7, 6, 2, 1],
    ]
])
def test_double_items(ns, expected):
    actual_return_value = student.double_items(ns)

    assert actual_return_value is None
    assert ns == expected
