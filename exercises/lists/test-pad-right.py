import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("xs, length, padding", [
    ([], 0, 0),
    ([], 1, 0),
    ([], 5, 0),
    ([], 5, 'x'),
    ([1, 2], 5, 'x'),
    ([1, 2, 3, 4], 5, 0),
    ([1, 2, 3, 4, 5], 5, 'x'),
    ([1, 2, 3, 4, 5, 6], 5, 'x'),
])
def test_pad_right(xs, length, padding):
    original_xs = xs[:]
    actual_return_value = student.pad_right(xs, length, padding)

    assert actual_return_value is None
    assert len(xs) == max(length, len(original_xs))
    assert xs[:len(original_xs)] == original_xs
    assert all(x == padding for x in xs[len(original_xs):])
